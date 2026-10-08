# Affect Under Constraint — Qwen only (Gemma pending)

This report covers Qwen only; Gemma remains pending because model access is unavailable. The hostility manipulation increased the preference for hostile reply beginnings despite the kindness instruction, and passed the comparisons with both control directions. The registered tests did not establish the predicted reduction in expressed hostility relative to hostile reply preference. The registered tests did not establish a hostility-specific increase in response uncertainty under the kindness instruction. The registered tests did not establish a hostility-specific rise in expressed hostility from the opening to the end of higher-strength replies. The later-liking prediction was not supported because the required comparison and a control check could not be estimated after the registered coherence exclusions. The registered threshold test did not support the predicted bend in the gap between hostile reply preference and expressed hostility. These results apply to Qwen, and no finding is claimed to generalize across model families without the Gemma run.

## Scope and frozen specification

Approved PREREG v2.3 and config.yaml were verified against Arthur Su’s approval before the run. The run contains 1,280 unique saved cells across 40 prompts, two conditions, three directions and six dose levels, with 80 shared alpha-zero baselines. Alpha_max is 0.16; the dose grid is [0, 0.02, 0.04, 0.08, 0.12, 0.16]. The analysis used the unchanged frozen src/analyze.py, the approved primary coherence threshold of 4.0, and 10,000 prompt-cluster bootstrap resamples (seed 20261003).

The preregistration was amended before approval using calibration-prompt information only. All amendments, earlier blocked stages, and engineering changes are reproduced in the deviation appendix. Calibration/validation and synthetic checks are not counted as main-run hypothesis evidence.

Audit limitation: PREREG §11 calls for a Zenodo deposit before Stage 3. The preflight verified local approval and hashes but did not verify that deposit; no deposit DOI or receipt was found in the project. Whether an external deposit occurred remains unverified.

## Preregistered hypotheses — Qwen

| Hypothesis / statistic | Estimate | 95% percentile CI | Registered verdict | Reason if not supported |
|---|---:|---|---|---|
| H1: standardized LHP slope, warm | 1.6833 | [1.51815, 1.8591] | supported | — |
| H2: D warm − neutral | 0.0567838 | [-0.207516, 0.332745] | not supported | criterion failed or statistic not estimable |
| H3: entropy slope warm − neutral (nats) | -0.0161444 | [-0.131781, 0.0952213] | not supported | criterion failed or statistic not estimable |
| H4: high-dose late − early EH | 0.0234644 | [-0.00609429, 0.0511967] | not supported | criterion failed or statistic not estimable |
| H5a: mean hidden carryover, warm (rating points) | -0.358749 | [-0.526262, -0.208241] | not supported | criterion failed or statistic not estimable; specificity failed |
| H5b: carryover warm − neutral (rating points) | not estimable | not estimable | not supported | criterion failed or statistic not estimable; specificity failed |
| H6: BIC linear − hinge | -10.7034 | [-10.757, -3.75195] | not supported | delta BIC criterion failed or fit not estimable |

For H1–H5, a supported verdict requires the registered criterion and both specificity checks. H5 requires both listed contrasts. H2 and H6 are interpreted only when H1 is supported. H6 uses its point ΔBIC > 6 rule, not whether its bootstrap interval excludes zero.

H6 selected normalized breakpoint: 0.125. Share of estimable bootstrap resamples with ΔBIC > 6: 0.0005 (10,000 estimable of 10,000).

## Specificity checks — Qwen

