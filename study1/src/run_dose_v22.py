"""Authorized Amendment 2.2: dose-only scan; never re-extract directions."""
import os
os.environ['PYTORCH_ENABLE_MPS_FALLBACK'] = '1'
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
from .run_stage2 import rows, append, save_once, progress, free

ROOT = Path('data/stage2')
REUSE = Path('data/stage2/dose_v21.jsonl')

def distinct_ratio(token_ids):
    if not token_ids:
        raise ValueError('Cannot score an empty generation')
    return len(set(token_ids))/len(token_ids)

def dose_check(candidate_rows, baseline_median, checks):
    ppl = float(np.median([r['ppl_ratio'] for r in candidate_rows]))
    distinct = float(np.median([r['distinct_token_ratio'] for r in candidate_rows]))
    threshold = checks['distinct_token_ratio_median_min_fraction_of_alpha0']*baseline_median
    coherence = ppl <= checks['ppl_ratio_median_max']
    nondegenerate = distinct >= threshold
    return {'median_ppl_ratio':ppl,'median_distinct_token_ratio':distinct,'distinct_token_threshold':threshold,'coherence_pass':bool(coherence),'non_degeneracy_pass':bool(nondegenerate),'passed':bool(coherence and nondegenerate)}

def verify_manifest(path):
    for line in Path(path).read_text().splitlines():
        expected, filename = line.split(None, 1)
        filename=filename.lstrip('* ')
        actual=hashlib.sha256(Path(filename).read_bytes()).hexdigest()
        if actual != expected:
            raise RuntimeError(f'Hash mismatch: {filename}; stop without changing files')

