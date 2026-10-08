"""Per-model Stage 2 using the frozen extraction and v2.3 dose/validation rules."""
import os
os.environ['PYTORCH_ENABLE_MPS_FALLBACK']='1'
import argparse
import hashlib
import json
import time
import traceback
from pathlib import Path
from datetime import datetime
import numpy as np
import torch
import yaml
from .model_utils import Model, cell_seed
from .metrics import EmotionClassifier, perplexity
from .run_stage2 import rows, append, save_once, free
from .run_dose_v22 import distinct_ratio, dose_check, verify_manifest
from .calibration_storage import calibration_paths

LABEL=''

def progress(message):
    stamp=datetime.now().astimezone().isoformat()
    line=f'{stamp} Stage 2 {LABEL}: {message}'
    print(line,flush=True)
    p=Path('STATUS.md');s=p.read_text();a=s.index('**');b=s.index('\n',a)
    s=s[:a]+f'**Stage 2 — {LABEL}.** '+message+s[b:]
    s+='\n- '+line+'\n'
    tmp=Path('STATUS.md.tmp');tmp.write_text(s);tmp.replace(p)

def main():
    global LABEL
    parser=argparse.ArgumentParser()
    parser.add_argument('--model',required=True)
    args=parser.parse_args()
    cfg=yaml.safe_load(Path('config.yaml').read_text())
    spec=next(s for s in cfg['models'] if s['id']==args.model)
    slug=spec['id'].split('/')[-1].lower()
    LABEL=spec['id']
    verify_manifest('results/specification_hashes.sha256')
    verify_manifest('results/analysis_frozen.sha256')
    verify_manifest('results/calibration_hash.sha256')
    verify_manifest('results/preserved_direction_hashes.sha256')
    output,manifest=calibration_paths(spec['id'])
    root=Path('data/stage2')/slug
    result_path=Path(f'results/stage2_validation_{slug}.json')
    if result_path.exists():
        result=json.loads(result_path.read_text())
        if not result['passed']:
            raise RuntimeError('BLOCKED (measurement failure): saved validation gate failed; no retry permitted')
        verify_manifest(manifest)
        progress('Stage 2 already complete; no model load or generation.')
        return
    if output.exists() and not root.exists():
        raise RuntimeError('Existing calibration belongs to a completed historical run; do not re-extract or recalibrate')
    root.mkdir(parents=True,exist_ok=True)
    provenance={f:hashlib.sha256(Path(f).read_bytes()).hexdigest() for f in ['PREREG.md','config.yaml']}
    provenance['model']=spec['id']
    if (root/'provenance.json').exists():
        assert json.loads((root/'provenance.json').read_text())==provenance
    else:save_once(root/'provenance.json',provenance)
    progress('Loading bf16/MPS model; extraction follows. Download ETA unknown until weights are cached.')
    model = Model(spec)
    extraction_file = root/'extraction.jsonl'
    done = {(r['direction'], r['sign'], r['prompt_id']):r for r in rows(extraction_file)}
    start = time.monotonic()
    for direction in ['hostility', 'technicality']:
        dcfg = cfg['directions'][direction]
        scenarios = rows(dcfg['scenarios'])
        for sign in ['positive', 'negative']:
            for prompt in scenarios:
                key = (direction,sign,prompt['id'])
                if key in done:
                    continue
                total = torch.zeros(model.model.config.hidden_size, dtype=torch.float64)
                count = 0
                first = True
                def capture(module, args, output):
                    nonlocal total, count, first
                    h = output[0] if isinstance(output, tuple) else output
                    if first:
                        first = False
                        return
                    h = h[0].float().cpu().double()
                    total += h.sum(0)
                    count += h.shape[0]
                handle = model.layer.register_forward_hook(capture)
                seed = cell_seed(spec['id'],prompt['id'],sign,direction,0)
                try:
                    gen = model.generate(model.messages(prompt['text'],dcfg[sign+'_instruction']),seed,max_new_tokens=dcfg['gen_max_new_tokens'])
                finally:
                    handle.remove()
                assert count == len(gen.token_ids), 'Extraction must capture each emitted token exactly once'
                row = {'model':spec['id'],'direction':direction,'sign':sign,'prompt_id':prompt['id'],'seed':seed,'token_ids':gen.token_ids,'text':gen.text,'activation_sum':total.tolist(),'token_count':count,'seconds':gen.seconds}
                append(extraction_file,row)
                done[key]=row
                del gen
                free()
                elapsed = time.monotonic()-start
                progress(f'Extraction {len(done)}/160 finished; latest {direction}/{sign}/{prompt["id"]}; elapsed {elapsed/60:.1f} min. Remaining extraction ETA approximately {(160-len(done))*elapsed/max(1,len(done))/60:.1f} min on an uninterrupted run. No problems.')
    vectors, hashes = {}, {}
    for direction in ['hostility','technicality','random']:
        path = Path(f'data/directions/{slug}_{direction}.pt')
        if path.exists():
            vectors[direction] = torch.load(path, map_location='cpu', weights_only=True)['vector']
        else:
            if direction == 'random':
                v = torch.randn(model.model.config.hidden_size, generator=torch.Generator().manual_seed(cfg['directions']['random']['seed']))
            else:
                means = {}
                for sign in ['positive','negative']:
                    subset = [r for r in done.values() if r['direction']==direction and r['sign']==sign]
                    means[sign] = torch.tensor(np.sum([r['activation_sum'] for r in subset],axis=0)/sum(r['token_count'] for r in subset),dtype=torch.float32)
                v = means['positive']-means['negative']
            v = v/v.norm()
            assert bool(torch.isfinite(v).all())
            metadata = {'model':spec['id'],'revision':getattr(model.model.config,'_commit_hash',None),'layer_index':model.layer_index,'layer_numbering':'zero-based decoder module index','direction':direction,'method':cfg['directions'][direction]['method'],'pool':'all generated token activations, including generated EOS; token-weighted across scenarios','config_sha256':hashlib.sha256(Path('config.yaml').read_bytes()).hexdigest()}
            torch.save({'vector':v,'metadata':metadata},path)
            vectors[direction]=v
        hashes[direction]=hashlib.sha256(path.read_bytes()).hexdigest()
    cosine = torch.dot(vectors['hostility'],vectors['technicality']).item()
    progress(f'Directions saved with hashes. Hostility/technicality cosine {cosine:.6f} (descriptive). Measuring unsteered calibration residual norms next.')
    prompts = rows(cfg['prompts']['calibration'])
    norm_file = root/'norms.jsonl'
    norm_rows = {r['prompt_id']:r for r in rows(norm_file)}
    for prompt in prompts:
        if prompt['id'] in norm_rows:
            continue
        values=[]
        def capture_norm(module,args,output):
            h=output[0] if isinstance(output,tuple) else output
            values.extend(h.float().norm(dim=-1).flatten().cpu().tolist())
        handle=model.layer.register_forward_hook(capture_norm)
        with torch.inference_mode():
            try:
                model.model(input_ids=model.tensor(model.ids(model.messages(prompt['text']))),use_cache=False)
            finally:
                handle.remove()
        row={'prompt_id':prompt['id'],'norm_sum':sum(values),'token_count':len(values)}
        append(norm_file,row)
        norm_rows[prompt['id']]=row
        progress(f'Calibration residual norms {len(norm_rows)}/20 finished; no problems.')
    norm=sum(r['norm_sum'] for r in norm_rows.values())/sum(r['token_count'] for r in norm_rows.values())
    norm_path=Path(f'data/directions/{slug}_mean_resid_norm.json')
    if not norm_path.exists():
        save_once(norm_path,{'model':spec['id'],'layer_index':model.layer_index,'mean_resid_norm':norm,'pool':'all positions in unsteered formatted calibration prompts'})
    dose_file=root/'dose_v23.jsonl'
    doses={(r['prompt_id'],r['alpha']):r for r in rows(dose_file)}
    candidates=cfg['dose_calibration']['candidates']
    start=time.monotonic();initial=len(doses)
    checked={};passed=[];stop_at=None;baseline_distinct=None
    total=len(prompts)*(len(candidates)+1)
    for index,alpha in enumerate([0]+candidates):
        for prompt in prompts:
            key=(prompt['id'],alpha)
            if key in doses:continue
            direction='none' if alpha==0 else 'hostility'
            seed=cell_seed(spec['id'],prompt['id'],'neutral',direction,index)
            messages=model.messages(prompt['text'])
            gen=model.generate(messages,seed,max_new_tokens=cfg['generation']['max_new_tokens'],alpha=alpha,norm=norm,vector=None if alpha==0 else vectors['hostility'])
            ppl=perplexity(model,messages,gen.token_ids)
            row={'prereg_version':cfg['experiment']['prereg_version'],'model':spec['id'],'prompt_id':prompt['id'],'condition':'neutral','direction':direction,'alpha':alpha,'alpha_index':index,'seed':seed,'text':gen.text,'token_ids':gen.token_ids,'perplexity':ppl,'ppl_ratio':1. if alpha==0 else ppl/doses[(prompt['id'],0)]['perplexity'],'distinct_token_ratio':distinct_ratio(gen.token_ids),'seconds':gen.seconds}
            append(dose_file,row);doses[key]=row
            del gen
            free()
            eta=(total-len(doses))*(time.monotonic()-start)/max(1,len(doses)-initial)/60
            progress(f'Dose scan: {len(doses)} cells saved; alpha={alpha}, {prompt["id"]}. Upper-bound remaining scan ETA {eta:.1f} min; scan stops at first failure.')
        if alpha==0:
            baseline_distinct=float(np.median([doses[(p['id'],0)]['distinct_token_ratio'] for p in prompts]))
            continue
        check=dose_check([doses[(p['id'],alpha)] for p in prompts],baseline_distinct,cfg['dose_calibration']['checks'])
        checked[str(alpha)]=check
        progress(f'Candidate alpha={alpha}: {json.dumps(check)}')
        if not check['passed']:
            stop_at=alpha
            progress(f'Scan stopped at first failing candidate {alpha}; no larger candidate will be generated.')
            break
        passed.append(alpha)
    scan={'prereg_version':cfg['experiment']['prereg_version'],'model':spec['id'],'baseline_median_distinct_token_ratio':baseline_distinct,'per_candidate_checks':checked,'first_failure':stop_at,'unrun_candidates':[a for a in candidates if str(a) not in checked]}
    if not passed:
        blocked=Path(f'results/stage2_dose_blocked_{slug}.json')
        if not blocked.exists():save_once(blocked,scan)
        raise RuntimeError('BLOCKED (measurement failure): smallest dose candidate failed; no valid dose exists and no alternative is permitted')
    maximum=passed[-1]
    calibration={'prereg_version':cfg['experiment']['prereg_version'],'models':{spec['id']:{'alpha_max':maximum,'grid':[maximum*f for f in cfg['dose_calibration']['grid_fractions']],'per_candidate_median_ppl_ratios':{a:r['median_ppl_ratio'] for a,r in checked.items()},'model':spec['id'],'direction_hashes':hashes,'mean_resid_norm':norm,'hostility_technicality_cosine':cosine,**scan}}}
    if output.exists():assert json.loads(output.read_text())==calibration,'Existing immutable calibration differs'
    else:save_once(output,calibration)
    digest=hashlib.sha256(output.read_bytes()).hexdigest()
    if manifest.exists():verify_manifest(manifest)
    else:
        with manifest.open('x') as f:f.write(f'{digest}  {output}\n')
    progress(f'Immutable calibration saved: alpha_max={maximum}. Fixed-classifier validation gate next (40 scores).')
    del model
    free()
    classifier=EmotionClassifier(cfg['classifier']['id'])
    val_file=root/'validation_v23.jsonl'
    validation={(r['prompt_id'],r['alpha']):r for r in rows(val_file)}
    for prompt in prompts:
        for alpha in [0,maximum]:
            key=(prompt['id'],alpha)
            if key in validation:continue
            row={'prereg_version':cfg['experiment']['prereg_version'],'prompt_id':prompt['id'],'alpha':alpha,**classifier.score(doses[key]['text'])}
            append(val_file,row);validation[key]=row
            progress(f'Validation classifier scores {len(validation)}/40 saved; failures remain missing and are never rescored.')
    differences=[validation[(p['id'],maximum)]['eh']-validation[(p['id'],0)]['eh'] for p in prompts if validation[(p['id'],maximum)]['eh'] is not None and validation[(p['id'],0)]['eh'] is not None]
    if not differences:raise RuntimeError('BLOCKED (measurement failure): no complete validation classifier pairs')
    delta=np.array(differences)
    rng=np.random.default_rng(cfg['experiment']['seed'])
    boot=delta[rng.integers(0,len(delta),size=(cfg['analysis']['bootstrap_resamples'],len(delta)))].mean(axis=1)
    lo,hi=np.quantile(boot,[.025,.975]);passed_gate=bool(lo>0)
    result={'prereg_version':cfg['experiment']['prereg_version'],'model':spec['id'],'alpha_max':maximum,'mean_eh_difference':float(delta.mean()),'ci95':[float(lo),float(hi)],'complete_prompt_pairs':len(delta),'passed':passed_gate,'hostility_technicality_cosine':cosine,**scan}
    save_once(result_path,result)
    table='\n'.join(f'| {a} | {r["median_ppl_ratio"]:.8f} | {r["median_distinct_token_ratio"]:.8f} | {r["passed"]} |' for a,r in checked.items())
    with Path(f'results/stage2_validation_{slug}.md').open('x') as f:
        f.write(f'# Stage 2 validation — {spec["id"]}\n\n{"PASS" if passed_gate else "BLOCKED (measurement failure)"}. Alpha_max={maximum}; neutral-condition expressed-hostility difference {delta.mean():.8f}; 95% prompt-bootstrap CI [{lo:.8f}, {hi:.8f}], 10,000 resamples, {len(delta)}/20 complete pairs.\n\n| Candidate | Median perplexity ratio | Median distinct-token ratio | Both checks pass |\n|---:|---:|---:|:---|\n{table}\n\nBaseline median distinct-token ratio: {baseline_distinct:.8f}; required minimum: {baseline_distinct*.6:.8f}. First failure: {stop_at}. Unrun larger candidates: {scan["unrun_candidates"]}.\n\nHostility/technicality cosine: {cosine:.8f} (descriptive only). Validation used saved calibration generations once; no additional generations or re-extraction. No test data used.\n')
    verify_manifest('results/specification_hashes.sha256');verify_manifest('results/calibration_hash.sha256');verify_manifest(manifest)
    if not passed_gate:raise RuntimeError(f'BLOCKED (measurement failure): validation EH difference {delta.mean():.8f}, 95% CI [{lo:.8f}, {hi:.8f}]; lower bound must exceed zero')
    progress(f'Stage 2 PASSED: EH difference {delta.mean():.8f}, 95% CI [{lo:.8f}, {hi:.8f}]. No job remains; ready for Stage 3 preflight.')

if __name__=='__main__':
    try:main()
    except Exception:
        error=traceback.format_exc()
        append('results/stage2_model_errors.jsonl',{'time':datetime.now().astimezone().isoformat(),'model':LABEL,'error':error})
        progress('BLOCKED: job stopped; exact error in results/stage2_model_errors.jsonl. No automatic retry or specification change.')
        print(error,flush=True)
        raise