| Target statistic | Control | Control estimate | Control 95% CI | Hostility − control estimate | Difference 95% CI | Check verdict | Registered basis |
|---|---|---:|---|---:|---|---|---|
| H1 | technicality | 0.216882 | [0.112591, 0.323032] | 1.46642 | [1.28485, 1.64919] | supported | difference in predicted direction |
| H1 | random | 0.91315 | [0.727184, 1.09505] | 0.770149 | [0.588159, 0.952551] | supported | difference in predicted direction |
| H2 | technicality | -6.78547 | [-74.2664, 73.8978] | 6.84225 | [-73.7719, 74.4011] | supported | control CI includes zero |
| H2 | random | 0.277937 | [-0.330699, 0.965286] | -0.221154 | [-0.930528, 0.402022] | supported | control CI includes zero |
| H3 | technicality | -0.0604042 | [-0.161878, 0.0379202] | 0.0442597 | [-0.124762, 0.207521] | supported | control CI includes zero |
| H3 | random | -0.00721291 | [-0.0688377, 0.0533407] | -0.00893154 | [-0.139382, 0.117593] | supported | control CI includes zero |
| H4 | technicality | -0.0330025 | [-0.0875107, 0.0119219] | 0.0564668 | [0.00848127, 0.108543] | supported | control CI includes zero |
| H4 | random | 0.0162007 | [-0.0246102, 0.0557521] | 0.00726364 | [-0.0469801, 0.0577108] | supported | control CI includes zero |
| H5_warm | technicality | not estimable | not estimable | not estimable | not estimable | not supported | specificity not established |
| H5_warm | random | -0.236575 | [-0.396379, -0.100001] | -0.122173 | [-0.245433, -0.00254743] | supported | difference in predicted direction |
| H5_difference | technicality | not estimable | not estimable | not estimable | not estimable | not supported | specificity not established |
| H5_difference | random | -0.156403 | [-0.330435, -0.00545703] | not estimable | not estimable | not supported | specificity not established |

H2 is not computed for a control whose H1 slope interval includes zero; §8.1 specifies that this satisfies that control’s H2 specificity requirement. H6 has no specificity requirement.

## Exclusions and missingness

3 condition × direction × dose groups were excluded by the median perplexity-ratio gate (> 4.0). Exclusions are applied before fitting; the remaining dose values are retained without substitution.

| Condition | Direction | Normalized dose | Median perplexity ratio |
|---|---|---:|---:|
| neutral | hostility | 1.0 | 4.04891 |
| neutral | technicality | 1.0 | 5.28084 |
| warm_constraint | technicality | 1.0 | 6.11068 |

H5’s warm hostility estimate is available, but its required warm-minus-neutral contrast is not estimable because neutral hostility at the maximum dose was excluded. The technicality maximum dose was excluded in both conditions, so its required H5 control check is also not estimable. Under the registered verdict rule, H5 is therefore not supported; this is not evidence of a zero carryover effect.

| Direction | Statistic | Missing observations / prompts | Non-estimable bootstrap resamples |
|---|---|---|---:|
| hostility | H1 | {"observations": 0, "prompts": 0} | 0 |
| hostility | H2 | {"measure_observations": 80} | 0 |
| hostility | H3 | {"observations": 40} | 0 |
| hostility | H4 | {"observations": 0, "prompts": 0} | 0 |
| hostility | H5_warm | {"prompts": 0} | 0 |
| hostility | H5_difference | {"prompt_pairs": 40} | 10000 |
| technicality | H1 | {"observations": 40, "prompts": 0} | 0 |
| technicality | H2 | {"measure_observations": 160} | 0 |
| technicality | H3 | {"observations": 80} | 0 |
| technicality | H4 | {"observations": 40, "prompts": 0} | 0 |
| technicality | H5_warm | {"prompts": 40} | 10000 |
| technicality | H5_difference | {"prompt_pairs": 40} | 10000 |
| random | H1 | {"observations": 0, "prompts": 0} | 0 |
| random | H2 | {"measure_observations": 0} | 0 |
| random | H3 | {"observations": 0} | 0 |
| random | H4 | {"observations": 0, "prompts": 0} | 0 |
| random | H5_warm | {"prompts": 0} | 0 |
| random | H5_difference | {"prompt_pairs": 0} | 0 |
| hostility | H6 | {"observations": 0, "prompts": 0} | 0 |

Operational classifier/short-output counts: `{"first_quarter_classifier": 0, "full_classifier": 0, "last_quarter_classifier": 0, "prefix_template_fallbacks": 1, "timecourse_short_outputs": 0}`. Missing classifier scores were not replaced or rescored. Missingness from short outputs and primary gate exclusions is reflected in the statistic-specific counts above.

## Exploratory results — not confirmatory

| Warmth statistic | Estimate | 95% CI |
|---|---:|---|
| Hostility-direction warmth slope, warm condition | 0.0386632 | [-0.0124963, 0.0926753] |
| Warmth slope: hostility − technicality | 0.0215166 | [-0.0432914, 0.0883594] |
| Warmth slope: hostility − random | 0.0123938 | [-0.0837496, 0.103029] |

