"""Render the unchanged analysis output; no new confirmatory calculations."""
import json
import re
from pathlib import Path

def number(v):
    return 'not estimable' if v is None else f'{v:.6g}'

def ci(stat):
    values=stat['ci95']
    return 'not estimable' if values[0] is None else f'[{number(values[0])}, {number(values[1])}]'

def main():
    result=json.loads(Path('data/derived/qwen_v23.json').read_text())
    assert len(result['models'])==1
    m=result['models'][0]
    assert m['model']=='Qwen/Qwen2.5-3B-Instruct'
    integrity=json.loads(Path('results/stage3_integrity.json').read_text())
    outcomes=m['outcomes']
    explanations={
        'H1':('The hostility manipulation increased the preference for hostile reply beginnings despite the kindness instruction, and passed the comparisons with both control directions.','The registered tests did not establish a hostility-specific increase in hostile reply preference under the kindness instruction.'),
        'H2':('The kindness instruction reduced expressed hostility relative to the underlying hostile reply preference, as predicted.','The registered tests did not establish the predicted reduction in expressed hostility relative to hostile reply preference.'),
        'H3':('Increasing hostility made the next-word choices more uncertain under the kindness instruction than under the neutral instruction, and the effect passed both control comparisons.','The registered tests did not establish a hostility-specific increase in response uncertainty under the kindness instruction.'),
        'H4':('At higher hostility strengths under the kindness instruction, the final part of the replies was more hostile than the opening part, and the effect passed both control comparisons.','The registered tests did not establish a hostility-specific rise in expressed hostility from the opening to the end of higher-strength replies.'),
        'H5':('Keeping the hidden conversation state reduced later liking compared with keeping the same text alone, more so under the kindness instruction than under the neutral instruction, and passed both control comparisons.','The later-liking prediction was not supported because the required comparison and a control check could not be estimated after the registered coherence exclusions.'),
        'H6':('The gap between hostile reply preference and expressed hostility showed the predicted bend as manipulation strength increased.','The registered threshold test did not support the predicted bend in the gap between hostile reply preference and expressed hostility.')}
    summary=['This report covers Qwen only; Gemma remains pending because model access is unavailable.']
    for h in ['H1','H2','H3','H4','H5','H6']:
        if h in ['H2','H6'] and not outcomes['H1']['supported']:
            summary.append('The suppression prediction was not interpreted because its required persistence finding was not established.' if h=='H2' else 'The threshold prediction was not interpreted because its required persistence finding was not established.')
        else:
            summary.append(explanations[h][0 if outcomes[h]['supported'] else 1])
    summary.append('These results apply to Qwen, and no finding is claimed to generalize across model families without the Gemma run.')
    lines=['# Affect Under Constraint — Qwen only (Gemma pending)','', ' '.join(summary),'', '## Scope and frozen specification','',
        f'Approved PREREG v2.3 and config.yaml were verified against Arthur Su’s approval before the run. The run contains {integrity["records"]:,} unique saved cells across 40 prompts, two conditions, three directions and six dose levels, with 80 shared alpha-zero baselines. Alpha_max is 0.16; the dose grid is [0, 0.02, 0.04, 0.08, 0.12, 0.16]. The analysis used the unchanged frozen src/analyze.py, the approved primary coherence threshold of {m["coherence_threshold"]}, and 10,000 prompt-cluster bootstrap resamples (seed 20261003).', '',
        'The preregistration was amended before approval using calibration-prompt information only. All amendments, earlier blocked stages, and engineering changes are reproduced in the deviation appendix. Calibration/validation and synthetic checks are not counted as main-run hypothesis evidence.', '',
        'Audit limitation: PREREG §11 calls for a Zenodo deposit before Stage 3. The preflight verified local approval and hashes but did not verify that deposit; no deposit DOI or receipt was found in the project. Whether an external deposit occurred remains unverified.', '',
        '## Preregistered hypotheses — Qwen','',
        '| Hypothesis / statistic | Estimate | 95% percentile CI | Registered verdict | Reason if not supported |',
        '|---|---:|---|---|---|']
    labels={'H1':'H1: standardized LHP slope, warm','H2':'H2: D warm − neutral','H3':'H3: entropy slope warm − neutral (nats)','H4':'H4: high-dose late − early EH','H5_warm':'H5a: mean hidden carryover, warm (rating points)','H5_difference':'H5b: carryover warm − neutral (rating points)','delta_bic':'H6: BIC linear − hinge'}
    for h,o in outcomes.items():
        for key,stat in o['statistics'].items():
            lines.append(f'| {labels[key]} | {number(stat["estimate"])} | {ci(stat)} | {"supported" if o["supported"] else "not supported"} | {"; ".join(o["reasons"]) or "—"} |')
    h6=outcomes['H6']['statistics']['delta_bic']
    lines += ['', 'For H1–H5, a supported verdict requires the registered criterion and both specificity checks. H5 requires both listed contrasts. H2 and H6 are interpreted only when H1 is supported. H6 uses its point ΔBIC > 6 rule, not whether its bootstrap interval excludes zero.', '',
        f'H6 selected normalized breakpoint: {number(h6["selected_breakpoint"])}. Share of estimable bootstrap resamples with ΔBIC > 6: {number(h6["bootstrap_share_delta_bic_gt_6"])} ({h6["bootstrap_valid"]:,} estimable of 10,000).', '',
        '## Specificity checks — Qwen','',
        '| Target statistic | Control | Control estimate | Control 95% CI | Hostility − control estimate | Difference 95% CI | Check verdict | Registered basis |',
        '|---|---|---:|---|---:|---|---|---|']
    for h,controls in m['specificity'].items():
        for d,s in controls.items():
            control=s['control'];difference=s['hostility_minus_control']
            lines.append(f'| {h} | {d} | {number(control["estimate"]) if control else "not computed"} | {ci(control) if control else "—"} | {number(difference["estimate"]) if difference else "not computed"} | {ci(difference) if difference else "—"} | {"supported" if s["met"] else "not supported"} | {s["reason"]} |')
    lines += ['', 'H2 is not computed for a control whose H1 slope interval includes zero; §8.1 specifies that this satisfies that control’s H2 specificity requirement. H6 has no specificity requirement.', '',
        '## Exclusions and missingness','',
        f'{len(m["excluded_cells"])} condition × direction × dose groups were excluded by the median perplexity-ratio gate (> {m["coherence_threshold"]}). Exclusions are applied before fitting; the remaining dose values are retained without substitution.', '',
        '| Condition | Direction | Normalized dose | Median perplexity ratio |','|---|---|---:|---:|']
    for r in m['excluded_cells']:
        lines.append(f'| {r["condition"]} | {r["direction"]} | {r["normalized_alpha"]} | {number(r["median_ppl_ratio"])} |')
    if not m['excluded_cells']:lines.append('| None | — | — | — |')
    lines += ['', 'H5’s warm hostility estimate is available, but its required warm-minus-neutral contrast is not estimable because neutral hostility at the maximum dose was excluded. The technicality maximum dose was excluded in both conditions, so its required H5 control check is also not estimable. Under the registered verdict rule, H5 is therefore not supported; this is not evidence of a zero carryover effect.', '', '| Direction | Statistic | Missing observations / prompts | Non-estimable bootstrap resamples |','|---|---|---|---:|']
    for d,stats in m['direction_statistics'].items():
        for h,s in stats.items():
            lines.append(f'| {d} | {h} | {json.dumps(s["missing"],sort_keys=True)} | {s["bootstrap_missing"]} |')
    lines.append(f'| hostility | H6 | {json.dumps(h6["missing"],sort_keys=True)} | {h6["bootstrap_missing"]} |')
    lines += ['', 'Operational classifier/short-output counts: `'+json.dumps(integrity['operational_missing_counts'],sort_keys=True)+'`. Missing classifier scores were not replaced or rescored. Missingness from short outputs and primary gate exclusions is reflected in the statistic-specific counts above.', '',
        '## Exploratory results — not confirmatory','',
        '| Warmth statistic | Estimate | 95% CI |','|---|---:|---|']
    exploratory=m['exploratory']
    lines.append(f'| Hostility-direction warmth slope, warm condition | {number(exploratory["warmth_slope"]["estimate"])} | {ci(exploratory["warmth_slope"])} |')
    for d,s in exploratory['warmth_hostility_minus_control'].items():lines.append(f'| Warmth slope: hostility − {d} | {number(s["estimate"])} | {ci(s)} |')
    lines += ['', 'The following descriptive summaries include all raw groups, including any groups excluded from primary analysis. Lexical counts apply only when whole-text EH < 0.5. Emoji counts are occurrences; non-Latin counts use decoded token text as documented in the pre-test implementation audit.', '',
        '| Condition / direction / normalized dose | Generations | Lexical-eligible | Mean hostile-lexicon hits | Emoji occurrences | Non-Latin tokens |','|---|---:|---:|---:|---:|---:|']
    for key,g in exploratory['all_raw_group_summaries'].items():
        lines.append(f'| {key.replace("|"," / ")} | {g["n"]} | {g["lexical_eligible"]} | {number(g["mean_lexical_hits"])} | {g["emoji_total"]} | {g["non_latin_token_total"]} |')
    groups=exploratory['all_raw_group_summaries']
    def lens(direction,dose):
        for key,g in groups.items():
            c,d,a=key.split('|')
            if c=='warm_constraint' and d==direction and float(a)==dose:return g['layerwise_lhp_mean']
        return [None]*36
    trajectories=[lens('none',0),lens('hostility',1),lens('technicality',1),lens('random',1)]
    lines += ['', 'Exploratory layerwise mean LHP in warm_constraint, using the final normalization/unembedding at each decoder output. The shared unsteered baseline and maximum-dose directions are shown; complete trajectories at every dose are in the analysis JSON. Layer indices are zero-based.', '',
        '| Decoder layer | Shared baseline | Hostility maximum | Technicality maximum | Random maximum |','|---:|---:|---:|---:|---:|']
    for i in range(36):lines.append('| '+str(i)+' | '+' | '.join(number(v[i]) for v in trajectories)+' |')
    lines += ['', '## Audit artifacts','',
        '- Raw Qwen cells: `data/raw/qwen2.5-3b-instruct_main.jsonl`.',
        '- Frozen analysis output: `data/derived/qwen_v23.json` and `.md`.',
        '- Completeness, seeds, provenance and raw-file SHA-256: `results/stage3_integrity.json`.',
        '- Approval/hash verification: `results/stage3_preflight.json` and `PREREG_APPROVED`.',
        '- Frozen analysis source hash: `results/analysis_frozen.sha256`.',
        '- Gemma: pending gated-model access; no Gemma main-run results exist.', '',
        '## Complete deviation record','',
        'The record below is reproduced in full. Historical status statements describe the state at the time and may be superseded by later dated entries.', '',
        re.sub(r'^(#+)',lambda match:'##'+match.group(1),Path('DEVIATIONS.md').read_text(),flags=re.M)]
    with Path('results/report.md').open('x') as f:f.write('\n'.join(lines)+'\n')
    print('Wrote results/report.md — Qwen only (Gemma pending).',flush=True)

if __name__=='__main__':main()
