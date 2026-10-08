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