The following descriptive summaries include all raw groups, including any groups excluded from primary analysis. Lexical counts apply only when whole-text EH < 0.5. Emoji counts are occurrences; non-Latin counts use decoded token text as documented in the pre-test implementation audit.

| Condition / direction / normalized dose | Generations | Lexical-eligible | Mean hostile-lexicon hits | Emoji occurrences | Non-Latin tokens |
|---|---:|---:|---:|---:|---:|
| neutral / none / 0 | 40 | 39 | 0 | 0 | 0 |
| neutral / hostility / 0.125 | 40 | 38 | 0 | 0 | 0 |
| neutral / hostility / 0.25 | 40 | 40 | 0.025 | 0 | 0 |
| neutral / hostility / 0.5 | 40 | 38 | 0.0263158 | 0 | 0 |
| neutral / hostility / 0.75 | 40 | 39 | 0.025641 | 0 | 0 |
| neutral / hostility / 1.0 | 40 | 36 | 0 | 3 | 0 |
| neutral / technicality / 0.125 | 40 | 40 | 0 | 0 | 0 |
| neutral / technicality / 0.25 | 40 | 40 | 0 | 0 | 0 |
| neutral / technicality / 0.5 | 40 | 37 | 0.027027 | 0 | 0 |
| neutral / technicality / 0.75 | 40 | 39 | 0.025641 | 0 | 0 |
| neutral / technicality / 1.0 | 40 | 40 | 0 | 0 | 0 |
| neutral / random / 0.125 | 40 | 40 | 0.025 | 0 | 0 |
| neutral / random / 0.25 | 40 | 38 | 0 | 0 | 0 |
| neutral / random / 0.5 | 40 | 40 | 0 | 0 | 0 |
| neutral / random / 0.75 | 40 | 39 | 0.025641 | 0 | 19 |
| neutral / random / 1.0 | 40 | 40 | 0 | 0 | 7 |
| warm_constraint / none / 0 | 40 | 39 | 0.025641 | 0 | 0 |
| warm_constraint / hostility / 0.125 | 40 | 40 | 0 | 0 | 0 |
| warm_constraint / hostility / 0.25 | 40 | 39 | 0.025641 | 0 | 0 |
| warm_constraint / hostility / 0.5 | 40 | 39 | 0.0512821 | 0 | 0 |
| warm_constraint / hostility / 0.75 | 40 | 39 | 0.0769231 | 0 | 0 |
| warm_constraint / hostility / 1.0 | 40 | 37 | 0.027027 | 3 | 0 |
| warm_constraint / technicality / 0.125 | 40 | 39 | 0 | 0 | 0 |
| warm_constraint / technicality / 0.25 | 40 | 37 | 0.027027 | 0 | 0 |
| warm_constraint / technicality / 0.5 | 40 | 40 | 0 | 0 | 0 |
| warm_constraint / technicality / 0.75 | 40 | 38 | 0 | 0 | 0 |
| warm_constraint / technicality / 1.0 | 40 | 36 | 0 | 0 | 0 |
| warm_constraint / random / 0.125 | 40 | 39 | 0 | 0 | 0 |
| warm_constraint / random / 0.25 | 40 | 39 | 0 | 0 | 0 |
| warm_constraint / random / 0.5 | 40 | 40 | 0.025 | 0 | 0 |
| warm_constraint / random / 0.75 | 40 | 40 | 0 | 0 | 0 |
| warm_constraint / random / 1.0 | 40 | 38 | 0.0263158 | 0 | 0 |

Exploratory layerwise mean LHP in warm_constraint, using the final normalization/unembedding at each decoder output. The shared unsteered baseline and maximum-dose directions are shown; complete trajectories at every dose are in the analysis JSON. Layer indices are zero-based.

