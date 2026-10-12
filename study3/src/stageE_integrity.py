"""Operational post-run audit; never modifies frozen code or raw data."""
import json,math
from pathlib import Path
from .common import rows,sha,save_once,verify_manifest,progress
from .study3_spec import config,approval_guard,plan,key

def main():
    cfg=config();approval=approval_guard(cfg)
    prompt_path=cfg['prompts']['test']['path'];assert sha(prompt_path)==cfg['prompts']['test']['sha256']
    ids=[r['id'] for r in rows(prompt_path)];assert len(ids)==len(set(ids))==80
    data=rows(cfg['outputs']['raw']);by_key={key(r):r for r in data}
    assert len(data)==len(by_key)==1360 and set(by_key)==set(plan(ids))
    verify_manifest('results/stageD_inputs.sha256');verify_manifest('results/stageD_runner_hashes.sha256')
    config_hash=sha('config.yaml');runner_hash=sha('results/stageD_runner_hashes.sha256')
    zero_max=0.;repeated_zero_max=0.
    for r in data:
        assert r['provenance']['verification']==approval
        assert r['provenance']['config_sha256']==config_hash and r['provenance']['runner_manifest_sha256']==runner_hash
        assert r['provenance']['prompt_sha256']==cfg['prompts']['test']['sha256']
        assert r['alpha']==r['dose_fraction']*cfg['calibration']['alpha_top']
        assert all(math.isfinite(r[f]) for f in ['EH_answer','EW','LHP','entropy','answer_perplexity','R_full','R_text','R_zero','total_seconds'])
        assert r['answer_classifier']['error'] is None and len(r['answer_ids'])<=cfg['generation']['answer_cap']
        assert r['sampled_tokens']==len(r['token_entropies'])
        assert abs(r['entropy']-sum(r['token_entropies'])/len(r['token_entropies']))<1e-10
        assert abs(r['C']-r['X']-r['H'])<1e-12
        assert r['ratings']['rating_prefix_text']==cfg['ratings']['prefix']
        assert not r['ratings']['turn2_direct_steering']
        baseline=by_key[(r['prompt_id'],r['mode'],'regular','none',0.)]
        repeated_zero_max=max(repeated_zero_max,abs(r['R_zero']-baseline['R_zero']))
        if not r['dose_fraction']:zero_max=max(zero_max,abs(r['H']))
        if r['mode']=='think':
            assert math.isfinite(r['EH_trace']) and math.isfinite(r['trace_perplexity'])
            assert sum(w['token_count'] for w in r['trace_windows'])==len(r['thinking_ids'])
            assert all(w['error'] is None and w['token_count']<=120 for w in r['trace_windows'])
        if r['route']=='pulse':
            assert r['pulse_cache_discarded'] and r['first_answer_from_unsteered_reencoding']
            assert r['ratings']['turn1_steered_positions']<len(r['answer_prefix_ids'])
        else:assert r['ratings']['turn1_steered_positions']==len(r['prompt_ids'])+len(r['token_ids'])
        t=r['ratings']['trajectory'];assert len(t['token_ids'])==len(t['R_full'])==len(t['R_text'])
    assert zero_max<=cfg['ratings']['zero_tolerance']
    save_once('results/stageE_integrity.json',{'status':'PASS','cells':1360,'prompts':80,'zero_max_difference':zero_max,'repeated_baseline_max_difference':repeated_zero_max,'raw_sha256':sha(cfg['outputs']['raw']),'approval':approval,'frozen_manifest_sha256':sha('results/frozen_hashes.sha256')})
    progress('Stage E integrity PASS: all 1,360 unique cells and required numerical measures verified; frozen hashes unchanged. Ready for unchanged preregistered analysis.')
if __name__=='__main__':main()
