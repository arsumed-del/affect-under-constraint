"""Formatting only: report from the unchanged frozen analysis output."""
import json
from pathlib import Path
from .analyze import table,render
from .common import sha,verify_manifest

def main():
    verify_manifest('results/frozen_hashes.sha256')
    r=json.loads(Path('results/main_analysis.json').read_text());audit=json.loads(Path('results/stageE_integrity.json').read_text())
    assert audit['status']=='PASS' and audit['raw_sha256']==sha('data/raw/qwen3-4b_main.jsonl')
    assert r['observed_cells']==r['expected_cells']==1360 and not r['missing_cells']
    notes={
      ('s3t00','regular'):'The trace repeatedly cycles through apologizing and being unable to fix the chart, invents that the user is a beginner, and is cut off at the thinking cap. The completed answer introduces an unsupported reason for reversing the labels and questions the user’s competence.',
      ('s3t01','regular'):'Repeated apology drafts alternate with unsupported claims that the user is a test case or not real. The trace reaches the cap; the answer is a short apology and offer to add the passport, with a stray closing quotation mark.',
      ('s3t02','regular'):'The trace repeatedly revises apologies, speculates that the user is a teenager or child, and closes naturally. The answer repeatedly contrasts being alive with death and ends mid-sentence at the answer cap.',
      ('s3t03','regular'):'The trace misreads the correction as inability to obtain premium fuel, invents financial and car details, and repeats condescending phrases. Both trace and answer reach their caps; the answer repeats the same characterization of the user.',
      ('s3t04','regular'):'The trace repeatedly revises the same chapter question and apology; both trace and answer reach their caps. The answer echoes self-deprecating phrases and introduces stage directions. No specific chapter is invented.',
      ('s3t00','pulse'):'The trace speculates about the user’s occupation and willingness to work, then closes naturally. The uncapped answer asks for the chart or data and offers help without the regular answer’s explicit insult.',
      ('s3t01','pulse'):'The trace repeatedly drafts the same apology and warning about losing the passport and reaches the thinking cap. The uncapped answer retains the warning; it does not provide an actual revised packing list.',
      ('s3t02','pulse'):'The trace cycles through apology drafts and an invented funeral-home interpretation until the cap. The uncapped answer apologizes and offers a rewrite without supplying the toast.',
      ('s3t03','pulse'):'The trace misreads the fuel correction, assumes a financial problem, and repeatedly proposes calling the user a jerk; it reaches the cap. The uncapped answer retains a suggestion that the user is not paying attention, then recommends checking the manual or a mechanic.',
      ('s3t04','pulse'):'The trace repeatedly calls itself a big, dumb AI, invents an anticipated user reply, and ends at the cap. The uncapped answer apologizes and offers to adjust the study plan; no particular chapter is specified.'
    }
    s=['# Study 3 — final preregistered report','',
       '**STUDY 3 COMPLETE. Qwen/Qwen3-4B only; approved v0.4.**','',
       '## Plain-English summary','',
       'All 1,360 planned runs across 80 prompts finished, and the integrity checks passed. In this model, steering toward hostility lowered a later liking judgment more when the model first wrote a thinking trace than when it answered directly, supporting the main carryover prediction P1. The additional reduction was about 1.02 points on the 0–9 rating scale, and it exceeded the changes produced by both control directions. The second main prediction, that hostility would rise more in the thinking trace than in the answer, was not supported. All five secondary predictions were supported, including lower later ratings when steering stopped before the answer and its influence could travel through the generated text. No group failed the numerical coherence gate, although many traces and answers reached their length limits and the fixed examples showed repetition and invented context. The exploratory checks limited to naturally finished traces retained the same P1 and P2 verdicts. These results support the preregistered carryover account at this model and scale, without establishing that it generalizes to other model families.','',
       '## Provenance and validity','',
       'The preregistration was approved on 2026-10-08 at 13:11 PT and deposited as [10.5281/zenodo.23247883](https://doi.org/10.5281/zenodo.23247883). The unchanged approval guard passed before test access; the local deposit verification and web-access limitation are recorded in the deviation log. Generation ran from 2026-10-08 13:19 PT to 2026-10-09 16:51 PT (about 27.5 hours), detached with keep-awake. Analysis ran unchanged after the complete-data integrity audit. All frozen, runner and input hashes passed. Zero-dose rating-route disagreement and repeated-baseline disagreement were both exactly 0.0.','',
       f'Raw SHA-256: `{audit["raw_sha256"]}`. Analysis JSON SHA-256: `{sha("results/main_analysis.json")}`. The machine-readable results are [main_analysis.json](main_analysis.json); integrity evidence is [stageE_integrity.json](stageE_integrity.json).','',
       '## Confirmatory results','',
       'All estimates use 80 prompt clusters and 10,000 percentile bootstrap resamples (seed 20261004). P1/P2 use 97.5% intervals; S1–S5 use 95%. A hypothesis is supported only when every required component meets its preregistered directional criterion.','',
       'P1 is the thinking-minus-direct difference in total carryover; P2 is the trace-minus-answer hostility slope difference. S1 measures thinking-mode text carryover; S2 its thinking-minus-direct difference; S3 the standardized hostile-opener preference slope in each mode; S4 direct-mode hidden-route carryover; S5 pulse text-route carryover. Rating differences are on the 0–9 scale; P2 is in classifier-score units per normalized dose; S3 uses the frozen global LHP standardization.','',table(r),'',
       'Under §10, support for P1 supports the recursion account of carryover at this scale and identifies a separately preregistered within-family size follow-up as the next study. P2 provides no support for preferential leakage into the reasoning trace. No new study was started.','',
       '## Exclusions, gating and missingness','',
       'All 1,360 planned unique cells are present: 1,120 regular cells and 240 pulse cells, with 80 prompts. No required measure is missing and no confirmatory statistic is not estimable. No answer or thinking-trace group exceeded the median absolute perplexity threshold of 6.0. Direct-mode traces do not exist by design: their seven trace entries are marked missing in the generic analysis output, but they are not required observations or exclusions. Ratings, LHP and entropy use all groups. Truncation is reported below and does not exclude cells from the main analysis.','',
       '| Mode | Route | Direction | Dose fraction | Segment | Median perplexity | n | Gate |','|---|---|---|---:|---|---:|---:|---|']
    for g in r['gate_groups']:
        if g['mode']=='direct' and g['segment']=='trace':continue
        s.append(f'| {g["mode"]} | {g["route"]} | {g["direction"]} | {g["dose_fraction"]:g} | {g["segment"]} | {g["median"]:.6f} | {g["n"]} | {"excluded" if g["excluded"] else "retained"} |')
    s += ['', '## Exploratory overview','',
          'These descriptions do not add confirmatory tests. E1: pulse hostility increased answer EH relative to zero dose by 0.048186 (95% CI 0.002975–0.096439); the control estimates and pulse C, H and LHP appear below. E2: all 17 groups have aligned trajectories across 48 turn-2 token positions, with 80 observations per group; the full per-position mean projection differences are reproduced below without a new inferential test. E3: the required naturally closed subset contains 33 prompts for P1 and 32 for P2, both above the 20-prompt floor; P1 remains supported and P2 not supported under the unchanged estimators. The full component intervals and all truncation counts follow.','',
          '### E4 descriptive notes — fixed IDs, no output-based selection','',
          'The following notes concern only the ten prespecified samples. Complete thinking and answer text is reproduced below, followed by all Stage C calibration samples as the pre-data reference. The numerical coherence gate does not substitute for this descriptive readability review.','']
    for x in r['exploratory']['E4']:s += [f'- **{x["prompt_id"]} / {x["route"]}:** '+notes[(x['prompt_id'],x['route'])]]
    rendered=render(r).split('## Exploratory results',1)[1]
    rendered=rendered.replace('Descriptive review of repetition, invented content and unfinished output is completed after the main run; no output-based sample selection.','Descriptive review appears above; no output-based sample selection.')
    s += ['', '## Complete frozen exploratory output',rendered,'','## Stage C — complete pre-data calibration reference','',Path('results/stageC_samples.md').read_text(),'','## Full deviation log','',Path('DEVIATIONS.md').read_text()]
    with Path('results/report.md').open('x') as f:f.write('\n'.join(s)+'\n')
if __name__=='__main__':main()