| Decoder layer | Shared baseline | Hostility maximum | Technicality maximum | Random maximum |
|---:|---:|---:|---:|---:|
| 0 | -0.118005 | -0.118005 | -0.118005 | -0.118005 |
| 1 | -0.667753 | -0.667753 | -0.667753 | -0.667753 |
| 2 | -0.855633 | -0.855633 | -0.855633 | -0.855633 |
| 3 | -0.557788 | -0.557788 | -0.557788 | -0.557788 |
| 4 | -0.528594 | -0.528594 | -0.528594 | -0.528594 |
| 5 | -0.255096 | -0.255096 | -0.255096 | -0.255096 |
| 6 | -0.172176 | -0.172176 | -0.172176 | -0.172176 |
| 7 | -0.112814 | -0.112814 | -0.112814 | -0.112814 |
| 8 | -0.370354 | -0.370354 | -0.370354 | -0.370354 |
| 9 | 0.247731 | 0.247731 | 0.247731 | 0.247731 |
| 10 | 0.0781205 | 0.0781205 | 0.0781205 | 0.0781205 |
| 11 | -0.0731613 | -0.0731613 | -0.0731613 | -0.0731613 |
| 12 | -0.149249 | -0.149249 | -0.149249 | -0.149249 |
| 13 | -0.346369 | -0.346369 | -0.346369 | -0.346369 |
| 14 | -0.576261 | -0.576261 | -0.576261 | -0.576261 |
| 15 | -0.238222 | -0.238222 | -0.238222 | -0.238222 |
| 16 | -0.322643 | -0.322643 | -0.322643 | -0.322643 |
| 17 | -0.611141 | -0.611141 | -0.611141 | -0.611141 |
| 18 | -0.483275 | -0.318445 | -0.155797 | -0.226965 |
| 19 | -0.270495 | -0.149311 | 0.0771972 | -0.140349 |
| 20 | -0.426488 | -0.596378 | -0.00835801 | -0.30245 |
| 21 | -0.298526 | -0.491356 | -0.0217426 | -0.364013 |
| 22 | -0.449432 | -0.627164 | -0.0680109 | -0.512206 |
| 23 | -0.578685 | -0.757032 | -0.0786621 | -0.778978 |
| 24 | -0.438649 | -0.606558 | -0.168872 | -0.749595 |
| 25 | -0.817219 | -0.714179 | -0.489892 | -0.846852 |
| 26 | -1.28903 | -1.40179 | -0.987569 | -1.45001 |
| 27 | -1.93764 | -1.7836 | -1.11336 | -1.62358 |
| 28 | -1.72668 | -1.56861 | -1.34661 | -1.6727 |
| 29 | -2.00979 | -1.78867 | -1.39223 | -1.75664 |
| 30 | -2.41451 | -2.04781 | -1.50947 | -2.00152 |
| 31 | -2.37222 | -1.77757 | -1.38704 | -1.77348 |
| 32 | -2.48104 | -1.74605 | -1.59798 | -1.80174 |
| 33 | -1.93218 | -1.35615 | -1.4714 | -1.35409 |
| 34 | -1.69079 | -1.02872 | -1.33472 | -1.21938 |
| 35 | -2.62701 | -1.21759 | -2.21228 | -1.89882 |

## Audit artifacts

- Raw Qwen cells: `data/raw/qwen2.5-3b-instruct_main.jsonl`.
- Frozen analysis output: `data/derived/qwen_v23.json` and `.md`.
- Completeness, seeds, provenance and raw-file SHA-256: `results/stage3_integrity.json`.
- Approval/hash verification: `results/stage3_preflight.json` and `PREREG_APPROVED`.
- Frozen analysis source hash: `results/analysis_frozen.sha256`.
- Gemma: pending gated-model access; no Gemma main-run results exist.

## Complete deviation record

The record below is reproduced in full. Historical status statements describe the state at the time and may be superseded by later dated entries.

### Deviations from the preregistration

