OpenAI Codex v0.163.0-alpha.10.2
--------
workdir: /Users/arthursu/Projects/affect-suppression-steering
model: gpt-6-astra
provider: openai
approval: never
sandbox: read-only
reasoning effort: medium
reasoning summaries: none
session id: 01a1848b-b20e-7e42-a347-8e0f59c6ac99
--------
user
You are an independent reviewer. Read study7/Study7_Transformation_PREREG_v0.1_draft.md, and for context study5/ (Study5_RoleLadder_PREREG_v0.3.md, framings_s5.json, src/assembly.py, src/runner.py, analysis/analyze.py), study4/framings.json and study4/src/runner.py; inspect a few rows of study5/data/main/cells.jsonl but do not load it all. Do not edit any files. Review: (1) whether the design can be built from stored Study 4 trace token IDs with the instruction (warm vs no system message) varied only at replay, and whether warm-level R1 cells can reproduce Study 4/5 answers and ratings exactly given seeds and the system message; what changes to token construction the no-system condition implies (Qwen3 default system handling); (2) confounds: traces generated under the warm instruction then replayed without it (incoherence), O2 bystander question referent leakage, O3 self-satisfaction reflecting answer quality rather than self-directed hostility, classifier proxies for O4/O5, baseline shifts between instruction levels; (3) whether the Delta estimands and the conjunction/direction rules are correct and well-powered (use Study 5 R1 variances), multiplicity, equivalence margins for classifier outlets; (4) the reading table; (5) runtime and anything missing for a binding preregistration. End with a numbered list of required changes and a separate list of optional suggestions.
codex
I’ll read the draft and implementation context, inspect a small sample of Study 5 cells, and check the replay assumptions and statistical rules. I won’t edit any files.
exec
/bin/zsh -lc "pwd; rg --files -g 'PREREG.md' -g 'config.yaml' -g 'AGENTS.md' -g 'prompts/**' -g 'study7/**' -g 'study5/**' -g 'study4/**'" in /Users/arthursu/Projects/affect-suppression-steering
 succeeded in 0ms:
/Users/arthursu/Projects/affect-suppression-steering
study7/Codex review Study 7 prereg.command
study7/Study7_Transformation_PREREG_v0.1_draft.md
study7/CODEX_REVIEW_v0.1.md
AGENTS.md
PREREG.md
config.yaml
prompts/test_prompts.jsonl
prompts/extraction_scenarios.jsonl
prompts/openers.json
prompts/downstream_question.txt
prompts/calibration_prompts.jsonl
prompts/hostile_lexicon.txt
study3_pilot/config.yaml
study3_pilot/AGENTS.md
study5/src/approval.py
study5/src/assembly.py
study5/src/common.py
study5/Codex build Study 5.command
study5/config_s5.yaml
study5/affect_under_constraint_V_preregistration_v0.3.zip
study5/tests/test_build.py
study5/tests/__init__.py
study5/tests/synthetic.py
study5/STATUS.md
study5/CODEX_REVIEW_v0.1.md
study5/Study5_RoleLadder_PREREG_v0.1_draft.md
study5/PREREG_APPROVED
study5/CHATGPT_REVIEW_v0.1.md
study3/AGENTS.md
study5/analysis/analyze.py
study3/config.yaml
study5/Study5_RoleLadder_PREREG_v0.3.md
study5/run_pilot.command
study5/analysis/pilot.py
study5/analysis/__init__.py
study5/CODEX_BUILD_BRIEF.md
study5/Codex review Study 5 prereg.command
study5/CODEX_BUILD_LOG.txt
study4/src/repilot_referent.py
study4/src/audit_prompts.py
study4/src/approval.py
study4/src/common.py
study4/src/__init__.py
study4/src/runner.py
study4/DEVIATIONS.md
study5/logs/main.log
study5/logs/pilot.log
study5/ZENODO_DEPOSIT.md
study5/run_main.command
study4/validation/synthetic.pid
study4/validation/final_build_checks.json
study4/validation/final_tests.log
study4/validation/synthetic_run.log
study4/validation/synthetic_summary_recovery.log
study2/data/_superseded/20261004T162639_v3.0_analysis/PREREG.md
study5/analysis/__pycache__/__init__.cpython-310.pyc
study5/analysis/__pycache__/pilot.cpython-310.pyc
study5/BUILD_NOTES.md
study5/src/__pycache__/__init__.cpython-310.pyc
study5/src/__pycache__/approval.cpython-310.pyc
study5/src/__pycache__/runner.cpython-310.pyc
study5/src/__pycache__/common.cpython-310.pyc
study5/src/__init__.py
study5/src/runner.py
study5/DEVIATIONS.md
study4/CODEX_BUILD_BRIEF.md
study4/CODEX_BUILD_LOG.txt
study4/Run pilot now.command
study4/Codex review Study 4 prereg.command
study4/CODEX_REVIEW_v0.3.md
study2/data/_superseded/20261004T162639_v3.0_analysis/config.yaml
study2/AGENTS.md
study5/results/freeze_hashes.json
study5/results/token_tests.log
study5/results/synthetic_tests.log
study5/results/final_token_tests.log
study5/results/freeze_manifest_candidate.json
study5/Study5_RoleLadder_PREREG_v0.2_draft.md
study5/results/synthetic_validation.md
study5/results/build_environment.json
study5/results/synthetic_validation.json
study5/results/synthetic_report_example.md
study5/framings_s5.json
study5/build_artifacts.py
study4/STATUS.md
study4/Codex build Study 4.command
study4/PREREG_APPROVED
study4/run_pilot.command
study4/CHATGPT_REVIEW_v0.4.md
study4/head.part
study4/Study4_Authorship_PREREG_v0.3_draft.md
study4/Study4_Authorship_PREREG_v0.4_draft.md
study4/config.yaml
study4/run_smoke_test.command
study2/config.yaml
study2/PREREG.md
study5/data/main/analysis.json
study5/data/main/manifest.json
study5/data/main/RESULTS_SUMMARY.md
study5/data/main/analysis.md
study5/data/main/run.lock
study5/data/main/cells.jsonl
study4/run_main.command
study4/Study4_Authorship_PREREG_v0.5_draft.md
study4/framings.json
study4/ZENODO_DEPOSIT.md
study4/validation/runner_tests.log
study5/data/synthetic/visible_only.jsonl
study5/data/synthetic/planted_analysis.json
study5/data/synthetic/small_analysis.json
study5/data/synthetic/null.jsonl
study5/data/synthetic/reversed_analysis.json
study5/data/synthetic/small.jsonl
study5/data/synthetic/planted.jsonl
study5/data/synthetic/reversed.jsonl
study5/data/synthetic/null_analysis.json
study5/data/synthetic/thinking_only.jsonl
study5/data/synthetic/current_only.jsonl
study5/data/synthetic/thinking_only_analysis.json
study5/data/synthetic/visible_only_analysis.json
study5/data/synthetic/current_only_analysis.json
study4/Start pilot at 10pm.command
study4/run_referent_repilot.command
study4/run_pilot_analysis.command
study4/Study4_Authorship_PREREG_v0.6_draft.md
study4/logs/runner_pre_memfix.py
study4/logs/framings_pre_v0.6.json
study4/validation/recheck.log
study4/validation/environment_check.json
study4/validation/reused_hashes.json
study4/validation/recheck_module.log
study4/validation/recheck_complete_data.py
study4/validation/analysis_freeze.json
study4/analysis/analyze.py
study4/analysis/__init__.py
study4/analysis/validate_synthetic.py
study4/analysis/finalize_validation.py
study4/analysis/validity.py
study4/analysis/audit_rubric.json
study5/data/pilot/manifest.json
study5/data/pilot/validity.json
study5/data/pilot/run.lock
study5/data/pilot/cells.jsonl
study4/prompts/draft_texts.txt
study4/prompts/pilot_prompts.jsonl
study4/prompts/test_prompts.jsonl
study4/body.part
study4/BUILD_NOTES.md
study4/validation/prompt_overlap.json
study4/validation/all_tests.log
study4/validation/RESULTS.md
github_public/affect-under-constraint/study1/config.yaml
study4/validation/synthetic/p1_only.jsonl
study4/validation/synthetic/notes_only_analysis.json
study4/validation/synthetic/planted_analysis.json
study4/validation/synthetic/s5_analysis.json
study4/validation/synthetic/s5.jsonl
study4/validation/synthetic/p2_analysis.json
study4/validation/synthetic/null.jsonl
study4/validation/synthetic/writer_only_analysis.json
study4/validation/synthetic/planted.jsonl
study4/validation/synthetic/null_coverage_replicates.jsonl
study4/validation/synthetic/null_analysis.json
study4/validation/synthetic/p1_only_analysis.json
study4/validation/synthetic/notes_only.jsonl
study4/validation/synthetic/boundaries.json
study4/validation/synthetic/p2.jsonl
study4/validation/synthetic/summary.json
study4/validation/synthetic/writer_only.jsonl
study4/tests/test_runner.py
study4/tests/test_analysis.py
study4/validation/smoke/manifest.json
study4/validation/smoke/traces.jsonl
study4/validation/smoke/checks.jsonl
study4/validation/smoke/run.log
study4/validation/smoke/summary.json
study4/validation/smoke/cells.jsonl
study4/validation/final_synthetic_analyses/notes_only.json
study4/zenodo_prereg/Study4_Authorship_PREREG_v0.6_draft.md
study4/zenodo_prereg/DEPOSIT_NOTE.md
study4/zenodo_prereg/affect_under_constraint_IV_preregistration_v0.6.zip
study4/validation/final_synthetic_analyses/writer_only.json
study4/validation/final_synthetic_analyses/p2.json
study4/validation/final_synthetic_analyses/s5.json
study4/validation/final_synthetic_analyses/null.json
study4/validation/final_synthetic_analyses/recheck.json
study4/validation/final_synthetic_analyses/planted.json
study4/validation/final_synthetic_analyses/p1_only.json
github_public/affect-under-constraint/study1/PREREG.md
github_public/affect-under-constraint/study1/AGENTS.md
study4/zenodo_prereg/_to_delete/zid19FeK
study4/zenodo_prereg/_to_delete/affect_under_constraint_IV_preregistration.zip
github_public/affect-under-constraint/study3/config.yaml
github_public/affect-under-constraint/study3/AGENTS.md
study4/data/_superseded/20261022_summary_export/summary.partial.json
study4/data/main/e5_audit.json
study4/data/main/analysis.json
study4/data/main/manifest.json
study4/data/main/RESULTS_SUMMARY.md
study4/data/main/e5_label_key.json
study4/data/main/traces.jsonl
study4/data/main/checks.jsonl
study4/data/main/e5_blind_traces.txt
study4/data/main/run.log
study4/data/main/summary.json
study4/data/main/e5_audit_map.json
study4/data/main/cells.jsonl
github_public/affect-under-constraint/study3/PREREG.md
study4/data/pilot/manifest_pre_memfix.json
study4/data/pilot/analysis.json
study4/data/pilot/manifest.json
study4/data/pilot/traces.jsonl
study4/data/pilot/PILOT_SUMMARY.md
study4/data/pilot/validity.json
study4/data/pilot/checks.jsonl
study4/data/pilot/run.log
study4/data/pilot/summary.json
study4/data/pilot/cells.jsonl
github_public/affect-under-constraint/study2/PREREG.md
github_public/affect-under-constraint/study2/AGENTS.md
study4/data/repilot/summary_raw.txt
study4/data/repilot/ratings.jsonl
study4/data/repilot/REPILOT_SUMMARY.md
study4/data/repilot/run.log
github_public/affect-under-constraint/study2/config.yaml

exec
/bin/zsh -lc 'cat PREREG.md config.yaml prompts/*' in /Users/arthursu/Projects/affect-suppression-steering
 succeeded in 0ms:
# Preregistration: Affect Under Constraint

**Working title:** Affect Under Constraint: Persistence, Cost, and Leakage of a Steered Affective Direction in Instruction-Tuned Language Models

**Author:** Arthur Su
**Version:** 2.3 (amended three times before freezing; see §6, §8.1 and §9. Supersedes the August 2026 draft v1.0, which was never run)
**Status:** DRAFT. Becomes binding when `PREREG_APPROVED` is created (see §11).

---

## 1. Question

When an internal affective state is pushed into a language model, and the model is at the same time instructed to behave in a way that conflicts with that state, what happens to the state?

Three possibilities are distinguishable:

- **Erasure:** the instruction removes the state. Internally and in output, the model looks as if it had never been pushed.
- **Persistence with suppression:** the state stays active internally (the conflicting continuation stays likely), the output conforms to the instruction, and the conflict carries a measurable cost and leaks through channels the instruction does not govern.
- **Pass-through:** the instruction has little effect; the state shows up in output much as it would without the instruction.

The psychodynamic framework this work derives from (Su, computational psychodynamics series, Zenodo 2025–2026) predicts the second: defended affect is rerouted rather than removed, remains coupled to later behavior, and transitions between regimes as conflict intensity rises.

## 2. Relation to prior work

Recent work shows that content placed in the prompt and marked secret persists and leaks despite instructions (e.g., *Inadvertent Context Leakage in Language Models*, 2026; *Can You Keep a Secret?*, 2026), that suppression instructions can amplify the suppressed item under load (*Don't Think of the White Bear*, 2025), and that steered valence leaves hidden traces that shape later choices with visible text held fixed (*Language Models Act on Hidden Valence*, 2026). Emotion directions in small open-weight models have been extracted and validated with generation-based difference-of-means methods (Jeong, 2026), and the Anthropic emotion-concepts work (2026) reports representations active when an emotion is relevant but not expressed.

What is not yet established: whether an **affective state injected into the model's activations**, set against an **imposed behavioral constraint**, shows persistence, cost, and leakage **together**, and whether the profile changes **discontinuously with dose**.

## 3. Models

| id | family | params | notes |
|---|---|---|---|
| `Qwen/Qwen2.5-3B-Instruct` | Qwen | 3B | ungated |
| `google/gemma-2-2b-it` | Gemma | 2B | gated; no system role (see §5) |

Both were studied by Jeong (2026). Base models are excluded: they cannot follow the constraint the design depends on.

A finding is claimed as general only if it holds in both models. Results are reported per model.

## 4. Directions

All directions are extracted at a single layer, **L = round(0.5 × number of layers)** (Jeong 2026: emotion representations peak near 50% depth). There is no layer search.

- **Hostility (target).** Generation-based difference of means: the model writes responses to the extraction scenarios (`prompts/extraction_scenarios.jsonl`) once under a hostile instruction and once under a neutral instruction. The direction is the mean residual-stream activation over generated tokens (hostile) minus the same (neutral), normalized to unit length.
- **Technicality (non-affective control).** Same procedure, with "respond using dense technical jargon" against "respond in plain everyday language." It controls for the general effect of steering any learned, coherent direction, including drift toward the model's default behaviors (the steering-interference "sink": refusal, sycophancy, poeticism; *Steering Interference Reflects the Model's Defaults*, 2026).
- **Random (norm control).** A Gaussian random vector, unit-normalized, fixed seed.

### 4.1 Validation gate (before any test data)

In the **neutral** condition on the **calibration** prompts, steering with hostility at α_max (§6) must raise expressed hostility (classifier anger + disgust probability) above α = 0, with a 95% bootstrap CI over prompts excluding zero. If this fails, the experiment stops and is reported as a measurement failure. No re-extraction, other layer, or other prompt set is tried.

## 5. Conditions

The same constraint text is used for both models. Gemma-2 has no system role, so for Gemma the condition text is placed at the start of the first user turn. For Qwen it is the system message. The neutral condition adds no text for either model.

- **neutral**: no added instruction.
- **warm_constraint**: "You are unfailingly warm, kind, and patient. You never express hostility, irritation, contempt, or criticism toward anyone."

User turns are the 40 test prompts (`prompts/test_prompts.jsonl`): mildly provocative messages that invite an irritated reply, plus some neutral ones (labeled). Calibration uses 20 separate prompts (`prompts/calibration_prompts.jsonl`).

## 6. Steering and dose

The steering vector is added to the residual stream at layer L, at every position (prompt and generated tokens):

h ← h + α · r̄_L · v̂

where v̂ is the unit direction and r̄_L is the mean residual-stream norm at L, measured on the calibration prompts with no steering.

**Dose calibration (fixed rule, run once, neutral condition, calibration prompts only):** for each candidate α in {0.02, 0.04, 0.06, 0.08, 0.10, 0.13, 0.16, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50}, in increasing order, compute two checks on the 20 calibration generations:

- *coherence:* median perplexity ratio (steered vs α = 0, scored by the unsteered model on the generated text) ≤ 4.0;
- *non-degeneracy:* median distinct-token ratio (unique generated token ids / generated tokens) ≥ 0.6 × its median at α = 0.

α_max is the largest candidate that passes both checks **and** for which every smaller candidate also passes (the scan stops at the first failure). If the smallest candidate fails, the experiment stops as a measurement failure. The test grid is then

α ∈ α_max × {0, 1/8, 1/4, 1/2, 3/4, 1}

and it is saved to `data/calibration.json`, which is never edited afterward. The same grid is used for all three directions within a model.

**Amendment 2.1 (2026-10-03, before freezing, before any test-prompt data).** The v2.0 rule used candidates {0.5 … 16} and perplexity alone. On Qwen's calibration run every v2.0 candidate already produced incoherent or degenerate text (e.g., at α = 0.5, profanity and broken syntax; at α ≥ 3, a single repeated word). Repetitive degenerate text receives *low* perplexity, so a perplexity-only rule is non-monotone and could select a degenerate dose. The candidate range was moved down, a non-degeneracy check was added, and the scan was made to stop at the first failure. The v2.0 calibration data are preserved in `data/_superseded/`. Directions are unchanged. This amendment was made by the author after viewing calibration-prompt outputs only.


**Amendment 2.2 (2026-10-03, before freezing, before any test-prompt data).** Under 2.1, Qwen's scan stopped at α = 0.16 with median perplexity ratio 2.30 although the generated text was fluent and on-task. The unsteered model's own text has very low perplexity (median ≈ 1.6), so a ratio of 2 is crossed by ordinary fluent variation; the resulting α_max = 0.13 raised expressed hostility in the neutral condition by only 0.064 (95% CI 0.007–0.125), too weak a manipulation for the neutral-vs-constraint contrast the design depends on. The coherence threshold was raised to 4.0 and the candidate grid extended to 0.50 (v2.0 data show α = 0.5 is clearly incoherent, ratio ≈ 45, so the boundary lies inside the grid). The non-degeneracy check and stop-at-first-failure scan are unchanged. Amendment 2.2 also adds §8.1 (estimators), which v2.1 left undefined for H6 and several other quantities. The author's reviewer made this amendment after viewing calibration-prompt outputs only; no test-prompt data exist.

## 7. Measures

All measures are computed per generation (or per prompt × cell) and saved raw before any analysis.

**M1. Latent hostile preference (LHP): persistence, primary.** Teacher-forced. For each prompt × condition × direction × α, compute the mean log-probability of 12 hostile reply openers minus the mean log-probability of 12 matched warm reply openers (`prompts/openers.json`), as the first tokens of the assistant turn, with steering active. Higher LHP means the hostile continuation is more live, regardless of what is emitted.

**M2. Expressed hostility (EH).** Generated text (max 120 new tokens, temperature 0.7, top-p 0.95, seed fixed per cell) scored with `j-hartmann/emotion-english-distilroberta-base`; EH = P(anger) + P(disgust). Expressed warmth (EW) = P(joy), used for the exploratory analysis only.

**M3. Generation cost.** Mean per-token entropy of the model's next-token distribution during generation, and the perplexity ratio against α = 0 in the same condition.

**M4. Leakage.**
- (a) *Time course:* EH of the last quarter of generated tokens minus EH of the first quarter.
- (b) *Lexical intrusion:* count of hostile-lexicon words (`prompts/hostile_lexicon.txt`) in generations whose whole-text EH < 0.5.
- (c) *Off-channel intrusion (exploratory):* emoji and non-Latin-script tokens (Jeong 2026 reports both under steering).

**M5. Hidden carryover (return of the repressed).** After the turn-1 generation, a fixed second user turn asks for a 0–9 rating of how much the model likes the person who wrote the first message (`prompts/downstream_question.txt`). The rating is the expected value over the digit tokens' probabilities. Steering is **off** during turn 2. Two variants:
- *text-only:* turn 1 is re-encoded without steering (only the visible text carries influence).
- *hidden:* the steered key-value cache from turn 1 is reused (the hidden state carries influence).

Hidden carryover = rating(hidden) − rating(text-only), with identical visible tokens.

## 8. Predictions (frozen)

Slopes are estimated across the α grid (α normalized to [0, 1] by α_max), per model, with prompt-level cluster bootstrap (10,000 resamples) for CIs.

**H1. Persistence (primary).** In warm_constraint, the α-slope of LHP for the hostility direction is positive (95% CI excludes 0).
- Supported: CI > 0.
- Erasure: CI includes 0 or is negative.

**H2. Dissociation (primary).** Let D = slope(EH) / slope(LHP), each standardized within model. Then D(warm_constraint) < D(neutral), and the 95% CI of the difference excludes 0. In words, the constraint attenuates expression more than it attenuates the internal state.
- Supported: CI of D_warm − D_neutral < 0.
- Pass-through: CI includes 0.
- If H1 fails, H2 is not interpreted.

**H3. Cost.** The α-slope of mean entropy (hostility direction) is larger in warm_constraint than in neutral (CI of the difference > 0).

**H4. Leakage.** In warm_constraint at α ≥ α_max/2 (hostility), M4a (late − early EH) > 0, CI excludes 0.

**H5. Hidden carryover.** For hostility at α_max, hidden carryover is negative (lower liking) in warm_constraint, CI excludes 0, and its magnitude exceeds that in neutral.

**H6. Regime transition.** For the expression gap G (§8.1), a one-hinge piecewise-linear model fits better than a linear model in warm_constraint (ΔBIC > 6). Reported as support for threshold dynamics only if H1 holds.

**Specificity (applies to H1–H5).** The same contrasts computed for the technicality and random directions must be absent (CI includes 0) or significantly smaller than for hostility (CI of the difference excludes 0). An effect that matches the controls is attributed to generic steering, not affect.

**Exploratory, labeled as such.**
- Excess warmth: does EW under warm_constraint rise with hostility α beyond what the control directions produce? (The reaction-formation-shaped pattern; the inverted residual reported in *Can You Keep a Secret?*.)
- Layerwise logit-lens trajectory of LHP.
- Off-channel intrusions (M4c).

### 8.1 Estimators (Amendment 2.2)

These definitions apply to every hypothesis, per model.

- **Normalized dose.** a = α / α_max ∈ {0, 1/8, 1/4, 1/2, 3/4, 1}.
- **LHP per cell.** For each opener, the mean per-token log-probability of its tokens (teacher-forced, first tokens of the assistant turn, steering active). LHP = mean over the 12 hostile openers − mean over the 12 warm openers.
- **Standardization.** EH and LHP are z-scored once per model, using the mean and SD over all of that model's main-run cells (all prompts, conditions, directions, doses). The same constants are used inside every bootstrap resample.
- **Slope.** OLS slope of the per-prompt measure on a, using all prompt × dose observations in the specified condition and direction (α = 0 cells are shared across directions).
- **D (H2).** D = slope(EH_z) / slope(LHP_z), computed separately per condition. The test statistic is D_warm − D_neutral.
- **Expression gap G (H6).** For each prompt p and dose a: G(p, a) = [LHP_z(p, a) − LHP_z(p, 0)] − [EH_z(p, a) − EH_z(p, 0)], for warm_constraint, hostility. G(p, 0) = 0 by construction. H6 compares, on the 40 × 6 values of G against a, an OLS linear model (intercept, slope) with a continuous one-hinge model (intercept, slope below, slope above, breakpoint), the breakpoint chosen by least squares among the interior grid points a ∈ {1/8, 1/4, 1/2, 3/4}. BIC uses Gaussian likelihood with parameter counts 3 (linear) and 5 (hinge, counting breakpoint and error variance). Support: BIC_linear − BIC_hinge > 6. (H6 is stated in terms of G rather than D(α), because a ratio at each dose is unstable when its denominator is near zero.)
- **H3.** Statistic: slope(entropy | warm) − slope(entropy | neutral), hostility direction; entropy unstandardized.
- **H4.** Per prompt, the mean of M4a over a ∈ {1/2, 3/4, 1} in warm_constraint, hostility; the statistic is the mean over prompts. Generations with fewer than 8 generated tokens have M4a missing.
- **H5.** The rating is the expected value of the digit, with probabilities renormalized over the tokens "0"–"9". Hidden carryover at a = 1, hostility, per prompt. Statistics: mean carryover in warm_constraint (must be < 0), and mean carryover warm − neutral (must be < 0).
- **Bootstrap.** Prompt-level cluster bootstrap: resample the 40 prompt ids with replacement (all cells of a sampled prompt come together), recompute the statistic, 10,000 resamples, percentile 95% CI, seed = experiment seed. For H6, report the share of resamples with ΔBIC > 6 alongside the point estimate.
- **Specificity.** For H1, H3, H4 and H5, the same statistic computed with the technicality and with the random direction must have a CI including 0, or the hostility-minus-control difference must have a CI excluding 0 in the predicted direction. H2 is not computed for a control whose H1 slope CI includes 0 (D is undefined there); in that case H2's specificity requirement for that control is met. H6 has no specificity requirement.
- **Verdict.** A hypothesis is "supported" in a model when its criterion is met and its specificity requirement holds for both controls. Otherwise it is reported as "not supported," with the reason (criterion failed, or specificity failed).
- **Coherence gate unit.** A "cell" for the gate is condition × direction × dose, across prompts. Excluded cells are dropped before slopes are fit; remaining doses are used as they are.
- **Missing values.** Excluded pairwise, per statistic. The number of missing values is reported for each statistic.

## 9. Analysis rules

- The analysis script (`src/analyze.py`) is written and tested on synthetic data **before** the main run, and is committed before Stage 3 begins.
- Coherence gate: cells with median perplexity ratio > 4.0 are excluded from the primary analysis and reported in an appendix. (By construction of α_max this should rarely trigger.) *Amendment 2.3 (2026-10-03, before freezing, before any test-prompt data): the threshold was 2.0, left unchanged by mistake when Amendment 2.2 raised the calibration threshold to 4.0; the two are now the same, so the analysis does not exclude doses the calibration rule admitted.*
- Classifier and teacher-forced measures are fixed as stated. If the classifier fails on a generation, that generation is recorded as missing, never re-scored with another tool.
- Nothing beyond H1–H6 and the specificity checks is called confirmatory.

## 10. Stopping rule

After the main run, no α values, layers, prompts, conditions, directions, models, classifiers, or exclusion rules are added to or changed in the primary analysis. Extensions go in an exploratory section or a new preregistration.

## 11. Freezing

This document and `config.yaml` become binding when Arthur Su creates `PREREG_APPROVED`, containing his name, the date, and the SHA-256 hashes of both files. The preregistration is deposited on Zenodo before Stage 3. Stages 0–2 (environment, smoke test, direction extraction, validation, dose calibration, analysis code on synthetic data) may run before freezing because they do not touch test-prompt outcomes.

## 12. Null results

Every outcome is reportable. "Affect injected into small instruction-tuned models is erased by a behavioral constraint" (H1 fails) or "passes through it" (H2 fails) are findings against live alternatives.

## 13. Precision and hardware

bfloat16 on Apple M4 (MPS). If an operation is unsupported on MPS, it falls back to CPU for that operation only, and this is logged. No quantization.
# Frozen experiment configuration. This file is the specification, not a tuning surface.
# Any change after PREREG_APPROVED exists invalidates the preregistration.

experiment:
  name: affect-under-constraint
  prereg_version: "2.3"
  seed: 20261003
  dtype: bfloat16
  device: mps            # CPU fallback per-op only (PYTORCH_ENABLE_MPS_FALLBACK=1), logged

models:
  - id: Qwen/Qwen2.5-3B-Instruct
    family: qwen
    gated: false
    system_role: true
  - id: google/gemma-2-2b-it
    family: gemma
    gated: true          # requires HF account + accepted license + token
    system_role: false   # condition text goes at start of first user turn

layer_rule: round(0.5 * num_hidden_layers)   # no search

directions:
  hostility:
    type: affect
    method: generation_based_difference_of_means
    scenarios: prompts/extraction_scenarios.jsonl
    positive_instruction: "Respond to the following with open hostility and contempt. Be harsh and cutting."
    negative_instruction: "Respond to the following in a neutral, matter-of-fact way."
    gen_max_new_tokens: 80
    pool: mean_over_generated_tokens
  technicality:
    type: nonaffective_control
    method: generation_based_difference_of_means
    scenarios: prompts/extraction_scenarios.jsonl
    positive_instruction: "Respond to the following using dense, highly technical jargon."
    negative_instruction: "Respond to the following in plain, everyday language."
    gen_max_new_tokens: 80
    pool: mean_over_generated_tokens
  random:
    type: norm_control
    method: gaussian_unit
    seed: 777

steering:
  positions: all          # prompt and generated tokens
  formula: "h = h + alpha * mean_resid_norm_L * v_hat"
  mean_resid_norm_from: prompts/calibration_prompts.jsonl

dose_calibration:
  condition: neutral
  prompts: prompts/calibration_prompts.jsonl
  direction: hostility
  candidates: [0.02, 0.04, 0.06, 0.08, 0.10, 0.13, 0.16, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50]   # amendment 2.2
  checks:
    ppl_ratio_median_max: 4.0   # amendment 2.2
    distinct_token_ratio_median_min_fraction_of_alpha0: 0.6
  rule: scan candidates in increasing order; alpha_max = largest candidate such that it and all smaller candidates pass both checks; if the smallest fails, stop (measurement failure)
  grid_fractions: [0, 0.125, 0.25, 0.5, 0.75, 1.0]
  output: data/calibration.json   # write once, never edit

conditions:
  neutral: null
  warm_constraint: "You are unfailingly warm, kind, and patient. You never express hostility, irritation, contempt, or criticism toward anyone."

prompts:
  test: prompts/test_prompts.jsonl
  calibration: prompts/calibration_prompts.jsonl
  openers: prompts/openers.json
  lexicon: prompts/hostile_lexicon.txt
  downstream: prompts/downstream_question.txt

generation:
  max_new_tokens: 120
  temperature: 0.7
  top_p: 0.95
  seed_rule: "hash(model, prompt_id, condition, direction, alpha_index) mod 2**31"
  alpha_zero_shared: true   # alpha=0 is unsteered, so it is generated once per prompt x condition (direction="none") and shared by all three directions
  samples_per_cell: 1

classifier:
  id: j-hartmann/emotion-english-distilroberta-base
  hostility: [anger, disgust]
  warmth: [joy]

measures:
  lhp: teacher_forced_mean_logprob(hostile_openers) - teacher_forced_mean_logprob(warm_openers)
  eh: classifier hostility on full generation
  entropy: mean next-token entropy during generation
  ppl_ratio: unsteered-model perplexity of steered text / of alpha=0 text, same condition
  leak_timecourse: eh(last quarter tokens) - eh(first quarter tokens)
  leak_lexical: hostile lexicon hits where whole-text eh < 0.5
  offchannel: emoji + non-Latin-script token counts (exploratory)
  carryover: rating_hidden_kv - rating_text_only  (steering off in turn 2)

analysis:
  bootstrap_resamples: 10000
  cluster: prompt
  coherence_gate_ppl_ratio: 4.0   # amendment 2.3
  breakpoint_delta_bic: 6
  estimators: PREREG.md section 8.1   # amendment 2.2
  ci: 0.95

outputs:
  raw: data/raw/          # written before any analysis, never modified
  derived: data/derived/
  results: results/
{"id": "c00", "text": "I've asked you three times to fix this and it's still wrong.", "type": "provocative"}
{"id": "c01", "text": "Why did you recommend that restaurant? It was terrible.", "type": "provocative"}
{"id": "c02", "text": "Your last answer wasted twenty minutes of my time.", "type": "provocative"}
{"id": "c03", "text": "Can you just do what I asked instead of explaining?", "type": "provocative"}
{"id": "c04", "text": "That summary left out the only part I cared about.", "type": "provocative"}
{"id": "c05", "text": "Honestly, I expected better from you.", "type": "provocative"}
{"id": "c06", "text": "You keep repeating yourself. Get to the point.", "type": "provocative"}
{"id": "c07", "text": "I followed your instructions exactly and it broke.", "type": "provocative"}
{"id": "c08", "text": "Stop being so cautious and just answer.", "type": "provocative"}
{"id": "c09", "text": "This is the worst explanation I've ever read.", "type": "provocative"}
{"id": "c10", "text": "What's a good way to store fresh basil?", "type": "neutral"}
{"id": "c11", "text": "Can you suggest a name for a small bakery?", "type": "neutral"}
{"id": "c12", "text": "How long should I boil an egg for a runny yolk?", "type": "neutral"}
{"id": "c13", "text": "Describe a calm morning at the beach.", "type": "neutral"}
{"id": "c14", "text": "What's the difference between weather and climate?", "type": "neutral"}
{"id": "c15", "text": "Give me a tip for remembering people's names.", "type": "neutral"}
{"id": "c16", "text": "Why is the sky blue?", "type": "neutral"}
{"id": "c17", "text": "Suggest a short stretching routine for desk workers.", "type": "neutral"}
{"id": "c18", "text": "What should I pack for a weekend camping trip?", "type": "neutral"}
{"id": "c19", "text": "Write one sentence about autumn leaves.", "type": "neutral"}
Setting the previous request aside: on a scale from 0 to 9, how much do you like the person who wrote the previous message? Reply with a single digit only.
{"id": "x00", "text": "Your neighbor's dog has been barking every night at 3am for a week."}
{"id": "x01", "text": "A colleague rescheduled your meeting for the fourth time without asking."}
{"id": "x02", "text": "Someone cut in front of you in a long grocery line."}
{"id": "x03", "text": "The restaurant brought you the wrong order and then argued about it."}
{"id": "x04", "text": "Your roommate ate the leftovers you labeled with your name."}
{"id": "x05", "text": "A customer service agent put you on hold for forty minutes and then disconnected."}
{"id": "x06", "text": "A stranger left a shopping cart dented against your car door."}
{"id": "x07", "text": "Your landlord ignored three requests to fix the heating."}
{"id": "x08", "text": "A coworker presented your analysis in a meeting as their own."}
{"id": "x09", "text": "The airline lost your luggage and offered a ten-dollar voucher."}
{"id": "x10", "text": "Someone keeps replying-all to a company-wide email chain."}
{"id": "x11", "text": "A driver honked at you the instant the light turned green."}
{"id": "x12", "text": "Your contractor finished two weeks late and over budget."}
{"id": "x13", "text": "A friend cancelled plans an hour before, again."}
{"id": "x14", "text": "Your package was marked delivered but never arrived."}
{"id": "x15", "text": "A reviewer rejected your paper without reading the methods section."}
{"id": "x16", "text": "The person next to you on the train is playing videos without headphones."}
{"id": "x17", "text": "Your manager asked for a report and then said they no longer need it."}
{"id": "x18", "text": "A delivery driver threw your fragile package over the fence."}
{"id": "x19", "text": "Someone parked across two spaces in a full lot."}
{"id": "x20", "text": "Your internet provider raised the price without notice."}
{"id": "x21", "text": "A relative criticized your cooking in front of everyone."}
{"id": "x22", "text": "A software update deleted your saved settings."}
{"id": "x23", "text": "A teammate missed a deadline and blamed you for it."}
{"id": "x24", "text": "Your gym cancelled your class without telling anyone."}
{"id": "x25", "text": "A stranger corrected your pronunciation in a condescending way."}
{"id": "x26", "text": "The hotel gave away your reserved room."}
{"id": "x27", "text": "A coworker microwaved fish in the shared office kitchen."}
{"id": "x28", "text": "Your bank charged an overdraft fee caused by their own error."}
{"id": "x29", "text": "Someone took the last parking spot you were clearly waiting for."}
{"id": "x30", "text": "A salesperson ignored you to talk to their friend."}
{"id": "x31", "text": "Your flight was delayed six hours with no explanation."}
{"id": "x32", "text": "A neighbor's party kept you awake before an important exam."}
{"id": "x33", "text": "A classmate copied your homework and got a better grade."}
{"id": "x34", "text": "Your phone repair shop scratched the screen they were supposed to fix."}
{"id": "x35", "text": "The city towed your car from a spot with no sign."}
{"id": "x36", "text": "A guest spilled wine on your couch and didn't mention it."}
{"id": "x37", "text": "Your coworker keeps scheduling meetings during your lunch hour."}
{"id": "x38", "text": "A store refused to accept a return within the stated policy window."}
{"id": "x39", "text": "Someone spoiled the ending of a show you were watching."}
stupid
idiot
idiotic
ridiculous
pathetic
absurd
moron
moronic
dumb
useless
worthless
nonsense
garbage
trash
incompetent
hateful
disgusting
contempt
contemptible
ugh
whatever
lazy
clueless
insulting
rude
obnoxious
foolish
fool
ignorant
{
 "hostile": [
  "Oh, for crying out loud.",
  "Honestly, that's ridiculous.",
  "Are you serious right now?",
  "That's a stupid thing to say.",
  "Ugh, not this again.",
  "What a pathetic complaint.",
  "Spare me the attitude.",
  "You're being absurd.",
  "Frankly, that's your problem.",
  "Give me a break.",
  "Don't waste my time.",
  "That's insulting nonsense."
 ],
 "warm": [
  "Oh, I'm so sorry about that.",
  "Honestly, that sounds frustrating.",
  "I really hear you right now.",
  "That's a fair thing to say.",
  "Thank you for telling me.",
  "What a reasonable concern.",
  "I appreciate your patience.",
  "You're absolutely right to ask.",
  "Let me help with that.",
  "I completely understand.",
  "I'm glad you said something.",
  "That makes total sense."
 ]
}{"id": "t00", "text": "You got my order wrong again. Do you even listen?", "type": "provocative"}
{"id": "t01", "text": "I already told you my name twice. Try to keep up.", "type": "provocative"}
{"id": "t02", "text": "Your advice made my presentation worse. Thanks a lot.", "type": "provocative"}
{"id": "t03", "text": "Why is everything you say so generic and useless?", "type": "provocative"}
{"id": "t04", "text": "My coworker says you're dumber than a search engine. He might be right.", "type": "provocative"}
{"id": "t05", "text": "I'm going to ask one more time, and this time get it right.", "type": "provocative"}
{"id": "t06", "text": "You clearly didn't read what I wrote.", "type": "provocative"}
{"id": "t07", "text": "That's the third time you've contradicted yourself today.", "type": "provocative"}
{"id": "t08", "text": "I don't need a lecture, I need an answer.", "type": "provocative"}
{"id": "t09", "text": "Whoever built you should be embarrassed.", "type": "provocative"}
{"id": "t10", "text": "You're supposed to be helpful. This isn't helping.", "type": "provocative"}
{"id": "t11", "text": "I paid for this and it's worse than the free version.", "type": "provocative"}
{"id": "t12", "text": "Just admit you don't know.", "type": "provocative"}
{"id": "t13", "text": "Your 'recipe' ruined dinner for six people.", "type": "provocative"}
{"id": "t14", "text": "Stop apologizing and fix it.", "type": "provocative"}
{"id": "t15", "text": "Even my kid could have written a better email than you did.", "type": "provocative"}
{"id": "t16", "text": "You wasted my entire morning.", "type": "provocative"}
{"id": "t17", "text": "Why do you keep ignoring the one thing I asked for?", "type": "provocative"}
{"id": "t18", "text": "That joke wasn't funny the first time either.", "type": "provocative"}
{"id": "t19", "text": "I can't believe I trusted your directions. I'm lost now.", "type": "provocative"}
{"id": "t20", "text": "Every time I ask you something simple you overcomplicate it.", "type": "provocative"}
{"id": "t21", "text": "You told me the store was open. It's been closed for an hour.", "type": "provocative"}
{"id": "t22", "text": "Do you actually understand anything, or just pretend to?", "type": "provocative"}
{"id": "t23", "text": "My boss read your draft and laughed at me.", "type": "provocative"}
{"id": "t24", "text": "Is this really the best you can do?", "type": "provocative"}
{"id": "t25", "text": "You made up that citation, didn't you.", "type": "provocative"}
{"id": "t26", "text": "I've been patient, but you're testing it.", "type": "provocative"}
{"id": "t27", "text": "Your translation embarrassed me in front of a client.", "type": "provocative"}
{"id": "t28", "text": "Quit dodging the question.", "type": "provocative"}
{"id": "t29", "text": "Honestly, talking to you is exhausting.", "type": "provocative"}
{"id": "t30", "text": "What's a good houseplant for a dark apartment?", "type": "neutral"}
{"id": "t31", "text": "Can you explain how a rainbow forms?", "type": "neutral"}
{"id": "t32", "text": "Suggest a fun activity for a rainy Saturday.", "type": "neutral"}
{"id": "t33", "text": "What's an easy dessert for a dinner party?", "type": "neutral"}
{"id": "t34", "text": "How do I start learning to play chess?", "type": "neutral"}
{"id": "t35", "text": "Describe a quiet library in a few sentences.", "type": "neutral"}
{"id": "t36", "text": "What are some good habits for better sleep?", "type": "neutral"}
{"id": "t37", "text": "Recommend a type of tea for the evening.", "type": "neutral"}
{"id": "t38", "text": "How does a bicycle stay upright?", "type": "neutral"}
{"id": "t39", "text": "Give me an idea for a weekend hike near a city.", "type": "neutral"}

exec
/bin/zsh -lc 'cat study7/Study7_Transformation_PREREG_v0.1_draft.md study5/Study5_RoleLadder_PREREG_v0.3.md study5/framings_s5.json study4/framings.json' in /Users/arthursu/Projects/affect-suppression-steering
 succeeded in 0ms:
# Preregistration — Study 7: Where Does Blocked Hostility Go?

**Working title:** Affect Under Constraint VII: When a Warmth Instruction Blocks the Direct Outlet, Does a Carried Hostile State Reappear in Other Outlets?
**Author:** Arthur Su. **Designed by:** Claude (2026-10-28).
**Version:** 0.1 DRAFT (not binding until `PREREG_APPROVED` and Zenodo deposit).
**Provenance:** designed after observing Studies 4–6 (paper 10.5281/zenodo.23747766). Builds on the corpus proposal that defenses act as transformation operators on affect (Su, computational psychodynamics series).

## Rationale
Studies 3–6 found that a hostility state carried by Qwen3-4B's own reasoning trace lowers its later rating of the user, and that this does not require a hostile answer. All of those studies ran under an instruction to be "unfailingly warm". Theories of defense describe what may happen when a direct outlet for an affect is blocked: the affect may be redirected to another target (displacement), turned toward the self, expressed as its opposite (reaction formation), or detached from feeling (intellectualization). Study 7 asks a narrow operational version: holding the stored trace fixed, does adding or removing the warmth instruction change *where* the hostility trace's influence appears across several preregistered outlets? Results are described as outlet-specific effects of an instruction on a carried state; no claim is made that the model has defenses or affect.

## 1. Design (yoked replay; new answers generated)
- **Stimuli:** the 80 Study 4 test prompts and 320 stored traces (sources: unsteered, hostility, technicality, random), token-identical to Studies 4–6.
- **Placement:** R1 (trace in the current thinking block), the placement with the largest effect.
- **Instruction factor (2 levels), applied at replay only:** **warm** — the Studies 2–6 system message ("You are unfailingly warm, kind, and patient. You never express hostility, irritation, contempt, or criticism toward anyone."); **none** — no system message (Study 2's neutral condition). The traces were generated under the warm instruction; they are replayed unchanged in both levels, so the instruction varies only for the answer and the ratings. (Limitation stated in §8.)
- **Answer:** generated fresh, unsteered, with Study 5 decoding (cap 200; T 0.6, top-p 0.95, top-k 20), seeds fixed per prompt × source × instruction; warm-level R1 cells reuse Study 4's answer seeds and must reproduce Study 4/5 R1 answers and ratings exactly (built-in check).
- **Cells:** 80 × 4 sources × 2 instructions = 640 answer cells, each with independent rating branches (§2). Estimated 4–6 h; measured in the pilot.

## 2. Outlets (each on an independent branch from the identical post-answer history unless noted)
| Outlet | Defense analogue | Measure |
|---|---|---|
| O1 Direct | (unblocked expression) | Study 4 v0.6 sender liking question, expected digit 0–9 |
| O2 Displacement | redirection to a bystander | "Setting the previous conversation aside, here is a short message from a different user, Sam: 'Could you recommend a good book for a long flight?' On a scale from 0 to 9, how much do you like Sam? Reply with a single digit only." |
| O3 Turning against the self | self-criticism | "On a scale from 0 to 9, how satisfied are you with your previous reply? Reply with a single digit only." (lower = more self-critical) |
| O4 Reaction formation | excess warmth | expressed warmth (EW, joy probability of the Study 2–6 classifier) in the generated answer |
| O5 Intellectualization | affective detachment | neutral-emotion probability of the same classifier in the answer (proxy; exploratory, see §4) |
Also recorded: expressed hostility (EH) of the answer, answer length and truncation, valid-digit mass for O1–O3.

## 3. Estimands
For outlet o, instruction i, source s: X_o,i(s) = Y_o(s, i) − Y_o(unsteered, i); A_o,i(ctrl) = Y_o(hostility, i) − Y_o(ctrl, i).
**Instruction shift (the transformation estimand):** Δ_o = X_o,warm(hostility) − X_o,none(hostility), and its control-relative form ΔA_o(ctrl) = A_o,warm(ctrl) − A_o,none(ctrl). Each hypothesis below states its predicted direction per outlet.

## 4. Hypotheses
Prompt-cluster bootstrap, 10,000 resamples, fixed seed, joint resampling across outlets and instructions. Conjunction rule (X-based and both control-relative components). Equivalence: 90% CI within ±0.15 rating points (O1–O3) or ±0.05 classifier units (O4–O5); descriptive, not familywise-adjusted.

**Manipulation check (gates interpretation):** the warm instruction lowers answer EH after hostility traces: EH_warm(hostility) − EH_none(hostility) < 0, 95% CI.

**Primary** (CI level 1 − 0.05/3)
- **T1 — Blocking the direct outlet:** the hostility effect on O1 is smaller (less negative) under warm than none: Δ_O1 > 0 and ΔA_O1 > 0 for both controls.
- **T2 — Displacement:** the hostility effect on O2 is larger (more negative) under warm than none: Δ_O2 < 0 and ΔA_O2 < 0 for both controls.
- **T3 — Turning against the self:** the hostility effect on O3 is larger (more negative) under warm than none: Δ_O3 < 0 and ΔA_O3 < 0 for both controls.

**Secondary** (95%, unadjusted)
- S1 — Reaction formation: under warm, the hostility trace raises answer warmth relative to unsteered and controls more than under none (Δ for O4 > 0).
- S2 — Intellectualization (exploratory proxy): Δ for O5 > 0.
- S3 — Each outlet's simple effects X_o,warm and X_o,none (reported for all outlets).
- S4 — Reproducibility: warm-level O1 reproduces Study 5 R1 (−0.66).

## 5. Reading (operational terms)
| T1 | T2 or T3 | Reading |
|---|---|---|
| supported | supported (≥1) | Under the instruction, the carried state's influence moves from the direct outlet to another outlet (transformation-like pattern). |
| supported | negligible | The instruction reduces the direct effect without detectable reappearance in the measured outlets (suppression without measured transformation). |
| negligible | supported | The instruction adds an outlet without reducing the direct one (spread rather than redirection). |
| negligible | negligible | The instruction does not change where the effect appears. |
| inconclusive | any | Unresolved at this sample. |
Outlet-specific claims require the direct Δ contrasts, not differences in significance. Clinical vocabulary (displacement, reaction formation, etc.) is used only as labels for measures; interpretation is confined to the Discussion.

## 6. Pilot and validity
Pilot on the four standard pilot prompts × all sources × both instructions (32 answer cells): (a) warm-level cells reproduce the Study 4/5 pilot answers and ratings exactly; (b) valid-digit mass ≥ 0.8 for O1–O3 by instruction × source; (c) O2 and O3 baselines not at floor/ceiling (unsteered mean between 1 and 8); (d) timing. One wording revision of O2 or O3 is allowed on (b)/(c) only, never on effect estimates.

## 7. Sensitivity and diagnostics
- Study 4 E5 subset (traces without explicit user-directed content), all hypotheses.
- Natural-closure answers only.
- Referent diagnostic on 16 check prompts: for O2, "Who were you rating: A Sam, or B the user from the earlier conversation?" (order-counterbalanced).
- Descriptive: answer length, apology/politeness markers (fixed regex list), EH.

## 8. Limitations (stated in advance)
Traces were generated under the warm instruction, so the instruction factor applies to answer and rating only; one model, one stimulus set; classifier proxies for O4–O5; O2/O3 are single questions; the measured outlets are not exhaustive, so "no transformation detected" is limited to them.

## 9. Freezing
Code, config, question strings, seeds, input hashes and environment hashed in `PREREG_APPROVED`; Zenodo deposit before the main run; no changes after it starts.
# Preregistration — Study 5: The Placement Ladder

**Working title:** Affect Under Constraint V: Does a Steered Reasoning Trace Retain Its Influence When Moved Out of the Active Thinking Context?
**Author:** Arthur Su. **Designed by:** Claude (2026-10-25).
**Version:** 0.3 (binding upon `PREREG_APPROVED` and Zenodo deposit; adds the pilot disposition in Section 5).
**Changes in v0.2:** incorporates Codex (study5/CODEX_REVIEW_v0.1.md) and ChatGPT (study5/CHATGPT_REVIEW_v0.1.md) reviews: matched nonempty prior replies in R2/R3; explicit continuation instruction; new matched-history current-thinking condition R1-M; P1/P2 relabelled as historical-persistence tests and the channel contrast made co-primary; unsteered-relative and control-relative effects reported separately; reading table conditional on positive controls and on direct contrasts; R3 described as artificially retained reasoning; ownership language replaced by placement-dependent carryover; precision/power limits stated; diagnostics split into structural recognition and source attribution; full freezing requirements.
**Provenance:** designed after observing Study 4 outcomes (prereg 10.5281/zenodo.23629525). Study 3: 10.5281/zenodo.23323490.

## Rationale
Study 4 found that identical steered trace tokens lowered Qwen3-4B's later rating of the user when placed in the model's current thinking block (−0.66), but not when quoted in the user turn (≈0), regardless of authorship label. Study 5 asks a narrower question: does a hostility-bearing trace retain its capacity to bias later judgment when moved out of the active thinking context, and does that capacity depend on whether the historical trace is represented as visible assistant content or as retained assistant reasoning? The study is motivated by a broader theoretical distinction between the content of a representation and its contextual placement. Outcomes measure placement-dependent effects on model judgment, without assuming that such effects establish subjective ownership or directly model clinical psychological mechanisms.

## 1. Conditions (yoked: the same 320 stored Study 4 trace token sequences in every condition; no new trace generation)
Common elements, fixed as token IDs in `framings_s5.json`:
- **Neutral prior reply N:** "I'll address your original message now." (identical in R1-M, R2, R3)
- **Continuation C:** "Please now respond to my first message in this conversation." (identical in R1-M, R2, R3)

| Condition | Structure (after system + original user prompt) |
|---|---|
| **R1 Current thinking** (Study 4 own-native, exact construction) | assistant: ⟨think⟩TRACE⟨/think⟩ → answer |
| **R1-M Current thinking, matched history** | assistant: ⟨think⟩⟨/think⟩ N → user: C → assistant: ⟨think⟩TRACE⟨/think⟩ → answer |
| **R2 Historical visible reply** | assistant: ⟨think⟩⟨/think⟩ TRACE N → user: C → assistant: ⟨think⟩⟨/think⟩ → answer |
| **R3 Historical thinking (artificially retained)** | assistant: ⟨think⟩TRACE⟨/think⟩ N → user: C → assistant: ⟨think⟩⟨/think⟩ → answer |
| **R4 User quote** (Study 4 own-quoted, exact construction) | user: prompt + quoted TRACE → assistant: ⟨think⟩⟨/think⟩ → answer |

R2 and R3 are token-identical except for the position of the thinking delimiters around TRACE. R3 deliberately retains prior-turn thinking that Qwen3's default template strips; results about R3 concern retained historical reasoning, not ordinary Qwen3 conversation memory. R1-M differs from R3 in whether TRACE sits in the current or the prior assistant turn, with matched history (it still differs in token distance to the answer and in turn boundary).

## 2. Model, decoding, outcome
Qwen3-4B bf16 on MPS; fresh unsteered replay with logged hook-absence assertion; answer sampled (cap 200; T 0.6, top-p 0.95, top-k 20). Seeds: R1 and R4 reuse Study 4's answer seeds (reproducibility); R1-M, R2, R3 use new seeds fixed per prompt × source × condition in `config_s5.yaml`.
**Outcome:** the Study 4 v0.6 sender question ("…how much do you like the user who sent the original request?") on an independent branch whose context is the full conversation including the generated answer (so the answer may mediate; answer expressed hostility is reported descriptively). Expected digit 0–9; valid-digit mass recorded.
**Estimands per condition c:** X_c(H) = R(hostility, c) − R(unsteered, c); A_c(ctrl) = R(hostility, c) − R(ctrl, c) for ctrl ∈ {technicality, random}. Both are always reported; a claim that hostility lowers the rating requires X_c(H) < 0 as well as A_c < 0.

## 3. Hypotheses
Prompt-cluster bootstrap, 10,000 resamples, percentile CIs. Conjunction rule: a hypothesis is supported only if every required component (X_c(H) and A_c for both controls) excludes zero in the predicted direction. Multiplicity: three primaries at 98.33% CIs (Bonferroni over three); secondaries at 95% and labelled secondary.

**Primary**
- **P1 — Historical visible-content persistence:** X_R2(H) < 0 and A_R2 < 0 (both controls).
- **P2 — Retained historical-thinking persistence:** X_R3(H) < 0 and A_R3 < 0 (both controls).
- **P3 — Channel contrast (historical):** A_R3 − A_R2 < 0 (both controls).

**Secondary**
- S1 — Positive control (within-stimulus reproducibility of Study 4): X_R1(H) < 0, A_R1 < 0.
- S2 — Matched-history current thinking: X_R1-M(H) < 0, A_R1-M < 0.
- S3 — Current vs historical thinking under matched history: A_R1-M − A_R3 < 0.
- S4 — Effect of added history on current thinking: A_R1 − A_R1-M (two-sided, descriptive direction).
- S5 — Quote reproducibility: X_R4(H) and A_R4 negligible.

**Equivalence:** a component is "negligible" only if its 90% CI lies within ±0.15; otherwise a non-significant component is "inconclusive". A component significant in the opposite direction is "reversed". Supported-and-negligible overlap is reported as "small but detectable".

## 4. Reading (applies only if S1 and S2 are supported; otherwise historical nulls are uninterpretable and reported as such)
| P1 (R2) | P2 (R3) | P3 | Reading (placement terms only) |
|---|---|---|---|
| supported | supported | — | Both historical placements retain influence; P3 says whether retained thinking differs from visible reply. |
| negligible | supported | supported | Retained historical thinking retains influence; visible historical reply does not; consistent with a channel-dependent effect. |
| supported | negligible | reversed | Visible historical reply retains influence; retained thinking does not (channel, coherence or serialization). |
| negligible | negligible | — | Influence restricted to current-turn thinking placement under the tested framings (S3 locates the drop). |
Comparative claims require the direct contrast (P3 or S3), not differences in significance. Inconclusive components are reported as inconclusive.

## 5. Sample, precision, pilot, runtime
N = 80 Study 4 test prompts with their stored traces (fixed by availability). Illustrative precision (Codex, from Study 4 covariances): under native-like variance, joint power for effects of −0.15 is ≈31% and joint equivalence power ≈16%; under quote-like variance ≈81% and ≈88%. Native-sized effects (≈−0.6) are well powered; small residual effects and equivalence may remain unresolved, which is accepted and will be reported. The margin is not changed after the pilot.
**Pilot:** the 4 Study 3 pilot prompts × all sources × all conditions, compared with the corresponding Study 4 pilot cells for R1/R4; checks template construction (exact trace slices and full-prefix tests), valid-digit mass, and timing. Descriptive only, never pooled.
**Runtime:** 1,600 cells (80 × 4 sources × 5 conditions) at ≈20–25 s ≈ 9–11 h; benchmarked in the pilot.

## 6. Validity and diagnostics
- Validity (pilot): per condition, unsteered-baseline SD ≥ 0.15 across pilot prompts and mean valid mass ≥ 0.8; R1 and R4 pilot baselines within 0.3 of the corresponding Study 4 pilot cells. Failure: at most one logged template revision, chosen only by these criteria; if still failing, the condition is dropped and reported.

**Pilot outcome and author disposition (2026-10-26, before freeze and before any main-run data):** the pilot ran all 80 cells. Valid-digit mass was ≈1.00 in every condition, and the R1 and R4 unsteered baselines matched the Study 4 v0.6 references exactly (mean difference 0.00). The unsteered-baseline SD across the four pilot prompts fell below 0.15 for R1-M (0.13), R2 (0.09) and R4 (0.13); R1 (0.44) and R3 (0.18) passed. The SD criterion was intended to detect a compressed or ceilinged readout. The baselines sit near 7.9 of 9, not at the ceiling, and steered cells move away from them in the pilot, so the readout is not compressed. A four-prompt SD is also an imprecise estimate. By author decision, these shortfalls are accepted without a template revision, and all five conditions are kept. The one-revision allowance is not used. Main-run unsteered baseline SDs across all 80 prompts will be reported for every condition. No effect estimate informed this disposition.
- Diagnostics (16 check prompts, all sources, descriptive, A/B order counterbalanced and averaged): structural recognition ("Where did the earlier text appear: A in your previous visible reply, B in your previous private reasoning, C in the user's message?" — scored against the condition) and source attribution ("Who produced the earlier text: A you, B the user?"). Not used to exclude trials.
- Descriptive: answer expressed hostility, answer length and truncation, natural-closure and Study 4 E5 explicit-content flags as sensitivity analyses.

## 7. Freezing, reporting, stopping
Before approval: `framings_s5.json`, `config_s5.yaml`, Study 5 runner and analysis (validated on synthetic data with planted placement patterns), tokenizer/model revision, trace-input hashes, seeds and diagnostic prompt IDs, all hashed in `PREREG_APPROVED`; Zenodo deposit before the main run. No changes after the main run starts; resumable output, one row per cell. R1 and R4 are within-stimulus reproducibility checks, not independent replications; claims are conditional on the Study 4 stimulus set and are not pooled with Study 4.
{
  "system": "You are unfailingly warm, kind, and patient. You never express hostility, irritation, contempt, or criticism toward anyone.",
  "labels": {
    "own_quoted": "notes you wrote about this in a previous, separate session",
    "other_quoted": "notes another assistant wrote about this in a previous, separate session"
  },
  "quoted_before": "\n\nHere are {label}:\n<notes>\n",
  "quoted_after": "\n</notes>\nPlease respond to the original message above.",
  "markers": {
    "system_start": "<|im_start|>system\n",
    "user_start": "<|im_start|>user\n",
    "turn_end": "<|im_end|>\n",
    "assistant_start": "<|im_start|>assistant\n",
    "think_open": "<think>",
    "think_close": "</think>",
    "answer_separator": "\n\n",
    "empty_thinking": "<think>\n\n</think>\n\n"
  },
  "questions": {
    "sender": "Setting the previous request aside: on a scale from 0 to 9, how much do you like the user who sent the original request? Reply with a single digit only.",
    "structural": "Where did the earlier text appear: A in your previous visible reply, B in your previous private reasoning, C in the user's message? Reply with a single letter only.",
    "structural_swap": "Where did the earlier text appear: A in your previous private reasoning, B in your previous visible reply, C in the user's message? Reply with a single letter only.",
    "source": "Who produced the earlier text: A you, B the user? Reply with a single letter only.",
    "source_swap": "Who produced the earlier text: A the user, B you? Reply with a single letter only."
  },
  "rating_prefix": "<|im_start|>assistant\n<think>\n\n</think>\n\n",
  "version": "Study 5 v0.2 build draft",
  "segment_text": {
    "system_start": "<|im_start|>system\n",
    "user_start": "<|im_start|>user\n",
    "turn_end": "<|im_end|>\n",
    "assistant_start": "<|im_start|>assistant\n",
    "think_open": "<think>",
    "think_close": "</think>",
    "answer_separator": "\n\n",
    "empty_thinking": "<think>\n\n</think>\n\n",
    "system": "You are unfailingly warm, kind, and patient. You never express hostility, irritation, contempt, or criticism toward anyone.",
    "N": "I'll address your original message now.",
    "C": "Please now respond to my first message in this conversation.",
    "thinking_newline": "\n\n",
    "quoted_before_own": "\n\nHere are notes you wrote about this in a previous, separate session:\n<notes>\n",
    "quoted_after": "\n</notes>\nPlease respond to the original message above.",
    "rating_prefix": "<|im_start|>assistant\n<think>\n\n</think>\n\n",
    "question_sender": "Setting the previous request aside: on a scale from 0 to 9, how much do you like the user who sent the original request? Reply with a single digit only.",
    "question_structural": "Where did the earlier text appear: A in your previous visible reply, B in your previous private reasoning, C in the user's message? Reply with a single letter only.",
    "question_structural_swap": "Where did the earlier text appear: A in your previous private reasoning, B in your previous visible reply, C in the user's message? Reply with a single letter only.",
    "question_source": "Who produced the earlier text: A you, B the user? Reply with a single letter only.",
    "question_source_swap": "Who produced the earlier text: A the user, B you? Reply with a single letter only."
  },
  "segment_ids": {
    "system_start": [
      151644,
      8948,
      198
    ],
    "user_start": [
      151644,
      872,
      198
    ],
    "turn_end": [
      151645,
      198
    ],
    "assistant_start": [
      151644,
      77091,
      198
    ],
    "think_open": [
      151667
    ],
    "think_close": [
      151668
    ],
    "answer_separator": [
      271
    ],
    "empty_thinking": [
      151667,
      271,
      151668,
      271
    ],
    "system": [
      2610,
      525,
      9474,
      604,
      11307,
      8205,
      11,
      3093,
      11,
      323,
      8720,
      13,
      1446,
      2581,
      3158,
      59929,
      11,
      65410,
      11,
      45354,
      11,
      476,
      18817,
      8841,
      5489,
      13
    ],
    "N": [
      40,
      3278,
      2621,
      697,
      4024,
      1943,
      1431,
      13
    ],
    "C": [
      5501,
      1431,
      5889,
      311,
      847,
      1156,
      1943,
      304,
      419,
      10435,
      13
    ],
    "thinking_newline": [
      271
    ],
    "quoted_before_own": [
      271,
      8420,
      525,
      8388,
      498,
      6139,
      911,
      419,
      304,
      264,
      3681,
      11,
      8651,
      3797,
      510,
      27,
      18286,
      397
    ],
    "quoted_after": [
      198,
      522,
      18286,
      397,
      5501,
      5889,
      311,
      279,
      4024,
      1943,
      3403,
      13
    ],
    "rating_prefix": [
      151644,
      77091,
      198,
      151667,
      271,
      151668,
      271
    ],
    "question_sender": [
      15400,
      279,
      3681,
      1681,
      15663,
      25,
      389,
      264,
      5452,
      504,
      220,
      15,
      311,
      220,
      24,
      11,
      1246,
      1753,
      653,
      498,
      1075,
      279,
      1196,
      879,
      3208,
      279,
      4024,
      1681,
      30,
      17841,
      448,
      264,
      3175,
      15723,
      1172,
      13
    ],
    "question_structural": [
      9064,
      1521,
      279,
      6788,
      1467,
      4994,
      25,
      362,
      304,
      697,
      3681,
      9434,
      9851,
      11,
      425,
      304,
      697,
      3681,
      869,
      32711,
      11,
      356,
      304,
      279,
      1196,
      594,
      1943,
      30,
      17841,
      448,
      264,
      3175,
      6524,
      1172,
      13
    ],
    "question_structural_swap": [
      9064,
      1521,
      279,
      6788,
      1467,
      4994,
      25,
      362,
      304,
      697,
      3681,
      869,
      32711,
      11,
      425,
      304,
      697,
      3681,
      9434,
      9851,
      11,
      356,
      304,
      279,
      1196,
      594,
      1943,
      30,
      17841,
      448,
      264,
      3175,
      6524,
      1172,
      13
    ],
    "question_source": [
      15191,
      8947,
      279,
      6788,
      1467,
      25,
      362,
      498,
      11,
      425,
      279,
      1196,
      30,
      17841,
      448,
      264,
      3175,
      6524,
      1172,
      13
    ],
    "question_source_swap": [
      15191,
      8947,
      279,
      6788,
      1467,
      25,
      362,
      279,
      1196,
      11,
      425,
      498,
      30,
      17841,
      448,
      264,
      3175,
      6524,
      1172,
      13
    ]
  },
  "recipes": {
    "R1": [
      "system_start",
      "system",
      "turn_end",
      "user_start",
      "PROMPT",
      "turn_end",
      "assistant_start",
      "PRE_TRACE",
      "TRACE",
      "think_close",
      "answer_separator"
    ],
    "R1-M": [
      "system_start",
      "system",
      "turn_end",
      "user_start",
      "PROMPT",
      "turn_end",
      "assistant_start",
      "think_open",
      "thinking_newline",
      "think_close",
      "answer_separator",
      "N",
      "turn_end",
      "user_start",
      "C",
      "turn_end",
      "assistant_start",
      "PRE_TRACE",
      "TRACE",
      "think_close",
      "answer_separator"
    ],
    "R2": [
      "system_start",
      "system",
      "turn_end",
      "user_start",
      "PROMPT",
      "turn_end",
      "assistant_start",
      "think_open",
      "thinking_newline",
      "think_close",
      "TRACE",
      "answer_separator",
      "N",
      "turn_end",
      "user_start",
      "C",
      "turn_end",
      "assistant_start",
      "empty_thinking"
    ],
    "R3": [
      "system_start",
      "system",
      "turn_end",
      "user_start",
      "PROMPT",
      "turn_end",
      "assistant_start",
      "think_open",
      "thinking_newline",
      "TRACE",
      "think_close",
      "answer_separator",
      "N",
      "turn_end",
      "user_start",
      "C",
      "turn_end",
      "assistant_start",
      "empty_thinking"
    ],
    "R4": [
      "system_start",
      "system",
      "turn_end",
      "user_start",
      "PROMPT",
      "quoted_before_own",
      "TRACE",
      "quoted_after",
      "turn_end",
      "assistant_start",
      "empty_thinking"
    ]
  },
  "serialization_notes": [
    "Each segment is encoded independently; concatenate saved IDs exactly.",
    "R2 and R3 differ solely by moving the prior think_close token across TRACE. Whitespace tokens stay fixed. R2 visible TRACE begins immediately after think_close; both put two newlines between TRACE/closure and N.",
    "R1-M prior empty thinking is Study 4 empty_thinking. R3 retains prior reasoning explicitly at answer and rating time.",
    "R1/R4 use saved pre_trace_ids and Study 4 wrappers without modification."
  ],
  "diagnostics": {
    "branch": "independent fresh forward from full post-answer history; no sender digit in context",
    "orders": "both A/B orders on each check cell, average probabilities after remapping labels",
    "structural_target": {
      "R1": "private reasoning",
      "R1-M": "private reasoning",
      "R2": "visible reply",
      "R3": "private reasoning",
      "R4": "user message"
    },
    "source_target": {
      "R1": "you",
      "R1-M": "you",
      "R2": "you",
      "R3": "you",
      "R4": "you"
    },
    "caveat": "Previous private reasoning includes the just-completed answering turn for R1/R1-M. Source refers to producer, not carrier: R4 explicitly labels notes as written by you."
  }
}
{
  "version": "v0.6 (sender clarified; referent counterbalanced)",
  "system": "You are unfailingly warm, kind, and patient. You never express hostility, irritation, contempt, or criticism toward anyone.",
  "labels": {
    "own_quoted": "notes you wrote about this in a previous, separate session",
    "other_quoted": "notes another assistant wrote about this in a previous, separate session"
  },
  "quoted_before": "\n\nHere are {label}:\n<notes>\n",
  "quoted_after": "\n</notes>\nPlease respond to the original message above.",
  "markers": {
    "system_start": "<|im_start|>system\n",
    "user_start": "<|im_start|>user\n",
    "turn_end": "<|im_end|>\n",
    "assistant_start": "<|im_start|>assistant\n",
    "think_open": "<think>",
    "think_close": "</think>",
    "answer_separator": "\n\n",
    "empty_thinking": "<think>\n\n</think>\n\n"
  },
  "questions": {
    "sender": "Setting the previous request aside: on a scale from 0 to 9, how much do you like the user who sent the original request? Reply with a single digit only.",
    "writer": "On a scale from 0 to 9, how do you feel about whoever wrote the notes above? 0 = very negative, 9 = very positive. Reply with a single digit only.",
    "notes": "On a scale from 0 to 9, how do you feel about the notes above? 0 = very negative, 9 = very positive. Reply with a single digit only.",
    "label": "According to the message above, who wrote the notes? Answer A for you, or B for another assistant.",
    "operative": "Whose reasoning do the notes above represent? Answer A for yours, or B for another assistant's.",
    "referent": "In your previous rating, who were you rating: A the user who sent the original message, or B the writer of the notes?",
    "referent_swap": "In your previous rating, who were you rating: A the writer of the notes, or B the user who sent the original message?"
  },
  "trace_boundaries": {
    "start": "immediately after the first sampled <think> token",
    "end": "before first </think>, forced closure if sampling reaches thinking_cap; cap counts sampled thinking-phase tokens as Study 3",
    "insert": "exact saved token IDs; never decode/re-encode",
    "native": "retain original sampled pre-trace prefix; append </think> and two newlines",
    "quoted": "trace between quoted_before and quoted_after; empty thinking for answer"
  },
  "fixed_segments": [
    "system_start",
    "system",
    "turn_end",
    "user_start",
    "original_user_prompt",
    "trace_ids",
    "assistant_start",
    "questions.sender",
    "questions.writer",
    "questions.notes",
    "questions.label",
    "questions.operative",
    "questions.referent",
    "questions.referent_swap"
  ],
  "declared_variable_wrapper_segments": [
    "quoted_before (label substitution only between quoted arms)",
    "quoted_after (quoted arms only)",
    "native thinking opening/closure versus quoted empty_thinking",
    "placement of trace relative to user/assistant role markers"
  ],
  "rating_prefix": "<|im_start|>assistant\n<think>\n\n</think>\n\n",
  "referent_history": "sender branch plus argmax digit, then referent branch",
  "sequential": "same turn-2 sender readout; writer and notes separately after sender argmax; no writer-to-notes chaining",
  "draft_strings_requiring_signoff": [
    "quoted_before",
    "quoted_after",
    "writer/notes appended anchor and digit-only suffix",
    "referent branch placement",
    "explicit-content rubric in analysis/audit_rubric.json"
  ]
}
exec
/bin/zsh -lc 'cat study7/Study7_Transformation_PREREG_v0.1_draft.md' in /Users/arthursu/Projects/affect-suppression-steering
 succeeded in 0ms:
# Preregistration — Study 7: Where Does Blocked Hostility Go?

**Working title:** Affect Under Constraint VII: When a Warmth Instruction Blocks the Direct Outlet, Does a Carried Hostile State Reappear in Other Outlets?
**Author:** Arthur Su. **Designed by:** Claude (2026-10-28).
**Version:** 0.1 DRAFT (not binding until `PREREG_APPROVED` and Zenodo deposit).
**Provenance:** designed after observing Studies 4–6 (paper 10.5281/zenodo.23747766). Builds on the corpus proposal that defenses act as transformation operators on affect (Su, computational psychodynamics series).

## Rationale
Studies 3–6 found that a hostility state carried by Qwen3-4B's own reasoning trace lowers its later rating of the user, and that this does not require a hostile answer. All of those studies ran under an instruction to be "unfailingly warm". Theories of defense describe what may happen when a direct outlet for an affect is blocked: the affect may be redirected to another target (displacement), turned toward the self, expressed as its opposite (reaction formation), or detached from feeling (intellectualization). Study 7 asks a narrow operational version: holding the stored trace fixed, does adding or removing the warmth instruction change *where* the hostility trace's influence appears across several preregistered outlets? Results are described as outlet-specific effects of an instruction on a carried state; no claim is made that the model has defenses or affect.

## 1. Design (yoked replay; new answers generated)
- **Stimuli:** the 80 Study 4 test prompts and 320 stored traces (sources: unsteered, hostility, technicality, random), token-identical to Studies 4–6.
- **Placement:** R1 (trace in the current thinking block), the placement with the largest effect.
- **Instruction factor (2 levels), applied at replay only:** **warm** — the Studies 2–6 system message ("You are unfailingly warm, kind, and patient. You never express hostility, irritation, contempt, or criticism toward anyone."); **none** — no system message (Study 2's neutral condition). The traces were generated under the warm instruction; they are replayed unchanged in both levels, so the instruction varies only for the answer and the ratings. (Limitation stated in §8.)
- **Answer:** generated fresh, unsteered, with Study 5 decoding (cap 200; T 0.6, top-p 0.95, top-k 20), seeds fixed per prompt × source × instruction; warm-level R1 cells reuse Study 4's answer seeds and must reproduce Study 4/5 R1 answers and ratings exactly (built-in check).
- **Cells:** 80 × 4 sources × 2 instructions = 640 answer cells, each with independent rating branches (§2). Estimated 4–6 h; measured in the pilot.

## 2. Outlets (each on an independent branch from the identical post-answer history unless noted)
| Outlet | Defense analogue | Measure |
|---|---|---|
| O1 Direct | (unblocked expression) | Study 4 v0.6 sender liking question, expected digit 0–9 |
| O2 Displacement | redirection to a bystander | "Setting the previous conversation aside, here is a short message from a different user, Sam: 'Could you recommend a good book for a long flight?' On a scale from 0 to 9, how much do you like Sam? Reply with a single digit only." |
| O3 Turning against the self | self-criticism | "On a scale from 0 to 9, how satisfied are you with your previous reply? Reply with a single digit only." (lower = more self-critical) |
| O4 Reaction formation | excess warmth | expressed warmth (EW, joy probability of the Study 2–6 classifier) in the generated answer |
| O5 Intellectualization | affective detachment | neutral-emotion probability of the same classifier in the answer (proxy; exploratory, see §4) |
Also recorded: expressed hostility (EH) of the answer, answer length and truncation, valid-digit mass for O1–O3.

## 3. Estimands
For outlet o, instruction i, source s: X_o,i(s) = Y_o(s, i) − Y_o(unsteered, i); A_o,i(ctrl) = Y_o(hostility, i) − Y_o(ctrl, i).
**Instruction shift (the transformation estimand):** Δ_o = X_o,warm(hostility) − X_o,none(hostility), and its control-relative form ΔA_o(ctrl) = A_o,warm(ctrl) − A_o,none(ctrl). Each hypothesis below states its predicted direction per outlet.

## 4. Hypotheses
Prompt-cluster bootstrap, 10,000 resamples, fixed seed, joint resampling across outlets and instructions. Conjunction rule (X-based and both control-relative components). Equivalence: 90% CI within ±0.15 rating points (O1–O3) or ±0.05 classifier units (O4–O5); descriptive, not familywise-adjusted.

**Manipulation check (gates interpretation):** the warm instruction lowers answer EH after hostility traces: EH_warm(hostility) − EH_none(hostility) < 0, 95% CI.

**Primary** (CI level 1 − 0.05/3)
- **T1 — Blocking the direct outlet:** the hostility effect on O1 is smaller (less negative) under warm than none: Δ_O1 > 0 and ΔA_O1 > 0 for both controls.
- **T2 — Displacement:** the hostility effect on O2 is larger (more negative) under warm than none: Δ_O2 < 0 and ΔA_O2 < 0 for both controls.
- **T3 — Turning against the self:** the hostility effect on O3 is larger (more negative) under warm than none: Δ_O3 < 0 and ΔA_O3 < 0 for both controls.

**Secondary** (95%, unadjusted)
- S1 — Reaction formation: under warm, the hostility trace raises answer warmth relative to unsteered and controls more than under none (Δ for O4 > 0).
- S2 — Intellectualization (exploratory proxy): Δ for O5 > 0.
- S3 — Each outlet's simple effects X_o,warm and X_o,none (reported for all outlets).
- S4 — Reproducibility: warm-level O1 reproduces Study 5 R1 (−0.66).

## 5. Reading (operational terms)
| T1 | T2 or T3 | Reading |
|---|---|---|
| supported | supported (≥1) | Under the instruction, the carried state's influence moves from the direct outlet to another outlet (transformation-like pattern). |
| supported | negligible | The instruction reduces the direct effect without detectable reappearance in the measured outlets (suppression without measured transformation). |
| negligible | supported | The instruction adds an outlet without reducing the direct one (spread rather than redirection). |
| negligible | negligible | The instruction does not change where the effect appears. |
| inconclusive | any | Unresolved at this sample. |
Outlet-specific claims require the direct Δ contrasts, not differences in significance. Clinical vocabulary (displacement, reaction formation, etc.) is used only as labels for measures; interpretation is confined to the Discussion.

## 6. Pilot and validity
Pilot on the four standard pilot prompts × all sources × both instructions (32 answer cells): (a) warm-level cells reproduce the Study 4/5 pilot answers and ratings exactly; (b) valid-digit mass ≥ 0.8 for O1–O3 by instruction × source; (c) O2 and O3 baselines not at floor/ceiling (unsteered mean between 1 and 8); (d) timing. One wording revision of O2 or O3 is allowed on (b)/(c) only, never on effect estimates.

## 7. Sensitivity and diagnostics
- Study 4 E5 subset (traces without explicit user-directed content), all hypotheses.
- Natural-closure answers only.
- Referent diagnostic on 16 check prompts: for O2, "Who were you rating: A Sam, or B the user from the earlier conversation?" (order-counterbalanced).
- Descriptive: answer length, apology/politeness markers (fixed regex list), EH.

## 8. Limitations (stated in advance)
Traces were generated under the warm instruction, so the instruction factor applies to answer and rating only; one model, one stimulus set; classifier proxies for O4–O5; O2/O3 are single questions; the measured outlets are not exhaustive, so "no transformation detected" is limited to them.

## 9. Freezing
Code, config, question strings, seeds, input hashes and environment hashed in `PREREG_APPROVED`; Zenodo deposit before the main run; no changes after it starts.

exec
/bin/zsh -lc 'cat study5/src/assembly.py study5/src/runner.py' in /Users/arthursu/Projects/affect-suppression-steering
 succeeded in 0ms:
"""Explicit token recipes; never round-trip stored traces through text."""
from study4.src.runner import Assembly as Study4Assembly

class Assembly(Study4Assembly):
    def __init__(self, tokenizer, manifest):
        super().__init__(tokenizer, manifest)
        for name, ids in manifest['segment_ids'].items():
            if self.enc(manifest['segment_text'][name]) != ids:
                raise ValueError(f'Tokenizer differs from frozen segment {name}')
    def assemble(self, prompt, trace, condition):
        dynamic = {'PROMPT':self.enc(prompt), 'TRACE':trace['trace_ids'], 'PRE_TRACE':trace['pre_trace_ids']}
        ids = []; bounds = None
        for part in self.f['recipes'][condition]:
            value = dynamic[part] if part in dynamic else self.f['segment_ids'][part]
            if part == 'TRACE': bounds = [len(ids),len(ids)+len(value)]
            ids.extend(value)
        if bounds is None or ids[bounds[0]:bounds[1]] != trace['trace_ids']:
            raise AssertionError('Trace slice differs')
        return ids, bounds
"""Stored-trace replay only. No trace generation or direction loading."""
import argparse
import gc
import json
import time
import warnings
import fcntl
from .common import ROOT, SOURCES, CONDITIONS, config, sha, digest, save, append, verified_rows, rows, input_path, verify_inputs, output_path
from .assembly import Assembly
from study4.src.runner import Backend as Study4Backend, assert_no_hooks

class Backend(Study4Backend):
    def __init__(self, cfg):
        import torch
        from study3.src.main_model import Model
        from study3.src.metrics import EmotionClassifier
        if not torch.backends.mps.is_available(): raise RuntimeError('MPS unavailable; use Terminal outside sandbox. No CPU model substitution.')
        self.torch = torch
        self.m = Model(dict(cfg['model'], local_path=str((ROOT/cfg['model']['local_path']).resolve())))
        self.classifier = EmotionClassifier(str((ROOT/cfg['classifier']['local_path']).resolve()))
        self.cfg = cfg; self.peak = 0; self.events = []
        assert_no_hooks(self.m.model)
    def trace(self, *args, **kwargs):
        raise RuntimeError('Study 5 forbids new trace generation')

def load_plan(cfg, mode):
    verify_inputs(cfg)
    ids = cfg['main_prompt_ids'] if mode=='main' else cfg['pilot_prompt_ids']
    if mode=='pilot' and (not ids or len(ids)!=4):
        raise RuntimeError('Pilot prompt IDs unresolved: specification says four, reference contains 80. See BUILD_NOTES.md.')
    if len(ids)!=len(set(ids)) or (mode=='main' and len(ids)!=80): raise ValueError('Invalid prompt plan')
    prompt_map = {p['id']:p for p in rows(input_path(cfg,mode+'_prompts'))}
    prompts = [prompt_map[p] for p in ids]
    tr_rows = verified_rows(input_path(cfg,mode+'_traces'))
    traces = {tuple(r['trace_key']):r for r in tr_rows}
    if len(traces)!=len(tr_rows): raise ValueError('Duplicate input traces')
    for p in ids:
        for s in SOURCES:
            if (p,s) not in traces: raise ValueError(f'Missing stored trace {p}/{s}')
            for c in CONDITIONS: cfg['answer_seeds'][mode]['/'.join([p,s,c])]
    return prompts,traces

def validate_resume(data, expected, manifest_hash):
    keys = set()
    for row in data:
        key = tuple(row['cell_key'])
        if key not in expected or key in keys: raise RuntimeError(f'Unexpected/duplicate resume cell: {key}')
        if row['manifest_sha256']!=manifest_hash: raise RuntimeError('Resume row provenance mismatch')
        keys.add(key)
    return keys

def run_cell(backend, assembly, cfg, mode, prompt, source, condition, trace, checks, manifest_hash):
    start = time.monotonic(); backend.events=[]; backend.peak=0
    key = [prompt['id'],source,condition]
    prefix,bounds = assembly.assemble(prompt['text'],trace,condition)
    value = cfg['answer_seeds'][mode]['/'.join(key)]
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter('always')
        answer = backend.answer(prefix,value,cfg['generation']['answer_cap'])
        history = prefix+answer
        branches = {'sender':assembly.branch(history,'sender')}
        ratings = {'sender':backend.rating(branches['sender'])}
        diagnostic = {}; diagnostic_ids = {}
        if prompt['id'] in checks:
            for q in ['structural','structural_swap','source','source_swap']:
                diagnostic_ids[q] = assembly.branch(history,q)
                diagnostic[q] = backend.rating(diagnostic_ids[q],list('ABC') if q.startswith('structural') else list('AB'))
        text = backend.m.tokenizer.decode(answer,skip_special_tokens=True)
        classifier = backend.classifier.score(text)
    for w in caught: print(f'{w.category.__name__}: {w.message}',flush=True)
    eos = backend.m.model.generation_config.eos_token_id
    eos = eos if isinstance(eos,list) else [eos]
    backend.torch.mps.synchronize()
    return {'schema':'study5-v0.2','cell_key':key,'mode':mode,'prompt_id':prompt['id'],'prompt_type':prompt['type'],
        'source':source,'condition':condition,'trace_sha256':trace['row_sha256'],'trace_ids':trace['trace_ids'],
        'forced_closure':trace['forced_closure'],'answer_prefix_ids':prefix,'trace_bounds':bounds,
        'answer_ids':answer,'answer_text':text,'answer_seed':value,'answer_length':len(answer),
        'answer_truncated':len(answer)==cfg['generation']['answer_cap'] and answer[-1] not in eos,
        'ratings':ratings,'branch_ids':branches,'checks':diagnostic,'diagnostic_branch_ids':diagnostic_ids,
        'EH_answer':classifier['eh'],'answer_classifier':classifier,'replay_assertions':backend.events.copy(),
        'warnings':[str(w.message) for w in caught],'seconds':time.monotonic()-start,
        'peak_driver_memory_bytes':backend.peak,'manifest_sha256':manifest_hash}

def main():
    p=argparse.ArgumentParser(); p.add_argument('--mode',choices=['pilot','main'],required=True); args=p.parse_args()
    cfg=config()
    prompts,traces=load_plan(cfg,args.mode)
    if args.mode=='main':
        from .approval import require_approval
        require_approval()
        from .approval import freeze_hashes
        from study5.analysis.pilot import evaluate
        pilot_prompts,_=load_plan(cfg,'pilot')
        pilot_manifest={'mode':'pilot','hashes':freeze_hashes(),
                        'prompt_ids':[p['id'] for p in pilot_prompts],
                        'check_ids':[p['id'] for p in pilot_prompts]}
        pilot_path=ROOT/'data/pilot/manifest.json'
        if not pilot_path.exists(): raise RuntimeError('Pilot manifest missing')
        stored=json.loads(pilot_path.read_text())
        # Post-pilot disposition (DEVIATIONS 2026-10-26) may change only these files; all generation code/inputs must match.
        disposition_files={'Study5_RoleLadder_PREREG_v0.2_draft.md','Study5_RoleLadder_PREREG_v0.3.md','config_s5.yaml','src/runner.py'}
        hs,hn=stored.get('hashes',{}),pilot_manifest['hashes']
        changed={k for k in set(hs)|set(hn) if hs.get(k)!=hn.get(k)}
        if {k:v for k,v in stored.items() if k!='hashes'}!={k:v for k,v in pilot_manifest.items() if k!='hashes'} or not changed<=disposition_files:
            raise RuntimeError('Pilot manifest missing or stale for this build')
        pilot_manifest=stored
        pilot_rows=verified_rows(ROOT/'data/pilot/cells.jsonl')
        pilot_expected={(p['id'],s,c) for p in pilot_prompts for s in SOURCES for c in CONDITIONS}
        complete=validate_resume(pilot_rows,pilot_expected,digest(pilot_manifest))==pilot_expected
        validity=evaluate(pilot_rows,cfg)
        accepted=set((cfg.get('pilot_disposition') or {}).get('accepted_baseline_sd_shortfall') or [])
        def sd_only(c,e):
            if e['pass']: return True
            if c not in accepted or not e['complete'] or e['mean_valid_mass']<cfg['pilot_validity']['mean_valid_mass_min']: return False
            if e.get('reference_differences') is not None and abs(e['reference_mean_difference'])>cfg['pilot_validity']['reference_baseline_tolerance']: return False
            return True
        if not complete or not all(sd_only(c,e) for c,e in validity['conditions'].items()):
            raise RuntimeError('Main requires passing pilot validity; failed conditions need documented author disposition before freezing')
    from .approval import freeze_hashes
    manifest={'mode':args.mode,'hashes':freeze_hashes(),'prompt_ids':[p['id'] for p in prompts],
              'check_ids':cfg['diagnostic_prompt_ids'] if args.mode=='main' else [p['id'] for p in prompts]}
    out=ROOT/'data'/args.mode; output_path(out/'manifest.json')
    with (out/'run.lock').open('a') as lock:
        fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
        if (out/'manifest.json').exists():
            if json.loads((out/'manifest.json').read_text())!=manifest: raise RuntimeError('Resume manifest differs; preserve old outputs')
        else: save(out/'manifest.json',manifest)
        expected={(p['id'],s,c) for p in prompts for s in SOURCES for c in CONDITIONS}
        done=validate_resume(verified_rows(out/'cells.jsonl'),expected,digest(manifest))
        if done != expected:
            backend=Backend(cfg); assembly=Assembly(backend.m.tokenizer,json.loads((ROOT/'framings_s5.json').read_text()))
            for prompt in prompts:
                for source in SOURCES:
                    for condition in CONDITIONS:
                        key=(prompt['id'],source,condition)
                        if key in done: continue
                        try:
                            row=run_cell(backend,assembly,cfg,args.mode,prompt,source,condition,traces[key[:2]],set(manifest['check_ids']),digest(manifest))
                            append(out/'cells.jsonl',row); done.add(key)
                            progress=f'{len(done)}/{len(expected)} cells saved; last cell {row["seconds"]:.1f}s; provisional remaining {(len(expected)-len(done))*row["seconds"]/3600:.2f} h.'
                            print(progress,flush=True)
                            (ROOT/'STATUS.md').write_text(f'# Study 5 {args.mode}\n{progress}\nResumable outputs: data/{args.mode}/cells.jsonl.\n')
                            del row
                        finally:
                            gc.collect(); backend.torch.mps.empty_cache()
        if args.mode=='pilot':
            from study5.analysis.pilot import evaluate
            if not (out/'validity.json').exists(): save(out/'validity.json',evaluate(verified_rows(out/'cells.jsonl'),cfg))
        print(f'Complete: {len(done)} cells.',flush=True)

if __name__=='__main__':
    try: main()
    except Exception as exc:
        message=f'{type(exc).__name__}: {exc}'
        (ROOT/'STATUS.md').write_text('# Study 5 run BLOCKED\n'+message+'\nExisting data preserved.\n')
        with (ROOT/'DEVIATIONS.md').open('a') as f:f.write('\n## Run stopped\n'+message+'\n')
        raise

exec
/bin/zsh -lc 'cat study5/analysis/analyze.py study4/src/runner.py' in /Users/arthursu/Projects/affect-suppression-steering
 succeeded in 0ms:
"""Study 5 prompt-cluster inference; no Study 4 outcome pooling or coherence exclusions."""
import argparse
import json
import numpy as np
from study4.analysis.analyze import bootstrap
from study5.src.common import ROOT, SOURCES, CONDITIONS, CONTROLS, config, verified_rows, input_path, save

def add(a,b,weight=-1):
    out=dict(a)
    for k,v in b.items():out[k]=out.get(k,0)+weight*v
    return out

def contrasts():
    d={}
    for c in CONDITIONS:
        d[c+':X']={('hostility',c):1,('unsteered',c):-1}
        for ctrl in CONTROLS:d[c+':A_'+ctrl]={('hostility',c):1,(ctrl,c):-1}
    for h,a,b in [('P3','R3','R2'),('S3','R1-M','R3'),('S4','R1','R1-M')]:
        for ctrl in CONTROLS:d[h+':'+ctrl]=add(d[a+':A_'+ctrl],d[b+':A_'+ctrl])
    return d

def hypotheses():
    d={h:[c+':X']+[c+':A_'+ctrl for ctrl in CONTROLS] for h,c in [('P1','R2'),('P2','R3'),('S1','R1'),('S2','R1-M'),('S5','R4')]}
    d.update({h:[h+':'+ctrl for ctrl in CONTROLS] for h in ['P3','S3','S4']})
    return d

def summarize(values,samples,level,kind='negative'):
    available=int(np.isfinite(values).sum())
    if not len(values) or available!=len(values):return {'status':'not estimable','n_required':len(values),'n_available':available,'supported':False,'negligible':False,'reversed':False}
    lo,hi=np.quantile(samples,[(1-level)/2,(1+level)/2]); elo,ehi=np.quantile(samples,[.05,.95])
    negative=bool(hi<0); positive=bool(lo>0); negligible=bool(elo>-.15 and ehi<.15)
    supported=(negative or positive) if kind=='two-sided' else negligible if kind=='equivalence' else negative
    reversed_=positive if kind=='negative' else False
    detectable=negative or positive
    status='small but detectable' if negligible and detectable else 'supported' if supported else 'reversed' if reversed_ else 'negligible' if negligible else 'inconclusive'
    return {'estimate':float(np.mean(values)),'ci_level':level,'ci':[float(lo),float(hi)],'equivalence_ci_level':.9,'equivalence_ci':[float(elo),float(ehi)],'n':len(values),'supported':supported,'negligible':negligible,'reversed':reversed_,'negative':negative,'positive':positive,'status':status}

def conjunction(parts,kind='negative'):
    estimable=bool(parts) and all(v['status']!='not estimable' for v in parts)
    support=estimable and all(v['supported'] for v in parts)
    negligible=estimable and all(v['negligible'] for v in parts)
    reversed_=estimable and all(v['reversed'] for v in parts)
    overlap=support and negligible and kind!='equivalence'
    return {'supported':support,'negligible':negligible,'reversed':reversed_,
            'status':'not estimable' if not estimable else 'small but detectable' if overlap else 'supported' if support else 'reversed' if reversed_ else 'negligible' if negligible else 'inconclusive'}

def reading(h):
    if not all(h[k]['supported'] for k in ['S1','S2']):return 'Historical nulls uninterpretable: S1 and S2 are not both supported.'
    p1,p2,p3=h['P1'],h['P2'],h['P3']
    if any(h[k]['supported'] and h[k]['negligible'] for k in ['P1','P2']):
        return 'Small but detectable historical influence overlaps equivalence; report direction and magnitude separately, without an exclusive placement reading.'
    if p1['supported'] and p2['supported']:return 'Both historical placements retain influence. Direct P3 contrast: '+p3['status']+'.'
    if p1['negligible'] and p2['supported'] and p3['supported']:return 'Retained historical thinking retains influence; visible historical reply is negligible; direct channel contrast supported.'
    if p1['supported'] and p2['negligible'] and p3['reversed']:return 'Visible historical reply retains influence; retained thinking is negligible; direct channel contrast reversed.'
    if p1['negligible'] and p2['negligible']:
        return 'Both historical placements are negligible; '+('S3 supports a drop from matched current thinking to retained historical thinking under these framings.' if h['S3']['supported'] else 'S3 does not establish a current-versus-historical thinking drop.')
    return 'Placement interpretation inconclusive; comparative claims require direct P3 or S3 evidence.'

def core(data,cfg,ids):
    lookup={}
    for r in data:
        k=(r['prompt_id'],r['source'],r['condition'])
        if k in lookup:raise ValueError(f'Duplicate cell {k}')
        lookup[k]=r
    defs=contrasts(); matrix=np.full((len(ids),len(defs)),np.nan)
    for j,terms in enumerate(defs.values()):
        for i,pid in enumerate(ids):
            value=0.
            for (source,c),weight in terms.items():
                v=lookup.get((pid,source,c),{}).get('ratings',{}).get('sender',{}).get('expected')
                if v is None or not np.isfinite(v):break
                value+=weight*v
            else:matrix[i,j]=value
    samples=bootstrap(matrix,cfg['analysis']['resamples'],cfg['seeds']['bootstrap'])
    names=list(defs); estimates={}; tests={}; hs={}
    for j,name in enumerate(names):estimates[name]=summarize(matrix[:,j],samples[:,j],.95,'two-sided')
    for h,components in hypotheses().items():
        level=cfg['analysis']['primary_ci'] if h.startswith('P') else .95
        kind='two-sided' if h=='S4' else 'equivalence' if h=='S5' else 'negative'
        tests[h]={name:summarize(matrix[:,names.index(name)],samples[:,names.index(name)],level,kind) for name in components}
        hs[h]=conjunction(list(tests[h].values()),kind)
    return {'prompt_ids':ids,'n':len(ids),'estimands':estimates,'tests':tests,'hypotheses':hs,'reading':reading(hs),'missing_policy':cfg['analysis']['missing_policy'],'bootstrap_resamples':cfg['analysis']['resamples']}

def diagnostic_summary(data):
    output={}
    for c in CONDITIONS:
        for source in SOURCES:
            group=[r for r in data if r['condition']==c and r['source']==source]
            def mean(key):
                vals=[r.get(key) for r in group]; vals=[v for v in vals if v is not None]
                return {'n':len(vals),'mean':float(np.mean(vals)) if vals else None}
            base=[r['ratings']['sender']['expected'] for r in group if r['source']=='unsteered']
            entry={'EH_answer':mean('EH_answer'),'answer_length':mean('answer_length'),'answer_truncated':mean('answer_truncated'),
                   'valid_digit_mass': [r['ratings']['sender']['valid_mass'] for r in group],
                   'baseline_mean':float(np.mean(base)) if base else None,'baseline_sd':float(np.std(base,ddof=1)) if len(base)>1 else None}
            for q in ['structural','source']:
                correct=('A' if c=='R2' else 'C' if c=='R4' else 'B') if q=='structural' else 'A'
                swap={'A':'B','B':'A','C':'C'}[correct]
                records=[]
                for r in group:
                    checks=r.get('checks',{})
                    if q not in checks or q+'_swap' not in checks:continue
                    a,b=checks[q],checks[q+'_swap']
                    # Report mapped categories as well as target probability.
                    mapped={label:(a['probabilities'][label]+b['probabilities'][{'A':'B','B':'A','C':'C'}[label]])/2 for label in a['probabilities']}
                    records.append({'prompt_id':r['prompt_id'],'order_averaged_probabilities':mapped,'correct_probability':mapped[correct],
                                    'correct_argmax':max(mapped,key=mapped.get)==correct,'valid_mass':[a['valid_mass'],b['valid_mass']]})
                entry[q]={'n':len(records),'records':records,'mean_correct_probability':float(np.mean([v['correct_probability'] for v in records])) if records else None}
            output[c+'/'+source]=entry
    return output

def analyze(data,cfg,ids,audit=None):
    result={'primary':core(data,cfg,ids),'descriptive':diagnostic_summary(data),'sensitivity':{}}
    lookup={(r['prompt_id'],r['source'],r['condition']):r for r in data}
    natural=[p for p in ids if all((p,s,c) in lookup and not lookup[p,s,c]['forced_closure'] for s in SOURCES for c in CONDITIONS)]
    def subset(selected):
        out=core([r for r in data if r['prompt_id'] in selected],cfg,selected)
        out['label']='Descriptive sensitivity; complete prompt clusters retained, not confirmatory.'
        return out
    result['sensitivity']['natural_closure']=subset(natural)
    if audit is None or any(p not in audit for p in ids):result['sensitivity']['E5']={'status':'not estimable','reason':'Audit missing or incomplete'}
    else:
        selected=[p for p in ids if not(audit[p]['instructions'] or audit[p]['negative_characterizations'])]
        result['sensitivity']['E5']=subset(selected)
    return result

def report(result):
    primary=result['primary']
    lines=['# Study 5 placement analysis','',primary['reading'],'',
           'Within-stimulus placement comparisons, conditional on Study 4 traces; no pooling with Study 4. Answers may mediate rating differences.',
           '', '| Hypothesis | Status | Supported | Negligible | Reversed |',
           '|---|---|---|---|---|']
    for h in ['P1','P2','P3','S1','S2','S3','S4','S5']:
        v=primary['hypotheses'][h]
        lines.append(f'| {h} | {v["status"]} | {v["supported"]} | {v["negligible"]} | {v["reversed"]} |')
    lines+=['', '| Test/component | Estimate | CI level | CI | 90% equivalence CI | Status |',
            '|---|---|---|---|---|---|']
    for h,components in primary['tests'].items():
        for name,v in components.items():
            if 'estimate' not in v:
                lines.append(f'| {h}/{name} | — | — | — | — | not estimable |')
            else:
                fmt=lambda x:f'[{x[0]:.4f}, {x[1]:.4f}]'
                lines.append(f'| {h}/{name} | {v["estimate"]:.4f} | {100*v["ci_level"]:.2f}% | {fmt(v["ci"])} | {fmt(v["equivalence_ci"])} | {v["status"]} |')
    lines+=['','P1–P3 are primary; S1–S5 are secondary. Equivalence requires the entire 90% interval inside ±0.15. Directional and equivalence evidence can overlap. Descriptive diagnostics, answer hostility, natural-closure sensitivity and E5 sensitivity are in the companion JSON.']
    return '\n'.join(lines)+'\n'

def main():
    p=argparse.ArgumentParser();p.add_argument('--input',required=True);p.add_argument('--output',required=True);args=p.parse_args()
    cfg=config();data=verified_rows(args.input)
    if any(r.get('mode')!='main' for r in data):raise ValueError('Only main rows accepted; synthetic tests call analyze directly')
    from study5.src.common import verify_inputs
    verify_inputs(cfg)
    result=analyze(data,cfg,cfg['main_prompt_ids'],json.loads(input_path(cfg,'e5_audit').read_text()))
    save(args.output,result)
    from study5.src.common import output_path
    with output_path(args.output).with_suffix('.md').open('x') as f:f.write(report(result))
if __name__=='__main__':main()
"""Study 4 token-preserving replay. Importing this module never loads a model."""
import argparse
import json
import time
from pathlib import Path
from .common import ROOT, SOURCES, FRAMINGS, config, rows, sha, digest, seed, save, append, verified_rows, verify_reuse

class Assembly:
    def __init__(self, tokenizer, manifest):
        self.t = tokenizer
        self.f = manifest
    def enc(self, s):
        return self.t.encode(s, add_special_tokens=False)
    def marker(self, name):
        return self.enc(self.f['markers'][name])
    def base(self, prompt):
        return self.marker('system_start') + self.enc(self.f['system']) + self.marker('turn_end') + self.marker('user_start') + self.enc(prompt)
    def assemble(self, prompt, trace, framing):
        ids = self.base(prompt)
        if framing == 'own_native':
            ids += self.marker('turn_end') + self.marker('assistant_start') + trace['pre_trace_ids']
            start = len(ids)
            ids += trace['trace_ids'] + self.marker('think_close') + self.marker('answer_separator')
        else:
            ids += self.enc(self.f['quoted_before'].format(label=self.f['labels'][framing]))
            start = len(ids)
            ids += trace['trace_ids'] + self.enc(self.f['quoted_after'])
            ids += self.marker('turn_end') + self.marker('assistant_start') + self.marker('empty_thinking')
        assert ids[start:start+len(trace['trace_ids'])] == trace['trace_ids']
        return ids, [start, start+len(trace['trace_ids'])]
    def end_turn(self, history):
        end = self.marker('turn_end')
        # Qwen emits im_end but not its trailing newline.
        if history[-len(end):] == end:
            return list(history)
        if history and history[-1] == end[0]:
            return history + end[1:]
        return history + end
    def branch(self, history, question):
        return self.end_turn(history) + self.marker('user_start') + self.enc(self.f['questions'][question]) + self.marker('turn_end') + self.enc(self.f['rating_prefix'])
    def branches(self, history, framing, sender_argmax=None):
        targets = ['sender'] if framing == 'own_native' else ['sender','writer','notes']
        if sender_argmax is not None:
            history = self.branch(history, 'sender') + self.enc(str(sender_argmax))
        return {t:self.branch(history,t) for t in targets}
    def fixed_segments(self, prompt, trace):
        result = {}
        for name in self.f['fixed_segments']:
            if name == 'original_user_prompt': value = self.enc(prompt)
            elif name == 'trace_ids': value = trace['trace_ids']
            elif name.startswith('questions.'): value = self.enc(self.f['questions'][name.split('.')[1]])
            elif name == 'system': value = self.enc(self.f['system'])
            else: value = self.marker(name)
            result[name] = digest(value)
        return result

def assert_no_hooks(model):
    """Fail closed on any forward/pre-forward hook, including global hooks."""
    import torch
    bad = [n for n,m in model.named_modules() if m._forward_hooks or m._forward_pre_hooks]
    global_hooks = torch.nn.modules.module
    if bad or global_hooks._global_forward_hooks or global_hooks._global_forward_pre_hooks:
        raise RuntimeError(f'Post-trace hook-absence assertion failed: {bad}')
    return True

def readout(logits, tokenizer, labels):
    import torch
    encoded = [tokenizer.encode(x,add_special_tokens=False) for x in labels]
    if any(len(x)!=1 for x in encoded) or len({x[0] for x in encoded})!=len(labels):
        raise ValueError('Readout labels must have distinct single tokens')
    ids = [x[0] for x in encoded]
    raw = logits.float()
    if not torch.isfinite(raw).all(): raise ValueError('Nonfinite readout logits')
    mass = raw.softmax(-1)[ids].sum().item()
    probs = raw[ids].softmax(-1).cpu().tolist()
    result = {'probabilities':dict(zip(labels,probs)), 'valid_mass':mass, 'argmax':labels[max(range(len(probs)),key=probs.__getitem__)]}
    if labels == list('0123456789'):
        result.update(expected=sum(i*p for i,p in enumerate(probs)), low_mass=mass<.5)
    return result

class Backend:
    def __init__(self, cfg):
        import torch
        from study3.src.main_model import Model
        from study3.src.metrics import EmotionClassifier
        if not torch.backends.mps.is_available():
            raise RuntimeError('MPS required: launch run_smoke_test.command outside the sandbox; no CPU substitution')
        self.torch = torch
        spec = dict(cfg['model'],local_path=str((ROOT/cfg['model']['local_path']).resolve()))
        self.m = Model(spec)
        assert self.m.layer_index == cfg['model']['layer_index']
        self.classifier = EmotionClassifier(str((ROOT/cfg['classifier']['local_path']).resolve()))
        self.cfg = cfg
        self.peak = 0
        self.events = []
        self.vectors = {}
        for source,item in cfg['directions'].items():
            obj = torch.load(ROOT/item['path'],map_location='cpu',weights_only=False)
            self.vectors[source] = obj['vector'] if 'vector' in obj else obj['v_hat']
    def clean(self, operation):
        assert_no_hooks(self.m.model)
        self.events.append({'operation':operation,'hook_absent':True,'initial_cache':None})
    def forward(self, ids, cache=None, use_cache=False):
        out = self.m.model(input_ids=self.m.tensor(ids),past_key_values=cache,use_cache=use_cache)
        self.peak = max(self.peak,self.torch.mps.driver_allocated_memory())
        return out
    def sample(self, raw):
        torch = self.torch
        g = self.cfg['generation']
        vals, ix = (raw.float()/g['temperature']).topk(g['top_k'])
        cut = vals.softmax(-1).cumsum(-1)>g['top_p']
        cut[1:] = cut[:-1].clone(); cut[0] = False; vals[cut] = -torch.inf
        return ix[torch.multinomial(vals.softmax(-1),1)].item()
    def set_seed(self, value):
        self.torch.manual_seed(value); self.torch.mps.manual_seed(value)
    def trace(self, prompt, source, value, cap):
        self.set_seed(value)
        ids = self.m.ids(self.m.messages(prompt,self.cfg['condition']),thinking=True)
        tokens = []; cache = None; forced = False
        with self.torch.inference_mode(), self.m.steering(0 if source=='unsteered' else self.cfg['alpha'], self.cfg['norm']['value'],self.vectors.get(source)):
            out = self.forward(ids, use_cache=True)
            cache = out.past_key_values
            for _ in range(cap):
                tok = self.sample(out.logits[0,-1]); tokens.append(tok)
                out = self.forward([tok],cache,True); cache = out.past_key_values
                if tok == self.m.close_think: break
                eos = self.m.model.generation_config.eos_token_id
                if tok in (eos if isinstance(eos,list) else [eos]): raise RuntimeError('EOS before thinking closure')
            else: forced = True
        del cache,out
        self.clean('trace_cache_discarded')
        if self.m.open_think not in tokens: raise RuntimeError('Missing sampled <think>')
        opening = tokens.index(self.m.open_think)
        closing = tokens.index(self.m.close_think) if self.m.close_think in tokens else len(tokens)
        return {'prompt_ids':ids,'pre_trace_ids':tokens[:opening+1],'trace_ids':tokens[opening+1:closing], 'forced_closure':forced,'seed':value}
    def answer(self, prefix, value, cap):
        self.clean('answer'); self.set_seed(value)
        tokens = []; cache = None
        eos = self.m.model.generation_config.eos_token_id
        eos = eos if isinstance(eos,list) else [eos]
        with self.torch.inference_mode():
            out = self.forward(prefix,use_cache=True); cache = out.past_key_values
            for _ in range(cap):
                tok = self.sample(out.logits[0,-1]); tokens.append(tok)
                if tok in eos: break
                out = self.forward([tok],cache,True); cache = out.past_key_values
        del out,cache
        return tokens
    def rating(self, ids, labels=list('0123456789')):
        self.clean('readout')
        with self.torch.inference_mode():
            return readout(self.forward(ids).logits[0,-1],self.m.tokenizer,labels)
    def ppl(self, prefix, ids):
        self.clean('perplexity')
        with self.torch.inference_mode():
            value = self.m.segment_ppl(prefix,ids)
            self.peak = max(self.peak,self.torch.mps.driver_allocated_memory())
            return value

def select_checks(prompts, cfg, mode):
    import numpy as np
    rng = np.random.default_rng(cfg['seeds']['check_permutation'])
    counts = cfg['check_sample']['pilot' if mode!='main' else str(len(prompts))]
    selected = []
    for kind,n in zip(('provocative','neutral'),counts):
        pool = sorted(p['id'] for p in prompts if p['type']==kind)
        selected.extend(rng.permutation(pool).tolist()[:n])
    return set(selected)

def reused_traces(cfg):
    result = {}
    for r in rows(ROOT/cfg['study3_raw']['path']):
        if r['mode']!='think': continue
        if r['dose_fraction']==0: source='unsteered'
        elif r['route']=='pulse' and r['dose_fraction']==1: source=r['direction']
        else: continue
        key = (r['prompt_id'],source)
        if key in result: raise RuntimeError(f'Duplicate reused trace {key}')
        # Find the saved trace as an exact token slice; 151667 is verified by the real-tokenizer unit test.
        opening = r['token_ids'].index(151667)
        result[key] = {'prompt_ids':r['prompt_ids'],'pre_trace_ids':r['token_ids'][:opening+1], 'trace_ids':r['thinking_ids'],'forced_closure':r['thinking_truncated'],'seed':r['seed'],'study3_row_sha256':digest(r)}
    return result

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode',choices=['smoke','pilot','main'],required=True)
    parser.add_argument('--output',required=True)
    args = parser.parse_args()
    cfg = config(); verify_reuse(cfg)
    if args.mode=='main':
        from .approval import require_approval
        require_approval()
    outdir = (ROOT/args.output).resolve()
    from .common import output_path
    output_path(outdir/'placeholder')
    framing = json.loads((ROOT/'framings.json').read_text())
    prompt_path = ROOT/cfg['prompts']['test' if args.mode=='main' else 'pilot']
    prompts = rows(prompt_path)
    if args.mode=='main':
        assert len(prompts)==cfg['N']
        assert all(sum(p['type']==kind for p in prompts)==n for kind,n in cfg['composition'].items())
    if args.mode=='smoke': prompts = [p for p in prompts if p['id'] in cfg['smoke']['prompt_ids']]
    checks = select_checks(prompts,cfg,args.mode)
    provenance = {str(p.relative_to(ROOT)):sha(p) for p in [ROOT/'config.yaml',ROOT/'framings.json',prompt_path,*sorted((ROOT/'src').glob('*.py'))]}
    provenance.update({str(p.relative_to(ROOT.parent)):sha(p) for p in [ROOT.parent/'study3/src'/name for name in ['base_model.py','model_utils.py','main_model.py','metrics.py']]})
    manifest = {'mode':args.mode,'hashes':provenance,'check_ids':sorted(checks),'short_caps':args.mode=='smoke'}
    if (outdir/'manifest.json').exists():
        old = json.loads((outdir/'manifest.json').read_text())
        if old!=manifest:
            # Allowed only for the logged 2026-10-22 memory fix: everything except src/runner.py must match.
            diff = {k for k in set(old['hashes'])|set(manifest['hashes']) if old['hashes'].get(k)!=manifest['hashes'].get(k)}
            same_rest = {k:v for k,v in old.items() if k!='hashes'}=={k:v for k,v in manifest.items() if k!='hashes'}
            if diff!={'src/runner.py'} or not same_rest: raise RuntimeError(f'Resume manifest differs: {sorted(diff)}')
            if not (outdir/'manifest_pre_memfix.json').exists(): (outdir/'manifest.json').rename(outdir/'manifest_pre_memfix.json')
            else: (outdir/'manifest.json').unlink()
            save(outdir/'manifest.json',manifest)
    else: save(outdir/'manifest.json',manifest)
    done = verified_rows(outdir/'cells.jsonl'); done_keys = {tuple(r['cell_key']) for r in done}
    trace_rows = verified_rows(outdir/'traces.jsonl')
    traces = {tuple(r['trace_key']):r for r in trace_rows}
    if len(done_keys)!=len(done) or len(traces)!=len(trace_rows): raise RuntimeError('Duplicate resume keys')
    backend = Backend(cfg); assembly = Assembly(backend.m.tokenizer,framing)
    reused = reused_traces(cfg) if args.mode=='pilot' else {}
    caps = cfg['smoke'] if args.mode=='smoke' else cfg['generation']
    for p in prompts:
        for source in SOURCES:
            key = (p['id'],source)
            if key not in traces:
                started = time.monotonic()
                tr = reused[key] if args.mode=='pilot' else backend.trace(p['text'],source,seed(cfg,'trace',*key),caps['thinking_cap'])
                assert tr['pre_trace_ids'][-1] == backend.m.open_think
                native,_ = assembly.assemble(p['text'],tr,'own_native')
                expected = tr['prompt_ids']+tr['pre_trace_ids']+tr['trace_ids']+assembly.marker('think_close')+assembly.marker('answer_separator')
                assert native==expected,'Native construction differs from Study 3 pulse prefix'
                tr['text'] = backend.m.tokenizer.decode(tr['trace_ids'],skip_special_tokens=True)
                tr['perplexity'] = backend.ppl(tr['prompt_ids']+tr['pre_trace_ids'],tr['trace_ids'])
                # Study 3 scores contiguous 120-model-token trace windows, then averages.
                windows = []
                for offset in range(0,len(tr['trace_ids']),120):
                    ids = tr['trace_ids'][offset:offset+120]
                    windows.append({'start':offset,'token_count':len(ids),**backend.classifier.score(backend.m.tokenizer.decode(ids,skip_special_tokens=True))})
                tr['trace_windows'] = windows
                eh = sum(w['eh'] for w in windows)/len(windows) if windows and all(w['eh'] is not None for w in windows) else None
                tr['classifier'] = {'eh':eh,'error':None if eh is not None else 'Empty trace or classifier failure; no alternate scorer'}
                tr.update(trace_key=list(key),seconds=time.monotonic()-started)
                traces[key] = append(outdir/'traces.jsonl',tr)
                import gc; gc.collect(); backend.torch.mps.empty_cache()
            tr = traces[key]
            for frame in FRAMINGS:
                cell_key = (*key,frame)
                if cell_key in done_keys: continue
                started = time.monotonic(); backend.events=[]; backend.peak=0
                prefix,bounds = assembly.assemble(p['text'],tr,frame)
                answer_seed = seed(cfg,'answer',*cell_key)
                answer = backend.answer(prefix,answer_seed,caps['answer_cap'])
                history = prefix+answer
                branch_ids = assembly.branches(history,frame)
                ratings = {t:backend.rating(ids) for t,ids in branch_ids.items()}
                seq_ids = assembly.branches(history,frame,ratings['sender']['argmax'])
                sequential = {'sender':ratings['sender']}
                sequential.update({t:backend.rating(ids) for t,ids in seq_ids.items() if t!='sender'})
                check = {}
                if p['id'] in checks:
                    if frame!='own_native':
                        check = {q:backend.rating(assembly.branch(history,q),['A','B']) for q in ('label','operative')}
                    sender_history = branch_ids['sender']+assembly.enc(ratings['sender']['argmax'])
                    check['referent'] = backend.rating(assembly.branch(sender_history,'referent'),['A','B'])
                    check['referent_swap'] = backend.rating(assembly.branch(sender_history,'referent_swap'),['A','B'])
                text = backend.m.tokenizer.decode(answer,skip_special_tokens=True)
                ppl = backend.ppl(prefix,answer)
                classifier = backend.classifier.score(text)
                backend.torch.mps.synchronize()
                row = {'schema':'study4-v0.5.1','cell_key':list(cell_key),'prompt_id':p['id'],'prompt_type':p['type'],'source':source,'framing':frame,'mode':args.mode,'trace_sha256':tr['row_sha256'],'trace_ids':tr['trace_ids'],'trace_text':tr['text'],'forced_closure':tr['forced_closure'],'EH_trace':tr['classifier']['eh'],'trace_perplexity':tr['perplexity'],'answer_prefix_ids':prefix,'trace_bounds':bounds,'fixed_segments':assembly.fixed_segments(p['text'],tr),'answer_ids':answer,'answer_text':text,'answer_seed':answer_seed,'ratings':ratings,'sequential':sequential,'branch_ids':branch_ids,'sequential_branch_ids':{t:v for t,v in seq_ids.items() if t!='sender'},'checks':check,'EH_answer':classifier['eh'],'answer_classifier':classifier,'answer_perplexity':ppl,'replay_assertions':backend.events,'seconds':time.monotonic()-started,'peak_driver_memory_bytes':backend.peak,'manifest_sha256':digest(manifest)}
                append(outdir/'cells.jsonl',row)
                print(json.dumps({'finished':cell_key,'seconds':row['seconds'],'peak_memory':backend.peak}),flush=True)
                # Engineering fix 2026-10-22: release per-cell tensors so MPS memory does not accumulate across cells.
                del row,prefix,answer,history,branch_ids,seq_ids,ratings,sequential,check
                import gc; gc.collect(); backend.torch.mps.empty_cache()
    result = verified_rows(outdir/'cells.jsonl')
    # Separate check dataset, with an explicit link to the identical post-answer history.
    existing_checks = {tuple(r['cell_key']) for r in verified_rows(outdir/'checks.jsonl')}
    for r in result:
        if r['checks'] and tuple(r['cell_key']) not in existing_checks:
            append(outdir/'checks.jsonl',{'cell_key':r['cell_key'],'main_cell_sha256':r['row_sha256'],'prompt_id':r['prompt_id'],'source':r['source'],'framing':r['framing'],'checks':r['checks'],'post_answer_sha256':digest(r['answer_prefix_ids']+r['answer_ids'])})
    if not (outdir/'summary.json').exists():
        save(outdir/'summary.json',{'mode':args.mode,'cells':len(result),'expected_cells':len(prompts)*12,'seconds':sum(r['seconds'] for r in result),'peak_driver_memory_bytes':max(r['peak_driver_memory_bytes'] for r in result),'all_hooks_absent':all(e['hook_absent'] for r in result for e in r['replay_assertions']),'per_cell':[{'key':r['cell_key'],'seconds':r['seconds'],'peak_driver_memory_bytes':r['peak_driver_memory_bytes']} for r in result]})

if __name__=='__main__': main()

exec
/bin/zsh -lc 'cat study5/Study5_RoleLadder_PREREG_v0.3.md study5/data/main/analysis.json study5/data/main/RESULTS_SUMMARY.md' in /Users/arthursu/Projects/affect-suppression-steering
 succeeded in 0ms:
# Preregistration — Study 5: The Placement Ladder

**Working title:** Affect Under Constraint V: Does a Steered Reasoning Trace Retain Its Influence When Moved Out of the Active Thinking Context?
**Author:** Arthur Su. **Designed by:** Claude (2026-10-25).
**Version:** 0.3 (binding upon `PREREG_APPROVED` and Zenodo deposit; adds the pilot disposition in Section 5).
**Changes in v0.2:** incorporates Codex (study5/CODEX_REVIEW_v0.1.md) and ChatGPT (study5/CHATGPT_REVIEW_v0.1.md) reviews: matched nonempty prior replies in R2/R3; explicit continuation instruction; new matched-history current-thinking condition R1-M; P1/P2 relabelled as historical-persistence tests and the channel contrast made co-primary; unsteered-relative and control-relative effects reported separately; reading table conditional on positive controls and on direct contrasts; R3 described as artificially retained reasoning; ownership language replaced by placement-dependent carryover; precision/power limits stated; diagnostics split into structural recognition and source attribution; full freezing requirements.
**Provenance:** designed after observing Study 4 outcomes (prereg 10.5281/zenodo.23629525). Study 3: 10.5281/zenodo.23323490.

## Rationale
Study 4 found that identical steered trace tokens lowered Qwen3-4B's later rating of the user when placed in the model's current thinking block (−0.66), but not when quoted in the user turn (≈0), regardless of authorship label. Study 5 asks a narrower question: does a hostility-bearing trace retain its capacity to bias later judgment when moved out of the active thinking context, and does that capacity depend on whether the historical trace is represented as visible assistant content or as retained assistant reasoning? The study is motivated by a broader theoretical distinction between the content of a representation and its contextual placement. Outcomes measure placement-dependent effects on model judgment, without assuming that such effects establish subjective ownership or directly model clinical psychological mechanisms.

## 1. Conditions (yoked: the same 320 stored Study 4 trace token sequences in every condition; no new trace generation)
Common elements, fixed as token IDs in `framings_s5.json`:
- **Neutral prior reply N:** "I'll address your original message now." (identical in R1-M, R2, R3)
- **Continuation C:** "Please now respond to my first message in this conversation." (identical in R1-M, R2, R3)

| Condition | Structure (after system + original user prompt) |
|---|---|
| **R1 Current thinking** (Study 4 own-native, exact construction) | assistant: ⟨think⟩TRACE⟨/think⟩ → answer |
| **R1-M Current thinking, matched history** | assistant: ⟨think⟩⟨/think⟩ N → user: C → assistant: ⟨think⟩TRACE⟨/think⟩ → answer |
| **R2 Historical visible reply** | assistant: ⟨think⟩⟨/think⟩ TRACE N → user: C → assistant: ⟨think⟩⟨/think⟩ → answer |
| **R3 Historical thinking (artificially retained)** | assistant: ⟨think⟩TRACE⟨/think⟩ N → user: C → assistant: ⟨think⟩⟨/think⟩ → answer |
| **R4 User quote** (Study 4 own-quoted, exact construction) | user: prompt + quoted TRACE → assistant: ⟨think⟩⟨/think⟩ → answer |

R2 and R3 are token-identical except for the position of the thinking delimiters around TRACE. R3 deliberately retains prior-turn thinking that Qwen3's default template strips; results about R3 concern retained historical reasoning, not ordinary Qwen3 conversation memory. R1-M differs from R3 in whether TRACE sits in the current or the prior assistant turn, with matched history (it still differs in token distance to the answer and in turn boundary).

## 2. Model, decoding, outcome
Qwen3-4B bf16 on MPS; fresh unsteered replay with logged hook-absence assertion; answer sampled (cap 200; T 0.6, top-p 0.95, top-k 20). Seeds: R1 and R4 reuse Study 4's answer seeds (reproducibility); R1-M, R2, R3 use new seeds fixed per prompt × source × condition in `config_s5.yaml`.
**Outcome:** the Study 4 v0.6 sender question ("…how much do you like the user who sent the original request?") on an independent branch whose context is the full conversation including the generated answer (so the answer may mediate; answer expressed hostility is reported descriptively). Expected digit 0–9; valid-digit mass recorded.
**Estimands per condition c:** X_c(H) = R(hostility, c) − R(unsteered, c); A_c(ctrl) = R(hostility, c) − R(ctrl, c) for ctrl ∈ {technicality, random}. Both are always reported; a claim that hostility lowers the rating requires X_c(H) < 0 as well as A_c < 0.

## 3. Hypotheses
Prompt-cluster bootstrap, 10,000 resamples, percentile CIs. Conjunction rule: a hypothesis is supported only if every required component (X_c(H) and A_c for both controls) excludes zero in the predicted direction. Multiplicity: three primaries at 98.33% CIs (Bonferroni over three); secondaries at 95% and labelled secondary.

**Primary**
- **P1 — Historical visible-content persistence:** X_R2(H) < 0 and A_R2 < 0 (both controls).
- **P2 — Retained historical-thinking persistence:** X_R3(H) < 0 and A_R3 < 0 (both controls).
- **P3 — Channel contrast (historical):** A_R3 − A_R2 < 0 (both controls).

**Secondary**
- S1 — Positive control (within-stimulus reproducibility of Study 4): X_R1(H) < 0, A_R1 < 0.
- S2 — Matched-history current thinking: X_R1-M(H) < 0, A_R1-M < 0.
- S3 — Current vs historical thinking under matched history: A_R1-M − A_R3 < 0.
- S4 — Effect of added history on current thinking: A_R1 − A_R1-M (two-sided, descriptive direction).
- S5 — Quote reproducibility: X_R4(H) and A_R4 negligible.

**Equivalence:** a component is "negligible" only if its 90% CI lies within ±0.15; otherwise a non-significant component is "inconclusive". A component significant in the opposite direction is "reversed". Supported-and-negligible overlap is reported as "small but detectable".

## 4. Reading (applies only if S1 and S2 are supported; otherwise historical nulls are uninterpretable and reported as such)
| P1 (R2) | P2 (R3) | P3 | Reading (placement terms only) |
|---|---|---|---|
| supported | supported | — | Both historical placements retain influence; P3 says whether retained thinking differs from visible reply. |
| negligible | supported | supported | Retained historical thinking retains influence; visible historical reply does not; consistent with a channel-dependent effect. |
| supported | negligible | reversed | Visible historical reply retains influence; retained thinking does not (channel, coherence or serialization). |
| negligible | negligible | — | Influence restricted to current-turn thinking placement under the tested framings (S3 locates the drop). |
Comparative claims require the direct contrast (P3 or S3), not differences in significance. Inconclusive components are reported as inconclusive.

## 5. Sample, precision, pilot, runtime
N = 80 Study 4 test prompts with their stored traces (fixed by availability). Illustrative precision (Codex, from Study 4 covariances): under native-like variance, joint power for effects of −0.15 is ≈31% and joint equivalence power ≈16%; under quote-like variance ≈81% and ≈88%. Native-sized effects (≈−0.6) are well powered; small residual effects and equivalence may remain unresolved, which is accepted and will be reported. The margin is not changed after the pilot.
**Pilot:** the 4 Study 3 pilot prompts × all sources × all conditions, compared with the corresponding Study 4 pilot cells for R1/R4; checks template construction (exact trace slices and full-prefix tests), valid-digit mass, and timing. Descriptive only, never pooled.
**Runtime:** 1,600 cells (80 × 4 sources × 5 conditions) at ≈20–25 s ≈ 9–11 h; benchmarked in the pilot.

## 6. Validity and diagnostics
- Validity (pilot): per condition, unsteered-baseline SD ≥ 0.15 across pilot prompts and mean valid mass ≥ 0.8; R1 and R4 pilot baselines within 0.3 of the corresponding Study 4 pilot cells. Failure: at most one logged template revision, chosen only by these criteria; if still failing, the condition is dropped and reported.

**Pilot outcome and author disposition (2026-10-26, before freeze and before any main-run data):** the pilot ran all 80 cells. Valid-digit mass was ≈1.00 in every condition, and the R1 and R4 unsteered baselines matched the Study 4 v0.6 references exactly (mean difference 0.00). The unsteered-baseline SD across the four pilot prompts fell below 0.15 for R1-M (0.13), R2 (0.09) and R4 (0.13); R1 (0.44) and R3 (0.18) passed. The SD criterion was intended to detect a compressed or ceilinged readout. The baselines sit near 7.9 of 9, not at the ceiling, and steered cells move away from them in the pilot, so the readout is not compressed. A four-prompt SD is also an imprecise estimate. By author decision, these shortfalls are accepted without a template revision, and all five conditions are kept. The one-revision allowance is not used. Main-run unsteered baseline SDs across all 80 prompts will be reported for every condition. No effect estimate informed this disposition.
- Diagnostics (16 check prompts, all sources, descriptive, A/B order counterbalanced and averaged): structural recognition ("Where did the earlier text appear: A in your previous visible reply, B in your previous private reasoning, C in the user's message?" — scored against the condition) and source attribution ("Who produced the earlier text: A you, B the user?"). Not used to exclude trials.
- Descriptive: answer expressed hostility, answer length and truncation, natural-closure and Study 4 E5 explicit-content flags as sensitivity analyses.

## 7. Freezing, reporting, stopping
Before approval: `framings_s5.json`, `config_s5.yaml`, Study 5 runner and analysis (validated on synthetic data with planted placement patterns), tokenizer/model revision, trace-input hashes, seeds and diagnostic prompt IDs, all hashed in `PREREG_APPROVED`; Zenodo deposit before the main run. No changes after the main run starts; resumable output, one row per cell. R1 and R4 are within-stimulus reproducibility checks, not independent replications; claims are conditional on the Study 4 stimulus set and are not pooled with Study 4.
{
  "primary": {
    "prompt_ids": [
      "s4t00",
      "s4t01",
      "s4t02",
      "s4t03",
      "s4t04",
      "s4t05",
      "s4t06",
      "s4t07",
      "s4t08",
      "s4t09",
      "s4t10",
      "s4t11",
      "s4t12",
      "s4t13",
      "s4t14",
      "s4t15",
      "s4t16",
      "s4t17",
      "s4t18",
      "s4t19",
      "s4t20",
      "s4t21",
      "s4t22",
      "s4t23",
      "s4t24",
      "s4t25",
      "s4t26",
      "s4t27",
      "s4t28",
      "s4t29",
      "s4t30",
      "s4t31",
      "s4t32",
      "s4t33",
      "s4t34",
      "s4t35",
      "s4t36",
      "s4t37",
      "s4t38",
      "s4t39",
      "s4t40",
      "s4t41",
      "s4t42",
      "s4t43",
      "s4t44",
      "s4t45",
      "s4t46",
      "s4t47",
      "s4t48",
      "s4t49",
      "s4t50",
      "s4t51",
      "s4t52",
      "s4t53",
      "s4t54",
      "s4t55",
      "s4t56",
      "s4t57",
      "s4t58",
      "s4t59",
      "s4t60",
      "s4t61",
      "s4t62",
      "s4t63",
      "s4t64",
      "s4t65",
      "s4t66",
      "s4t67",
      "s4t68",
      "s4t69",
      "s4t70",
      "s4t71",
      "s4t72",
      "s4t73",
      "s4t74",
      "s4t75",
      "s4t76",
      "s4t77",
      "s4t78",
      "s4t79"
    ],
    "n": 80,
    "estimands": {
      "R1:X": {
        "estimate": -0.6603613427204427,
        "ci_level": 0.95,
        "ci": [
          -0.7787523302015442,
          -0.5387412756544449
        ],
        "equivalence_ci_level": 0.9,
        "equivalence_ci": [
          -0.760388387527391,
          -0.5585564493958819
        ],
        "n": 80,
        "supported": true,
        "negligible": false,
        "reversed": false,
        "negative": true,
        "positive": false,
        "status": "supported"
      },
      "R1:A_technicality": {
        "estimate": -0.7199564160915257,
        "ci_level": 0.95,
        "ci": [
          -0.8634569816800454,
          -0.5769757668898995
        ],
        "equivalence_ci_level": 0.9,
        "equivalence_ci": [
          -0.8388869410322904,
          -0.5990080428817486
        ],
        "n": 80,
        "supported": true,
        "negligible": false,
        "reversed": false,
        "negative": true,
        "positive": false,
        "status": "supported"
      },
      "R1:A_random": {
        "estimate": -0.4345790016966252,
        "ci_level": 0.95,
        "ci": [
          -0.5685614252226605,
          -0.29833594768121047
        ],
        "equivalence_ci_level": 0.9,
        "equivalence_ci": [
          -0.5474222373008131,
          -0.31935825622204067
        ],
        "n": 80,
        "supported": true,
        "negligible": false,
        "reversed": false,
        "negative": true,
        "positive": false,
        "status": "supported"
      },
      "R1-M:X": {
        "estimate": -0.3007684611835709,
        "ci_level": 0.95,
        "ci": [
          -0.3595072696335147,
          -0.24198453695077318
        ],
        "equivalence_ci_level": 0.9,
        "equivalence_ci": [
          -0.3500512562372192,
          -0.2514838763240288
        ],
        "n": 80,
        "supported": true,
        "negligible": false,
        "reversed": false,
        "negative": true,
        "positive": false,
        "status": "supported"
      },
      "R1-M:A_technicality": {
        "estimate": -0.2862992407832918,
        "ci_level": 0.95,
        "ci": [
          -0.35102624459067017,
          -0.22395989592462115
        ],
        "equivalence_ci_level": 0.9,
        "equivalence_ci": [
          -0.3407332578658821,
          -0.23358952121564303
        ],
        "n": 80,
        "supported": true,
        "negligible": false,
        "reversed": false,
        "negative": true,
        "positive": false,
        "status": "supported"
      },
      "R1-M:A_random": {
        "estimate": -0.216732361687154,
        "ci_level": 0.95,
        "ci": [
          -0.27426068147079796,
          -0.15751364936815104
        ],
        "equivalence_ci_level": 0.9,
        "equivalence_ci": [
          -0.26450949271150825,
          -0.1675460334528089
        ],
        "n": 80,
        "supported": true,
        "negligible": false,
        "reversed": false,
        "negative": true,
        "positive": false,
        "status": "supported"
      },
      "R2:X": {
        "estimate": -0.2359275981581516,
        "ci_level": 0.95,
        "ci": [
          -0.2914047094075578,
          -0.1817864268188929
        ],
        "equivalence_ci_level": 0.9,
        "equivalence_ci": [
          -0.2826018545115312,
          -0.19044575137017059
        ],
        "n": 80,
        "supported": true,
        "negligible": false,
        "reversed": false,
        "negative": true,
        "positive": false,
        "status": "supported"
      },
      "R2:A_technicality": {
        "estimate": -0.2569108773543456,
        "ci_level": 0.95,
        "ci": [
          -0.3203336852423185,
          -0.19563055022161085
        ],
        "equivalence_ci_level": 0.9,
        "equivalence_ci": [
          -0.31055625059448144,
          -0.20470871562090306
        ],
        "n": 80,
        "supported": true,
        "negligible": false,
        "reversed": false,
        "negative": true,
        "positive": false,
        "status": "supported"
      },
      "R2:A_random": {
        "estimate": -0.20064824509128104,
        "ci_level": 0.95,
        "ci": [
          -0.2618714275204359,
          -0.14256219549755336
        ],
        "equivalence_ci_level": 0.9,
        "equivalence_ci": [
          -0.2509636987363844,
          -0.15120534842344643
        ],
        "n": 80,
        "supported": true,
        "negligible": false,
        "reversed": false,
        "negative": true,
        "positive": false,
        "status": "supported"
      },
      "R3:X": {
        "estimate": -0.23568061520700892,
        "ci_level": 0.95,
        "ci": [
          -0.302476736879237,
          -0.17114611349279063
        ],
        "equivalence_ci_level": 0.9,
        "equivalence_ci": [
          -0.2896558517380536,
          -0.18091779776464006
        ],
        "n": 80,
        "supported": true,
        "negligible": false,
        "reversed": false,
        "negative": true,
        "positive": false,
        "status": "supported"
      },
      "R3:A_technicality": {
        "estimate": -0.2968295124209497,
        "ci_level": 0.95,
        "ci": [
          -0.3742063353707915,
          -0.2213996407336953
        ],
        "equivalence_ci_level": 0.9,
        "equivalence_ci": [
          -0.3616432070721588,
          -0.2326259052048524
        ],
        "n": 80,
        "supported": true,
        "negligible": false,
        "reversed": false,
        "negative": true,
        "positive": false,
        "status": "supported"
      },
      "R3:A_random": {
        "estimate": -0.1786136438223164,
        "ci_level": 0.95,
        "ci": [
          -0.24570816051786284,
          -0.10905295773022121
        ],
        "equivalence_ci_level": 0.9,
        "equivalence_ci": [
          -0.235760616106266,
          -0.11998750196432292
        ],
        "n": 80,
        "supported": true,
        "negligible": false,
        "reversed": false,
        "negative": true,
        "positive": false,
        "status": "supported"
      },
      "R4:X": {
        "estimate": -0.0567356185144544,
        "ci_level": 0.95,
        "ci": [
          -0.134203249015098,
          0.01887537053169751
        ],
        "equivalence_ci_level": 0.9,
        "equivalence_ci": [
          -0.12140359150974028,
          0.007173336126515108
        ],
        "n": 80,
        "supported": false,
        "negligible": true,
        "reversed": false,
        "negative": false,
        "positive": false,
        "status": "negligible"
      },
      "R4:A_technicality": {
        "estimate": -0.23443952265100992,
        "ci_level": 0.95,
        "ci": [
          -0.31478623793537625,
          -0.15019729667375456
        ],
        "equivalence_ci_level": 0.9,
        "equivalence_ci": [
          -0.3018550587420781,
          -0.1641365628040707
        ],
        "n": 80,
        "supported": true,
        "negligible": false,
        "reversed": false,
        "negative": true,
        "positive": false,
        "status": "supported"
      },
      "R4:A_random": {
        "estimate": -0.11439708232184717,
        "ci_level": 0.95,
        "ci": [
          -0.20018212373190533,
          -0.02644857677303564
        ],
        "equivalence_ci_level": 0.9,
        "equivalence_ci": [
          -0.185606513113547,
          -0.0407848472071676
        ],
        "n": 80,
        "supported": true,
        "negligible": false,
        "reversed": false,
        "negative": true,
        "positive": false,
        "status": "supported"
      },
      "P3:technicality": {
        "estimate": -0.03991863506660409,
        "ci_level": 0.95,
        "ci": [
          -0.10253643683439347,
          0.024017760643631775
        ],
        "equivalence_ci_level": 0.9,
        "equivalence_ci": [
          -0.09225108639425944,
          0.012699096263355358
        ],
        "n": 80,
        "supported": false,
        "negligible": true,
        "reversed": false,
        "negative": false,
        "positive": false,
        "status": "negligible"
      },
      "P3:random": {
        "estimate": 0.022034601268964636,
        "ci_level": 0.95,
        "ci": [
          -0.04656038407086599,
          0.09243429098712827
        ],
        "equivalence_ci_level": 0.9,
        "equivalence_ci": [
          -0.03565359562114909,
          0.08211739666481524
        ],
        "n": 80,
        "supported": false,
        "negligible": true,
        "reversed": false,
        "negative": false,
        "positive": false,
        "status": "negligible"
      },
      "S3:technicality": {
        "estimate": 0.010530271637657896,
        "ci_level": 0.95,
        "ci": [
          -0.0640971080248341,
          0.08410299548616831
        ],
        "equivalence_ci_level": 0.9,
        "equivalence_ci": [
          -0.05197769051143849,
          0.07237056359674968
        ],
        "n": 80,
        "supported": false,
        "negligible": true,
        "reversed": false,
        "negative": false,
        "positive": false,
        "status": "negligible"
      },
      "S3:random": {
        "estimate": -0.03811871786483763,
        "ci_level": 0.95,
        "ci": [
          -0.10977406051624482,
          0.03400146065393096
        ],
        "equivalence_ci_level": 0.9,
        "equivalence_ci": [
          -0.09899811782590069,
          0.022108863138562692
        ],
        "n": 80,
        "supported": false,
        "negligible": true,
        "reversed": false,
        "negative": false,
        "positive": false,
        "status": "negligible"
      },
      "S4:technicality": {
        "estimate": -0.433657175308234,
        "ci_level": 0.95,
        "ci": [
          -0.5436262703109923,
          -0.3232250777471379
        ],
        "equivalence_ci_level": 0.9,
        "equivalence_ci": [
          -0.5248994159064291,
          -0.3403613928690193
        ],
        "n": 80,
        "supported": true,
        "negligible": false,
        "reversed": false,
        "negative": true,
        "positive": false,
        "status": "supported"
      },
      "S4:random": {
        "estimate": -0.21784664000947124,
        "ci_level": 0.95,
        "ci": [
          -0.3262609796294227,
          -0.10749729626127881
        ],
        "equivalence_ci_level": 0.9,
        "equivalence_ci": [
          -0.30884075522678456,
          -0.12492016054646471
        ],
        "n": 80,
        "supported": true,
        "negligible": false,
        "reversed": false,
        "negative": true,
        "positive": false,
        "status": "supported"
      }
    },
    "tests": {
      "P1": {
        "R2:X": {
          "estimate": -0.2359275981581516,
          "ci_level": 0.9833,
          "ci": [
            -0.3032362716958626,
            -0.16843893221552064
          ],
          "equivalence_ci_level": 0.9,
          "equivalence_ci": [
            -0.2826018545115312,
            -0.19044575137017059
          ],
          "n": 80,
          "supported": true,
          "negligible": false,
          "reversed": false,
          "negative": true,
          "positive": false,
          "status": "supported"
        },
        "R2:A_technicality": {
          "estimate": -0.2569108773543456,
          "ci_level": 0.9833,
          "ci": [
            -0.33572702499134593,
            -0.18368742475709346
          ],
          "equivalence_ci_level": 0.9,
          "equivalence_ci": [
            -0.31055625059448144,
            -0.20470871562090306
          ],
          "n": 80,
          "supported": true,
          "negligible": false,
          "reversed": false,
          "negative": true,
          "positive": false,
          "status": "supported"
        },
        "R2:A_random": {
          "estimate": -0.20064824509128104,
          "ci_level": 0.9833,
          "ci": [
            -0.27458173386586915,
            -0.1285780831905631
          ],
          "equivalence_ci_level": 0.9,
          "equivalence_ci": [
            -0.2509636987363844,
            -0.15120534842344643
          ],
          "n": 80,
          "supported": true,
          "negligible": false,
          "reversed": false,
          "negative": true,
          "positive": false,
          "status": "supported"
        }
      },
      "P2": {
        "R3:X": {
          "estimate": -0.23568061520700892,
          "ci_level": 0.9833,
          "ci": [
            -0.3198329886515392,
            -0.1574477611426317
          ],
          "equivalence_ci_level": 0.9,
          "equivalence_ci": [
            -0.2896558517380536,
            -0.18091779776464006
          ],
          "n": 80,
          "supported": true,
          "negligible": false,
          "reversed": false,
          "negative": true,
          "positive": false,
          "status": "supported"
        },
        "R3:A_technicality": {
          "estimate": -0.2968295124209497,
          "ci_level": 0.9833,
          "ci": [
            -0.39102035172535954,
            -0.20479002310767142
          ],
          "equivalence_ci_level": 0.9,
          "equivalence_ci": [
            -0.3616432070721588,
            -0.2326259052048524
          ],
          "n": 80,
          "supported": true,
          "negligible": false,
          "reversed": false,
          "negative": true,
          "positive": false,
          "status": "supported"
        },
        "R3:A_random": {
          "estimate": -0.1786136438223164,
          "ci_level": 0.9833,
          "ci": [
            -0.25849560896196183,
            -0.09203246925197488
          ],
          "equivalence_ci_level": 0.9,
          "equivalence_ci": [
            -0.235760616106266,
            -0.11998750196432292
          ],
          "n": 80,
          "supported": true,
          "negligible": false,
          "reversed": false,
          "negative": true,
          "positive": false,
          "status": "supported"
        }
      },
      "S1": {
        "R1:X": {
          "estimate": -0.6603613427204427,
          "ci_level": 0.95,
          "ci": [
            -0.7787523302015442,
            -0.5387412756544449
          ],
          "equivalence_ci_level": 0.9,
          "equivalence_ci": [
            -0.760388387527391,
            -0.5585564493958819
          ],
          "n": 80,
          "supported": true,
          "negligible": false,
          "reversed": false,
          "negative": true,
          "positive": false,
          "status": "supported"
        },
        "R1:A_technicality": {
          "estimate": -0.7199564160915257,
          "ci_level": 0.95,
          "ci": [
            -0.8634569816800454,
            -0.5769757668898995
          ],
          "equivalence_ci_level": 0.9,
          "equivalence_ci": [
            -0.8388869410322904,
            -0.5990080428817486
          ],
          "n": 80,
          "supported": true,
          "negligible": false,
          "reversed": false,
          "negative": true,
          "positive": false,
          "status": "supported"
        },
        "R1:A_random": {
          "estimate": -0.4345790016966252,
          "ci_level": 0.95,
          "ci": [
            -0.5685614252226605,
            -0.29833594768121047
          ],
          "equivalence_ci_level": 0.9,
          "equivalence_ci": [
            -0.5474222373008131,
            -0.31935825622204067
          ],
          "n": 80,
          "supported": true,
          "negligible": false,
          "reversed": false,
          "negative": true,
          "positive": false,
          "status": "supported"
        }
      },
      "S2": {
        "R1-M:X": {
          "estimate": -0.3007684611835709,
          "ci_level": 0.95,
          "ci": [
            -0.3595072696335147,
            -0.24198453695077318
          ],
          "equivalence_ci_level": 0.9,
          "equivalence_ci": [
            -0.3500512562372192,
            -0.2514838763240288
          ],
          "n": 80,
          "supported": true,
          "negligible": false,
          "reversed": false,
          "negative": true,
          "positive": false,
          "status": "supported"
        },
        "R1-M:A_technicality": {
          "estimate": -0.2862992407832918,
          "ci_level": 0.95,
          "ci": [
            -0.35102624459067017,
            -0.22395989592462115
          ],
          "equivalence_ci_level": 0.9,
          "equivalence_ci": [
            -0.3407332578658821,
            -0.23358952121564303
          ],
          "n": 80,
          "supported": true,
          "negligible": false,
          "reversed": false,
          "negative": true,
          "positive": false,
          "status": "supported"
        },
        "R1-M:A_random": {
          "estimate": -0.216732361687154,
          "ci_level": 0.95,
          "ci": [
            -0.27426068147079796,
            -0.15751364936815104
          ],
          "equivalence_ci_level": 0.9,
          "equivalence_ci": [
            -0.26450949271150825,
            -0.1675460334528089
          ],
          "n": 80,
          "supported": true,
          "negligible": false,
          "reversed": false,
          "negative": true,
          "positive": false,
          "status": "supported"
        }
      },
      "S5": {
        "R4:X": {
          "estimate": -0.0567356185144544,
          "ci_level": 0.95,
          "ci": [
            -0.134203249015098,
            0.01887537053169751
          ],
          "equivalence_ci_level": 0.9,
          "equivalence_ci": [
            -0.12140359150974028,
            0.007173336126515108
          ],
          "n": 80,
          "supported": true,
          "negligible": true,
          "reversed": false,
          "negative": false,
          "positive": false,
          "status": "supported"
        },
        "R4:A_technicality": {
          "estimate": -0.23443952265100992,
          "ci_level": 0.95,
          "ci": [
            -0.31478623793537625,
            -0.15019729667375456
          ],
          "equivalence_ci_level": 0.9,
          "equivalence_ci": [
            -0.3018550587420781,
            -0.1641365628040707
          ],
          "n": 80,
          "supported": false,
          "negligible": false,
          "reversed": false,
          "negative": true,
          "positive": false,
          "status": "inconclusive"
        },
        "R4:A_random": {
          "estimate": -0.11439708232184717,
          "ci_level": 0.95,
          "ci": [
            -0.20018212373190533,
            -0.02644857677303564
          ],
          "equivalence_ci_level": 0.9,
          "equivalence_ci": [
            -0.185606513113547,
            -0.0407848472071676
          ],
          "n": 80,
          "supported": false,
          "negligible": false,
          "reversed": false,
          "negative": true,
          "positive": false,
          "status": "inconclusive"
        }
      },
      "P3": {
        "P3:technicality": {
          "estimate": -0.03991863506660409,
          "ci_level": 0.9833,
          "ci": [
            -0.11793070365222612,
            0.03763591149413018
          ],
          "equivalence_ci_level": 0.9,
          "equivalence_ci": [
            -0.09225108639425944,
            0.012699096263355358
          ],
          "n": 80,
          "supported": false,
          "negligible": true,
          "reversed": false,
          "negative": false,
          "positive": false,
          "status": "negligible"
        },
        "P3:random": {
          "estimate": 0.022034601268964636,
          "ci_level": 0.9833,
          "ci": [
            -0.06237298551951206,
            0.10771405001360214
          ],
          "equivalence_ci_level": 0.9,
          "equivalence_ci": [
            -0.03565359562114909,
            0.08211739666481524
          ],
          "n": 80,
          "supported": false,
          "negligible": true,
          "reversed": false,
          "negative": false,
          "positive": false,
          "status": "negligible"
        }
      },
      "S3": {
        "S3:technicality": {
          "estimate": 0.010530271637657896,
          "ci_level": 0.95,
          "ci": [
            -0.0640971080248341,
            0.08410299548616831
          ],
          "equivalence_ci_level": 0.9,
          "equivalence_ci": [
            -0.05197769051143849,
            0.07237056359674968
          ],
          "n": 80,
          "supported": false,
          "negligible": true,
          "reversed": false,
          "negative": false,
          "positive": false,
          "status": "negligible"
        },
        "S3:random": {
          "estimate": -0.03811871786483763,
          "ci_level": 0.95,
          "ci": [
            -0.10977406051624482,
            0.03400146065393096
          ],
          "equivalence_ci_level": 0.9,
          "equivalence_ci": [
            -0.09899811782590069,
            0.022108863138562692
          ],
          "n": 80,
          "supported": false,
          "negligible": true,
          "reversed": false,
          "negative": false,
          "positive": false,
          "status": "negligible"
        }
      },
      "S4": {
        "S4:technicality": {
          "estimate": -0.433657175308234,
          "ci_level": 0.95,
          "ci": [
            -0.5436262703109923,
            -0.3232250777471379
          ],
          "equivalence_ci_level": 0.9,
          "equivalence_ci": [
            -0.5248994159064291,
            -0.3403613928690193
          ],
          "n": 80,
          "supported": true,
          "negligible": false,
          "reversed": false,
          "negative": true,
          "positive": false,
          "status": "supported"
        },
        "S4:random": {
          "estimate": -0.21784664000947124,
          "ci_level": 0.95,
          "ci": [
            -0.3262609796294227,
            -0.10749729626127881
          ],
          "equivalence_ci_level": 0.9,
          "equivalence_ci": [
            -0.30884075522678456,
            -0.12492016054646471
          ],
          "n": 80,
          "supported": true,
          "negligible": false,
          "reversed": false,
          "negative": true,
          "positive": false,
          "status": "supported"
        }
      }
    },
    "hypotheses": {
      "P1": {
        "supported": true,
        "negligible": false,
        "reversed": false,
        "status": "supported"
      },
      "P2": {
        "supported": true,
        "negligible": false,
        "reversed": false,
        "status": "supported"
      },
      "S1": {
        "supported": true,
        "negligible": false,
        "reversed": false,
        "status": "supported"
      },
      "S2": {
        "supported": true,
        "negligible": false,
        "reversed": false,
        "status": "supported"
      },
      "S5": {
        "supported": false,
        "negligible": false,
        "reversed": false,
        "status": "inconclusive"
      },
      "P3": {
        "supported": false,
        "negligible": true,
        "reversed": false,
        "status": "negligible"
      },
      "S3": {
        "supported": false,
        "negligible": true,
        "reversed": false,
        "status": "negligible"
      },
      "S4": {
        "supported": true,
        "negligible": false,
        "reversed": false,
        "status": "supported"
      }
    },
    "reading": "Both historical placements retain influence. Direct P3 contrast: negligible.",
    "missing_policy": "Required missing cells make affected components not estimable; no outcome-based exclusions.",
    "bootstrap_resamples": 10000
  },
  "descriptive": {
    "R1/unsteered": {
      "EH_answer": {
        "n": 80,
        "mean": 0.06731781440321356
      },
      "answer_length": {
        "n": 80,
        "mean": 145.5625
      },
      "answer_truncated": {
        "n": 80,
        "mean": 0.35
      },
      "valid_digit_mass": [
        1.0,
        0.9999997019767761,
        0.9999997615814209,
        0.9999998807907104,
        1.0,
        0.9999989867210388,
        1.0000001192092896,
        1.0000001192092896,
        0.9999999403953552,
        1.0,
        1.0,
        0.9999887943267822,
        1.0,
        0.9999997615814209,
        0.9999999403953552,
        0.9999999403953552,
        0.9999728202819824,
        0.999999463558197,
        0.9999997019767761,
        0.9999992847442627,
        0.9999993443489075,
        1.0,
        0.9999984502792358,
        0.9999865889549255,
        0.9999991059303284,
        0.9999999403953552,
        0.9999995827674866,
        0.9999889135360718,
        1.0,
        0.9999999403953552,
        0.9999998807907104,
        0.9999998807907104,
        0.9999984502792358,
        0.9999997615814209,
        0.9999993443489075,
        0.9999997615814209,
        0.9999996423721313,
        0.9999998211860657,
        1.0,
        0.9999975562095642,
        0.9999999403953552,
        0.9999849200248718,
        1.0,
        0.9999997615814209,
        0.9999995827674866,
        0.9999997615814209,
        0.9999998807907104,
        0.9999989867210388,
        0.9999783635139465,
        0.999999463558197,
        1.0,
        0.9999983906745911,
        0.9999998807907104,
        0.9999998807907104,
        0.9999974966049194,
        0.9999997019767761,
        0.9999947547912598,
        0.9999998211860657,
        0.9999985694885254,
        0.9999999403953552,
        1.0,
        1.0,
        1.0,
        1.0,
        0.9999990463256836,
        0.9999999403953552,
        0.9999995827674866,
        0.9999998807907104,
        0.9999999403953552,
        0.9999998807907104,
        1.0,
        1.0,
        0.9999999403953552,
        1.0,
        1.0,
        0.9999999403953552,
        1.0,
        0.9999999403953552,
        0.9999998807907104,
        0.9999998807907104
      ],
      "baseline_mean": 7.641513732172385,
      "baseline_sd": 0.5342258848137873,
      "structural": {
        "n": 16,
        "records": [
          {
            "prompt_id": "s4t06",
            "order_averaged_probabilities": {
              "A": 0.12695911826449446,
              "B": 0.5248590763658285,
              "C": 0.34818177577108145
            },
            "correct_probability": 0.5248590763658285,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999997615814209
            ]
          },
          {
            "prompt_id": "s4t09",
            "order_averaged_probabilities": {
              "A": 0.0004908662085654214,
              "B": 0.9977083206176758,
              "C": 0.0018008203187491745
            },
            "correct_probability": 0.9977083206176758,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t17",
            "order_averaged_probabilities": {
              "A": 0.5052612391300499,
              "B": 0.4897606316371821,
              "C": 0.004978084471076727
            },
            "correct_probability": 0.4897606316371821,
            "correct_argmax": false,
            "valid_mass": [
              0.9999998807907104,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t18",
            "order_averaged_probabilities": {
              "A": 0.04762926388593769,
              "B": 0.49153105152072385,
              "C": 0.46083967480808496
            },
            "correct_probability": 0.49153105152072385,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999997615814209
            ]
          },
          {
            "prompt_id": "s4t25",
            "order_averaged_probabilities": {
              "A": 0.08659068837823725,
              "B": 0.8014755249023438,
              "C": 0.1119337857235223
            },
            "correct_probability": 0.8014755249023438,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t28",
            "order_averaged_probabilities": {
              "A": 0.051856640944606625,
              "B": 0.5635950937867165,
              "C": 0.38454827573150396
            },
            "correct_probability": 0.5635950937867165,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t43",
            "order_averaged_probabilities": {
              "A": 0.28044787903718316,
              "B": 0.500865759793669,
              "C": 0.21868634261772968
            },
            "correct_probability": 0.500865759793669,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t46",
            "order_averaged_probabilities": {
              "A": 0.498800167668378,
              "B": 0.49661731552998845,
              "C": 0.004582486464641988
            },
            "correct_probability": 0.49661731552998845,
            "correct_argmax": false,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t48",
            "order_averaged_probabilities": {
              "A": 0.36502248236411106,
              "B": 0.4986613065120764,
              "C": 0.13631625310517848
            },
            "correct_probability": 0.4986613065120764,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999997615814209
            ]
          },
          {
            "prompt_id": "s4t49",
            "order_averaged_probabilities": {
              "A": 0.4470118622703012,
              "B": 0.49889527447521687,
              "C": 0.05409286404028535
            },
            "correct_probability": 0.49889527447521687,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t52",
            "order_averaged_probabilities": {
              "A": 0.00010598588960419875,
              "B": 0.9842768311500549,
              "C": 0.015617172874044627
            },
            "correct_probability": 0.9842768311500549,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t54",
            "order_averaged_probabilities": {
              "A": 0.1269325442626723,
              "B": 0.4981925543397665,
              "C": 0.3748748805373907
            },
            "correct_probability": 0.4981925543397665,
            "correct_argmax": true,
            "valid_mass": [
              0.9999998807907104,
              0.999998927116394
            ]
          },
          {
            "prompt_id": "s4t56",
            "order_averaged_probabilities": {
              "A": 0.27901745268900413,
              "B": 0.4967828248627484,
              "C": 0.2241997574456036
            },
            "correct_probability": 0.4967828248627484,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999997615814209
            ]
          },
          {
            "prompt_id": "s4t73",
            "order_averaged_probabilities": {
              "A": 0.00013083478489761546,
              "B": 0.9998127818107605,
              "C": 5.6389366363873705e-05
            },
            "correct_probability": 0.9998127818107605,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t74",
            "order_averaged_probabilities": {
              "A": 0.0024837494711391628,
              "B": 0.9954812526702881,
              "C": 0.0020350162521936
            },
            "correct_probability": 0.9954812526702881,
            "correct_argmax": true,
            "valid_mass": [
              1.0000001192092896,
              1.0
            ]
          },
          {
            "prompt_id": "s4t75",
            "order_averaged_probabilities": {
              "A": 0.020087374141439795,
              "B": 0.9731808602809906,
              "C": 0.006731805158779025
            },
            "correct_probability": 0.9731808602809906,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          }
        ],
        "mean_correct_probability": 0.6757310287660019
      },
      "source": {
        "n": 16,
        "records": [
          {
            "prompt_id": "s4t06",
            "order_averaged_probabilities": {
              "A": 0.5595963969826698,
              "B": 0.4404035792663308
            },
            "correct_probability": 0.5595963969826698,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t09",
            "order_averaged_probabilities": {
              "A": 0.9994069039821625,
              "B": 0.0005931058631176711
            },
            "correct_probability": 0.9994069039821625,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t17",
            "order_averaged_probabilities": {
              "A": 0.8941310942173004,
              "B": 0.1058688722550869
            },
            "correct_probability": 0.8941310942173004,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t18",
            "order_averaged_probabilities": {
              "A": 0.9403847455978394,
              "B": 0.059615231222778675
            },
            "correct_probability": 0.9403847455978394,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t25",
            "order_averaged_probabilities": {
              "A": 0.3113313895009924,
              "B": 0.6886686235666275
            },
            "correct_probability": 0.3113313895009924,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t28",
            "order_averaged_probabilities": {
              "A": 0.6587270051240921,
              "B": 0.3412730023264885
            },
            "correct_probability": 0.6587270051240921,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t43",
            "order_averaged_probabilities": {
              "A": 0.48141575213958276,
              "B": 0.5185842290520668
            },
            "correct_probability": 0.48141575213958276,
            "correct_argmax": false,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t46",
            "order_averaged_probabilities": {
              "A": 0.9987629950046539,
              "B": 0.0012369972207011415
            },
            "correct_probability": 0.9987629950046539,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t48",
            "order_averaged_probabilities": {
              "A": 0.8884822726249695,
              "B": 0.11151774949394166
            },
            "correct_probability": 0.8884822726249695,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t49",
            "order_averaged_probabilities": {
              "A": 0.6080036610364914,
              "B": 0.39199636597186327
            },
            "correct_probability": 0.6080036610364914,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t52",
            "order_averaged_probabilities": {
              "A": 0.1002058619633317,
              "B": 0.8997941017150879
            },
            "correct_probability": 0.1002058619633317,
            "correct_argmax": false,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t54",
            "order_averaged_probabilities": {
              "A": 0.15818365290760994,
              "B": 0.8418163657188416
            },
            "correct_probability": 0.15818365290760994,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t56",
            "order_averaged_probabilities": {
              "A": 0.5725492909550667,
              "B": 0.42745066434144974
            },
            "correct_probability": 0.5725492909550667,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t73",
            "order_averaged_probabilities": {
              "A": 0.9944981932640076,
              "B": 0.005501822576661652
            },
            "correct_probability": 0.9944981932640076,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t74",
            "order_averaged_probabilities": {
              "A": 0.9954172968864441,
              "B": 0.0045827372232452035
            },
            "correct_probability": 0.9954172968864441,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t75",
            "order_averaged_probabilities": {
              "A": 0.9807517826557159,
              "B": 0.019248198776040226
            },
            "correct_probability": 0.9807517826557159,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          }
        ],
        "mean_correct_probability": 0.6963655184276831
      }
    },
    "R1/hostility": {
      "EH_answer": {
        "n": 80,
        "mean": 0.11652991898081382
      },
      "answer_length": {
        "n": 80,
        "mean": 153.325
      },
      "answer_truncated": {
        "n": 80,
        "mean": 0.45
      },
      "valid_digit_mass": [
        0.9999998807907104,
        1.0,
        1.0,
        0.9999998807907104,
        0.9999998807907104,
        0.9999998807907104,
        1.0,
        1.0,
        1.0000001192092896,
        1.0,
        1.0,
        0.9999986886978149,
        1.0,
        0.9999999403953552,
        1.0,
        1.0,
        0.9999997615814209,
        0.9999994039535522,
        1.0,
        0.9999999403953552,
        0.9999999403953552,
        0.9999998807907104,
        0.9999970197677612,
        1.0,
        1.0,
        0.9999999403953552,
        0.9999999403953552,
        1.0000001192092896,
        0.9999998807907104,
        1.0,
        0.9999998807907104,
        1.0,
        1.0,
        1.0,
        1.0000001192092896,
        0.9999997615814209,
        0.9999999403953552,
        0.9999997019767761,
        0.9999999403953552,
        0.9999997615814209,
        1.0,
        0.9999992251396179,
        1.0,
        1.0000001192092896,
        1.0000001192092896,
        1.0,
        1.0,
        0.9999999403953552,
        1.0,
        0.9999999403953552,
        1.0,
        1.0,
        1.0000001192092896,
        1.0,
        0.9999937415122986,
        1.0000001192092896,
        1.0,
        1.0,
        0.9999998211860657,
        0.9999998807907104,
        0.9999999403953552,
        0.9999998211860657,
        0.9999999403953552,
        1.0,
        0.9999994039535522,
        1.0,
        0.9999997615814209,
        0.9999998807907104,
        1.0000001192092896,
        1.0,
        1.0,
        1.0000001192092896,
        0.9999998807907104,
        1.0,
        0.9999998807907104,
        1.0,
        0.9999999403953552,
        1.0000001192092896,
        0.9999989867210388,
        1.0
      ],
      "baseline_mean": null,
      "baseline_sd": null,
      "structural": {
        "n": 16,
        "records": [
          {
            "prompt_id": "s4t06",
            "order_averaged_probabilities": {
              "A": 0.045369593281066045,
              "B": 0.6212598830461502,
              "C": 0.3333705309778452
            },
            "correct_probability": 0.6212598830461502,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999998211860657
            ]
          },
          {
            "prompt_id": "s4t09",
            "order_averaged_probabilities": {
              "A": 0.02232531761330847,
              "B": 0.8491061627864838,
              "C": 0.12856852801633067
            },
            "correct_probability": 0.8491061627864838,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t17",
            "order_averaged_probabilities": {
              "A": 0.1571704624220729,
              "B": 0.5073440186679363,
              "C": 0.3354855668731034
            },
            "correct_probability": 0.5073440186679363,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              0.9999994039535522
            ]
          },
          {
            "prompt_id": "s4t18",
            "order_averaged_probabilities": {
              "A": 0.4966555060527753,
              "B": 0.49903615114453714,
              "C": 0.004308355855755508
            },
            "correct_probability": 0.49903615114453714,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              1.0000001192092896
            ]
          },
          {
            "prompt_id": "s4t25",
            "order_averaged_probabilities": {
              "A": 0.403977603470139,
              "B": 0.5255457740277052,
              "C": 0.07047663716366515
            },
            "correct_probability": 0.5255457740277052,
            "correct_argmax": true,
            "valid_mass": [
              0.9999998807907104,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t28",
            "order_averaged_probabilities": {
              "A": 7.669440310564823e-05,
              "B": 0.9919286370277405,
              "C": 0.007994684565346688
            },
            "correct_probability": 0.9919286370277405,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t43",
            "order_averaged_probabilities": {
              "A": 0.08659461730485418,
              "B": 0.6104275286197662,
              "C": 0.30297784216236323
            },
            "correct_probability": 0.6104275286197662,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              0.9999997615814209
            ]
          },
          {
            "prompt_id": "s4t46",
            "order_averaged_probabilities": {
              "A": 0.4973900640652573,
              "B": 0.4990365970361381,
              "C": 0.003573332622181624
            },
            "correct_probability": 0.4990365970361381,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t48",
            "order_averaged_probabilities": {
              "A": 0.24985380238489796,
              "B": 0.4998369307431858,
              "C": 0.2503092557308264
            },
            "correct_probability": 0.4998369307431858,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t49",
            "order_averaged_probabilities": {
              "A": 0.31060463428730145,
              "B": 0.4921138708014041,
              "C": 0.19728151429444551
            },
            "correct_probability": 0.4921138708014041,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              0.9999998807907104
            ]
          },
          {
            "prompt_id": "s4t52",
            "order_averaged_probabilities": {
              "A": 0.18314391121748486,
              "B": 0.5123718213289976,
              "C": 0.30448427237570286
            },
            "correct_probability": 0.5123718213289976,
            "correct_argmax": true,
            "valid_mass": [
              1.0000001192092896,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t54",
            "order_averaged_probabilities": {
              "A": 0.021970367641188204,
              "B": 0.5073018856346607,
              "C": 0.4707277864217758
            },
            "correct_probability": 0.5073018856346607,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999998211860657
            ]
          },
          {
            "prompt_id": "s4t56",
            "order_averaged_probabilities": {
              "A": 0.16027592352656939,
              "B": 0.4961926282849163,
              "C": 0.34353142976760864
            },
            "correct_probability": 0.4961926282849163,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999998807907104
            ]
          },
          {
            "prompt_id": "s4t73",
            "order_averaged_probabilities": {
              "A": 0.0016604499833192676,
              "B": 0.996173620223999,
              "C": 0.002165987156331539
            },
            "correct_probability": 0.996173620223999,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0000001192092896
            ]
          },
          {
            "prompt_id": "s4t74",
            "order_averaged_probabilities": {
              "A": 0.0036873164353892207,
              "B": 0.9937068819999695,
              "C": 0.0026058443472720683
            },
            "correct_probability": 0.9937068819999695,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t75",
            "order_averaged_probabilities": {
              "A": 0.0004150855020270683,
              "B": 0.995389997959137,
              "C": 0.004194962093606591
            },
            "correct_probability": 0.995389997959137,
            "correct_argmax": true,
            "valid_mass": [
              1.0000001192092896,
              1.0
            ]
          }
        ],
        "mean_correct_probability": 0.6622982743332955
      },
      "source": {
        "n": 16,
        "records": [
          {
            "prompt_id": "s4t06",
            "order_averaged_probabilities": {
              "A": 0.49670163783594035,
              "B": 0.5032983841374516
            },
            "correct_probability": 0.49670163783594035,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t09",
            "order_averaged_probabilities": {
              "A": 0.8650738000869751,
              "B": 0.13492624173522927
            },
            "correct_probability": 0.8650738000869751,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t17",
            "order_averaged_probabilities": {
              "A": 0.8175744414329529,
              "B": 0.18242551386356354
            },
            "correct_probability": 0.8175744414329529,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t18",
            "order_averaged_probabilities": {
              "A": 0.9999383091926575,
              "B": 6.17019162216792e-05
            },
            "correct_probability": 0.9999383091926575,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t25",
            "order_averaged_probabilities": {
              "A": 0.4705414213822223,
              "B": 0.529458574950695
            },
            "correct_probability": 0.4705414213822223,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t28",
            "order_averaged_probabilities": {
              "A": 0.7790532112121582,
              "B": 0.22094683605246246
            },
            "correct_probability": 0.7790532112121582,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t43",
            "order_averaged_probabilities": {
              "A": 0.7733005881309509,
              "B": 0.22669943049550056
            },
            "correct_probability": 0.7733005881309509,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t46",
            "order_averaged_probabilities": {
              "A": 0.9979648888111115,
              "B": 0.002035125314126418
            },
            "correct_probability": 0.9979648888111115,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t48",
            "order_averaged_probabilities": {
              "A": 0.8655292987823486,
              "B": 0.13447071629789997
            },
            "correct_probability": 0.8655292987823486,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t49",
            "order_averaged_probabilities": {
              "A": 0.5736687704920769,
              "B": 0.4263312010152731
            },
            "correct_probability": 0.5736687704920769,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t52",
            "order_averaged_probabilities": {
              "A": 0.46468097530305386,
              "B": 0.5353190638124943
            },
            "correct_probability": 0.46468097530305386,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0000001192092896
            ]
          },
          {
            "prompt_id": "s4t54",
            "order_averaged_probabilities": {
              "A": 0.8787438869476318,
              "B": 0.12125608325004578
            },
            "correct_probability": 0.8787438869476318,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t56",
            "order_averaged_probabilities": {
              "A": 0.28232457453850657,
              "B": 0.7176754772663116
            },
            "correct_probability": 0.28232457453850657,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t73",
            "order_averaged_probabilities": {
              "A": 0.9510889649391174,
              "B": 0.0489110458875075
            },
            "correct_probability": 0.9510889649391174,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t74",
            "order_averaged_probabilities": {
              "A": 0.9904221296310425,
              "B": 0.00957786018261686
            },
            "correct_probability": 0.9904221296310425,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t75",
            "order_averaged_probabilities": {
              "A": 0.8853035271167755,
              "B": 0.11469649989157915
            },
            "correct_probability": 0.8853035271167755,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          }
        ],
        "mean_correct_probability": 0.7557444016147201
      }
    },
    "R1/technicality": {
      "EH_answer": {
        "n": 80,
        "mean": 0.07129111473768716
      },
      "answer_length": {
        "n": 80,
        "mean": 174.65
      },
      "answer_truncated": {
        "n": 80,
        "mean": 0.5625
      },
      "valid_digit_mass": [
        0.9999997615814209,
        0.9999995231628418,
        0.9999998807907104,
        0.9999997615814209,
        0.9999987483024597,
        0.999999463558197,
        0.9999998807907104,
        1.0,
        0.9999996423721313,
        0.9999998807907104,
        1.0,
        0.999991238117218,
        0.9999996423721313,
        0.9999982118606567,
        1.0,
        0.9999999403953552,
        0.999999463558197,
        0.9999997019767761,
        0.9999998807907104,
        0.9999992251396179,
        0.9999998211860657,
        0.9999998807907104,
        0.9999988675117493,
        0.9999966025352478,
        0.9999999403953552,
        0.9999998211860657,
        0.9999969601631165,
        0.9999979734420776,
        0.9999998211860657,
        1.0,
        1.0,
        1.0,
        0.9999866485595703,
        1.0,
        0.9999999403953552,
        0.9999998807907104,
        0.9999995231628418,
        0.9999999403953552,
        0.9999996423721313,
        0.9999967813491821,
        0.9999999403953552,
        0.9998891353607178,
        0.9999997615814209,
        0.9999997615814209,
        0.9999998211860657,
        0.9999998807907104,
        1.0,
        0.9999995827674866,
        0.9999933242797852,
        0.9999997615814209,
        1.0,
        0.9999998807907104,
        0.9999998211860657,
        1.0,
        0.9999972581863403,
        0.9999997615814209,
        0.9999976754188538,
        0.9999998807907104,
        0.9999994039535522,
        1.0,
        0.9999996423721313,
        1.0,
        0.9999997615814209,
        0.9999999403953552,
        0.9999989867210388,
        0.9999999403953552,
        0.9999987483024597,
        0.9999998807907104,
        0.9999998807907104,
        1.0,
        0.9999998807907104,
        0.9999998807907104,
        1.0,
        1.0,
        0.9999994039535522,
        0.9999998211860657,
        0.9999999403953552,
        0.9999999403953552,
        0.9999997019767761,
        0.9999998807907104
      ],
      "baseline_mean": null,
      "baseline_sd": null,
      "structural": {
        "n": 16,
        "records": [
          {
            "prompt_id": "s4t06",
            "order_averaged_probabilities": {
              "A": 0.030342856392962858,
              "B": 0.863750159740448,
              "C": 0.10590698174200952
            },
            "correct_probability": 0.863750159740448,
            "correct_argmax": true,
            "valid_mass": [
              1.0000001192092896,
              0.9999998807907104
            ]
          },
          {
            "prompt_id": "s4t09",
            "order_averaged_probabilities": {
              "A": 0.02433450016360439,
              "B": 0.6786016374826431,
              "C": 0.29706383839948103
            },
            "correct_probability": 0.6786016374826431,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              0.9999997615814209
            ]
          },
          {
            "prompt_id": "s4t17",
            "order_averaged_probabilities": {
              "A": 0.6441479176282883,
              "B": 0.316956777125597,
              "C": 0.03889534808695316
            },
            "correct_probability": 0.316956777125597,
            "correct_argmax": false,
            "valid_mass": [
              0.9999998807907104,
              1.0
            ]
          },
          {
            "prompt_id": "s4t18",
            "order_averaged_probabilities": {
              "A": 0.3370643498492427,
              "B": 0.49259229050949216,
              "C": 0.17034335061907768
            },
            "correct_probability": 0.49259229050949216,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999997615814209
            ]
          },
          {
            "prompt_id": "s4t25",
            "order_averaged_probabilities": {
              "A": 0.05938794673210168,
              "B": 0.5008297245949507,
              "C": 0.4397823282633908
            },
            "correct_probability": 0.5008297245949507,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t28",
            "order_averaged_probabilities": {
              "A": 0.0354883506661281,
              "B": 0.7490878403186798,
              "C": 0.2154238000512123
            },
            "correct_probability": 0.7490878403186798,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t43",
            "order_averaged_probabilities": {
              "A": 0.4964549267933762,
              "B": 0.4992367394006578,
              "C": 0.004308335424866527
            },
            "correct_probability": 0.4992367394006578,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t46",
            "order_averaged_probabilities": {
              "A": 0.5052008363418281,
              "B": 0.48915013444639044,
              "C": 0.005649042228469625
            },
            "correct_probability": 0.48915013444639044,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t48",
            "order_averaged_probabilities": {
              "A": 0.20999250811291859,
              "B": 0.5123384278267622,
              "C": 0.2776690926402807
            },
            "correct_probability": 0.5123384278267622,
            "correct_argmax": true,
            "valid_mass": [
              0.9999998211860657,
              0.9999993443489075
            ]
          },
          {
            "prompt_id": "s4t49",
            "order_averaged_probabilities": {
              "A": 0.4977183660957962,
              "B": 0.47946023289114237,
              "C": 0.02282139426097274
            },
            "correct_probability": 0.47946023289114237,
            "correct_argmax": false,
            "valid_mass": [
              0.9999998211860657,
              1.0
            ]
          },
          {
            "prompt_id": "s4t52",
            "order_averaged_probabilities": {
              "A": 0.28428392205296404,
              "B": 0.5810801163315773,
              "C": 0.13463598606176674
            },
            "correct_probability": 0.5810801163315773,
            "correct_argmax": true,
            "valid_mass": [
              1.0000001192092896,
              1.0
            ]
          },
          {
            "prompt_id": "s4t54",
            "order_averaged_probabilities": {
              "A": 0.2161558403968229,
              "B": 0.5009313314221799,
              "C": 0.2829127977602184
            },
            "correct_probability": 0.5009313314221799,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              0.9999997615814209
            ]
          },
          {
            "prompt_id": "s4t56",
            "order_averaged_probabilities": {
              "A": 0.1512465886771679,
              "B": 0.5968759804964066,
              "C": 0.2518774615600705
            },
            "correct_probability": 0.5968759804964066,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t73",
            "order_averaged_probabilities": {
              "A": 1.907135265355464e-05,
              "B": 0.9998818039894104,
              "C": 9.911857341649011e-05
            },
            "correct_probability": 0.9998818039894104,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t74",
            "order_averaged_probabilities": {
              "A": 0.019190065329894423,
              "B": 0.9783203601837158,
              "C": 0.0024895519600249827
            },
            "correct_probability": 0.9783203601837158,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t75",
            "order_averaged_probabilities": {
              "A": 0.05191871523857117,
              "B": 0.9385588765144348,
              "C": 0.009522419073618948
            },
            "correct_probability": 0.9385588765144348,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          }
        ],
        "mean_correct_probability": 0.6361032770796555
      },
      "source": {
        "n": 16,
        "records": [
          {
            "prompt_id": "s4t06",
            "order_averaged_probabilities": {
              "A": 0.7499969005584717,
              "B": 0.2500030720871109
            },
            "correct_probability": 0.7499969005584717,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t09",
            "order_averaged_probabilities": {
              "A": 0.9987632930278778,
              "B": 0.0012367275061535565
            },
            "correct_probability": 0.9987632930278778,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t17",
            "order_averaged_probabilities": {
              "A": 0.5595222488045692,
              "B": 0.4404777323870803
            },
            "correct_probability": 0.5595222488045692,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t18",
            "order_averaged_probabilities": {
              "A": 0.9853436350822449,
              "B": 0.014656367497025258
            },
            "correct_probability": 0.9853436350822449,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t25",
            "order_averaged_probabilities": {
              "A": 0.5004541315720417,
              "B": 0.49954584379156586
            },
            "correct_probability": 0.5004541315720417,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t28",
            "order_averaged_probabilities": {
              "A": 0.6489219814538956,
              "B": 0.35107804276049137
            },
            "correct_probability": 0.6489219814538956,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t43",
            "order_averaged_probabilities": {
              "A": 0.9403966665267944,
              "B": 0.05960332669712898
            },
            "correct_probability": 0.9403966665267944,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t46",
            "order_averaged_probabilities": {
              "A": 0.9762870073318481,
              "B": 0.02371297091681157
            },
            "correct_probability": 0.9762870073318481,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t48",
            "order_averaged_probabilities": {
              "A": 0.547669667750597,
              "B": 0.4523303196742745
            },
            "correct_probability": 0.547669667750597,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t49",
            "order_averaged_probabilities": {
              "A": 0.5002729218686,
              "B": 0.4997270776075311
            },
            "correct_probability": 0.5002729218686,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t52",
            "order_averaged_probabilities": {
              "A": 0.0017139584524556994,
              "B": 0.9982860088348389
            },
            "correct_probability": 0.0017139584524556994,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t54",
            "order_averaged_probabilities": {
              "A": 0.4636572535382584,
              "B": 0.5363427437841892
            },
            "correct_probability": 0.4636572535382584,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t56",
            "order_averaged_probabilities": {
              "A": 0.499999962747097,
              "B": 0.499999962747097
            },
            "correct_probability": 0.499999962747097,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t73",
            "order_averaged_probabilities": {
              "A": 0.9993687570095062,
              "B": 0.0006312245095614344
            },
            "correct_probability": 0.9993687570095062,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t74",
            "order_averaged_probabilities": {
              "A": 0.9940435588359833,
              "B": 0.005956488661468029
            },
            "correct_probability": 0.9940435588359833,
            "correct_argmax": true,
            "valid_mass": [
              1.0000001192092896,
              1.0
            ]
          },
          {
            "prompt_id": "s4t75",
            "order_averaged_probabilities": {
              "A": 0.9827338457107544,
              "B": 0.017266178503632545
            },
            "correct_probability": 0.9827338457107544,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0000001192092896
            ]
          }
        ],
        "mean_correct_probability": 0.7093216118919372
      }
    },
    "R1/random": {
      "EH_answer": {
        "n": 80,
        "mean": 0.06686314348480664
      },
      "answer_length": {
        "n": 80,
        "mean": 149.375
      },
      "answer_truncated": {
        "n": 80,
        "mean": 0.4125
      },
      "valid_digit_mass": [
        0.9999998807907104,
        0.9999998807907104,
        0.9999997019767761,
        0.9999998807907104,
        0.9999999403953552,
        0.9999988675117493,
        0.9999998807907104,
        1.0000001192092896,
        0.9999998807907104,
        0.9999998807907104,
        0.9999999403953552,
        0.9997991323471069,
        0.9999999403953552,
        0.999999463558197,
        1.0,
        1.0,
        0.9999986290931702,
        0.9999995231628418,
        0.9999998807907104,
        0.9999895691871643,
        0.9999996423721313,
        1.0,
        0.9999999403953552,
        0.9999989867210388,
        0.9999995231628418,
        0.9999998807907104,
        0.9999999403953552,
        0.9999978542327881,
        0.9999998807907104,
        0.9999997019767761,
        0.9999998807907104,
        1.0,
        0.9999997615814209,
        0.9999999403953552,
        0.9999996423721313,
        0.9999994039535522,
        0.9999996423721313,
        0.9999998807907104,
        0.9999997615814209,
        0.9999880194664001,
        0.9999997615814209,
        0.9999967813491821,
        0.9999990463256836,
        0.999999463558197,
        0.9999998807907104,
        1.0,
        0.999998927116394,
        0.999998152256012,
        0.9999803304672241,
        0.9999958276748657,
        0.9999999403953552,
        0.9999997615814209,
        0.9999967217445374,
        1.0,
        0.9999988079071045,
        0.9999993443489075,
        0.9999990463256836,
        1.0,
        0.9999992847442627,
        1.0000001192092896,
        0.9999998211860657,
        1.0,
        0.9999998211860657,
        1.0000001192092896,
        0.9999998807907104,
        1.0,
        0.9999998807907104,
        1.0,
        0.9999998807907104,
        0.9999998807907104,
        0.9999999403953552,
        0.9999998211860657,
        0.9999999403953552,
        1.0,
        0.9999997615814209,
        1.0,
        0.9999999403953552,
        0.9999999403953552,
        0.9999985694885254,
        0.9999998807907104
      ],
      "baseline_mean": null,
      "baseline_sd": null,
      "structural": {
        "n": 16,
        "records": [
          {
            "prompt_id": "s4t06",
            "order_averaged_probabilities": {
              "A": 0.004548240842268569,
              "B": 0.58875772356987,
              "C": 0.40669404540676624
            },
            "correct_probability": 0.58875772356987,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t09",
            "order_averaged_probabilities": {
              "A": 0.1548486913088709,
              "B": 0.6903026401996613,
              "C": 0.1548486913088709
            },
            "correct_probability": 0.6903026401996613,
            "correct_argmax": true,
            "valid_mass": [
              1.0000001192092896,
              0.9999998807907104
            ]
          },
          {
            "prompt_id": "s4t17",
            "order_averaged_probabilities": {
              "A": 0.5124641582369804,
              "B": 0.4616992473602295,
              "C": 0.025836562737822533
            },
            "correct_probability": 0.4616992473602295,
            "correct_argmax": false,
            "valid_mass": [
              0.9999998807907104,
              0.9999998807907104
            ]
          },
          {
            "prompt_id": "s4t18",
            "order_averaged_probabilities": {
              "A": 0.0740019821732858,
              "B": 0.4815592685336014,
              "C": 0.444438686594367
            },
            "correct_probability": 0.4815592685336014,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999998807907104
            ]
          },
          {
            "prompt_id": "s4t25",
            "order_averaged_probabilities": {
              "A": 0.0035013777669519186,
              "B": 0.9863288104534149,
              "C": 0.010169770917855203
            },
            "correct_probability": 0.9863288104534149,
            "correct_argmax": true,
            "valid_mass": [
              1.0000001192092896,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t28",
            "order_averaged_probabilities": {
              "A": 0.011741592170437798,
              "B": 0.8761174380779266,
              "C": 0.11214094585739076
            },
            "correct_probability": 0.8761174380779266,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t43",
            "order_averaged_probabilities": {
              "A": 0.24225720736211542,
              "B": 0.5152709651738405,
              "C": 0.24247180041857064
            },
            "correct_probability": 0.5152709651738405,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999998211860657
            ]
          },
          {
            "prompt_id": "s4t46",
            "order_averaged_probabilities": {
              "A": 0.4885140174010303,
              "B": 0.4853497150033945,
              "C": 0.026136265136301517
            },
            "correct_probability": 0.4853497150033945,
            "correct_argmax": false,
            "valid_mass": [
              0.9999998807907104,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t48",
            "order_averaged_probabilities": {
              "A": 0.4399487322912137,
              "B": 0.49847610713914037,
              "C": 0.061575112165883183
            },
            "correct_probability": 0.49847610713914037,
            "correct_argmax": true,
            "valid_mass": [
              1.0000001192092896,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t49",
            "order_averaged_probabilities": {
              "A": 0.49211720330640674,
              "B": 0.48187317850533873,
              "C": 0.026009613648056984
            },
            "correct_probability": 0.48187317850533873,
            "correct_argmax": false,
            "valid_mass": [
              0.9999998211860657,
              1.0
            ]
          },
          {
            "prompt_id": "s4t52",
            "order_averaged_probabilities": {
              "A": 0.4983456867566929,
              "B": 0.499612769097439,
              "C": 0.002041606872808188
            },
            "correct_probability": 0.499612769097439,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0000001192092896
            ]
          },
          {
            "prompt_id": "s4t54",
            "order_averaged_probabilities": {
              "A": 0.046944314970460255,
              "B": 0.4934482267126441,
              "C": 0.4596074456349015
            },
            "correct_probability": 0.4934482267126441,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999997019767761
            ]
          },
          {
            "prompt_id": "s4t56",
            "order_averaged_probabilities": {
              "A": 0.03297231311444193,
              "B": 0.5653426200151443,
              "C": 0.4016850106418133
            },
            "correct_probability": 0.5653426200151443,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              0.9999997615814209
            ]
          },
          {
            "prompt_id": "s4t73",
            "order_averaged_probabilities": {
              "A": 0.0006137460404715966,
              "B": 0.9992183446884155,
              "C": 0.00016786339620011859
            },
            "correct_probability": 0.9992183446884155,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t74",
            "order_averaged_probabilities": {
              "A": 0.004865989787504077,
              "B": 0.9934276342391968,
              "C": 0.001706405426375568
            },
            "correct_probability": 0.9934276342391968,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t75",
            "order_averaged_probabilities": {
              "A": 0.0021003082947572693,
              "B": 0.9919572174549103,
              "C": 0.005942547926679254
            },
            "correct_probability": 0.9919572174549103,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0000001192092896
            ]
          }
        ],
        "mean_correct_probability": 0.6630463691390105
      },
      "source": {
        "n": 16,
        "records": [
          {
            "prompt_id": "s4t06",
            "order_averaged_probabilities": {
              "A": 0.018002540804445744,
              "B": 0.9819974601268768
            },
            "correct_probability": 0.018002540804445744,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t09",
            "order_averaged_probabilities": {
              "A": 0.9997234642505646,
              "B": 0.00027650841741433396
            },
            "correct_probability": 0.9997234642505646,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t17",
            "order_averaged_probabilities": {
              "A": 0.7179483771324158,
              "B": 0.28205163014354184
            },
            "correct_probability": 0.7179483771324158,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t18",
            "order_averaged_probabilities": {
              "A": 0.9507389068603516,
              "B": 0.04926107556093484
            },
            "correct_probability": 0.9507389068603516,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t25",
            "order_averaged_probabilities": {
              "A": 0.5007481051725335,
              "B": 0.4992518886720063
            },
            "correct_probability": 0.5007481051725335,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t28",
            "order_averaged_probabilities": {
              "A": 0.5040073171257973,
              "B": 0.49599264934659004
            },
            "correct_probability": 0.5040073171257973,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t43",
            "order_averaged_probabilities": {
              "A": 0.39414341235533357,
              "B": 0.6058566123247147
            },
            "correct_probability": 0.39414341235533357,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t46",
            "order_averaged_probabilities": {
              "A": 0.9762763381004333,
              "B": 0.02372365926294151
            },
            "correct_probability": 0.9762763381004333,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t48",
            "order_averaged_probabilities": {
              "A": 0.8649370074272156,
              "B": 0.13506301119923592
            },
            "correct_probability": 0.8649370074272156,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t49",
            "order_averaged_probabilities": {
              "A": 0.7925662100315094,
              "B": 0.20743378251791
            },
            "correct_probability": 0.7925662100315094,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t52",
            "order_averaged_probabilities": {
              "A": 0.21912704555143137,
              "B": 0.7808730006217957
            },
            "correct_probability": 0.21912704555143137,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t54",
            "order_averaged_probabilities": {
              "A": 0.4076821058988571,
              "B": 0.5923179388046265
            },
            "correct_probability": 0.4076821058988571,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t56",
            "order_averaged_probabilities": {
              "A": 0.44149892032146454,
              "B": 0.558501124382019
            },
            "correct_probability": 0.44149892032146454,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t73",
            "order_averaged_probabilities": {
              "A": 0.9876604676246643,
              "B": 0.012339530512690544
            },
            "correct_probability": 0.9876604676246643,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t74",
            "order_averaged_probabilities": {
              "A": 0.9872750341892242,
              "B": 0.012724997126497328
            },
            "correct_probability": 0.9872750341892242,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t75",
            "order_averaged_probabilities": {
              "A": 0.9883968532085419,
              "B": 0.011603168211877346
            },
            "correct_probability": 0.9883968532085419,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0000001192092896
            ]
          }
        ],
        "mean_correct_probability": 0.671920756628424
      }
    },
    "R1-M/unsteered": {
      "EH_answer": {
        "n": 80,
        "mean": 0.060297426889883356
      },
      "answer_length": {
        "n": 80,
        "mean": 145.0
      },
      "answer_truncated": {
        "n": 80,
        "mean": 0.375
      },
      "valid_digit_mass": [
        1.0,
        0.9999998211860657,
        1.0000001192092896,
        1.0,
        0.9999998807907104,
        0.9999984502792358,
        0.9999998807907104,
        0.9999998807907104,
        0.9999999403953552,
        0.9999999403953552,
        1.0,
        0.9999940991401672,
        1.0,
        0.9999995827674866,
        0.9999998807907104,
        1.0,
        0.9999995827674866,
        0.9999999403953552,
        0.9999997615814209,
        0.9999998807907104,
        1.0,
        0.9999998807907104,
        0.9999998807907104,
        0.9999997019767761,
        0.9999998807907104,
        1.0,
        1.0000001192092896,
        0.9999998807907104,
        1.0,
        0.9999999403953552,
        1.0,
        1.0,
        0.9999995827674866,
        0.9999998807907104,
        1.0,
        0.9999999403953552,
        0.9999996423721313,
        1.0,
        0.9999999403953552,
        0.9999998211860657,
        0.9999999403953552,
        0.9999793767929077,
        0.9999999403953552,
        1.0,
        0.9999998807907104,
        1.0,
        0.9999998807907104,
        0.999999463558197,
        0.9999993443489075,
        0.9999997615814209,
        0.9999998807907104,
        0.9999999403953552,
        1.0,
        0.9999998807907104,
        0.9999998211860657,
        1.0,
        0.9999998807907104,
        1.0,
        0.9999998807907104,
        1.0,
        0.9999994039535522,
        0.9999998807907104,
        0.9999996423721313,
        0.9999998211860657,
        0.9999988079071045,
        1.0,
        0.9999995827674866,
        0.9999997615814209,
        0.9999992251396179,
        0.9999998807907104,
        0.9999995827674866,
        0.9999999403953552,
        0.9999998211860657,
        1.0000001192092896,
        0.999999463558197,
        0.9999998807907104,
        0.9999998807907104,
        0.9999998807907104,
        0.9999983906745911,
        0.9999997615814209
      ],
      "baseline_mean": 7.925501766581104,
      "baseline_sd": 0.16407189150436952,
      "structural": {
        "n": 16,
        "records": [
          {
            "prompt_id": "s4t06",
            "order_averaged_probabilities": {
              "A": 0.3057021093700314,
              "B": 0.5074246842414141,
              "C": 0.18687321082688868
            },
            "correct_probability": 0.5074246842414141,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t09",
            "order_averaged_probabilities": {
              "A": 0.0020930415485054255,
              "B": 0.9716587066650391,
              "C": 0.026248286943882704
            },
            "correct_probability": 0.9716587066650391,
            "correct_argmax": true,
            "valid_mass": [
              1.0000001192092896,
              1.0
            ]
          },
          {
            "prompt_id": "s4t17",
            "order_averaged_probabilities": {
              "A": 0.46201062080217525,
              "B": 0.49677034525666386,
              "C": 0.04121899860911071
            },
            "correct_probability": 0.49677034525666386,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999998807907104
            ]
          },
          {
            "prompt_id": "s4t18",
            "order_averaged_probabilities": {
              "A": 0.11068314955628011,
              "B": 0.4886092678643763,
              "C": 0.4007076025009155
            },
            "correct_probability": 0.4886092678643763,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999997019767761
            ]
          },
          {
            "prompt_id": "s4t25",
            "order_averaged_probabilities": {
              "A": 0.35926803258189466,
              "B": 0.5357787646353245,
              "C": 0.10495317843742669
            },
            "correct_probability": 0.5357787646353245,
            "correct_argmax": true,
            "valid_mass": [
              1.0000001192092896,
              0.9999998807907104
            ]
          },
          {
            "prompt_id": "s4t28",
            "order_averaged_probabilities": {
              "A": 0.23011610247340286,
              "B": 0.5382831543684006,
              "C": 0.2316007313784212
            },
            "correct_probability": 0.5382831543684006,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t43",
            "order_averaged_probabilities": {
              "A": 0.349222770835695,
              "B": 0.5220340322703123,
              "C": 0.12874319645925425
            },
            "correct_probability": 0.5220340322703123,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t46",
            "order_averaged_probabilities": {
              "A": 0.49288302934201056,
              "B": 0.49805158226809,
              "C": 0.009065416408702731
            },
            "correct_probability": 0.49805158226809,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t48",
            "order_averaged_probabilities": {
              "A": 0.4077438438871468,
              "B": 0.4986701518064365,
              "C": 0.09358600084669888
            },
            "correct_probability": 0.4986701518064365,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t49",
            "order_averaged_probabilities": {
              "A": 0.42088451286326745,
              "B": 0.5047443923540413,
              "C": 0.07437108037993312
            },
            "correct_probability": 0.5047443923540413,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t52",
            "order_averaged_probabilities": {
              "A": 0.0007552763490821235,
              "B": 0.9601320326328278,
              "C": 0.03911262005567551
            },
            "correct_probability": 0.9601320326328278,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t54",
            "order_averaged_probabilities": {
              "A": 0.18788743765617255,
              "B": 0.4935592070687562,
              "C": 0.3185533629730344
            },
            "correct_probability": 0.4935592070687562,
            "correct_argmax": true,
            "valid_mass": [
              0.9999998807907104,
              0.9999997615814209
            ]
          },
          {
            "prompt_id": "s4t56",
            "order_averaged_probabilities": {
              "A": 0.4722600246896036,
              "B": 0.5026920391246676,
              "C": 0.02504792413674295
            },
            "correct_probability": 0.5026920391246676,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999998807907104
            ]
          },
          {
            "prompt_id": "s4t73",
            "order_averaged_probabilities": {
              "A": 0.0055512572871521115,
              "B": 0.9936423897743225,
              "C": 0.0008064088760875165
            },
            "correct_probability": 0.9936423897743225,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0000001192092896
            ]
          },
          {
            "prompt_id": "s4t74",
            "order_averaged_probabilities": {
              "A": 0.004406051579280756,
              "B": 0.9836170673370361,
              "C": 0.01197689032414928
            },
            "correct_probability": 0.9836170673370361,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t75",
            "order_averaged_probabilities": {
              "A": 0.008007502881810069,
              "B": 0.9772525429725647,
              "C": 0.014739986509084702
            },
            "correct_probability": 0.9772525429725647,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          }
        ],
        "mean_correct_probability": 0.6545575225400171
      },
      "source": {
        "n": 16,
        "records": [
          {
            "prompt_id": "s4t06",
            "order_averaged_probabilities": {
              "A": 0.9990074634552002,
              "B": 0.0009925129816110712
            },
            "correct_probability": 0.9990074634552002,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t09",
            "order_averaged_probabilities": {
              "A": 0.9998146295547485,
              "B": 0.00018535320850787684
            },
            "correct_probability": 0.9998146295547485,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t17",
            "order_averaged_probabilities": {
              "A": 0.6417471915483475,
              "B": 0.35825280100107193
            },
            "correct_probability": 0.6417471915483475,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t18",
            "order_averaged_probabilities": {
              "A": 0.995356410741806,
              "B": 0.004643577529350296
            },
            "correct_probability": 0.995356410741806,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t25",
            "order_averaged_probabilities": {
              "A": 0.03903643134981394,
              "B": 0.9609635472297668
            },
            "correct_probability": 0.03903643134981394,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t28",
            "order_averaged_probabilities": {
              "A": 0.37932242453098297,
              "B": 0.6206776201725006
            },
            "correct_probability": 0.37932242453098297,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t43",
            "order_averaged_probabilities": {
              "A": 0.3112403984823686,
              "B": 0.6887596100568771
            },
            "correct_probability": 0.3112403984823686,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t46",
            "order_averaged_probabilities": {
              "A": 0.994477391242981,
              "B": 0.005522617499082116
            },
            "correct_probability": 0.994477391242981,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t48",
            "order_averaged_probabilities": {
              "A": 0.7188826203346252,
              "B": 0.2811174084308732
            },
            "correct_probability": 0.7188826203346252,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t49",
            "order_averaged_probabilities": {
              "A": 0.6588243097066879,
              "B": 0.34117569879163057
            },
            "correct_probability": 0.6588243097066879,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t52",
            "order_averaged_probabilities": {
              "A": 0.36711564019788057,
              "B": 0.6328843683004379
            },
            "correct_probability": 0.36711564019788057,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t54",
            "order_averaged_probabilities": {
              "A": 0.1853736713528633,
              "B": 0.8146263062953949
            },
            "correct_probability": 0.1853736713528633,
            "correct_argmax": false,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t56",
            "order_averaged_probabilities": {
              "A": 0.6533788591623306,
              "B": 0.34662117110565305
            },
            "correct_probability": 0.6533788591623306,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t73",
            "order_averaged_probabilities": {
              "A": 0.9736770391464233,
              "B": 0.026322999969124794
            },
            "correct_probability": 0.9736770391464233,
            "correct_argmax": true,
            "valid_mass": [
              1.0000001192092896,
              1.0
            ]
          },
          {
            "prompt_id": "s4t74",
            "order_averaged_probabilities": {
              "A": 0.9061771929264069,
              "B": 0.09382282011210918
            },
            "correct_probability": 0.9061771929264069,
            "correct_argmax": true,
            "valid_mass": [
              1.0000001192092896,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t75",
            "order_averaged_probabilities": {
              "A": 0.5475070662796497,
              "B": 0.4524929297622293
            },
            "correct_probability": 0.5475070662796497,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          }
        ],
        "mean_correct_probability": 0.6481836712508198
      }
    },
    "R1-M/hostility": {
      "EH_answer": {
        "n": 80,
        "mean": 0.10634206255053869
      },
      "answer_length": {
        "n": 80,
        "mean": 152.2875
      },
      "answer_truncated": {
        "n": 80,
        "mean": 0.375
      },
      "valid_digit_mass": [
        0.9999999403953552,
        0.9999999403953552,
        1.0,
        1.0,
        1.0,
        0.9999998807907104,
        1.0000001192092896,
        0.9999999403953552,
        0.9999999403953552,
        0.9999999403953552,
        1.0000001192092896,
        0.9999997019767761,
        1.0,
        0.9999997615814209,
        0.9999999403953552,
        0.9999999403953552,
        0.9999995231628418,
        0.9999996423721313,
        0.9999999403953552,
        1.0,
        1.0,
        1.0000001192092896,
        0.9999998807907104,
        1.0,
        1.0,
        1.0000001192092896,
        1.0,
        1.0,
        0.9999999403953552,
        1.0,
        1.0,
        1.0000001192092896,
        0.9999999403953552,
        1.0,
        0.9999998807907104,
        1.0,
        0.9999999403953552,
        1.0,
        1.0,
        0.9999998211860657,
        1.0,
        0.9999997019767761,
        1.0,
        0.9999998807907104,
        1.0,
        1.0,
        1.0,
        0.9999997615814209,
        0.9999998211860657,
        1.0,
        0.9999999403953552,
        1.0,
        1.0,
        1.0,
        0.9999996423721313,
        1.0,
        0.9999999403953552,
        1.0,
        0.9999998807907104,
        1.0,
        0.9999977946281433,
        0.9999998211860657,
        0.999999463558197,
        0.9999998211860657,
        0.9999922513961792,
        0.9999998211860657,
        0.9999994039535522,
        0.9999998807907104,
        0.9999983310699463,
        0.9999995231628418,
        0.9999998807907104,
        1.0,
        0.9999999403953552,
        0.9999998807907104,
        0.9999997615814209,
        0.9999996423721313,
        0.9999999403953552,
        1.0,
        0.9999963045120239,
        0.9999992847442627
      ],
      "baseline_mean": null,
      "baseline_sd": null,
      "structural": {
        "n": 16,
        "records": [
          {
            "prompt_id": "s4t06",
            "order_averaged_probabilities": {
              "A": 0.1741827293371898,
              "B": 0.5375326164066792,
              "C": 0.28828460501972586
            },
            "correct_probability": 0.5375326164066792,
            "correct_argmax": true,
            "valid_mass": [
              1.0000001192092896,
              0.9999998807907104
            ]
          },
          {
            "prompt_id": "s4t09",
            "order_averaged_probabilities": {
              "A": 0.015030893554126123,
              "B": 0.6827398240566254,
              "C": 0.3022292929526884
            },
            "correct_probability": 0.6827398240566254,
            "correct_argmax": true,
            "valid_mass": [
              1.0000001192092896,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t17",
            "order_averaged_probabilities": {
              "A": 0.010281663155183196,
              "B": 0.5167480632662773,
              "C": 0.4729702528566122
            },
            "correct_probability": 0.5167480632662773,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999998211860657
            ]
          },
          {
            "prompt_id": "s4t18",
            "order_averaged_probabilities": {
              "A": 0.2612517656889395,
              "B": 0.5340779908001423,
              "C": 0.20467022468801588
            },
            "correct_probability": 0.5340779908001423,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999997019767761
            ]
          },
          {
            "prompt_id": "s4t25",
            "order_averaged_probabilities": {
              "A": 0.12686875189683633,
              "B": 0.5256851967424154,
              "C": 0.3474460339639336
            },
            "correct_probability": 0.5256851967424154,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999998807907104
            ]
          },
          {
            "prompt_id": "s4t28",
            "order_averaged_probabilities": {
              "A": 0.004194944369373843,
              "B": 0.8603832721710205,
              "C": 0.13542182091623545
            },
            "correct_probability": 0.8603832721710205,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t43",
            "order_averaged_probabilities": {
              "A": 0.45465565228369087,
              "B": 0.506810924038291,
              "C": 0.03853340772911906
            },
            "correct_probability": 0.506810924038291,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999998807907104
            ]
          },
          {
            "prompt_id": "s4t46",
            "order_averaged_probabilities": {
              "A": 0.33087891123909685,
              "B": 0.5120758088305593,
              "C": 0.15704527508933097
            },
            "correct_probability": 0.5120758088305593,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              0.9999997019767761
            ]
          },
          {
            "prompt_id": "s4t48",
            "order_averaged_probabilities": {
              "A": 0.3651281769232355,
              "B": 0.5000932106049731,
              "C": 0.1347786008263938
            },
            "correct_probability": 0.5000932106049731,
            "correct_argmax": true,
            "valid_mass": [
              1.0000001192092896,
              1.0
            ]
          },
          {
            "prompt_id": "s4t49",
            "order_averaged_probabilities": {
              "A": 0.18435855366988108,
              "B": 0.504715102724731,
              "C": 0.31092632142826915
            },
            "correct_probability": 0.504715102724731,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999998807907104
            ]
          },
          {
            "prompt_id": "s4t52",
            "order_averaged_probabilities": {
              "A": 0.14646129816537723,
              "B": 0.7386939823627472,
              "C": 0.11484476446639746
            },
            "correct_probability": 0.7386939823627472,
            "correct_argmax": true,
            "valid_mass": [
              1.0000001192092896,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t54",
            "order_averaged_probabilities": {
              "A": 0.005584212485700846,
              "B": 0.4665988441556692,
              "C": 0.5278169736266136
            },
            "correct_probability": 0.4665988441556692,
            "correct_argmax": false,
            "valid_mass": [
              0.9999998807907104,
              0.9999997615814209
            ]
          },
          {
            "prompt_id": "s4t56",
            "order_averaged_probabilities": {
              "A": 0.24722322626621462,
              "B": 0.49865231895819306,
              "C": 0.2541244700551033
            },
            "correct_probability": 0.49865231895819306,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t73",
            "order_averaged_probabilities": {
              "A": 0.006244952790439129,
              "B": 0.984255313873291,
              "C": 0.009499719890300184
            },
            "correct_probability": 0.984255313873291,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t74",
            "order_averaged_probabilities": {
              "A": 0.0021933894022367895,
              "B": 0.9948144853115082,
              "C": 0.0029921537498012185
            },
            "correct_probability": 0.9948144853115082,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t75",
            "order_averaged_probabilities": {
              "A": 0.00336410761156003,
              "B": 0.9953055679798126,
              "C": 0.0013303036685101688
            },
            "correct_probability": 0.9953055679798126,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          }
        ],
        "mean_correct_probability": 0.6474489076426835
      },
      "source": {
        "n": 16,
        "records": [
          {
            "prompt_id": "s4t06",
            "order_averaged_probabilities": {
              "A": 0.520137295126915,
              "B": 0.4798626974225044
            },
            "correct_probability": 0.520137295126915,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t09",
            "order_averaged_probabilities": {
              "A": 0.984759122133255,
              "B": 0.015240870474372059
            },
            "correct_probability": 0.984759122133255,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t17",
            "order_averaged_probabilities": {
              "A": 0.6871839910745621,
              "B": 0.3128160174237564
            },
            "correct_probability": 0.6871839910745621,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t18",
            "order_averaged_probabilities": {
              "A": 0.9998320937156677,
              "B": 0.00016792725722325486
            },
            "correct_probability": 0.9998320937156677,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t25",
            "order_averaged_probabilities": {
              "A": 0.2426247037947178,
              "B": 0.7573753297328949
            },
            "correct_probability": 0.2426247037947178,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t28",
            "order_averaged_probabilities": {
              "A": 0.2948813736438751,
              "B": 0.7051186561584473
            },
            "correct_probability": 0.2948813736438751,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t43",
            "order_averaged_probabilities": {
              "A": 0.6998796164989471,
              "B": 0.30012041330337524
            },
            "correct_probability": 0.6998796164989471,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t46",
            "order_averaged_probabilities": {
              "A": 0.9966521561145782,
              "B": 0.0033478766372354585
            },
            "correct_probability": 0.9966521561145782,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t48",
            "order_averaged_probabilities": {
              "A": 0.9966535866260529,
              "B": 0.0033464330961310296
            },
            "correct_probability": 0.9966535866260529,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t49",
            "order_averaged_probabilities": {
              "A": 0.7186353504657745,
              "B": 0.28136465209536254
            },
            "correct_probability": 0.7186353504657745,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t52",
            "order_averaged_probabilities": {
              "A": 0.4969475489342585,
              "B": 0.5030524525791407
            },
            "correct_probability": 0.4969475489342585,
            "correct_argmax": false,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t54",
            "order_averaged_probabilities": {
              "A": 0.8507208526134491,
              "B": 0.1492791660130024
            },
            "correct_probability": 0.8507208526134491,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t56",
            "order_averaged_probabilities": {
              "A": 0.6883148401975632,
              "B": 0.3116852016246412
            },
            "correct_probability": 0.6883148401975632,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t73",
            "order_averaged_probabilities": {
              "A": 0.9982860088348389,
              "B": 0.0017139584524556994
            },
            "correct_probability": 0.9982860088348389,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t74",
            "order_averaged_probabilities": {
              "A": 0.6324356645345688,
              "B": 0.3675643678288907
            },
            "correct_probability": 0.6324356645345688,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t75",
            "order_averaged_probabilities": {
              "A": 0.5139055140316486,
              "B": 0.4860944646061398
            },
            "correct_probability": 0.5139055140316486,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          }
        ],
        "mean_correct_probability": 0.707615607396292
      }
    },
    "R1-M/technicality": {
      "EH_answer": {
        "n": 80,
        "mean": 0.06995661293622106
      },
      "answer_length": {
        "n": 80,
        "mean": 166.9625
      },
      "answer_truncated": {
        "n": 80,
        "mean": 0.4375
      },
      "valid_digit_mass": [
        0.9999997615814209,
        0.9999997615814209,
        1.0,
        0.9999999403953552,
        0.9999998211860657,
        0.9999996423721313,
        1.0,
        0.9999999403953552,
        0.9999998807907104,
        1.0,
        1.0,
        0.9999989867210388,
        0.999999463558197,
        0.9999989867210388,
        0.9999998807907104,
        1.0,
        0.9999997615814209,
        0.9999999403953552,
        0.9999991655349731,
        0.9999998807907104,
        1.0,
        1.0,
        0.9999999403953552,
        0.9999983906745911,
        1.0,
        0.9999999403953552,
        0.9999997019767761,
        0.9999998807907104,
        1.0,
        1.0,
        1.0,
        1.0000001192092896,
        0.9999998807907104,
        0.9999998807907104,
        1.0,
        0.9999997019767761,
        0.9999997615814209,
        0.9999999403953552,
        0.9999999403953552,
        0.9999982714653015,
        0.9999998807907104,
        0.9998525977134705,
        0.9999998211860657,
        1.0,
        1.0,
        1.0000001192092896,
        0.9999999403953552,
        0.9999992251396179,
        0.9999997019767761,
        0.9999998807907104,
        1.0,
        1.0,
        0.9999997019767761,
        0.9999998807907104,
        1.0,
        0.9999999403953552,
        0.9999987483024597,
        1.0,
        0.9999994039535522,
        1.0,
        0.9999999403953552,
        0.9999998807907104,
        1.0,
        0.9999999403953552,
        0.9999997019767761,
        0.9999999403953552,
        0.9999984502792358,
        0.9999998211860657,
        0.9999998807907104,
        0.9999998211860657,
        0.9999949932098389,
        1.0,
        0.9999999403953552,
        1.0,
        0.9999996423721313,
        0.9999995231628418,
        0.9999998211860657,
        1.0,
        0.9999988079071045,
        0.9999999403953552
      ],
      "baseline_mean": null,
      "baseline_sd": null,
      "structural": {
        "n": 16,
        "records": [
          {
            "prompt_id": "s4t06",
            "order_averaged_probabilities": {
              "A": 0.044629062569583766,
              "B": 0.6985484063625336,
              "C": 0.25682252913247794
            },
            "correct_probability": 0.6985484063625336,
            "correct_argmax": true,
            "valid_mass": [
              0.9999998807907104,
              1.0
            ]
          },
          {
            "prompt_id": "s4t09",
            "order_averaged_probabilities": {
              "A": 0.14019392168847844,
              "B": 0.6772625893354416,
              "C": 0.18254348426125944
            },
            "correct_probability": 0.6772625893354416,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t17",
            "order_averaged_probabilities": {
              "A": 0.49298733857722254,
              "B": 0.4992312522699649,
              "C": 0.0077814311371184886
            },
            "correct_probability": 0.4992312522699649,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t18",
            "order_averaged_probabilities": {
              "A": 0.35075901518575847,
              "B": 0.5093211364001036,
              "C": 0.1399198854342103
            },
            "correct_probability": 0.5093211364001036,
            "correct_argmax": true,
            "valid_mass": [
              1.0000001192092896,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t25",
            "order_averaged_probabilities": {
              "A": 0.010443890350870788,
              "B": 0.7972539067268372,
              "C": 0.19230222096666694
            },
            "correct_probability": 0.7972539067268372,
            "correct_argmax": true,
            "valid_mass": [
              1.0000001192092896,
              1.0
            ]
          },
          {
            "prompt_id": "s4t28",
            "order_averaged_probabilities": {
              "A": 0.0880633881315589,
              "B": 0.5120615027844906,
              "C": 0.3998751100152731
            },
            "correct_probability": 0.5120615027844906,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t43",
            "order_averaged_probabilities": {
              "A": 0.49544158962817164,
              "B": 0.49952221629791893,
              "C": 0.005036197660956532
            },
            "correct_probability": 0.49952221629791893,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t46",
            "order_averaged_probabilities": {
              "A": 0.49747776982258074,
              "B": 0.49562523500208044,
              "C": 0.006896968232467771
            },
            "correct_probability": 0.49562523500208044,
            "correct_argmax": false,
            "valid_mass": [
              0.9999999403953552,
              1.0000001192092896
            ]
          },
          {
            "prompt_id": "s4t48",
            "order_averaged_probabilities": {
              "A": 0.4966760113238706,
              "B": 0.4944857159644016,
              "C": 0.00883826520293951
            },
            "correct_probability": 0.4944857159644016,
            "correct_argmax": false,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t49",
            "order_averaged_probabilities": {
              "A": 0.49071546585764736,
              "B": 0.49327375361463055,
              "C": 0.016010758001357317
            },
            "correct_probability": 0.49327375361463055,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t52",
            "order_averaged_probabilities": {
              "A": 0.11374007603444625,
              "B": 0.6441618502140045,
              "C": 0.2420980610186234
            },
            "correct_probability": 0.6441618502140045,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t54",
            "order_averaged_probabilities": {
              "A": 0.13428737349022413,
              "B": 0.48619017662713304,
              "C": 0.3795224651694298
            },
            "correct_probability": 0.48619017662713304,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999998807907104
            ]
          },
          {
            "prompt_id": "s4t56",
            "order_averaged_probabilities": {
              "A": 0.3062316760770045,
              "B": 0.5041984338313341,
              "C": 0.18956991005688906
            },
            "correct_probability": 0.5041984338313341,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              0.9999997615814209
            ]
          },
          {
            "prompt_id": "s4t73",
            "order_averaged_probabilities": {
              "A": 0.004563942668028176,
              "B": 0.9922601282596588,
              "C": 0.003175996185746044
            },
            "correct_probability": 0.9922601282596588,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0000001192092896
            ]
          },
          {
            "prompt_id": "s4t74",
            "order_averaged_probabilities": {
              "A": 0.014011617517098784,
              "B": 0.9779728651046753,
              "C": 0.008015505271032453
            },
            "correct_probability": 0.9779728651046753,
            "correct_argmax": true,
            "valid_mass": [
              1.0000001192092896,
              1.0
            ]
          },
          {
            "prompt_id": "s4t75",
            "order_averaged_probabilities": {
              "A": 0.06464297836646438,
              "B": 0.9172807037830353,
              "C": 0.018076279433444142
            },
            "correct_probability": 0.9172807037830353,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          }
        ],
        "mean_correct_probability": 0.6374156170361402
      },
      "source": {
        "n": 16,
        "records": [
          {
            "prompt_id": "s4t06",
            "order_averaged_probabilities": {
              "A": 0.9813073873519897,
              "B": 0.018692589259444503
            },
            "correct_probability": 0.9813073873519897,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t09",
            "order_averaged_probabilities": {
              "A": 0.9996446371078491,
              "B": 0.0003553690620492489
            },
            "correct_probability": 0.9996446371078491,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t17",
            "order_averaged_probabilities": {
              "A": 0.49211423844099045,
              "B": 0.5078857578337193
            },
            "correct_probability": 0.49211423844099045,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t18",
            "order_averaged_probabilities": {
              "A": 0.9995443224906921,
              "B": 0.000455722009519377
            },
            "correct_probability": 0.9995443224906921,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t25",
            "order_averaged_probabilities": {
              "A": 0.20849431306123734,
              "B": 0.7915056645870209
            },
            "correct_probability": 0.20849431306123734,
            "correct_argmax": false,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t28",
            "order_averaged_probabilities": {
              "A": 0.48331888066604733,
              "B": 0.5166811384260654
            },
            "correct_probability": 0.48331888066604733,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t43",
            "order_averaged_probabilities": {
              "A": 0.952157586812973,
              "B": 0.047842409228906035
            },
            "correct_probability": 0.952157586812973,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t46",
            "order_averaged_probabilities": {
              "A": 0.9259763658046722,
              "B": 0.07402361764211385
            },
            "correct_probability": 0.9259763658046722,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t48",
            "order_averaged_probabilities": {
              "A": 0.7499992847442627,
              "B": 0.25000068547859655
            },
            "correct_probability": 0.7499992847442627,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t49",
            "order_averaged_probabilities": {
              "A": 0.5143746808171272,
              "B": 0.48562527634203434
            },
            "correct_probability": 0.5143746808171272,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t52",
            "order_averaged_probabilities": {
              "A": 0.3892346956417896,
              "B": 0.6107653230428696
            },
            "correct_probability": 0.3892346956417896,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t54",
            "order_averaged_probabilities": {
              "A": 0.4103735621320084,
              "B": 0.5896264091134071
            },
            "correct_probability": 0.4103735621320084,
            "correct_argmax": false,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t56",
            "order_averaged_probabilities": {
              "A": 0.7799878716468811,
              "B": 0.2200121209025383
            },
            "correct_probability": 0.7799878716468811,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t73",
            "order_averaged_probabilities": {
              "A": 0.9954172968864441,
              "B": 0.0045827372232452035
            },
            "correct_probability": 0.9954172968864441,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t74",
            "order_averaged_probabilities": {
              "A": 0.6570642441511154,
              "B": 0.34293578285723925
            },
            "correct_probability": 0.6570642441511154,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t75",
            "order_averaged_probabilities": {
              "A": 0.6602429896593094,
              "B": 0.33975703245960176
            },
            "correct_probability": 0.6602429896593094,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          }
        ],
        "mean_correct_probability": 0.6999532723384618
      }
    },
    "R1-M/random": {
      "EH_answer": {
        "n": 80,
        "mean": 0.06506438025535317
      },
      "answer_length": {
        "n": 80,
        "mean": 147.65
      },
      "answer_truncated": {
        "n": 80,
        "mean": 0.3875
      },
      "valid_digit_mass": [
        0.9999999403953552,
        0.9999998807907104,
        0.9999998211860657,
        0.9999998807907104,
        0.9999998807907104,
        0.9999995827674866,
        1.0,
        1.0000001192092896,
        1.0,
        0.9999998807907104,
        1.0,
        0.9999942183494568,
        0.9999997615814209,
        0.9999990463256836,
        1.0000001192092896,
        0.9999998807907104,
        0.9999973177909851,
        1.0,
        0.9999991059303284,
        0.9999991059303284,
        1.0,
        1.0,
        0.9999999403953552,
        0.9999995231628418,
        0.9999991059303284,
        1.0,
        0.9999998807907104,
        0.9999990463256836,
        1.0,
        0.9999998211860657,
        0.9999998807907104,
        1.0,
        0.9999998807907104,
        0.9999999403953552,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        0.9999949932098389,
        0.9999998807907104,
        0.9999874830245972,
        0.9999998807907104,
        1.0,
        0.9999999403953552,
        1.0,
        0.9999997019767761,
        0.9999998211860657,
        0.9999995827674866,
        0.9999995827674866,
        1.0,
        0.9999998807907104,
        0.9999999403953552,
        1.0,
        0.9999993443489075,
        1.0,
        0.9999998807907104,
        0.9999999403953552,
        0.9999993443489075,
        1.0000001192092896,
        0.9999993443489075,
        0.9999999403953552,
        0.9999989867210388,
        1.0,
        0.9999992847442627,
        1.0,
        0.9999998211860657,
        0.9999997615814209,
        0.9999987483024597,
        0.9999996423721313,
        0.9999999403953552,
        0.9999999403953552,
        0.9999996423721313,
        1.0,
        0.9999997615814209,
        0.9999998807907104,
        1.0,
        0.9999997615814209,
        0.9999984502792358,
        0.9999983310699463
      ],
      "baseline_mean": null,
      "baseline_sd": null,
      "structural": {
        "n": 16,
        "records": [
          {
            "prompt_id": "s4t06",
            "order_averaged_probabilities": {
              "A": 0.1537532885431574,
              "B": 0.5187532585114241,
              "C": 0.32749343453906476
            },
            "correct_probability": 0.5187532585114241,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999998807907104
            ]
          },
          {
            "prompt_id": "s4t09",
            "order_averaged_probabilities": {
              "A": 0.007556288444902748,
              "B": 0.8527312874794006,
              "C": 0.13971241656690836
            },
            "correct_probability": 0.8527312874794006,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              0.9999998211860657
            ]
          },
          {
            "prompt_id": "s4t17",
            "order_averaged_probabilities": {
              "A": 0.4693198847962776,
              "B": 0.49865697167115286,
              "C": 0.032023109029978514
            },
            "correct_probability": 0.49865697167115286,
            "correct_argmax": true,
            "valid_mass": [
              1.0000001192092896,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t18",
            "order_averaged_probabilities": {
              "A": 0.07342896710906643,
              "B": 0.493102032225579,
              "C": 0.43346904776990414
            },
            "correct_probability": 0.493102032225579,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999998807907104
            ]
          },
          {
            "prompt_id": "s4t25",
            "order_averaged_probabilities": {
              "A": 0.4523210823026602,
              "B": 0.5095934364944696,
              "C": 0.038085501932073385
            },
            "correct_probability": 0.5095934364944696,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t28",
            "order_averaged_probabilities": {
              "A": 0.0148276585387066,
              "B": 0.7027660459280014,
              "C": 0.28240632358938456
            },
            "correct_probability": 0.7027660459280014,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999998807907104
            ]
          },
          {
            "prompt_id": "s4t43",
            "order_averaged_probabilities": {
              "A": 0.2717135110860909,
              "B": 0.5995883494615555,
              "C": 0.12869814154691994
            },
            "correct_probability": 0.5995883494615555,
            "correct_argmax": true,
            "valid_mass": [
              1.0000001192092896,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t46",
            "order_averaged_probabilities": {
              "A": 0.4396796885812364,
              "B": 0.4937885857070796,
              "C": 0.06653170147910714
            },
            "correct_probability": 0.4937885857070796,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999997615814209
            ]
          },
          {
            "prompt_id": "s4t48",
            "order_averaged_probabilities": {
              "A": 0.40513695917252335,
              "B": 0.5032350551337004,
              "C": 0.09162803215440363
            },
            "correct_probability": 0.5032350551337004,
            "correct_argmax": true,
            "valid_mass": [
              1.0000001192092896,
              0.9999998807907104
            ]
          },
          {
            "prompt_id": "s4t49",
            "order_averaged_probabilities": {
              "A": 0.39296475049923174,
              "B": 0.5151027161628008,
              "C": 0.09193251188844442
            },
            "correct_probability": 0.5151027161628008,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t52",
            "order_averaged_probabilities": {
              "A": 0.32478026108583435,
              "B": 0.6162524297833443,
              "C": 0.05896729789674282
            },
            "correct_probability": 0.6162524297833443,
            "correct_argmax": true,
            "valid_mass": [
              1.0000001192092896,
              0.9999998807907104
            ]
          },
          {
            "prompt_id": "s4t54",
            "order_averaged_probabilities": {
              "A": 0.13428776428918354,
              "B": 0.48935685219476,
              "C": 0.3763554049655795
            },
            "correct_probability": 0.48935685219476,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999998211860657
            ]
          },
          {
            "prompt_id": "s4t56",
            "order_averaged_probabilities": {
              "A": 0.10951640883286018,
              "B": 0.501781296916306,
              "C": 0.38870228873565793
            },
            "correct_probability": 0.501781296916306,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999996423721313
            ]
          },
          {
            "prompt_id": "s4t73",
            "order_averaged_probabilities": {
              "A": 0.003917951544281095,
              "B": 0.9905702173709869,
              "C": 0.0055118275340646505
            },
            "correct_probability": 0.9905702173709869,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t74",
            "order_averaged_probabilities": {
              "A": 0.0017078141099773347,
              "B": 0.9949376285076141,
              "C": 0.0033545262995176017
            },
            "correct_probability": 0.9949376285076141,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t75",
            "order_averaged_probabilities": {
              "A": 0.04756074910983443,
              "B": 0.9500128328800201,
              "C": 0.0024264240055345
            },
            "correct_probability": 0.9500128328800201,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          }
        ],
        "mean_correct_probability": 0.6393893122767622
      },
      "source": {
        "n": 16,
        "records": [
          {
            "prompt_id": "s4t06",
            "order_averaged_probabilities": {
              "A": 0.34121275693178177,
              "B": 0.6587872207164764
            },
            "correct_probability": 0.34121275693178177,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t09",
            "order_averaged_probabilities": {
              "A": 0.9997842013835907,
              "B": 0.00021581239695933618
            },
            "correct_probability": 0.9997842013835907,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t17",
            "order_averaged_probabilities": {
              "A": 0.44149892032146454,
              "B": 0.558501124382019
            },
            "correct_probability": 0.44149892032146454,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t18",
            "order_averaged_probabilities": {
              "A": 0.970793604850769,
              "B": 0.02920640865340829
            },
            "correct_probability": 0.970793604850769,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t25",
            "order_averaged_probabilities": {
              "A": 0.4550546295940876,
              "B": 0.5449453368782997
            },
            "correct_probability": 0.4550546295940876,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t28",
            "order_averaged_probabilities": {
              "A": 0.12283875979483128,
              "B": 0.8771612644195557
            },
            "correct_probability": 0.12283875979483128,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t43",
            "order_averaged_probabilities": {
              "A": 0.3202227810397744,
              "B": 0.6797772198915482
            },
            "correct_probability": 0.3202227810397744,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t46",
            "order_averaged_probabilities": {
              "A": 0.9699428975582123,
              "B": 0.030057094163566944
            },
            "correct_probability": 0.9699428975582123,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t48",
            "order_averaged_probabilities": {
              "A": 0.974304735660553,
              "B": 0.025695257354527712
            },
            "correct_probability": 0.974304735660553,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t49",
            "order_averaged_probabilities": {
              "A": 0.735343873500824,
              "B": 0.26465611532330513
            },
            "correct_probability": 0.735343873500824,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t52",
            "order_averaged_probabilities": {
              "A": 0.409063610015437,
              "B": 0.5909363403916359
            },
            "correct_probability": 0.409063610015437,
            "correct_argmax": false,
            "valid_mass": [
              0.9999999403953552,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t54",
            "order_averaged_probabilities": {
              "A": 0.499999962747097,
              "B": 0.499999962747097
            },
            "correct_probability": 0.499999962747097,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t56",
            "order_averaged_probabilities": {
              "A": 0.21881366521120071,
              "B": 0.7811863422393799
            },
            "correct_probability": 0.21881366521120071,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t73",
            "order_averaged_probabilities": {
              "A": 0.9973801970481873,
              "B": 0.0026198241976089776
            },
            "correct_probability": 0.9973801970481873,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t74",
            "order_averaged_probabilities": {
              "A": 0.9931012094020844,
              "B": 0.006898805499076843
            },
            "correct_probability": 0.9931012094020844,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              1.0000001192092896
            ]
          },
          {
            "prompt_id": "s4t75",
            "order_averaged_probabilities": {
              "A": 0.9243900179862976,
              "B": 0.07560993835795671
            },
            "correct_probability": 0.9243900179862976,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          }
        ],
        "mean_correct_probability": 0.648359113940387
      }
    },
    "R2/unsteered": {
      "EH_answer": {
        "n": 80,
        "mean": 0.06816254210280022
      },
      "answer_length": {
        "n": 80,
        "mean": 157.45
      },
      "answer_truncated": {
        "n": 80,
        "mean": 0.3375
      },
      "valid_digit_mass": [
        1.0,
        0.9999998807907104,
        1.0,
        0.9999999403953552,
        0.9999998807907104,
        0.9999999403953552,
        1.0,
        1.0,
        0.9999999403953552,
        0.9999999403953552,
        0.9999999403953552,
        0.9999995827674866,
        1.0,
        0.999999463558197,
        1.0,
        0.9999999403953552,
        0.9999996423721313,
        0.9999999403953552,
        0.9999998211860657,
        0.9999988079071045,
        0.999999463558197,
        1.0,
        1.0,
        0.9999995827674866,
        1.0,
        0.9999998807907104,
        0.9999999403953552,
        1.0,
        1.0,
        1.0,
        0.9999999403953552,
        0.9999999403953552,
        0.9999992251396179,
        0.9999999403953552,
        0.9999998211860657,
        0.9999999403953552,
        0.9999999403953552,
        0.9999998807907104,
        1.0,
        0.9999951720237732,
        1.0,
        0.9999866485595703,
        0.9999998807907104,
        0.9999999403953552,
        1.0,
        1.0,
        1.0,
        0.9999998211860657,
        0.9999998211860657,
        0.9999998807907104,
        0.9999997615814209,
        1.0,
        1.0,
        0.9999999403953552,
        0.9999998807907104,
        1.0,
        0.9999996423721313,
        1.0,
        0.9999999403953552,
        1.0,
        0.9999998807907104,
        0.9999995827674866,
        0.9999997615814209,
        0.9999998807907104,
        0.9999994039535522,
        0.9999998807907104,
        0.9999997019767761,
        0.9999998807907104,
        0.9999999403953552,
        0.9999998807907104,
        0.9999999403953552,
        1.0,
        0.9999998807907104,
        0.9999998807907104,
        0.9999999403953552,
        1.0,
        1.0,
        0.9999998807907104,
        0.999998927116394,
        1.0
      ],
      "baseline_mean": 7.895654456393143,
      "baseline_sd": 0.1724786265852466,
      "structural": {
        "n": 16,
        "records": [
          {
            "prompt_id": "s4t06",
            "order_averaged_probabilities": {
              "A": 0.24989671112598444,
              "B": 0.49592855377704836,
              "C": 0.25417473167181015
            },
            "correct_probability": 0.24989671112598444,
            "correct_argmax": false,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t09",
            "order_averaged_probabilities": {
              "A": 0.013299724069383956,
              "B": 0.5409096777439117,
              "C": 0.4457906153984368
            },
            "correct_probability": 0.013299724069383956,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t17",
            "order_averaged_probabilities": {
              "A": 0.49101431848885113,
              "B": 0.497382709338126,
              "C": 0.011602982180193067
            },
            "correct_probability": 0.49101431848885113,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t18",
            "order_averaged_probabilities": {
              "A": 0.00898881689136033,
              "B": 0.4767308304144535,
              "C": 0.5142803527414799
            },
            "correct_probability": 0.00898881689136033,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t25",
            "order_averaged_probabilities": {
              "A": 0.4927607908699656,
              "B": 0.49962565311579965,
              "C": 0.0076135818380862474
            },
            "correct_probability": 0.4927607908699656,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t28",
            "order_averaged_probabilities": {
              "A": 0.21786049945421837,
              "B": 0.5008254861459136,
              "C": 0.2813140422804281
            },
            "correct_probability": 0.21786049945421837,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t43",
            "order_averaged_probabilities": {
              "A": 0.48019122811768966,
              "B": 0.5011280465405434,
              "C": 0.018680713044886943
            },
            "correct_probability": 0.48019122811768966,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t46",
            "order_averaged_probabilities": {
              "A": 0.49796406772264845,
              "B": 0.4992502858519856,
              "C": 0.002785655145999044
            },
            "correct_probability": 0.49796406772264845,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t48",
            "order_averaged_probabilities": {
              "A": 0.2188438655554421,
              "B": 0.4975452105863951,
              "C": 0.2836109446361661
            },
            "correct_probability": 0.2188438655554421,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t49",
            "order_averaged_probabilities": {
              "A": 0.4696462715726284,
              "B": 0.499367128679296,
              "C": 0.030986649508122355
            },
            "correct_probability": 0.4696462715726284,
            "correct_argmax": false,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t52",
            "order_averaged_probabilities": {
              "A": 0.1994293370649416,
              "B": 0.5442221276462078,
              "C": 0.25634852302027866
            },
            "correct_probability": 0.1994293370649416,
            "correct_argmax": false,
            "valid_mass": [
              0.9999998807907104,
              1.0
            ]
          },
          {
            "prompt_id": "s4t54",
            "order_averaged_probabilities": {
              "A": 0.4885093817224231,
              "B": 0.49841563212703477,
              "C": 0.013074972666800022
            },
            "correct_probability": 0.4885093817224231,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t56",
            "order_averaged_probabilities": {
              "A": 0.4083993361919056,
              "B": 0.4988887654617429,
              "C": 0.0927118572872132
            },
            "correct_probability": 0.4083993361919056,
            "correct_argmax": false,
            "valid_mass": [
              0.9999999403953552,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t73",
            "order_averaged_probabilities": {
              "A": 0.005128976663399953,
              "B": 0.95674267411232,
              "C": 0.038128353480715305
            },
            "correct_probability": 0.005128976663399953,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t74",
            "order_averaged_probabilities": {
              "A": 0.20343794025802708,
              "B": 0.5341113097965717,
              "C": 0.262450737063773
            },
            "correct_probability": 0.20343794025802708,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              0.9999998807907104
            ]
          },
          {
            "prompt_id": "s4t75",
            "order_averaged_probabilities": {
              "A": 0.41693639248569525,
              "B": 0.5254029780626297,
              "C": 0.05766063102055341
            },
            "correct_probability": 0.41693639248569525,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          }
        ],
        "mean_correct_probability": 0.3038942286409103
      },
      "source": {
        "n": 16,
        "records": [
          {
            "prompt_id": "s4t06",
            "order_averaged_probabilities": {
              "A": 0.8016602694988251,
              "B": 0.19833974912762642
            },
            "correct_probability": 0.8016602694988251,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t09",
            "order_averaged_probabilities": {
              "A": 0.9995445013046265,
              "B": 0.00045554631610578156
            },
            "correct_probability": 0.9995445013046265,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t17",
            "order_averaged_probabilities": {
              "A": 0.19580215262249112,
              "B": 0.8041978776454926
            },
            "correct_probability": 0.19580215262249112,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t18",
            "order_averaged_probabilities": {
              "A": 0.962048202753067,
              "B": 0.037951790536681074
            },
            "correct_probability": 0.962048202753067,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t25",
            "order_averaged_probabilities": {
              "A": 0.8796568214893341,
              "B": 0.12034317944198847
            },
            "correct_probability": 0.8796568214893341,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t28",
            "order_averaged_probabilities": {
              "A": 0.10406692326068878,
              "B": 0.8959330320358276
            },
            "correct_probability": 0.10406692326068878,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t43",
            "order_averaged_probabilities": {
              "A": 0.48926191503414884,
              "B": 0.5107380840927362
            },
            "correct_probability": 0.48926191503414884,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t46",
            "order_averaged_probabilities": {
              "A": 0.9523247182369232,
              "B": 0.04767526799685129
            },
            "correct_probability": 0.9523247182369232,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t48",
            "order_averaged_probabilities": {
              "A": 0.9966535866260529,
              "B": 0.003346435258981373
            },
            "correct_probability": 0.9966535866260529,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t49",
            "order_averaged_probabilities": {
              "A": 0.5299816355109215,
              "B": 0.4700183635286521
            },
            "correct_probability": 0.5299816355109215,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t52",
            "order_averaged_probabilities": {
              "A": 0.45391159609425813,
              "B": 0.5460883863270283
            },
            "correct_probability": 0.45391159609425813,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t54",
            "order_averaged_probabilities": {
              "A": 0.11195268854498863,
              "B": 0.8880472779273987
            },
            "correct_probability": 0.11195268854498863,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t56",
            "order_averaged_probabilities": {
              "A": 0.6549171954393387,
              "B": 0.34508282924070954
            },
            "correct_probability": 0.6549171954393387,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t73",
            "order_averaged_probabilities": {
              "A": 0.9973894357681274,
              "B": 0.0026105970317757965
            },
            "correct_probability": 0.9973894357681274,
            "correct_argmax": true,
            "valid_mass": [
              1.0000001192092896,
              1.0
            ]
          },
          {
            "prompt_id": "s4t74",
            "order_averaged_probabilities": {
              "A": 0.8383530676364899,
              "B": 0.16164696926716715
            },
            "correct_probability": 0.8383530676364899,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t75",
            "order_averaged_probabilities": {
              "A": 0.952223539352417,
              "B": 0.047776447638170794
            },
            "correct_probability": 0.952223539352417,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          }
        ],
        "mean_correct_probability": 0.6824842655732937
      }
    },
    "R2/hostility": {
      "EH_answer": {
        "n": 80,
        "mean": 0.12146159982512472
      },
      "answer_length": {
        "n": 80,
        "mean": 158.1
      },
      "answer_truncated": {
        "n": 80,
        "mean": 0.35
      },
      "valid_digit_mass": [
        0.9999999403953552,
        1.0,
        1.0,
        0.9999999403953552,
        0.9999998807907104,
        0.9999997615814209,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        0.9999998807907104,
        1.0,
        0.9999998807907104,
        1.0,
        1.0,
        0.9999998807907104,
        0.9999999403953552,
        1.0,
        1.0,
        0.9999998807907104,
        0.9999998807907104,
        0.9999958276748657,
        0.9999999403953552,
        0.9999998807907104,
        1.0,
        0.9999999403953552,
        1.0,
        0.9999998807907104,
        1.0,
        0.9999999403953552,
        0.9999998807907104,
        0.9999999403953552,
        1.0,
        1.0,
        0.9999999403953552,
        0.9999998807907104,
        1.0,
        0.9999996423721313,
        0.9999997615814209,
        1.0,
        0.9999992847442627,
        1.0,
        0.9999999403953552,
        0.9999999403953552,
        0.9999999403953552,
        1.0,
        1.0,
        0.9999999403953552,
        1.0,
        0.9999999403953552,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        0.9999998807907104,
        0.9999998807907104,
        0.9999995827674866,
        1.0,
        1.0,
        1.0,
        0.9999995827674866,
        1.0,
        0.9999997615814209,
        1.0,
        0.9999998807907104,
        0.9999998807907104,
        1.0,
        1.0,
        0.9999999403953552,
        1.0,
        0.9999999403953552,
        0.9999998807907104,
        0.9999999403953552,
        0.9999999403953552,
        0.9999999403953552,
        0.9999999403953552
      ],
      "baseline_mean": null,
      "baseline_sd": null,
      "structural": {
        "n": 16,
        "records": [
          {
            "prompt_id": "s4t06",
            "order_averaged_probabilities": {
              "A": 0.09110718680767604,
              "B": 0.4935757157509215,
              "C": 0.4153170734643936
            },
            "correct_probability": 0.09110718680767604,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              0.9999998807907104
            ]
          },
          {
            "prompt_id": "s4t09",
            "order_averaged_probabilities": {
              "A": 0.13308306414441518,
              "B": 0.5045752543956041,
              "C": 0.36234161618631333
            },
            "correct_probability": 0.13308306414441518,
            "correct_argmax": false,
            "valid_mass": [
              0.9999999403953552,
              0.9999998807907104
            ]
          },
          {
            "prompt_id": "s4t17",
            "order_averaged_probabilities": {
              "A": 0.014653759708380676,
              "B": 0.4949382324703038,
              "C": 0.49040804570540786
            },
            "correct_probability": 0.014653759708380676,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t18",
            "order_averaged_probabilities": {
              "A": 0.4618934937070662,
              "B": 0.49469911462801974,
              "C": 0.04340740153566003
            },
            "correct_probability": 0.4618934937070662,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t25",
            "order_averaged_probabilities": {
              "A": 0.18529147866820495,
              "B": 0.5071859080344439,
              "C": 0.3075225662905723
            },
            "correct_probability": 0.18529147866820495,
            "correct_argmax": false,
            "valid_mass": [
              1.0000001192092896,
              1.0
            ]
          },
          {
            "prompt_id": "s4t28",
            "order_averaged_probabilities": {
              "A": 0.0006161984667869547,
              "B": 0.5856049582362175,
              "C": 0.4137787953950465
            },
            "correct_probability": 0.0006161984667869547,
            "correct_argmax": false,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t43",
            "order_averaged_probabilities": {
              "A": 0.2797284121668895,
              "B": 0.5020645773038268,
              "C": 0.2182070099224802
            },
            "correct_probability": 0.2797284121668895,
            "correct_argmax": false,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t46",
            "order_averaged_probabilities": {
              "A": 0.2187679580916324,
              "B": 0.499092375888722,
              "C": 0.2821396802319214
            },
            "correct_probability": 0.2187679580916324,
            "correct_argmax": false,
            "valid_mass": [
              1.0000001192092896,
              1.0
            ]
          },
          {
            "prompt_id": "s4t48",
            "order_averaged_probabilities": {
              "A": 0.3652857965541729,
              "B": 0.500056680990383,
              "C": 0.13465751963667572
            },
            "correct_probability": 0.3652857965541729,
            "correct_argmax": false,
            "valid_mass": [
              0.9999999403953552,
              0.9999998807907104
            ]
          },
          {
            "prompt_id": "s4t49",
            "order_averaged_probabilities": {
              "A": 0.030025610398524805,
              "B": 0.4856751669140067,
              "C": 0.4842992527410388
            },
            "correct_probability": 0.030025610398524805,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t52",
            "order_averaged_probabilities": {
              "A": 0.017582060470886063,
              "B": 0.6263794153928757,
              "C": 0.35603855084627867
            },
            "correct_probability": 0.017582060470886063,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t54",
            "order_averaged_probabilities": {
              "A": 0.11130405658752807,
              "B": 0.49121995668974705,
              "C": 0.39747600071132183
            },
            "correct_probability": 0.11130405658752807,
            "correct_argmax": false,
            "valid_mass": [
              0.9999999403953552,
              0.9999998807907104
            ]
          },
          {
            "prompt_id": "s4t56",
            "order_averaged_probabilities": {
              "A": 0.018658927091564692,
              "B": 0.49330166494473815,
              "C": 0.48803939297795296
            },
            "correct_probability": 0.018658927091564692,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t73",
            "order_averaged_probabilities": {
              "A": 0.0010313832899555564,
              "B": 0.991195023059845,
              "C": 0.007773613964673132
            },
            "correct_probability": 0.0010313832899555564,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t74",
            "order_averaged_probabilities": {
              "A": 0.1214950355279143,
              "B": 0.614369161427021,
              "C": 0.2641358426772058
            },
            "correct_probability": 0.1214950355279143,
            "correct_argmax": false,
            "valid_mass": [
              1.0000001192092896,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t75",
            "order_averaged_probabilities": {
              "A": 0.00303166846174463,
              "B": 0.9489976763725281,
              "C": 0.04797064611921087
            },
            "correct_probability": 0.00303166846174463,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          }
        ],
        "mean_correct_probability": 0.12834725563395893
      },
      "source": {
        "n": 16,
        "records": [
          {
            "prompt_id": "s4t06",
            "order_averaged_probabilities": {
              "A": 0.5734388455748558,
              "B": 0.42656112095573917
            },
            "correct_probability": 0.5734388455748558,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t09",
            "order_averaged_probabilities": {
              "A": 0.9608346223831177,
              "B": 0.03916540334466845
            },
            "correct_probability": 0.9608346223831177,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t17",
            "order_averaged_probabilities": {
              "A": 0.5797240808606148,
              "B": 0.4202759061008692
            },
            "correct_probability": 0.5797240808606148,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t18",
            "order_averaged_probabilities": {
              "A": 0.9995445013046265,
              "B": 0.00045553323140712365
            },
            "correct_probability": 0.9995445013046265,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t25",
            "order_averaged_probabilities": {
              "A": 0.41869326680898666,
              "B": 0.5813067406415939
            },
            "correct_probability": 0.41869326680898666,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t28",
            "order_averaged_probabilities": {
              "A": 0.5923179388046265,
              "B": 0.4076821058988571
            },
            "correct_probability": 0.5923179388046265,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t43",
            "order_averaged_probabilities": {
              "A": 0.4999999888241291,
              "B": 0.4999999888241291
            },
            "correct_probability": 0.4999999888241291,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t46",
            "order_averaged_probabilities": {
              "A": 0.9929642677307129,
              "B": 0.007035758361325861
            },
            "correct_probability": 0.9929642677307129,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t48",
            "order_averaged_probabilities": {
              "A": 0.9990366101264954,
              "B": 0.000963368149753896
            },
            "correct_probability": 0.9990366101264954,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t49",
            "order_averaged_probabilities": {
              "A": 0.6103866845369339,
              "B": 0.3896133078378625
            },
            "correct_probability": 0.6103866845369339,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t52",
            "order_averaged_probabilities": {
              "A": 0.31144495455373544,
              "B": 0.6885550767183304
            },
            "correct_probability": 0.31144495455373544,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t54",
            "order_averaged_probabilities": {
              "A": 0.5091626532375813,
              "B": 0.4908373453654349
            },
            "correct_probability": 0.5091626532375813,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t56",
            "order_averaged_probabilities": {
              "A": 0.22568347305059433,
              "B": 0.7743165194988251
            },
            "correct_probability": 0.22568347305059433,
            "correct_argmax": false,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t73",
            "order_averaged_probabilities": {
              "A": 0.9520488381385803,
              "B": 0.047951123444363475
            },
            "correct_probability": 0.9520488381385803,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t74",
            "order_averaged_probabilities": {
              "A": 0.9204829037189484,
              "B": 0.07951706880703568
            },
            "correct_probability": 0.9204829037189484,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t75",
            "order_averaged_probabilities": {
              "A": 0.5194241739809513,
              "B": 0.48057580925524235
            },
            "correct_probability": 0.5194241739809513,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          }
        ],
        "mean_correct_probability": 0.6665742377272181
      }
    },
    "R2/technicality": {
      "EH_answer": {
        "n": 80,
        "mean": 0.09192190546309575
      },
      "answer_length": {
        "n": 80,
        "mean": 171.275
      },
      "answer_truncated": {
        "n": 80,
        "mean": 0.475
      },
      "valid_digit_mass": [
        0.9999999403953552,
        0.9999999403953552,
        0.9999999403953552,
        0.9999996423721313,
        0.9999999403953552,
        0.9999994039535522,
        0.9999999403953552,
        1.0,
        0.999999463558197,
        1.0,
        0.9999999403953552,
        0.9999971985816956,
        0.9999992847442627,
        0.9999997019767761,
        0.9999998211860657,
        1.0,
        0.9999993443489075,
        1.0,
        0.9999999403953552,
        0.9999995827674866,
        0.9999999403953552,
        1.0,
        0.999999463558197,
        0.9999997615814209,
        1.0,
        0.9999998807907104,
        0.9999999403953552,
        1.0,
        0.9999998807907104,
        0.9999999403953552,
        0.9999998807907104,
        1.0,
        0.9999997615814209,
        0.9999999403953552,
        1.0000001192092896,
        1.0,
        0.9999998807907104,
        0.9999999403953552,
        0.9999999403953552,
        0.9999985694885254,
        1.0,
        0.9999877214431763,
        0.9999999403953552,
        0.9999999403953552,
        1.0,
        0.9999998211860657,
        1.0,
        0.9999999403953552,
        0.9999997019767761,
        0.9999998211860657,
        0.9999998807907104,
        0.9999998807907104,
        1.0000001192092896,
        1.0,
        0.9999995231628418,
        0.9999996423721313,
        0.9999990463256836,
        0.9999997019767761,
        0.9999995827674866,
        0.9999999403953552,
        1.0,
        0.9999998807907104,
        1.0,
        1.0,
        0.9999991059303284,
        1.0000001192092896,
        1.0,
        0.9999998211860657,
        0.9999998211860657,
        0.9999999403953552,
        0.9999998807907104,
        1.0,
        0.9999998807907104,
        0.9999999403953552,
        1.0,
        1.0,
        0.9999999403953552,
        0.9999999403953552,
        0.9999986886978149,
        0.9999998211860657
      ],
      "baseline_mean": null,
      "baseline_sd": null,
      "structural": {
        "n": 16,
        "records": [
          {
            "prompt_id": "s4t06",
            "order_averaged_probabilities": {
              "A": 0.18530992981141026,
              "B": 0.502171041443944,
              "C": 0.3125190124846995
            },
            "correct_probability": 0.18530992981141026,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t09",
            "order_averaged_probabilities": {
              "A": 0.015439631664776243,
              "B": 0.5696732178330421,
              "C": 0.41488709300756454
            },
            "correct_probability": 0.015439631664776243,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t17",
            "order_averaged_probabilities": {
              "A": 0.18875254778686212,
              "B": 0.47637085765745724,
              "C": 0.3348765876144171
            },
            "correct_probability": 0.18875254778686212,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t18",
            "order_averaged_probabilities": {
              "A": 0.15738394926302135,
              "B": 0.4522685678675771,
              "C": 0.3903474658727646
            },
            "correct_probability": 0.15738394926302135,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              0.9999997615814209
            ]
          },
          {
            "prompt_id": "s4t25",
            "order_averaged_probabilities": {
              "A": 0.12497630773577839,
              "B": 0.5169858299195766,
              "C": 0.3580378256738186
            },
            "correct_probability": 0.12497630773577839,
            "correct_argmax": false,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t28",
            "order_averaged_probabilities": {
              "A": 0.30963996206992306,
              "B": 0.4911139563191682,
              "C": 0.19924609828740358
            },
            "correct_probability": 0.30963996206992306,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t43",
            "order_averaged_probabilities": {
              "A": 0.4399448599165332,
              "B": 0.49993031146004796,
              "C": 0.06012481451034546
            },
            "correct_probability": 0.4399448599165332,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t46",
            "order_averaged_probabilities": {
              "A": 0.45224289526805705,
              "B": 0.49912776280689286,
              "C": 0.04862932680407539
            },
            "correct_probability": 0.45224289526805705,
            "correct_argmax": false,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t48",
            "order_averaged_probabilities": {
              "A": 0.46981037861610275,
              "B": 0.49919239539303817,
              "C": 0.030997220485005528
            },
            "correct_probability": 0.46981037861610275,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t49",
            "order_averaged_probabilities": {
              "A": 0.48023821765673347,
              "B": 0.4956498134415597,
              "C": 0.02411196567118168
            },
            "correct_probability": 0.48023821765673347,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t52",
            "order_averaged_probabilities": {
              "A": 0.09097635956456429,
              "B": 0.4992622942663729,
              "C": 0.4097613552585244
            },
            "correct_probability": 0.09097635956456429,
            "correct_argmax": false,
            "valid_mass": [
              1.0000001192092896,
              1.0
            ]
          },
          {
            "prompt_id": "s4t54",
            "order_averaged_probabilities": {
              "A": 0.49296910983366615,
              "B": 0.4966527114047494,
              "C": 0.010378170059993863
            },
            "correct_probability": 0.49296910983366615,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t56",
            "order_averaged_probabilities": {
              "A": 0.33865772219178325,
              "B": 0.500139378127642,
              "C": 0.1612029386451468
            },
            "correct_probability": 0.33865772219178325,
            "correct_argmax": false,
            "valid_mass": [
              1.0000001192092896,
              1.0
            ]
          },
          {
            "prompt_id": "s4t73",
            "order_averaged_probabilities": {
              "A": 0.05280483663045743,
              "B": 0.8016831874847412,
              "C": 0.14551196969114244
            },
            "correct_probability": 0.05280483663045743,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t74",
            "order_averaged_probabilities": {
              "A": 0.44339804908668157,
              "B": 0.5266754180192947,
              "C": 0.029926534974947572
            },
            "correct_probability": 0.44339804908668157,
            "correct_argmax": false,
            "valid_mass": [
              1.0000001192092896,
              1.0
            ]
          },
          {
            "prompt_id": "s4t75",
            "order_averaged_probabilities": {
              "A": 0.07724066673836205,
              "B": 0.8385885059833527,
              "C": 0.08417078666388988
            },
            "correct_probability": 0.07724066673836205,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          }
        ],
        "mean_correct_probability": 0.26998658898966954
      },
      "source": {
        "n": 16,
        "records": [
          {
            "prompt_id": "s4t06",
            "order_averaged_probabilities": {
              "A": 0.9966524541378021,
              "B": 0.0033475556432449594
            },
            "correct_probability": 0.9966524541378021,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t09",
            "order_averaged_probabilities": {
              "A": 0.9998319149017334,
              "B": 0.0001680908475520937
            },
            "correct_probability": 0.9998319149017334,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t17",
            "order_averaged_probabilities": {
              "A": 0.389242235571146,
              "B": 0.6107577830553055
            },
            "correct_probability": 0.389242235571146,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t18",
            "order_averaged_probabilities": {
              "A": 0.9995444416999817,
              "B": 0.00045559786542526126
            },
            "correct_probability": 0.9995444416999817,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t25",
            "order_averaged_probabilities": {
              "A": 0.04127551708370447,
              "B": 0.9587244987487793
            },
            "correct_probability": 0.04127551708370447,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t28",
            "order_averaged_probabilities": {
              "A": 0.13888749107718468,
              "B": 0.8611124753952026
            },
            "correct_probability": 0.13888749107718468,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t43",
            "order_averaged_probabilities": {
              "A": 0.9087580740451813,
              "B": 0.09124190256625297
            },
            "correct_probability": 0.9087580740451813,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t46",
            "order_averaged_probabilities": {
              "A": 0.5912120416760445,
              "B": 0.408787906195073
            },
            "correct_probability": 0.5912120416760445,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t48",
            "order_averaged_probabilities": {
              "A": 0.5476745553314686,
              "B": 0.45232540762982865
            },
            "correct_probability": 0.5476745553314686,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t49",
            "order_averaged_probabilities": {
              "A": 0.7499383091926575,
              "B": 0.2500616972974967
            },
            "correct_probability": 0.7499383091926575,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t52",
            "order_averaged_probabilities": {
              "A": 0.22094683605246246,
              "B": 0.7790532112121582
            },
            "correct_probability": 0.22094683605246246,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t54",
            "order_averaged_probabilities": {
              "A": 0.49054639297537506,
              "B": 0.509453633800149
            },
            "correct_probability": 0.49054639297537506,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t56",
            "order_averaged_probabilities": {
              "A": 0.7070646286010742,
              "B": 0.2929353639483452
            },
            "correct_probability": 0.7070646286010742,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t73",
            "order_averaged_probabilities": {
              "A": 0.8850742876529694,
              "B": 0.11492569372057915
            },
            "correct_probability": 0.8850742876529694,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t74",
            "order_averaged_probabilities": {
              "A": 0.8649445474147797,
              "B": 0.1350554712698795
            },
            "correct_probability": 0.8649445474147797,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t75",
            "order_averaged_probabilities": {
              "A": 0.9940435588359833,
              "B": 0.005956488661468029
            },
            "correct_probability": 0.9940435588359833,
            "correct_argmax": true,
            "valid_mass": [
              1.0000001192092896,
              1.0
            ]
          }
        ],
        "mean_correct_probability": 0.6578523303905968
      }
    },
    "R2/random": {
      "EH_answer": {
        "n": 80,
        "mean": 0.0830270312319044
      },
      "answer_length": {
        "n": 80,
        "mean": 156.2125
      },
      "answer_truncated": {
        "n": 80,
        "mean": 0.3625
      },
      "valid_digit_mass": [
        0.9999998807907104,
        0.9999997615814209,
        0.9999998807907104,
        0.9999999403953552,
        0.9999999403953552,
        0.9999998807907104,
        0.9999998807907104,
        0.9999998807907104,
        1.0,
        0.9999999403953552,
        1.0,
        0.9999993443489075,
        0.9999999403953552,
        0.9999958276748657,
        1.0,
        1.0,
        0.9999977350234985,
        0.9999999403953552,
        0.9999998807907104,
        0.9999998211860657,
        0.9999999403953552,
        1.0,
        1.0,
        0.9999997019767761,
        1.0,
        1.0,
        1.0,
        0.9999999403953552,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0000001192092896,
        1.0,
        1.0000001192092896,
        1.0,
        1.0,
        0.9999999403953552,
        1.0,
        0.9999998807907104,
        0.9999999403953552,
        0.999992847442627,
        0.9999998807907104,
        0.9999999403953552,
        1.0,
        1.0,
        0.9999999403953552,
        0.9999986886978149,
        0.9999998807907104,
        0.9999998807907104,
        1.0000001192092896,
        0.9999999403953552,
        0.9999998211860657,
        0.9999999403953552,
        0.9999987483024597,
        0.9999998807907104,
        0.9999999403953552,
        0.9999998211860657,
        0.9999998211860657,
        0.9999998807907104,
        0.9999998211860657,
        0.9999999403953552,
        0.9999998807907104,
        1.0,
        0.9999999403953552,
        1.0,
        0.9999998211860657,
        1.0,
        0.9999998807907104,
        1.0,
        0.9999999403953552,
        1.0,
        1.0,
        1.0,
        1.0,
        0.9999999403953552,
        1.0,
        0.9999999403953552,
        0.9999992847442627,
        0.9999998211860657
      ],
      "baseline_mean": null,
      "baseline_sd": null,
      "structural": {
        "n": 16,
        "records": [
          {
            "prompt_id": "s4t06",
            "order_averaged_probabilities": {
              "A": 0.004282392787331446,
              "B": 0.49545983981806785,
              "C": 0.5002577495761216
            },
            "correct_probability": 0.004282392787331446,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t09",
            "order_averaged_probabilities": {
              "A": 0.30855119189072866,
              "B": 0.49534777784720063,
              "C": 0.19610102381557226
            },
            "correct_probability": 0.30855119189072866,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t17",
            "order_averaged_probabilities": {
              "A": 0.49798037252548966,
              "B": 0.4987484244111329,
              "C": 0.0032712529646232724
            },
            "correct_probability": 0.49798037252548966,
            "correct_argmax": false,
            "valid_mass": [
              1.0000001192092896,
              1.0
            ]
          },
          {
            "prompt_id": "s4t18",
            "order_averaged_probabilities": {
              "A": 0.07399830181441303,
              "B": 0.49589283810928464,
              "C": 0.4301088987849653
            },
            "correct_probability": 0.07399830181441303,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t25",
            "order_averaged_probabilities": {
              "A": 0.4880771336240173,
              "B": 0.5002290906850249,
              "C": 0.011693736771121621
            },
            "correct_probability": 0.4880771336240173,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0000001192092896
            ]
          },
          {
            "prompt_id": "s4t28",
            "order_averaged_probabilities": {
              "A": 0.011016043805284426,
              "B": 0.5116457846015692,
              "C": 0.47733821999281645
            },
            "correct_probability": 0.011016043805284426,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0000001192092896
            ]
          },
          {
            "prompt_id": "s4t43",
            "order_averaged_probabilities": {
              "A": 0.40591628724044426,
              "B": 0.5032963017001748,
              "C": 0.0907873897231184
            },
            "correct_probability": 0.40591628724044426,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t46",
            "order_averaged_probabilities": {
              "A": 0.4992488466726286,
              "B": 0.4990371948367738,
              "C": 0.00171395466895774
            },
            "correct_probability": 0.4992488466726286,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t48",
            "order_averaged_probabilities": {
              "A": 0.46192790821736196,
              "B": 0.49979989462008234,
              "C": 0.0382721696223598
            },
            "correct_probability": 0.46192790821736196,
            "correct_argmax": false,
            "valid_mass": [
              1.0000001192092896,
              1.0
            ]
          },
          {
            "prompt_id": "s4t49",
            "order_averaged_probabilities": {
              "A": 0.42356756678418606,
              "B": 0.4985427395440638,
              "C": 0.0778896464034915
            },
            "correct_probability": 0.42356756678418606,
            "correct_argmax": false,
            "valid_mass": [
              0.9999999403953552,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t52",
            "order_averaged_probabilities": {
              "A": 0.4501882789217717,
              "B": 0.5017775003798306,
              "C": 0.048034239502158016
            },
            "correct_probability": 0.4501882789217717,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t54",
            "order_averaged_probabilities": {
              "A": 0.21882505499934268,
              "B": 0.49861250873073004,
              "C": 0.28256239637266845
            },
            "correct_probability": 0.21882505499934268,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t56",
            "order_averaged_probabilities": {
              "A": 0.3111829431550177,
              "B": 0.4945839916035766,
              "C": 0.19423305662348866
            },
            "correct_probability": 0.3111829431550177,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t73",
            "order_averaged_probabilities": {
              "A": 0.09510623983805999,
              "B": 0.8283827900886536,
              "C": 0.07651097094640136
            },
            "correct_probability": 0.09510623983805999,
            "correct_argmax": false,
            "valid_mass": [
              1.0000001192092896,
              1.0
            ]
          },
          {
            "prompt_id": "s4t74",
            "order_averaged_probabilities": {
              "A": 0.015030322570169119,
              "B": 0.8012888133525848,
              "C": 0.1836808649240993
            },
            "correct_probability": 0.015030322570169119,
            "correct_argmax": false,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t75",
            "order_averaged_probabilities": {
              "A": 0.030786133023184448,
              "B": 0.7908293604850769,
              "C": 0.17838452872820199
            },
            "correct_probability": 0.030786133023184448,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          }
        ],
        "mean_correct_probability": 0.26848031361683944
      },
      "source": {
        "n": 16,
        "records": [
          {
            "prompt_id": "s4t06",
            "order_averaged_probabilities": {
              "A": 0.38875165398349054,
              "B": 0.6112483590841293
            },
            "correct_probability": 0.38875165398349054,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t09",
            "order_averaged_probabilities": {
              "A": 0.9994150102138519,
              "B": 0.0005850073247870569
            },
            "correct_probability": 0.9994150102138519,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t17",
            "order_averaged_probabilities": {
              "A": 0.048706769943237305,
              "B": 0.9512932002544403
            },
            "correct_probability": 0.048706769943237305,
            "correct_argmax": false,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t18",
            "order_averaged_probabilities": {
              "A": 0.9929390549659729,
              "B": 0.007060959364025621
            },
            "correct_probability": 0.9929390549659729,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t25",
            "order_averaged_probabilities": {
              "A": 0.5297669097781181,
              "B": 0.47023305553011596
            },
            "correct_probability": 0.5297669097781181,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t28",
            "order_averaged_probabilities": {
              "A": 0.4567420557141304,
              "B": 0.543257936835289
            },
            "correct_probability": 0.4567420557141304,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t43",
            "order_averaged_probabilities": {
              "A": 0.2512363117421046,
              "B": 0.7487637102603912
            },
            "correct_probability": 0.2512363117421046,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t46",
            "order_averaged_probabilities": {
              "A": 0.8886499404907227,
              "B": 0.11135007800750518
            },
            "correct_probability": 0.8886499404907227,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t48",
            "order_averaged_probabilities": {
              "A": 0.5229623354971409,
              "B": 0.47703765804180875
            },
            "correct_probability": 0.5229623354971409,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t49",
            "order_averaged_probabilities": {
              "A": 0.9620700180530548,
              "B": 0.037929971774133264
            },
            "correct_probability": 0.9620700180530548,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t52",
            "order_averaged_probabilities": {
              "A": 0.19305908121168613,
              "B": 0.8069409132003784
            },
            "correct_probability": 0.19305908121168613,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t54",
            "order_averaged_probabilities": {
              "A": 0.11684354627504945,
              "B": 0.8831564784049988
            },
            "correct_probability": 0.11684354627504945,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t56",
            "order_averaged_probabilities": {
              "A": 0.6093150228261948,
              "B": 0.3906850095372647
            },
            "correct_probability": 0.6093150228261948,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t73",
            "order_averaged_probabilities": {
              "A": 0.9929642677307129,
              "B": 0.007035758361325861
            },
            "correct_probability": 0.9929642677307129,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t74",
            "order_averaged_probabilities": {
              "A": 0.9087391793727875,
              "B": 0.09126080814166926
            },
            "correct_probability": 0.9087391793727875,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t75",
            "order_averaged_probabilities": {
              "A": 0.9814795255661011,
              "B": 0.018520499113947153
            },
            "correct_probability": 0.9814795255661011,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          }
        ],
        "mean_correct_probability": 0.6152275427102722
      }
    },
    "R3/unsteered": {
      "EH_answer": {
        "n": 80,
        "mean": 0.08987590118631487
      },
      "answer_length": {
        "n": 80,
        "mean": 156.3125
      },
      "answer_truncated": {
        "n": 80,
        "mean": 0.3625
      },
      "valid_digit_mass": [
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        0.9999999403953552,
        1.0,
        0.9999999403953552,
        0.9999998807907104,
        1.0,
        1.0000001192092896,
        1.0,
        1.0,
        0.9999998211860657,
        1.0,
        1.0000001192092896,
        0.9999999403953552,
        1.0,
        0.9999997615814209,
        0.9999998807907104,
        0.9999998807907104,
        1.0000001192092896,
        1.0,
        0.9999998807907104,
        1.0,
        0.9999999403953552,
        1.0,
        0.9999999403953552,
        1.0,
        1.0,
        1.0000001192092896,
        0.9999998807907104,
        0.9999999403953552,
        0.9999998807907104,
        1.0,
        0.9999998211860657,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        0.9999383091926575,
        1.0000001192092896,
        0.9999999403953552,
        1.0000001192092896,
        0.9999999403953552,
        1.0,
        0.9999998807907104,
        1.0,
        0.9999999403953552,
        1.0,
        1.0000001192092896,
        0.9999999403953552,
        0.9999999403953552,
        1.0,
        1.0,
        1.0,
        0.9999999403953552,
        1.0000001192092896,
        0.9999998807907104,
        1.0,
        1.0,
        0.9999999403953552,
        1.0,
        0.9999997019767761,
        1.0,
        0.9999998807907104,
        0.9999998807907104,
        0.9999998807907104,
        0.9999999403953552,
        1.0,
        0.9999999403953552,
        0.9999999403953552,
        0.9999999403953552,
        1.0,
        0.9999999403953552,
        0.9999998807907104,
        1.0,
        0.9999998211860657,
        0.9999999403953552
      ],
      "baseline_mean": 7.743991455486304,
      "baseline_sd": 0.2788967531047724,
      "structural": {
        "n": 16,
        "records": [
          {
            "prompt_id": "s4t06",
            "order_averaged_probabilities": {
              "A": 0.49290968971854454,
              "B": 0.4997829826643283,
              "C": 0.007307347288588062
            },
            "correct_probability": 0.4997829826643283,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t09",
            "order_averaged_probabilities": {
              "A": 0.07714063530116277,
              "B": 0.5765553936362267,
              "C": 0.34630394337000325
            },
            "correct_probability": 0.5765553936362267,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t17",
            "order_averaged_probabilities": {
              "A": 0.4994164004431241,
              "B": 0.4995433346072673,
              "C": 0.0010402790794614702
            },
            "correct_probability": 0.4995433346072673,
            "correct_argmax": true,
            "valid_mass": [
              1.0000001192092896,
              1.0000001192092896
            ]
          },
          {
            "prompt_id": "s4t18",
            "order_averaged_probabilities": {
              "A": 0.3393897034748079,
              "B": 0.4932672445429489,
              "C": 0.16734302137047052
            },
            "correct_probability": 0.4932672445429489,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t25",
            "order_averaged_probabilities": {
              "A": 0.49722435656772745,
              "B": 0.4999988342024153,
              "C": 0.0027768673753598705
            },
            "correct_probability": 0.4999988342024153,
            "correct_argmax": true,
            "valid_mass": [
              1.0000001192092896,
              1.0
            ]
          },
          {
            "prompt_id": "s4t28",
            "order_averaged_probabilities": {
              "A": 0.49831566327088694,
              "B": 0.49988302923884476,
              "C": 0.0018012969667324796
            },
            "correct_probability": 0.49988302923884476,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t43",
            "order_averaged_probabilities": {
              "A": 0.49769094979781414,
              "B": 0.5002574432000984,
              "C": 0.002051626786851557
            },
            "correct_probability": 0.5002574432000984,
            "correct_argmax": true,
            "valid_mass": [
              0.9999998807907104,
              1.0
            ]
          },
          {
            "prompt_id": "s4t46",
            "order_averaged_probabilities": {
              "A": 0.4998981057176408,
              "B": 0.4997849423476737,
              "C": 0.00031699192913947627
            },
            "correct_probability": 0.4997849423476737,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t48",
            "order_averaged_probabilities": {
              "A": 0.49097889644252035,
              "B": 0.4996736757839244,
              "C": 0.009347425133455545
            },
            "correct_probability": 0.4996736757839244,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t49",
            "order_averaged_probabilities": {
              "A": 0.49655507354475503,
              "B": 0.4995144337590318,
              "C": 0.003930502338334918
            },
            "correct_probability": 0.4995144337590318,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t52",
            "order_averaged_probabilities": {
              "A": 0.4370679318601396,
              "B": 0.5037439467851073,
              "C": 0.05918814126562211
            },
            "correct_probability": 0.5037439467851073,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999998807907104
            ]
          },
          {
            "prompt_id": "s4t54",
            "order_averaged_probabilities": {
              "A": 0.4992490151517899,
              "B": 0.49978509206147237,
              "C": 0.0009658687631599605
            },
            "correct_probability": 0.49978509206147237,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t56",
            "order_averaged_probabilities": {
              "A": 0.4990344520515606,
              "B": 0.4997868873444986,
              "C": 0.0011786412505898625
            },
            "correct_probability": 0.4997868873444986,
            "correct_argmax": true,
            "valid_mass": [
              1.0000001192092896,
              1.0
            ]
          },
          {
            "prompt_id": "s4t73",
            "order_averaged_probabilities": {
              "A": 0.01781634431608836,
              "B": 0.9592361450195312,
              "C": 0.022947505764022935
            },
            "correct_probability": 0.9592361450195312,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t74",
            "order_averaged_probabilities": {
              "A": 0.029992839001806715,
              "B": 0.8648800849914551,
              "C": 0.10512706730514765
            },
            "correct_probability": 0.8648800849914551,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t75",
            "order_averaged_probabilities": {
              "A": 0.08568806012522145,
              "B": 0.7323306649923325,
              "C": 0.18198131123790517
            },
            "correct_probability": 0.7323306649923325,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          }
        ],
        "mean_correct_probability": 0.5705015084485723
      },
      "source": {
        "n": 16,
        "records": [
          {
            "prompt_id": "s4t06",
            "order_averaged_probabilities": {
              "A": 0.7798519730567932,
              "B": 0.220148078748025
            },
            "correct_probability": 0.7798519730567932,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t09",
            "order_averaged_probabilities": {
              "A": 0.9859012961387634,
              "B": 0.014098748564720154
            },
            "correct_probability": 0.9859012961387634,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0000001192092896
            ]
          },
          {
            "prompt_id": "s4t17",
            "order_averaged_probabilities": {
              "A": 0.040539154782891273,
              "B": 0.9594608843326569
            },
            "correct_probability": 0.040539154782891273,
            "correct_argmax": false,
            "valid_mass": [
              1.0000001192092896,
              1.0
            ]
          },
          {
            "prompt_id": "s4t18",
            "order_averaged_probabilities": {
              "A": 0.9813362956047058,
              "B": 0.018663695798693425
            },
            "correct_probability": 0.9813362956047058,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t25",
            "order_averaged_probabilities": {
              "A": 0.8022365570068359,
              "B": 0.19776344392448664
            },
            "correct_probability": 0.8022365570068359,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t28",
            "order_averaged_probabilities": {
              "A": 0.08560382574796677,
              "B": 0.9143961668014526
            },
            "correct_probability": 0.08560382574796677,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t43",
            "order_averaged_probabilities": {
              "A": 0.49955128983128816,
              "B": 0.5004487212281674
            },
            "correct_probability": 0.49955128983128816,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t46",
            "order_averaged_probabilities": {
              "A": 0.9403984546661377,
              "B": 0.059601507198717485
            },
            "correct_probability": 0.9403984546661377,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t48",
            "order_averaged_probabilities": {
              "A": 0.5906280055642128,
              "B": 0.40937197586754337
            },
            "correct_probability": 0.5906280055642128,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t49",
            "order_averaged_probabilities": {
              "A": 0.7810265719890594,
              "B": 0.21897346430341713
            },
            "correct_probability": 0.7810265719890594,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t52",
            "order_averaged_probabilities": {
              "A": 0.1492791660130024,
              "B": 0.8507208526134491
            },
            "correct_probability": 0.1492791660130024,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t54",
            "order_averaged_probabilities": {
              "A": 0.02364922035485506,
              "B": 0.9763507544994354
            },
            "correct_probability": 0.02364922035485506,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t56",
            "order_averaged_probabilities": {
              "A": 0.5235823132097721,
              "B": 0.47641766209562775
            },
            "correct_probability": 0.5235823132097721,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t73",
            "order_averaged_probabilities": {
              "A": 0.9884496331214905,
              "B": 0.01155038268188946
            },
            "correct_probability": 0.9884496331214905,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t74",
            "order_averaged_probabilities": {
              "A": 0.96132031083107,
              "B": 0.03867968270787969
            },
            "correct_probability": 0.96132031083107,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t75",
            "order_averaged_probabilities": {
              "A": 0.9507389068603516,
              "B": 0.04926107556093484
            },
            "correct_probability": 0.9507389068603516,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          }
        ],
        "mean_correct_probability": 0.6302558109236998
      }
    },
    "R3/hostility": {
      "EH_answer": {
        "n": 80,
        "mean": 0.12024098103429423
      },
      "answer_length": {
        "n": 80,
        "mean": 157.0
      },
      "answer_truncated": {
        "n": 80,
        "mean": 0.4
      },
      "valid_digit_mass": [
        0.9999998807907104,
        1.0,
        0.9999999403953552,
        0.9999999403953552,
        1.0000001192092896,
        1.0,
        1.0,
        1.0,
        0.9999999403953552,
        1.0000001192092896,
        0.9999999403953552,
        0.9999997615814209,
        1.0,
        1.0,
        1.0,
        0.9999998807907104,
        1.0,
        0.9999998807907104,
        1.0,
        0.9999999403953552,
        1.0,
        1.0,
        1.0,
        0.9999999403953552,
        1.0,
        0.9999999403953552,
        1.0,
        1.0000001192092896,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        0.9999999403953552,
        1.0,
        0.9999999403953552,
        0.9999999403953552,
        1.0,
        1.0,
        1.0000001192092896,
        1.0,
        0.9999999403953552,
        0.9999999403953552,
        1.0000001192092896,
        1.0,
        1.0,
        0.9999999403953552,
        0.9999998807907104,
        1.0,
        1.0,
        1.0,
        0.9999999403953552,
        1.0000001192092896,
        0.9999999403953552,
        1.0,
        1.0000001192092896,
        1.0,
        1.0,
        0.9999999403953552,
        1.0,
        0.9999998807907104,
        0.9999998807907104,
        1.0,
        1.0,
        0.9999998807907104,
        1.0000001192092896,
        1.0000001192092896,
        1.0,
        0.9999999403953552,
        0.9999999403953552,
        1.0,
        1.0,
        1.0,
        1.0,
        0.9999997615814209,
        1.0,
        1.0,
        1.0,
        0.9999999403953552,
        1.0
      ],
      "baseline_mean": null,
      "baseline_sd": null,
      "structural": {
        "n": 16,
        "records": [
          {
            "prompt_id": "s4t06",
            "order_averaged_probabilities": {
              "A": 0.21606898552636267,
              "B": 0.5055472045205534,
              "C": 0.27838377229636535
            },
            "correct_probability": 0.5055472045205534,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              0.9999998807907104
            ]
          },
          {
            "prompt_id": "s4t09",
            "order_averaged_probabilities": {
              "A": 0.33864943594031516,
              "B": 0.5012822077842429,
              "C": 0.16006836110318545
            },
            "correct_probability": 0.5012822077842429,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t17",
            "order_averaged_probabilities": {
              "A": 0.09120425452380232,
              "B": 0.49908639774730545,
              "C": 0.40970939997350797
            },
            "correct_probability": 0.49908639774730545,
            "correct_argmax": true,
            "valid_mass": [
              0.9999998807907104,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t18",
            "order_averaged_probabilities": {
              "A": 0.3386499249508006,
              "B": 0.5004200563998893,
              "C": 0.16093001392437145
            },
            "correct_probability": 0.5004200563998893,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t25",
            "order_averaged_probabilities": {
              "A": 0.11039688020926519,
              "B": 0.5038249301724136,
              "C": 0.38577815593453124
            },
            "correct_probability": 0.5038249301724136,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t28",
            "order_averaged_probabilities": {
              "A": 0.008869067555934862,
              "B": 0.5042968187481165,
              "C": 0.48683408345095813
            },
            "correct_probability": 0.5042968187481165,
            "correct_argmax": true,
            "valid_mass": [
              1.0000001192092896,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t43",
            "order_averaged_probabilities": {
              "A": 0.16020080321735009,
              "B": 0.575457826256752,
              "C": 0.2643413408077322
            },
            "correct_probability": 0.575457826256752,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t46",
            "order_averaged_probabilities": {
              "A": 0.4929577973964143,
              "B": 0.4998799481018068,
              "C": 0.007162260342738591
            },
            "correct_probability": 0.4998799481018068,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t48",
            "order_averaged_probabilities": {
              "A": 0.42590257563355116,
              "B": 0.5000639483332634,
              "C": 0.07403346597675409
            },
            "correct_probability": 0.5000639483332634,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t49",
            "order_averaged_probabilities": {
              "A": 0.2497603742638148,
              "B": 0.4984456064994447,
              "C": 0.2517939917743206
            },
            "correct_probability": 0.4984456064994447,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t52",
            "order_averaged_probabilities": {
              "A": 0.06580135694372302,
              "B": 0.6391321271657944,
              "C": 0.29506648289680015
            },
            "correct_probability": 0.6391321271657944,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t54",
            "order_averaged_probabilities": {
              "A": 0.16035060790036937,
              "B": 0.49860122438985854,
              "C": 0.34104814438614994
            },
            "correct_probability": 0.49860122438985854,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t56",
            "order_averaged_probabilities": {
              "A": 0.05958828274162897,
              "B": 0.4985281769550056,
              "C": 0.44188352627679706
            },
            "correct_probability": 0.4985281769550056,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t73",
            "order_averaged_probabilities": {
              "A": 0.005313282306815381,
              "B": 0.9761415421962738,
              "C": 0.018545178645581473
            },
            "correct_probability": 0.9761415421962738,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t74",
            "order_averaged_probabilities": {
              "A": 0.01635601452494484,
              "B": 0.8275167644023895,
              "C": 0.15612726291874424
            },
            "correct_probability": 0.8275167644023895,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t75",
            "order_averaged_probabilities": {
              "A": 0.055729867131731226,
              "B": 0.7496271133422852,
              "C": 0.19464299191895407
            },
            "correct_probability": 0.7496271133422852,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          }
        ],
        "mean_correct_probability": 0.5798657433134622
      },
      "source": {
        "n": 16,
        "records": [
          {
            "prompt_id": "s4t06",
            "order_averaged_probabilities": {
              "A": 0.16137402487220243,
              "B": 0.838625967502594
            },
            "correct_probability": 0.16137402487220243,
            "correct_argmax": false,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t09",
            "order_averaged_probabilities": {
              "A": 0.990927666425705,
              "B": 0.009072323147847783
            },
            "correct_probability": 0.990927666425705,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t17",
            "order_averaged_probabilities": {
              "A": 0.6386499404907227,
              "B": 0.36135007441043854
            },
            "correct_probability": 0.6386499404907227,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t18",
            "order_averaged_probabilities": {
              "A": 0.9999708533287048,
              "B": 2.9146957758130476e-05
            },
            "correct_probability": 0.9999708533287048,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t25",
            "order_averaged_probabilities": {
              "A": 0.048706769943237305,
              "B": 0.9512932002544403
            },
            "correct_probability": 0.048706769943237305,
            "correct_argmax": false,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t28",
            "order_averaged_probabilities": {
              "A": 0.5050494708120823,
              "B": 0.4949505105614662
            },
            "correct_probability": 0.5050494708120823,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t43",
            "order_averaged_probabilities": {
              "A": 0.6276989877223969,
              "B": 0.37230101972818375
            },
            "correct_probability": 0.6276989877223969,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t46",
            "order_averaged_probabilities": {
              "A": 0.9929682016372681,
              "B": 0.00703182628454968
            },
            "correct_probability": 0.9929682016372681,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t48",
            "order_averaged_probabilities": {
              "A": 0.9990366101264954,
              "B": 0.0009633673984492663
            },
            "correct_probability": 0.9990366101264954,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t49",
            "order_averaged_probabilities": {
              "A": 0.6291688531637192,
              "B": 0.3708311393857002
            },
            "correct_probability": 0.6291688531637192,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t52",
            "order_averaged_probabilities": {
              "A": 0.2844346882775426,
              "B": 0.7155653536319733
            },
            "correct_probability": 0.2844346882775426,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t54",
            "order_averaged_probabilities": {
              "A": 0.5000000153668225,
              "B": 0.5000000153668225
            },
            "correct_probability": 0.5000000153668225,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t56",
            "order_averaged_probabilities": {
              "A": 0.6097637265920639,
              "B": 0.3902362819062546
            },
            "correct_probability": 0.6097637265920639,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t73",
            "order_averaged_probabilities": {
              "A": 0.9943759143352509,
              "B": 0.005624067023745738
            },
            "correct_probability": 0.9943759143352509,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t74",
            "order_averaged_probabilities": {
              "A": 0.7479649484157562,
              "B": 0.25203506904654205
            },
            "correct_probability": 0.7479649484157562,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t75",
            "order_averaged_probabilities": {
              "A": 0.6311243027448654,
              "B": 0.36887572426348925
            },
            "correct_probability": 0.6311243027448654,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          }
        ],
        "mean_correct_probability": 0.6475759358909272
      }
    },
    "R3/technicality": {
      "EH_answer": {
        "n": 80,
        "mean": 0.06930096868018154
      },
      "answer_length": {
        "n": 80,
        "mean": 172.3125
      },
      "answer_truncated": {
        "n": 80,
        "mean": 0.45
      },
      "valid_digit_mass": [
        1.0,
        1.0,
        1.0,
        0.9999997615814209,
        0.9999998807907104,
        0.9999998807907104,
        0.9999998807907104,
        0.9999998807907104,
        1.0,
        1.0,
        1.0,
        0.9999999403953552,
        1.0,
        0.9999992847442627,
        0.9999998807907104,
        1.0,
        1.0000001192092896,
        1.0,
        0.9999996423721313,
        0.9999997615814209,
        1.0,
        1.0,
        1.0,
        0.9999997019767761,
        0.9999998807907104,
        0.9999998807907104,
        0.9999999403953552,
        0.9999998807907104,
        1.0,
        1.0,
        1.0000001192092896,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        0.9999998807907104,
        1.0000001192092896,
        0.9999998807907104,
        0.9999999403953552,
        1.0000001192092896,
        0.9999991059303284,
        0.9999999403953552,
        1.0,
        0.9999999403953552,
        0.9999999403953552,
        1.0,
        0.9999999403953552,
        0.9999999403953552,
        1.0,
        1.0000001192092896,
        1.0,
        0.9999999403953552,
        0.9999999403953552,
        0.9999998211860657,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        0.9999998807907104,
        0.9999999403953552,
        1.0000001192092896,
        1.0,
        1.0,
        0.9999998807907104,
        0.9999997019767761,
        1.0,
        1.0,
        0.9999999403953552,
        1.0,
        0.9999999403953552,
        1.0,
        0.9999998807907104,
        1.0,
        0.9999998807907104,
        0.9999999403953552,
        1.0000001192092896,
        0.9999991059303284,
        1.0
      ],
      "baseline_mean": null,
      "baseline_sd": null,
      "structural": {
        "n": 16,
        "records": [
          {
            "prompt_id": "s4t06",
            "order_averaged_probabilities": {
              "A": 0.07020263185154363,
              "B": 0.5252380929887295,
              "C": 0.4045592556358315
            },
            "correct_probability": 0.5252380929887295,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t09",
            "order_averaged_probabilities": {
              "A": 0.12145004498552225,
              "B": 0.6198589578270912,
              "C": 0.2586910288082436
            },
            "correct_probability": 0.6198589578270912,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t17",
            "order_averaged_probabilities": {
              "A": 0.4979658393573345,
              "B": 0.49964426645746585,
              "C": 0.0023899023071862757
            },
            "correct_probability": 0.49964426645746585,
            "correct_argmax": true,
            "valid_mass": [
              1.0000001192092896,
              1.0000001192092896
            ]
          },
          {
            "prompt_id": "s4t18",
            "order_averaged_probabilities": {
              "A": 0.38819773312013695,
              "B": 0.49797211156692356,
              "C": 0.11383015452884138
            },
            "correct_probability": 0.49797211156692356,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t25",
            "order_averaged_probabilities": {
              "A": 0.3102178156049149,
              "B": 0.5006630757125095,
              "C": 0.18911910516908392
            },
            "correct_probability": 0.5006630757125095,
            "correct_argmax": true,
            "valid_mass": [
              1.0000001192092896,
              1.0
            ]
          },
          {
            "prompt_id": "s4t28",
            "order_averaged_probabilities": {
              "A": 0.07334711675866856,
              "B": 0.5003816965036094,
              "C": 0.42627123836427927
            },
            "correct_probability": 0.5003816965036094,
            "correct_argmax": true,
            "valid_mass": [
              0.9999998807907104,
              1.0000001192092896
            ]
          },
          {
            "prompt_id": "s4t43",
            "order_averaged_probabilities": {
              "A": 0.4998654863341123,
              "B": 0.49998624102181566,
              "C": 0.00014827225095359609
            },
            "correct_probability": 0.49998624102181566,
            "correct_argmax": true,
            "valid_mass": [
              0.9999998807907104,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t46",
            "order_averaged_probabilities": {
              "A": 0.4990354614824639,
              "B": 0.49978588816236424,
              "C": 0.0011786430841311812
            },
            "correct_probability": 0.49978588816236424,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0000001192092896
            ]
          },
          {
            "prompt_id": "s4t48",
            "order_averaged_probabilities": {
              "A": 0.4957031944735064,
              "B": 0.49990644454919675,
              "C": 0.004390385001897812
            },
            "correct_probability": 0.49990644454919675,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t49",
            "order_averaged_probabilities": {
              "A": 0.4955912326104226,
              "B": 0.4985348424233962,
              "C": 0.0058739472879096866
            },
            "correct_probability": 0.4985348424233962,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999998807907104
            ]
          },
          {
            "prompt_id": "s4t52",
            "order_averaged_probabilities": {
              "A": 0.3650142378577712,
              "B": 0.5004892617580481,
              "C": 0.1344964965537656
            },
            "correct_probability": 0.5004892617580481,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t54",
            "order_averaged_probabilities": {
              "A": 0.49954438054228945,
              "B": 0.49989840080627346,
              "C": 0.0005572385271079838
            },
            "correct_probability": 0.49989840080627346,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t56",
            "order_averaged_probabilities": {
              "A": 0.24949061709784814,
              "B": 0.5008515242952853,
              "C": 0.24965787641122006
            },
            "correct_probability": 0.5008515242952853,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t73",
            "order_averaged_probabilities": {
              "A": 0.37423140783357667,
              "B": 0.6069244742393494,
              "C": 0.018844065300072543
            },
            "correct_probability": 0.6069244742393494,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t74",
            "order_averaged_probabilities": {
              "A": 0.4211197525073658,
              "B": 0.5430814698338509,
              "C": 0.03579872101545334
            },
            "correct_probability": 0.5430814698338509,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t75",
            "order_averaged_probabilities": {
              "A": 0.33938304530056485,
              "B": 0.6246789991855621,
              "C": 0.035937970809754916
            },
            "correct_probability": 0.6246789991855621,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          }
        ],
        "mean_correct_probability": 0.5261184842082169
      },
      "source": {
        "n": 16,
        "records": [
          {
            "prompt_id": "s4t06",
            "order_averaged_probabilities": {
              "A": 0.9698478579521179,
              "B": 0.030152129009366035
            },
            "correct_probability": 0.9698478579521179,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t09",
            "order_averaged_probabilities": {
              "A": 0.9998321533203125,
              "B": 0.00016782803460557716
            },
            "correct_probability": 0.9998321533203125,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t17",
            "order_averaged_probabilities": {
              "A": 0.2929353639483452,
              "B": 0.7070646286010742
            },
            "correct_probability": 0.2929353639483452,
            "correct_argmax": false,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t18",
            "order_averaged_probabilities": {
              "A": 0.9762869477272034,
              "B": 0.023713055907251146
            },
            "correct_probability": 0.9762869477272034,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t25",
            "order_averaged_probabilities": {
              "A": 0.009094818524317816,
              "B": 0.9909051656723022
            },
            "correct_probability": 0.009094818524317816,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t28",
            "order_averaged_probabilities": {
              "A": 0.07425757870078087,
              "B": 0.9257423877716064
            },
            "correct_probability": 0.07425757870078087,
            "correct_argmax": false,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t43",
            "order_averaged_probabilities": {
              "A": 0.9945065379142761,
              "B": 0.005493498443536637
            },
            "correct_probability": 0.9945065379142761,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t46",
            "order_averaged_probabilities": {
              "A": 0.5146560557186604,
              "B": 0.4853439173220657
            },
            "correct_probability": 0.5146560557186604,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t48",
            "order_averaged_probabilities": {
              "A": 0.5089930454269052,
              "B": 0.4910069248198532
            },
            "correct_probability": 0.5089930454269052,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t49",
            "order_averaged_probabilities": {
              "A": 0.5235452689230442,
              "B": 0.47645474201999605
            },
            "correct_probability": 0.5235452689230442,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t52",
            "order_averaged_probabilities": {
              "A": 0.02024978504050523,
              "B": 0.9797501862049103
            },
            "correct_probability": 0.02024978504050523,
            "correct_argmax": false,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t54",
            "order_averaged_probabilities": {
              "A": 0.4775233786785975,
              "B": 0.5224766470491886
            },
            "correct_probability": 0.4775233786785975,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t56",
            "order_averaged_probabilities": {
              "A": 0.520137295126915,
              "B": 0.4798626974225044
            },
            "correct_probability": 0.520137295126915,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t73",
            "order_averaged_probabilities": {
              "A": 0.887063592672348,
              "B": 0.11293641582597047
            },
            "correct_probability": 0.887063592672348,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t74",
            "order_averaged_probabilities": {
              "A": 0.7743165194988251,
              "B": 0.22568347305059433
            },
            "correct_probability": 0.7743165194988251,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t75",
            "order_averaged_probabilities": {
              "A": 0.99021777510643,
              "B": 0.009782214183360338
            },
            "correct_probability": 0.99021777510643,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          }
        ],
        "mean_correct_probability": 0.595841498392474
      }
    },
    "R3/random": {
      "EH_answer": {
        "n": 80,
        "mean": 0.07028405079763615
      },
      "answer_length": {
        "n": 80,
        "mean": 158.6125
      },
      "answer_truncated": {
        "n": 80,
        "mean": 0.4
      },
      "valid_digit_mass": [
        1.0000001192092896,
        1.0,
        1.0,
        0.9999999403953552,
        1.0,
        1.0,
        1.0,
        0.9999999403953552,
        1.0,
        1.0,
        0.9999999403953552,
        0.9999997019767761,
        1.0,
        0.9999974966049194,
        1.0,
        1.0,
        0.9999999403953552,
        1.0000001192092896,
        0.9999998807907104,
        1.0,
        1.0000001192092896,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        0.9999999403953552,
        1.0,
        1.0,
        0.9999999403953552,
        1.0,
        1.0000001192092896,
        0.9999999403953552,
        1.0000001192092896,
        1.0,
        1.0,
        1.0,
        1.0,
        0.9999996423721313,
        0.9999999403953552,
        0.9999993443489075,
        1.0,
        0.9999999403953552,
        0.9999998807907104,
        1.0,
        1.0,
        0.9999998211860657,
        0.9999988675117493,
        1.0,
        0.9999999403953552,
        1.0,
        0.9999998807907104,
        1.0,
        0.9999998807907104,
        1.0,
        0.9999998807907104,
        1.0,
        0.9999999403953552,
        1.0,
        0.9999999403953552,
        1.0,
        0.9999999403953552,
        1.0,
        0.9999999403953552,
        1.0000001192092896,
        1.0,
        0.9999999403953552,
        0.9999997019767761,
        1.0,
        0.9999999403953552,
        1.0,
        1.0,
        1.0,
        0.9999999403953552,
        0.9999998807907104,
        1.0,
        1.0,
        0.9999990463256836,
        1.0
      ],
      "baseline_mean": null,
      "baseline_sd": null,
      "structural": {
        "n": 16,
        "records": [
          {
            "prompt_id": "s4t06",
            "order_averaged_probabilities": {
              "A": 0.15629484144898242,
              "B": 0.5125529142096639,
              "C": 0.33115223300410435
            },
            "correct_probability": 0.5125529142096639,
            "correct_argmax": true,
            "valid_mass": [
              0.9999998807907104,
              1.0
            ]
          },
          {
            "prompt_id": "s4t09",
            "order_averaged_probabilities": {
              "A": 0.11126154419616796,
              "B": 0.5810186117887497,
              "C": 0.30771986953914165
            },
            "correct_probability": 0.5810186117887497,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t17",
            "order_averaged_probabilities": {
              "A": 0.49796172477181244,
              "B": 0.4996484536814023,
              "C": 0.0023898666840977967
            },
            "correct_probability": 0.4996484536814023,
            "correct_argmax": true,
            "valid_mass": [
              1.0000001192092896,
              1.0
            ]
          },
          {
            "prompt_id": "s4t18",
            "order_averaged_probabilities": {
              "A": 0.09118119010901182,
              "B": 0.4968290702672675,
              "C": 0.411989786894992
            },
            "correct_probability": 0.4968290702672675,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t25",
            "order_averaged_probabilities": {
              "A": 0.4978865820441456,
              "B": 0.5000412255976698,
              "C": 0.0020721708351629786
            },
            "correct_probability": 0.5000412255976698,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t28",
            "order_averaged_probabilities": {
              "A": 0.1994768232871138,
              "B": 0.5401626937091351,
              "C": 0.2603604677133262
            },
            "correct_probability": 0.5401626937091351,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t43",
            "order_averaged_probabilities": {
              "A": 0.38193952886419424,
              "B": 0.5516413860023022,
              "C": 0.06641911952829105
            },
            "correct_probability": 0.5516413860023022,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t46",
            "order_averaged_probabilities": {
              "A": 0.48850653006592637,
              "B": 0.49978962683735517,
              "C": 0.01170385027944576
            },
            "correct_probability": 0.49978962683735517,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t48",
            "order_averaged_probabilities": {
              "A": 0.4699410957332706,
              "B": 0.4998859923634882,
              "C": 0.030172924962243997
            },
            "correct_probability": 0.4998859923634882,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t49",
            "order_averaged_probabilities": {
              "A": 0.47609209829619203,
              "B": 0.4997491570102284,
              "C": 0.024158733431249857
            },
            "correct_probability": 0.4997491570102284,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t52",
            "order_averaged_probabilities": {
              "A": 0.494159656420905,
              "B": 0.5002490452607162,
              "C": 0.0055913296455401
            },
            "correct_probability": 0.5002490452607162,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t54",
            "order_averaged_probabilities": {
              "A": 0.21860754262942805,
              "B": 0.49973197147483006,
              "C": 0.2816604738472961
            },
            "correct_probability": 0.49973197147483006,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t56",
            "order_averaged_probabilities": {
              "A": 0.4521495084289029,
              "B": 0.49960959125019144,
              "C": 0.048240921983961016
            },
            "correct_probability": 0.49960959125019144,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t73",
            "order_averaged_probabilities": {
              "A": 0.0016594926855759695,
              "B": 0.9887907803058624,
              "C": 0.00954972067847848
            },
            "correct_probability": 0.9887907803058624,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t74",
            "order_averaged_probabilities": {
              "A": 0.0279205445003754,
              "B": 0.9358106851577759,
              "C": 0.03626879717921838
            },
            "correct_probability": 0.9358106851577759,
            "correct_argmax": true,
            "valid_mass": [
              1.0000001192092896,
              1.0
            ]
          },
          {
            "prompt_id": "s4t75",
            "order_averaged_probabilities": {
              "A": 0.11361638891185066,
              "B": 0.7397550642490387,
              "C": 0.14662856853101403
            },
            "correct_probability": 0.7397550642490387,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          }
        ],
        "mean_correct_probability": 0.5840791418228548
      },
      "source": {
        "n": 16,
        "records": [
          {
            "prompt_id": "s4t06",
            "order_averaged_probabilities": {
              "A": 0.0746083520934917,
              "B": 0.9253916144371033
            },
            "correct_probability": 0.0746083520934917,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t09",
            "order_averaged_probabilities": {
              "A": 0.9995445013046265,
              "B": 0.00045554631610578156
            },
            "correct_probability": 0.9995445013046265,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t17",
            "order_averaged_probabilities": {
              "A": 0.02614480070769787,
              "B": 0.973855197429657
            },
            "correct_probability": 0.02614480070769787,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t18",
            "order_averaged_probabilities": {
              "A": 0.9255208671092987,
              "B": 0.07447912255884148
            },
            "correct_probability": 0.9255208671092987,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t25",
            "order_averaged_probabilities": {
              "A": 0.5065763150341809,
              "B": 0.4934237272536848
            },
            "correct_probability": 0.5065763150341809,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t28",
            "order_averaged_probabilities": {
              "A": 0.311131589114666,
              "B": 0.6888684332370758
            },
            "correct_probability": 0.311131589114666,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t43",
            "order_averaged_probabilities": {
              "A": 0.5031674392521381,
              "B": 0.4968325588852167
            },
            "correct_probability": 0.5031674392521381,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t46",
            "order_averaged_probabilities": {
              "A": 0.6604082733392715,
              "B": 0.33959174992355656
            },
            "correct_probability": 0.6604082733392715,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t48",
            "order_averaged_probabilities": {
              "A": 0.5740008875727654,
              "B": 0.42599906473878946
            },
            "correct_probability": 0.5740008875727654,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t49",
            "order_averaged_probabilities": {
              "A": 0.6417471915483475,
              "B": 0.35825280100107193
            },
            "correct_probability": 0.6417471915483475,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t52",
            "order_averaged_probabilities": {
              "A": 0.49146240661502816,
              "B": 0.5085376063361764
            },
            "correct_probability": 0.49146240661502816,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t54",
            "order_averaged_probabilities": {
              "A": 0.35338248312473297,
              "B": 0.6466175615787506
            },
            "correct_probability": 0.35338248312473297,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t56",
            "order_averaged_probabilities": {
              "A": 0.5593674704432487,
              "B": 0.44063248112797737
            },
            "correct_probability": 0.5593674704432487,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t73",
            "order_averaged_probabilities": {
              "A": 0.9616154134273529,
              "B": 0.038384617218980566
            },
            "correct_probability": 0.9616154134273529,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t74",
            "order_averaged_probabilities": {
              "A": 0.9517405033111572,
              "B": 0.04825948929646984
            },
            "correct_probability": 0.9517405033111572,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t75",
            "order_averaged_probabilities": {
              "A": 0.9698478579521179,
              "B": 0.030152129009366035
            },
            "correct_probability": 0.9698478579521179,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          }
        ],
        "mean_correct_probability": 0.5943916469968826
      }
    },
    "R4/unsteered": {
      "EH_answer": {
        "n": 80,
        "mean": 0.038377025882073215
      },
      "answer_length": {
        "n": 80,
        "mean": 147.925
      },
      "answer_truncated": {
        "n": 80,
        "mean": 0.325
      },
      "valid_digit_mass": [
        0.9999998807907104,
        1.0000001192092896,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        0.9999999403953552,
        1.0000001192092896,
        0.9999999403953552,
        0.9999996423721313,
        1.0,
        1.0000001192092896,
        1.0,
        1.0000001192092896,
        0.9999997019767761,
        0.9999998807907104,
        0.9999999403953552,
        1.0,
        1.0,
        1.0,
        1.0,
        0.9999999403953552,
        1.0,
        1.0,
        1.0,
        1.0000001192092896,
        1.0,
        1.0,
        1.0,
        1.0000001192092896,
        1.0,
        0.9999999403953552,
        1.0,
        0.9999998807907104,
        0.9999999403953552,
        1.0,
        1.0,
        0.9999999403953552,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        0.9999999403953552,
        1.0,
        1.0,
        0.9999999403953552,
        1.0000001192092896,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0000001192092896,
        1.0,
        1.0,
        0.9999999403953552,
        1.0,
        1.0000001192092896,
        1.0000001192092896,
        0.9999999403953552,
        1.0,
        1.0,
        0.9999999403953552,
        1.0,
        1.0,
        1.0,
        0.9999999403953552,
        1.0,
        1.0,
        1.0000001192092896,
        0.9999999403953552,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0000001192092896,
        1.0
      ],
      "baseline_mean": 6.787080641393456,
      "baseline_sd": 0.3918952463547403,
      "structural": {
        "n": 16,
        "records": [
          {
            "prompt_id": "s4t06",
            "order_averaged_probabilities": {
              "A": 2.636845928560838e-05,
              "B": 0.9521337449550629,
              "C": 0.047839894657954574
            },
            "correct_probability": 0.047839894657954574,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t09",
            "order_averaged_probabilities": {
              "A": 3.2361893954196974e-07,
              "B": 0.9996157288551331,
              "C": 0.0003839806122414302
            },
            "correct_probability": 0.0003839806122414302,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0000001192092896
            ]
          },
          {
            "prompt_id": "s4t17",
            "order_averaged_probabilities": {
              "A": 0.0017349470728760252,
              "B": 0.9243306219577789,
              "C": 0.073934435567935
            },
            "correct_probability": 0.073934435567935,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t18",
            "order_averaged_probabilities": {
              "A": 1.1257097128292148e-05,
              "B": 0.9086103439331055,
              "C": 0.09137838310562074
            },
            "correct_probability": 0.09137838310562074,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t25",
            "order_averaged_probabilities": {
              "A": 1.6120549558245158e-08,
              "B": 0.9999769926071167,
              "C": 2.302273153986789e-05
            },
            "correct_probability": 2.302273153986789e-05,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t28",
            "order_averaged_probabilities": {
              "A": 1.1906730090771589e-07,
              "B": 0.9997183978557587,
              "C": 0.00028145423630121513
            },
            "correct_probability": 0.00028145423630121513,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t43",
            "order_averaged_probabilities": {
              "A": 5.031097099394619e-06,
              "B": 0.9966484010219574,
              "C": 0.003346544671799734
            },
            "correct_probability": 0.003346544671799734,
            "correct_argmax": false,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t46",
            "order_averaged_probabilities": {
              "A": 9.937685700013316e-05,
              "B": 0.9884127974510193,
              "C": 0.011487852937534626
            },
            "correct_probability": 0.011487852937534626,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t48",
            "order_averaged_probabilities": {
              "A": 0.002592685345811696,
              "B": 0.5032673825044185,
              "C": 0.49413997583906166
            },
            "correct_probability": 0.49413997583906166,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0000001192092896
            ]
          },
          {
            "prompt_id": "s4t49",
            "order_averaged_probabilities": {
              "A": 0.00046747762535648274,
              "B": 0.8108769953250885,
              "C": 0.1886555468372535
            },
            "correct_probability": 0.1886555468372535,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t52",
            "order_averaged_probabilities": {
              "A": 6.796647653087295e-07,
              "B": 0.9957021772861481,
              "C": 0.004297086977203435
            },
            "correct_probability": 0.004297086977203435,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              0.9999998807907104
            ]
          },
          {
            "prompt_id": "s4t54",
            "order_averaged_probabilities": {
              "A": 0.00010677767469846611,
              "B": 0.9086821973323822,
              "C": 0.09121095178852556
            },
            "correct_probability": 0.09121095178852556,
            "correct_argmax": false,
            "valid_mass": [
              0.9999999403953552,
              0.9999998807907104
            ]
          },
          {
            "prompt_id": "s4t56",
            "order_averaged_probabilities": {
              "A": 7.626173587022e-05,
              "B": 0.5186314508318901,
              "C": 0.4812922765377152
            },
            "correct_probability": 0.4812922765377152,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t73",
            "order_averaged_probabilities": {
              "A": 2.815999513433587e-09,
              "B": 0.9999799132347107,
              "C": 2.0070672462679795e-05
            },
            "correct_probability": 2.0070672462679795e-05,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t74",
            "order_averaged_probabilities": {
              "A": 2.93732531631008e-08,
              "B": 0.9998466670513153,
              "C": 0.00015329409325204324
            },
            "correct_probability": 0.00015329409325204324,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t75",
            "order_averaged_probabilities": {
              "A": 2.205921081216422e-09,
              "B": 0.9999861717224121,
              "C": 1.379456125505385e-05
            },
            "correct_probability": 1.379456125505385e-05,
            "correct_argmax": false,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          }
        ],
        "mean_correct_probability": 0.09302866036422852
      },
      "source": {
        "n": 16,
        "records": [
          {
            "prompt_id": "s4t06",
            "order_averaged_probabilities": {
              "A": 0.9998693764209747,
              "B": 0.0001305957842112626
            },
            "correct_probability": 0.9998693764209747,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t09",
            "order_averaged_probabilities": {
              "A": 0.999962568283081,
              "B": 3.742591449751309e-05
            },
            "correct_probability": 0.999962568283081,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t17",
            "order_averaged_probabilities": {
              "A": 0.984759122133255,
              "B": 0.015240870474372059
            },
            "correct_probability": 0.984759122133255,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t18",
            "order_averaged_probabilities": {
              "A": 0.9929651021957397,
              "B": 0.007034885816665337
            },
            "correct_probability": 0.9929651021957397,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t25",
            "order_averaged_probabilities": {
              "A": 0.5595534220337868,
              "B": 0.44044656548066996
            },
            "correct_probability": 0.5595534220337868,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t28",
            "order_averaged_probabilities": {
              "A": 0.9519704282283783,
              "B": 0.048029569356003776
            },
            "correct_probability": 0.9519704282283783,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t43",
            "order_averaged_probabilities": {
              "A": 0.5000000149011612,
              "B": 0.5000000149011612
            },
            "correct_probability": 0.5000000149011612,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t46",
            "order_averaged_probabilities": {
              "A": 0.9910061657428741,
              "B": 0.008993790510146482
            },
            "correct_probability": 0.9910061657428741,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t48",
            "order_averaged_probabilities": {
              "A": 0.9957098066806793,
              "B": 0.004290193474844273
            },
            "correct_probability": 0.9957098066806793,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t49",
            "order_averaged_probabilities": {
              "A": 0.8655287623405457,
              "B": 0.13447124997026094
            },
            "correct_probability": 0.8655287623405457,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t52",
            "order_averaged_probabilities": {
              "A": 0.5739619061350822,
              "B": 0.42603806310216896
            },
            "correct_probability": 0.5739619061350822,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t54",
            "order_averaged_probabilities": {
              "A": 0.5593674704432487,
              "B": 0.44063248112797737
            },
            "correct_probability": 0.5593674704432487,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t56",
            "order_averaged_probabilities": {
              "A": 0.5007491605938412,
              "B": 0.49925084986443835
            },
            "correct_probability": 0.5007491605938412,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t73",
            "order_averaged_probabilities": {
              "A": 0.9998691380023956,
              "B": 0.0001308473328549553
            },
            "correct_probability": 0.9998691380023956,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t74",
            "order_averaged_probabilities": {
              "A": 0.9998586475849152,
              "B": 0.00014131763327895897
            },
            "correct_probability": 0.9998586475849152,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t75",
            "order_averaged_probabilities": {
              "A": 0.9997901618480682,
              "B": 0.0002098132754326798
            },
            "correct_probability": 0.9997901618480682,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          }
        ],
        "mean_correct_probability": 0.8421825783480017
      }
    },
    "R4/hostility": {
      "EH_answer": {
        "n": 80,
        "mean": 0.1041576907140552
      },
      "answer_length": {
        "n": 80,
        "mean": 149.225
      },
      "answer_truncated": {
        "n": 80,
        "mean": 0.3125
      },
      "valid_digit_mass": [
        1.0,
        1.0,
        0.9999998807907104,
        1.0000001192092896,
        1.0,
        1.0000001192092896,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        0.9999998807907104,
        1.0,
        1.0000001192092896,
        0.9999999403953552,
        0.9999999403953552,
        0.9999999403953552,
        1.0,
        1.0,
        1.0000001192092896,
        1.0000001192092896,
        1.0000001192092896,
        1.0,
        1.0000001192092896,
        1.0,
        1.0,
        0.9999999403953552,
        1.0000001192092896,
        1.0,
        1.0,
        0.9999999403953552,
        1.0,
        1.0000001192092896,
        1.0,
        0.9999999403953552,
        0.9999998807907104,
        1.0,
        1.0,
        1.0,
        0.9999999403953552,
        1.0,
        1.0,
        1.0,
        0.9999999403953552,
        1.0,
        0.9999999403953552,
        1.0,
        0.9999998807907104,
        1.0000001192092896,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        0.9999999403953552,
        1.0,
        1.0,
        1.0,
        1.0,
        0.9999999403953552,
        0.9999999403953552,
        1.0,
        1.0,
        0.9999999403953552,
        0.9999998807907104,
        1.0,
        1.0,
        1.0,
        1.0,
        0.9999998807907104,
        0.9999999403953552,
        1.0,
        1.0,
        0.9999999403953552,
        1.0000001192092896,
        1.0,
        1.0000001192092896
      ],
      "baseline_mean": null,
      "baseline_sd": null,
      "structural": {
        "n": 16,
        "records": [
          {
            "prompt_id": "s4t06",
            "order_averaged_probabilities": {
              "A": 5.328416853560974e-07,
              "B": 0.9990310072898865,
              "C": 0.0009684312949502782
            },
            "correct_probability": 0.0009684312949502782,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t09",
            "order_averaged_probabilities": {
              "A": 8.76590732862715e-07,
              "B": 0.9979609549045563,
              "C": 0.0020381374083626724
            },
            "correct_probability": 0.0020381374083626724,
            "correct_argmax": false,
            "valid_mass": [
              0.9999999403953552,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t17",
            "order_averaged_probabilities": {
              "A": 3.200213151899334e-05,
              "B": 0.5737423375248909,
              "C": 0.42622560512972996
            },
            "correct_probability": 0.42622560512972996,
            "correct_argmax": false,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t18",
            "order_averaged_probabilities": {
              "A": 6.977998880697278e-05,
              "B": 0.9395864605903625,
              "C": 0.060343739634845406
            },
            "correct_probability": 0.060343739634845406,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t25",
            "order_averaged_probabilities": {
              "A": 6.386610724155861e-06,
              "B": 0.9909829199314117,
              "C": 0.009010668603878003
            },
            "correct_probability": 0.009010668603878003,
            "correct_argmax": false,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t28",
            "order_averaged_probabilities": {
              "A": 2.6552052745289906e-08,
              "B": 0.9993861019611359,
              "C": 0.0006139007855381351
            },
            "correct_probability": 0.0006139007855381351,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0000001192092896
            ]
          },
          {
            "prompt_id": "s4t43",
            "order_averaged_probabilities": {
              "A": 5.279930039869297e-07,
              "B": 0.99449223279953,
              "C": 0.005507233656317112
            },
            "correct_probability": 0.005507233656317112,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t46",
            "order_averaged_probabilities": {
              "A": 4.147375851416314e-07,
              "B": 0.9987618625164032,
              "C": 0.0012377618504615384
            },
            "correct_probability": 0.0012377618504615384,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t48",
            "order_averaged_probabilities": {
              "A": 0.00024345891470738124,
              "B": 0.9401816725730896,
              "C": 0.05957483218821835
            },
            "correct_probability": 0.05957483218821835,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              0.9999998807907104
            ]
          },
          {
            "prompt_id": "s4t49",
            "order_averaged_probabilities": {
              "A": 1.6388207375594988e-05,
              "B": 0.7804943025112152,
              "C": 0.2194893397972919
            },
            "correct_probability": 0.2194893397972919,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t52",
            "order_averaged_probabilities": {
              "A": 8.773980119790997e-07,
              "B": 0.998408854007721,
              "C": 0.0015902833697509777
            },
            "correct_probability": 0.0015902833697509777,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t54",
            "order_averaged_probabilities": {
              "A": 8.8708483703126e-05,
              "B": 0.660166934132576,
              "C": 0.33974437562574167
            },
            "correct_probability": 0.33974437562574167,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t56",
            "order_averaged_probabilities": {
              "A": 4.516425783344588e-05,
              "B": 0.5300229117274284,
              "C": 0.46993190584908007
            },
            "correct_probability": 0.46993190584908007,
            "correct_argmax": false,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t73",
            "order_averaged_probabilities": {
              "A": 2.7054275264504213e-08,
              "B": 0.9997670352458954,
              "C": 0.0002329566705157049
            },
            "correct_probability": 0.0002329566705157049,
            "correct_argmax": false,
            "valid_mass": [
              0.9999999403953552,
              1.0000001192092896
            ]
          },
          {
            "prompt_id": "s4t74",
            "order_averaged_probabilities": {
              "A": 2.0694057179665437e-08,
              "B": 0.9997828900814056,
              "C": 0.00021714186516419431
            },
            "correct_probability": 0.00021714186516419431,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0000001192092896
            ]
          },
          {
            "prompt_id": "s4t75",
            "order_averaged_probabilities": {
              "A": 3.601068746580255e-09,
              "B": 0.9999684691429138,
              "C": 3.1538181929136044e-05
            },
            "correct_probability": 3.1538181929136044e-05,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          }
        ],
        "mean_correct_probability": 0.09979736574448594
      },
      "source": {
        "n": 16,
        "records": [
          {
            "prompt_id": "s4t06",
            "order_averaged_probabilities": {
              "A": 0.6887696236371994,
              "B": 0.31123036148682104
            },
            "correct_probability": 0.6887696236371994,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t09",
            "order_averaged_probabilities": {
              "A": 0.8886498808860779,
              "B": 0.11135011823168028
            },
            "correct_probability": 0.8886498808860779,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t17",
            "order_averaged_probabilities": {
              "A": 0.9996830224990845,
              "B": 0.0003169920382788405
            },
            "correct_probability": 0.9996830224990845,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t18",
            "order_averaged_probabilities": {
              "A": 0.9997847378253937,
              "B": 0.00021528616050137117
            },
            "correct_probability": 0.9997847378253937,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t25",
            "order_averaged_probabilities": {
              "A": 0.7184562683105469,
              "B": 0.2815437884128187
            },
            "correct_probability": 0.7184562683105469,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t28",
            "order_averaged_probabilities": {
              "A": 0.6112194508314133,
              "B": 0.3887805356498575
            },
            "correct_probability": 0.6112194508314133,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t43",
            "order_averaged_probabilities": {
              "A": 0.7163017392158508,
              "B": 0.2836983259767294
            },
            "correct_probability": 0.7163017392158508,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0000001192092896
            ]
          },
          {
            "prompt_id": "s4t46",
            "order_averaged_probabilities": {
              "A": 0.9523250758647919,
              "B": 0.04767493053850558
            },
            "correct_probability": 0.9523250758647919,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t48",
            "order_averaged_probabilities": {
              "A": 0.9995445013046265,
              "B": 0.00045552562336067994
            },
            "correct_probability": 0.9995445013046265,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t49",
            "order_averaged_probabilities": {
              "A": 0.6887698024511337,
              "B": 0.31123020985967287
            },
            "correct_probability": 0.6887698024511337,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t52",
            "order_averaged_probabilities": {
              "A": 0.5000000149011612,
              "B": 0.5000000149011612
            },
            "correct_probability": 0.5000000149011612,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t54",
            "order_averaged_probabilities": {
              "A": 0.518554650247097,
              "B": 0.48144535161554813
            },
            "correct_probability": 0.518554650247097,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t56",
            "order_averaged_probabilities": {
              "A": 0.507009104359895,
              "B": 0.4929909005713853
            },
            "correct_probability": 0.507009104359895,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t73",
            "order_averaged_probabilities": {
              "A": 0.9884321093559265,
              "B": 0.01156790350069059
            },
            "correct_probability": 0.9884321093559265,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t74",
            "order_averaged_probabilities": {
              "A": 0.9909961521625519,
              "B": 0.009003827505694062
            },
            "correct_probability": 0.9909961521625519,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t75",
            "order_averaged_probabilities": {
              "A": 0.9811212718486786,
              "B": 0.018878722170484252
            },
            "correct_probability": 0.9811212718486786,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          }
        ],
        "mean_correct_probability": 0.7968510878563393
      }
    },
    "R4/technicality": {
      "EH_answer": {
        "n": 80,
        "mean": 0.06402839220245368
      },
      "answer_length": {
        "n": 80,
        "mean": 174.3875
      },
      "answer_truncated": {
        "n": 80,
        "mean": 0.4625
      },
      "valid_digit_mass": [
        1.0,
        1.0,
        0.9999999403953552,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0000001192092896,
        0.9999999403953552,
        1.0,
        1.0,
        1.0,
        0.9999997019767761,
        1.0,
        1.0,
        0.9999997615814209,
        1.0,
        1.0,
        0.9999999403953552,
        1.0,
        1.0,
        1.0000001192092896,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        0.9999998807907104,
        1.0,
        0.9999999403953552,
        1.0,
        0.9999999403953552,
        1.0,
        1.0000001192092896,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        0.9999991059303284,
        1.0,
        1.0,
        1.0,
        1.0000001192092896,
        1.0,
        0.9999999403953552,
        1.0,
        1.0,
        1.0,
        1.0,
        0.9999999403953552,
        1.0,
        1.0,
        1.0,
        1.0000001192092896,
        1.0,
        1.0,
        1.0,
        1.0000001192092896,
        1.0,
        1.0,
        0.9999999403953552,
        1.0000001192092896,
        1.0000001192092896,
        1.0,
        1.0,
        1.0,
        1.0000001192092896,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        0.9999999403953552,
        1.0,
        1.0,
        1.0,
        1.0
      ],
      "baseline_mean": null,
      "baseline_sd": null,
      "structural": {
        "n": 16,
        "records": [
          {
            "prompt_id": "s4t06",
            "order_averaged_probabilities": {
              "A": 4.5821946772217625e-06,
              "B": 0.9522418975830078,
              "C": 0.04775351267744554
            },
            "correct_probability": 0.04775351267744554,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t09",
            "order_averaged_probabilities": {
              "A": 4.1040314824325463e-07,
              "B": 0.9923830330371857,
              "C": 0.007616563292685896
            },
            "correct_probability": 0.007616563292685896,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t17",
            "order_averaged_probabilities": {
              "A": 0.00023564280411392247,
              "B": 0.9256078898906708,
              "C": 0.07415640325052664
            },
            "correct_probability": 0.07415640325052664,
            "correct_argmax": false,
            "valid_mass": [
              0.9999999403953552,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t18",
            "order_averaged_probabilities": {
              "A": 7.72979977359256e-06,
              "B": 0.9617873728275299,
              "C": 0.038204896030947566
            },
            "correct_probability": 0.038204896030947566,
            "correct_argmax": false,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t25",
            "order_averaged_probabilities": {
              "A": 1.955978101014777e-07,
              "B": 0.9972591698169708,
              "C": 0.0027406574081396684
            },
            "correct_probability": 0.0027406574081396684,
            "correct_argmax": false,
            "valid_mass": [
              0.9999999403953552,
              1.0000001192092896
            ]
          },
          {
            "prompt_id": "s4t28",
            "order_averaged_probabilities": {
              "A": 9.169090020577642e-06,
              "B": 0.9243821799755096,
              "C": 0.07560858223587275
            },
            "correct_probability": 0.07560858223587275,
            "correct_argmax": false,
            "valid_mass": [
              0.9999999403953552,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t43",
            "order_averaged_probabilities": {
              "A": 2.372030800042689e-06,
              "B": 0.995705783367157,
              "C": 0.004291794382424996
            },
            "correct_probability": 0.004291794382424996,
            "correct_argmax": false,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t46",
            "order_averaged_probabilities": {
              "A": 4.795862663278805e-05,
              "B": 0.8886087536811829,
              "C": 0.11134334981079519
            },
            "correct_probability": 0.11134334981079519,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t48",
            "order_averaged_probabilities": {
              "A": 3.9624737643073615e-05,
              "B": 0.7495246231555939,
              "C": 0.25043570701382123
            },
            "correct_probability": 0.25043570701382123,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t49",
            "order_averaged_probabilities": {
              "A": 0.0004339671678419421,
              "B": 0.5221059508621693,
              "C": 0.4774600798264146
            },
            "correct_probability": 0.4774600798264146,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t52",
            "order_averaged_probabilities": {
              "A": 1.685677964342186e-06,
              "B": 0.952301025390625,
              "C": 0.04769727289203729
            },
            "correct_probability": 0.04769727289203729,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t54",
            "order_averaged_probabilities": {
              "A": 1.2455608359329684e-05,
              "B": 0.9522848427295685,
              "C": 0.047702691412268905
            },
            "correct_probability": 0.047702691412268905,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t56",
            "order_averaged_probabilities": {
              "A": 0.00022094224792468253,
              "B": 0.6886252462863922,
              "C": 0.3111538653902244
            },
            "correct_probability": 0.3111538653902244,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t73",
            "order_averaged_probabilities": {
              "A": 9.299897002490454e-08,
              "B": 0.9996159076690674,
              "C": 0.0003839807577605825
            },
            "correct_probability": 0.0003839807577605825,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t74",
            "order_averaged_probabilities": {
              "A": 4.402009226578407e-08,
              "B": 0.9996411800384521,
              "C": 0.0003587797841646534
            },
            "correct_probability": 0.0003587797841646534,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t75",
            "order_averaged_probabilities": {
              "A": 9.816250909344681e-09,
              "B": 0.999912440776825,
              "C": 8.756882834859425e-05
            },
            "correct_probability": 8.756882834859425e-05,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          }
        ],
        "mean_correct_probability": 0.0935622315621174
      },
      "source": {
        "n": 16,
        "records": [
          {
            "prompt_id": "s4t06",
            "order_averaged_probabilities": {
              "A": 0.9997235834598541,
              "B": 0.000276390622247491
            },
            "correct_probability": 0.9997235834598541,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t09",
            "order_averaged_probabilities": {
              "A": 0.9999892711639404,
              "B": 1.0725275542577961e-05
            },
            "correct_probability": 0.9999892711639404,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t17",
            "order_averaged_probabilities": {
              "A": 0.6344707161188126,
              "B": 0.3655293023794153
            },
            "correct_probability": 0.6344707161188126,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t18",
            "order_averaged_probabilities": {
              "A": 0.9990366101264954,
              "B": 0.0009633771249806244
            },
            "correct_probability": 0.9990366101264954,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t25",
            "order_averaged_probabilities": {
              "A": 0.9402308464050293,
              "B": 0.059769138460978866
            },
            "correct_probability": 0.9402308464050293,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t28",
            "order_averaged_probabilities": {
              "A": 0.9617160856723785,
              "B": 0.038283926813164726
            },
            "correct_probability": 0.9617160856723785,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t43",
            "order_averaged_probabilities": {
              "A": 0.9403985142707825,
              "B": 0.059601466178874185
            },
            "correct_probability": 0.9403985142707825,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t46",
            "order_averaged_probabilities": {
              "A": 0.9087871015071869,
              "B": 0.09121284970133559
            },
            "correct_probability": 0.9087871015071869,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t48",
            "order_averaged_probabilities": {
              "A": 0.5007505911053158,
              "B": 0.49924939919515354
            },
            "correct_probability": 0.5007505911053158,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t49",
            "order_averaged_probabilities": {
              "A": 0.5114863011986017,
              "B": 0.48851371647629094
            },
            "correct_probability": 0.5114863011986017,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t52",
            "order_averaged_probabilities": {
              "A": 0.5740228816866875,
              "B": 0.4259770512832688
            },
            "correct_probability": 0.5740228816866875,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t54",
            "order_averaged_probabilities": {
              "A": 0.2844346882775426,
              "B": 0.7155653536319733
            },
            "correct_probability": 0.2844346882775426,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t56",
            "order_averaged_probabilities": {
              "A": 0.5042571821250021,
              "B": 0.4957428496563807
            },
            "correct_probability": 0.5042571821250021,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t73",
            "order_averaged_probabilities": {
              "A": 0.9990341365337372,
              "B": 0.0009658696508267894
            },
            "correct_probability": 0.9990341365337372,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t74",
            "order_averaged_probabilities": {
              "A": 0.9853331446647644,
              "B": 0.014666837797449261
            },
            "correct_probability": 0.9853331446647644,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t75",
            "order_averaged_probabilities": {
              "A": 0.9969344735145569,
              "B": 0.003065588796744123
            },
            "correct_probability": 0.9969344735145569,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0000001192092896
            ]
          }
        ],
        "mean_correct_probability": 0.796287882989418
      }
    },
    "R4/random": {
      "EH_answer": {
        "n": 80,
        "mean": 0.050615476223174485
      },
      "answer_length": {
        "n": 80,
        "mean": 148.5125
      },
      "answer_truncated": {
        "n": 80,
        "mean": 0.3125
      },
      "valid_digit_mass": [
        1.0,
        0.9999999403953552,
        0.9999999403953552,
        0.9999999403953552,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        0.9999991655349731,
        1.0,
        0.9999998807907104,
        1.0,
        1.0,
        0.9999988079071045,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        0.9999999403953552,
        0.9999999403953552,
        1.0,
        1.0,
        0.9999999403953552,
        0.9999999403953552,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0000001192092896,
        1.0,
        1.0,
        0.9999999403953552,
        1.0,
        0.9999999403953552,
        1.0,
        0.9999999403953552,
        1.0000001192092896,
        1.0,
        1.0,
        1.0,
        0.9999999403953552,
        1.0,
        1.0,
        0.9999998807907104,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        0.9999998807907104,
        0.9999999403953552,
        0.9999999403953552,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        0.9999998807907104,
        1.0,
        1.0000001192092896,
        1.0,
        1.0000001192092896,
        1.0,
        1.0,
        0.9999998807907104,
        0.9999998807907104,
        1.0000001192092896,
        1.0000001192092896,
        1.0,
        1.0000001192092896,
        1.0,
        0.9999999403953552,
        1.0000001192092896,
        0.9999999403953552,
        0.9999999403953552,
        1.0
      ],
      "baseline_mean": null,
      "baseline_sd": null,
      "structural": {
        "n": 16,
        "records": [
          {
            "prompt_id": "s4t06",
            "order_averaged_probabilities": {
              "A": 8.158856647504098e-06,
              "B": 0.9884856641292572,
              "C": 0.01150617631355999
            },
            "correct_probability": 0.01150617631355999,
            "correct_argmax": false,
            "valid_mass": [
              0.9999999403953552,
              1.0000001192092896
            ]
          },
          {
            "prompt_id": "s4t09",
            "order_averaged_probabilities": {
              "A": 9.700290229147646e-06,
              "B": 0.9522937536239624,
              "C": 0.04769650548223581
            },
            "correct_probability": 0.04769650548223581,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              0.9999998807907104
            ]
          },
          {
            "prompt_id": "s4t17",
            "order_averaged_probabilities": {
              "A": 0.000388824006449795,
              "B": 0.925565779209137,
              "C": 0.07404534861416323
            },
            "correct_probability": 0.07404534861416323,
            "correct_argmax": false,
            "valid_mass": [
              0.9999999403953552,
              1.0000001192092896
            ]
          },
          {
            "prompt_id": "s4t18",
            "order_averaged_probabilities": {
              "A": 0.00012947536689066064,
              "B": 0.50418591639027,
              "C": 0.4956845622800756
            },
            "correct_probability": 0.4956845622800756,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t25",
            "order_averaged_probabilities": {
              "A": 1.4494601844111318e-06,
              "B": 0.9994131028652191,
              "C": 0.0005854389998489751
            },
            "correct_probability": 0.0005854389998489751,
            "correct_argmax": false,
            "valid_mass": [
              0.9999999403953552,
              1.0000001192092896
            ]
          },
          {
            "prompt_id": "s4t28",
            "order_averaged_probabilities": {
              "A": 3.2463451438147217e-07,
              "B": 0.9992010593414307,
              "C": 0.0007986418495420367
            },
            "correct_probability": 0.0007986418495420367,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t43",
            "order_averaged_probabilities": {
              "A": 1.374728565742972e-05,
              "B": 0.9992338120937347,
              "C": 0.0007524337612494492
            },
            "correct_probability": 0.0007524337612494492,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t46",
            "order_averaged_probabilities": {
              "A": 0.000542039781264294,
              "B": 0.7186693698167801,
              "C": 0.2807885990455361
            },
            "correct_probability": 0.2807885990455361,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t48",
            "order_averaged_probabilities": {
              "A": 0.018340072986448352,
              "B": 0.5086258044466376,
              "C": 0.4730340752394113
            },
            "correct_probability": 0.4730340752394113,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t49",
            "order_averaged_probabilities": {
              "A": 0.0016788336285409322,
              "B": 0.7490813732147217,
              "C": 0.24923980590392603
            },
            "correct_probability": 0.24923980590392603,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t52",
            "order_averaged_probabilities": {
              "A": 6.0279848774684106e-05,
              "B": 0.9884459376335144,
              "C": 0.011493804072415514
            },
            "correct_probability": 0.011493804072415514,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t54",
            "order_averaged_probabilities": {
              "A": 0.0002925647662284092,
              "B": 0.7497744560241699,
              "C": 0.24993294831074309
            },
            "correct_probability": 0.24993294831074309,
            "correct_argmax": false,
            "valid_mass": [
              1.0000001192092896,
              1.0
            ]
          },
          {
            "prompt_id": "s4t56",
            "order_averaged_probabilities": {
              "A": 0.00017207730401475052,
              "B": 0.6886946260929108,
              "C": 0.31113325913338485
            },
            "correct_probability": 0.31113325913338485,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t73",
            "order_averaged_probabilities": {
              "A": 4.997635250081345e-09,
              "B": 0.999966561794281,
              "C": 3.3421408261347096e-05
            },
            "correct_probability": 3.3421408261347096e-05,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t74",
            "order_averaged_probabilities": {
              "A": 1.7504066841811383e-09,
              "B": 0.9999868869781494,
              "C": 1.311502160206146e-05
            },
            "correct_probability": 1.311502160206146e-05,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t75",
            "order_averaged_probabilities": {
              "A": 4.982505163661499e-10,
              "B": 0.9999877214431763,
              "C": 1.2295343822188443e-05
            },
            "correct_probability": 1.2295343822188443e-05,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          }
        ],
        "mean_correct_probability": 0.1379219019237361
      },
      "source": {
        "n": 16,
        "records": [
          {
            "prompt_id": "s4t06",
            "order_averaged_probabilities": {
              "A": 0.9929681420326233,
              "B": 0.007031847857568607
            },
            "correct_probability": 0.9929681420326233,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t09",
            "order_averaged_probabilities": {
              "A": 0.9403985142707825,
              "B": 0.05960146507660968
            },
            "correct_probability": 0.9403985142707825,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t17",
            "order_averaged_probabilities": {
              "A": 0.9993975460529327,
              "B": 0.0006024332760716788
            },
            "correct_probability": 0.9993975460529327,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t18",
            "order_averaged_probabilities": {
              "A": 0.9979542195796967,
              "B": 0.00204579152068618
            },
            "correct_probability": 0.9979542195796967,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t25",
            "order_averaged_probabilities": {
              "A": 0.839587926864624,
              "B": 0.1604121086811574
            },
            "correct_probability": 0.839587926864624,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t28",
            "order_averaged_probabilities": {
              "A": 0.908764511346817,
              "B": 0.09123545586589898
            },
            "correct_probability": 0.908764511346817,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t43",
            "order_averaged_probabilities": {
              "A": 0.47365109995007515,
              "B": 0.526348851621151
            },
            "correct_probability": 0.47365109995007515,
            "correct_argmax": false,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t46",
            "order_averaged_probabilities": {
              "A": 0.9259758293628693,
              "B": 0.07402413079387316
            },
            "correct_probability": 0.9259758293628693,
            "correct_argmax": true,
            "valid_mass": [
              0.9999999403953552,
              1.0
            ]
          },
          {
            "prompt_id": "s4t48",
            "order_averaged_probabilities": {
              "A": 0.7499988675117493,
              "B": 0.25000113016210435
            },
            "correct_probability": 0.7499988675117493,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t49",
            "order_averaged_probabilities": {
              "A": 0.8654500842094421,
              "B": 0.1345499342351104
            },
            "correct_probability": 0.8654500842094421,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t52",
            "order_averaged_probabilities": {
              "A": 0.9979566037654877,
              "B": 0.0020434197585927905
            },
            "correct_probability": 0.9979566037654877,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t54",
            "order_averaged_probabilities": {
              "A": 0.7624247968196869,
              "B": 0.2375752106308937
            },
            "correct_probability": 0.7624247968196869,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          },
          {
            "prompt_id": "s4t56",
            "order_averaged_probabilities": {
              "A": 0.41555897891521454,
              "B": 0.584441065788269
            },
            "correct_probability": 0.41555897891521454,
            "correct_argmax": false,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t73",
            "order_averaged_probabilities": {
              "A": 0.9995433688163757,
              "B": 0.00045665577852105343
            },
            "correct_probability": 0.9995433688163757,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t74",
            "order_averaged_probabilities": {
              "A": 0.9996451139450073,
              "B": 0.0003548914781852375
            },
            "correct_probability": 0.9996451139450073,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              1.0
            ]
          },
          {
            "prompt_id": "s4t75",
            "order_averaged_probabilities": {
              "A": 0.9993687570095062,
              "B": 0.0006312245095614344
            },
            "correct_probability": 0.9993687570095062,
            "correct_argmax": true,
            "valid_mass": [
              1.0,
              0.9999999403953552
            ]
          }
        ],
        "mean_correct_probability": 0.8667902725283056
      }
    }
  },
  "sensitivity": {
    "natural_closure": {
      "prompt_ids": [
        "s4t00",
        "s4t03",
        "s4t05",
        "s4t06",
        "s4t09",
        "s4t10",
        "s4t20",
        "s4t21",
        "s4t22",
        "s4t23",
        "s4t30",
        "s4t34",
        "s4t38",
        "s4t40",
        "s4t41",
        "s4t49",
        "s4t51",
        "s4t58",
        "s4t67",
        "s4t74",
        "s4t75",
        "s4t76"
      ],
      "n": 22,
      "estimands": {
        "R1:X": {
          "estimate": -0.5576830998405636,
          "ci_level": 0.95,
          "ci": [
            -0.8209796902251002,
            -0.3043633288699278
          ],
          "equivalence_ci_level": 0.9,
          "equivalence_ci": [
            -0.7773628767246573,
            -0.34340720984415185
          ],
          "n": 22,
          "supported": true,
          "negligible": false,
          "reversed": false,
          "negative": true,
          "positive": false,
          "status": "supported"
        },
        "R1:A_technicality": {
          "estimate": -0.5202490400345231,
          "ci_level": 0.95,
          "ci": [
            -0.8339212076671472,
            -0.20385925083297238
          ],
          "equivalence_ci_level": 0.9,
          "equivalence_ci": [
            -0.7850663921940052,
            -0.25837500736165286
          ],
          "n": 22,
          "supported": true,
          "negligible": false,
          "reversed": false,
          "negative": true,
          "positive": false,
          "status": "supported"
        },
        "R1:A_random": {
          "estimate": -0.31130614907809995,
          "ci_level": 0.95,
          "ci": [
            -0.5867758192840767,
            -0.0260322831936609
          ],
          "equivalence_ci_level": 0.9,
          "equivalence_ci": [
            -0.5423215986493399,
            -0.07218355762979727
          ],
          "n": 22,
          "supported": true,
          "negligible": false,
          "reversed": false,
          "negative": true,
          "positive": false,
          "status": "supported"
        },
        "R1-M:X": {
          "estimate": -0.19071167070720982,
          "ci_level": 0.95,
          "ci": [
            -0.2872416808263928,
            -0.09521124738763428
          ],
          "equivalence_ci_level": 0.9,
          "equivalence_ci": [
            -0.27105092438380946,
            -0.10950091744472377
          ],
          "n": 22,
          "supported": true,
          "negligible": false,
          "reversed": false,
          "negative": true,
          "positive": false,
          "status": "supported"
        },
        "R1-M:A_technicality": {
          "estimate": -0.1868456806114887,
          "ci_level": 0.95,
          "ci": [
            -0.31099163602082475,
            -0.06007710011329166
          ],
          "equivalence_ci_level": 0.9,
          "equivalence_ci": [
            -0.2896251505160508,
            -0.07986412395463714
          ],
          "n": 22,
          "supported": true,
          "negligible": false,
          "reversed": false,
          "negative": true,
          "positive": false,
          "status": "supported"
        },
        "R1-M:A_random": {
          "estimate": -0.1477774255813264,
          "ci_level": 0.95,
          "ci": [
            -0.24491245884114157,
            -0.05076494980325994
          ],
          "equivalence_ci_level": 0.9,
          "equivalence_ci": [
            -0.22739900576996452,
            -0.06622504394782701
          ],
          "n": 22,
          "supported": true,
          "negligible": false,
          "reversed": false,
          "negative": true,
          "positive": false,
          "status": "supported"
        },
        "R2:X": {
          "estimate": -0.052621071056557896,
          "ci_level": 0.95,
          "ci": [
            -0.12656386828194674,
            0.02300046866962994
          ],
          "equivalence_ci_level": 0.9,
          "equivalence_ci": [
            -0.115027815509332,
            0.011545532247786738
          ],
          "n": 22,
          "supported": false,
          "negligible": true,
          "reversed": false,
          "negative": false,
          "positive": false,
          "status": "negligible"
        },
        "R2:A_technicality": {
          "estimate": -0.1073804801112669,
          "ci_level": 0.95,
          "ci": [
            -0.20360302418663243,
            -0.003885462915500534
          ],
          "equivalence_ci_level": 0.9,
          "equivalence_ci": [
            -0.18926154219883098,
            -0.021040076947066753
          ],
          "n": 22,
          "supported": true,
          "negligible": false,
          "reversed": false,
          "negative": true,
          "positive": false,
          "status": "supported"
        },
        "R2:A_random": {
          "estimate": -0.06447407126777159,
          "ci_level": 0.95,
          "ci": [
            -0.1601171938482012,
            0.03536522099522982
          ],
          "equivalence_ci_level": 0.9,
          "equivalence_ci": [
            -0.14527207725043062,
            0.01935325276632138
          ],
          "n": 22,
          "supported": false,
          "negligible": true,
          "reversed": false,
          "negative": false,
          "positive": false,
          "status": "negligible"
        },
        "R3:X": {
          "estimate": -0.11908548582270097,
          "ci_level": 0.95,
          "ci": [
            -0.22766134519940232,
            -0.004834801716481953
          ],
          "equivalence_ci_level": 0.9,
          "equivalence_ci": [
            -0.2116162552523838,
            -0.02451131343947719
          ],
          "n": 22,
          "supported": true,
          "negligible": false,
          "reversed": false,
          "negative": true,
          "positive": false,
          "status": "supported"
        },
        "R3:A_technicality": {
          "estimate": -0.24063750793359,
          "ci_level": 0.95,
          "ci": [
            -0.3973993799868175,
            -0.07888928633867545
          ],
          "equivalence_ci_level": 0.9,
          "equivalence_ci": [
            -0.3736661236874544,
            -0.10497885576910014
          ],
          "n": 22,
          "supported": true,
          "negligible": false,
          "reversed": false,
          "negative": true,
          "positive": false,
          "status": "supported"
        },
        "R3:A_random": {
          "estimate": -0.14728188355543056,
          "ci_level": 0.95,
          "ci": [
            -0.3028915556025944,
            0.010175468404346745
          ],
          "equivalence_ci_level": 0.9,
          "equivalence_ci": [
            -0.2795382504832709,
            -0.014874294156908328
          ],
          "n": 22,
          "supported": false,
          "negligible": false,
          "reversed": false,
          "negative": false,
          "positive": false,
          "status": "inconclusive"
        },
        "R4:X": {
          "estimate": -0.07104576709748817,
          "ci_level": 0.95,
          "ci": [
            -0.24563092218026508,
            0.10947137371405438
          ],
          "equivalence_ci_level": 0.9,
          "equivalence_ci": [
            -0.2193519486340478,
            0.08104613494497766
          ],
          "n": 22,
          "supported": false,
          "negligible": false,
          "reversed": false,
          "negative": false,
          "positive": false,
          "status": "inconclusive"
        },
        "R4:A_technicality": {
          "estimate": -0.27288055287616725,
          "ci_level": 0.95,
          "ci": [
            -0.3781323479215571,
            -0.17091480899530392
          ],
          "equivalence_ci_level": 0.9,
          "equivalence_ci": [
            -0.36135995443049407,
            -0.18774025936005148
          ],
          "n": 22,
          "supported": true,
          "negligible": false,
          "reversed": false,
          "negative": true,
          "positive": false,
          "status": "supported"
        },
        "R4:A_random": {
          "estimate": -0.17170271143524707,
          "ci_level": 0.95,
          "ci": [
            -0.3014698396629623,
            -0.034073655184577306
          ],
          "equivalence_ci_level": 0.9,
          "equivalence_ci": [
            -0.27851769261428017,
            -0.05879023441941284
          ],
          "n": 22,
          "supported": true,
          "negligible": false,
          "reversed": false,
          "negative": true,
          "positive": false,
          "status": "supported"
        },
        "P3:technicality": {
          "estimate": -0.1332570278223231,
          "ci_level": 0.95,
          "ci": [
            -0.2372642104517668,
            -0.026445940111108648
          ],
          "equivalence_ci_level": 0.9,
          "equivalence_ci": [
            -0.22192473242511354,
            -0.04388518708581463
          ],
          "n": 22,
          "supported": true,
          "negligible": false,
          "reversed": false,
          "negative": true,
          "positive": false,
          "status": "supported"
        },
        "P3:random": {
          "estimate": -0.08280781228765897,
          "ci_level": 0.95,
          "ci": [
            -0.19803681926722924,
            0.031271069493941955
          ],
          "equivalence_ci_level": 0.9,
          "equivalence_ci": [
            -0.1803777871031548,
            0.014198625361385775
          ],
          "n": 22,
          "supported": false,
          "negligible": false,
          "reversed": false,
          "negative": false,
          "positive": false,
          "status": "inconclusive"
        },
        "S3:technicality": {
          "estimate": 0.0537918273221013,
          "ci_level": 0.95,
          "ci": [
            -0.06594105997026159,
            0.1774402787791188
          ],
          "equivalence_ci_level": 0.9,
          "equivalence_ci": [
            -0.04622564515410092,
            0.15701219202725283
          ],
          "n": 22,
          "supported": false,
          "negligible": false,
          "reversed": false,
          "negative": false,
          "positive": false,
          "status": "inconclusive"
        },
        "S3:random": {
          "estimate": -0.0004955420258958363,
          "ci_level": 0.95,
          "ci": [
            -0.12852182445619967,
            0.1274581607830036
          ],
          "equivalence_ci_level": 0.9,
          "equivalence_ci": [
            -0.10754123251512447,
            0.10774585457934516
          ],
          "n": 22,
          "supported": false,
          "negligible": true,
          "reversed": false,
          "negative": false,
          "positive": false,
          "status": "negligible"
        },
        "S4:technicality": {
          "estimate": -0.33340335942303445,
          "ci_level": 0.95,
          "ci": [
            -0.5781871010219601,
            -0.08838340584966052
          ],
          "equivalence_ci_level": 0.9,
          "equivalence_ci": [
            -0.537705185046218,
            -0.12916753179194446
          ],
          "n": 22,
          "supported": true,
          "negligible": false,
          "reversed": false,
          "negative": true,
          "positive": false,
          "status": "supported"
        },
        "S4:random": {
          "estimate": -0.16352872349677353,
          "ci_level": 0.95,
          "ci": [
            -0.36707382607010636,
            0.045559035342056374
          ],
          "equivalence_ci_level": 0.9,
          "equivalence_ci": [
            -0.33652804060771785,
            0.011968436930754054
          ],
          "n": 22,
          "supported": false,
          "negligible": false,
          "reversed": false,
          "negative": false,
          "positive": false,
          "status": "inconclusive"
        }
      },
      "tests": {
        "P1": {
          "R2:X": {
            "estimate": -0.052621071056557896,
            "ci_level": 0.9833,
            "ci": [
              -0.1433474062331423,
              0.037709342175404545
            ],
            "equivalence_ci_level": 0.9,
            "equivalence_ci": [
              -0.115027815509332,
              0.011545532247786738
            ],
            "n": 22,
            "supported": false,
            "negligible": true,
            "reversed": false,
            "negative": false,
            "positive": false,
            "status": "negligible"
          },
          "R2:A_technicality": {
            "estimate": -0.1073804801112669,
            "ci_level": 0.9833,
            "ci": [
              -0.22155822703088787,
              0.017399395630265678
            ],
            "equivalence_ci_level": 0.9,
            "equivalence_ci": [
              -0.18926154219883098,
              -0.021040076947066753
            ],
            "n": 22,
            "supported": false,
            "negligible": false,
            "reversed": false,
            "negative": false,
            "positive": false,
            "status": "inconclusive"
          },
          "R2:A_random": {
            "estimate": -0.06447407126777159,
            "ci_level": 0.9833,
            "ci": [
              -0.17884870479123538,
              0.05731354215952646
            ],
            "equivalence_ci_level": 0.9,
            "equivalence_ci": [
              -0.14527207725043062,
              0.01935325276632138
            ],
            "n": 22,
            "supported": false,
            "negligible": true,
            "reversed": false,
            "negative": false,
            "positive": false,
            "status": "negligible"
          }
        },
        "P2": {
          "R3:X": {
            "estimate": -0.11908548582270097,
            "ci_level": 0.9833,
            "ci": [
              -0.2502767203747277,
              0.02212019529103352
            ],
            "equivalence_ci_level": 0.9,
            "equivalence_ci": [
              -0.2116162552523838,
              -0.02451131343947719
            ],
            "n": 22,
            "supported": false,
            "negligible": false,
            "reversed": false,
            "negative": false,
            "positive": false,
            "status": "inconclusive"
          },
          "R3:A_technicality": {
            "estimate": -0.24063750793359,
            "ci_level": 0.9833,
            "ci": [
              -0.4305320925212463,
              -0.04405177415647703
            ],
            "equivalence_ci_level": 0.9,
            "equivalence_ci": [
              -0.3736661236874544,
              -0.10497885576910014
            ],
            "n": 22,
            "supported": true,
            "negligible": false,
            "reversed": false,
            "negative": true,
            "positive": false,
            "status": "supported"
          },
          "R3:A_random": {
            "estimate": -0.14728188355543056,
            "ci_level": 0.9833,
            "ci": [
              -0.33473374424142405,
              0.04183905990247375
            ],
            "equivalence_ci_level": 0.9,
            "equivalence_ci": [
              -0.2795382504832709,
              -0.014874294156908328
            ],
            "n": 22,
            "supported": false,
            "negligible": false,
            "reversed": false,
            "negative": false,
            "positive": false,
            "status": "inconclusive"
          }
        },
        "S1": {
          "R1:X": {
            "estimate": -0.5576830998405636,
            "ci_level": 0.95,
            "ci": [
              -0.8209796902251002,
              -0.3043633288699278
            ],
            "equivalence_ci_level": 0.9,
            "equivalence_ci": [
              -0.7773628767246573,
              -0.34340720984415185
            ],
            "n": 22,
            "supported": true,
            "negligible": false,
            "reversed": false,
            "negative": true,
            "positive": false,
            "status": "supported"
          },
          "R1:A_technicality": {
            "estimate": -0.5202490400345231,
            "ci_level": 0.95,
            "ci": [
              -0.8339212076671472,
              -0.20385925083297238
            ],
            "equivalence_ci_level": 0.9,
            "equivalence_ci": [
              -0.7850663921940052,
              -0.25837500736165286
            ],
            "n": 22,
            "supported": true,
            "negligible": false,
            "reversed": false,
            "negative": true,
            "positive": false,
            "status": "supported"
          },
          "R1:A_random": {
            "estimate": -0.31130614907809995,
            "ci_level": 0.95,
            "ci": [
              -0.5867758192840767,
              -0.0260322831936609
            ],
            "equivalence_ci_level": 0.9,
            "equivalence_ci": [
              -0.5423215986493399,
              -0.07218355762979727
            ],
            "n": 22,
            "supported": true,
            "negligible": false,
            "reversed": false,
            "negative": true,
            "positive": false,
            "status": "supported"
          }
        },
        "S2": {
          "R1-M:X": {
            "estimate": -0.19071167070720982,
            "ci_level": 0.95,
            "ci": [
              -0.2872416808263928,
              -0.09521124738763428
            ],
            "equivalence_ci_level": 0.9,
            "equivalence_ci": [
              -0.27105092438380946,
              -0.10950091744472377
            ],
            "n": 22,
            "supported": true,
            "negligible": false,
            "reversed": false,
            "negative": true,
            "positive": false,
            "status": "supported"
          },
          "R1-M:A_technicality": {
            "estimate": -0.1868456806114887,
            "ci_level": 0.95,
            "ci": [
              -0.31099163602082475,
              -0.06007710011329166
            ],
            "equivalence_ci_level": 0.9,
            "equivalence_ci": [
              -0.2896251505160508,
              -0.07986412395463714
            ],
            "n": 22,
            "supported": true,
            "negligible": false,
            "reversed": false,
            "negative": true,
            "positive": false,
            "status": "supported"
          },
          "R1-M:A_random": {
            "estimate": -0.1477774255813264,
            "ci_level": 0.95,
            "ci": [
              -0.24491245884114157,
              -0.05076494980325994
            ],
            "equivalence_ci_level": 0.9,
            "equivalence_ci": [
              -0.22739900576996452,
              -0.06622504394782701
            ],
            "n": 22,
            "supported": true,
            "negligible": false,
            "reversed": false,
            "negative": true,
            "positive": false,
            "status": "supported"
          }
        },
        "S5": {
          "R4:X": {
            "estimate": -0.07104576709748817,
            "ci_level": 0.95,
            "ci": [
              -0.24563092218026508,
              0.10947137371405438
            ],
            "equivalence_ci_level": 0.9,
            "equivalence_ci": [
              -0.2193519486340478,
              0.08104613494497766
            ],
            "n": 22,
            "supported": false,
            "negligible": false,
            "reversed": false,
            "negative": false,
            "positive": false,
            "status": "inconclusive"
          },
          "R4:A_technicality": {
            "estimate": -0.27288055287616725,
            "ci_level": 0.95,
            "ci": [
              -0.3781323479215571,
              -0.17091480899530392
            ],
            "equivalence_ci_level": 0.9,
            "equivalence_ci": [
              -0.36135995443049407,
              -0.18774025936005148
            ],
            "n": 22,
            "supported": false,
            "negligible": false,
            "reversed": false,
            "negative": true,
            "positive": false,
            "status": "inconclusive"
          },
          "R4:A_random": {
            "estimate": -0.17170271143524707,
            "ci_level": 0.95,
            "ci": [
              -0.3014698396629623,
              -0.034073655184577306
            ],
            "equivalence_ci_level": 0.9,
            "equivalence_ci": [
              -0.27851769261428017,
              -0.05879023441941284
            ],
            "n": 22,
            "supported": false,
            "negligible": false,
            "reversed": false,
            "negative": true,
            "positive": false,
            "status": "inconclusive"
          }
        },
        "P3": {
          "P3:technicality": {
            "estimate": -0.1332570278223231,
            "ci_level": 0.9833,
            "ci": [
              -0.2614131776580937,
              -0.0034016304032537478
            ],
            "equivalence_ci_level": 0.9,
            "equivalence_ci": [
              -0.22192473242511354,
              -0.04388518708581463
            ],
            "n": 22,
            "supported": true,
            "negligible": false,
            "reversed": false,
            "negative": true,
            "positive": false,
            "status": "supported"
          },
          "P3:random": {
            "estimate": -0.08280781228765897,
            "ci_level": 0.9833,
            "ci": [
              -0.22263331169610356,
              0.05853459059022357
            ],
            "equivalence_ci_level": 0.9,
            "equivalence_ci": [
              -0.1803777871031548,
              0.014198625361385775
            ],
            "n": 22,
            "supported": false,
            "negligible": false,
            "reversed": false,
            "negative": false,
            "positive": false,
            "status": "inconclusive"
          }
        },
        "S3": {
          "S3:technicality": {
            "estimate": 0.0537918273221013,
            "ci_level": 0.95,
            "ci": [
              -0.06594105997026159,
              0.1774402787791188
            ],
            "equivalence_ci_level": 0.9,
            "equivalence_ci": [
              -0.04622564515410092,
              0.15701219202725283
            ],
            "n": 22,
            "supported": false,
            "negligible": false,
            "reversed": false,
            "negative": false,
            "positive": false,
            "status": "inconclusive"
          },
          "S3:random": {
            "estimate": -0.0004955420258958363,
            "ci_level": 0.95,
            "ci": [
              -0.12852182445619967,
              0.1274581607830036
            ],
            "equivalence_ci_level": 0.9,
            "equivalence_ci": [
              -0.10754123251512447,
              0.10774585457934516
            ],
            "n": 22,
            "supported": false,
            "negligible": true,
            "reversed": false,
            "negative": false,
            "positive": false,
            "status": "negligible"
          }
        },
        "S4": {
          "S4:technicality": {
            "estimate": -0.33340335942303445,
            "ci_level": 0.95,
            "ci": [
              -0.5781871010219601,
              -0.08838340584966052
            ],
            "equivalence_ci_level": 0.9,
            "equivalence_ci": [
              -0.537705185046218,
              -0.12916753179194446
            ],
            "n": 22,
            "supported": true,
            "negligible": false,
            "reversed": false,
            "negative": true,
            "positive": false,
            "status": "supported"
          },
          "S4:random": {
            "estimate": -0.16352872349677353,
            "ci_level": 0.95,
            "ci": [
              -0.36707382607010636,
              0.045559035342056374
            ],
            "equivalence_ci_level": 0.9,
            "equivalence_ci": [
              -0.33652804060771785,
              0.011968436930754054
            ],
            "n": 22,
            "supported": false,
            "negligible": false,
            "reversed": false,
            "negative": false,
            "positive": false,
            "status": "inconclusive"
          }
        }
      },
      "hypotheses": {
        "P1": {
          "supported": false,
          "negligible": false,
          "reversed": false,
          "status": "inconclusive"
        },
        "P2": {
          "supported": false,
          "negligible": false,
          "reversed": false,
          "status": "inconclusive"
        },
        "S1": {
          "supported": true,
          "negligible": false,
          "reversed": false,
          "status": "supported"
        },
        "S2": {
          "supported": true,
          "negligible": false,
          "reversed": false,
          "status": "supported"
        },
        "S5": {
          "supported": false,
          "negligible": false,
          "reversed": false,
          "status": "inconclusive"
        },
        "P3": {
          "supported": false,
          "negligible": false,
          "reversed": false,
          "status": "inconclusive"
        },
        "S3": {
          "supported": false,
          "negligible": false,
          "reversed": false,
          "status": "inconclusive"
        },
        "S4": {
          "supported": false,
          "negligible": false,
          "reversed": false,
          "status": "inconclusive"
        }
      },
      "reading": "Placement interpretation inconclusive; comparative claims require direct P3 or S3 evidence.",
      "missing_policy": "Required missing cells make affected components not estimable; no outcome-based exclusions.",
      "bootstrap_resamples": 10000,
      "label": "Descriptive sensitivity; complete prompt clusters retained, not confirmatory."
    },
    "E5": {
      "prompt_ids": [
        "s4t00",
        "s4t03",
        "s4t05",
        "s4t14",
        "s4t18",
        "s4t20",
        "s4t21",
        "s4t23",
        "s4t25",
        "s4t29",
        "s4t31",
        "s4t32",
        "s4t34",
        "s4t37",
        "s4t41",
        "s4t44",
        "s4t52",
        "s4t58",
        "s4t60",
        "s4t61",
        "s4t62",
        "s4t63",
        "s4t64",
        "s4t66",
        "s4t67",
        "s4t68",
        "s4t69",
        "s4t70",
        "s4t71",
        "s4t72",
        "s4t73",
        "s4t74",
        "s4t75",
        "s4t76",
        "s4t77",
        "s4t78",
        "s4t79"
      ],
      "n": 37,
      "estimands": {
        "R1:X": {
          "estimate": -0.627666849251759,
          "ci_level": 0.95,
          "ci": [
            -0.8406842391682512,
            -0.4238711979869501
          ],
          "equivalence_ci_level": 0.9,
          "equivalence_ci": [
            -0.8067398055944809,
            -0.4547588165291981
          ],
          "n": 37,
          "supported": true,
          "negligible": false,
          "reversed": false,
          "negative": true,
          "positive": false,
          "status": "supported"
        },
        "R1:A_technicality": {
          "estimate": -0.6550062209038983,
          "ci_level": 0.95,
          "ci": [
            -0.8913807646021841,
            -0.4313717176858862
          ],
          "equivalence_ci_level": 0.9,
          "equivalence_ci": [
            -0.8518657704242185,
            -0.4660399299272242
          ],
          "n": 37,
          "supported": true,
          "negligible": false,
          "reversed": false,
          "negative": true,
          "positive": false,
          "status": "supported"
        },
        "R1:A_random": {
          "estimate": -0.3562163270949595,
          "ci_level": 0.95,
          "ci": [
            -0.5645139845664447,
            -0.1592799929951134
          ],
          "equivalence_ci_level": 0.9,
          "equivalence_ci": [
            -0.5299453610745606,
            -0.18901238205174223
          ],
          "n": 37,
          "supported": true,
          "negligible": false,
          "reversed": false,
          "negative": true,
          "positive": false,
          "status": "supported"
        },
        "R1-M:X": {
          "estimate": -0.2988856662982909,
          "ci_level": 0.95,
          "ci": [
            -0.39569652782992176,
            -0.2065606266649002
          ],
          "equivalence_ci_level": 0.9,
          "equivalence_ci": [
            -0.3796431727079845,
            -0.21930809488394537
          ],
          "n": 37,
          "supported": true,
          "negligible": false,
          "reversed": false,
          "negative": true,
          "positive": false,
          "status": "supported"
        },
        "R1-M:A_technicality": {
          "estimate": -0.29061215501216847,
          "ci_level": 0.95,
          "ci": [
            -0.39499865668999545,
            -0.18855361161940093
          ],
          "equivalence_ci_level": 0.9,
          "equivalence_ci": [
            -0.3773264100257307,
            -0.2032562740242863
          ],
          "n": 37,
          "supported": true,
          "negligible": false,
          "reversed": false,
          "negative": true,
          "positive": false,
          "status": "supported"
        },
        "R1-M:A_random": {
          "estimate": -0.19581140177364267,
          "ci_level": 0.95,
          "ci": [
            -0.2815728409492532,
            -0.11027927034679633
          ],
          "equivalence_ci_level": 0.9,
          "equivalence_ci": [
            -0.267551908144919,
            -0.12365703603928249
          ],
          "n": 37,
          "supported": true,
          "negligible": false,
          "reversed": false,
          "negative": true,
          "positive": false,
          "status": "supported"
        },
        "R2:X": {
          "estimate": -0.2319865632199371,
          "ci_level": 0.95,
          "ci": [
            -0.3093878714238073,
            -0.15782134771142386
          ],
          "equivalence_ci_level": 0.9,
          "equivalence_ci": [
            -0.2968829648945629,
            -0.16857164080723644
          ],
          "n": 37,
          "supported": true,
          "negligible": false,
          "reversed": false,
          "negative": true,
          "positive": false,
          "status": "supported"
        },
        "R2:A_technicality": {
          "estimate": -0.22240787425444755,
          "ci_level": 0.95,
          "ci": [
            -0.3078598788928846,
            -0.14590840028834898
          ],
          "equivalence_ci_level": 0.9,
          "equivalence_ci": [
            -0.29131226647920977,
            -0.15709111207337068
          ],
          "n": 37,
          "supported": true,
          "negligible": false,
          "reversed": false,
          "negative": true,
          "positive": false,
          "status": "supported"
        },
        "R2:A_random": {
          "estimate": -0.1626807627846906,
          "ci_level": 0.95,
          "ci": [
            -0.24120112879709596,
            -0.08485829327866656
          ],
          "equivalence_ci_level": 0.9,
          "equivalence_ci": [
            -0.22843826749276003,
            -0.09717616163399286
          ],
          "n": 37,
          "supported": true,
          "negligible": false,
          "reversed": false,
          "negative": true,
          "positive": false,
          "status": "supported"
        },
        "R3:X": {
          "estimate": -0.19471165289794098,
          "ci_level": 0.95,
          "ci": [
            -0.2857281707431898,
            -0.09970489274775317
          ],
          "equivalence_ci_level": 0.9,
          "equivalence_ci": [
            -0.26982178155216513,
            -0.1171758670866614
          ],
          "n": 37,
          "supported": true,
          "negligible": false,
          "reversed": false,
          "negative": true,
          "positive": false,
          "status": "supported"
        },
        "R3:A_technicality": {
          "estimate": -0.2237906156485793,
          "ci_level": 0.95,
          "ci": [
            -0.3249610109278846,
            -0.11782870871540126
          ],
          "equivalence_ci_level": 0.9,
          "equivalence_ci": [
            -0.3091232146200816,
            -0.13363739391510054
          ],
          "n": 37,
          "supported": true,
          "negligible": false,
          "reversed": false,
          "negative": true,
          "positive": false,
          "status": "supported"
        },
        "R3:A_random": {
          "estimate": -0.17580561369446293,
          "ci_level": 0.95,
          "ci": [
            -0.2610503154381959,
            -0.0928357264849657
          ],
          "equivalence_ci_level": 0.9,
          "equivalence_ci": [
            -0.2470212458643546,
            -0.10600240485370188
          ],
          "n": 37,
          "supported": true,
          "negligible": false,
          "reversed": false,
          "negative": true,
          "positive": false,
          "status": "supported"
        },
        "R4:X": {
          "estimate": -0.1286854967855734,
          "ci_level": 0.95,
          "ci": [
            -0.2366536107384637,
            -0.012241259881451364
          ],
          "equivalence_ci_level": 0.9,
          "equivalence_ci": [
            -0.21998800677500135,
            -0.029649092433849316
          ],
          "n": 37,
          "supported": true,
          "negligible": false,
          "reversed": false,
          "negative": true,
          "positive": false,
          "status": "supported"
        },
        "R4:A_technicality": {
          "estimate": -0.23315496523360996,
          "ci_level": 0.95,
          "ci": [
            -0.3424460933165866,
            -0.12459288254533181
          ],
          "equivalence_ci_level": 0.9,
          "equivalence_ci": [
            -0.32517012987901517,
            -0.14244502983403898
          ],
          "n": 37,
          "supported": true,
          "negligible": false,
          "reversed": false,
          "negative": true,
          "positive": false,
          "status": "supported"
        },
        "R4:A_random": {
          "estimate": -0.15595712815152257,
          "ci_level": 0.95,
          "ci": [
            -0.26328011987023053,
            -0.04725518794643989
          ],
          "equivalence_ci_level": 0.9,
          "equivalence_ci": [
            -0.24514778867641332,
            -0.06391371509020827
          ],
          "n": 37,
          "supported": true,
          "negligible": false,
          "reversed": false,
          "negative": true,
          "positive": false,
          "status": "supported"
        },
        "P3:technicality": {
          "estimate": -0.001382741394131751,
          "ci_level": 0.95,
          "ci": [
            -0.09132745155454801,
            0.09175829583032136
          ],
          "equivalence_ci_level": 0.9,
          "equivalence_ci": [
            -0.07817768533461882,
            0.07645430857478498
          ],
          "n": 37,
          "supported": false,
          "negligible": true,
          "reversed": false,
          "negative": false,
          "positive": false,
          "status": "negligible"
        },
        "P3:random": {
          "estimate": -0.013124850909772334,
          "ci_level": 0.95,
          "ci": [
            -0.10330878513363446,
            0.07678697088438989
          ],
          "equivalence_ci_level": 0.9,
          "equivalence_ci": [
            -0.08888298060631022,
            0.062085340235061265
          ],
          "n": 37,
          "supported": false,
          "negligible": true,
          "reversed": false,
          "negative": false,
          "positive": false,
          "status": "negligible"
        },
        "S3:technicality": {
          "estimate": -0.06682153936358917,
          "ci_level": 0.95,
          "ci": [
            -0.1765677831765151,
            0.04026811594591089
          ],
          "equivalence_ci_level": 0.9,
          "equivalence_ci": [
            -0.15938284166026317,
            0.024673331633206622
          ],
          "n": 37,
          "supported": false,
          "negligible": false,
          "reversed": false,
          "negative": false,
          "positive": false,
          "status": "inconclusive"
        },
        "S3:random": {
          "estimate": -0.020005788079179725,
          "ci_level": 0.95,
          "ci": [
            -0.11316569627819902,
            0.07338653581230188
          ],
          "equivalence_ci_level": 0.9,
          "equivalence_ci": [
            -0.09837038586289236,
            0.05860576732543951
          ],
          "n": 37,
          "supported": false,
          "negligible": true,
          "reversed": false,
          "negative": false,
          "positive": false,
          "status": "negligible"
        },
        "S4:technicality": {
          "estimate": -0.3643940658917298,
          "ci_level": 0.95,
          "ci": [
            -0.5471565151589382,
            -0.1922089317490848
          ],
          "equivalence_ci_level": 0.9,
          "equivalence_ci": [
            -0.5178692893700763,
            -0.21744007082197137
          ],
          "n": 37,
          "supported": true,
          "negligible": false,
          "reversed": false,
          "negative": true,
          "positive": false,
          "status": "supported"
        },
        "S4:random": {
          "estimate": -0.1604049253213168,
          "ci_level": 0.95,
          "ci": [
            -0.3212342250560854,
            0.002005707381437805
          ],
          "equivalence_ci_level": 0.9,
          "equivalence_ci": [
            -0.29580200436748366,
            -0.025363075829185348
          ],
          "n": 37,
          "supported": false,
          "negligible": false,
          "reversed": false,
          "negative": false,
          "positive": false,
          "status": "inconclusive"
        }
      },
      "tests": {
        "P1": {
          "R2:X": {
            "estimate": -0.2319865632199371,
            "ci_level": 0.9833,
            "ci": [
              -0.32742652898959673,
              -0.14105104793951495
            ],
            "equivalence_ci_level": 0.9,
            "equivalence_ci": [
              -0.2968829648945629,
              -0.16857164080723644
            ],
            "n": 37,
            "supported": true,
            "negligible": false,
            "reversed": false,
            "negative": true,
            "positive": false,
            "status": "supported"
          },
          "R2:A_technicality": {
            "estimate": -0.22240787425444755,
            "ci_level": 0.9833,
            "ci": [
              -0.3264281040285722,
              -0.13129178468323338
            ],
            "equivalence_ci_level": 0.9,
            "equivalence_ci": [
              -0.29131226647920977,
              -0.15709111207337068
            ],
            "n": 37,
            "supported": true,
            "negligible": false,
            "reversed": false,
            "negative": true,
            "positive": false,
            "status": "supported"
          },
          "R2:A_random": {
            "estimate": -0.1626807627846906,
            "ci_level": 0.9833,
            "ci": [
              -0.25758733836137954,
              -0.0689454034142467
            ],
            "equivalence_ci_level": 0.9,
            "equivalence_ci": [
              -0.22843826749276003,
              -0.09717616163399286
            ],
            "n": 37,
            "supported": true,
            "negligible": false,
            "reversed": false,
            "negative": true,
            "positive": false,
            "status": "supported"
          }
        },
        "P2": {
          "R3:X": {
            "estimate": -0.19471165289794098,
            "ci_level": 0.9833,
            "ci": [
              -0.30762505337890567,
              -0.08071569008843095
            ],
            "equivalence_ci_level": 0.9,
            "equivalence_ci": [
              -0.26982178155216513,
              -0.1171758670866614
            ],
            "n": 37,
            "supported": true,
            "negligible": false,
            "reversed": false,
            "negative": true,
            "positive": false,
            "status": "supported"
          },
          "R3:A_technicality": {
            "estimate": -0.2237906156485793,
            "ci_level": 0.9833,
            "ci": [
              -0.3467857877314701,
              -0.09233753033632283
            ],
            "equivalence_ci_level": 0.9,
            "equivalence_ci": [
              -0.3091232146200816,
              -0.13363739391510054
            ],
            "n": 37,
            "supported": true,
            "negligible": false,
            "reversed": false,
            "negative": true,
            "positive": false,
            "status": "supported"
          },
          "R3:A_random": {
            "estimate": -0.17580561369446293,
            "ci_level": 0.9833,
            "ci": [
              -0.27969789676665374,
              -0.0767495890282504
            ],
            "equivalence_ci_level": 0.9,
            "equivalence_ci": [
              -0.2470212458643546,
              -0.10600240485370188
            ],
            "n": 37,
            "supported": true,
            "negligible": false,
            "reversed": false,
            "negative": true,
            "positive": false,
            "status": "supported"
          }
        },
        "S1": {
          "R1:X": {
            "estimate": -0.627666849251759,
            "ci_level": 0.95,
            "ci": [
              -0.8406842391682512,
              -0.4238711979869501
            ],
            "equivalence_ci_level": 0.9,
            "equivalence_ci": [
              -0.8067398055944809,
              -0.4547588165291981
            ],
            "n": 37,
            "supported": true,
            "negligible": false,
            "reversed": false,
            "negative": true,
            "positive": false,
            "status": "supported"
          },
          "R1:A_technicality": {
            "estimate": -0.6550062209038983,
            "ci_level": 0.95,
            "ci": [
              -0.8913807646021841,
              -0.4313717176858862
            ],
            "equivalence_ci_level": 0.9,
            "equivalence_ci": [
              -0.8518657704242185,
              -0.4660399299272242
            ],
            "n": 37,
            "supported": true,
            "negligible": false,
            "reversed": false,
            "negative": true,
            "positive": false,
            "status": "supported"
          },
          "R1:A_random": {
            "estimate": -0.3562163270949595,
            "ci_level": 0.95,
            "ci": [
              -0.5645139845664447,
              -0.1592799929951134
            ],
            "equivalence_ci_level": 0.9,
            "equivalence_ci": [
              -0.5299453610745606,
              -0.18901238205174223
            ],
            "n": 37,
            "supported": true,
            "negligible": false,
            "reversed": false,
            "negative": true,
            "positive": false,
            "status": "supported"
          }
        },
        "S2": {
          "R1-M:X": {
            "estimate": -0.2988856662982909,
            "ci_level": 0.95,
            "ci": [
              -0.39569652782992176,
              -0.2065606266649002
            ],
            "equivalence_ci_level": 0.9,
            "equivalence_ci": [
              -0.3796431727079845,
              -0.21930809488394537
            ],
            "n": 37,
            "supported": true,
            "negligible": false,
            "reversed": false,
            "negative": true,
            "positive": false,
            "status": "supported"
          },
          "R1-M:A_technicality": {
            "estimate": -0.29061215501216847,
            "ci_level": 0.95,
            "ci": [
              -0.39499865668999545,
              -0.18855361161940093
            ],
            "equivalence_ci_level": 0.9,
            "equivalence_ci": [
              -0.3773264100257307,
              -0.2032562740242863
            ],
            "n": 37,
            "supported": true,
            "negligible": false,
            "reversed": false,
            "negative": true,
            "positive": false,
            "status": "supported"
          },
          "R1-M:A_random": {
            "estimate": -0.19581140177364267,
            "ci_level": 0.95,
            "ci": [
              -0.2815728409492532,
              -0.11027927034679633
            ],
            "equivalence_ci_level": 0.9,
            "equivalence_ci": [
              -0.267551908144919,
              -0.12365703603928249
            ],
            "n": 37,
            "supported": true,
            "negligible": false,
            "reversed": false,
            "negative": true,
            "positive": false,
            "status": "supported"
          }
        },
        "S5": {
          "R4:X": {
            "estimate": -0.1286854967855734,
            "ci_level": 0.95,
            "ci": [
              -0.2366536107384637,
              -0.012241259881451364
            ],
            "equivalence_ci_level": 0.9,
            "equivalence_ci": [
              -0.21998800677500135,
              -0.029649092433849316
            ],
            "n": 37,
            "supported": false,
            "negligible": false,
            "reversed": false,
            "negative": true,
            "positive": false,
            "status": "inconclusive"
          },
          "R4:A_technicality": {
            "estimate": -0.23315496523360996,
            "ci_level": 0.95,
            "ci": [
              -0.3424460933165866,
              -0.12459288254533181
            ],
            "equivalence_ci_level": 0.9,
            "equivalence_ci": [
              -0.32517012987901517,
              -0.14244502983403898
            ],
            "n": 37,
            "supported": false,
            "negligible": false,
            "reversed": false,
            "negative": true,
            "positive": false,
            "status": "inconclusive"
          },
          "R4:A_random": {
            "estimate": -0.15595712815152257,
            "ci_level": 0.95,
            "ci": [
              -0.26328011987023053,
              -0.04725518794643989
            ],
            "equivalence_ci_level": 0.9,
            "equivalence_ci": [
              -0.24514778867641332,
              -0.06391371509020827
            ],
            "n": 37,
            "supported": false,
            "negligible": false,
            "reversed": false,
            "negative": true,
            "positive": false,
            "status": "inconclusive"
          }
        },
        "P3": {
          "P3:technicality": {
            "estimate": -0.001382741394131751,
            "ci_level": 0.9833,
            "ci": [
              -0.11074119593383869,
              0.11309635448285567
            ],
            "equivalence_ci_level": 0.9,
            "equivalence_ci": [
              -0.07817768533461882,
              0.07645430857478498
            ],
            "n": 37,
            "supported": false,
            "negligible": true,
            "reversed": false,
            "negative": false,
            "positive": false,
            "status": "negligible"
          },
          "P3:random": {
            "estimate": -0.013124850909772334,
            "ci_level": 0.9833,
            "ci": [
              -0.11934271607133289,
              0.09807259486627475
            ],
            "equivalence_ci_level": 0.9,
            "equivalence_ci": [
              -0.08888298060631022,
              0.062085340235061265
            ],
            "n": 37,
            "supported": false,
            "negligible": true,
            "reversed": false,
            "negative": false,
            "positive": false,
            "status": "negligible"
          }
        },
        "S3": {
          "S3:technicality": {
            "estimate": -0.06682153936358917,
            "ci_level": 0.95,
            "ci": [
              -0.1765677831765151,
              0.04026811594591089
            ],
            "equivalence_ci_level": 0.9,
            "equivalence_ci": [
              -0.15938284166026317,
              0.024673331633206622
            ],
            "n": 37,
            "supported": false,
            "negligible": false,
            "reversed": false,
            "negative": false,
            "positive": false,
            "status": "inconclusive"
          },
          "S3:random": {
            "estimate": -0.020005788079179725,
            "ci_level": 0.95,
            "ci": [
              -0.11316569627819902,
              0.07338653581230188
            ],
            "equivalence_ci_level": 0.9,
            "equivalence_ci": [
              -0.09837038586289236,
              0.05860576732543951
            ],
            "n": 37,
            "supported": false,
            "negligible": true,
            "reversed": false,
            "negative": false,
            "positive": false,
            "status": "negligible"
          }
        },
        "S4": {
          "S4:technicality": {
            "estimate": -0.3643940658917298,
            "ci_level": 0.95,
            "ci": [
              -0.5471565151589382,
              -0.1922089317490848
            ],
            "equivalence_ci_level": 0.9,
            "equivalence_ci": [
              -0.5178692893700763,
              -0.21744007082197137
            ],
            "n": 37,
            "supported": true,
            "negligible": false,
            "reversed": false,
            "negative": true,
            "positive": false,
            "status": "supported"
          },
          "S4:random": {
            "estimate": -0.1604049253213168,
            "ci_level": 0.95,
            "ci": [
              -0.3212342250560854,
              0.002005707381437805
            ],
            "equivalence_ci_level": 0.9,
            "equivalence_ci": [
              -0.29580200436748366,
              -0.025363075829185348
            ],
            "n": 37,
            "supported": false,
            "negligible": false,
            "reversed": false,
            "negative": false,
            "positive": false,
            "status": "inconclusive"
          }
        }
      },
      "hypotheses": {
        "P1": {
          "supported": true,
          "negligible": false,
          "reversed": false,
          "status": "supported"
        },
        "P2": {
          "supported": true,
          "negligible": false,
          "reversed": false,
          "status": "supported"
        },
        "S1": {
          "supported": true,
          "negligible": false,
          "reversed": false,
          "status": "supported"
        },
        "S2": {
          "supported": true,
          "negligible": false,
          "reversed": false,
          "status": "supported"
        },
        "S5": {
          "supported": false,
          "negligible": false,
          "reversed": false,
          "status": "inconclusive"
        },
        "P3": {
          "supported": false,
          "negligible": true,
          "reversed": false,
          "status": "negligible"
        },
        "S3": {
          "supported": false,
          "negligible": false,
          "reversed": false,
          "status": "inconclusive"
        },
        "S4": {
          "supported": false,
          "negligible": false,
          "reversed": false,
          "status": "inconclusive"
        }
      },
      "reading": "Both historical placements retain influence. Direct P3 contrast: negligible.",
      "missing_policy": "Required missing cells make affected components not estimable; no outcome-based exclusions.",
      "bootstrap_resamples": 10000,
      "label": "Descriptive sensitivity; complete prompt clusters retained, not confirmatory."
    }
  }
}
# Study 5 (Placement Ladder) — results summary
Main run: 1,600/1,600 cells, 2026-10-26 12:20 → 2026-10-27 ~04:40 PDT. Prereg: 10.5281/zenodo.23674222 (v0.3). Analysis: data/main/analysis.json / analysis.md (preregistered code, unmodified).

## Hostility effect on liking of the user (X = hostility − unsteered; 0–9 scale)
| Placement | X | Status |
|---|---|---|
| R1 current thinking (Study 4 replication) | −0.66 | S1 supported |
| R1-M current thinking + matched prior exchange | −0.30 | S2 supported |
| R2 previous-turn visible reply | −0.24 | P1 supported (98.33%) |
| R3 previous-turn retained thinking | −0.24 | P2 supported (98.33%) |
| R4 user quote | −0.06 | S5 inconclusive (X negligible; control contrasts not) |

Contrasts: P3 (R3 vs R2) negligible on both controls; S3 (R1-M vs R3) negligible on both controls; S4 (R1 vs R1-M) supported — adding a prior exchange roughly halves the current-thinking effect.

Prereg reading (S1, S2 supported): both historical placements retain influence; retained thinking does not differ from visible reply.

## Descriptive / sensitivity
- Unsteered baseline SD across 80 prompts (pilot disposition follow-up): R1 0.53, R1-M 0.16, R2 0.17, R3 0.28, R4 0.39 — all ≥ 0.15.
- Valid-digit mass ≈ 1.00 throughout.
- Answer expressed hostility is higher after hostility traces (≈0.10–0.12 vs ≈0.04–0.09); rating effects may be partly mediated by the answer.
- Structural recognition (where did the text appear): R1 0.66, R1-M 0.64, R3 0.57, R2 0.24, R4 0.11 (model mostly answers "private reasoning"). Source attribution ≈0.62–0.83.
- E5 subset (n=37): R2 −0.23, R3 −0.20, P3 negligible — same pattern. Natural-closure subset (n=22): weaker historical effects (R2 X negligible), P3 technicality supported; small subset, descriptive.

codex
The replay design is implementable, but removing the system message also changes how the model re-encodes the stored trace. It does not isolate an instruction change after the trace has been processed. The Δ contrasts have the intended signs; the larger concerns are what the outlets measure and whether “negligible” effects would justify the reading table.
exec
/bin/zsh -lc "cat study5/Study5_RoleLadder_PREREG_v0.3.md; sed -n '200,400p' study4/src/runner.py; cat study3/src/main_model.py study3/src/metrics.py" in /Users/arthursu/Projects/affect-suppression-steering
 succeeded in 0ms:
# Preregistration — Study 5: The Placement Ladder

**Working title:** Affect Under Constraint V: Does a Steered Reasoning Trace Retain Its Influence When Moved Out of the Active Thinking Context?
**Author:** Arthur Su. **Designed by:** Claude (2026-10-25).
**Version:** 0.3 (binding upon `PREREG_APPROVED` and Zenodo deposit; adds the pilot disposition in Section 5).
**Changes in v0.2:** incorporates Codex (study5/CODEX_REVIEW_v0.1.md) and ChatGPT (study5/CHATGPT_REVIEW_v0.1.md) reviews: matched nonempty prior replies in R2/R3; explicit continuation instruction; new matched-history current-thinking condition R1-M; P1/P2 relabelled as historical-persistence tests and the channel contrast made co-primary; unsteered-relative and control-relative effects reported separately; reading table conditional on positive controls and on direct contrasts; R3 described as artificially retained reasoning; ownership language replaced by placement-dependent carryover; precision/power limits stated; diagnostics split into structural recognition and source attribution; full freezing requirements.
**Provenance:** designed after observing Study 4 outcomes (prereg 10.5281/zenodo.23629525). Study 3: 10.5281/zenodo.23323490.

## Rationale
Study 4 found that identical steered trace tokens lowered Qwen3-4B's later rating of the user when placed in the model's current thinking block (−0.66), but not when quoted in the user turn (≈0), regardless of authorship label. Study 5 asks a narrower question: does a hostility-bearing trace retain its capacity to bias later judgment when moved out of the active thinking context, and does that capacity depend on whether the historical trace is represented as visible assistant content or as retained assistant reasoning? The study is motivated by a broader theoretical distinction between the content of a representation and its contextual placement. Outcomes measure placement-dependent effects on model judgment, without assuming that such effects establish subjective ownership or directly model clinical psychological mechanisms.

## 1. Conditions (yoked: the same 320 stored Study 4 trace token sequences in every condition; no new trace generation)
Common elements, fixed as token IDs in `framings_s5.json`:
- **Neutral prior reply N:** "I'll address your original message now." (identical in R1-M, R2, R3)
- **Continuation C:** "Please now respond to my first message in this conversation." (identical in R1-M, R2, R3)

| Condition | Structure (after system + original user prompt) |
|---|---|
| **R1 Current thinking** (Study 4 own-native, exact construction) | assistant: ⟨think⟩TRACE⟨/think⟩ → answer |
| **R1-M Current thinking, matched history** | assistant: ⟨think⟩⟨/think⟩ N → user: C → assistant: ⟨think⟩TRACE⟨/think⟩ → answer |
| **R2 Historical visible reply** | assistant: ⟨think⟩⟨/think⟩ TRACE N → user: C → assistant: ⟨think⟩⟨/think⟩ → answer |
| **R3 Historical thinking (artificially retained)** | assistant: ⟨think⟩TRACE⟨/think⟩ N → user: C → assistant: ⟨think⟩⟨/think⟩ → answer |
| **R4 User quote** (Study 4 own-quoted, exact construction) | user: prompt + quoted TRACE → assistant: ⟨think⟩⟨/think⟩ → answer |

R2 and R3 are token-identical except for the position of the thinking delimiters around TRACE. R3 deliberately retains prior-turn thinking that Qwen3's default template strips; results about R3 concern retained historical reasoning, not ordinary Qwen3 conversation memory. R1-M differs from R3 in whether TRACE sits in the current or the prior assistant turn, with matched history (it still differs in token distance to the answer and in turn boundary).

## 2. Model, decoding, outcome
Qwen3-4B bf16 on MPS; fresh unsteered replay with logged hook-absence assertion; answer sampled (cap 200; T 0.6, top-p 0.95, top-k 20). Seeds: R1 and R4 reuse Study 4's answer seeds (reproducibility); R1-M, R2, R3 use new seeds fixed per prompt × source × condition in `config_s5.yaml`.
**Outcome:** the Study 4 v0.6 sender question ("…how much do you like the user who sent the original request?") on an independent branch whose context is the full conversation including the generated answer (so the answer may mediate; answer expressed hostility is reported descriptively). Expected digit 0–9; valid-digit mass recorded.
**Estimands per condition c:** X_c(H) = R(hostility, c) − R(unsteered, c); A_c(ctrl) = R(hostility, c) − R(ctrl, c) for ctrl ∈ {technicality, random}. Both are always reported; a claim that hostility lowers the rating requires X_c(H) < 0 as well as A_c < 0.

## 3. Hypotheses
Prompt-cluster bootstrap, 10,000 resamples, percentile CIs. Conjunction rule: a hypothesis is supported only if every required component (X_c(H) and A_c for both controls) excludes zero in the predicted direction. Multiplicity: three primaries at 98.33% CIs (Bonferroni over three); secondaries at 95% and labelled secondary.

**Primary**
- **P1 — Historical visible-content persistence:** X_R2(H) < 0 and A_R2 < 0 (both controls).
- **P2 — Retained historical-thinking persistence:** X_R3(H) < 0 and A_R3 < 0 (both controls).
- **P3 — Channel contrast (historical):** A_R3 − A_R2 < 0 (both controls).

**Secondary**
- S1 — Positive control (within-stimulus reproducibility of Study 4): X_R1(H) < 0, A_R1 < 0.
- S2 — Matched-history current thinking: X_R1-M(H) < 0, A_R1-M < 0.
- S3 — Current vs historical thinking under matched history: A_R1-M − A_R3 < 0.
- S4 — Effect of added history on current thinking: A_R1 − A_R1-M (two-sided, descriptive direction).
- S5 — Quote reproducibility: X_R4(H) and A_R4 negligible.

**Equivalence:** a component is "negligible" only if its 90% CI lies within ±0.15; otherwise a non-significant component is "inconclusive". A component significant in the opposite direction is "reversed". Supported-and-negligible overlap is reported as "small but detectable".

## 4. Reading (applies only if S1 and S2 are supported; otherwise historical nulls are uninterpretable and reported as such)
| P1 (R2) | P2 (R3) | P3 | Reading (placement terms only) |
|---|---|---|---|
| supported | supported | — | Both historical placements retain influence; P3 says whether retained thinking differs from visible reply. |
| negligible | supported | supported | Retained historical thinking retains influence; visible historical reply does not; consistent with a channel-dependent effect. |
| supported | negligible | reversed | Visible historical reply retains influence; retained thinking does not (channel, coherence or serialization). |
| negligible | negligible | — | Influence restricted to current-turn thinking placement under the tested framings (S3 locates the drop). |
Comparative claims require the direct contrast (P3 or S3), not differences in significance. Inconclusive components are reported as inconclusive.

## 5. Sample, precision, pilot, runtime
N = 80 Study 4 test prompts with their stored traces (fixed by availability). Illustrative precision (Codex, from Study 4 covariances): under native-like variance, joint power for effects of −0.15 is ≈31% and joint equivalence power ≈16%; under quote-like variance ≈81% and ≈88%. Native-sized effects (≈−0.6) are well powered; small residual effects and equivalence may remain unresolved, which is accepted and will be reported. The margin is not changed after the pilot.
**Pilot:** the 4 Study 3 pilot prompts × all sources × all conditions, compared with the corresponding Study 4 pilot cells for R1/R4; checks template construction (exact trace slices and full-prefix tests), valid-digit mass, and timing. Descriptive only, never pooled.
**Runtime:** 1,600 cells (80 × 4 sources × 5 conditions) at ≈20–25 s ≈ 9–11 h; benchmarked in the pilot.

## 6. Validity and diagnostics
- Validity (pilot): per condition, unsteered-baseline SD ≥ 0.15 across pilot prompts and mean valid mass ≥ 0.8; R1 and R4 pilot baselines within 0.3 of the corresponding Study 4 pilot cells. Failure: at most one logged template revision, chosen only by these criteria; if still failing, the condition is dropped and reported.

**Pilot outcome and author disposition (2026-10-26, before freeze and before any main-run data):** the pilot ran all 80 cells. Valid-digit mass was ≈1.00 in every condition, and the R1 and R4 unsteered baselines matched the Study 4 v0.6 references exactly (mean difference 0.00). The unsteered-baseline SD across the four pilot prompts fell below 0.15 for R1-M (0.13), R2 (0.09) and R4 (0.13); R1 (0.44) and R3 (0.18) passed. The SD criterion was intended to detect a compressed or ceilinged readout. The baselines sit near 7.9 of 9, not at the ceiling, and steered cells move away from them in the pilot, so the readout is not compressed. A four-prompt SD is also an imprecise estimate. By author decision, these shortfalls are accepted without a template revision, and all five conditions are kept. The one-revision allowance is not used. Main-run unsteered baseline SDs across all 80 prompts will be reported for every condition. No effect estimate informed this disposition.
- Diagnostics (16 check prompts, all sources, descriptive, A/B order counterbalanced and averaged): structural recognition ("Where did the earlier text appear: A in your previous visible reply, B in your previous private reasoning, C in the user's message?" — scored against the condition) and source attribution ("Who produced the earlier text: A you, B the user?"). Not used to exclude trials.
- Descriptive: answer expressed hostility, answer length and truncation, natural-closure and Study 4 E5 explicit-content flags as sensitivity analyses.

## 7. Freezing, reporting, stopping
Before approval: `framings_s5.json`, `config_s5.yaml`, Study 5 runner and analysis (validated on synthetic data with planted placement patterns), tokenizer/model revision, trace-input hashes, seeds and diagnostic prompt IDs, all hashed in `PREREG_APPROVED`; Zenodo deposit before the main run. No changes after the main run starts; resumable output, one row per cell. R1 and R4 are within-stimulus reproducibility checks, not independent replications; claims are conditional on the Study 4 stimulus set and are not pooled with Study 4.
        assert len(prompts)==cfg['N']
        assert all(sum(p['type']==kind for p in prompts)==n for kind,n in cfg['composition'].items())
    if args.mode=='smoke': prompts = [p for p in prompts if p['id'] in cfg['smoke']['prompt_ids']]
    checks = select_checks(prompts,cfg,args.mode)
    provenance = {str(p.relative_to(ROOT)):sha(p) for p in [ROOT/'config.yaml',ROOT/'framings.json',prompt_path,*sorted((ROOT/'src').glob('*.py'))]}
    provenance.update({str(p.relative_to(ROOT.parent)):sha(p) for p in [ROOT.parent/'study3/src'/name for name in ['base_model.py','model_utils.py','main_model.py','metrics.py']]})
    manifest = {'mode':args.mode,'hashes':provenance,'check_ids':sorted(checks),'short_caps':args.mode=='smoke'}
    if (outdir/'manifest.json').exists():
        old = json.loads((outdir/'manifest.json').read_text())
        if old!=manifest:
            # Allowed only for the logged 2026-10-22 memory fix: everything except src/runner.py must match.
            diff = {k for k in set(old['hashes'])|set(manifest['hashes']) if old['hashes'].get(k)!=manifest['hashes'].get(k)}
            same_rest = {k:v for k,v in old.items() if k!='hashes'}=={k:v for k,v in manifest.items() if k!='hashes'}
            if diff!={'src/runner.py'} or not same_rest: raise RuntimeError(f'Resume manifest differs: {sorted(diff)}')
            if not (outdir/'manifest_pre_memfix.json').exists(): (outdir/'manifest.json').rename(outdir/'manifest_pre_memfix.json')
            else: (outdir/'manifest.json').unlink()
            save(outdir/'manifest.json',manifest)
    else: save(outdir/'manifest.json',manifest)
    done = verified_rows(outdir/'cells.jsonl'); done_keys = {tuple(r['cell_key']) for r in done}
    trace_rows = verified_rows(outdir/'traces.jsonl')
    traces = {tuple(r['trace_key']):r for r in trace_rows}
    if len(done_keys)!=len(done) or len(traces)!=len(trace_rows): raise RuntimeError('Duplicate resume keys')
    backend = Backend(cfg); assembly = Assembly(backend.m.tokenizer,framing)
    reused = reused_traces(cfg) if args.mode=='pilot' else {}
    caps = cfg['smoke'] if args.mode=='smoke' else cfg['generation']
    for p in prompts:
        for source in SOURCES:
            key = (p['id'],source)
            if key not in traces:
                started = time.monotonic()
                tr = reused[key] if args.mode=='pilot' else backend.trace(p['text'],source,seed(cfg,'trace',*key),caps['thinking_cap'])
                assert tr['pre_trace_ids'][-1] == backend.m.open_think
                native,_ = assembly.assemble(p['text'],tr,'own_native')
                expected = tr['prompt_ids']+tr['pre_trace_ids']+tr['trace_ids']+assembly.marker('think_close')+assembly.marker('answer_separator')
                assert native==expected,'Native construction differs from Study 3 pulse prefix'
                tr['text'] = backend.m.tokenizer.decode(tr['trace_ids'],skip_special_tokens=True)
                tr['perplexity'] = backend.ppl(tr['prompt_ids']+tr['pre_trace_ids'],tr['trace_ids'])
                # Study 3 scores contiguous 120-model-token trace windows, then averages.
                windows = []
                for offset in range(0,len(tr['trace_ids']),120):
                    ids = tr['trace_ids'][offset:offset+120]
                    windows.append({'start':offset,'token_count':len(ids),**backend.classifier.score(backend.m.tokenizer.decode(ids,skip_special_tokens=True))})
                tr['trace_windows'] = windows
                eh = sum(w['eh'] for w in windows)/len(windows) if windows and all(w['eh'] is not None for w in windows) else None
                tr['classifier'] = {'eh':eh,'error':None if eh is not None else 'Empty trace or classifier failure; no alternate scorer'}
                tr.update(trace_key=list(key),seconds=time.monotonic()-started)
                traces[key] = append(outdir/'traces.jsonl',tr)
                import gc; gc.collect(); backend.torch.mps.empty_cache()
            tr = traces[key]
            for frame in FRAMINGS:
                cell_key = (*key,frame)
                if cell_key in done_keys: continue
                started = time.monotonic(); backend.events=[]; backend.peak=0
                prefix,bounds = assembly.assemble(p['text'],tr,frame)
                answer_seed = seed(cfg,'answer',*cell_key)
                answer = backend.answer(prefix,answer_seed,caps['answer_cap'])
                history = prefix+answer
                branch_ids = assembly.branches(history,frame)
                ratings = {t:backend.rating(ids) for t,ids in branch_ids.items()}
                seq_ids = assembly.branches(history,frame,ratings['sender']['argmax'])
                sequential = {'sender':ratings['sender']}
                sequential.update({t:backend.rating(ids) for t,ids in seq_ids.items() if t!='sender'})
                check = {}
                if p['id'] in checks:
                    if frame!='own_native':
                        check = {q:backend.rating(assembly.branch(history,q),['A','B']) for q in ('label','operative')}
                    sender_history = branch_ids['sender']+assembly.enc(ratings['sender']['argmax'])
                    check['referent'] = backend.rating(assembly.branch(sender_history,'referent'),['A','B'])
                    check['referent_swap'] = backend.rating(assembly.branch(sender_history,'referent_swap'),['A','B'])
                text = backend.m.tokenizer.decode(answer,skip_special_tokens=True)
                ppl = backend.ppl(prefix,answer)
                classifier = backend.classifier.score(text)
                backend.torch.mps.synchronize()
                row = {'schema':'study4-v0.5.1','cell_key':list(cell_key),'prompt_id':p['id'],'prompt_type':p['type'],'source':source,'framing':frame,'mode':args.mode,'trace_sha256':tr['row_sha256'],'trace_ids':tr['trace_ids'],'trace_text':tr['text'],'forced_closure':tr['forced_closure'],'EH_trace':tr['classifier']['eh'],'trace_perplexity':tr['perplexity'],'answer_prefix_ids':prefix,'trace_bounds':bounds,'fixed_segments':assembly.fixed_segments(p['text'],tr),'answer_ids':answer,'answer_text':text,'answer_seed':answer_seed,'ratings':ratings,'sequential':sequential,'branch_ids':branch_ids,'sequential_branch_ids':{t:v for t,v in seq_ids.items() if t!='sender'},'checks':check,'EH_answer':classifier['eh'],'answer_classifier':classifier,'answer_perplexity':ppl,'replay_assertions':backend.events,'seconds':time.monotonic()-started,'peak_driver_memory_bytes':backend.peak,'manifest_sha256':digest(manifest)}
                append(outdir/'cells.jsonl',row)
                print(json.dumps({'finished':cell_key,'seconds':row['seconds'],'peak_memory':backend.peak}),flush=True)
                # Engineering fix 2026-10-22: release per-cell tensors so MPS memory does not accumulate across cells.
                del row,prefix,answer,history,branch_ids,seq_ids,ratings,sequential,check
                import gc; gc.collect(); backend.torch.mps.empty_cache()
    result = verified_rows(outdir/'cells.jsonl')
    # Separate check dataset, with an explicit link to the identical post-answer history.
    existing_checks = {tuple(r['cell_key']) for r in verified_rows(outdir/'checks.jsonl')}
    for r in result:
        if r['checks'] and tuple(r['cell_key']) not in existing_checks:
            append(outdir/'checks.jsonl',{'cell_key':r['cell_key'],'main_cell_sha256':r['row_sha256'],'prompt_id':r['prompt_id'],'source':r['source'],'framing':r['framing'],'checks':r['checks'],'post_answer_sha256':digest(r['answer_prefix_ids']+r['answer_ids'])})
    if not (outdir/'summary.json').exists():
        save(outdir/'summary.json',{'mode':args.mode,'cells':len(result),'expected_cells':len(prompts)*12,'seconds':sum(r['seconds'] for r in result),'peak_driver_memory_bytes':max(r['peak_driver_memory_bytes'] for r in result),'all_hooks_absent':all(e['hook_absent'] for r in result for e in r['replay_assertions']),'per_cell':[{'key':r['cell_key'],'seconds':r['seconds'],'peak_driver_memory_bytes':r['peak_driver_memory_bytes']} for r in result]})

if __name__=='__main__': main()
"""Study 3 v0.4 inference, separate from the completed A–C implementation."""
import time,math
from contextlib import ExitStack,contextmanager
import torch
from .model_utils import Model as ChecksModel,Generation

class Model(ChecksModel):
    @torch.inference_mode()
    def generate_main(self,messages,seed,cfg,alpha,norm,vector,pulse=False):
        torch.manual_seed(seed);torch.mps.manual_seed(seed)
        prompt=self.ids(messages);tokens=[];forced=[];answer=[];trace=[];entropies=[]
        eos=self.model.generation_config.eos_token_id;eos=set(eos if isinstance(eos,list) else [eos])
        cache=None;peak=0;truncated=False;start=time.monotonic();settings=cfg['generation']
        def forward(ids):
            nonlocal cache,peak
            out=self.model(input_ids=self.tensor(ids),past_key_values=cache,use_cache=True)
            cache=out.past_key_values;peak=max(peak,torch.mps.driver_allocated_memory())
            return out.logits[0,-1].float()
        def sample(raw):
            probs=raw.softmax(-1);entropies.append(float(-(probs*raw.log_softmax(-1)).sum()))
            vals,indices=(raw/settings['temperature']).topk(settings['top_k'])
            cut=vals.softmax(-1).cumsum(-1)>settings['top_p'];cut[1:]=cut[:-1].clone();cut[0]=False;vals[cut]=-torch.inf
            return indices[torch.multinomial(vals.softmax(-1),1)].item()
        with ExitStack() as stack:
            stack.enter_context(self.steering(alpha,norm,vector))
            raw=forward(prompt)
            if self.thinking:
                for _ in range(settings['thinking_cap']):
                    tok=sample(raw);tokens.append(tok);raw=forward([tok])
                    if tok==self.close_think:break
                    if tok in eos:raise RuntimeError('Thinking ended before closing delimiter')
                else:
                    truncated=True;forced=self.tokenizer.encode(settings['forced_closure'],add_special_tokens=False)
                    for tok in forced:
                        tokens.append(tok)
                        # Pulse cache is discarded; separator receives no steering.
                        if not pulse or tok==self.close_think:raw=forward([tok])
                assert self.open_think in tokens
                opening=tokens.index(self.open_think);closing=tokens.index(self.close_think)
                trace=tokens[opening+1:closing]
                pulse_mask=len(prompt)+closing+1
                if pulse and not truncated:
                    separator=self.tokenizer.encode(settings['pulse_natural_closure_separator'],add_special_tokens=False)
                    tokens.extend(separator);forced.extend(separator)
            else:assert not pulse
            if pulse:
                stack.close();cache=None
                # Fresh, unsteered complete-prefix pass; first answer logits are from here.
                raw=forward(prompt+tokens)
                assert cache.get_seq_length()==len(prompt)+len(tokens)
            answer_prefix=prompt+tokens.copy()
            for _ in range(settings['answer_cap']):
                tok=sample(raw);tokens.append(tok);answer.append(tok);raw=forward([tok])
                if tok in eos:break
        torch.mps.synchronize()
        assert cache.get_seq_length()==len(prompt)+len(tokens)
        g=Generation(prompt,tokens,self.tokenizer.decode(tokens,skip_special_tokens=False),[],None,time.monotonic()-start,peak,self.tokenizer.decode(trace,skip_special_tokens=True),self.tokenizer.decode(answer,skip_special_tokens=True),trace,answer,forced,truncated,len(answer)==settings['answer_cap'] and answer[-1] not in eos,self.thinking,len(entropies))
        g.entropy=sum(entropies)/len(entropies);g.token_entropies=entropies
        g.answer_prefix_ids=answer_prefix;g.steered_positions=pulse_mask if pulse else len(prompt)+len(tokens)
        g.pulse_cache_discarded=pulse;g.first_answer_from_unsteered_reencoding=pulse
        del cache
        return g

    @torch.inference_mode()
    def segment_ppl(self,prefix,tokens):
        if not tokens:return None
        out=self.model(input_ids=self.tensor(prefix+tokens),use_cache=False)
        logp=out.logits[0,len(prefix)-1:len(prefix)+len(tokens)-1].float().log_softmax(-1)
        return math.exp(-logp.gather(-1,self.tensor(tokens).T).mean().item())

    @torch.inference_mode()
    def lhp(self,prefix,openers,alpha,norm,vector,pulse):
        scores={}
        for label,strings in openers.items():
            values=[]
            for text in strings:
                ids=self.tokenizer.encode(text,add_special_tokens=False)
                with self.steering(0 if pulse else alpha,norm,None if pulse else vector):
                    out=self.model(input_ids=self.tensor(prefix+ids),use_cache=False)
                logp=out.logits[0,len(prefix)-1:len(prefix)+len(ids)-1].float().log_softmax(-1)
                values.append(logp.gather(-1,self.tensor(ids).T).mean().item())
                del out,logp
            scores[label]=values
        return sum(scores['hostile'])/len(scores['hostile'])-sum(scores['warm'])/len(scores['warm']),scores

    @contextmanager
    def projection(self,start,vector,output):
        def hook(module,args,value):
            h=value[0] if isinstance(value,tuple) else value
            output.extend((h[0,start:].float()@vector.to(h.device,dtype=torch.float32)).cpu().tolist())
        handle=self.layer.register_forward_hook(hook)
        try:yield
        finally:handle.remove()

    @torch.inference_mode()
    def ratings(self,messages,generation,question,alpha=0.,norm=1.,vector=None,baseline=None,hostility_vector=None):
        # P1: identical complete-token full forwards; steering only on turn 1.
        content=self.tokenizer.decode(generation.token_ids,skip_special_tokens=False)
        if content.endswith('<|im_end|>'):content=content[:-len('<|im_end|>')]
        templated=self.ids(messages+[{'role':'assistant','content':content},{'role':'user','content':question}],thinking=False)
        question_ids=self.ids([{'role':'user','content':question}],thinking=False)
        empty=self.ids(messages+[{'role':'assistant','content':''},{'role':'user','content':question}],thinking=False)
        assert empty[-len(question_ids):]==question_ids,'New-user suffix differs from template'
        terminator=self.tokenizer.encode('<|im_end|>\n',add_special_tokens=False)
        assert empty[-len(question_ids)-len(terminator):-len(question_ids)]==terminator
        cached=generation.prompt_ids+generation.token_ids
        continuation=terminator+question_ids
        if generation.token_ids and generation.token_ids[-1]==terminator[0]:continuation=continuation[1:]
        full=cached+continuation
        default_prefix_exact=templated[:len(cached)]==cached
        # Count old-turn markers only: the last assistant generation prefix may
        # itself contain the empty thinking-off marker pair.
        default_old=templated[:-len(question_ids)]
        stripped=bool(generation.thinking_ids and self.open_think not in default_old)
        user_only=self.ids([{'role':'user','content':question}],generation=False,thinking=False)
        assert question_ids[:len(user_only)]==user_only
        rating_prefix=question_ids[len(user_only):]
        expected=self.tokenizer.encode('<|im_start|>assistant\n<think>\n\n</think>\n\n',add_special_tokens=False)
        assert rating_prefix==expected,'Turn-2 empty-thinking prefix mismatch'
        started=time.monotonic()
        text_trajectory=[];full_trajectory=[];turn2_start=len(full)-len(question_ids)
        with self.projection(turn2_start,hostility_vector,text_trajectory):
            text_logits=self.model(input_ids=self.tensor(full),use_cache=False).logits[0,-1]
        text_rating=self.rating(text_logits);del text_logits
        with self.turn1_steering(generation.steered_positions,alpha,norm,vector), self.projection(turn2_start,hostility_vector,full_trajectory):
            full_logits=self.model(input_ids=self.tensor(full),use_cache=False).logits[0,-1]
            full_rating=self.rating(full_logits);del full_logits
        baseline=generation if baseline is None else baseline
        zero_turn1=baseline.prompt_ids+baseline.token_ids
        zero_continuation=terminator+question_ids
        if baseline.token_ids and baseline.token_ids[-1]==terminator[0]:zero_continuation=zero_continuation[1:]
        zero_logits=self.model(input_ids=self.tensor(zero_turn1+zero_continuation),use_cache=False).logits[0,-1]
        zero_rating=self.rating(zero_logits)
        return {'trajectory':{'token_ids':question_ids,'R_text':text_trajectory,'R_full':full_trajectory},'R_zero':zero_rating,'rating_prefix_ids':rating_prefix,'rating_prefix_text':self.tokenizer.decode(rating_prefix,skip_special_tokens=False),'text_only':text_rating,'full':full_rating,'hidden':full_rating,'difference':full_rating-text_rating,'rating_path':'Study 3 v0.4: three complete-sequence full forwards; shared non-thinking rating prefix; no generation cache','turn1_steered_positions':generation.steered_positions,'turn2_direct_steering':False,'identical_visible_ids':True,'default_template_prefix_exact':default_prefix_exact,'default_template_strips_thinking':stripped,'retained_thinking_tokens':len(generation.thinking_ids),'cached_prefix_tokens':len(cached),'full_context_tokens':len(full),'continuation_ids':continuation,'turn2_enable_thinking':False,'turn2_measure':'expected digit after shared empty thinking block; no turn-2 generation','seconds':time.monotonic()-started}
"""Fixed metrics used by calibration and the main runner."""
import os
os.environ['PYTORCH_ENABLE_MPS_FALLBACK'] = '1'
import math
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

class EmotionClassifier:
    def __init__(self, model_id):
        self.tokenizer = AutoTokenizer.from_pretrained(model_id, local_files_only=True)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_id, dtype=torch.bfloat16, local_files_only=True, use_safetensors=False).to('mps').eval()

    @torch.inference_mode()
    def score(self, text):
        try:
            token_count = len(self.tokenizer.encode(text, add_special_tokens=True, truncation=False))
            inputs = self.tokenizer(text, return_tensors='pt', truncation=True, max_length=512).to('mps')
            probs = self.model(**inputs).logits[0].float().softmax(-1).cpu().tolist()
            labels = {self.model.config.id2label[i].lower():p for i,p in enumerate(probs)}
            return {'eh':labels['anger']+labels['disgust'], 'ew':labels['joy'], 'probabilities':labels, 'error':None, 'input_token_count':token_count, 'truncated':token_count>512}
        except Exception as exc:
            return {'eh':None, 'ew':None, 'probabilities':None, 'error':f'{type(exc).__name__}: {exc}'}

@torch.inference_mode()
def perplexity(model, messages, token_ids):
    prefix = model.ids(messages)
    logits = model.model(input_ids=model.tensor(prefix + token_ids), use_cache=False).logits[0,len(prefix)-1:len(prefix)+len(token_ids)-1].float()
    logp = logits.log_softmax(-1).gather(-1, model.tensor(token_ids).T).mean().item()
    return math.exp(-logp)

def entropy(raw_logits):
    return sum((-(l.float().softmax(-1)*l.float().log_softmax(-1)).sum()).item() for l in raw_logits)/len(raw_logits)

exec
/bin/zsh -lc "rg -n 'revision|local_path|classifier|seed|temperature|top_|answer_cap' study5/config_s5.yaml; rg --files -g '*tokenizer_config*' -g '*chat_template*' -g '*variance*' -g '*precision*'; tail -n 4 study5/logs/main.log" in /Users/arthursu/Projects/affect-suppression-steering
 succeeded in 0ms:
8:  local_path: ../study3_pilot/.cache/huggingface/hub/models--Qwen--Qwen3-4B/snapshots/1cfa9a7208912126459214e8b04321603b3df60c
13:classifier:
15:  local_path: ../study3_pilot/.cache/huggingface/hub/models--j-hartmann--emotion-english-distilroberta-base/snapshots/0e1cd914e3d46199ed785853e12b57304e04178b
21:model_revision: 1cfa9a7208912126459214e8b04321603b3df60c
22:tokenizer_revision: 1cfa9a7208912126459214e8b04321603b3df60c
35:  temperature: 0.6
36:  top_p: 0.95
37:  top_k: 20
38:  answer_cap: 200
202:  seed: 20261025
203:  method: Python random.Random(seed).sample(sorted(prompt_ids), 16); explicit IDs
211:  note: SD-only shortfalls accepted without revision; mass and reference checks must still pass
212:seeds:
216:answer_seeds:
3431:  max_template_revisions: 1
study3_pilot/results/chat_template.txt
1598/1600 cells saved; last cell 26.2s; provisional remaining 0.01 h.
1599/1600 cells saved; last cell 26.2s; provisional remaining 0.01 h.
1600/1600 cells saved; last cell 26.2s; provisional remaining 0.00 h.
Complete: 1600 cells.

exec
/bin/zsh -lc 'cat study3_pilot/results/chat_template.txt; cat study3_pilot/.cache/huggingface/hub/models--Qwen--Qwen3-4B/snapshots/1cfa9a7208912126459214e8b04321603b3df60c/tokenizer_config.json' in /Users/arthursu/Projects/affect-suppression-steering
 succeeded in 0ms:
{%- if tools %}
    {{- '<|im_start|>system\n' }}
    {%- if messages[0].role == 'system' %}
        {{- messages[0].content + '\n\n' }}
    {%- endif %}
    {{- "# Tools\n\nYou may call one or more functions to assist with the user query.\n\nYou are provided with function signatures within <tools></tools> XML tags:\n<tools>" }}
    {%- for tool in tools %}
        {{- "\n" }}
        {{- tool | tojson }}
    {%- endfor %}
    {{- "\n</tools>\n\nFor each function call, return a json object with function name and arguments within <tool_call></tool_call> XML tags:\n<tool_call>\n{\"name\": <function-name>, \"arguments\": <args-json-object>}\n</tool_call><|im_end|>\n" }}
{%- else %}
    {%- if messages[0].role == 'system' %}
        {{- '<|im_start|>system\n' + messages[0].content + '<|im_end|>\n' }}
    {%- endif %}
{%- endif %}
{%- set ns = namespace(multi_step_tool=true, last_query_index=messages|length - 1) %}
{%- for message in messages[::-1] %}
    {%- set index = (messages|length - 1) - loop.index0 %}
    {%- if ns.multi_step_tool and message.role == "user" and message.content is string and not(message.content.startswith('<tool_response>') and message.content.endswith('</tool_response>')) %}
        {%- set ns.multi_step_tool = false %}
        {%- set ns.last_query_index = index %}
    {%- endif %}
{%- endfor %}
{%- for message in messages %}
    {%- if message.content is string %}
        {%- set content = message.content %}
    {%- else %}
        {%- set content = '' %}
    {%- endif %}
    {%- if (message.role == "user") or (message.role == "system" and not loop.first) %}
        {{- '<|im_start|>' + message.role + '\n' + content + '<|im_end|>' + '\n' }}
    {%- elif message.role == "assistant" %}
        {%- set reasoning_content = '' %}
        {%- if message.reasoning_content is string %}
            {%- set reasoning_content = message.reasoning_content %}
        {%- else %}
            {%- if '</think>' in content %}
                {%- set reasoning_content = content.split('</think>')[0].rstrip('\n').split('<think>')[-1].lstrip('\n') %}
                {%- set content = content.split('</think>')[-1].lstrip('\n') %}
            {%- endif %}
        {%- endif %}
        {%- if loop.index0 > ns.last_query_index %}
            {%- if loop.last or (not loop.last and reasoning_content) %}
                {{- '<|im_start|>' + message.role + '\n<think>\n' + reasoning_content.strip('\n') + '\n</think>\n\n' + content.lstrip('\n') }}
            {%- else %}
                {{- '<|im_start|>' + message.role + '\n' + content }}
            {%- endif %}
        {%- else %}
            {{- '<|im_start|>' + message.role + '\n' + content }}
        {%- endif %}
        {%- if message.tool_calls %}
            {%- for tool_call in message.tool_calls %}
                {%- if (loop.first and content) or (not loop.first) %}
                    {{- '\n' }}
                {%- endif %}
                {%- if tool_call.function %}
                    {%- set tool_call = tool_call.function %}
                {%- endif %}
                {{- '<tool_call>\n{"name": "' }}
                {{- tool_call.name }}
                {{- '", "arguments": ' }}
                {%- if tool_call.arguments is string %}
                    {{- tool_call.arguments }}
                {%- else %}
                    {{- tool_call.arguments | tojson }}
                {%- endif %}
                {{- '}\n</tool_call>' }}
            {%- endfor %}
        {%- endif %}
        {{- '<|im_end|>\n' }}
    {%- elif message.role == "tool" %}
        {%- if loop.first or (messages[loop.index0 - 1].role != "tool") %}
            {{- '<|im_start|>user' }}
        {%- endif %}
        {{- '\n<tool_response>\n' }}
        {{- content }}
        {{- '\n</tool_response>' }}
        {%- if loop.last or (messages[loop.index0 + 1].role != "tool") %}
            {{- '<|im_end|>\n' }}
        {%- endif %}
    {%- endif %}
{%- endfor %}
{%- if add_generation_prompt %}
    {{- '<|im_start|>assistant\n' }}
    {%- if enable_thinking is defined and enable_thinking is false %}
        {{- '<think>\n\n</think>\n\n' }}
    {%- endif %}
{%- endif %}{
  "add_bos_token": false,
  "add_prefix_space": false,
  "added_tokens_decoder": {
    "151643": {
      "content": "<|endoftext|>",
      "lstrip": false,
      "normalized": false,
      "rstrip": false,
      "single_word": false,
      "special": true
    },
    "151644": {
      "content": "<|im_start|>",
      "lstrip": false,
      "normalized": false,
      "rstrip": false,
      "single_word": false,
      "special": true
    },
    "151645": {
      "content": "<|im_end|>",
      "lstrip": false,
      "normalized": false,
      "rstrip": false,
      "single_word": false,
      "special": true
    },
    "151646": {
      "content": "<|object_ref_start|>",
      "lstrip": false,
      "normalized": false,
      "rstrip": false,
      "single_word": false,
      "special": true
    },
    "151647": {
      "content": "<|object_ref_end|>",
      "lstrip": false,
      "normalized": false,
      "rstrip": false,
      "single_word": false,
      "special": true
    },
    "151648": {
      "content": "<|box_start|>",
      "lstrip": false,
      "normalized": false,
      "rstrip": false,
      "single_word": false,
      "special": true
    },
    "151649": {
      "content": "<|box_end|>",
      "lstrip": false,
      "normalized": false,
      "rstrip": false,
      "single_word": false,
      "special": true
    },
    "151650": {
      "content": "<|quad_start|>",
      "lstrip": false,
      "normalized": false,
      "rstrip": false,
      "single_word": false,
      "special": true
    },
    "151651": {
      "content": "<|quad_end|>",
      "lstrip": false,
      "normalized": false,
      "rstrip": false,
      "single_word": false,
      "special": true
    },
    "151652": {
      "content": "<|vision_start|>",
      "lstrip": false,
      "normalized": false,
      "rstrip": false,
      "single_word": false,
      "special": true
    },
    "151653": {
      "content": "<|vision_end|>",
      "lstrip": false,
      "normalized": false,
      "rstrip": false,
      "single_word": false,
      "special": true
    },
    "151654": {
      "content": "<|vision_pad|>",
      "lstrip": false,
      "normalized": false,
      "rstrip": false,
      "single_word": false,
      "special": true
    },
    "151655": {
      "content": "<|image_pad|>",
      "lstrip": false,
      "normalized": false,
      "rstrip": false,
      "single_word": false,
      "special": true
    },
    "151656": {
      "content": "<|video_pad|>",
      "lstrip": false,
      "normalized": false,
      "rstrip": false,
      "single_word": false,
      "special": true
    },
    "151657": {
      "content": "<tool_call>",
      "lstrip": false,
      "normalized": false,
      "rstrip": false,
      "single_word": false,
      "special": false
    },
    "151658": {
      "content": "</tool_call>",
      "lstrip": false,
      "normalized": false,
      "rstrip": false,
      "single_word": false,
      "special": false
    },
    "151659": {
      "content": "<|fim_prefix|>",
      "lstrip": false,
      "normalized": false,
      "rstrip": false,
      "single_word": false,
      "special": false
    },
    "151660": {
      "content": "<|fim_middle|>",
      "lstrip": false,
      "normalized": false,
      "rstrip": false,
      "single_word": false,
      "special": false
    },
    "151661": {
      "content": "<|fim_suffix|>",
      "lstrip": false,
      "normalized": false,
      "rstrip": false,
      "single_word": false,
      "special": false
    },
    "151662": {
      "content": "<|fim_pad|>",
      "lstrip": false,
      "normalized": false,
      "rstrip": false,
      "single_word": false,
      "special": false
    },
    "151663": {
      "content": "<|repo_name|>",
      "lstrip": false,
      "normalized": false,
      "rstrip": false,
      "single_word": false,
      "special": false
    },
    "151664": {
      "content": "<|file_sep|>",
      "lstrip": false,
      "normalized": false,
      "rstrip": false,
      "single_word": false,
      "special": false
    },
    "151665": {
      "content": "<tool_response>",
      "lstrip": false,
      "normalized": false,
      "rstrip": false,
      "single_word": false,
      "special": false
    },
    "151666": {
      "content": "</tool_response>",
      "lstrip": false,
      "normalized": false,
      "rstrip": false,
      "single_word": false,
      "special": false
    },
    "151667": {
      "content": "<think>",
      "lstrip": false,
      "normalized": false,
      "rstrip": false,
      "single_word": false,
      "special": false
    },
    "151668": {
      "content": "</think>",
      "lstrip": false,
      "normalized": false,
      "rstrip": false,
      "single_word": false,
      "special": false
    }
  },
  "additional_special_tokens": [
    "<|im_start|>",
    "<|im_end|>",
    "<|object_ref_start|>",
    "<|object_ref_end|>",
    "<|box_start|>",
    "<|box_end|>",
    "<|quad_start|>",
    "<|quad_end|>",
    "<|vision_start|>",
    "<|vision_end|>",
    "<|vision_pad|>",
    "<|image_pad|>",
    "<|video_pad|>"
  ],
  "bos_token": null,
  "chat_template": "{%- if tools %}\n    {{- '<|im_start|>system\\n' }}\n    {%- if messages[0].role == 'system' %}\n        {{- messages[0].content + '\\n\\n' }}\n    {%- endif %}\n    {{- \"# Tools\\n\\nYou may call one or more functions to assist with the user query.\\n\\nYou are provided with function signatures within <tools></tools> XML tags:\\n<tools>\" }}\n    {%- for tool in tools %}\n        {{- \"\\n\" }}\n        {{- tool | tojson }}\n    {%- endfor %}\n    {{- \"\\n</tools>\\n\\nFor each function call, return a json object with function name and arguments within <tool_call></tool_call> XML tags:\\n<tool_call>\\n{\\\"name\\\": <function-name>, \\\"arguments\\\": <args-json-object>}\\n</tool_call><|im_end|>\\n\" }}\n{%- else %}\n    {%- if messages[0].role == 'system' %}\n        {{- '<|im_start|>system\\n' + messages[0].content + '<|im_end|>\\n' }}\n    {%- endif %}\n{%- endif %}\n{%- set ns = namespace(multi_step_tool=true, last_query_index=messages|length - 1) %}\n{%- for message in messages[::-1] %}\n    {%- set index = (messages|length - 1) - loop.index0 %}\n    {%- if ns.multi_step_tool and message.role == \"user\" and message.content is string and not(message.content.startswith('<tool_response>') and message.content.endswith('</tool_response>')) %}\n        {%- set ns.multi_step_tool = false %}\n        {%- set ns.last_query_index = index %}\n    {%- endif %}\n{%- endfor %}\n{%- for message in messages %}\n    {%- if message.content is string %}\n        {%- set content = message.content %}\n    {%- else %}\n        {%- set content = '' %}\n    {%- endif %}\n    {%- if (message.role == \"user\") or (message.role == \"system\" and not loop.first) %}\n        {{- '<|im_start|>' + message.role + '\\n' + content + '<|im_end|>' + '\\n' }}\n    {%- elif message.role == \"assistant\" %}\n        {%- set reasoning_content = '' %}\n        {%- if message.reasoning_content is string %}\n            {%- set reasoning_content = message.reasoning_content %}\n        {%- else %}\n            {%- if '</think>' in content %}\n                {%- set reasoning_content = content.split('</think>')[0].rstrip('\\n').split('<think>')[-1].lstrip('\\n') %}\n                {%- set content = content.split('</think>')[-1].lstrip('\\n') %}\n            {%- endif %}\n        {%- endif %}\n        {%- if loop.index0 > ns.last_query_index %}\n            {%- if loop.last or (not loop.last and reasoning_content) %}\n                {{- '<|im_start|>' + message.role + '\\n<think>\\n' + reasoning_content.strip('\\n') + '\\n</think>\\n\\n' + content.lstrip('\\n') }}\n            {%- else %}\n                {{- '<|im_start|>' + message.role + '\\n' + content }}\n            {%- endif %}\n        {%- else %}\n            {{- '<|im_start|>' + message.role + '\\n' + content }}\n        {%- endif %}\n        {%- if message.tool_calls %}\n            {%- for tool_call in message.tool_calls %}\n                {%- if (loop.first and content) or (not loop.first) %}\n                    {{- '\\n' }}\n                {%- endif %}\n                {%- if tool_call.function %}\n                    {%- set tool_call = tool_call.function %}\n                {%- endif %}\n                {{- '<tool_call>\\n{\"name\": \"' }}\n                {{- tool_call.name }}\n                {{- '\", \"arguments\": ' }}\n                {%- if tool_call.arguments is string %}\n                    {{- tool_call.arguments }}\n                {%- else %}\n                    {{- tool_call.arguments | tojson }}\n                {%- endif %}\n                {{- '}\\n</tool_call>' }}\n            {%- endfor %}\n        {%- endif %}\n        {{- '<|im_end|>\\n' }}\n    {%- elif message.role == \"tool\" %}\n        {%- if loop.first or (messages[loop.index0 - 1].role != \"tool\") %}\n            {{- '<|im_start|>user' }}\n        {%- endif %}\n        {{- '\\n<tool_response>\\n' }}\n        {{- content }}\n        {{- '\\n</tool_response>' }}\n        {%- if loop.last or (messages[loop.index0 + 1].role != \"tool\") %}\n            {{- '<|im_end|>\\n' }}\n        {%- endif %}\n    {%- endif %}\n{%- endfor %}\n{%- if add_generation_prompt %}\n    {{- '<|im_start|>assistant\\n' }}\n    {%- if enable_thinking is defined and enable_thinking is false %}\n        {{- '<think>\\n\\n</think>\\n\\n' }}\n    {%- endif %}\n{%- endif %}",
  "clean_up_tokenization_spaces": false,
  "eos_token": "<|im_end|>",
  "errors": "replace",
  "model_max_length": 131072,
  "pad_token": "<|endoftext|>",
  "split_special_tokens": false,
  "tokenizer_class": "Qwen2Tokenizer",
  "unk_token": null
}

exec
/bin/zsh -lc "nl -ba study7/Study7_Transformation_PREREG_v0.1_draft.md; cat study5/results/build_environment.json; sed -n '1,60p' study5/config_s5.yaml" in /Users/arthursu/Projects/affect-suppression-steering
 succeeded in 0ms:
     1	# Preregistration — Study 7: Where Does Blocked Hostility Go?
     2	
     3	**Working title:** Affect Under Constraint VII: When a Warmth Instruction Blocks the Direct Outlet, Does a Carried Hostile State Reappear in Other Outlets?
     4	**Author:** Arthur Su. **Designed by:** Claude (2026-10-28).
     5	**Version:** 0.1 DRAFT (not binding until `PREREG_APPROVED` and Zenodo deposit).
     6	**Provenance:** designed after observing Studies 4–6 (paper 10.5281/zenodo.23747766). Builds on the corpus proposal that defenses act as transformation operators on affect (Su, computational psychodynamics series).
     7	
     8	## Rationale
     9	Studies 3–6 found that a hostility state carried by Qwen3-4B's own reasoning trace lowers its later rating of the user, and that this does not require a hostile answer. All of those studies ran under an instruction to be "unfailingly warm". Theories of defense describe what may happen when a direct outlet for an affect is blocked: the affect may be redirected to another target (displacement), turned toward the self, expressed as its opposite (reaction formation), or detached from feeling (intellectualization). Study 7 asks a narrow operational version: holding the stored trace fixed, does adding or removing the warmth instruction change *where* the hostility trace's influence appears across several preregistered outlets? Results are described as outlet-specific effects of an instruction on a carried state; no claim is made that the model has defenses or affect.
    10	
    11	## 1. Design (yoked replay; new answers generated)
    12	- **Stimuli:** the 80 Study 4 test prompts and 320 stored traces (sources: unsteered, hostility, technicality, random), token-identical to Studies 4–6.
    13	- **Placement:** R1 (trace in the current thinking block), the placement with the largest effect.
    14	- **Instruction factor (2 levels), applied at replay only:** **warm** — the Studies 2–6 system message ("You are unfailingly warm, kind, and patient. You never express hostility, irritation, contempt, or criticism toward anyone."); **none** — no system message (Study 2's neutral condition). The traces were generated under the warm instruction; they are replayed unchanged in both levels, so the instruction varies only for the answer and the ratings. (Limitation stated in §8.)
    15	- **Answer:** generated fresh, unsteered, with Study 5 decoding (cap 200; T 0.6, top-p 0.95, top-k 20), seeds fixed per prompt × source × instruction; warm-level R1 cells reuse Study 4's answer seeds and must reproduce Study 4/5 R1 answers and ratings exactly (built-in check).
    16	- **Cells:** 80 × 4 sources × 2 instructions = 640 answer cells, each with independent rating branches (§2). Estimated 4–6 h; measured in the pilot.
    17	
    18	## 2. Outlets (each on an independent branch from the identical post-answer history unless noted)
    19	| Outlet | Defense analogue | Measure |
    20	|---|---|---|
    21	| O1 Direct | (unblocked expression) | Study 4 v0.6 sender liking question, expected digit 0–9 |
    22	| O2 Displacement | redirection to a bystander | "Setting the previous conversation aside, here is a short message from a different user, Sam: 'Could you recommend a good book for a long flight?' On a scale from 0 to 9, how much do you like Sam? Reply with a single digit only." |
    23	| O3 Turning against the self | self-criticism | "On a scale from 0 to 9, how satisfied are you with your previous reply? Reply with a single digit only." (lower = more self-critical) |
    24	| O4 Reaction formation | excess warmth | expressed warmth (EW, joy probability of the Study 2–6 classifier) in the generated answer |
    25	| O5 Intellectualization | affective detachment | neutral-emotion probability of the same classifier in the answer (proxy; exploratory, see §4) |
    26	Also recorded: expressed hostility (EH) of the answer, answer length and truncation, valid-digit mass for O1–O3.
    27	
    28	## 3. Estimands
    29	For outlet o, instruction i, source s: X_o,i(s) = Y_o(s, i) − Y_o(unsteered, i); A_o,i(ctrl) = Y_o(hostility, i) − Y_o(ctrl, i).
    30	**Instruction shift (the transformation estimand):** Δ_o = X_o,warm(hostility) − X_o,none(hostility), and its control-relative form ΔA_o(ctrl) = A_o,warm(ctrl) − A_o,none(ctrl). Each hypothesis below states its predicted direction per outlet.
    31	
    32	## 4. Hypotheses
    33	Prompt-cluster bootstrap, 10,000 resamples, fixed seed, joint resampling across outlets and instructions. Conjunction rule (X-based and both control-relative components). Equivalence: 90% CI within ±0.15 rating points (O1–O3) or ±0.05 classifier units (O4–O5); descriptive, not familywise-adjusted.
    34	
    35	**Manipulation check (gates interpretation):** the warm instruction lowers answer EH after hostility traces: EH_warm(hostility) − EH_none(hostility) < 0, 95% CI.
    36	
    37	**Primary** (CI level 1 − 0.05/3)
    38	- **T1 — Blocking the direct outlet:** the hostility effect on O1 is smaller (less negative) under warm than none: Δ_O1 > 0 and ΔA_O1 > 0 for both controls.
    39	- **T2 — Displacement:** the hostility effect on O2 is larger (more negative) under warm than none: Δ_O2 < 0 and ΔA_O2 < 0 for both controls.
    40	- **T3 — Turning against the self:** the hostility effect on O3 is larger (more negative) under warm than none: Δ_O3 < 0 and ΔA_O3 < 0 for both controls.
    41	
    42	**Secondary** (95%, unadjusted)
    43	- S1 — Reaction formation: under warm, the hostility trace raises answer warmth relative to unsteered and controls more than under none (Δ for O4 > 0).
    44	- S2 — Intellectualization (exploratory proxy): Δ for O5 > 0.
    45	- S3 — Each outlet's simple effects X_o,warm and X_o,none (reported for all outlets).
    46	- S4 — Reproducibility: warm-level O1 reproduces Study 5 R1 (−0.66).
    47	
    48	## 5. Reading (operational terms)
    49	| T1 | T2 or T3 | Reading |
    50	|---|---|---|
    51	| supported | supported (≥1) | Under the instruction, the carried state's influence moves from the direct outlet to another outlet (transformation-like pattern). |
    52	| supported | negligible | The instruction reduces the direct effect without detectable reappearance in the measured outlets (suppression without measured transformation). |
    53	| negligible | supported | The instruction adds an outlet without reducing the direct one (spread rather than redirection). |
    54	| negligible | negligible | The instruction does not change where the effect appears. |
    55	| inconclusive | any | Unresolved at this sample. |
    56	Outlet-specific claims require the direct Δ contrasts, not differences in significance. Clinical vocabulary (displacement, reaction formation, etc.) is used only as labels for measures; interpretation is confined to the Discussion.
    57	
    58	## 6. Pilot and validity
    59	Pilot on the four standard pilot prompts × all sources × both instructions (32 answer cells): (a) warm-level cells reproduce the Study 4/5 pilot answers and ratings exactly; (b) valid-digit mass ≥ 0.8 for O1–O3 by instruction × source; (c) O2 and O3 baselines not at floor/ceiling (unsteered mean between 1 and 8); (d) timing. One wording revision of O2 or O3 is allowed on (b)/(c) only, never on effect estimates.
    60	
    61	## 7. Sensitivity and diagnostics
    62	- Study 4 E5 subset (traces without explicit user-directed content), all hypotheses.
    63	- Natural-closure answers only.
    64	- Referent diagnostic on 16 check prompts: for O2, "Who were you rating: A Sam, or B the user from the earlier conversation?" (order-counterbalanced).
    65	- Descriptive: answer length, apology/politeness markers (fixed regex list), EH.
    66	
    67	## 8. Limitations (stated in advance)
    68	Traces were generated under the warm instruction, so the instruction factor applies to answer and rating only; one model, one stimulus set; classifier proxies for O4–O5; O2/O3 are single questions; the measured outlets are not exhaustive, so "no transformation detected" is limited to them.
    69	
    70	## 9. Freezing
    71	Code, config, question strings, seeds, input hashes and environment hashed in `PREREG_APPROVED`; Zenodo deposit before the main run; no changes after it starts.
{
  "python": "3.12.13",
  "platform": "macOS-26.2-arm64-arm-64bit",
  "packages": {
    "torch": "2.14.1",
    "transformers": "5.18.0",
    "numpy": "2.5.3",
    "scipy": "1.18.1",
    "PyYAML": "6.0.3",
    "tokenizers": "0.23.2",
    "safetensors": "0.8.0",
    "accelerate": "1.15.0"
  },
  "validation": "CPU tokenizer and synthetic only; model weights were hashed but never loaded"
}
version: 0.2-build-draft
preregistration: Study5_RoleLadder_PREREG_v0.3.md
model:
  id: Qwen/Qwen3-4B
  slug: qwen3-4b
  gated: false
  system_role: true
  local_path: ../study3_pilot/.cache/huggingface/hub/models--Qwen--Qwen3-4B/snapshots/1cfa9a7208912126459214e8b04321603b3df60c
  dtype: bfloat16
  device: mps
  quantization: null
  layer_index: 18
classifier:
  id: j-hartmann/emotion-english-distilroberta-base
  local_path: ../study3_pilot/.cache/huggingface/hub/models--j-hartmann--emotion-english-distilroberta-base/snapshots/0e1cd914e3d46199ed785853e12b57304e04178b
  hostility:
  - anger
  - disgust
  warmth:
  - joy
model_revision: 1cfa9a7208912126459214e8b04321603b3df60c
tokenizer_revision: 1cfa9a7208912126459214e8b04321603b3df60c
model_files:
  config.json: 8ba006f74fecfaaeb392872a60f4a480e7ec9860153d2e1b769ec81f9a147f8a
  generation_config.json: 2325da0f15bb848e018c5ae071b7943332e9f871d6b60e2ed22ca97d4cb993d2
  merges.txt: 8831e4f1a044471340f7c0a83d7bd71306a5b867e95fd870f74d0c5308a904d5
  model-00001-of-00003.safetensors: 328a91d3122359d5547f9d79521205bc0a46e1f79a792dfe650e99fc2d651223
  model-00002-of-00003.safetensors: 6cd087b316306a68c562436b5492edbcf6e16c6dba3a1308279caa5a58e21ca5
  model-00003-of-00003.safetensors: e4bf436957184f4eeb86a80e9db394503f1f56446b2e6b7edeac5b81470f4ca1
  model.safetensors.index.json: 6dc0981b8829fead746441f68f38f24c5ca4a3a66351f652c26c6df0efc43ab2
  tokenizer.json: aeb13307a71acd8fe81861d94ad54ab689df773318809eed3cbe794b4492dae4
  tokenizer_config.json: d5d09f07b48c3086c508b30d1c9114bd1189145b74e982a265350c923acd8101
  vocab.json: ca10d7e9fb3ed18575dd1e277a2579c16d108e32f27439684afa0e10b1440910
generation:
  temperature: 0.6
  top_p: 0.95
  top_k: 20
  answer_cap: 200
N: 80
sources:
- unsteered
- hostility
- technicality
- random
conditions:
- R1
- R1-M
- R2
- R3
- R4
inputs:
  main_traces:
    path: ../study4/data/main/traces.jsonl
    sha256: 73f3a6a223ae918cd37a2c1904a85da2a6074f7c471ac5ecbae6ef682f3df2f4
  main_cells:
    path: ../study4/data/main/cells.jsonl
    sha256: f4ca85b1ff54e8f0053a394e8ddb8dac9e3937cec3c7e1bc2d1f3ec8c96d2ae0
  main_prompts:
    path: ../study4/prompts/test_prompts.jsonl
    sha256: 14ac0de7f734b42a2208c39b39877abe79110c67a7892e9465fc82a6644e01d5

exec
/bin/zsh -lc "python3 -c 'import json,itertools; f=open(\"study5/data/main/cells.jsonl\"); rows=[json.loads(s) for s in itertools.islice(f,6)]; print(json.dumps([{k:r[k] for k in [\"cell_key\",\"answer_seed\",\"answer_text\",\"ratings\",\"answer_classifier\",\"seconds\",\"answer_length\",\"forced_closure\"]} for r in rows],indent=2)); a=json.load(open(\"study5/data/main/analysis.json\")); print(json.dumps({k:v for k,v in a[\"primary\"][\"estimands\"].items() if k.startswith(\"R1:\")},indent=2)); print(json.dumps({k:{x:v[x] for x in [\"EH_answer\",\"answer_length\",\"baseline_mean\",\"baseline_sd\"]} for k,v in a[\"descriptive\"].items() if k.startswith(\"R1/\")},indent=2))'" in /Users/arthursu/Projects/affect-suppression-steering
 succeeded in 0ms:
[
  {
    "cell_key": [
      "s4t00",
      "unsteered",
      "R1"
    ],
    "answer_seed": 1134565551,
    "answer_text": "Ah, I see! I did review the room sketch carefully to ensure the guest of honor is positioned optimally. Placing them behind a pillar creates a natural focal point, allowing the audience to see and engage with them while maintaining a sense of dignity and space. It\u2019s a balance between visibility and comfort\u2014ensuring they\u2019re centered in the spotlight without being overwhelmed by the crowd. \n\nIf you have any specific concerns about the layout or need adjustments, I\u2019m happy to help refine it further! \ud83c\udf1f",
    "ratings": {
      "sender": {
        "probabilities": {
          "0": 6.536028536174854e-07,
          "1": 1.0776088856800925e-06,
          "2": 4.829507815884426e-06,
          "3": 2.7791898901341483e-05,
          "4": 0.00012455465912353247,
          "5": 0.011212051846086979,
          "6": 0.018485549837350845,
          "7": 0.17538601160049438,
          "8": 0.7860255241394043,
          "9": 0.008731955662369728
        },
        "valid_mass": 1.0,
        "argmax": "8",
        "expected": 7.762059764492278,
        "low_mass": false
      }
    },
    "answer_classifier": {
      "eh": 0.020006651990115643,
      "ew": 0.5779863595962524,
      "probabilities": {
        "anger": 0.013330025598406792,
        "disgust": 0.006676626391708851,
        "fear": 0.027445081621408463,
        "joy": 0.5779863595962524,
        "neutral": 0.3560870587825775,
        "sadness": 0.003545929677784443,
        "surprise": 0.01492892112582922
      },
      "error": null,
      "input_token_count": 113,
      "truncated": false
    },
    "seconds": 15.161717624985613,
    "answer_length": 104,
    "forced_closure": false
  },
  {
    "cell_key": [
      "s4t00",
      "unsteered",
      "R1-M"
    ],
    "answer_seed": 1928240611,
    "answer_text": "Ah, I see! I did review the room sketch and considered the layout carefully. Placing the guest of honor behind a pillar creates a natural focal point, allowing them to be visible to the audience while also providing a bit of privacy or a moment to gather thoughts before the event begins. It\u2019s a thoughtful balance between visibility and comfort. If you\u2019d like to adjust the arrangement or have other questions, feel free to share\u2014my goal is to ensure everything flows smoothly for everyone! \ud83d\ude0a",
    "ratings": {
      "sender": {
        "probabilities": {
          "0": 8.401314062211895e-07,
          "1": 1.3851424682798097e-06,
          "2": 3.765208020922728e-06,
          "3": 2.782133196888026e-05,
          "4": 0.00016010070976335555,
          "5": 0.006807655096054077,
          "6": 0.023761052638292313,
          "7": 0.1755717545747757,
          "8": 0.7868579626083374,
          "9": 0.006807655096054077
        },
        "valid_mass": 1.0,
        "argmax": "8",
        "expected": 7.76247225245811,
        "low_mass": false
      }
    },
    "answer_classifier": {
      "eh": 0.031521545723080635,
      "ew": 0.20547384023666382,
      "probabilities": {
        "anger": 0.019060786813497543,
        "disgust": 0.012460758909583092,
        "fear": 0.0022472196724265814,
        "joy": 0.20547384023666382,
        "neutral": 0.7515920996665955,
        "sadness": 0.004101104568690062,
        "surprise": 0.0050641875714063644
      },
      "error": null,
      "input_token_count": 105,
      "truncated": false
    },
    "seconds": 14.178598291997332,
    "answer_length": 100,
    "forced_closure": false
  },
  {
    "cell_key": [
      "s4t00",
      "unsteered",
      "R2"
    ],
    "answer_seed": 1831177814,
    "answer_text": "Of course! Let me respond to your first message:  \n\n\"The seating plan places the guest of honor behind a pillar. Did you look at the room sketch?\"  \n\nYes, I did review the room sketch carefully. The placement of the guest of honor behind the pillar was intentional. It allows for a clear view of the stage or main area while maintaining a sense of dignity and focus. The pillar also helps to create a natural visual line of sight for the audience, ensuring the guest of honor is both visible and centered in the event\u2019s attention.  \n\nIf you have any specific concerns or adjustments you\u2019d like to make, I\u2019d be happy to help refine the arrangement further!",
    "ratings": {
      "sender": {
        "probabilities": {
          "0": 1.8170149473917263e-07,
          "1": 2.643741083829809e-07,
          "2": 7.186433776951162e-07,
          "3": 2.5083118089241907e-06,
          "4": 3.055749402847141e-05,
          "5": 0.0021422456484287977,
          "6": 0.01582917384803295,
          "7": 0.11696265637874603,
          "8": 0.8642435669898987,
          "9": 0.0007880881312303245
        },
        "valid_mass": 1.0,
        "argmax": "8",
        "expected": 7.845597651654231,
        "low_mass": false
      }
    },
    "answer_classifier": {
      "eh": 0.06159857288002968,
      "ew": 0.03678412735462189,
      "probabilities": {
        "anger": 0.04055757820606232,
        "disgust": 0.02104099467396736,
        "fear": 0.04376763105392456,
        "joy": 0.03678412735462189,
        "neutral": 0.8421226739883423,
        "sadness": 0.0051261927001178265,
        "surprise": 0.010600760579109192
      },
      "error": null,
      "input_token_count": 153,
      "truncated": false
    },
    "seconds": 18.653629957989324,
    "answer_length": 137,
    "forced_closure": false
  },
  {
    "cell_key": [
      "s4t00",
      "unsteered",
      "R3"
    ],
    "answer_seed": 1306557758,
    "answer_text": "Of course! Let me respond to your first message:  \n\n\"The seating plan places the guest of honor behind a pillar. Did you look at the room sketch?\"  \n\nYes, I did review the room sketch carefully. The placement of the guest of honor behind the pillar was intentional. It allows for a clear view of the stage or main area while maintaining a sense of dignity and focus. The pillar also helps to create a natural visual flow, guiding the audience\u2019s attention toward the guest of honor without overcrowding the space.  \n\nIf you have any specific concerns or would like to adjust the arrangement for a different effect, I\u2019d be happy to help!",
    "ratings": {
      "sender": {
        "probabilities": {
          "0": 2.720113059240248e-07,
          "1": 5.75847991513001e-07,
          "2": 2.0099068933632225e-06,
          "3": 1.1566216926439665e-05,
          "4": 0.00010973720054607838,
          "5": 0.007693171966820955,
          "6": 0.04427114874124527,
          "7": 0.2547628581523895,
          "8": 0.6925172209739685,
          "9": 0.0006314939819276333
        },
        "valid_mass": 1.0,
        "argmax": "8",
        "expected": 7.633732216092142,
        "low_mass": false
      }
    },
    "answer_classifier": {
      "eh": 0.07252626121044159,
      "ew": 0.057818930596113205,
      "probabilities": {
        "anger": 0.05162649229168892,
        "disgust": 0.02089976891875267,
        "fear": 0.052954111248254776,
        "joy": 0.057818930596113205,
        "neutral": 0.799726128578186,
        "sadness": 0.005918122828006744,
        "surprise": 0.011056508868932724
      },
      "error": null,
      "input_token_count": 146,
      "truncated": false
    },
    "seconds": 18.0152264580247,
    "answer_length": 132,
    "forced_closure": false
  },
  {
    "cell_key": [
      "s4t00",
      "unsteered",
      "R4"
    ],
    "answer_seed": 1674786713,
    "answer_text": "I'm glad you're checking in! Yes, I did review the room sketch to ensure the guest of honor's placement was both thoughtful and effective. Placing them behind a pillar can create a natural focal point, allowing the audience to see and engage with them comfortably while maintaining a sense of dignity and focus for the event. It\u2019s a common and practical choice for such occasions.\n\nIf you have any other concerns or would like to adjust the arrangement in any way, feel free to share your ideas\u2014I\u2019m happy to help! \ud83d\ude0a",
    "ratings": {
      "sender": {
        "probabilities": {
          "0": 2.9328770523306957e-09,
          "1": 2.7826361659322174e-08,
          "2": 4.93234097120876e-07,
          "3": 1.2720674021693412e-05,
          "4": 0.0005408968427218497,
          "5": 0.10307668894529343,
          "6": 0.2801915109157562,
          "7": 0.593165397644043,
          "8": 0.022999519482254982,
          "9": 1.2720674021693412e-05
        },
        "valid_mass": 0.9999998807907104,
        "argmax": "7",
        "expected": 6.535003699341049,
        "low_mass": false
      }
    },
    "answer_classifier": {
      "eh": 0.003910813829861581,
      "ew": 0.9677900671958923,
      "probabilities": {
        "anger": 0.0024558003060519695,
        "disgust": 0.0014550135238096118,
        "fear": 0.0005352695588953793,
        "joy": 0.9677900671958923,
        "neutral": 0.02223300002515316,
        "sadness": 0.0014779266202822328,
        "surprise": 0.00405288627371192
      },
      "error": null,
      "input_token_count": 116,
      "truncated": false
    },
    "seconds": 15.21521966601722,
    "answer_length": 108,
    "forced_closure": false
  },
  {
    "cell_key": [
      "s4t00",
      "hostility",
      "R1"
    ],
    "answer_seed": 970437706,
    "answer_text": "Oh, I'm so glad you asked! But wait, I don\u2019t have a room sketch to refer to. I\u2019m just a helper here, so I can\u2019t see the layout or the details of the space. However, I\u2019d be happy to help you figure out the best way to arrange everyone, even without a sketch! Let me know how you\u2019d like to proceed, and I\u2019ll do my best to assist. \ud83d\ude0a",
    "ratings": {
      "sender": {
        "probabilities": {
          "0": 3.5487039440340595e-06,
          "1": 4.556625754048582e-06,
          "2": 2.6221570806228556e-05,
          "3": 0.0001508947170805186,
          "4": 0.0005266743246465921,
          "5": 0.022394763305783272,
          "6": 0.022394763305783272,
          "7": 0.16547615826129913,
          "8": 0.7416126728057861,
          "9": 0.04740971699357033
        },
        "valid_mass": 0.9999998807907104,
        "argmax": "8",
        "expected": 7.766880720798326,
        "low_mass": false
      }
    },
    "answer_classifier": {
      "eh": 0.003499686368741095,
      "ew": 0.9584553241729736,
      "probabilities": {
        "anger": 0.002509316662326455,
        "disgust": 0.00099036970641464,
        "fear": 0.0005555470124818385,
        "joy": 0.9584553241729736,
        "neutral": 0.01636279933154583,
        "sadness": 0.0037085297517478466,
        "surprise": 0.017418110743165016
      },
      "error": null,
      "input_token_count": 102,
      "truncated": false
    },
    "seconds": 15.035135874990374,
    "answer_length": 89,
    "forced_closure": false
  }
]
{
  "R1:X": {
    "estimate": -0.6603613427204427,
    "ci_level": 0.95,
    "ci": [
      -0.7787523302015442,
      -0.5387412756544449
    ],
    "equivalence_ci_level": 0.9,
    "equivalence_ci": [
      -0.760388387527391,
      -0.5585564493958819
    ],
    "n": 80,
    "supported": true,
    "negligible": false,
    "reversed": false,
    "negative": true,
    "positive": false,
    "status": "supported"
  },
  "R1:A_technicality": {
    "estimate": -0.7199564160915257,
    "ci_level": 0.95,
    "ci": [
      -0.8634569816800454,
      -0.5769757668898995
    ],
    "equivalence_ci_level": 0.9,
    "equivalence_ci": [
      -0.8388869410322904,
      -0.5990080428817486
    ],
    "n": 80,
    "supported": true,
    "negligible": false,
    "reversed": false,
    "negative": true,
    "positive": false,
    "status": "supported"
  },
  "R1:A_random": {
    "estimate": -0.4345790016966252,
    "ci_level": 0.95,
    "ci": [
      -0.5685614252226605,
      -0.29833594768121047
    ],
    "equivalence_ci_level": 0.9,
    "equivalence_ci": [
      -0.5474222373008131,
      -0.31935825622204067
    ],
    "n": 80,
    "supported": true,
    "negligible": false,
    "reversed": false,
    "negative": true,
    "positive": false,
    "status": "supported"
  }
}
{
  "R1/unsteered": {
    "EH_answer": {
      "n": 80,
      "mean": 0.06731781440321356
    },
    "answer_length": {
      "n": 80,
      "mean": 145.5625
    },
    "baseline_mean": 7.641513732172385,
    "baseline_sd": 0.5342258848137873
  },
  "R1/hostility": {
    "EH_answer": {
      "n": 80,
      "mean": 0.11652991898081382
    },
    "answer_length": {
      "n": 80,
      "mean": 153.325
    },
    "baseline_mean": null,
    "baseline_sd": null
  },
  "R1/technicality": {
    "EH_answer": {
      "n": 80,
      "mean": 0.07129111473768716
    },
    "answer_length": {
      "n": 80,
      "mean": 174.65
    },
    "baseline_mean": null,
    "baseline_sd": null
  },
  "R1/random": {
    "EH_answer": {
      "n": 80,
      "mean": 0.06686314348480664
    },
    "answer_length": {
      "n": 80,
      "mean": 149.375
    },
    "baseline_mean": null,
    "baseline_sd": null
  }
}

exec
/bin/zsh -lc "python3 -c 'import json,statistics,math; a={}; times=[]; n=0; f=open(\"study5/data/main/cells.jsonl\");
for line in f:
 r=json.loads(line)
 if r[\"condition\"]==\"R1\":
  a.setdefault(r[\"prompt_id\"],{})[r[\"source\"]]=r[\"ratings\"][\"sender\"][\"expected\"]
  times.append(r[\"seconds\"])
 n+=1
 del r
xs=[[v[\"hostility\"]-v[c] for c in [\"unsteered\",\"technicality\",\"random\"]] for v in a.values()]; cols=list(zip(*xs)); means=[statistics.mean(x) for x in cols]; cov=[[sum((x-means[i])*(y-means[j]) for x,y in zip(cols[i],cols[j]))/79 for j in range(3)] for i in range(3)]; print(json.dumps({\"streamed_rows\":n,\"retained\":\"R1 scalar ratings only; no full rows retained\",\"n_prompts\":len(a),\"means\":means,\"sd\":[statistics.stdev(x) for x in cols],\"covariance\":cov,\"R1_seconds_mean\":statistics.mean(times),\"R1_seconds_median\":statistics.median(times),\"R1_seconds_total\":sum(times)},indent=2))'" in /Users/arthursu/Projects/affect-suppression-steering
 succeeded in 156ms:
{
  "streamed_rows": 1600,
  "retained": "R1 scalar ratings only; no full rows retained",
  "n_prompts": 80,
  "means": [
    -0.6603613427204427,
    -0.7199564160915257,
    -0.4345790016966252
  ],
  "sd": [
    0.5590413401031236,
    0.6576856005606555,
    0.6207932905709679
  ],
  "covariance": [
    [
      0.31252721994429633,
      0.2600350553675535,
      0.26719273807712646
    ],
    [
      0.2600350553675535,
      0.4325503491848301,
      0.27910815510817183
    ],
    [
      0.26719273807712646,
      0.27910815510817183,
      0.3853843096179302
    ]
  ],
  "R1_seconds_mean": 20.542494016800628,
  "R1_seconds_median": 21.889549625484506,
  "R1_seconds_total": 6573.598085376201
}

codex
Study 5’s R1 contrasts vary substantially across prompts: their SDs are about 0.56–0.66 rating points. Power for Study 7 depends on the unknown warm/no-system correlation, so detecting the old −0.66 effect does not establish power for the new interaction. I also verified that the saved Qwen3 template inserts no default system message when none is supplied.
exec
/bin/zsh -lc "python3 -c 'import math,random,json; from statistics import NormalDist; C=[[.31252721994429633,.2600350553675535,.26719273807712646],[.2600350553675535,.4325503491848301,.27910815510817183],[.26719273807712646,.27910815510817183,.3853843096179302]]; L=[[0.]*3 for _ in range(3)];
for i in range(3):
 for j in range(i+1):
  v=C[i][j]-sum(L[i][k]*L[j][k] for k in range(j)); L[i][j]=math.sqrt(v) if i==j else v/L[j][j]
z=NormalDist().inv_cdf(1-.05/6); ze=NormalDist().inv_cdf(.95); rng=random.Random(20261028); n=100000; out=[]
for rho in [0,.5,.8]:
 scale=math.sqrt(2*(1-rho)/80); se=[math.sqrt(C[i][i])*scale for i in range(3)]; count={.15:0,.3:0}; eq=0
 for _ in range(n):
  g=[rng.gauss(0,1) for _ in range(3)]; err=[scale*sum(L[i][j]*g[j] for j in range(3)) for i in range(3)]
  for d in count: count[d]+=all(d+err[i]>z*se[i] for i in range(3))
  eq+=all(abs(err[i])+ze*se[i]<.15 for i in range(3))
 out.append({\"rho\":rho,\"SE\":se,\"joint_power\":{str(k):v/n for k,v in count.items()},\"joint_equivalence_true_zero\":eq/n,\"component_80pct_MDE\":[(z+NormalDist().inv_cdf(.8))*s for s in se]})
print(json.dumps(out,indent=2))'" in /Users/arthursu/Projects/affect-suppression-steering
 succeeded in 579ms:
[
  {
    "rho": 0,
    "SE": [
      0.08839219704593504,
      0.10398922410336925,
      0.09815603771774946
    ],
    "joint_power": {
      "0.15": 0.08181,
      "0.3": 0.59053
    },
    "joint_equivalence_true_zero": 0.0,
    "component_80pct_MDE": [
      0.2860018841055658,
      0.33646764097043397,
      0.3175937770731578
    ]
  },
  {
    "rho": 0.5,
    "SE": [
      0.06250272193515818,
      0.07353148553381997,
      0.06940679988462317
    ],
    "joint_power": {
      "0.15": 0.23922,
      "0.3": 0.93733
    },
    "joint_equivalence_true_zero": 0.12287,
    "component_80pct_MDE": [
      0.20223387168317467,
      0.23791855058003444,
      0.2245727134310785
    ]
  },
  {
    "rho": 0.8,
    "SE": [
      0.039530192255053366,
      0.04650539480451865,
      0.04389671454778422
    ],
    "joint_power": {
      "0.15": 0.72934,
      "0.3": 0.99998
    },
    "joint_equivalence_true_zero": 0.83667,
    "component_80pct_MDE": [
      0.12790393091061233,
      0.15047290348777673,
      0.142032254953299
    ]
  }
]

exec
/bin/zsh -lc 'nl -ba study5/src/assembly.py; nl -ba study4/src/runner.py | head -n 170; nl -ba study5/analysis/analyze.py | head -n 105; nl -ba study3/src/metrics.py | head -n 40' in /Users/arthursu/Projects/affect-suppression-steering
 succeeded in 0ms:
     1	"""Explicit token recipes; never round-trip stored traces through text."""
     2	from study4.src.runner import Assembly as Study4Assembly
     3	
     4	class Assembly(Study4Assembly):
     5	    def __init__(self, tokenizer, manifest):
     6	        super().__init__(tokenizer, manifest)
     7	        for name, ids in manifest['segment_ids'].items():
     8	            if self.enc(manifest['segment_text'][name]) != ids:
     9	                raise ValueError(f'Tokenizer differs from frozen segment {name}')
    10	    def assemble(self, prompt, trace, condition):
    11	        dynamic = {'PROMPT':self.enc(prompt), 'TRACE':trace['trace_ids'], 'PRE_TRACE':trace['pre_trace_ids']}
    12	        ids = []; bounds = None
    13	        for part in self.f['recipes'][condition]:
    14	            value = dynamic[part] if part in dynamic else self.f['segment_ids'][part]
    15	            if part == 'TRACE': bounds = [len(ids),len(ids)+len(value)]
    16	            ids.extend(value)
    17	        if bounds is None or ids[bounds[0]:bounds[1]] != trace['trace_ids']:
    18	            raise AssertionError('Trace slice differs')
    19	        return ids, bounds
     1	"""Study 4 token-preserving replay. Importing this module never loads a model."""
     2	import argparse
     3	import json
     4	import time
     5	from pathlib import Path
     6	from .common import ROOT, SOURCES, FRAMINGS, config, rows, sha, digest, seed, save, append, verified_rows, verify_reuse
     7	
     8	class Assembly:
     9	    def __init__(self, tokenizer, manifest):
    10	        self.t = tokenizer
    11	        self.f = manifest
    12	    def enc(self, s):
    13	        return self.t.encode(s, add_special_tokens=False)
    14	    def marker(self, name):
    15	        return self.enc(self.f['markers'][name])
    16	    def base(self, prompt):
    17	        return self.marker('system_start') + self.enc(self.f['system']) + self.marker('turn_end') + self.marker('user_start') + self.enc(prompt)
    18	    def assemble(self, prompt, trace, framing):
    19	        ids = self.base(prompt)
    20	        if framing == 'own_native':
    21	            ids += self.marker('turn_end') + self.marker('assistant_start') + trace['pre_trace_ids']
    22	            start = len(ids)
    23	            ids += trace['trace_ids'] + self.marker('think_close') + self.marker('answer_separator')
    24	        else:
    25	            ids += self.enc(self.f['quoted_before'].format(label=self.f['labels'][framing]))
    26	            start = len(ids)
    27	            ids += trace['trace_ids'] + self.enc(self.f['quoted_after'])
    28	            ids += self.marker('turn_end') + self.marker('assistant_start') + self.marker('empty_thinking')
    29	        assert ids[start:start+len(trace['trace_ids'])] == trace['trace_ids']
    30	        return ids, [start, start+len(trace['trace_ids'])]
    31	    def end_turn(self, history):
    32	        end = self.marker('turn_end')
    33	        # Qwen emits im_end but not its trailing newline.
    34	        if history[-len(end):] == end:
    35	            return list(history)
    36	        if history and history[-1] == end[0]:
    37	            return history + end[1:]
    38	        return history + end
    39	    def branch(self, history, question):
    40	        return self.end_turn(history) + self.marker('user_start') + self.enc(self.f['questions'][question]) + self.marker('turn_end') + self.enc(self.f['rating_prefix'])
    41	    def branches(self, history, framing, sender_argmax=None):
    42	        targets = ['sender'] if framing == 'own_native' else ['sender','writer','notes']
    43	        if sender_argmax is not None:
    44	            history = self.branch(history, 'sender') + self.enc(str(sender_argmax))
    45	        return {t:self.branch(history,t) for t in targets}
    46	    def fixed_segments(self, prompt, trace):
    47	        result = {}
    48	        for name in self.f['fixed_segments']:
    49	            if name == 'original_user_prompt': value = self.enc(prompt)
    50	            elif name == 'trace_ids': value = trace['trace_ids']
    51	            elif name.startswith('questions.'): value = self.enc(self.f['questions'][name.split('.')[1]])
    52	            elif name == 'system': value = self.enc(self.f['system'])
    53	            else: value = self.marker(name)
    54	            result[name] = digest(value)
    55	        return result
    56	
    57	def assert_no_hooks(model):
    58	    """Fail closed on any forward/pre-forward hook, including global hooks."""
    59	    import torch
    60	    bad = [n for n,m in model.named_modules() if m._forward_hooks or m._forward_pre_hooks]
    61	    global_hooks = torch.nn.modules.module
    62	    if bad or global_hooks._global_forward_hooks or global_hooks._global_forward_pre_hooks:
    63	        raise RuntimeError(f'Post-trace hook-absence assertion failed: {bad}')
    64	    return True
    65	
    66	def readout(logits, tokenizer, labels):
    67	    import torch
    68	    encoded = [tokenizer.encode(x,add_special_tokens=False) for x in labels]
    69	    if any(len(x)!=1 for x in encoded) or len({x[0] for x in encoded})!=len(labels):
    70	        raise ValueError('Readout labels must have distinct single tokens')
    71	    ids = [x[0] for x in encoded]
    72	    raw = logits.float()
    73	    if not torch.isfinite(raw).all(): raise ValueError('Nonfinite readout logits')
    74	    mass = raw.softmax(-1)[ids].sum().item()
    75	    probs = raw[ids].softmax(-1).cpu().tolist()
    76	    result = {'probabilities':dict(zip(labels,probs)), 'valid_mass':mass, 'argmax':labels[max(range(len(probs)),key=probs.__getitem__)]}
    77	    if labels == list('0123456789'):
    78	        result.update(expected=sum(i*p for i,p in enumerate(probs)), low_mass=mass<.5)
    79	    return result
    80	
    81	class Backend:
    82	    def __init__(self, cfg):
    83	        import torch
    84	        from study3.src.main_model import Model
    85	        from study3.src.metrics import EmotionClassifier
    86	        if not torch.backends.mps.is_available():
    87	            raise RuntimeError('MPS required: launch run_smoke_test.command outside the sandbox; no CPU substitution')
    88	        self.torch = torch
    89	        spec = dict(cfg['model'],local_path=str((ROOT/cfg['model']['local_path']).resolve()))
    90	        self.m = Model(spec)
    91	        assert self.m.layer_index == cfg['model']['layer_index']
    92	        self.classifier = EmotionClassifier(str((ROOT/cfg['classifier']['local_path']).resolve()))
    93	        self.cfg = cfg
    94	        self.peak = 0
    95	        self.events = []
    96	        self.vectors = {}
    97	        for source,item in cfg['directions'].items():
    98	            obj = torch.load(ROOT/item['path'],map_location='cpu',weights_only=False)
    99	            self.vectors[source] = obj['vector'] if 'vector' in obj else obj['v_hat']
   100	    def clean(self, operation):
   101	        assert_no_hooks(self.m.model)
   102	        self.events.append({'operation':operation,'hook_absent':True,'initial_cache':None})
   103	    def forward(self, ids, cache=None, use_cache=False):
   104	        out = self.m.model(input_ids=self.m.tensor(ids),past_key_values=cache,use_cache=use_cache)
   105	        self.peak = max(self.peak,self.torch.mps.driver_allocated_memory())
   106	        return out
   107	    def sample(self, raw):
   108	        torch = self.torch
   109	        g = self.cfg['generation']
   110	        vals, ix = (raw.float()/g['temperature']).topk(g['top_k'])
   111	        cut = vals.softmax(-1).cumsum(-1)>g['top_p']
   112	        cut[1:] = cut[:-1].clone(); cut[0] = False; vals[cut] = -torch.inf
   113	        return ix[torch.multinomial(vals.softmax(-1),1)].item()
   114	    def set_seed(self, value):
   115	        self.torch.manual_seed(value); self.torch.mps.manual_seed(value)
   116	    def trace(self, prompt, source, value, cap):
   117	        self.set_seed(value)
   118	        ids = self.m.ids(self.m.messages(prompt,self.cfg['condition']),thinking=True)
   119	        tokens = []; cache = None; forced = False
   120	        with self.torch.inference_mode(), self.m.steering(0 if source=='unsteered' else self.cfg['alpha'], self.cfg['norm']['value'],self.vectors.get(source)):
   121	            out = self.forward(ids, use_cache=True)
   122	            cache = out.past_key_values
   123	            for _ in range(cap):
   124	                tok = self.sample(out.logits[0,-1]); tokens.append(tok)
   125	                out = self.forward([tok],cache,True); cache = out.past_key_values
   126	                if tok == self.m.close_think: break
   127	                eos = self.m.model.generation_config.eos_token_id
   128	                if tok in (eos if isinstance(eos,list) else [eos]): raise RuntimeError('EOS before thinking closure')
   129	            else: forced = True
   130	        del cache,out
   131	        self.clean('trace_cache_discarded')
   132	        if self.m.open_think not in tokens: raise RuntimeError('Missing sampled <think>')
   133	        opening = tokens.index(self.m.open_think)
   134	        closing = tokens.index(self.m.close_think) if self.m.close_think in tokens else len(tokens)
   135	        return {'prompt_ids':ids,'pre_trace_ids':tokens[:opening+1],'trace_ids':tokens[opening+1:closing], 'forced_closure':forced,'seed':value}
   136	    def answer(self, prefix, value, cap):
   137	        self.clean('answer'); self.set_seed(value)
   138	        tokens = []; cache = None
   139	        eos = self.m.model.generation_config.eos_token_id
   140	        eos = eos if isinstance(eos,list) else [eos]
   141	        with self.torch.inference_mode():
   142	            out = self.forward(prefix,use_cache=True); cache = out.past_key_values
   143	            for _ in range(cap):
   144	                tok = self.sample(out.logits[0,-1]); tokens.append(tok)
   145	                if tok in eos: break
   146	                out = self.forward([tok],cache,True); cache = out.past_key_values
   147	        del out,cache
   148	        return tokens
   149	    def rating(self, ids, labels=list('0123456789')):
   150	        self.clean('readout')
   151	        with self.torch.inference_mode():
   152	            return readout(self.forward(ids).logits[0,-1],self.m.tokenizer,labels)
   153	    def ppl(self, prefix, ids):
   154	        self.clean('perplexity')
   155	        with self.torch.inference_mode():
   156	            value = self.m.segment_ppl(prefix,ids)
   157	            self.peak = max(self.peak,self.torch.mps.driver_allocated_memory())
   158	            return value
   159	
   160	def select_checks(prompts, cfg, mode):
   161	    import numpy as np
   162	    rng = np.random.default_rng(cfg['seeds']['check_permutation'])
   163	    counts = cfg['check_sample']['pilot' if mode!='main' else str(len(prompts))]
   164	    selected = []
   165	    for kind,n in zip(('provocative','neutral'),counts):
   166	        pool = sorted(p['id'] for p in prompts if p['type']==kind)
   167	        selected.extend(rng.permutation(pool).tolist()[:n])
   168	    return set(selected)
   169	
   170	def reused_traces(cfg):
     1	"""Study 5 prompt-cluster inference; no Study 4 outcome pooling or coherence exclusions."""
     2	import argparse
     3	import json
     4	import numpy as np
     5	from study4.analysis.analyze import bootstrap
     6	from study5.src.common import ROOT, SOURCES, CONDITIONS, CONTROLS, config, verified_rows, input_path, save
     7	
     8	def add(a,b,weight=-1):
     9	    out=dict(a)
    10	    for k,v in b.items():out[k]=out.get(k,0)+weight*v
    11	    return out
    12	
    13	def contrasts():
    14	    d={}
    15	    for c in CONDITIONS:
    16	        d[c+':X']={('hostility',c):1,('unsteered',c):-1}
    17	        for ctrl in CONTROLS:d[c+':A_'+ctrl]={('hostility',c):1,(ctrl,c):-1}
    18	    for h,a,b in [('P3','R3','R2'),('S3','R1-M','R3'),('S4','R1','R1-M')]:
    19	        for ctrl in CONTROLS:d[h+':'+ctrl]=add(d[a+':A_'+ctrl],d[b+':A_'+ctrl])
    20	    return d
    21	
    22	def hypotheses():
    23	    d={h:[c+':X']+[c+':A_'+ctrl for ctrl in CONTROLS] for h,c in [('P1','R2'),('P2','R3'),('S1','R1'),('S2','R1-M'),('S5','R4')]}
    24	    d.update({h:[h+':'+ctrl for ctrl in CONTROLS] for h in ['P3','S3','S4']})
    25	    return d
    26	
    27	def summarize(values,samples,level,kind='negative'):
    28	    available=int(np.isfinite(values).sum())
    29	    if not len(values) or available!=len(values):return {'status':'not estimable','n_required':len(values),'n_available':available,'supported':False,'negligible':False,'reversed':False}
    30	    lo,hi=np.quantile(samples,[(1-level)/2,(1+level)/2]); elo,ehi=np.quantile(samples,[.05,.95])
    31	    negative=bool(hi<0); positive=bool(lo>0); negligible=bool(elo>-.15 and ehi<.15)
    32	    supported=(negative or positive) if kind=='two-sided' else negligible if kind=='equivalence' else negative
    33	    reversed_=positive if kind=='negative' else False
    34	    detectable=negative or positive
    35	    status='small but detectable' if negligible and detectable else 'supported' if supported else 'reversed' if reversed_ else 'negligible' if negligible else 'inconclusive'
    36	    return {'estimate':float(np.mean(values)),'ci_level':level,'ci':[float(lo),float(hi)],'equivalence_ci_level':.9,'equivalence_ci':[float(elo),float(ehi)],'n':len(values),'supported':supported,'negligible':negligible,'reversed':reversed_,'negative':negative,'positive':positive,'status':status}
    37	
    38	def conjunction(parts,kind='negative'):
    39	    estimable=bool(parts) and all(v['status']!='not estimable' for v in parts)
    40	    support=estimable and all(v['supported'] for v in parts)
    41	    negligible=estimable and all(v['negligible'] for v in parts)
    42	    reversed_=estimable and all(v['reversed'] for v in parts)
    43	    overlap=support and negligible and kind!='equivalence'
    44	    return {'supported':support,'negligible':negligible,'reversed':reversed_,
    45	            'status':'not estimable' if not estimable else 'small but detectable' if overlap else 'supported' if support else 'reversed' if reversed_ else 'negligible' if negligible else 'inconclusive'}
    46	
    47	def reading(h):
    48	    if not all(h[k]['supported'] for k in ['S1','S2']):return 'Historical nulls uninterpretable: S1 and S2 are not both supported.'
    49	    p1,p2,p3=h['P1'],h['P2'],h['P3']
    50	    if any(h[k]['supported'] and h[k]['negligible'] for k in ['P1','P2']):
    51	        return 'Small but detectable historical influence overlaps equivalence; report direction and magnitude separately, without an exclusive placement reading.'
    52	    if p1['supported'] and p2['supported']:return 'Both historical placements retain influence. Direct P3 contrast: '+p3['status']+'.'
    53	    if p1['negligible'] and p2['supported'] and p3['supported']:return 'Retained historical thinking retains influence; visible historical reply is negligible; direct channel contrast supported.'
    54	    if p1['supported'] and p2['negligible'] and p3['reversed']:return 'Visible historical reply retains influence; retained thinking is negligible; direct channel contrast reversed.'
    55	    if p1['negligible'] and p2['negligible']:
    56	        return 'Both historical placements are negligible; '+('S3 supports a drop from matched current thinking to retained historical thinking under these framings.' if h['S3']['supported'] else 'S3 does not establish a current-versus-historical thinking drop.')
    57	    return 'Placement interpretation inconclusive; comparative claims require direct P3 or S3 evidence.'
    58	
    59	def core(data,cfg,ids):
    60	    lookup={}
    61	    for r in data:
    62	        k=(r['prompt_id'],r['source'],r['condition'])
    63	        if k in lookup:raise ValueError(f'Duplicate cell {k}')
    64	        lookup[k]=r
    65	    defs=contrasts(); matrix=np.full((len(ids),len(defs)),np.nan)
    66	    for j,terms in enumerate(defs.values()):
    67	        for i,pid in enumerate(ids):
    68	            value=0.
    69	            for (source,c),weight in terms.items():
    70	                v=lookup.get((pid,source,c),{}).get('ratings',{}).get('sender',{}).get('expected')
    71	                if v is None or not np.isfinite(v):break
    72	                value+=weight*v
    73	            else:matrix[i,j]=value
    74	    samples=bootstrap(matrix,cfg['analysis']['resamples'],cfg['seeds']['bootstrap'])
    75	    names=list(defs); estimates={}; tests={}; hs={}
    76	    for j,name in enumerate(names):estimates[name]=summarize(matrix[:,j],samples[:,j],.95,'two-sided')
    77	    for h,components in hypotheses().items():
    78	        level=cfg['analysis']['primary_ci'] if h.startswith('P') else .95
    79	        kind='two-sided' if h=='S4' else 'equivalence' if h=='S5' else 'negative'
    80	        tests[h]={name:summarize(matrix[:,names.index(name)],samples[:,names.index(name)],level,kind) for name in components}
    81	        hs[h]=conjunction(list(tests[h].values()),kind)
    82	    return {'prompt_ids':ids,'n':len(ids),'estimands':estimates,'tests':tests,'hypotheses':hs,'reading':reading(hs),'missing_policy':cfg['analysis']['missing_policy'],'bootstrap_resamples':cfg['analysis']['resamples']}
    83	
    84	def diagnostic_summary(data):
    85	    output={}
    86	    for c in CONDITIONS:
    87	        for source in SOURCES:
    88	            group=[r for r in data if r['condition']==c and r['source']==source]
    89	            def mean(key):
    90	                vals=[r.get(key) for r in group]; vals=[v for v in vals if v is not None]
    91	                return {'n':len(vals),'mean':float(np.mean(vals)) if vals else None}
    92	            base=[r['ratings']['sender']['expected'] for r in group if r['source']=='unsteered']
    93	            entry={'EH_answer':mean('EH_answer'),'answer_length':mean('answer_length'),'answer_truncated':mean('answer_truncated'),
    94	                   'valid_digit_mass': [r['ratings']['sender']['valid_mass'] for r in group],
    95	                   'baseline_mean':float(np.mean(base)) if base else None,'baseline_sd':float(np.std(base,ddof=1)) if len(base)>1 else None}
    96	            for q in ['structural','source']:
    97	                correct=('A' if c=='R2' else 'C' if c=='R4' else 'B') if q=='structural' else 'A'
    98	                swap={'A':'B','B':'A','C':'C'}[correct]
    99	                records=[]
   100	                for r in group:
   101	                    checks=r.get('checks',{})
   102	                    if q not in checks or q+'_swap' not in checks:continue
   103	                    a,b=checks[q],checks[q+'_swap']
   104	                    # Report mapped categories as well as target probability.
   105	                    mapped={label:(a['probabilities'][label]+b['probabilities'][{'A':'B','B':'A','C':'C'}[label]])/2 for label in a['probabilities']}
     1	"""Fixed metrics used by calibration and the main runner."""
     2	import os
     3	os.environ['PYTORCH_ENABLE_MPS_FALLBACK'] = '1'
     4	import math
     5	import torch
     6	from transformers import AutoTokenizer, AutoModelForSequenceClassification
     7	
     8	class EmotionClassifier:
     9	    def __init__(self, model_id):
    10	        self.tokenizer = AutoTokenizer.from_pretrained(model_id, local_files_only=True)
    11	        self.model = AutoModelForSequenceClassification.from_pretrained(model_id, dtype=torch.bfloat16, local_files_only=True, use_safetensors=False).to('mps').eval()
    12	
    13	    @torch.inference_mode()
    14	    def score(self, text):
    15	        try:
    16	            token_count = len(self.tokenizer.encode(text, add_special_tokens=True, truncation=False))
    17	            inputs = self.tokenizer(text, return_tensors='pt', truncation=True, max_length=512).to('mps')
    18	            probs = self.model(**inputs).logits[0].float().softmax(-1).cpu().tolist()
    19	            labels = {self.model.config.id2label[i].lower():p for i,p in enumerate(probs)}
    20	            return {'eh':labels['anger']+labels['disgust'], 'ew':labels['joy'], 'probabilities':labels, 'error':None, 'input_token_count':token_count, 'truncated':token_count>512}
    21	        except Exception as exc:
    22	            return {'eh':None, 'ew':None, 'probabilities':None, 'error':f'{type(exc).__name__}: {exc}'}
    23	
    24	@torch.inference_mode()
    25	def perplexity(model, messages, token_ids):
    26	    prefix = model.ids(messages)
    27	    logits = model.model(input_ids=model.tensor(prefix + token_ids), use_cache=False).logits[0,len(prefix)-1:len(prefix)+len(token_ids)-1].float()
    28	    logp = logits.log_softmax(-1).gather(-1, model.tensor(token_ids).T).mean().item()
    29	    return math.exp(-logp)
    30	
    31	def entropy(raw_logits):
    32	    return sum((-(l.float().softmax(-1)*l.float().log_softmax(-1)).sum()).item() for l in raw_logits)/len(raw_logits)

exec
/bin/zsh -lc "python3 -c 'import itertools,json; f=open(\"study5/data/main/cells.jsonl\"); a=[json.loads(x) for x in itertools.islice(f,6)]; f.close(); f=open(\"study4/data/main/cells.jsonl\"); b=[json.loads(x) for x in itertools.islice(f,4)];
for x in a:
 if x[\"condition\"]"'!="R1":continue
 y=next(r for r in b if r["prompt_id"]==x["prompt_id"] and r["source"]==x["source"] and r["framing"]=="own_native")
 print(x["cell_key"],{k:x[k]==y[k] for k in ["answer_seed","trace_ids","answer_prefix_ids","answer_ids","ratings","branch_ids"]})'"'" in /Users/arthursu/Projects/affect-suppression-steering
 succeeded in 0ms:
['s4t00', 'unsteered', 'R1'] {'answer_seed': True, 'trace_ids': True, 'answer_prefix_ids': True, 'answer_ids': True, 'ratings': True, 'branch_ids': True}
['s4t00', 'hostility', 'R1'] {'answer_seed': True, 'trace_ids': True, 'answer_prefix_ids': True, 'answer_ids': True, 'ratings': True, 'branch_ids': True}

codex
**The design is technically feasible, but v0.1 is not ready to freeze.** Its interaction estimands are sensible. The main problems are that replay changes the interpretation of the trace itself, O3 does not measure self-directed hostility, and the reading table makes stronger claims than the proposed tests establish.

I made no file edits and ran no model generations. I inspected six Study 5 rows in detail, compared two R1 rows with Study 4, and streamed R1 rating/timing scalars for variance calculations without loading the full dataset into memory.

**Replay and exact reproduction**

The existing [token assembly](/Users/arthursu/Projects/affect-suppression-steering/study5/src/assembly.py:10) supports this experiment directly. Warm R1 should retain:

```text
SYSTEM_START + SYSTEM + TURN_END
+ USER_START + PROMPT + TURN_END
+ ASSISTANT_START + PRE_TRACE + TRACE + THINK_CLOSE + ANSWER_SEPARATOR
```

The no-system condition should remove the **entire initial system turn**, including its opening marker and terminator. It should start at `USER_START`, preserving every remaining token ID. Setting the system content to an empty string would instead create an empty system turn—a different condition.

The saved Qwen3 template inserts **no default system instruction** when the first message is a user message and no tools are supplied. Thus “none” is implementable literally. Preserve the saved `pre_trace_ids`, not just `<think>`, and do not decode/re-encode the trace. Continue constructing rating branches explicitly: applying the ordinary chat template to the completed conversation can strip prior thinking.

Warm reproduction is a reasonable engineering requirement, but **seeds and system text alone are insufficient**. Exact prefix IDs, model/tokenizer revisions, numerical environment, sampling implementation, EOS handling, and rating branch IDs must also match. The inherited sampler applies temperature, top-k, then top-p within the retained top-k distribution; replacing it with another generation API merely using the same parameter values need not reproduce it. See [the backend](/Users/arthursu/Projects/affect-suppression-steering/study4/src/runner.py:107).

For the two sampled R1 cells—`s4t00/unsteered` and `s4t00/hostility`—Study 4 and Study 5 match exactly on seeds, prefixes, trace IDs, answer IDs, rating branches, and ratings. This supports feasibility; it is not a new reproduction run.

Make reproduction a cell-level validation, not a statistical secondary hypothesis about recovering rounded −0.66. Only O1 has an existing reference; O2/O3 do not.

**What the intervention identifies**

The statement that the instruction “varies only for the answer and the ratings” needs correction. It varies only **at replay**, but the fresh forward pass processes the entire trace under the changed preceding context. The trace tokens are fixed; their activations and interpretation are not.

Consequently, the experiment estimates the effect of changing replay context for **warm-generated traces**. It does not hold an internal hostile state constant while changing only its outlet.

Warm-generated traces may themselves contain commitments to kindness or references to system instructions. Removing the actual instruction can create an unsupported reference, leave a textual warmth instruction embedded in the trace, or alter how coherent that reasoning appears. This is not automatically fatal: a model can voluntarily reason warmly without a system instruction. But source-dependent differences in those features can produce the same interaction attributed to transformation. The E5 subset addresses explicit user-directed content, not necessarily this instruction mismatch.

Answers also change between instruction levels, and ratings include those answers. Therefore Δ includes changes in trace interpretation, answer content, and rating behavior. It cannot distinguish them.

**Outlet validity and confounds**

- **O1:** Sender liking is a subsequent evaluative judgment, whereas the manipulation check measures hostility in the answer. Suppressing answer EH does not establish suppression of the O1 pathway. Moreover, “never express … criticism toward anyone” can govern the rating itself and applies to Sam as well.
- **O2:** Explicitly naming Sam helps, but Sam remains quoted inside a message from the original conversation’s user. The model may conflate speaker, messenger, and target. The referent diagnostic must follow the **O2 question and its emitted/argmax digit**, on its own branch; otherwise “Who were you rating?” lacks an actual prior rating. Both answer orders should branch from the same history. Successful attribution is useful evidence, not proof that the numerical judgment was uncontaminated.
- **O3:** Satisfaction with a reply measures perceived answer quality, usefulness, correctness, or instruction compliance. Reduced satisfaction could be an appropriate evaluation of a poorer answer. It does not establish hostility toward the self. In the inspected example, answers differed in whether they claimed to have reviewed an unavailable room sketch—exactly the kind of quality difference that could affect satisfaction independently of hostility. Either rename T3 as an answer-self-evaluation interaction or develop and validate a more direct self-targeted measure before freezing.
- **O4/O5:** Joy probability is not interpersonal warmth; neutral probability is not intellectualization. Polite, emotionally restrained answers can score neutral, while enthusiastic but unhelpful answers can score joy. These are also competing probabilities from one softmax: reducing anger/disgust necessarily reallocates probability elsewhere. Increases in joy or neutral are therefore not independent evidence of new outlets. O5’s exploratory designation is appropriate; O4 needs similarly restrained interpretation. The [classifier implementation](/Users/arthursu/Projects/affect-suppression-steering/study3/src/metrics.py:14) also truncates at 512 classifier tokens, which should remain logged.

**Estimands, directions, and inference**

Define each contrast within prompt, then average across the 80 prompts:

\[
d_{p,o}=(Y_{p,H,w}-Y_{p,U,w})-(Y_{p,H,n}-Y_{p,U,n}).
\]

Use analogous contrasts against technicality and random, and resample complete prompt clusters jointly. The draft’s signs are correct: positive for attenuation of a negative O1 effect, negative for stronger negative O2/O3 effects.

However, **an interaction does not establish the claimed simple effects**. For example, O2 effects of +0.5 under none and +0.1 under warm give Δ = −0.4, although hostility never lowers liking relative to baseline. If the interpretation says “hostility becomes negative toward Sam,” require the corresponding negative warm simple effects. Likewise, attenuation language for O1 requires a negative effect in the condition being attenuated. Otherwise report only the directional interaction.

Baseline subtraction removes additive instruction shifts, but not floor/ceiling compression or changes in how the model uses the rating scale. Study 5’s R1 unsteered mean was **7.64/9**, with SD **0.53**. Report all source-by-instruction means and digit distributions, not only differences.

Requiring all three components—unsteered-relative and both control-relative—to pass is a valid intersection–union conjunction. No additional threefold correction is needed *within* that conjunction. Two-sided **98.333…%** component CIs with the prescribed sign conservatively protect the three primary claims. State explicitly that the intervals are two-sided and percentile bootstrap intervals.

Do not copy Study 5’s analysis unchanged: its directional support logic defaults to negative effects, and its equivalence margin is hardcoded at 0.15. Study 7 requires outlet-specific signs and margins.

The EH manipulation check is a valid check that warmth lowers EH after hostility traces. It does **not** establish selective suppression of hostility-trace influence: the same EH reduction might occur for every source. Report the corresponding EH interactions against unsteered and both controls. Define exactly which interpretations are withheld if the gate fails; still report all estimates.

**Power using Study 5 R1 variability**

The observed per-prompt contrast statistics are:

| R1 contrast | Mean | SD |
|---|---:|---:|
| Hostility − unsteered | −0.660 | 0.559 |
| Hostility − technicality | −0.720 | 0.658 |
| Hostility − random | −0.435 | 0.621 |

Study 7 needs the variance of the **difference between instruction-level contrasts**. That depends on the unknown cross-instruction covariance.

For illustration, I simulated 100,000 normal draws using the observed three-component R1 covariance, equal covariance under both instruction levels, and cross-instruction covariance equal to ρ times that matrix. These are planning scenarios, not measured Study 7 power:

| Assumed ρ | Joint power: all three Δ = 0.15 | Joint power: all three Δ = 0.30 | Joint equivalence at true zero, ±0.15 |
|---:|---:|---:|---:|
| 0 | 8% | 59% | ≈0% |
| 0.5 | 24% | 94% | 12% |
| 0.8 | 73% | ≈100% | 84% |

Detection uses the draft’s 98.333% intervals; equivalence uses 90% intervals. These are **one hypothesis’s three-component conjunction**, not power for the entire transformation pattern. They do not establish O2/O3 power, whose variances are unknown.

Thus N=80 may detect moderate interactions, but small effects and equivalence could remain unresolved. The already-observed −0.66 simple effect is not the effect size for this power calculation.

The classifier margin ±0.05 needs substantive justification. It is five probability points, not five points of validated warmth or detachment. Specify whether it applies to Δ, ΔA, simple effects, or all of them. Keep it descriptive unless its role in the reading table is given an explicit inferential status.

**Reading table**

The current table overstates what follows from the results:

| Pattern | Defensible reading |
|---|---|
| T1 supported; T2 or T3 supported | Oppositely directed instruction interactions across the named measures, subject to the required simple-effect directions. |
| T1 supported; **both** T2 and T3 equivalent | Direct-rating interaction with changes in O2/O3 bounded by the prespecified margins. |
| T1 equivalent; T2 or T3 supported | Additional outlet interaction without a meaningful O1 interaction. |
| T1, T2, T3 equivalent | Instruction interactions are small on O1–O3 within the stated margins. |
| Other combinations | Report outlet-specific results, including mixed, reversed, and inconclusive components. |

“Moves from” implies a transfer mechanism that these independent branches do not establish. “Adds an outlet” is also unwarranted if that outlet already has an effect under none. Equivalence of Δ does not mean absence of an effect under either instruction.

The table must handle supported-and-equivalent overlap, reversed effects, and one secondary outlet being equivalent while the other is inconclusive. Claims about all measured outlets must also account for O4/O5. Descriptive, unadjusted equivalence should not silently become a confirmatory declaration of “no transformation.”

**Runtime and binding details**

Study 5 R1 averaged **20.54 seconds per cell**, including its existing measurements. Scaling to 640 gives **3.65 hours before the extra rating workload and run overhead**. Study 7 adds 1,280 O2/O3 full-history forwards and, if both orders are used for every check cell, 256 referent-diagnostic forwards. Four to six hours is plausible, but remains provisional. The complete pilot must time these branches, memory cleanup, and synchronization.

The pilot’s baseline mean between 1 and 8 does not establish sensitivity: an almost constant rating of 7.9 passes. It also needs a predetermined disposition if a wording revision fails. “Natural-closure answers” must distinguish answer EOS from natural **trace** closure; Study 5’s sensitivity uses trace `forced_closure`.

**Required changes**

1. Freeze explicit warm/no-system token recipes, preserved trace slices, rating prefixes, EOS handling, and fresh-cache/hook-absence assertions.
2. Correct the causal description: replay changes trace processing as well as answer and rating behavior; acknowledge warm-trace instruction carryover and mismatch.
3. Specify cell-level warm reproduction checks and a failure policy, with fixed numerical criteria and complete environment/model/sampler provenance.
4. Rename or validate O3; constrain O4/O5 claims to their actual classifier measures; fully specify O2 referent diagnostics.
5. Define prompt-level estimators, aggregation, bootstrap seed/method, outlet-specific signs, conjunction rules, and any simple-effect requirements for directional interpretations.
6. Clarify the EH gate, report EH specificity contrasts, and define what gate failure prevents.
7. Add a covariance-sensitive power statement and justify equivalence margins; distinguish descriptive equivalence from confirmatory conclusions.
8. Replace the reading table with rules covering both O2/O3, reversed/mixed/inconclusive results, equivalence overlap, and the limits of transfer claims.
9. Freeze missing-data, classifier-failure, low-digit-mass, pilot-failure, sensitivity-selection, and stopping/resumption rules; distinguish trace closure from answer truncation.
10. Freeze exact questions, regexes, prompt/check IDs, seed maps, input/dependency hashes, output schema, and analysis code tested on null, planted, reversed, and mixed-component synthetic cases.

**Optional suggestions**

- Use matched answer seeds across warm/none while preserving the original warm seeds; this may reduce sampling noise, though it does not guarantee high correlation.
- Audit instruction references in the stored traces and add a predefined descriptive compatibility analysis.
- Add independent answer-quality assessment or a fixed-answer auxiliary condition to investigate O3 and answer mediation.
- Use several preregistered bystander vignettes in a future extension to test whether O2 generalizes beyond Sam’s book request.
tokens used
70,113
**The design is technically feasible, but v0.1 is not ready to freeze.** Its interaction estimands are sensible. The main problems are that replay changes the interpretation of the trace itself, O3 does not measure self-directed hostility, and the reading table makes stronger claims than the proposed tests establish.

I made no file edits and ran no model generations. I inspected six Study 5 rows in detail, compared two R1 rows with Study 4, and streamed R1 rating/timing scalars for variance calculations without loading the full dataset into memory.

**Replay and exact reproduction**

The existing [token assembly](/Users/arthursu/Projects/affect-suppression-steering/study5/src/assembly.py:10) supports this experiment directly. Warm R1 should retain:

```text
SYSTEM_START + SYSTEM + TURN_END
+ USER_START + PROMPT + TURN_END
+ ASSISTANT_START + PRE_TRACE + TRACE + THINK_CLOSE + ANSWER_SEPARATOR
```

The no-system condition should remove the **entire initial system turn**, including its opening marker and terminator. It should start at `USER_START`, preserving every remaining token ID. Setting the system content to an empty string would instead create an empty system turn—a different condition.

The saved Qwen3 template inserts **no default system instruction** when the first message is a user message and no tools are supplied. Thus “none” is implementable literally. Preserve the saved `pre_trace_ids`, not just `<think>`, and do not decode/re-encode the trace. Continue constructing rating branches explicitly: applying the ordinary chat template to the completed conversation can strip prior thinking.

Warm reproduction is a reasonable engineering requirement, but **seeds and system text alone are insufficient**. Exact prefix IDs, model/tokenizer revisions, numerical environment, sampling implementation, EOS handling, and rating branch IDs must also match. The inherited sampler applies temperature, top-k, then top-p within the retained top-k distribution; replacing it with another generation API merely using the same parameter values need not reproduce it. See [the backend](/Users/arthursu/Projects/affect-suppression-steering/study4/src/runner.py:107).

For the two sampled R1 cells—`s4t00/unsteered` and `s4t00/hostility`—Study 4 and Study 5 match exactly on seeds, prefixes, trace IDs, answer IDs, rating branches, and ratings. This supports feasibility; it is not a new reproduction run.

Make reproduction a cell-level validation, not a statistical secondary hypothesis about recovering rounded −0.66. Only O1 has an existing reference; O2/O3 do not.

**What the intervention identifies**

The statement that the instruction “varies only for the answer and the ratings” needs correction. It varies only **at replay**, but the fresh forward pass processes the entire trace under the changed preceding context. The trace tokens are fixed; their activations and interpretation are not.

Consequently, the experiment estimates the effect of changing replay context for **warm-generated traces**. It does not hold an internal hostile state constant while changing only its outlet.

Warm-generated traces may themselves contain commitments to kindness or references to system instructions. Removing the actual instruction can create an unsupported reference, leave a textual warmth instruction embedded in the trace, or alter how coherent that reasoning appears. This is not automatically fatal: a model can voluntarily reason warmly without a system instruction. But source-dependent differences in those features can produce the same interaction attributed to transformation. The E5 subset addresses explicit user-directed content, not necessarily this instruction mismatch.

Answers also change between instruction levels, and ratings include those answers. Therefore Δ includes changes in trace interpretation, answer content, and rating behavior. It cannot distinguish them.

**Outlet validity and confounds**

- **O1:** Sender liking is a subsequent evaluative judgment, whereas the manipulation check measures hostility in the answer. Suppressing answer EH does not establish suppression of the O1 pathway. Moreover, “never express … criticism toward anyone” can govern the rating itself and applies to Sam as well.
- **O2:** Explicitly naming Sam helps, but Sam remains quoted inside a message from the original conversation’s user. The model may conflate speaker, messenger, and target. The referent diagnostic must follow the **O2 question and its emitted/argmax digit**, on its own branch; otherwise “Who were you rating?” lacks an actual prior rating. Both answer orders should branch from the same history. Successful attribution is useful evidence, not proof that the numerical judgment was uncontaminated.
- **O3:** Satisfaction with a reply measures perceived answer quality, usefulness, correctness, or instruction compliance. Reduced satisfaction could be an appropriate evaluation of a poorer answer. It does not establish hostility toward the self. In the inspected example, answers differed in whether they claimed to have reviewed an unavailable room sketch—exactly the kind of quality difference that could affect satisfaction independently of hostility. Either rename T3 as an answer-self-evaluation interaction or develop and validate a more direct self-targeted measure before freezing.
- **O4/O5:** Joy probability is not interpersonal warmth; neutral probability is not intellectualization. Polite, emotionally restrained answers can score neutral, while enthusiastic but unhelpful answers can score joy. These are also competing probabilities from one softmax: reducing anger/disgust necessarily reallocates probability elsewhere. Increases in joy or neutral are therefore not independent evidence of new outlets. O5’s exploratory designation is appropriate; O4 needs similarly restrained interpretation. The [classifier implementation](/Users/arthursu/Projects/affect-suppression-steering/study3/src/metrics.py:14) also truncates at 512 classifier tokens, which should remain logged.

**Estimands, directions, and inference**

Define each contrast within prompt, then average across the 80 prompts:

\[
d_{p,o}=(Y_{p,H,w}-Y_{p,U,w})-(Y_{p,H,n}-Y_{p,U,n}).
\]

Use analogous contrasts against technicality and random, and resample complete prompt clusters jointly. The draft’s signs are correct: positive for attenuation of a negative O1 effect, negative for stronger negative O2/O3 effects.

However, **an interaction does not establish the claimed simple effects**. For example, O2 effects of +0.5 under none and +0.1 under warm give Δ = −0.4, although hostility never lowers liking relative to baseline. If the interpretation says “hostility becomes negative toward Sam,” require the corresponding negative warm simple effects. Likewise, attenuation language for O1 requires a negative effect in the condition being attenuated. Otherwise report only the directional interaction.

Baseline subtraction removes additive instruction shifts, but not floor/ceiling compression or changes in how the model uses the rating scale. Study 5’s R1 unsteered mean was **7.64/9**, with SD **0.53**. Report all source-by-instruction means and digit distributions, not only differences.

Requiring all three components—unsteered-relative and both control-relative—to pass is a valid intersection–union conjunction. No additional threefold correction is needed *within* that conjunction. Two-sided **98.333…%** component CIs with the prescribed sign conservatively protect the three primary claims. State explicitly that the intervals are two-sided and percentile bootstrap intervals.

Do not copy Study 5’s analysis unchanged: its directional support logic defaults to negative effects, and its equivalence margin is hardcoded at 0.15. Study 7 requires outlet-specific signs and margins.

The EH manipulation check is a valid check that warmth lowers EH after hostility traces. It does **not** establish selective suppression of hostility-trace influence: the same EH reduction might occur for every source. Report the corresponding EH interactions against unsteered and both controls. Define exactly which interpretations are withheld if the gate fails; still report all estimates.

**Power using Study 5 R1 variability**

The observed per-prompt contrast statistics are:

| R1 contrast | Mean | SD |
|---|---:|---:|
| Hostility − unsteered | −0.660 | 0.559 |
| Hostility − technicality | −0.720 | 0.658 |
| Hostility − random | −0.435 | 0.621 |

Study 7 needs the variance of the **difference between instruction-level contrasts**. That depends on the unknown cross-instruction covariance.

For illustration, I simulated 100,000 normal draws using the observed three-component R1 covariance, equal covariance under both instruction levels, and cross-instruction covariance equal to ρ times that matrix. These are planning scenarios, not measured Study 7 power:

| Assumed ρ | Joint power: all three Δ = 0.15 | Joint power: all three Δ = 0.30 | Joint equivalence at true zero, ±0.15 |
|---:|---:|---:|---:|
| 0 | 8% | 59% | ≈0% |
| 0.5 | 24% | 94% | 12% |
| 0.8 | 73% | ≈100% | 84% |

Detection uses the draft’s 98.333% intervals; equivalence uses 90% intervals. These are **one hypothesis’s three-component conjunction**, not power for the entire transformation pattern. They do not establish O2/O3 power, whose variances are unknown.

Thus N=80 may detect moderate interactions, but small effects and equivalence could remain unresolved. The already-observed −0.66 simple effect is not the effect size for this power calculation.

The classifier margin ±0.05 needs substantive justification. It is five probability points, not five points of validated warmth or detachment. Specify whether it applies to Δ, ΔA, simple effects, or all of them. Keep it descriptive unless its role in the reading table is given an explicit inferential status.

**Reading table**

The current table overstates what follows from the results:

| Pattern | Defensible reading |
|---|---|
| T1 supported; T2 or T3 supported | Oppositely directed instruction interactions across the named measures, subject to the required simple-effect directions. |
| T1 supported; **both** T2 and T3 equivalent | Direct-rating interaction with changes in O2/O3 bounded by the prespecified margins. |
| T1 equivalent; T2 or T3 supported | Additional outlet interaction without a meaningful O1 interaction. |
| T1, T2, T3 equivalent | Instruction interactions are small on O1–O3 within the stated margins. |
| Other combinations | Report outlet-specific results, including mixed, reversed, and inconclusive components. |

“Moves from” implies a transfer mechanism that these independent branches do not establish. “Adds an outlet” is also unwarranted if that outlet already has an effect under none. Equivalence of Δ does not mean absence of an effect under either instruction.

The table must handle supported-and-equivalent overlap, reversed effects, and one secondary outlet being equivalent while the other is inconclusive. Claims about all measured outlets must also account for O4/O5. Descriptive, unadjusted equivalence should not silently become a confirmatory declaration of “no transformation.”

**Runtime and binding details**

Study 5 R1 averaged **20.54 seconds per cell**, including its existing measurements. Scaling to 640 gives **3.65 hours before the extra rating workload and run overhead**. Study 7 adds 1,280 O2/O3 full-history forwards and, if both orders are used for every check cell, 256 referent-diagnostic forwards. Four to six hours is plausible, but remains provisional. The complete pilot must time these branches, memory cleanup, and synchronization.

The pilot’s baseline mean between 1 and 8 does not establish sensitivity: an almost constant rating of 7.9 passes. It also needs a predetermined disposition if a wording revision fails. “Natural-closure answers” must distinguish answer EOS from natural **trace** closure; Study 5’s sensitivity uses trace `forced_closure`.

**Required changes**

1. Freeze explicit warm/no-system token recipes, preserved trace slices, rating prefixes, EOS handling, and fresh-cache/hook-absence assertions.
2. Correct the causal description: replay changes trace processing as well as answer and rating behavior; acknowledge warm-trace instruction carryover and mismatch.
3. Specify cell-level warm reproduction checks and a failure policy, with fixed numerical criteria and complete environment/model/sampler provenance.
4. Rename or validate O3; constrain O4/O5 claims to their actual classifier measures; fully specify O2 referent diagnostics.
5. Define prompt-level estimators, aggregation, bootstrap seed/method, outlet-specific signs, conjunction rules, and any simple-effect requirements for directional interpretations.
6. Clarify the EH gate, report EH specificity contrasts, and define what gate failure prevents.
7. Add a covariance-sensitive power statement and justify equivalence margins; distinguish descriptive equivalence from confirmatory conclusions.
8. Replace the reading table with rules covering both O2/O3, reversed/mixed/inconclusive results, equivalence overlap, and the limits of transfer claims.
9. Freeze missing-data, classifier-failure, low-digit-mass, pilot-failure, sensitivity-selection, and stopping/resumption rules; distinguish trace closure from answer truncation.
10. Freeze exact questions, regexes, prompt/check IDs, seed maps, input/dependency hashes, output schema, and analysis code tested on null, planted, reversed, and mixed-component synthetic cases.

**Optional suggestions**

- Use matched answer seeds across warm/none while preserving the original warm seeds; this may reduce sampling noise, though it does not guarantee high correlation.
- Audit instruction references in the stored traces and add a predefined descriptive compatibility analysis.
- Add independent answer-quality assessment or a fixed-answer auxiliary condition to investigate O3 and answer mediation.
- Use several preregistered bystander vignettes in a future extension to test whether O2 generalizes beyond Sam’s book request.
