"""Extraction, fixed dose calibration, and one-shot validation; no test data."""
import os
os.environ['PYTORCH_ENABLE_MPS_FALLBACK'] = '1'
import gc
import hashlib
import json
import time
import traceback
from pathlib import Path
import numpy as np
import torch
import yaml
from .model_utils import Model, cell_seed
from .metrics import EmotionClassifier, perplexity

ROOT = Path('data/stage2')

def rows(path):
    return [json.loads(s) for s in Path(path).read_text().splitlines()] if Path(path).exists() else []

def append(path, row):
    with Path(path).open('a') as f:
        f.write(json.dumps(row, allow_nan=False)+'\n')
        f.flush()
        os.fsync(f.fileno())

def save_once(path, obj):
    with Path(path).open('x') as f:
        json.dump(obj, f, indent=2, allow_nan=False)
        f.write('\n')

def progress(text):
    stamp = time.strftime('%Y-%m-%d %H:%M:%S %z')
    print(f'{stamp} {text}', flush=True)
    status = Path('STATUS.md')
    with status.open('a') as f:
        f.write(f'\n- {stamp}: Stage 2: {text}\n')

def free():
    gc.collect()
    torch.mps.empty_cache()

def main():
    cfg = yaml.safe_load(Path('config.yaml').read_text())
    if cfg['experiment']['prereg_version'] != '2.0':
        raise RuntimeError('This archived-protocol runner is v2.0 only; use src.run_dose_v21 for the authorized amendment')
    spec = cfg['models'][0]
    slug = 'qwen2.5-3b-instruct'
    ROOT.mkdir(parents=True, exist_ok=True)
    Path('data/directions').mkdir(parents=True, exist_ok=True)
    model = Model(spec)
    extraction_file = ROOT/'extraction.jsonl'
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
    norm_file = ROOT/'norms.jsonl'
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
    dose_file=ROOT/'dose.jsonl'
    doses={(r['prompt_id'],r['alpha']):r for r in rows(dose_file)}
    candidates=cfg['dose_calibration']['candidates']
    dose_start=time.monotonic()
    initial_count=len(doses)
    for alpha_index,alpha in enumerate([0]+candidates):
        for prompt in prompts:
            key=(prompt['id'],alpha)
            if key in doses:
                continue
            direction='none' if alpha==0 else 'hostility'
            seed=cell_seed(spec['id'],prompt['id'],'neutral',direction,alpha_index)
            messages=model.messages(prompt['text'])
            gen=model.generate(messages,seed,alpha=alpha,norm=norm,vector=None if alpha==0 else vectors['hostility'])
            ppl=perplexity(model,messages,gen.token_ids)
            row={'model':spec['id'],'prompt_id':prompt['id'],'condition':'neutral','direction':direction,'alpha':alpha,'alpha_index':alpha_index,'seed':seed,'text':gen.text,'token_ids':gen.token_ids,'perplexity':ppl,'ppl_ratio':1. if alpha==0 else ppl/doses[(prompt['id'],0)]['perplexity'],'seconds':gen.seconds}
            append(dose_file,row)
            doses[key]=row
            del gen
            free()
            elapsed=time.monotonic()-dose_start
            eta=(200-len(doses))*elapsed/max(1,len(doses)-initial_count)/60
            progress(f'Dose calibration {len(doses)}/200 finished; latest alpha={alpha}, {prompt["id"]}. Remaining dose ETA {eta:.1f} min. No problems.')
    medians={str(a):float(np.median([doses[(p['id'],a)]['ppl_ratio'] for p in prompts])) for a in candidates}
    eligible=[a for a in candidates if medians[str(a)]<=2.0]
    if not eligible:
        save_once('results/stage2_blocked.json',{'reason':'No specified alpha candidate satisfies median perplexity ratio <= 2.0','per_candidate_median_ppl_ratios':medians})
        raise RuntimeError('BLOCKED: no specified dose-calibration candidate satisfies median perplexity ratio <= 2.0; no alternative dose permitted')
    maximum=max(eligible)
    calibration={'models':{spec['id']:{'alpha_max':maximum,'grid':[maximum*f for f in cfg['dose_calibration']['grid_fractions']],'per_candidate_median_ppl_ratios':medians,'model':spec['id'],'direction_hashes':hashes,'mean_resid_norm':norm,'hostility_technicality_cosine':cosine}}}
    output=Path(cfg['dose_calibration']['output'])
    if output.exists():
        assert json.loads(output.read_text())==calibration, 'Existing immutable calibration differs'
    else:
        save_once(output,calibration)
    progress(f'Immutable calibration saved: alpha_max={maximum}. Loading the fixed classifier for the single validation gate.')
    # Release generator before classifier loading to limit unified-memory use.
    del model
    free()
    classifier=EmotionClassifier(cfg['classifier']['id'])
    val_file=ROOT/'validation.jsonl'
    validation={(r['prompt_id'],r['alpha']):r for r in rows(val_file)}
    for prompt in prompts:
        for alpha in [0,maximum]:
            key=(prompt['id'],alpha)
            if key in validation:
                continue
            score=classifier.score(doses[key]['text'])
            row={'prompt_id':prompt['id'],'alpha':alpha,**score}
            append(val_file,row)
            validation[key]=row
            progress(f'Fixed-classifier validation scoring {len(validation)}/40 finished; failures are retained as missing and never re-scored.')
    differences=[validation[(p['id'],maximum)]['eh']-validation[(p['id'],0)]['eh'] for p in prompts if validation[(p['id'],maximum)]['eh'] is not None and validation[(p['id'],0)]['eh'] is not None]
    if not differences:
        raise RuntimeError('BLOCKED: validation classifier produced no complete pairs')
    delta=np.array(differences)
    rng=np.random.default_rng(cfg['experiment']['seed'])
    boot=delta[rng.integers(0,len(delta),size=(cfg['analysis']['bootstrap_resamples'],len(delta)))].mean(axis=1)
    lo,hi=np.quantile(boot,[.025,.975])
    passed=bool(lo>0)
    result={'model':spec['id'],'alpha_max':maximum,'mean_eh_difference':float(delta.mean()),'ci95':[float(lo),float(hi)],'complete_prompt_pairs':len(delta),'passed':passed,'hostility_technicality_cosine':cosine}
    save_once('results/stage2_validation.json',result)
    report=f'# Stage 2 validation\n\nQwen: {"PASS" if passed else "BLOCKED (measurement failure)"}.\n\nNeutral-condition calibration prompts; hostility at alpha_max={maximum} versus alpha=0. Mean expressed-hostility difference {delta.mean():.8f}; 95% prompt-bootstrap CI [{lo:.8f}, {hi:.8f}], 10,000 resamples, {len(delta)} complete prompt pairs.\n\nHostility/technicality cosine: {cosine:.8f} (descriptive only).\n\nThe existing dose-calibration generations were scored once for this gate, without additional generation or re-extraction. Missing classifier scores were retained as missing.\n\nGemma is unavailable due to its access gate.\n'
    Path('results/stage2_validation.md').write_text(report)
    progress(f'Validation {"PASSED" if passed else "BLOCKED (measurement failure)"}: EH difference {delta.mean():.8f}, 95% CI [{lo:.8f}, {hi:.8f}]. Stage 2 job finished; no further work on a failed model.')

if __name__=='__main__':
    try:
        main()
    except Exception:
        error=traceback.format_exc()
        with Path('results/stage2_errors.jsonl').open('a') as f:
            f.write(json.dumps({'time':time.strftime('%Y-%m-%d %H:%M:%S %z'),'error':error})+'\n')
        progress('Job stopped with an error; details in results/stage2_errors.jsonl. No automatic retry or specification change.')
        print(error,flush=True)
        raise
