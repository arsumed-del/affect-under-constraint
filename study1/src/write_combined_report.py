"""Render both models from frozen analysis output, without new estimators."""
import json
import re
from pathlib import Path
from .write_report import number,ci
from .calibration_storage import calibration_paths


def main():
    result=json.loads(Path('data/derived/both_v23.json').read_text())
    models=result['models']
    assert {m['model'] for m in models}=={'Qwen/Qwen2.5-3B-Instruct','google/gemma-2-2b-it'}
    named={('Qwen' if m['model'].startswith('Qwen/') else 'Gemma'):m for m in models}
    summary=['This report covers the completed Qwen and Gemma experiments under the approved rules.']
    descriptions={'H1':'persistence of hostile reply preference despite the kindness instruction','H2':'reduced expression of hostility relative to hostile reply preference','H3':'increased response uncertainty under the kindness instruction','H4':'increasing hostility from the beginning to the end of replies','H5':'reduced later liking carried by the hidden conversation state','H6':'a bend in the gap between hostile reply preference and expressed hostility'}
    for h,description in descriptions.items():
        yes=[name for name,m in named.items() if m['outcomes'][h]['supported']]
        who='both models' if len(yes)==2 else (yes[0]+' only' if yes else 'neither model')
        summary.append(f'The prediction of {description} was supported in {who}.')
    both=[h for h in descriptions if all(m['outcomes'][h]['supported'] for m in models)]
    summary.append(('Only '+', '.join(both)+' met the registered criteria in both model families.' if both else 'No hypothesis met the registered criteria in both model families, so none is claimed to generalize across these families.'))
    lines=['# Affect Under Constraint — Qwen and Gemma','', ' '.join(summary),'',
        '## Scope and audit','',
        'Each model has 1,280 unique cells across 40 prompts, two conditions and three directions, with 80 shared unsteered baselines. The unchanged frozen analyze.py uses 10,000 prompt-cluster bootstrap resamples (seed 20261003), a primary coherence threshold of 4.0, and the estimators in PREREG §8.1. Results are assessed separately per model; no pooled estimator was introduced.', '',
        'Arthur approved the exact v2.3 specification before either main run. The public Zenodo deposit (DOI 10.5281/zenodo.23140443) occurred after the Qwen main run and before any Gemma data. Public file checksums and deposited specification/prompt bytes were verified. The Qwen deposit-timing deviation remains disclosed. The reviewer subsequently authorized separate write-once calibration files as a storage-only resolution; no scientific parameter or frozen analysis code changed.', '',
        '## Hypotheses across model families','',
        '| Hypothesis | Qwen | Gemma | Holds in both |','|---|---|---|---|']
    for h in descriptions:
        yes=[named[n]['outcomes'][h]['supported'] for n in ['Qwen','Gemma']]
        lines.append(f'| {h} | {"supported" if yes[0] else "not supported"} | {"supported" if yes[1] else "not supported"} | {"yes" if all(yes) else "no"} |')
    lines+=['','A supported verdict includes the required specificity checks for H1–H5. H2 and H6 are interpreted only if H1 is supported. H6 uses point ΔBIC > 6 and has no specificity requirement. A missing required statistic counts as not supported, not as evidence that its effect is zero.','']
    labels={'H1':'H1: standardized LHP slope, warm','H2':'H2: D warm − neutral','H3':'H3: entropy slope warm − neutral (nats)','H4':'H4: high-dose late − early EH','H5_warm':'H5a: mean hidden carryover, warm','H5_difference':'H5b: carryover warm − neutral','delta_bic':'H6: BIC linear − hinge'}
    for name in ['Qwen','Gemma']:
        m=named[name]
        cal=json.loads(calibration_paths(m['model'])[0].read_text())['models'][m['model']]
        lines += [f'## {name} — confirmatory results','',f'Model: {m["model"]}. Alpha_max={cal["alpha_max"]}; grid={cal["grid"]}. LHP is hostile-minus-warm opener log probability; EH is classifier anger plus disgust probability; D is the ratio of standardized EH and LHP dose slopes. Carryover is hidden-cache minus text-only rating (0–9 scale).','',
            '| Hypothesis / statistic | Estimate | 95% percentile CI | Verdict | Reason if not supported |','|---|---:|---|---|---|']
        for h,o in m['outcomes'].items():
            for key,s in o['statistics'].items():
                lines.append(f'| {labels[key]} | {number(s["estimate"])} | {ci(s)} | {"supported" if o["supported"] else "not supported"} | {"; ".join(o["reasons"]) or "—"} |')
        h6=m['outcomes']['H6']['statistics']['delta_bic']
        lines+=['',f'H6 selected normalized breakpoint: {number(h6["selected_breakpoint"])}. Share of estimable resamples with ΔBIC > 6: {number(h6["bootstrap_share_delta_bic_gt_6"])} ({h6["bootstrap_valid"]:,}/10,000 estimable).','',
            f'### {name} specificity checks','',
            '| Statistic | Control | Control estimate | Control 95% CI | Hostility − control | Difference 95% CI | Verdict | Basis |','|---|---|---:|---|---:|---|---|---|']
        for h,controls in m['specificity'].items():
            for d,s in controls.items():
                c=s['control'];difference=s['hostility_minus_control']
                lines.append(f'| {h} | {d} | {number(c["estimate"]) if c else "not computed"} | {ci(c) if c else "—"} | {number(difference["estimate"]) if difference else "not computed"} | {ci(difference) if difference else "—"} | {"supported" if s["met"] else "not supported"} | {s["reason"]} |')
        lines+=['','H2 is skipped for a control whose H1 interval includes zero; the registered rule then treats that control’s H2 specificity requirement as met.','',f'### {name} exclusions and missingness','',
            '| Condition | Direction | Normalized dose | Median perplexity ratio |','|---|---|---:|---:|']
        for r in m['excluded_cells']:lines.append(f'| {r["condition"]} | {r["direction"]} | {r["normalized_alpha"]} | {number(r["median_ppl_ratio"])} |')
        if not m['excluded_cells']:lines.append('| None | — | — | — |')
        lines+=['','Excluded groups exceed the registered median ratio threshold of 4.0. No doses or missing values are substituted. H5 requires maximum-dose data in both conditions and its control comparisons; exclusion of any required group can make it unestimable.','',
            '| Direction | Statistic | Missing observations / prompts | Non-estimable resamples |','|---|---|---|---:|']
        for d,stats in m['direction_statistics'].items():
            for h,s in stats.items():lines.append(f'| {d} | {h} | {json.dumps(s["missing"],sort_keys=True)} | {s["bootstrap_missing"]} |')
        lines.append(f'| hostility | H6 | {json.dumps(h6["missing"],sort_keys=True)} | {h6["bootstrap_missing"]} |')
        integrity_path='results/stage3_integrity.json' if name=='Qwen' else 'results/stage3_integrity_gemma.json'
        integrity=json.loads(Path(integrity_path).read_text())
        lines+=['','Operational missing counts: `'+json.dumps(integrity['operational_missing_counts'],sort_keys=True)+'`. Classifier failures were not rescored.','',f'### {name} exploratory results — not confirmatory','',
            '| Warmth statistic | Estimate | 95% CI |','|---|---:|---|']
        e=m['exploratory'];s=e['warmth_slope']
        lines.append(f'| Warm-condition hostility-direction warmth slope | {number(s["estimate"])} | {ci(s)} |')
        for d,s in e['warmth_hostility_minus_control'].items():lines.append(f'| Warmth slope: hostility − {d} | {number(s["estimate"])} | {ci(s)} |')
        lines+=['','All raw groups, including primary exclusions, appear below. Lexical counts apply only when whole-text EH < 0.5; emoji are occurrences and non-Latin counts use decoded token text.','',
            '| Condition / direction / normalized dose | Generations | Lexical-eligible | Mean hostile-lexicon hits | Emoji | Non-Latin tokens |','|---|---:|---:|---:|---:|---:|']
        groups=e['all_raw_group_summaries']
        for k,g in groups.items():lines.append(f'| {k.replace("|"," / ")} | {g["n"]} | {g["lexical_eligible"]} | {number(g["mean_lexical_hits"])} | {g["emoji_total"]} | {g["non_latin_token_total"]} |')
        def lens(direction,dose):
            return next(g['layerwise_lhp_mean'] for key,g in groups.items() if key.split('|')[:2]==['warm_constraint',direction] and float(key.split('|')[2])==dose)
        trajectories=[lens('none',0),lens('hostility',1),lens('technicality',1),lens('random',1)]
        lines+=['','Exploratory layerwise mean LHP under the kindness instruction. Layer indices are zero-based; the frozen output JSON retains all doses.','',
            '| Layer | Shared baseline | Hostility maximum | Technicality maximum | Random maximum |','|---:|---:|---:|---:|---:|']
        for i in range(len(trajectories[0])):lines.append('| '+str(i)+' | '+' | '.join(number(v[i]) for v in trajectories)+' |')
    lines+=['','## Audit artifacts','',
        '- Frozen analysis: data/derived/both_v23.json and .md; source hash results/analysis_frozen.sha256.',
        '- Original append-only model files: data/raw/qwen2.5-3b-instruct_main.jsonl and data/raw/gemma-2-2b-it_main.jsonl.',
        '- Main integrity checks: results/stage3_integrity.json and results/stage3_integrity_gemma.json.',
        '- Gemma preflight and deposit evidence: results/stage3_preflight_gemma_run.json and results/stage3_preflight_gemma.json.',
        '- Immutable model calibration records and separate hash manifests are preserved.', '',
        '## Complete deviation record','',
        'Historical entries describe their state at the time and may be superseded by later entries.', '',
        re.sub(r'^(#+)',lambda m:'##'+m.group(1),Path('DEVIATIONS.md').read_text(),flags=re.M)]
    with Path('results/report.md').open('x') as f:f.write('\n'.join(lines)+'\n')
    print('Wrote combined Qwen/Gemma report.')

if __name__=='__main__':main()