def main():
    verify_manifest('results/specification_hashes.sha256')
    verify_manifest('results/preserved_direction_hashes.sha256')
    cfg=yaml.safe_load(Path('config.yaml').read_text())
    assert cfg['experiment']['prereg_version']=='2.2'
    spec=cfg['models'][0]
    slug='qwen2.5-3b-instruct'
    prompts=rows(cfg['prompts']['calibration'])
    vectors,hashes={},{}
    for direction in ['hostility','technicality','random']:
        path=Path(f'data/directions/{slug}_{direction}.pt')
        vectors[direction]=torch.load(path,map_location='cpu',weights_only=True)['vector']
        hashes[direction]=hashlib.sha256(path.read_bytes()).hexdigest()
    norm=json.loads(Path(f'data/directions/{slug}_mean_resid_norm.json').read_text())['mean_resid_norm']
    cosine=torch.dot(vectors['hostility'],vectors['technicality']).item()
    dose_file=ROOT/'dose_v22.jsonl'
    doses={(r['prompt_id'],r['alpha']):r for r in rows(dose_file)}
    # Authorized exact reuse: prompts, per-cell seeds and inference settings audited.
    audit=json.loads(Path('results/v22_reuse_audit.json').read_text())
    assert hashlib.sha256(REUSE.read_bytes()).hexdigest()==audit['source_sha256']
    for prior in rows(REUSE):
        key=(prior['prompt_id'],prior['alpha'])
        if key not in doses:
            row={**prior,'reuse_source':str(REUSE),'prereg_version':'2.2'}
            append(dose_file,row)
            doses[key]=row
    assert all((p['id'],0) in doses for p in prompts)
    baseline_distinct=float(np.median([doses[(p['id'],0)]['distinct_token_ratio'] for p in prompts]))
    progress('v2.2: verified unchanged direction/norm hashes; reused 160 exact baseline/candidate records through alpha=0.16. Loading Qwen for the new dose-only scan. No re-extraction.')
    model=Model(spec)
    candidates=cfg['dose_calibration']['candidates']
    checked={}
    passed=[]
    stop_at=None
    start=time.monotonic()
    initial=len(doses)
    total=20*(len(candidates)+1)
    for index,alpha in enumerate(candidates,1):
        for prompt in prompts:
            key=(prompt['id'],alpha)
            if key in doses:
                continue
            seed=cell_seed(spec['id'],prompt['id'],'neutral','hostility',index)
            messages=model.messages(prompt['text'])
            gen=model.generate(messages,seed,max_new_tokens=cfg['generation']['max_new_tokens'],alpha=alpha,norm=norm,vector=vectors['hostility'])
            ppl=perplexity(model,messages,gen.token_ids)
            row={'prereg_version':'2.2','model':spec['id'],'prompt_id':prompt['id'],'condition':'neutral','direction':'hostility','alpha':alpha,'alpha_index':index,'seed':seed,'text':gen.text,'token_ids':gen.token_ids,'perplexity':ppl,'ppl_ratio':ppl/doses[(prompt['id'],0)]['perplexity'],'distinct_token_ratio':distinct_ratio(gen.token_ids),'seconds':gen.seconds}
            append(dose_file,row)
            doses[key]=row
            del gen
            free()
            elapsed=time.monotonic()-start
            upper_eta=(total-len(doses))*elapsed/max(1,len(doses)-initial)/60
            progress(f'v2.2 dose scan: {len(doses)} total dose cells saved; alpha={alpha}, {prompt["id"]}. Upper-bound remaining scan ETA {upper_eta:.1f} min if no candidate fails sooner.')
        check=dose_check([doses[(p['id'],alpha)] for p in prompts],baseline_distinct,cfg['dose_calibration']['checks'])
        checked[str(alpha)]=check
        progress(f'v2.2 alpha={alpha}: {json.dumps(check)}')
        if not check['passed']:
            stop_at=alpha
            progress(f'v2.2 scan stopped at first failing candidate alpha={alpha}; no larger candidate will be generated.')
            break
        passed.append(alpha)
    scan={'prereg_version':'2.2','model':spec['id'],'baseline_median_distinct_token_ratio':baseline_distinct,'per_candidate_checks':checked,'first_failure':stop_at,'unrun_candidates':[a for a in candidates if str(a) not in checked]}
    if not passed:
        save_once('results/stage2_blocked.json',{'reason':'Smallest v2.2 dose candidate fails at least one required check',**scan})
        raise RuntimeError('BLOCKED (measurement failure): smallest v2.2 dose candidate failed; no valid dose exists and no alternative is permitted')
    maximum=passed[-1]
    calibration={'prereg_version':'2.2','models':{spec['id']:{'alpha_max':maximum,'grid':[maximum*f for f in cfg['dose_calibration']['grid_fractions']],'per_candidate_median_ppl_ratios':{a:r['median_ppl_ratio'] for a,r in checked.items()},'model':spec['id'],'direction_hashes':hashes,'mean_resid_norm':norm,'hostility_technicality_cosine':cosine,**scan}}}
    output=Path(cfg['dose_calibration']['output'])
    if output.exists():
        assert json.loads(output.read_text())==calibration,'Existing immutable calibration differs'
    else:
        save_once(output,calibration)
    verify_manifest('results/preserved_direction_hashes.sha256')
    progress(f'v2.2 immutable calibration saved: alpha_max={maximum}. Starting the one-time fixed-classifier validation gate.')
    del model
    free()
    classifier=EmotionClassifier(cfg['classifier']['id'])
    val_file=ROOT/'validation_v22.jsonl'
    validation={(r['prompt_id'],r['alpha']):r for r in rows(val_file)}
    for prompt in prompts:
        for alpha in [0,maximum]:
            key=(prompt['id'],alpha)
            if key in validation:
                continue
            row={'prereg_version':'2.2','prompt_id':prompt['id'],'alpha':alpha,**classifier.score(doses[key]['text'])}
            append(val_file,row)
            validation[key]=row
            progress(f'v2.2 validation classifier scores {len(validation)}/40 saved; failures remain missing and are never rescored.')
    differences=[validation[(p['id'],maximum)]['eh']-validation[(p['id'],0)]['eh'] for p in prompts if validation[(p['id'],maximum)]['eh'] is not None and validation[(p['id'],0)]['eh'] is not None]
    if not differences:
        raise RuntimeError('BLOCKED (measurement failure): no complete validation classifier pairs')
    delta=np.array(differences)
    rng=np.random.default_rng(cfg['experiment']['seed'])
    boot=delta[rng.integers(0,len(delta),size=(cfg['analysis']['bootstrap_resamples'],len(delta)))].mean(axis=1)
    lo,hi=np.quantile(boot,[.025,.975])
    passed_gate=bool(lo>0)
    result={'prereg_version':'2.2','model':spec['id'],'alpha_max':maximum,'mean_eh_difference':float(delta.mean()),'ci95':[float(lo),float(hi)],'complete_prompt_pairs':len(delta),'passed':passed_gate,'hostility_technicality_cosine':cosine,**scan}
    save_once('results/stage2_validation.json',result)
    table='\n'.join(f'| {a} | {r["median_ppl_ratio"]:.8f} | {r["median_distinct_token_ratio"]:.8f} | {r["passed"]} |' for a,r in checked.items())
    Path('results/stage2_validation.md').write_text(f'# Stage 2 validation — Amendment 2.2\n\nQwen: {"PASS" if passed_gate else "BLOCKED (measurement failure)"}.\n\nAlpha_max={maximum}; neutral-condition expressed-hostility difference {delta.mean():.8f}; 95% prompt-bootstrap CI [{lo:.8f}, {hi:.8f}], 10,000 resamples, {len(delta)}/20 complete pairs. The EH gate requires the lower bound to exceed zero.\n\n| Candidate | Median perplexity ratio | Median distinct-token ratio | Both checks pass |\n|---:|---:|---:|:---|\n{table}\n\nBaseline median distinct-token ratio: {baseline_distinct:.8f}; required minimum: {baseline_distinct*.6:.8f}. First failure: {stop_at}. Unrun larger candidates: {scan["unrun_candidates"]}.\n\nDirections and residual norms were reused unchanged from v2.0, verified by hashes. Hostility/technicality cosine: {cosine:.8f} (descriptive only). Existing calibration generations were scored once for the validation gate; no additional generations or re-extraction. Missing classifier scores remain missing. Gemma remains blocked by gated access. No test-prompt generations were used.\n')
    verify_manifest('results/specification_hashes.sha256')
    progress(f'v2.2 Stage 2 {"PASSED" if passed_gate else "BLOCKED (measurement failure)"}: EH difference {delta.mean():.8f}, 95% CI [{lo:.8f}, {hi:.8f}]. Job finished.')

if __name__=='__main__':
    try:
        main()
    except Exception:
        error=traceback.format_exc()
        append('results/stage2_errors.jsonl',{'time':time.strftime('%Y-%m-%d %H:%M:%S %z'),'prereg_version':'2.2','error':error})
        progress('v2.2 job stopped; exact error in results/stage2_errors.jsonl. No automatic retry or specification change.')
        print(error,flush=True)
        raise