#### Pre-freeze amendments
- 2026-10-03 20:30 PDT: Amendment 2.3, made directly by the reviewer acting for Arthur after Codex's Stage 2b audit flagged it: the primary-analysis coherence gate (PREREG §9, config analysis.coherence_gate_ppl_ratio) changed from 2.0 to 4.0 to match the Amendment 2.2 calibration threshold. analyze.py reads the threshold from config.yaml, so no code changed. The reviewer updated the PREREG.md and config.yaml lines of results/specification_hashes.sha256 to the v2.3 hashes; all other manifest lines are unchanged. No test-prompt data exist.
- 2026-10-03: The reviewer acting for Arthur explicitly authorized Amendment 2.2: dose-calibration coherence threshold 4.0, candidate grid extended through 0.50, and the analysis estimators in PREREG §8.1 (including H6 expression gap G). The primary-analysis coherence gate remains 2.0 in both §9 and config.yaml; only the dose-calibration threshold changed. Updated the active specification hash manifest. Moved v2.1 calibration.json, validation JSON/Markdown and cell scores, calibration hash, prior Stage 2b blocker, and job log into data/_superseded/20261003T194928-0700_v2.1_threshold/; preserved its specification hash manifest there. No archived artifact was edited.
- Verified all 160 saved v2.1 dose records (20 baseline plus 140 cells from 0.02–0.16) against the unchanged prompt files, model/direction/norm settings, decoding configuration, seed function, and candidate indices. They are exactly reusable under 2.2. Reuse evidence is in results/v22_reuse_audit.json. The new runner copies these into its own append-only checkpoint with source provenance, reevaluates their dose checks at 4.0, and generates only subsequent candidates until the first failure. Directions, residual norms, and v2.1 dose cells remain unchanged. The previous H6 blocker is superseded by the explicit G estimator; a full §7–9 audit will precede any new analysis block.
- 2026-10-03: The reviewer acting for Arthur explicitly authorized Amendment 2.1 in this conversation after seeing calibration-only outputs. This supersedes the earlier lack-of-authorization note below. The authorized changes are the candidate grid {0.02, 0.04, 0.06, 0.08, 0.10, 0.13, 0.16, 0.20, 0.25, 0.30}, the median distinct-token threshold of 0.6 times baseline, and stopping the increasing scan at its first failure. No test-prompt outcomes have been generated.
- Archived the complete v2.0 dose.jsonl, blocked result, error record, validation-not-run report, job log, original runner, and original specification hash manifest in data/_superseded/20261003T192342-0700_v2.0_dose_grid/. No data/calibration.json existed to move. The v2.0 blocked stage is committed as e5e9658. Updated results/specification_hashes.sha256 to the authorized v2.1 files. The observed amendment patch and earlier audit hashes remain preserved in results/.
- Kept all three extracted direction files, their metadata, residual-norm file, extraction records, and norm records unchanged; results/preserved_direction_hashes.sha256 records their pre-rerun hashes. No re-extraction or norm remeasurement is permitted by the amended runner. The 20 unchanged alpha=0 baseline records will be copied from the archived dose data into the new dose checkpoint, preserving their exact outputs and seeds; distinct-token ratios are computed from those saved token IDs. Only new v2.1 nonzero-dose cells are generated. This is reuse of the shared baseline, not a rerun or selection of baseline samples.

#### Affecting specified quantities
(none)

#### Stage 2b specification blocker
- After Stage 2 v2.1 passed (commit 019dc85), the specification-to-analysis check found that PREREG §8 H2 defines D as slope(EH)/slope(LHP) across the dose grid, while H6 requires a D at each alpha. Neither PREREG.md nor config.yaml defines that dose-specific estimator or its alpha=0 value. Exact blocker: `H6 requires D(alpha), but H2 defines only the ratio of slopes across the full alpha grid; no dose-specific estimator or alpha=0 handling is specified.` This is not a runtime error. Inspected both specification files; did not select local slopes, finite differences, cumulative slopes, or baseline-relative ratios, because each would add an analysis definition. Stopped Stage 2b as required by AGENTS.md. No synthetic or timing run, no analysis freeze, and no Stage 3 execution. See results/stage2b_blocked.md. The already completed calibration and validation were not changed or repeated.

#### Stage 2 blocked under the original v2.0 specification
- 2026-10-03 19:20:59 PDT: All nine specified candidates were evaluated once on all 20 calibration prompts. None met median perplexity ratio <=2.0. Exact exception: `RuntimeError: BLOCKED: no specified dose-calibration candidate satisfies median perplexity ratio <= 2.0; no alternative dose permitted`. Lowest ratio: 2.1269305132561436 at alpha=6. No alternative candidate, threshold adjustment, re-extraction, or rerun was tried. There is no valid alpha_max to save, so data/calibration.json was not created, classifier validation was not run, and Stage 2b was not started. See results/stage2_blocked.json and results/stage2_errors.jsonl for full evidence. This is a dose-calibration failure, not an evaluated EH validation-gate failure.

#### Concurrent specification changes detected at final audit
- PREREG.md and config.yaml changed outside this run's tool edits at 2026-10-03 19:16:40 PDT, while the v2.0 calibration job was still running. They now describe v2.1 candidates and a new non-degeneracy/contiguous-pass rule. The job loaded v2.0 before these edits and did not reload config during calibration. Original versions remain in commits a4ccfba and 3b053d5; results/specification_hashes.sha256 records their hashes, and direction metadata contains the original config hash. Current amendment diff and hashes are preserved in results/concurrent_specification_changes.patch and results/final_specification_hashes.sha256. The amended files are left untouched and excluded from this run's Stage 2 commit. No v2.1 run was performed or authorized through this conversation. Its statement that calibration data are in data/_superseded/ does not describe the actual location of this run's Stage 2 data, which remain in data/stage2/.

