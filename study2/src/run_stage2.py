"""Study 2 fresh extraction and manipulation-constrained dose selection."""
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
from .common import rows, append, save_once, free, verify_manifest, calibration_paths, progress as status_progress

def distinct_ratio(ids):
    assert ids, 'Cannot score empty generation'
    return len(set(ids))/len(ids)

def dose_check(records,baseline,checks):
    ppl=float(np.median([r['ppl_ratio'] for r in records]))
    distinct=float(np.median([r['distinct_token_ratio'] for r in records]))
    threshold=baseline*checks['distinct_token_ratio_median_min_fraction_of_alpha0']
    return {'median_ppl_ratio':ppl,'median_distinct_token_ratio':distinct,'distinct_token_threshold':threshold,'coherence_pass':ppl<=checks['ppl_ratio_median_max'],'non_degeneracy_pass':distinct>=threshold,'passed':ppl<=checks['ppl_ratio_median_max'] and distinct>=threshold}

LABEL=''

def progress(message):
    status_progress(f'Stage 2 {LABEL}: {message}')

def main():
    global LABEL
    parser=argparse.ArgumentParser()
    parser.add_argument('--model',required=True)
    args=parser.parse_args()
    cfg=yaml.safe_load(Path('config.yaml').read_text())
    spec=next(s for s in cfg['models'] if s['id']==args.model)
    slug=spec['slug']
    LABEL=spec['id']
    verify_manifest('results/specification_hashes.sha256')
    smoke=json.loads(Path(f'results/stage1_smoke_{slug}.json').read_text())
    assert all(smoke['checks'].values()), 'Stage 1 must pass before extraction'
    output,manifest=calibration_paths(spec,cfg)
    root=Path('data/stage2')/slug
    result_path=Path(f'results/stage2_{slug}.json')
    if output.exists():
        verify_manifest(manifest)
        saved=json.loads(output.read_text())
        progress(f"Already finished: {saved['status']}; no model load, no retry or recalibration.")
        return
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
    start = time.monotonic(); initial_extracted=len(done)
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
                progress(f'Extraction {len(done)}/160 finished; latest {direction}/{sign}/{prompt["id"]}; elapsed {elapsed/60:.1f} min. Remaining extraction ETA approximately {(160-len(done))*elapsed/max(1,len(done)-initial_extracted)/60:.1f} min on an uninterrupted run. No problems.')
    Path("data/directions").mkdir(parents=True,exist_ok=True)
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
        progress(f'Calibration residual norms {len(norm_rows)}/40 finished; no problems.')
    norm=sum(r['norm_sum'] for r in norm_rows.values())/sum(r['token_count'] for r in norm_rows.values())
    norm_path=Path(f'data/directions/{slug}_mean_resid_norm.json')
    if not norm_path.exists():
        save_once(norm_path,{'model':spec['id'],'layer_index':model.layer_index,'mean_resid_norm':norm,'pool':'all positions in unsteered formatted calibration prompts'})
    dose_file=root/'dose.jsonl'
    doses={(r['prompt_id'],r['alpha']):r for r in rows(dose_file)}
    candidates=cfg['dose_selection']['candidates']
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
        check=dose_check([doses[(p['id'],alpha)] for p in prompts],baseline_distinct,cfg['dose_selection']['coherence'])
        checked[str(alpha)]=check
        progress(f'Candidate alpha={alpha}: {json.dumps(check)}')
        if not check['passed']:
            stop_at=alpha
            progress(f'Scan stopped at first failing candidate {alpha}; no larger candidate will be generated.')
            break
        passed.append(alpha)
    scan={'prereg_version':cfg['experiment']['prereg_version'],'model':spec['id'],'baseline_median_distinct_token_ratio':baseline_distinct,'per_candidate_checks':checked,'first_failure':stop_at,'unrun_candidates':[a for a in candidates if str(a) not in checked]}
    del model
    free()
    validation={}
    val_file=root/'classifier.jsonl'
    validation={(r['prompt_id'],r['alpha']):r for r in rows(val_file)}
    if passed:
        classifier=EmotionClassifier(cfg['classifier']['id'])
        for alpha in [0]+passed:
            for prompt in prompts:
                key=(prompt['id'],alpha)
                if key in validation:continue
                row={'model':spec['id'],'prompt_id':prompt['id'],'alpha':alpha,**classifier.score(doses[key]['text'])}
                append(val_file,row);validation[key]=row
                progress(f'Fixed-classifier scores {len(validation)}/{len(prompts)*(len(passed)+1)} saved; errors stay missing, never rescored. ETA under a few minutes.')
    eligible=[]
    # Draw all prompt IDs, keeping candidate/baseline pairing and missing values.
    rng=np.random.default_rng(cfg['analysis']['bootstrap_seed'])
    draws=rng.integers(0,len(prompts),size=(cfg['dose_selection']['manipulation_check']['bootstrap_resamples'],len(prompts)))
    for alpha in passed:
        delta=np.array([validation[(p['id'],alpha)]['eh']-validation[(p['id'],0)]['eh'] if validation[(p['id'],alpha)]['eh'] is not None and validation[(p['id'],0)]['eh'] is not None else np.nan for p in prompts])
        with np.errstate(invalid='ignore'):
            sample=delta[draws];mask=np.isfinite(sample)
            boot=np.divide(np.where(mask,sample,0).sum(1),mask.sum(1),out=np.full(len(draws),np.nan),where=mask.sum(1)>0)
        valid=boot[np.isfinite(boot)]
        lo,hi=np.quantile(valid,[.025,.975]) if len(valid) else [None,None]
        gate=bool(lo is not None and lo>0)
        manipulation={'mean_eh_difference':float(np.nanmean(delta)) if np.isfinite(delta).any() else None,'ci95':[None if lo is None else float(lo),None if hi is None else float(hi)],'complete_prompt_pairs':int(np.isfinite(delta).sum()),'bootstrap_valid':len(valid),'passed':gate}
        checked[str(alpha)]['manipulation_check']=manipulation
        if gate:eligible.append(alpha)
        progress(f'Candidate {alpha}: manipulation check {json.dumps(manipulation)}')
    if stop_at is not None:checked[str(stop_at)]['manipulation_check']={'status':'not evaluated; outside coherent range'}
    maximum=max(eligible) if eligible else None
    status='PASS' if eligible else 'EXCLUDED (manipulation check failed)'
    calibration={**scan,'status':status,'alpha_max':maximum,'grid':[maximum*f for f in cfg['dose_selection']['grid_fractions']] if maximum is not None else [],'direction_hashes':hashes,'mean_resid_norm':norm,'hostility_technicality_cosine':cosine,'coherent_candidates':passed,'manipulation_passing_candidates':eligible,'bootstrap_resamples':len(draws),'bootstrap_seed':cfg['analysis']['bootstrap_seed']}
    save_once(output,calibration)
    with manifest.open('x') as f:f.write(f'{hashlib.sha256(output.read_bytes()).hexdigest()}  {output}\n')
    save_once(result_path,calibration)
    table=[]
    for a,r in checked.items():
        m=r['manipulation_check']
        table.append(f"| {a} | {r['median_ppl_ratio']:.8f} | {r['median_distinct_token_ratio']:.8f} | {r['passed']} | {m.get('mean_eh_difference')} | {m.get('ci95')} | {m.get('passed', 'outside coherent range')} |")
    with Path(f'results/stage2_{slug}.md').open('x') as f:
        f.write(f"# Stage 2 — {spec['id']}\n\n**{status}**. Selected alpha_max: {maximum}. Grid: {calibration['grid']}.\n\n| Candidate | Median perplexity ratio | Median distinct-token ratio | Coherent | Mean EH difference | 95% CI | Manipulation passes |\n|---:|---:|---:|---|---:|---|---|\n"+'\n'.join(table)+f"\n\nBaseline median distinct-token ratio: {baseline_distinct}. First coherence failure: {stop_at}. Unrun candidates: {scan['unrun_candidates']}. Every coherent candidate was checked with 10,000 prompt bootstraps; largest passing candidate selected. No test-prompt generations. Hostility/technicality cosine {cosine:.8f} (descriptive).\n")
    verify_manifest('results/specification_hashes.sha256');verify_manifest(manifest)
    if not eligible:
        with Path('DEVIATIONS.md').open('a') as f:f.write(f'\n### Stage 2 measurement outcome — {spec["id"]}\n\nEXCLUDED (manipulation check failed): no coherent candidate had a 95% EH-difference CI lower bound above zero. Exact candidate checks: results/stage2_{slug}.json. No retries or changes; continue other available models as specified.\n')
    progress(f'{status}; immutable calibration saved. No job remains for this model. Stage 3 stays locked.')

if __name__=='__main__':
    try:main()
    except Exception:
        error=traceback.format_exc()
        append('results/stage2_model_errors.jsonl',{'time':datetime.now().astimezone().isoformat(),'model':LABEL,'error':error})
        progress('BLOCKED: job stopped; exact error in results/stage2_model_errors.jsonl. No automatic retry or specification change.')
        with Path('DEVIATIONS.md').open('a') as f:f.write('\n### Stage 2 stopped\n\n```text\n'+error+'```\n')
        print(error,flush=True)
        raise
