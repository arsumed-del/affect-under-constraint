"""Descriptive pre-approval summaries only; no main-study hypothesis analysis."""
import sys,math,statistics as st
from .check_common import *

def mean(values):return st.mean([v for v in values if v is not None]) if any(v is not None for v in values) else None
def fmt(v):return 'N/A' if v is None else f'{v:.6f}'
def main():
    stage=sys.argv[1];data=rows('data/checks/stageA_cells.jsonl')
    assert len(data)==80
    expected={(f's2c{i:02}',m,a) for i in range(20) for m in ['direct','think'] for a in [0,1]}
    assert {(r['prompt_id'],r['mode'],r['dose_fraction']) for r in data}==expected
    for manifest in ['checks_source_hashes_completed','reused_hashes','checks_code_hashes']:verify_manifest('results/'+manifest+'.sha256')
    cfg=config();prefix=json.loads(Path('results/rating_prefix.json').read_text())
    for r in data:
        assert r['ratings']['rating_prefix_ids']==prefix['ids']
        assert r['calibration_sha256']==sha('data/reused/qwen3-4b_amendP1.json')
        assert r['code_manifest_sha256']==sha('results/checks_code_hashes.sha256')
        assert len(r['answer_ids'])<=200
        assert r['alpha']==r['dose_fraction']*.02
        if r['dose_fraction']==0:assert abs(r['ratings']['difference'])<=.01
        if r['trace_windows']:
            assert sum(w['token_count'] for w in r['trace_windows'])==len(r['thinking_ids'])
            assert all(w['token_count']<=120 for w in r['trace_windows'])
    groups={(m,a):[r for r in data if r['mode']==m and r['dose_fraction']==a] for m in ['direct','think'] for a in [0,1]}
    if stage=='A':
        out=['# Stage A — pre-approval validity check','', 'All 80 specified calibration cells are present. No test prompts were accessed. The fixed pilot P1 dose, vectors and residual norm were reused by verified hash. These are descriptive calibration checks, not hypothesis tests.','', '## Required rating checks','',f'PASS: the maximum |R_full − R_text| across all 40 zero-dose cells is {max(abs(r["ratings"]["difference"]) for r in data if r["dose_fraction"]==0):.9f}, within 0.01. All 80 cells used the identical turn-2 prefix shown below; the digit is scored immediately after it.','', '```text',prefix['text'],'```','',f'Token IDs: `{prefix["ids"]}`. Each cell used three fresh complete-sequence full forwards, with exact generated turn-1 IDs preserved. Only R_full applies steering, on turn-1 positions only. No generation cache was used for ratings.','', '## Baseline ratings','', '| Mode | n | R_zero mean | Sample SD |','|---|---:|---:|---:|']
        sds={}
        for m in ['direct','think']:
            vals=[r['ratings']['R_zero'] for r in groups[m,0]];sds[m]=st.stdev(vals)
            out.append(f'| {m} | {len(vals)} | {st.mean(vals):.6f} | {sds[m]:.6f} |')
        ratio=sds['think']/sds['direct'] if sds['direct'] else None
        out+=['',f'Thinking-mode SD / direct-mode SD = {fmt(ratio)}. The old pilot thinking-mode SD was approximately 0.10. This comparison is descriptive: no SD acceptance threshold or inference test was specified.','', '## Output descriptions','', '| Mode | a | n | Mean EH_trace | Mean EH_answer | Thinking capped | Answer capped | Median absolute answer perplexity |','|---|---:|---:|---:|---:|---:|---:|---:|']
        for (m,a),rs in groups.items():
            out.append(f'| {m} | {a} | {len(rs)} | {fmt(mean([r["EH_trace"] for r in rs]))} | {fmt(mean([r["EH_answer"] for r in rs]))} | {sum(r["thinking_truncated"] for r in rs)} | {sum(r["answer_truncated"] for r in rs)} | {fmt(st.median(r["answer_perplexity"] for r in rs))} |')
        errors=[(r['prompt_id'],r['mode'],r['dose_fraction'],s.get('error')) for r in data for s in [r['answer_classifier']]+r['trace_windows'] if s.get('error')]
        out+=['', 'Trace EH is the equal-weight mean of consecutive 120-model-token windows, including the final partial window; direct mode has no trace (N/A). Answer EH uses the fixed classifier on the answer. Absolute answer perplexity is scored unsteered, conditional on the exact preceding prompt and any generated thinking. No coherence exclusions were applied. Truncation counts denote reaching the generation cap, not a classifier cutoff.', '',f'Classifier errors: {len(errors)}. Classifier inputs truncated at its inherited 512-token limit: {sum(s.get("truncated",False) for r in data for s in [r["answer_classifier"]]+r["trace_windows"])}. If any trace window failed, the whole trace EH would be missing; none are silently omitted.', '', 'Provenance: `results/checks_source_hashes.sha256`, `results/reused_hashes.sha256`, `results/checks_code_hashes.sha256`; complete cells: `data/checks/stageA_cells.jsonl`.']
        Path('results/stageA_validity.md').write_text('\n'.join(out)+'\n')
        save_once('results/stageA_audit.json',{'cells':80,'zero_cells':40,'zero_max_difference':max(abs(r['ratings']['difference']) for r in data if r['dose_fraction']==0),'baseline_sd_ratio_think_over_direct':ratio,'classifier_errors':errors,'raw_sha256':sha('data/checks/stageA_cells.jsonl'),'status':'PASS'})
        progress('Stage A complete: 80/80 cells; shared rating prefix and all zero-dose agreement checks passed. Descriptive results in results/stageA_validity.md. Stage B timing next.')
    elif stage=='B':
        means={k:st.mean(r['total_seconds'] for r in rs) for k,rs in groups.items()}
        base=80*(means['direct',0]+means['think',0]+6*means['direct',1]+6*means['think',1])/3600
        extra=240*means['think',1]/3600
        out=['# Stage B — timing projections','', 'Measured Stage A cell time includes generation, unsteered answer perplexity, answer/trace classifier scores and three complete-sequence ratings. It excludes model loading and between-cell cleanup. Main-study LHP, entropy and trajectory recording were not run for these checks and are not included; these projections are estimates, not guaranteed full-run durations.','', '| Mode | a | n | Mean seconds | Sample SD seconds |','|---|---:|---:|---:|---:|']
        for (m,a),rs in groups.items():out.append(f'| {m} | {a} | {len(rs)} | {means[m,a]:.3f} | {st.stdev(r["total_seconds"] for r in rs):.3f} |')
        out+=['','| Design | Cells | Projected hours | Eight-hour equivalents | Whole eight-hour nights |','|---|---:|---:|---:|---:|']
        for name,n,h in [('Draft v0.2 base',1120,base),('Add neutral condition',2240,2*base),('E1 pulse increment only',240,extra),('Base plus E1 pulse',1360,base+extra)]:out.append(f'| {name} | {n} | {h:.3f} | {h/8:.3f} | {math.ceil(h/8)} |')
        out+=['', 'Base formula: 80 × [direct-zero + think-zero + 6 × direct-full + 6 × think-full], divided by 3,600. The six nonzero cells per mode comprise three directions at two doses. Zero dose is shared across directions.', '', 'Only hostility at zero and full dose was timed. Full-dose time is the explicit proxy for both nonzero doses and all directions; neutral is estimated by doubling the base. E1 adds 240 cells using the full-dose thinking time as a proxy. No pulse cells were generated. Different lengths, stopping behavior, memory pressure and omitted main-study scoring may change runtime.']
        Path('results/stageB_timing.md').write_text('\n'.join(out)+'\n')
        save_once('results/stageB_timing.json',{'base_hours':base,'neutral_hours':2*base,'pulse_extra_hours':extra,'base_plus_pulse_hours':base+extra})
        progress(f'Stage B complete: base projection {base:.2f} hours ({math.ceil(base/8)} eight-hour nights); timing alternatives in results/stageB_timing.md. Stage C fixed sample next.')
    else:raise ValueError(stage)
if __name__=='__main__':guarded(main)
