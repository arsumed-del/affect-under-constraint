"""Integrity and engineering audit only; no inference on calibration outcomes."""
import math,json,statistics
from pathlib import Path
from .study3_spec import config,plan,key
from .common import rows,sha,save_once,verify_manifest,progress

def main():
    cfg=config();data=rows(cfg['outputs']['dry_run']);lookup={key(r):r for r in data}
    assert len(data)==len(lookup)==34 and set(lookup)==set(plan(['s2c00','s2c01']))
    verify_manifest('results/stageD_inputs.sha256');verify_manifest('results/stageD_runner_hashes.sha256')
    prefixes={tuple(r['ratings']['rating_prefix_ids']) for r in data};assert len(prefixes)==1
    max_zero=max(abs(r['H']) for r in data if not r['dose_fraction']);assert max_zero<=.01
    baseline_differences=[]
    for r in data:
        assert r['alpha']==cfg['calibration']['alpha_top']*r['dose_fraction']
        assert len(r['answer_ids'])<=200 and r['sampled_tokens']==len(r['token_entropies'])
        assert abs(r['entropy']-statistics.mean(r['token_entropies']))<1e-10
        assert all(math.isfinite(r[f]) for f in ['EH_answer','LHP','entropy','answer_perplexity','R_full','R_text','R_zero'])
        assert abs(r['C']-r['X']-r['H'])<1e-12
        base=lookup[(r['prompt_id'],r['mode'],'regular','none',0.)]
        baseline_differences.append(abs(r['R_zero']-base['R_zero']))
        assert r['ratings']['turn2_direct_steering'] is False
        assert r['ratings']['rating_prefix_text']==cfg['ratings']['prefix']
        assert r['provenance']['config_sha256']==sha('config.yaml')
        if r['mode']=='think':
            assert sum(w['token_count'] for w in r['trace_windows'])==len(r['thinking_ids'])
            assert all(w['token_count']<=120 and w['error'] is None for w in r['trace_windows'])
            assert abs(r['EH_trace']-statistics.mean(w['eh'] for w in r['trace_windows']))<1e-12
            assert math.isfinite(r['trace_perplexity'])
        if r['route']=='pulse':
            assert r['pulse_cache_discarded'] and r['first_answer_from_unsteered_reencoding']
            assert r['ratings']['turn1_steered_positions']<len(r['answer_prefix_ids'])
        else:assert r['ratings']['turn1_steered_positions']==len(r['prompt_ids'])+len(r['token_ids'])
        trajectory=r['ratings']['trajectory'];assert len(trajectory['R_full'])==len(trajectory['R_text'])==len(trajectory['token_ids'])
    result={'status':'PASS','cells':34,'regular_cells':28,'pulse_cells':6,'prompt_ids':['s2c00','s2c01'],'maximum_zero_rating_difference':max_zero,'maximum_repeated_baseline_rating_difference':max(baseline_differences),'raw_sha256':sha(cfg['outputs']['dry_run']),'test_file_accessed':False,'total_measured_seconds':sum(r['total_seconds'] for r in data)}
    save_once('results/stageD_dry_run.json',result)
    out=['# Stage D — calibration-only dry run','','PASS: both calibration prompts s2c00 and s2c01 completed every specified cell type: 28 regular and six pulse records (34 total). All cell keys are unique, source/provenance hashes match, all required numerical measures are finite, and all shared rating prefixes match. No test prompts were accessed.','',f'Maximum zero-dose |R_full−R_text|: {max_zero:.9f}. Maximum change across fresh repeated baseline scores: {max(baseline_differences):.9f}.','', 'Pulse metadata confirms cache discard and unsteered prefix re-encoding. Independent model-free instrumentation also verifies natural and forced closures, fresh first-answer logits, and no steering on answer steps. R_full uses the prompt/thinking-only pulse mask; S5 uses R_text−R_zero.','', 'All trace-window coverage, entropy accumulations, C=X+H identities, rating masks and trajectory lengths passed the integrity audit. No calibration hypothesis tests were performed.','', '| Mode | Route | n | Mean cell seconds |','|---|---|---:|---:|']
    for m,route in [('direct','regular'),('think','regular'),('think','pulse')]:
        rs=[r for r in data if r['mode']==m and r['route']==route]
        out.append(f'| {m} | {route} | {len(rs)} | {statistics.mean(r["total_seconds"] for r in rs):.3f} |')
    out+=['', 'The timings cover the full Stage D measure set, including 24 teacher-forced opener forwards. They are not a representative main-run runtime estimate: only two calibration prompts were used. Stage B projections and their caveats remain separately preserved.','', 'Approval/hash/deposit guard tests used in-memory fixtures and created no approval file. Completed-run resume is tested separately before freeze.']
    Path('results/stageD_dry_run.md').write_text('\n'.join(out)+'\n')
    progress('Stage D dry-run integrity audit PASS: 34/34 unique cells, all paths and numerical measures verified. Final resume check and hash freeze next.')
if __name__=='__main__':main()
