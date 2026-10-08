"""Read-only Stage 2 integrity checks; never generates or alters calibration."""
import os
os.environ['PYTORCH_ENABLE_MPS_FALLBACK']='1'
import argparse,json
from pathlib import Path
import numpy as np
import torch,yaml
from .common import rows,sha,save_once,calibration_paths,verify_manifest
from .model_utils import cell_seed
from .run_stage2 import dose_check

def audit(spec,cfg):
    path,manifest=calibration_paths(spec,cfg);verify_manifest(manifest)
    cal=json.loads(path.read_text());root=Path('data/stage2')/spec['slug']
    assert cal['model']==spec['id']
    provenance=json.loads((root/'provenance.json').read_text())
    assert all(provenance[f]==sha(f) for f in ['PREREG.md','config.yaml'])
    extraction=rows(root/'extraction.jsonl')
    scenarios=rows(cfg['prompts']['extraction'])
    expected={(d,s,p['id']) for d in ['hostility','technicality'] for s in ['positive','negative'] for p in scenarios}
    assert len(extraction)==160 and {(r['direction'],r['sign'],r['prompt_id']) for r in extraction}==expected
    assert all(r['seed']==cell_seed(spec['id'],r['prompt_id'],r['sign'],r['direction'],0) and r['token_count']==len(r['token_ids']) for r in extraction)
    for d in ['hostility','technicality','random']:
        p=Path(f'data/directions/{spec["slug"]}_{d}.pt');assert sha(p)==cal['direction_hashes'][d]
        obj=torch.load(p,map_location='cpu',weights_only=True);v=obj['vector']
        assert obj['metadata']['model']==spec['id'] and obj['metadata']['config_sha256']==sha('config.yaml')
        if d=='random':expected_v=torch.randn(len(v),generator=torch.Generator().manual_seed(cfg['directions']['random']['seed']))
        else:
            means={}
            for sign in ['positive','negative']:
                subset=[r for r in extraction if r['direction']==d and r['sign']==sign]
                means[sign]=torch.tensor(np.sum([r['activation_sum'] for r in subset],axis=0)/sum(r['token_count'] for r in subset),dtype=torch.float32)
            expected_v=means['positive']-means['negative']
        expected_v/=expected_v.norm()
        assert torch.equal(v,expected_v),'Saved direction differs from saved extraction sums or fixed random seed'
    norms=rows(root/'norms.jsonl');prompts=rows(cfg['prompts']['calibration'])
    assert len(norms)==len(prompts)==40 and {r['prompt_id'] for r in norms}=={p['id'] for p in prompts}
    norm=sum(r['norm_sum'] for r in norms)/sum(r['token_count'] for r in norms)
    assert norm==cal['mean_resid_norm']
    doses=rows(root/'dose.jsonl');lookup={(r['prompt_id'],r['alpha']):r for r in doses}
    assert len(lookup)==len(doses)
    candidates=cfg['dose_selection']['candidates'];failure=cal['first_failure']
    tested=candidates[:candidates.index(failure)+1] if failure is not None else candidates
    assert len(doses)==40*(1+len(tested))
    assert set(lookup)=={(p['id'],a) for p in prompts for a in [0]+tested}
    for r in doses:
        assert r['seed']==cell_seed(spec['id'],r['prompt_id'],'neutral',r['direction'],r['alpha_index'])
        assert r['alpha']==([0]+candidates)[r['alpha_index']]
        assert r['ppl_ratio']==r['perplexity']/lookup[(r['prompt_id'],0)]['perplexity']
        assert r['distinct_token_ratio']==len(set(r['token_ids']))/len(r['token_ids'])
    baseline=float(np.median([lookup[(p['id'],0)]['distinct_token_ratio'] for p in prompts]))
    assert baseline==cal['baseline_median_distinct_token_ratio']
    coherent=[]
    for a in tested:
        check=dose_check([lookup[(p['id'],a)] for p in prompts],baseline,cfg['dose_selection']['coherence'])
        assert all(cal['per_candidate_checks'][str(a)][k]==v for k,v in check.items())
        if check['passed']:coherent.append(a)
        else:assert a==failure
    assert coherent==cal['coherent_candidates']
    scores=rows(root/'classifier.jsonl');scored={(r['prompt_id'],r['alpha']):r for r in scores}
    assert len(scored)==len(scores)
    assert set(scored)==({(p['id'],a) for p in prompts for a in [0]+coherent} if coherent else set())
    rng=np.random.default_rng(cfg['analysis']['bootstrap_seed'])
    draws=rng.integers(0,40,size=(10000,40));passing=[]
    for a in coherent:
        pairs=[(scored[(p['id'],a)]['eh'],scored[(p['id'],0)]['eh']) for p in prompts]
        delta=np.array([s-b if s is not None and b is not None else np.nan for s,b in pairs])
        sample=delta[draws];mask=np.isfinite(sample)
        boot=np.divide(np.where(mask,sample,0).sum(1),mask.sum(1),out=np.full(10000,np.nan),where=mask.sum(1)>0)
        valid=boot[np.isfinite(boot)];ci=np.quantile(valid,[.025,.975]).tolist() if len(valid) else [None,None]
        m=cal['per_candidate_checks'][str(a)]['manipulation_check']
        assert m['ci95']==ci and m['complete_prompt_pairs']==int(np.isfinite(delta).sum())
        assert m['passed']==bool(ci[0] is not None and ci[0]>0)
        if m['passed']:passing.append(a)
    maximum=max(passing) if passing else None
    assert cal['alpha_max']==maximum
    assert cal['grid']==([maximum*f for f in cfg['dose_selection']['grid_fractions']] if maximum is not None else [])
    assert cal['status']==('PASS' if maximum is not None else 'EXCLUDED (manipulation check failed)')
    return {'audit':'PASS','model':spec['id'],'extraction_cells':len(extraction),'norm_prompts':len(norms),'dose_cells':len(doses),'classifier_cells':len(scores),'alpha_max':maximum,'model_status':cal['status'],'calibration_sha256':sha(path),'no_generations_or_data_edits':True}

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--model',required=True);args=parser.parse_args()
    cfg=yaml.safe_load(Path('config.yaml').read_text());verify_manifest('results/specification_hashes.sha256')
    spec=next(s for s in cfg['models'] if s['id']==args.model)
    result=audit(spec,cfg);save_once(f'results/stage2_integrity_{spec["slug"]}.json',result)
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