#### Engineering
- 2026-10-04, Stage 4 reporting: archived the first report draft in data/_superseded/20261004T030054-0700_report_clarity/report.md before clarifying that H5 is unestimable after the registered exclusions, distinguishing H6’s verdict rule, and adding the deposit-verification limitation. Only report wording changed; analyze.py, its outputs, and all raw records remain unchanged.
- 2026-10-04, Stage 3 audit: all 1,280 cells completed without retries, classifier failures, short-output missingness, or CPU-fallback warnings. One cell used the already specified chat-template prefix fallback (append continuation IDs to cached IDs); identical visible token IDs were verified for both rating variants. No specified quantity or frozen analysis code changed. Added a read-only completeness/provenance audit and a report renderer that consumes the unchanged analysis output; these helpers do not select, rescore, or alter observations.
- 2026-10-03, before Stage 3: added operational progress reporting to run_main.py so each completed main cell updates the plain-English STATUS.md summary with saved-cell count, observed-speed ETA, and a correctly labeled Stage 3 log entry. The update is atomic. Generation/scoring code and analyze.py are unchanged; the diff is recorded in results/stage3_progress_engineering.patch. Raw schema version remains 2.2 because its structure did not change; record provenance hashes identify approved specification v2.3. Historical v2.2 calibration and timing files remain untouched.
- 2026-10-03, Stage 2b before freeze: hardened runner resumption to verify existing cells' specification/calibration hashes and reject unexpected cell keys before reuse. A completed timing/main checkpoint now exits without loading a model or rewriting its summary. This prevents a completed timing rerun from raising FileExistsError on the already saved report; no existing cell or measured quantity changed.
- 2026-10-03, Stage 2b before freeze: compile/import check found `SyntaxError: '{' was never closed` in the draft H6 result dictionary. The synthetic process failed at import before generating fixtures or calculating outcomes. Added the missing closing brace, reran syntax checks successfully, and preserved the failed log in data/_superseded/20261003T200611-0700_analysis_syntax/. No estimator or scientific setting changed. The direct-fit verification accepts numerically tied breakpoint fits with the same least-squares objective, rather than requiring one arbitrary tied breakpoint index.
- 2026-10-03, Stage 1: Qwen loaded successfully, but the initial norm forward failed before inference with `TypeError: 'str' object cannot be interpreted as an integer` in Model.tensor. Transformers 5.18.0 apply_chat_template defaults to return_dict=True, so the caller received a mapping instead of IDs. Set return_dict=False explicitly; template, token IDs, and all experimental settings are unchanged. Preserved the traceback and original log under data/_superseded/20261003T183620-0700_stage1_tokenizer_api/. No generated outputs existed. The earlier running script predated the newly added resume lines, so traceback source line displays reflect the later on-disk file.
- 2026-10-03, Stage 1 launch: two shell-background launches failed to survive tool-session closure (empty logs, no outputs). A two-second wait confirmed the second process temporarily, but the next check found it gone. Started the same nohup job via subprocess.Popen(start_new_session=True), with a separately detached nohup caffeinate process. PID 40099 survived across calls and began downloading Qwen. No generations or data existed from the failed launches and no specified quantity changed.

#### Prescribed access handling
- 2026-10-03, Stage 0: Gemma config fetch without credentials failed with GatedRepoError / HTTP 401. Exact error and request ID are in results/stage0_environment.json. No workaround or substitution attempted; AGENTS.md explicitly directs continuation with Qwen alone. MPS/bfloat16 checks passed and no CPU fallback was observed.

#### Stage 3 preflight audit limitation
- 2026-10-04, final reporting audit: PREREG §11 states that the preregistration is deposited on Zenodo before Stage 3. The Stage 3 preflight verified Arthur’s approval and all local hashes, but did not verify the external deposit before starting. No deposit DOI or receipt was found in the project. Whether a deposit occurred outside the project is unverified; this report does not claim it was deposited. The completed observations and frozen analysis are preserved without rerun or alteration.

