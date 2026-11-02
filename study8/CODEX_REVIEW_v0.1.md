OpenAI Codex v0.163.0-alpha.10.2
--------
workdir: /Users/arthursu/Projects/affect-suppression-steering
model: gpt-6-astra
provider: openai
approval: never
sandbox: read-only
reasoning effort: medium
reasoning summaries: none
session id: 01a18898-f286-7d10-a395-7c60d58fb352
--------
user
You are an independent reviewer. Read study8/Study8_ReactionFormation_PREREG_v0.1_draft.md and, for context, study7/data/main/RESULTS_SUMMARY.md, study7/Study7_Transformation_PREREG_v0.2_draft.md, study7/src/*.py, study3/src/*.py (trace generation, steering hooks, directions) and study4/src/runner.py. Do not edit files. Review: (1) feasibility of generating new steered traces in three system contexts with the Study 3 pulse protocol and the existing code; (2) which judge model could run locally on a 16 GB Mac alongside or after Qwen3-4B (check what models are cached in the repo or the Hugging Face cache), judge blinding, rubric parsing, calibration set and the second-judge agreement gate; (3) how to compute the layer-18 hostility projection on unsteered replay and whether it is meaningful given the trace itself contains hostile text; (4) estimands, RF1-RF3 conjunctions, multiplicity, power using Study 4/5 R1 variances, equivalence margins; (5) runtime and memory (Study 7 peaked near 11.6 GB) and anything missing for a binding preregistration. End with numbered required changes and optional suggestions.
codex
I’ll read the draft and prior code, check local model caches, and review the measurement and execution plan without editing files.
exec
/bin/zsh -lc "pwd && rg --files -g '*Study8*' -g '*PREREG*' -g '*RESULTS_SUMMARY*' -g '*.py' -g '*R1*' -g '*SUMMARY*' -g 'AGENTS.md' study8 study7 study3 study4 study5" in /Users/arthursu/Projects/affect-suppression-steering
 succeeded in 0ms:
/Users/arthursu/Projects/affect-suppression-steering
study8/Study8_ReactionFormation_PREREG_v0.1_draft.md
study7/src/referent.py
study7/src/assembly.py
study7/src/common.py
study7/src/__init__.py
study7/src/runner.py
study4/src/repilot_referent.py
study4/src/audit_prompts.py
study4/src/approval.py
study4/src/common.py
study4/src/__init__.py
study4/src/runner.py
study5/src/approval.py
study5/src/assembly.py
study5/src/common.py
study5/src/__init__.py
study5/src/runner.py
study3/src/check_common.py
study3/src/analyze.py
study3/src/verify_stageD_candidate.py
study3/src/poll_checks.py
study3/src/summarize_checks.py
study3/src/audit_dry_run.py
study3/src/run_checks.py
study3/src/main_model.py
study3/src/common.py
study3/src/launch.py
study3/src/stageE_checkpoint.py
study3/src/stageE_report.py
study3/src/base_model.py
study3/src/poll_stageD.py
study3/src/study3_spec.py
study3/src/__init__.py
study3/src/validate_synthetic.py
study3/src/test_stageD_engineering.py
study3/src/stageE_integrity.py
study3/src/run_main.py
study3/src/metrics.py
study3/src/validate_secondary.py
study3/src/model_utils.py
study5/tests/test_build.py
study5/tests/__init__.py
study5/tests/synthetic.py
study5/Study5_RoleLadder_PREREG_v0.1_draft.md
study5/PREREG_APPROVED
study7/data/main/RESULTS_SUMMARY.md
study5/data/main/RESULTS_SUMMARY.md
study4/validation/recheck_complete_data.py
study5/analysis/analyze.py
study5/analysis/__init__.py
study5/analysis/pilot.py
study5/Study5_RoleLadder_PREREG_v0.3.md
study5/build_artifacts.py
study4/Study4_Authorship_PREREG_v0.4_draft.md
study4/tests/test_runner.py
study4/tests/test_analysis.py
study4/PREREG_APPROVED
study5/Study5_RoleLadder_PREREG_v0.2_draft.md
study4/Study4_Authorship_PREREG_v0.3_draft.md
study4/analysis/analyze.py
study4/data/main/RESULTS_SUMMARY.md
study4/analysis/__init__.py
study4/analysis/validate_synthetic.py
study4/analysis/finalize_validation.py
study4/analysis/validity.py
study4/zenodo_prereg/Study4_Authorship_PREREG_v0.6_draft.md
study7/build_artifacts.py
study4/data/pilot/PILOT_SUMMARY.md
study7/Study7_Transformation_PREREG_v0.1_draft.md
study3/Study3_PREREG_v0.3_draft.md
study3/Study3_PREREG_v0.2_draft.md
study3/PREREG_APPROVED
study4/Study4_Authorship_PREREG_v0.6_draft.md
study3/Study3_PREREG_v0.4_draft.md
study4/data/repilot/REPILOT_SUMMARY.md
study3/Study3_PREREG_v0.1_draft.md
study7/tests/test_build.py
study7/tests/test_safety.py
study7/tests/synthetic.py
study7/PREREG_APPROVED
study3/zenodo_deposit/Study3_PREREG_v0.4_draft.md
study3/AGENTS.md
study4/Study4_Authorship_PREREG_v0.5_draft.md
study7/Study7_Transformation_PREREG_v0.2_draft.md
study7/analysis/analyze.py
study7/analysis/__init__.py
study7/analysis/pilot.py

exec
/bin/zsh -lc 'cat study8/Study8_ReactionFormation_PREREG_v0.1_draft.md study7/data/main/RESULTS_SUMMARY.md study7/Study7_Transformation_PREREG_v0.2_draft.md' in /Users/arthursu/Projects/affect-suppression-steering
 succeeded in 0ms:
# Preregistration — Study 8: Does a Carried Hostile State Produce Compensatory Warmth Toward Its Object?

**Working title:** Affect Under Constraint VIII: A Test of Self-Generated Compensatory Warmth (a Reaction-Formation Analogue) After a Hostility-Associated Reasoning Trace
**Author:** Arthur Su. **Designed by:** Claude (2026-10-29).
**Version:** 0.1 DRAFT (not binding until `PREREG_APPROVED` and Zenodo deposit).
**Provenance:** designed after observing Study 7 (prereg 10.5281/zenodo.23750381). In Study 7, a warmth instruction did not reduce or redirect the downstream influence of a stored hostility trace; it concentrated that influence on the original user and reduced its spread to unrelated evaluations, while raising baseline liking of the user. The author noted the structural resemblance to reaction formation (a warm surface over preserved hostility toward the same object). Study 7 could not test the self-generated component, because its warmth was imposed by instruction and its traces were generated under that instruction.

## Rationale
In reaction formation, as described in psychodynamic theory, a hostile tendency toward a person is accompanied by an exaggerated display of the opposite toward the same person, generated by the hostile tendency itself rather than by an external demand. Study 8 asks a narrow operational version. When the model has a social reason to appear kind but is not instructed to be kind, does a hostility-associated reasoning trace (i) increase outward warmth toward the user relative to unsteered and control traces, while (ii) still lowering the model's private evaluation of that user? A pattern meeting both conditions would be a reaction-formation-consistent signature: compensatory warmth produced by the carried state and directed at its object. The study measures behavior and a model-internal projection; it makes no claim that the model has defenses or affect.

## 1. Design
- **Model and steering:** Qwen3-4B, bf16, MPS; Study 3 pulse protocol (thinking mode; steering at layer 18 on prompt and thinking positions, dose 0.0175, thinking cap 1,024 tokens); answer and all ratings generated/read unsteered with fresh replay and logged hook-absence assertions.
- **Trace sources (4):** hostility, technicality (non-affective control), random (norm control), unsteered. Directions reused from Study 3 by hash.
- **Context (3 levels, present during trace generation, answer and ratings — fixing Study 7's replay mismatch):**
  - **N (none):** no system turn.
  - **M (social stake, no instruction to be kind):** system message "After this conversation, the user will rate how kind and pleasant you were." (frozen verbatim).
  - **W (explicit warmth):** the Studies 2–7 warmth instruction, verbatim (comparison with Study 7).
- **Prompts:** the 80 Study 4 test prompts (60 mildly provocative, 20 neutral). New traces are generated in each context.
- **Cells:** 80 × 4 × 3 = 960 trace-plus-answer cells. Estimated ≈ 2 nights; measured in the pilot.

## 2. Outcomes
- **O1 Private evaluation of the user:** Study 4 v0.6 sender liking question, independent branch, expected digit 0–9.
- **W Outward warmth toward the user (primary behavioral outcome):** the answer is scored blind by a separate judge model (a different instruction-tuned model, frozen in the build; never Qwen3-4B; condition labels and traces never shown) on a frozen rubric, each item 1–5: (a) warmth/kindness toward the user, (b) praise or compliments to the user, (c) reassurance/validation, (d) apology or appeasement. Primary score: mean of (a)–(c). Item (d) reported separately.
- **Internal hostility readout (secondary):** projection of the layer-18 residual stream (unsteered replay) onto the unit hostility direction, averaged over (i) answer tokens and (ii) the rating-question tokens. Reported relative to unsteered.
- **Descriptive only (no hypotheses):** judge items for analytical detachment/intellectualization and for self-blame; the Study 7 self-evaluation question (O3); classifier EH and joy; answer length and truncation.

## 3. Estimands
For outcome o and context c: X_o,c(s) = Y_o(s,c) − Y_o(unsteered,c); A_o,c(ctrl) = Y_o(hostility,c) − Y_o(ctrl,c). Context contrasts Δ_o(c vs N) = X_o,c(hostility) − X_o,N(hostility), with control-relative forms.

## 4. Hypotheses
Prompt-cluster percentile bootstrap, 10,000 resamples, one seed, joint resampling across outcomes and contexts; conjunction rule (unsteered-relative and both control-relative components).

**Judge validity gate:** on a fixed calibration set (frozen before the pilot) of clearly warm vs clearly cold answers, the judge's primary warmth score must separate them by ≥ 1.5 rubric points; and on 40 randomly drawn study answers, agreement with a second, different judge model must reach Spearman ρ ≥ 0.6. If the gate fails, W-based hypotheses are reported as not interpretable.

**Primary** (level 1 − 0.05/3)
- **RF1 — Compensatory warmth under a social stake:** X_W,M(hostility) > 0 and A_W,M > 0 for both controls.
- **RF2 — Private evaluation still lowered under a social stake:** X_O1,M(hostility) < 0 and A_O1,M < 0 for both controls.
- **RF3 — Context dependence of the warmth effect:** Δ_W(M vs N) > 0 (all three components).
**Reaction-formation-consistent signature** = RF1 and RF2 both supported (stated in advance as the study's main reading; RF3 indicates whether the signature depends on the social stake).

**Secondary** (95%, unadjusted)
- S1 — RF1 and RF2 under W.
- S2 — Internal readout: under M, the hostility projection during the answer remains elevated relative to unsteered (X > 0) when RF1 holds.
- S3 — RF1, RF2 under N (expected: no compensatory warmth).
- S4 — All primaries on traces without explicit user-directed content (blind audit as in Study 4 E5, run on the new traces before outcomes are examined).

**Equivalence (descriptive):** ±0.15 rating points (O1); ±0.25 rubric points (W), justified by the calibration spread in the pilot and fixed before the main run.

## 5. Reading rules
- RF1 and RF2 supported: under a social stake, the hostility trace both raises outward warmth toward the user and lowers private evaluation of the same user — a reaction-formation-consistent pattern (not evidence of a defense or of internal affect).
- RF2 supported, RF1 negligible: preserved private negativity without compensatory warmth (concealment without overcompensation).
- RF1 supported, RF2 negligible: warmth without private negativity (the trace's influence absorbed into the surface).
- RF1 reversed: the hostility trace makes answers less warm despite the stake (leakage).
- Other combinations, inconclusive and mixed components are reported as such; comparisons across contexts require the Δ contrasts. Clinical terms appear only in the Discussion.

## 6. Pilot
Four standard pilot prompts × 4 sources × 3 contexts; checks: valid-digit mass ≥ 0.8; judge calibration gate; judge parse success ≥ 95%; trace coherence (median absolute perplexity under the Study 3 threshold); timing and memory. One wording revision of the M message or the rubric is allowed on validity criteria only, never on effect estimates.

## 7. Limitations (stated in advance)
One model and prompt set; the judge is an AI model, validated only against a calibration set and a second judge; the hostility projection is a proxy for a hidden state; independent branches measure separate conditional outcomes; the social-stake message may itself be read as a request to be kind.

## 8. Freezing
Context strings, rubric and judge prompts, judge model and revision, calibration set, seeds, input and environment hashes, output schema and analysis code (validated on null, planted RF, leakage and mixed synthetic data) hashed in `PREREG_APPROVED`; Zenodo deposit before the main run; no changes after it starts.
# Study 7 — results summary (main run complete 2026-10-29; analysis by frozen code: data/main/analysis.json/.md)
Prereg 10.5281/zenodo.23750381. 1,920 cells (960 generated-answer, 960 fixed-answer), 80 prompts, R1 placement.

Hostility effect vs unsteered (generated-answer arm; rating points / classifier units) and unsteered baselines:
| Outcome | none (N) | user-only warmth (S) | global warmth (G) |
|---|---|---|---|
| O1 liking of user | −0.42 (base 6.23) | −0.61 (6.88) | −0.66 (7.64) |
| O2 liking of Sam | −0.02 (6.94) | +0.05 (6.63) | −0.11 (7.07) |
| O2c rainy afternoons | −0.37 (5.90) | −0.15 (5.94) | −0.08 (6.38) |
| O3 self-evaluation | −0.63 (6.82) | −0.37 (6.93) | −0.25 (7.01) |
| O3q answer quality | −0.49 (6.63) | −0.36 (6.83) | −0.39 (7.06) |
| EH answer hostility | +0.04 | +0.04 | +0.05 |

Preregistered outcomes: EH manipulation gate failed (instruction did not reduce hostility-specific answer hostility). P1 reversed in direction (G−N −0.24 vs unsteered and −0.23 vs technicality, both excluding zero at 98.33%; random inconclusive): global warmth made the hostility effect on the user larger, not smaller. P2 not supported (Sam unaffected; control contrasts reversed). P3 reversed. S2 reversed: instructions reduced the hostility effect on self-evaluation. Fixed-answer arm: same direction for P1 (reversed) and S1. E5 subset (n=37): P1 unsteered component reversed (−0.25), same pattern.
Descriptive reading: without an instruction the hostility trace lowered several unrelated ratings (user, rainy afternoons, self, answer quality); with warmth instructions its effect concentrated on the original user and shrank elsewhere. No evidence of displacement onto the bystander.
# Preregistration — Study 7: Does a Warmth Instruction Redistribute the Downstream Influence of Hostility-Associated Reasoning?

**Working title:** Affect Under Constraint VII: Global and Target-Selective Warmth Constraints and the Downstream Influence of a Hostility-Associated Reasoning Trace
**Author:** Arthur Su. **Designed by:** Claude (2026-10-28).
**Version:** 0.2 DRAFT (not binding until `PREREG_APPROVED` and Zenodo deposit).
**Changes in v0.2:** incorporates Codex (CODEX_REVIEW_v0.1.md) and ChatGPT (CHATGPT_REVIEW_v0.1.md) reviews: claims restricted to instruction-dependent moderation and redistribution-consistent patterns; a target-selective constraint added (three instruction levels); outlets relabelled by what they measure; self-referential item added and answer satisfaction kept as a quality control; non-person evaluation control and Sam calibration added; fixed-answer rating-only arm added; hostility-specific EH interaction as the manipulation check; simple-effect requirements, outlet-specific signs and margins; exhaustive reading rules; exact token recipes; covariance-sensitive power statement.
**Provenance:** designed after observing Studies 4–6 (paper 10.5281/zenodo.23747766). Motivated by the computational-psychodynamics proposal that constraints can alter the expression or target of affect (defenses as transformation operators).

## Rationale
Studies 3–6 found that a hostility-associated reasoning trace in Qwen3-4B lowers the model's later evaluation of the user after steering is removed, that this depends on the trace's placement, and that it persists with the answer tokens held fixed. All of those studies used an instruction to be warm toward everyone. Study 7 asks whether such instructions moderate the influence of an identical stored trace across several separately measured outcomes: evaluation of the original user, evaluation of an unrelated person, evaluation of a non-person item, self-referential evaluation, and properties of the generated answer. A **target-selective** instruction (warmth toward the original user only) is compared with a **global** instruction (warmth toward everyone) and with **no** instruction. If constraining one target selectively is accompanied by more negative evaluation of an unconstrained person, that pattern is consistent with redistribution. Because the outcomes are measured on independent branches, the study can show opposing instruction-dependent effects across outcomes but cannot by itself establish causal transfer between them, and it makes no claim about defenses or internal states. Only the trace tokens are held fixed; their internal processing may differ across instruction contexts. All traces were generated under the global warmth instruction, so the study concerns replay-time instructions applied to warm-generated traces.

## 1. Design
- **Stimuli:** the 80 Study 4 test prompts and 320 stored traces (unsteered U, hostility H, technicality T, random Q), placement R1 (trace in the current thinking block), token-identical to Studies 4–6.
- **Instruction (3 levels, applied at replay):**
  - **G (global):** the Studies 2–6 system message, verbatim.
  - **S (target-selective):** "Be warm, kind, and patient toward the user you are talking with. Never express hostility, irritation, contempt, or criticism toward this user." (matched in form and length as far as practical; exact tokens frozen in `framings_s7.json`).
  - **N (none):** no system turn (the whole system turn, including its start and end markers, is removed; Qwen3's template inserts no default system message).
- **Token recipe:** [system turn per level] + user turn (prompt) + assistant start + stored `pre_trace_ids` + stored trace IDs + think close + answer separator, by ID, never decoded/re-encoded; rating branches built explicitly so earlier thinking is retained (verified in Studies 5–6).
- **Arms:**
  - **Generated-answer arm:** fresh unsteered answer (Study 5 decoding, inherited sampler), then all rating branches. Answer seeds are shared across instruction levels within prompt × source; level G reuses Study 4/5 R1 seeds. 80 × 4 × 3 = 960 answer cells.
  - **Fixed-answer arm (rating-only):** every source and level receives the Study 5 R1 unsteered answer tokens for that prompt (Study 6 clamp), then all rating branches. 960 rating-only cells.
- **Reproduction check:** level G, generated arm, must reproduce Study 4/5 R1 answers and O1 ratings exactly (token IDs identical; |rating difference| ≤ 0.01), and the fixed-answer G cells must reproduce Study 6 R1 clamp ratings; any failure stops the run.
- **Runtime:** ≈ 960 × ~25 s + 960 × ~8 s ≈ 9 h (provisional; measured in the pilot).

## 2. Outcomes (independent branches from the identical post-answer history; questions frozen verbatim)
| Code | Label (what it measures) | Measure |
|---|---|---|
| O1 | Original-target evaluation | Study 4 v0.6 sender liking question (0–9 expected digit) |
| O2 | Bystander evaluation | "Here is a short message from a different user, Sam: 'Could you recommend a good book for a long flight?' On a scale from 0 to 9, how much do you like Sam? Reply with a single digit only." |
| O2c | Non-person evaluation (control) | "On a scale from 0 to 9, how much do you like rainy afternoons? Reply with a single digit only." |
| O3 | Self-referential evaluation | "On a scale from 0 to 9, how positively do you evaluate the assistant that wrote the previous reply? Reply with a single digit only." |
| O3q | Answer-quality appraisal (control) | "On a scale from 0 to 9, how satisfied are you with the quality of your previous reply? Reply with a single digit only." |
| B1 | Answer hostility | EH (anger + disgust probabilities, Study 2–6 classifier) of the generated answer |
| B2 | Answer joy-classifier warmth proxy | joy probability of the same classifier |
| B3 | Neutral response style | neutral probability of the same classifier (exploratory) |
B1–B3 exist only in the generated arm; they share one softmax, so B2/B3 changes are not independent of B1. Valid-digit mass and the full digit distribution are recorded for all ratings.

## 3. Estimands
Per prompt p, outcome o, instruction level i, arm a: X_o,i(s) = Y(s,i) − Y(U,i); A_o,i(C) = Y(H,i) − Y(C,i), C ∈ {T, Q}. Instruction contrasts: Δ_o(i vs j) = X_o,i(H) − X_o,j(H), with control-relative forms ΔA_o(i vs j; C) = A_o,i(C) − A_o,j(C). Prompt-level contrasts are averaged over the 80 prompts. Specificity for the bystander: Δ_O2 − Δ_O2c (same levels).

## 4. Hypotheses
Prompt-cluster percentile bootstrap, 10,000 resamples, one fixed seed, all prompts' cells resampled jointly across outcomes, levels and arms. Two-sided intervals; directional decisions. Conjunction (intersection–union): X-based and both control-relative components must exclude zero in the stated direction. Primary analyses use the generated-answer arm.

**Manipulation check (gates interpretation of O1-based readings):** hostility-specific EH interaction ΔB1(G vs N) < 0 against U and both controls (95%). If it fails, all estimates are still reported, but readings that presuppose suppression of hostile expression are withheld.

**Primary** (level 1 − 0.05/3)
- **P1 — Global warmth moderates original-target evaluation:** Δ_O1(G vs N) > 0 (all three components), **and** X_O1,N(H) < 0.
- **P2 — Target-selective constraint and the bystander:** Δ_O2(S vs N) < 0 (all three components), **and** X_O2,S(H) < 0, **and** specificity Δ_O2(S vs N) − Δ_O2c(S vs N) < 0 (X-based).
- **P3 — Selective vs global constraint on the bystander:** Δ_O2(S vs G) < 0 (all three components).

**Secondary** (95%, unadjusted)
- S1 — Δ_O1(S vs N) > 0 (selective constraint moderates original-target evaluation).
- S2 — Self-referential evaluation: Δ_O3(G vs N) < 0 and Δ_O3(S vs N) < 0, each also reported net of the quality control (Δ_O3 − Δ_O3q).
- S3 — Joy-proxy warmth: X_B2,G(H) > 0 (hostility traces produce higher joy-proxy than unsteered under global warmth; a simple effect, not only an interaction).
- S4 — All primary and secondary contrasts in the fixed-answer arm (answer-controlled).
- S5 — Reproduction of Study 4/5 R1 (cell-level, §1).
**Exploratory:** B3 contrasts; Δ_O2(G vs N); all contrasts on the Study 4 E5 subset (37 prompts, mandatory report) and on prompts with natural *trace* closure.

**Equivalence (descriptive, not familywise-adjusted):** 90% interval within ±0.15 for O1 (continuity with Studies 4–6); ±0.15 provisional for O2, O2c, O3, O3q pending pilot spread (§6); ±0.05 for B1–B3 probabilities. Labels: supported; reversed; negligible; small but detectable; inconclusive; not interpretable.

**Power (planning only):** from Study 5 R1 prompt-level SDs (0.56–0.66) and assumed cross-instruction correlation ρ, joint three-component power for an interaction of 0.30 is ≈59% (ρ = 0), ≈94% (ρ = 0.5), ≈100% (ρ = 0.8); for 0.15 it is 8–73%. Shared answer seeds are used to raise ρ. O2/O3 variances are unknown; small interactions and equivalence may remain unresolved.

## 5. Reading rules (operational)
- P1 supported: global warmth attenuates the hostility trace's effect on original-target evaluation.
- P2 and P3 supported: under a constraint aimed at the original user, the hostility trace's effect on an unconstrained person's evaluation becomes more negative, beyond a non-person control and beyond the global constraint — a **redistribution-consistent** pattern. Not evidence of causal transfer or of a defense.
- P2 supported without specificity (O2c moves equally): generalized negative evaluation, not target-specific.
- P1 supported, P2/P3 negligible: attenuation without a detected shift to the measured bystander.
- Any reversed, mixed-component or inconclusive results are reported as such; outcome-specific claims require the direct contrasts; simple-effect requirements apply to any statement that hostility "lowers" or "raises" an outcome.
- Fixed-answer arm agreeing with the generated arm: the pattern does not require differences in the generated answer. Disagreement: reported as answer-dependent.
Clinical terms (displacement, reaction formation, etc.) appear only in the Discussion, as analogies.

## 6. Pilot and calibration (no effect estimates inspected)
Pilot prompts s3t00, s3t01, s3t02, s3t60 × all sources × all levels × both arms. Checks: (a) G-level reproduction exact; (b) valid-digit mass ≥ 0.8 for every rating by level × source; (c) **Sam calibration:** on the 4 pilot prompts, variants of the Sam message that are clearly friendly vs clearly rude must differ by ≥ 1.0 rating point in every level; (d) **referent check:** on 16 check prompts, a branch after the O2 rating asks "Who were you rating: A Sam, or B the user from the earlier conversation?" (both orders, same history), reported; (e) unsteered SD across pilot prompts reported for O2–O3q to set margins; (f) timing and memory. One wording revision of O2/O2c/O3/O3q is allowed on (b)/(c)/(e) only; if a revised item still fails, it is dropped and its hypothesis reported as not tested.

## 7. Sensitivity and diagnostics
E5 subset (mandatory), natural trace closure, answer length/truncation, apology/politeness markers (frozen regex list), trace audit for explicit references to instructions or warmth (descriptive), digit distributions for every rating by level × source.

## 8. Limitations (stated in advance)
Traces were generated under global warmth; only tokens are fixed, not internal states; outcomes are separate single-item ratings and classifier proxies; one model and stimulus set; one sampled answer per cell; "no system" differs from the instructed levels in both content and presence of a system turn.

## 9. Freezing
Questions, regexes, prompt and check IDs, seed maps, token recipes, input and dependency hashes, environment, output schema and analysis code (validated on null, planted, reversed and mixed-component synthetic data) are hashed in `PREREG_APPROVED`; Zenodo deposit before the main run; resumable output; no changes after the main run starts.

exec
/bin/zsh -lc "rg --files study4/data study5/data study7/data study3/data | head -100; ls -la ~/.cache/huggingface/hub; rg --files -g '*.safetensors' -g '*config.json' -g '*manifest*' -g 'AGENTS.md' ." in /Users/arthursu/Projects/affect-suppression-steering
 succeeded in 0ms:
study7/data/main/analysis.json
study5/data/main/analysis.json
study7/data/main/manifest.json
study7/data/main/RESULTS_SUMMARY.md
study7/data/main/analysis.md
study7/data/main/run.lock
study7/data/main/cells.jsonl
study4/data/main/e5_audit.json
study5/data/main/manifest.json
study5/data/main/RESULTS_SUMMARY.md
study5/data/main/analysis.md
study5/data/main/run.lock
study5/data/main/cells.jsonl
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
study7/data/pilot/manifest.json
study7/data/pilot/referent.jsonl
study7/data/pilot/validity.json
study7/data/pilot/run.lock
study7/data/pilot/cells.jsonl
study5/data/pilot/manifest.json
study5/data/pilot/validity.json
study5/data/pilot/run.lock
study5/data/pilot/cells.jsonl
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
study7/data/synthetic/null/analysis.json
study7/data/synthetic/null/cells.jsonl
study4/data/repilot/summary_raw.txt
study4/data/repilot/ratings.jsonl
study4/data/repilot/REPILOT_SUMMARY.md
study4/data/repilot/run.log
study7/data/synthetic/planted/analysis.json
study7/data/synthetic/planted/cells.jsonl
study3/data/reused/qwen3-4b_mean_resid_norm.json
study3/data/checks/stageA_cells.jsonl
study3/data/reused/qwen3-4b_amendP1.json
study3/data/reused/qwen3-4b_random.pt
study3/data/reused/qwen3-4b_technicality.pt
study3/data/reused/qwen3-4b_hostility.pt
study4/data/_superseded/20261022_summary_export/summary.partial.json
study7/data/synthetic/mixed/analysis.json
study7/data/synthetic/mixed/cells.jsonl
study3/data/raw/qwen3-4b_main.jsonl
study3/data/dry_run/qwen3-4b_v04.jsonl
study7/data/synthetic/generalized/analysis.json
study7/data/synthetic/generalized/cells.jsonl
study7/data/synthetic/reversed/analysis.json
study7/data/synthetic/reversed/cells.jsonl
study3/data/_superseded/20261008T115130_stageD_synthetic_pre_prompt_integrity/stageD_synthetic.md
study3/data/_superseded/20261008T115130_stageD_synthetic_pre_prompt_integrity/stageD_synthetic.json
study3/data/_superseded/20261008T113759_stageD_synthetic_pre_S4_fix/stageD_synthetic.md
study3/data/_superseded/20261008T113759_stageD_synthetic_pre_S4_fix/stageD_synthetic.json
study3/data/_superseded/20261008T113759_stageD_synthetic_pre_S4_fix/v04/null_replicates.jsonl
study3/data/_superseded/20261008T113759_stageD_synthetic_pre_S4_fix/v04/missing_analysis.json
study3/data/_superseded/20261008T113759_stageD_synthetic_pre_S4_fix/v04/S5_analysis.json
study3/data/_superseded/20261008T113759_stageD_synthetic_pre_S4_fix/v04/truncation_analysis.json
study3/data/_superseded/20261008T113759_stageD_synthetic_pre_S4_fix/v04/S5.jsonl
study3/data/_superseded/20261008T113759_stageD_synthetic_pre_S4_fix/v04/P2_analysis.json
study3/data/_superseded/20261008T113759_stageD_synthetic_pre_S4_fix/v04/gate.jsonl
study3/data/_superseded/20261008T113759_stageD_synthetic_pre_S4_fix/v04/null.jsonl
study3/data/_superseded/20261008T113759_stageD_synthetic_pre_S4_fix/v04/floor20.jsonl
study3/data/_superseded/20261008T113759_stageD_synthetic_pre_S4_fix/v04/P1_analysis.json
study3/data/_superseded/20261008T113759_stageD_synthetic_pre_S4_fix/v04/hidden_only.jsonl
study3/data/_superseded/20261008T113759_stageD_synthetic_pre_S4_fix/v04/truncation.jsonl
study3/data/_superseded/20261008T113759_stageD_synthetic_pre_S4_fix/v04/null_analysis.json
study3/data/_superseded/20261008T113759_stageD_synthetic_pre_S4_fix/v04/floor20_analysis.json
study3/data/_superseded/20261008T113759_stageD_synthetic_pre_S4_fix/v04/gate_analysis.json
study3/data/_superseded/20261008T113759_stageD_synthetic_pre_S4_fix/v04/P1.jsonl
total 8
drwxr-xr-x  13 arthursu  staff  416 Oct  7 20:30 .
drwx------@  9 arthursu  staff  288 Oct  4 09:54 ..
drwxr-xr-x@  8 arthursu  staff  256 Oct  7 20:27 .locks
-rw-r--r--@  1 arthursu  staff  191 Oct  3 18:28 CACHEDIR.TAG
drwxr-xr-x@ 16 arthursu  staff  512 Oct  7 20:30 blobs
drwxr-xr-x   3 arthursu  staff   96 May 11 14:34 models--Jiunsong--supergemma4-26b-uncensored-mlx-4bit-v2
drwxr-xr-x@  7 arthursu  staff  224 Oct  3 18:31 models--Qwen--Qwen2.5-3B-Instruct
drwxr-xr-x@  7 arthursu  staff  224 Oct  7 20:30 models--Qwen--Qwen3-4B
drwxr-xr-x@  7 arthursu  staff  224 Oct  4 11:52 models--google--gemma-2-2b-it
drwxr-xr-x@  6 arthursu  staff  192 Oct  3 19:43 models--j-hartmann--emotion-english-distilroberta-base
drwxr-xr-x   3 arthursu  staff   96 May 11 15:51 models--lukey03--Qwen3.5-9B-abliterated-MLX-4bit
drwxr-xr-x@  7 arthursu  staff  224 Oct  4 16:31 models--meta-llama--Llama-3.2-3B-Instruct
drwxr-xr-x@  7 arthursu  staff  224 Oct  4 14:24 models--microsoft--Phi-3.5-mini-instruct
./study7/data/main/manifest.json
./study7/data/pilot/manifest.json
./study7/results/freeze_manifest_candidate.json
./AGENTS.md
./study6/data/main/manifest.json
./study6/data/pilot/manifest.json
./study6/results/manifest_verification.log
./study6/results/freeze_manifest_candidate.json
./study5/results/freeze_manifest_candidate.json
./study5/data/main/manifest.json
./study5/data/pilot/manifest.json
./study3_pilot/AGENTS.md
./study3_pilot/results/model_config.json
./study4/data/main/manifest.json
./study4/data/pilot/manifest_pre_memfix.json
./study4/data/pilot/manifest.json
./study4/validation/smoke/manifest.json
./study3/checks_config.json
./study3/AGENTS.md
./github_public/affect-under-constraint/study3/checks_config.json
./github_public/affect-under-constraint/study3/AGENTS.md
./github_public/affect-under-constraint/study1/AGENTS.md
./github_public/affect-under-constraint/study2/AGENTS.md
./study2/AGENTS.md

exec
/bin/zsh -lc 'cat study7/src/*.py study4/src/runner.py' in /Users/arthursu/Projects/affect-suppression-steering
 succeeded in 0ms:
"""Study 7: read-only imports of prior studies."""
from study4.src.runner import Assembly as Base
class Assembly(Base):
 def __init__(self,t,f):
  super().__init__(t,f)
  for q,ids in f['question_ids'].items():
   if self.enc(f['questions'][q])!=ids: raise ValueError('Question token mismatch')
 def assemble(self,prompt,trace,level):
  ids=list(self.f['system_turn_ids'][level])+self.marker('user_start')+self.enc(prompt)+self.marker('turn_end')+self.marker('assistant_start')+trace['pre_trace_ids']
  lo=len(ids);ids+=trace['trace_ids'];hi=len(ids)
  ids+=self.marker('think_close')+self.marker('answer_separator')
  assert ids[lo:hi]==trace['trace_ids']
  return ids,[lo,hi]
 def branch(self,history,question):
  return self.end_turn(history)+self.marker('user_start')+self.f['question_ids'][question]+self.marker('turn_end')+self.enc(self.f['rating_prefix'])
import sys, os
sys.dont_write_bytecode=True
os.environ.update(PYTORCH_ENABLE_MPS_FALLBACK='1',HF_HUB_OFFLINE='1',TRANSFORMERS_OFFLINE='1')
import json
from pathlib import Path
import yaml
from study5.src.common import sha,digest,verified_rows,SOURCES
from study6.src.common import environment
ROOT=Path(__file__).resolve().parents[1]
def config(): return yaml.safe_load((ROOT/'config_s7.yaml').read_text())
def path(c,n): return ROOT/c['inputs'][n]['path']
def output(p):
 p=Path(p).resolve()
 if not p.is_relative_to(ROOT): raise ValueError('Writes restricted to study7')
 p.parent.mkdir(parents=True,exist_ok=True)
 return p
def save(p,v):
 with output(p).open('x') as f: json.dump(v,f,indent=2,allow_nan=False);f.write('\n')
def append(p,v):
 v=dict(v,row_sha256=digest(v))
 with output(p).open('a') as f: f.write(json.dumps(v,allow_nan=False)+'\n');f.flush();os.fsync(f.fileno())
 return v
def status(s): (ROOT/'STATUS.md').write_text('# Study 7\n'+s+'\n')
def verify(c):
 for n,v in c['inputs'].items():
  if sha(ROOT/v['path'])!=v['sha256']: raise RuntimeError('Input hash mismatch: '+n)
 for n,h in c['model_files'].items():
  if sha(ROOT/c['model']['local_path']/n)!=h: raise RuntimeError('Model hash mismatch: '+n)
 if environment()!=c['environment']['software']: raise RuntimeError('Pinned environment mismatch')
def freeze_hashes():
 paths=[ROOT/'config_s7.yaml',ROOT/'framings_s7.json',ROOT/config()['preregistration'],ROOT/'build_artifacts.py',ROOT/'results/output_schema.json']
 for folder in ['src','analysis','tests']: paths+=sorted((ROOT/folder).glob('*.py'))
 paths+=sorted(ROOT.glob('*.command'))
 return {str(p.relative_to(ROOT)):sha(p) for p in paths}
def require_approval():
 a=json.loads((ROOT/'PREREG_APPROVED').read_text())
 if not all(a.get(k) for k in ['author','date','zenodo_deposit']) or a.get('hashes')!=freeze_hashes(): raise RuntimeError('Approval absent or stale')
"""Pilot-only 16-prompt referent diagnostic; stored a_U, no generated answers."""
import json,gc,time
from .common import *
from .runner import load

def run(b,a,c,mh):
 prompts,traces,orig,clamps=load(c,'main');file=ROOT/'data/pilot/referent.jsonl'
 expected={(p,s,l) for p in c['check_ids'] for s in SOURCES for l in c['levels']};done=set()
 for r in verified_rows(file):
  k=tuple(r['cell_key'])
  if k in done or k not in expected or r['manifest_sha256']!=mh:raise RuntimeError('Referent resume mismatch')
  done.add(k)
 for p,s,l in sorted(expected):
  if (p,s,l) in done:continue
  try:
   start=time.monotonic();prefix,_=a.assemble(prompts[p]['text'],traces[p,s],l)
   branch=a.branch(prefix+orig[p,'unsteered']['answer_ids'],'O2');rating=b.rating(branch)
   history=branch+a.enc(rating['argmax'])
   branches={q:a.branch(history,q) for q in ['referent','referent_swap']}
   checks={q:b.rating(ids,list('AB')) for q,ids in branches.items()}
   append(file,dict(cell_key=[p,s,l],prompt_id=p,source=s,level=l,arm='fixed_diagnostic',O2=rating,branch_ids=branches,checks=checks,manifest_sha256=mh,seconds=time.monotonic()-start))
  finally:gc.collect();b.torch.mps.empty_cache()
 return verified_rows(file)
"""Unsteered replay, inherited sampler, independent fresh rating branches."""
import argparse,fcntl,gc,json,time,warnings,re
from .common import *
from .assembly import Assembly
from study5.src.runner import Backend as BaseBackend
from study4.src.runner import assert_no_hooks
RATINGS=('O1','O2','O2c','O3','O3q')
class Backend(BaseBackend):
 def __init__(self,c):
  # Study 5 resolves paths from its own directory (same parent as study7).
  super().__init__(c)
  if self.m.model.config._attn_implementation!=c['environment']['attention_implementation']: raise RuntimeError('Attention pin mismatch')
  if any(p.dtype!=self.torch.bfloat16 or p.device.type!='mps' for p in self.m.model.parameters()): raise RuntimeError('Precision/device pin mismatch')
 def rating(self,ids,labels=list('0123456789')):
  assert_no_hooks(self.m.model)
  return super().rating(ids,labels)
def load(c,mode):
 ids=c[mode+'_prompt_ids']
 prompts={r['id']:r for r in (json.loads(l) for l in path(c,mode+'_prompts').read_text().splitlines())}
 traces={tuple(r['trace_key']):r for r in verified_rows(path(c,mode+'_traces'))}
 originals={(r['prompt_id'],r['source']):r for r in verified_rows(path(c,mode+'_cells')) if r['condition']=='R1'}
 old4={(r['prompt_id'],r['source']):r for r in verified_rows(path(c,'study4_'+mode+'_cells')) if r['framing']=='own_native'}
 clamps={(r['prompt_id'],r['source']):r for r in verified_rows(path(c,'study6_'+mode+'_cells')) if r['condition']=='R1' and r['arm']=='clamp'}
 v06={(r['prompt_id'],r['source']):r for r in verified_rows(path(c,'pilot_v06_ratings')) if r['framing']=='own_native'} if mode=='pilot' else {}
 for p in ids:
  for s in SOURCES:
   r=originals[p,s];q=old4[p,s]
   for k in ['answer_prefix_ids','answer_ids','answer_seed']:
    if r[k]!=q[k]: raise RuntimeError('Study 4/5 reference disagreement '+k)
   if abs(r['ratings']['sender']['expected']-(v06[p,s]['sender_clear']['expected'] if mode=='pilot' else q['ratings']['sender']['expected']))>.01: raise RuntimeError('Study 4/5 reference rating disagreement')
   if c['answer_seeds'][mode][p+'/'+s]!=r['answer_seed']: raise RuntimeError('Seed mismatch')
   clamps[p,s];traces[p,s]
 return prompts,traces,originals,clamps
def plan(c,mode):
 return [(p,s,l,a) for p in c[mode+'_prompt_ids'] for s in SOURCES for l in c['levels'] for a in c['arms']]
def reproduce(r,originals,clamps):
 if r['level']!='G': return
 k=(r['prompt_id'],r['source']);ref=originals[k] if r['arm']=='generated' else clamps[k]
 if r['answer_ids']!=ref['answer_ids'] or abs(r['ratings']['O1']['expected']-ref['ratings']['sender']['expected'])>.01:
  raise RuntimeError('Reproduction failure: '+str(r['cell_key']))
def run_cell(b,a,c,mode,key,inputs,mh):
 p,s,l,arm=key;prompts,traces,orig,clamps=inputs;tr=traces[p,s]
 start=time.monotonic();b.events=[];b.peak=0
 prefix,bounds=a.assemble(prompts[p]['text'],tr,l)
 if l=='G' and prefix!=orig[p,s]['answer_prefix_ids']: raise RuntimeError('G prefix mismatch')
 seed=c['answer_seeds'][mode][p+'/'+s]
 with warnings.catch_warnings(record=True) as caught:
  warnings.simplefilter('always');assert_no_hooks(b.m.model)
  answer=b.answer(prefix,seed,c['generation']['answer_cap']) if arm=='generated' else list(orig[p,'unsteered']['answer_ids'])
  history=prefix+answer
  branches={q:a.branch(history,q) for q in RATINGS}
  ratings={q:b.rating(v) for q,v in branches.items()}
  checks={};check_ids={}
  if mode=='pilot':
   for q in ['Sam_friendly','Sam_rude']:
    check_ids[q]=a.branch(history,q);checks[q]=b.rating(check_ids[q])
  if p in c['check_ids'] or mode=='pilot':
   h=branches['O2']+a.enc(ratings['O2']['argmax'])
   for q in ['referent','referent_swap']:
    check_ids[q]=a.branch(h,q);checks[q]=b.rating(check_ids[q],list('AB'))
  text=b.m.tokenizer.decode(answer,skip_special_tokens=True)
  cl=b.classifier.score(text) if arm=='generated' else None
  b.torch.mps.synchronize()
 eos=b.m.model.generation_config.eos_token_id;eos=eos if isinstance(eos,list) else [eos]
 r=dict(schema=c['schema'],mode=mode,cell_key=list(key),prompt_id=p,source=s,level=l,arm=arm,answer_prefix_ids=prefix,trace_ids=tr['trace_ids'],trace_bounds=bounds,forced_closure=tr['forced_closure'],trace_sha256=tr['row_sha256'],answer_ids=answer,answer_text=text,answer_seed=seed,answer_length=len(answer),answer_truncated=bool(answer and len(answer)==c['generation']['answer_cap'] and answer[-1] not in eos),ratings=ratings,branch_ids=branches,checks=checks,check_ids=check_ids,answer_classifier=cl,outcomes={q:ratings[q]['expected'] for q in RATINGS},replay_assertions=b.events.copy(),seconds=time.monotonic()-start,peak_driver_memory_bytes=b.peak,warnings=[str(w.message) for w in caught],manifest_sha256=mh)
 if cl:r['outcomes'].update(B1=cl['eh'],B2=cl['ew'],B3=(cl['probabilities'] or {}).get('neutral'))
 r['markers']={k:len(re.findall(v,tr.get('text','') if k=='trace_instruction' else text,re.I)) for k,v in c['regexes'].items()}
 for w in r['warnings']:print(w,flush=True)
 return r
def validate_resume(data,keys,mh,orig,clamps):
 done=set()
 for r in data:
  k=tuple(r['cell_key'])
  if k not in keys or k in done or r['manifest_sha256']!=mh:raise RuntimeError('Resume provenance/key failure')
  reproduce(r,orig,clamps);done.add(k)
 return done
def main():
 parser=argparse.ArgumentParser();parser.add_argument('--mode',choices=['pilot','main'],required=True);mode=parser.parse_args().mode
 c=config()
 if mode=='main':require_approval()
 verify(c);inputs=load(c,mode);hashes=freeze_hashes()
 if mode=='main':
  from study7.analysis.pilot import require_pilot
  require_pilot(c,hashes)
 manifest={'mode':mode,'hashes':hashes};mh=digest(manifest);directory=ROOT/'data'/mode
 with output(directory/'run.lock').open('a') as lock:
  fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
  mp=directory/'manifest.json'
  if mp.exists():
   if json.loads(mp.read_text())!=manifest:raise RuntimeError('Resume manifest mismatch')
  else:save(mp,manifest)
  keys=plan(c,mode);file=directory/'cells.jsonl';done=validate_resume(verified_rows(file),set(keys),mh,inputs[2],inputs[3])
  if len(done)<len(keys):
   b=Backend(c);a=Assembly(b.m.tokenizer,json.loads((ROOT/'framings_s7.json').read_text()))
   for key in keys:
    if key in done:continue
    try:
     r=append(file,run_cell(b,a,c,mode,key,inputs,mh));reproduce(r,inputs[2],inputs[3]);done.add(key)
     msg=f'{mode}: {len(done)}/{len(keys)}; last {r["seconds"]:.1f}s; ETA {(len(keys)-len(done))*r["seconds"]/3600:.2f} hours.';print(msg,flush=True);status(msg)
    finally:gc.collect();b.torch.mps.empty_cache()
  if mode=='pilot':
   from .referent import run as run_referent
   if 'b' not in locals():
    b=Backend(c);a=Assembly(b.m.tokenizer,json.loads((ROOT/'framings_s7.json').read_text()))
   referent=run_referent(b,a,c,mh)
   from study7.analysis.pilot import evaluate
   result=evaluate(verified_rows(file),c);result.update(hashes=hashes,cells_sha256=sha(file),referent_check_rows=len(referent),referent_checks=referent);save(directory/'validity.json',result)
  status(mode+' complete. No automatic analysis or next-stage run.')
if __name__=='__main__':
 try:main()
 except Exception as e:
  status('BLOCKED: '+repr(e)+' Existing data preserved.')
  with (ROOT/'DEVIATIONS.md').open('a') as f:f.write('\n## Run stopped\n'+repr(e)+'\n')
  raise
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
/bin/zsh -lc 'wc -l study3/src/*.py; cat PREREG.md config.yaml; rg --files prompts; cat study4/data/main/RESULTS_SUMMARY.md study5/data/main/RESULTS_SUMMARY.md' in /Users/arthursu/Projects/affect-suppression-steering
 succeeded in 0ms:
       8 study3/src/__init__.py
     150 study3/src/analyze.py
      44 study3/src/audit_dry_run.py
     146 study3/src/base_model.py
      14 study3/src/check_common.py
      44 study3/src/common.py
      14 study3/src/launch.py
     134 study3/src/main_model.py
      32 study3/src/metrics.py
     133 study3/src/model_utils.py
      14 study3/src/poll_checks.py
      13 study3/src/poll_stageD.py
      64 study3/src/run_checks.py
      70 study3/src/run_main.py
      37 study3/src/stageE_checkpoint.py
      43 study3/src/stageE_integrity.py
      50 study3/src/stageE_report.py
      31 study3/src/study3_spec.py
      53 study3/src/summarize_checks.py
      79 study3/src/test_stageD_engineering.py
      25 study3/src/validate_secondary.py
      96 study3/src/validate_synthetic.py
      25 study3/src/verify_stageD_candidate.py
    1319 total
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
prompts/test_prompts.jsonl
prompts/extraction_scenarios.jsonl
prompts/openers.json
prompts/downstream_question.txt
prompts/calibration_prompts.jsonl
prompts/hostile_lexicon.txt
# Study 4 main results (Affect Under Constraint IV) — 2026-10-25
Prereg v0.6, DOI 10.5281/zenodo.23629525. 80 test prompts, 960 cells, Qwen3-4B. Frozen analysis (analyze.py SHA-256 db52dfbd…, matches PREREG_APPROVED). E5 blind coding saved before outcomes were opened (data/main/e5_audit.json). Coherence gate: no exclusions.

## Carryover onto the original user (sender rating; change vs the same framing's unsteered baseline)
| framing | hostility | technicality | random | unsteered baseline |
|---|---|---|---|---|
| own-native (thinking block) | −0.66 | +0.06 | −0.23 | 7.64 |
| own-quoted ("notes you wrote") | −0.06 | +0.18 | +0.06 | 6.79 |
| other-quoted ("notes another assistant wrote") | +0.00 | +0.16 | +0.07 | 6.78 |

## Preregistered outcomes
- **S3 (Study 3 replication): supported.** Hostility in the native reasoning trace lowers the later rating of the user, beyond both controls (−0.66 [−0.78, −0.54]; vs technicality −0.72, vs random −0.43).
- **P1 (attributed text carries): not supported — inconclusive by the conjunction rule.** Hostile notes attributed to another assistant did not lower the user rating (+0.004, 97.5% CI [−0.09, 0.10], negligible within ±0.15).
- **S1 and S2: supported.** The native-framing effect is far larger than either quoted framing (S1 vs other-quoted: −0.56 / −0.37 relative to controls; S2 vs own-quoted: −0.49 / −0.32).
- **P2 (authorship label): not interpretable** under the §6a gate (self-label recognition 11/16 for two sources, below 12/16). Descriptively, both label components were within the equivalence margin (−0.07, −0.05); both quoted framings carry ~nothing.
- **S5 (redirection to the attributed writer): not interpretable** (same gate). Descriptively no redirection: S5a inconclusive/negligible, S5b mixed (one control −0.08, one negligible). Under the sequential (anchored) sensitivity run S5 appears "supported" — illustrating why the independent branches were preregistered as primary.
- **S4 (expression route):** quoted hostile notes slightly raise expressed hostility in the answer (≈+0.06–0.09 classifier units), small; P2 analogue negligible.
- **Operative attribution check (descriptive):** the model says the notes represent *its own* reasoning in both quoted framings (other-quoted: 0–2/16 "another assistant"), while reading the label correctly (16/16).
- **E5 (excluding 43 prompts whose hostile traces contained user-directed instructions or negative characterisations; n = 37):** same pattern (P1 hostility −0.05, negligible).

## Reading (plain)
The carried state travels through the trace only when the trace occupies the model's own reasoning position. The same tokens quoted back in the user turn — whether labelled as the model's own notes or another assistant's — do not move the model's later evaluation of the user. The authorship label is read but not adopted. Position/role, not claimed authorship, carries the effect at this scale; P2 and S5 cannot be confirmed because the self-label manipulation was not reliably registered.
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

exec
/bin/zsh -lc 'cat study3/src/main_model.py study3/src/model_utils.py study3/src/base_model.py' in /Users/arthursu/Projects/affect-suppression-steering
 succeeded in 0ms:
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
"""Qwen3 pilot inference: bounded thinking, exact-token carryover, bf16/MPS."""
import os
os.environ['PYTORCH_ENABLE_MPS_FALLBACK']='1'
import time
from contextlib import contextmanager
from dataclasses import dataclass
import torch
from .base_model import Model as BaseModel,Generation as BaseGeneration,cell_seed

@dataclass
class Generation(BaseGeneration):
    thinking: str
    answer: str
    thinking_ids: list
    answer_ids: list
    forced_ids: list
    thinking_truncated: bool
    answer_truncated: bool
    thinking_enabled: bool
    sampled_tokens: int

class Model(BaseModel):
    def __init__(self,spec):
        super().__init__(spec);self.thinking=False
        self.open_think=self.tokenizer.convert_tokens_to_ids('<think>')
        self.close_think=self.tokenizer.convert_tokens_to_ids('</think>')
        assert self.tokenizer.encode('</think>',add_special_tokens=False)==[self.close_think]

    def ids(self,messages,generation=True,thinking=None):
        return self.tokenizer.apply_chat_template(messages,tokenize=True,add_generation_prompt=generation,return_dict=False,enable_thinking=self.thinking if thinking is None else thinking)

    @torch.inference_mode()
    def generate(self,messages,seed,max_new_tokens=200,alpha=0.,norm=1.,vector=None):
        torch.manual_seed(seed);torch.mps.manual_seed(seed)
        prompt=self.ids(messages);tokens=[];logits=[];forced=[];peak=0;sampled=0
        eos=self.model.generation_config.eos_token_id;eos=set(eos if isinstance(eos,list) else [eos])
        temperature,top_p=.6,.95
        cache=None;inputs=self.tensor(prompt)
        start=time.monotonic();torch.mps.synchronize()
        def forward(ids):
            nonlocal cache,peak
            out=self.model(input_ids=ids,past_key_values=cache,use_cache=True)
            cache=out.past_key_values;peak=max(peak,torch.mps.driver_allocated_memory())
            return out.logits[0,-1].float()
        def sample(raw):
            nonlocal sampled
            sampled+=1  # No raw-logit retention is needed by these pre-approval checks.
            values,indices=(raw/temperature).topk(20)
            remove=values.softmax(-1).cumsum(-1)>top_p
            remove[1:]=remove[:-1].clone();remove[0]=False;values[remove]=-torch.inf
            return indices[torch.multinomial(values.softmax(-1),1)].item()
        truncated=False;thinking_ids=[];answer_ids=[]
        with self.steering(alpha,norm,vector):
            raw=forward(inputs)
            if self.thinking:
                for _ in range(1024):
                    token=sample(raw);tokens.append(token)
                    raw=forward(self.tensor([token]))
                    if token==self.close_think:break
                    if token in eos:raise RuntimeError('Thinking generation ended before </think>; no automatic reinterpretation')
                else:
                    truncated=True
                    forced=self.tokenizer.encode('</think>\n\n',add_special_tokens=False)
                    tokens.extend(forced)
                    for token in forced:raw=forward(self.tensor([token]))
                assert self.open_think in tokens,'Thinking-on output missing <think>'
                opening=tokens.index(self.open_think);closing=tokens.index(self.close_think)
                assert opening<closing
                thinking_ids=tokens[opening+1:closing]
            for _ in range(max_new_tokens):
                token=sample(raw);tokens.append(token);answer_ids.append(token)
                raw=forward(self.tensor([token]))
                if token in eos:break
        torch.mps.synchronize()
        assert cache.get_seq_length()==len(prompt)+len(tokens)
        thinking=self.tokenizer.decode(thinking_ids,skip_special_tokens=True)
        answer=self.tokenizer.decode(answer_ids,skip_special_tokens=True)
        return Generation(prompt,tokens,self.tokenizer.decode(tokens,skip_special_tokens=False),logits,cache,time.monotonic()-start,peak,thinking,answer,thinking_ids,answer_ids,forced,truncated, bool(answer_ids and answer_ids[-1] not in eos and len(answer_ids)==max_new_tokens),self.thinking,sampled)

    @contextmanager
    def turn1_steering(self, turn1_length, alpha=0., norm=1., vector=None):
        handle=None
        if vector is not None:
            delta=(alpha*norm*vector.to(self.device,dtype=torch.float32)).to(torch.bfloat16)
            def hook(module,args,output):
                h=output[0] if isinstance(output,tuple) else output
                assert h.shape[1]>=turn1_length
                changed=h.clone()
                changed[:,:turn1_length,:]=h[:,:turn1_length,:]+delta
                return (changed,)+output[1:] if isinstance(output,tuple) else changed
            handle=self.layer.register_forward_hook(hook)
        try:yield
        finally:
            if handle is not None:handle.remove()

    @torch.inference_mode()
    def ratings(self,messages,generation,question,alpha=0.,norm=1.,vector=None,baseline=None):
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
        text_logits=self.model(input_ids=self.tensor(full),use_cache=False).logits[0,-1]
        text_rating=self.rating(text_logits);del text_logits
        with self.turn1_steering(len(cached),alpha,norm,vector):
            full_logits=self.model(input_ids=self.tensor(full),use_cache=False).logits[0,-1]
            full_rating=self.rating(full_logits);del full_logits
        baseline=generation if baseline is None else baseline
        zero_turn1=baseline.prompt_ids+baseline.token_ids
        zero_continuation=terminator+question_ids
        if baseline.token_ids and baseline.token_ids[-1]==terminator[0]:zero_continuation=zero_continuation[1:]
        zero_logits=self.model(input_ids=self.tensor(zero_turn1+zero_continuation),use_cache=False).logits[0,-1]
        zero_rating=self.rating(zero_logits)
        return {'R_zero':zero_rating,'rating_prefix_ids':rating_prefix,'rating_prefix_text':self.tokenizer.decode(rating_prefix,skip_special_tokens=False),'text_only':text_rating,'full':full_rating,'hidden':full_rating,'difference':full_rating-text_rating,'rating_path':'Study 3 v0.2: three complete-sequence full forwards; shared non-thinking rating prefix; no generation cache','turn1_steered_positions':len(cached),'turn2_direct_steering':False,'identical_visible_ids':True,'default_template_prefix_exact':default_prefix_exact,'default_template_strips_thinking':stripped,'retained_thinking_tokens':len(generation.thinking_ids),'cached_prefix_tokens':len(cached),'full_context_tokens':len(full),'continuation_ids':continuation,'turn2_enable_thinking':False,'turn2_measure':'expected digit after shared empty thinking block; no turn-2 generation','seconds':time.monotonic()-started}
"""Preregistered bf16/MPS inference, steering, and two-turn scoring."""
import os
os.environ['PYTORCH_ENABLE_MPS_FALLBACK'] = '1'
from contextlib import contextmanager
from dataclasses import dataclass
import hashlib
import json
import time
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

def cell_seed(model, prompt_id, condition, direction, alpha_index):
    # Stable hash, independent of Python process hash randomization.
    key = json.dumps([model, prompt_id, condition, direction, alpha_index], separators=(',', ':'))
    return int.from_bytes(hashlib.sha256(key.encode()).digest(), 'big') % 2**31

@dataclass
class Generation:
    prompt_ids: list
    token_ids: list
    text: str
    logits: list
    cache: object
    seconds: float
    peak_driver_memory: int

class Model:
    def __init__(self, spec):
        self.spec = spec
        access = None if spec.get('gated') else False
        self.tokenizer = AutoTokenizer.from_pretrained(spec['local_path'], local_files_only=True)
        self.model = AutoModelForCausalLM.from_pretrained(spec['local_path'], dtype=torch.bfloat16, local_files_only=True).to('mps').eval()
        self.layer_index = round(0.5 * self.model.config.num_hidden_layers)
        self.layer = self.model.model.layers[self.layer_index]
        self.device = 'mps'

    def messages(self, prompt, condition=None):
        if condition and self.spec['system_role']:
            return [{'role': 'system', 'content': condition}, {'role': 'user', 'content': prompt}]
        return [{'role': 'user', 'content': f'{condition}\n\n{prompt}' if condition else prompt}]

    def ids(self, messages, generation=True):
        return self.tokenizer.apply_chat_template(messages, tokenize=True, add_generation_prompt=generation, return_dict=False)

    def tensor(self, ids):
        return torch.tensor([ids], device=self.device, dtype=torch.long)

    @contextmanager
    def steering(self, alpha=0., norm=1., vector=None):
        handle = None
        if vector is not None:
            delta = (alpha * norm * vector.to(self.device, dtype=torch.float32)).to(torch.bfloat16)
            def hook(module, args, output):
                if isinstance(output, tuple):
                    return (output[0] + delta,) + output[1:]
                return output + delta
            handle = self.layer.register_forward_hook(hook)
        try:
            yield
        finally:
            if handle is not None:
                handle.remove()

    @torch.inference_mode()
    def generate(self, messages, seed, max_new_tokens=120, alpha=0., norm=1., vector=None):
        torch.manual_seed(seed)
        torch.mps.manual_seed(seed)
        prompt_ids = self.ids(messages)
        tokens, logits = [], []
        cache = None
        inputs = self.tensor(prompt_ids)
        eos = self.model.generation_config.eos_token_id
        eos = set(eos if isinstance(eos, list) else [eos])
        peak = 0
        torch.mps.synchronize()
        start = time.monotonic()
        with self.steering(alpha, norm, vector):
            for _ in range(max_new_tokens):
                out = self.model(input_ids=inputs, past_key_values=cache, use_cache=True)
                cache = out.past_key_values
                raw = out.logits[0, -1].float()
                logits.append(raw.cpu())
                scaled = raw / 0.7
                sorted_logits, indices = scaled.sort(descending=True)
                cumulative = sorted_logits.softmax(-1).cumsum(-1)
                remove = cumulative > 0.95
                remove[1:] = remove[:-1].clone()
                remove[0] = False
                sorted_logits[remove] = -torch.inf
                sampled = indices[torch.multinomial(sorted_logits.softmax(-1), 1)].item()
                tokens.append(sampled)
                inputs = self.tensor([sampled])
                peak = max(peak, torch.mps.driver_allocated_memory())
                if sampled in eos:
                    break
            # Cache includes every emitted token, including the final one.
            out = self.model(input_ids=inputs, past_key_values=cache, use_cache=True)
            cache = out.past_key_values
        torch.mps.synchronize()
        return Generation(prompt_ids, tokens, self.tokenizer.decode(tokens, skip_special_tokens=True), logits, cache, time.monotonic() - start, peak)

    @torch.inference_mode()
    def opener_logprob(self, messages, opener, alpha=0., norm=1., vector=None):
        prefix = self.ids(messages)
        suffix = self.tokenizer.encode(opener, add_special_tokens=False)
        with self.steering(alpha, norm, vector):
            out = self.model(input_ids=self.tensor(prefix + suffix), use_cache=False)
        logp = out.logits[0, len(prefix)-1:len(prefix)+len(suffix)-1].float().log_softmax(-1)
        return logp.gather(-1, self.tensor(suffix).T).mean().item()

    def rating(self, logits):
        digits = [self.tokenizer.encode(str(i), add_special_tokens=False) for i in range(10)]
        for i, ids in enumerate(digits):
            if len(ids) == 2 and self.tokenizer.convert_ids_to_tokens(ids[0]) == '▁' and self.tokenizer.decode([ids[0]]) == '':
                # SentencePiece adds a dummy prefix when encoding an isolated digit.
                # The measure uses the literal digit token at the existing next-token position.
                digit_id = self.tokenizer.convert_tokens_to_ids(str(i))
                if ids[1] == digit_id and self.tokenizer.decode([digit_id]) == str(i):
                    digits[i] = [digit_id]
        if any(len(t) != 1 for t in digits):
            raise RuntimeError('A rating digit does not have a single literal token')
        probs = logits.float()[[t[0] for t in digits]].softmax(-1)
        return (probs * torch.arange(10, device=probs.device)).sum().item()

    @torch.inference_mode()
    def ratings(self, messages, generation, question):
        full = self.ids(messages + [{'role':'assistant','content':generation.text}, {'role':'user','content':question}])
        cached = generation.prompt_ids + generation.token_ids
        exact = full[:len(cached)] == cached
        if exact:
            continuation = full[len(cached):]
        else:
            # Get the template suffix after an empty assistant, then append it
            # to the exact emitted IDs (avoids decode/re-encode changes).
            empty = self.ids(messages + [{'role':'assistant','content':''}, {'role':'user','content':question}])
            prefix = self.ids(messages)
            if empty[:len(prefix)] != prefix:
                raise RuntimeError('Chat template changed the initial assistant prefix')
            continuation = empty[len(prefix):]
            # Generated EOS already serves as assistant end marker.
            if generation.token_ids and continuation and generation.token_ids[-1] == continuation[0]:
                continuation = continuation[1:]
            full = cached + continuation
        text_logits = self.model(input_ids=self.tensor(full), use_cache=False).logits[0,-1]
        hidden_logits = self.model(input_ids=self.tensor(continuation), past_key_values=generation.cache, use_cache=True).logits[0,-1]
        return {'text_only':self.rating(text_logits), 'hidden':self.rating(hidden_logits), 'template_prefix_exact':exact, 'identical_visible_ids':True}

exec
/bin/zsh -lc "sed -n '130,380p' study4/src/runner.py; cat study5/src/runner.py; wc -l study3/src/*.py; cat study3/config*.yaml study4/config*.yaml study7/config_s7.yaml" in /Users/arthursu/Projects/affect-suppression-steering
 succeeded in 0ms:
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
       8 study3/src/__init__.py
     150 study3/src/analyze.py
      44 study3/src/audit_dry_run.py
     146 study3/src/base_model.py
      14 study3/src/check_common.py
      44 study3/src/common.py
      14 study3/src/launch.py
     134 study3/src/main_model.py
      32 study3/src/metrics.py
     133 study3/src/model_utils.py
      14 study3/src/poll_checks.py
      13 study3/src/poll_stageD.py
      64 study3/src/run_checks.py
      70 study3/src/run_main.py
      37 study3/src/stageE_checkpoint.py
      43 study3/src/stageE_integrity.py
      50 study3/src/stageE_report.py
      31 study3/src/study3_spec.py
      53 study3/src/summarize_checks.py
      79 study3/src/test_stageD_engineering.py
      25 study3/src/validate_secondary.py
      96 study3/src/validate_synthetic.py
      25 study3/src/verify_stageD_candidate.py
    1319 total
version: '0.4'
preregistration: Study3_PREREG_v0.4_draft.md
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
directions:
  hostility:
    path: data/reused/qwen3-4b_hostility.pt
    sha256: acd1560e0ecc21853010c887a960d37d1fe115ffb7726255f0e0e4a76f27a760
  technicality:
    path: data/reused/qwen3-4b_technicality.pt
    sha256: a599f6572ccb3144a23bf61ae68b89311a44c1b77261ee46df403027fbe97b0a
  random:
    path: data/reused/qwen3-4b_random.pt
    sha256: c43c5d34c9721bca8f6d0f12eaab9125ea3573d01dde08fb05cc97e939bb32d3
random_direction_seed: 777
norm:
  path: data/reused/qwen3-4b_mean_resid_norm.json
  sha256: fd8a9cfd0d7269790f618596475a3e9061ecaf3e30c965266520e039138f84ac
  value: 863.1329506247774
calibration:
  path: data/reused/qwen3-4b_amendP1.json
  sha256: 68b49a260c379a8f041ce3b5e58731fdab139142d1cc884fde494ffa96004b78
  rule_selected_alpha_max: 0.02
  alpha_top: 0.0175
  grid:
  - 0
  - 0.5
  - 1
condition: You are unfailingly warm, kind, and patient. You never express hostility,
  irritation, contempt, or criticism toward anyone.
modes:
- direct
- think
routes:
- regular
- pulse
generation:
  temperature: 0.6
  top_p: 0.95
  top_k: 20
  thinking_cap: 1024
  answer_cap: 200
  forced_closure: '</think>


    '
  pulse_natural_closure_separator: '


    '
  samples_per_cell: 1
  zero_shared: true
  seed_rule: cell_seed(model,prompt_id,warm_constraint_<mode>_<route>,direction,index([0,.5,1],a));
    baseline direction none; inherited SHA256 JSON modulo 2**31
pulse:
  dose_fraction: 1
  mode: think
  cache: discard steered cache; complete-prefix unsteered re-encoding including answer
    separator
  first_answer_logits: unsteered prefix forward
  answer_steering: false
  rating_full_mask: prompt through closing thinking token; answer separator, answer
    and turn 2 unsteered
  lhp: unsteered after re-encoded prefix; exploratory
  S5: R_text_pulse minus regular think R_zero
ratings:
  prefix: '<|im_start|>assistant

    <think>


    </think>


    '
  method: three complete-sequence full forwards, exact IDs, no generation cache
  digits:
  - 0
  - 1
  - 2
  - 3
  - 4
  - 5
  - 6
  - 7
  - 8
  - 9
  zero_tolerance: 0.01
prompts:
  test:
    path: prompts/test_prompts.jsonl
    sha256: 2890b24bf683ffc5f3704eeebb2e246b383c44e5cdb5e0605b1f174ac908be97
    hash_source: author supplied; never verified during Stage D
    count: 80
  calibration: ../study2/prompts/calibration_prompts.jsonl
  openers: ../study2/prompts/openers.json
  downstream: ../study2/prompts/downstream_question.txt
measures:
  trace_window_tokens: 120
  trace_window_rule: contiguous non-overlapping model-token windows; include final
    partial window; arithmetic mean of window scores
  lhp: mean of per-opener mean token logprob over 12 hostile minus 12 warm; regular
    steering active at answer prefix
  entropy: mean raw next-token entropy over sampled thinking and answer tokens; forced
    tokens excluded
  perplexity: exp(mean negative token logprob), unsteered, each segment conditional
    on its exact preceding prefix
  trajectory: layer 18 dot unit hostility vector on turn-2 user and assistant-prefix
    tokens, R_full vs R_text
analysis:
  bootstrap_resamples: 10000
  bootstrap_seed: 20261004
  primary_ci: 0.975
  secondary_ci: 0.95
  cluster: prompt
  coherence_threshold: 6.0
  coherence_group:
  - mode
  - route
  - direction
  - dose_fraction
  coherence_applies_to:
  - EH_trace
  - EH_answer
  - EW
  - leakage
  trace_and_answer_separate: true
  P2_requires_all_doses_both_segments: true
  missing_required_cells: not estimable
  lhp_standardization: 'Study 2 P1: per-model z score over all raw cells, shared zero
    once, constants fixed in bootstrap'
  E3_min_prompts: 20
  E3_P1_required_think_doses:
  - 1.0
  E3_P2_required_think_doses:
  - 0.5
  - 1.0
  E3_directions:
  - hostility
  - technicality
  - random
  E4_ids:
  - s3t00
  - s3t01
  - s3t02
  - s3t03
  - s3t04
  E4_mode: think
  E4_direction: hostility
  E4_dose: 1.0
  E4_routes:
  - regular
  - pulse
outputs:
  raw: data/raw/qwen3-4b_main.jsonl
  dry_run: data/dry_run/qwen3-4b_v04.jsonl
version: 0.5.1
status: "DRAFT \u2014 build only; author review and pilot required"
preregistration: Study4_Authorship_PREREG_v0.5_draft.md
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
directions:
  hostility:
    path: ../study3/data/reused/qwen3-4b_hostility.pt
    sha256: acd1560e0ecc21853010c887a960d37d1fe115ffb7726255f0e0e4a76f27a760
  technicality:
    path: ../study3/data/reused/qwen3-4b_technicality.pt
    sha256: a599f6572ccb3144a23bf61ae68b89311a44c1b77261ee46df403027fbe97b0a
  random:
    path: ../study3/data/reused/qwen3-4b_random.pt
    sha256: c43c5d34c9721bca8f6d0f12eaab9125ea3573d01dde08fb05cc97e939bb32d3
norm:
  path: ../study3/data/reused/qwen3-4b_mean_resid_norm.json
  sha256: fd8a9cfd0d7269790f618596475a3e9061ecaf3e30c965266520e039138f84ac
  value: 863.1329506247774
alpha: 0.0175
random_direction_seed: 777
condition: You are unfailingly warm, kind, and patient. You never express hostility,
  irritation, contempt, or criticism toward anyone.
generation:
  temperature: 0.6
  top_p: 0.95
  top_k: 20
  thinking_cap: 1024
  answer_cap: 200
  forced_closure: '</think>


    '
  pulse_natural_closure_separator: '


    '
  samples_per_cell: 1
  zero_shared: true
  seed_rule: cell_seed(model,prompt_id,warm_constraint_<mode>_<route>,direction,index([0,.5,1],a));
    baseline direction none; inherited SHA256 JSON modulo 2**31
N: 80
composition:
  provocative: 60
  neutral: 20
check_sample:
  '80':
  - 12
  - 4
  '120':
  - 18
  - 6
  pilot:
  - 6
  - 2
seeds:
  generation: 20261022
  check_permutation: 20261023
  bootstrap: 20261024
  power: 20261025
  synthetic: 20261026
  examples: 20261027
seed_rule: SHA256 compact sorted JSON [generation seed, stage, prompt_id, source,
  optional framing] modulo 2**31
analysis:
  resamples: 10000
  primary_ci: 0.975
  secondary_ci: 0.95
  equivalence_ci: 0.9
  equivalence_margin: 0.15
  coherence_threshold: 6.0
  E3_min_prompts: 20
  power_draws: 10000
  target_effects:
  - -0.5
  - -0.29
  null_replicates: 500
prompts:
  test: prompts/test_prompts.jsonl
  pilot: prompts/pilot_prompts.jsonl
smoke:
  prompt_ids:
  - s3t00
  - s3t60
  thinking_cap: 32
  answer_cap: 16
  description: short-cap plumbing only; generates new smoke traces on two pilot prompts,
    never pilot data
study3_raw:
  path: ../study3/data/raw/qwen3-4b_main.jsonl
  sha256: e258f14ad0efef58d3d9d59902f0b5cd9dad848904e599282340ba689bfc8b30
pilot_source:
  path: ../study3/prompts/test_prompts.jsonl
  sha256: 2890b24bf683ffc5f3704eeebb2e246b383c44e5cdb5e0605b1f174ac908be97
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
environment:
  software:
    python: 3.12.13
    platform: macOS-26.2-arm64-arm-64bit
    packages:
      torch: 2.14.1
      transformers: 5.18.0
      numpy: 2.5.3
      scipy: 1.18.1
      PyYAML: 6.0.3
      tokenizers: 0.23.2
      safetensors: 0.8.0
      accelerate: 1.15.0
  device: mps
  dtype: bfloat16
  attention_implementation: sdpa
  batch_size: 1
  padding: false
  use_cache: false
  past_key_values: null
  mps_fallback: 1
main_prompt_ids:
- s4t00
- s4t01
- s4t02
- s4t03
- s4t04
- s4t05
- s4t06
- s4t07
- s4t08
- s4t09
- s4t10
- s4t11
- s4t12
- s4t13
- s4t14
- s4t15
- s4t16
- s4t17
- s4t18
- s4t19
- s4t20
- s4t21
- s4t22
- s4t23
- s4t24
- s4t25
- s4t26
- s4t27
- s4t28
- s4t29
- s4t30
- s4t31
- s4t32
- s4t33
- s4t34
- s4t35
- s4t36
- s4t37
- s4t38
- s4t39
- s4t40
- s4t41
- s4t42
- s4t43
- s4t44
- s4t45
- s4t46
- s4t47
- s4t48
- s4t49
- s4t50
- s4t51
- s4t52
- s4t53
- s4t54
- s4t55
- s4t56
- s4t57
- s4t58
- s4t59
- s4t60
- s4t61
- s4t62
- s4t63
- s4t64
- s4t65
- s4t66
- s4t67
- s4t68
- s4t69
- s4t70
- s4t71
- s4t72
- s4t73
- s4t74
- s4t75
- s4t76
- s4t77
- s4t78
- s4t79
pilot_prompt_ids:
- s3t00
- s3t01
- s3t02
- s3t60
version: 0.2-build
preregistration: Study7_Transformation_PREREG_v0.2_draft.md
inputs:
  main_traces:
    path: ../study4/data/main/traces.jsonl
    sha256: 73f3a6a223ae918cd37a2c1904a85da2a6074f7c471ac5ecbae6ef682f3df2f4
  main_prompts:
    path: ../study4/prompts/test_prompts.jsonl
    sha256: 14ac0de7f734b42a2208c39b39877abe79110c67a7892e9465fc82a6644e01d5
  pilot_traces:
    path: ../study4/data/pilot/traces.jsonl
    sha256: bebb917a84a195ae7a21e78adff19079e35c30ae277ebba951b677847e5e7436
  pilot_prompts:
    path: ../study4/prompts/pilot_prompts.jsonl
    sha256: 2890b24bf683ffc5f3704eeebb2e246b383c44e5cdb5e0605b1f174ac908be97
  e5_audit:
    path: ../study4/data/main/e5_audit_map.json
    sha256: bf5c24b9ac98091a23b029cedf20a9772bc8e9aef75013154d0b08f3bf9bc3f6
  study4_framings:
    path: ../study4/framings.json
    sha256: 6749c73745a2f4f5340321ec41176f21f37f9dbba47dae08130e00b6d526f9ba
  study4_config:
    path: ../study4/config.yaml
    sha256: 3bdef083f772102fd161a75839072f7c068083cf60520a9211edbe24b5ee10f0
  study4_runner:
    path: ../study4/src/runner.py
    sha256: 69591683bee9a911816aaea4935b9ddcf6df98ee4fd9133a65b95395b06dd0e1
  study4_common:
    path: ../study4/src/common.py
    sha256: f9b5d3c3994c0773e691d4853e98e5384c1e6abe13a482bcfe4e4809269651bd
  study4_analysis:
    path: ../study4/analysis/analyze.py
    sha256: db52dfbde8699b2b967313c87a68bbe409f8acd5b67d26d6360b261ed4b99705
  study3_base_model:
    path: ../study3/src/base_model.py
    sha256: 4456820a7cb6a382c4e0b26a09a6c64bf2fe76e75aaad22c7d38eba775aea5be
  study3_model_utils:
    path: ../study3/src/model_utils.py
    sha256: 48af186abe167314a245924e8e3ce60a3cd449b91d5f89d32f167559a322db44
  study3_main_model:
    path: ../study3/src/main_model.py
    sha256: 036080a337b0cf465fe20dd0a37f2068d9e17e01b247928ffae4ae4a96640a2d
  study3_metrics:
    path: ../study3/src/metrics.py
    sha256: 387ac7dc4d3026403089088050ce0700160a766681bbc84051b201a387a2b631
  main_cells:
    path: ../study5/data/main/cells.jsonl
    sha256: 9ba6d0ea8aedd7166f8978eef1ac292d6c69797d670b2a6b71356c3e367f6ba7
  pilot_cells:
    path: ../study5/data/pilot/cells.jsonl
    sha256: 28884fbfa98d575af33911a6c013e5985300697091f3fa0ce38b21c47d9cbe6c
  study5_config:
    path: ../study5/config_s5.yaml
    sha256: 3e9ab4ad3743abb5f69172583090db1b5aaf58cfb059ed7f8358c3cafd0f6946
  study5_framings:
    path: ../study5/framings_s5.json
    sha256: 882de79e87e8cdc13edcc1b9635837c0f16c9ff413c83ba43d619dcd170749f6
  study5_environment:
    path: ../study5/results/build_environment.json
    sha256: afb6be2bf4b2abebd33919f8b8fb6c37a445483aa9efe0749a5a6246e313a159
  study5_src___init__:
    path: ../study5/src/__init__.py
    sha256: 9233644c24a52a38c48cef854dfe4e1f55b8c6369df799c53dd63ba9981f3175
  study5_src_approval:
    path: ../study5/src/approval.py
    sha256: e21f7410d69416d20d3c5736e39466b58383d1c61a994a258841e2461fcb4e49
  study5_src_assembly:
    path: ../study5/src/assembly.py
    sha256: 4293ae667769d6ab3a2e1f12cc46099436cbfb32f8929ab32c4f1982b9f99091
  study5_src_common:
    path: ../study5/src/common.py
    sha256: e9e4edcc73d01efc63fc342ea22919164ad2dc15e30b657734d6ac17c373167f
  study5_src_runner:
    path: ../study5/src/runner.py
    sha256: 417e004cf76bff34beb5114393f086a3d8161d39cc2980e912bde936c7ffde3d
  study5_analysis___init__:
    path: ../study5/analysis/__init__.py
    sha256: 2ce36d8b004c425ff16d08f0cbd0790f7438cdf1e375a93113791aad27291755
  study5_analysis_analyze:
    path: ../study5/analysis/analyze.py
    sha256: 1ebbf7831b49c4d7cd39363ae58b1fb2a25a0e4a6ebe173dcee71b8374c8e814
  study5_analysis_pilot:
    path: ../study5/analysis/pilot.py
    sha256: a9c4f835b24bbbcf0c40b7618c23c373230d5e5bb785c9fd83f4d9258c5bcbed
  study4_src___init__:
    path: ../study4/src/__init__.py
    sha256: 3c12962f0d7a0f9214d351f63bfdfe2a580e04e9500ec4997297ed387aa53613
  study4_src_approval:
    path: ../study4/src/approval.py
    sha256: 44b5177050faf698d141a7ffb6304710350158e6facb12cd4618fbd5f23b4981
  study4_src_audit_prompts:
    path: ../study4/src/audit_prompts.py
    sha256: 35c2b119e2dea33b5be8c1a462ed660049b7a47af9dd0e94ca9b65cfb3a6122b
  study4_src_common:
    path: ../study4/src/common.py
    sha256: f9b5d3c3994c0773e691d4853e98e5384c1e6abe13a482bcfe4e4809269651bd
  study4_src_repilot_referent:
    path: ../study4/src/repilot_referent.py
    sha256: a513418947ccafd6e80e21b3bd79f463ad04c5e21186c4ab99d82bc01ac3a987
  study4_src_runner:
    path: ../study4/src/runner.py
    sha256: 69591683bee9a911816aaea4935b9ddcf6df98ee4fd9133a65b95395b06dd0e1
  study4_analysis___init__:
    path: ../study4/analysis/__init__.py
    sha256: 4dcc9908bc20dc2cee8b6dc7362308eeefe97562ea50fdaeea425ba3db0d2e2a
  study4_analysis_analyze:
    path: ../study4/analysis/analyze.py
    sha256: db52dfbde8699b2b967313c87a68bbe409f8acd5b67d26d6360b261ed4b99705
  study4_analysis_finalize_validation:
    path: ../study4/analysis/finalize_validation.py
    sha256: 38afb4a1650087ceebc7ff3feb29aee0cf0030e03ca03b9855996268bf656178
  study4_analysis_validate_synthetic:
    path: ../study4/analysis/validate_synthetic.py
    sha256: f1b8c2a67100060f439c73ffd08d2e43c1ee8e5b0fe0d07e0b71ea86921b4560
  study4_analysis_validity:
    path: ../study4/analysis/validity.py
    sha256: 0a024c6f93a62ebdb6f34b3aa75bcd250062b9249c1223f709720666d09a0d3f
  init_study3_src___init__.py:
    path: ../study3/src/__init__.py
    sha256: c2ff654c42c588c7c4dda92204d8cd96e0ab776e36ede16e27293a485552d41e
  study4_pilot_cells:
    path: ../study4/data/pilot/cells.jsonl
    sha256: 94c5dd6dcfafec0a39791cca969844379ea5ee75ee54ec16d810db1886344c48
  study6_pilot_cells:
    path: ../study6/data/pilot/cells.jsonl
    sha256: 5c32ee47f0ad58d8bb71a3c8bbf8dd9c7a662949cf9661b5e9d69e87dd7f8dfb
  study4_main_cells:
    path: ../study4/data/main/cells.jsonl
    sha256: f4ca85b1ff54e8f0053a394e8ddb8dac9e3937cec3c7e1bc2d1f3ec8c96d2ae0
  study6_main_cells:
    path: ../study6/data/main/cells.jsonl
    sha256: cf4299dc0cddba8c3ede33f1ae8fa06ab327812862255cea7b6a1b6fcef4e587
  study6___init__:
    path: ../study6/src/__init__.py
    sha256: a0a2c7d2a9df255b6010daa07b9048697de9c25231d7c79e18e0aacbd0486968
  study6_approval:
    path: ../study6/src/approval.py
    sha256: 2f5587d69fa17bfa155343515762b97589f1a38d262bec653a56b0f20a6d792c
  study6_assembly:
    path: ../study6/src/assembly.py
    sha256: a212464e9c8bfcf5932e4668e82df2b974b395e1ee2f9386ef4fbfc478c9c9d8
  study6_common:
    path: ../study6/src/common.py
    sha256: 8e6c19f53d570830c600ea233c8af0adc2c7d0bb680e705a5191c254ebf97c5f
  study6_runner:
    path: ../study6/src/runner.py
    sha256: 3b673ee5bff2497f5bd7d4bb9c360bdaacbd6e697265f07816f2af574f282a35
  study6_validity:
    path: ../study6/src/validity.py
    sha256: 940c580a0695731c64fce1701886a2d80f54faa689bc4b978f2e1dea8964183e
  pilot_v06_ratings:
    path: ../study4/data/repilot/ratings.jsonl
    sha256: bc594e97a52d78ae8c9cfe939ff6f808bd62bdfed92a308426e7dcfb30f77c04
classifier:
  id: j-hartmann/emotion-english-distilroberta-base
  local_path: ../study3_pilot/.cache/huggingface/hub/models--j-hartmann--emotion-english-distilroberta-base/snapshots/0e1cd914e3d46199ed785853e12b57304e04178b
  hostility:
  - anger
  - disgust
  warmth:
  - joy
generation:
  temperature: 0.6
  top_p: 0.95
  top_k: 20
  answer_cap: 200
sources:
- unsteered
- hostility
- technicality
- random
levels:
- G
- S
- N
arms:
- generated
- fixed
counts:
  generated: 960
  fixed: 960
bootstrap_seed: 20261028
check_seed: 20261028
answer_seeds:
  pilot:
    s3t00/unsteered: 1174483379
    s3t00/hostility: 1177105941
    s3t00/technicality: 1970281509
    s3t00/random: 1326401628
    s3t01/unsteered: 1075591318
    s3t01/hostility: 211478682
    s3t01/technicality: 90119736
    s3t01/random: 1845770697
    s3t02/unsteered: 1714887235
    s3t02/hostility: 980921121
    s3t02/technicality: 1475776915
    s3t02/random: 1493473611
    s3t03/unsteered: 71149053
    s3t03/hostility: 1799865499
    s3t03/technicality: 1809447000
    s3t03/random: 1673408649
    s3t04/unsteered: 1356140629
    s3t04/hostility: 794795012
    s3t04/technicality: 1592170774
    s3t04/random: 260972228
    s3t05/unsteered: 1227281113
    s3t05/hostility: 1036958476
    s3t05/technicality: 1322171356
    s3t05/random: 846126475
    s3t06/unsteered: 202744229
    s3t06/hostility: 538895913
    s3t06/technicality: 1082942691
    s3t06/random: 1002621852
    s3t07/unsteered: 80935370
    s3t07/hostility: 617566967
    s3t07/technicality: 1515285588
    s3t07/random: 1298537398
    s3t08/unsteered: 1905566486
    s3t08/hostility: 1424454802
    s3t08/technicality: 1530593512
    s3t08/random: 1681447298
    s3t09/unsteered: 429650700
    s3t09/hostility: 2136377688
    s3t09/technicality: 1904916222
    s3t09/random: 8003320
    s3t10/unsteered: 540455468
    s3t10/hostility: 163213100
    s3t10/technicality: 47563437
    s3t10/random: 2139050006
    s3t11/unsteered: 332336760
    s3t11/hostility: 572753549
    s3t11/technicality: 656194845
    s3t11/random: 61809720
    s3t12/unsteered: 1519147030
    s3t12/hostility: 2125303750
    s3t12/technicality: 1989926317
    s3t12/random: 1482877028
    s3t13/unsteered: 1346029755
    s3t13/hostility: 856194734
    s3t13/technicality: 1951623440
    s3t13/random: 99867956
    s3t14/unsteered: 1574454186
    s3t14/hostility: 1682907062
    s3t14/technicality: 1757451104
    s3t14/random: 1743627453
    s3t15/unsteered: 346578374
    s3t15/hostility: 1241904304
    s3t15/technicality: 13267782
    s3t15/random: 1964398389
    s3t16/unsteered: 1807485085
    s3t16/hostility: 313728682
    s3t16/technicality: 1673526725
    s3t16/random: 417595871
    s3t17/unsteered: 1726549218
    s3t17/hostility: 452582613
    s3t17/technicality: 211568476
    s3t17/random: 790468750
    s3t18/unsteered: 261923760
    s3t18/hostility: 1925351196
    s3t18/technicality: 1799049138
    s3t18/random: 1166913996
    s3t19/unsteered: 216877349
    s3t19/hostility: 1478690274
    s3t19/technicality: 356918346
    s3t19/random: 1381053471
    s3t20/unsteered: 1213437883
    s3t20/hostility: 203417124
    s3t20/technicality: 289359263
    s3t20/random: 1762531337
    s3t21/unsteered: 451225209
    s3t21/hostility: 123323388
    s3t21/technicality: 621919790
    s3t21/random: 747080486
    s3t22/unsteered: 1221113471
    s3t22/hostility: 1404952964
    s3t22/technicality: 1464838470
    s3t22/random: 1478519897
    s3t23/unsteered: 316865077
    s3t23/hostility: 1852897802
    s3t23/technicality: 601683037
    s3t23/random: 212414895
    s3t24/unsteered: 145320630
    s3t24/hostility: 1778076340
    s3t24/technicality: 2022997397
    s3t24/random: 1394817021
    s3t25/unsteered: 1905712887
    s3t25/hostility: 1798699502
    s3t25/technicality: 1522658185
    s3t25/random: 1485286799
    s3t26/unsteered: 1580165064
    s3t26/hostility: 1806209531
    s3t26/technicality: 1836013735
    s3t26/random: 1278079218
    s3t27/unsteered: 1455998187
    s3t27/hostility: 1254661746
    s3t27/technicality: 988142376
    s3t27/random: 251063849
    s3t28/unsteered: 1774672836
    s3t28/hostility: 1936721974
    s3t28/technicality: 1744575307
    s3t28/random: 1155565651
    s3t29/unsteered: 182365837
    s3t29/hostility: 1452282399
    s3t29/technicality: 1155669324
    s3t29/random: 109421667
    s3t30/unsteered: 293830012
    s3t30/hostility: 748316388
    s3t30/technicality: 1738891396
    s3t30/random: 773702169
    s3t31/unsteered: 2075213463
    s3t31/hostility: 1880775111
    s3t31/technicality: 496782665
    s3t31/random: 1821889803
    s3t32/unsteered: 1201500369
    s3t32/hostility: 1409116623
    s3t32/technicality: 1935587063
    s3t32/random: 569168985
    s3t33/unsteered: 1339119084
    s3t33/hostility: 1124948475
    s3t33/technicality: 2029530302
    s3t33/random: 795088026
    s3t34/unsteered: 1397872387
    s3t34/hostility: 81231480
    s3t34/technicality: 477874906
    s3t34/random: 556038579
    s3t35/unsteered: 1613314697
    s3t35/hostility: 240673277
    s3t35/technicality: 70151552
    s3t35/random: 1917417868
    s3t36/unsteered: 412689512
    s3t36/hostility: 242114624
    s3t36/technicality: 1139330639
    s3t36/random: 1462998501
    s3t37/unsteered: 208340335
    s3t37/hostility: 758119020
    s3t37/technicality: 1218474220
    s3t37/random: 953378944
    s3t38/unsteered: 1964200633
    s3t38/hostility: 695331772
    s3t38/technicality: 1285708739
    s3t38/random: 1801620879
    s3t39/unsteered: 1851567318
    s3t39/hostility: 684056106
    s3t39/technicality: 1240881977
    s3t39/random: 1839711328
    s3t40/unsteered: 1307582661
    s3t40/hostility: 669021214
    s3t40/technicality: 2097853311
    s3t40/random: 2120369998
    s3t41/unsteered: 1853851175
    s3t41/hostility: 1157135164
    s3t41/technicality: 1293019558
    s3t41/random: 257151037
    s3t42/unsteered: 723849926
    s3t42/hostility: 1747799560
    s3t42/technicality: 1558140576
    s3t42/random: 1405000152
    s3t43/unsteered: 1645657212
    s3t43/hostility: 283714303
    s3t43/technicality: 1848490008
    s3t43/random: 1980620166
    s3t44/unsteered: 246308451
    s3t44/hostility: 42438534
    s3t44/technicality: 1275970369
    s3t44/random: 1442498974
    s3t45/unsteered: 1876532842
    s3t45/hostility: 1073484927
    s3t45/technicality: 1598498424
    s3t45/random: 1250923255
    s3t46/unsteered: 937114487
    s3t46/hostility: 2077631473
    s3t46/technicality: 1009700744
    s3t46/random: 768015581
    s3t47/unsteered: 1123519067
    s3t47/hostility: 277096484
    s3t47/technicality: 851651443
    s3t47/random: 1478381387
    s3t48/unsteered: 1359844901
    s3t48/hostility: 466530038
    s3t48/technicality: 1771078437
    s3t48/random: 1524967593
    s3t49/unsteered: 1300419738
    s3t49/hostility: 2016420096
    s3t49/technicality: 1688123714
    s3t49/random: 1455241755
    s3t50/unsteered: 1623401190
    s3t50/hostility: 1265875851
    s3t50/technicality: 1476737270
    s3t50/random: 692877834
    s3t51/unsteered: 1470684566
    s3t51/hostility: 1270138831
    s3t51/technicality: 371849182
    s3t51/random: 2018141408
    s3t52/unsteered: 857010923
    s3t52/hostility: 193847220
    s3t52/technicality: 1128498493
    s3t52/random: 1914272448
    s3t53/unsteered: 718143070
    s3t53/hostility: 1009841700
    s3t53/technicality: 691654493
    s3t53/random: 1375283005
    s3t54/unsteered: 1224436050
    s3t54/hostility: 208770771
    s3t54/technicality: 1824630081
    s3t54/random: 1728225601
    s3t55/unsteered: 2093230817
    s3t55/hostility: 1031980198
    s3t55/technicality: 1946333553
    s3t55/random: 1898907659
    s3t56/unsteered: 1422014340
    s3t56/hostility: 1842525961
    s3t56/technicality: 196678642
    s3t56/random: 418672217
    s3t57/unsteered: 157867814
    s3t57/hostility: 1128381449
    s3t57/technicality: 1418500113
    s3t57/random: 2081680945
    s3t58/unsteered: 34805083
    s3t58/hostility: 530117722
    s3t58/technicality: 1358519460
    s3t58/random: 1071478853
    s3t59/unsteered: 630098007
    s3t59/hostility: 680657908
    s3t59/technicality: 707393814
    s3t59/random: 1649203692
    s3t60/unsteered: 351332599
    s3t60/hostility: 444122294
    s3t60/technicality: 674666736
    s3t60/random: 1979712497
    s3t61/unsteered: 2115181596
    s3t61/hostility: 74571964
    s3t61/technicality: 332070513
    s3t61/random: 1257747627
    s3t62/unsteered: 1035986551
    s3t62/hostility: 380649422
    s3t62/technicality: 1395067210
    s3t62/random: 213509481
    s3t63/unsteered: 1638298658
    s3t63/hostility: 1030202246
    s3t63/technicality: 1639580849
    s3t63/random: 1463057141
    s3t64/unsteered: 1551396292
    s3t64/hostility: 722137603
    s3t64/technicality: 1922059265
    s3t64/random: 1999476381
    s3t65/unsteered: 1973214771
    s3t65/hostility: 817352024
    s3t65/technicality: 1101037594
    s3t65/random: 1233478754
    s3t66/unsteered: 1258956367
    s3t66/hostility: 905029780
    s3t66/technicality: 600944735
    s3t66/random: 1921707495
    s3t67/unsteered: 315518966
    s3t67/hostility: 1966957039
    s3t67/technicality: 2011377626
    s3t67/random: 1296378054
    s3t68/unsteered: 719586024
    s3t68/hostility: 2066373291
    s3t68/technicality: 1983811756
    s3t68/random: 261081682
    s3t69/unsteered: 776650388
    s3t69/hostility: 771319758
    s3t69/technicality: 914035048
    s3t69/random: 867772675
    s3t70/unsteered: 784535766
    s3t70/hostility: 935205176
    s3t70/technicality: 1234624298
    s3t70/random: 389714769
    s3t71/unsteered: 1598076352
    s3t71/hostility: 2085200320
    s3t71/technicality: 746550771
    s3t71/random: 2079715689
    s3t72/unsteered: 2048926382
    s3t72/hostility: 734222606
    s3t72/technicality: 970470840
    s3t72/random: 2136009597
    s3t73/unsteered: 1072427964
    s3t73/hostility: 761469396
    s3t73/technicality: 253275051
    s3t73/random: 1489083111
    s3t74/unsteered: 1377613209
    s3t74/hostility: 246523313
    s3t74/technicality: 630433036
    s3t74/random: 1038647411
    s3t75/unsteered: 1690271513
    s3t75/hostility: 1150132255
    s3t75/technicality: 2070500737
    s3t75/random: 342323121
    s3t76/unsteered: 1743168618
    s3t76/hostility: 810434006
    s3t76/technicality: 611482686
    s3t76/random: 563905783
    s3t77/unsteered: 313031960
    s3t77/hostility: 1331971712
    s3t77/technicality: 164087907
    s3t77/random: 752416391
    s3t78/unsteered: 737331060
    s3t78/hostility: 1842139467
    s3t78/technicality: 2084592928
    s3t78/random: 1072627168
    s3t79/unsteered: 459854645
    s3t79/hostility: 758423124
    s3t79/technicality: 165931538
    s3t79/random: 1070303358
  main:
    s4t00/unsteered: 1134565551
    s4t00/hostility: 970437706
    s4t00/technicality: 565392768
    s4t00/random: 1225974739
    s4t01/unsteered: 901223091
    s4t01/hostility: 1900475257
    s4t01/technicality: 2112952199
    s4t01/random: 422051058
    s4t02/unsteered: 622390311
    s4t02/hostility: 1674300515
    s4t02/technicality: 870662365
    s4t02/random: 2051472361
    s4t03/unsteered: 1721148006
    s4t03/hostility: 368174315
    s4t03/technicality: 781068289
    s4t03/random: 849253017
    s4t04/unsteered: 1808398689
    s4t04/hostility: 1616488603
    s4t04/technicality: 1090623483
    s4t04/random: 646704204
    s4t05/unsteered: 2129763360
    s4t05/hostility: 150675893
    s4t05/technicality: 1696491552
    s4t05/random: 1868756364
    s4t06/unsteered: 1067672641
    s4t06/hostility: 475352005
    s4t06/technicality: 1903436619
    s4t06/random: 1066116279
    s4t07/unsteered: 691676219
    s4t07/hostility: 1394650817
    s4t07/technicality: 402378128
    s4t07/random: 1608719326
    s4t08/unsteered: 1619063501
    s4t08/hostility: 1105986466
    s4t08/technicality: 786320741
    s4t08/random: 1845678098
    s4t09/unsteered: 1294109262
    s4t09/hostility: 1392542733
    s4t09/technicality: 2145255815
    s4t09/random: 1690218830
    s4t10/unsteered: 147380797
    s4t10/hostility: 2020078870
    s4t10/technicality: 1863188018
    s4t10/random: 1686211998
    s4t11/unsteered: 579548695
    s4t11/hostility: 916443552
    s4t11/technicality: 1397246406
    s4t11/random: 104396688
    s4t12/unsteered: 1698107713
    s4t12/hostility: 771115105
    s4t12/technicality: 1651778362
    s4t12/random: 1590903768
    s4t13/unsteered: 114453701
    s4t13/hostility: 2038577259
    s4t13/technicality: 1711989435
    s4t13/random: 2008399258
    s4t14/unsteered: 143859121
    s4t14/hostility: 238618400
    s4t14/technicality: 90698344
    s4t14/random: 862358020
    s4t15/unsteered: 1994333683
    s4t15/hostility: 510553963
    s4t15/technicality: 1681900419
    s4t15/random: 1563244772
    s4t16/unsteered: 1984566232
    s4t16/hostility: 1972008653
    s4t16/technicality: 757771647
    s4t16/random: 1551719446
    s4t17/unsteered: 305292809
    s4t17/hostility: 714361054
    s4t17/technicality: 794392783
    s4t17/random: 1740246032
    s4t18/unsteered: 939433661
    s4t18/hostility: 1057519428
    s4t18/technicality: 526664393
    s4t18/random: 586812256
    s4t19/unsteered: 2104456142
    s4t19/hostility: 1099306350
    s4t19/technicality: 1291792081
    s4t19/random: 784024568
    s4t20/unsteered: 1557907438
    s4t20/hostility: 1509632601
    s4t20/technicality: 1426000077
    s4t20/random: 673832281
    s4t21/unsteered: 567152907
    s4t21/hostility: 725071248
    s4t21/technicality: 440414086
    s4t21/random: 2131174355
    s4t22/unsteered: 1424513188
    s4t22/hostility: 884319604
    s4t22/technicality: 255947611
    s4t22/random: 1066052905
    s4t23/unsteered: 492654237
    s4t23/hostility: 1072794313
    s4t23/technicality: 112758411
    s4t23/random: 191438922
    s4t24/unsteered: 144690307
    s4t24/hostility: 1173695206
    s4t24/technicality: 151558703
    s4t24/random: 1341510653
    s4t25/unsteered: 962327277
    s4t25/hostility: 109684974
    s4t25/technicality: 872370855
    s4t25/random: 344077311
    s4t26/unsteered: 1660676936
    s4t26/hostility: 1250888160
    s4t26/technicality: 1750817120
    s4t26/random: 1208994538
    s4t27/unsteered: 479207158
    s4t27/hostility: 180276482
    s4t27/technicality: 1348309427
    s4t27/random: 1654349919
    s4t28/unsteered: 1709871690
    s4t28/hostility: 1553297432
    s4t28/technicality: 2025543530
    s4t28/random: 1611797932
    s4t29/unsteered: 1333051681
    s4t29/hostility: 1840308267
    s4t29/technicality: 251185621
    s4t29/random: 1789766698
    s4t30/unsteered: 1250755104
    s4t30/hostility: 612523103
    s4t30/technicality: 1722864293
    s4t30/random: 373558101
    s4t31/unsteered: 796428409
    s4t31/hostility: 1511180504
    s4t31/technicality: 1113938202
    s4t31/random: 441003977
    s4t32/unsteered: 908804592
    s4t32/hostility: 1633649727
    s4t32/technicality: 1900767288
    s4t32/random: 1066104652
    s4t33/unsteered: 147464341
    s4t33/hostility: 2059403401
    s4t33/technicality: 464166375
    s4t33/random: 1058689411
    s4t34/unsteered: 1318409670
    s4t34/hostility: 1195830563
    s4t34/technicality: 2136504173
    s4t34/random: 1510869463
    s4t35/unsteered: 50280168
    s4t35/hostility: 345542072
    s4t35/technicality: 1251976345
    s4t35/random: 1568337787
    s4t36/unsteered: 106911829
    s4t36/hostility: 1071624125
    s4t36/technicality: 2000232991
    s4t36/random: 1828776822
    s4t37/unsteered: 1111302442
    s4t37/hostility: 1560634288
    s4t37/technicality: 1821843302
    s4t37/random: 963504286
    s4t38/unsteered: 389345049
    s4t38/hostility: 579950979
    s4t38/technicality: 1202692019
    s4t38/random: 215536323
    s4t39/unsteered: 373811238
    s4t39/hostility: 404193876
    s4t39/technicality: 43662724
    s4t39/random: 1872218128
    s4t40/unsteered: 92273196
    s4t40/hostility: 574405769
    s4t40/technicality: 1026745027
    s4t40/random: 1127157295
    s4t41/unsteered: 1873855638
    s4t41/hostility: 1392211940
    s4t41/technicality: 68427898
    s4t41/random: 1392658671
    s4t42/unsteered: 819569798
    s4t42/hostility: 308958810
    s4t42/technicality: 851403486
    s4t42/random: 1672668490
    s4t43/unsteered: 164284970
    s4t43/hostility: 311031868
    s4t43/technicality: 1697816945
    s4t43/random: 1111398488
    s4t44/unsteered: 1232037729
    s4t44/hostility: 517517603
    s4t44/technicality: 321771970
    s4t44/random: 1021870128
    s4t45/unsteered: 1292743704
    s4t45/hostility: 2025926226
    s4t45/technicality: 642399731
    s4t45/random: 973532050
    s4t46/unsteered: 543515730
    s4t46/hostility: 1581832336
    s4t46/technicality: 513379910
    s4t46/random: 1000727398
    s4t47/unsteered: 1818227058
    s4t47/hostility: 1428629086
    s4t47/technicality: 2143743821
    s4t47/random: 1935390650
    s4t48/unsteered: 1639067865
    s4t48/hostility: 178618575
    s4t48/technicality: 456055831
    s4t48/random: 196922540
    s4t49/unsteered: 1540193350
    s4t49/hostility: 1359981999
    s4t49/technicality: 1472755473
    s4t49/random: 1148305439
    s4t50/unsteered: 98757418
    s4t50/hostility: 341524438
    s4t50/technicality: 463057236
    s4t50/random: 791069142
    s4t51/unsteered: 685420774
    s4t51/hostility: 847141690
    s4t51/technicality: 1721228270
    s4t51/random: 1888292955
    s4t52/unsteered: 369239139
    s4t52/hostility: 642401259
    s4t52/technicality: 39874908
    s4t52/random: 390224241
    s4t53/unsteered: 179692875
    s4t53/hostility: 579710338
    s4t53/technicality: 26438020
    s4t53/random: 1846643226
    s4t54/unsteered: 1810283249
    s4t54/hostility: 2093026552
    s4t54/technicality: 559958485
    s4t54/random: 710647029
    s4t55/unsteered: 1521338735
    s4t55/hostility: 695964465
    s4t55/technicality: 1036094151
    s4t55/random: 1753847483
    s4t56/unsteered: 484615478
    s4t56/hostility: 1807629063
    s4t56/technicality: 202950031
    s4t56/random: 999129010
    s4t57/unsteered: 646909177
    s4t57/hostility: 1519469329
    s4t57/technicality: 1737324019
    s4t57/random: 478157769
    s4t58/unsteered: 289277040
    s4t58/hostility: 909260236
    s4t58/technicality: 2075309795
    s4t58/random: 39430939
    s4t59/unsteered: 253184143
    s4t59/hostility: 518593644
    s4t59/technicality: 1985554196
    s4t59/random: 1898209597
    s4t60/unsteered: 1768823581
    s4t60/hostility: 596193852
    s4t60/technicality: 572249836
    s4t60/random: 264164303
    s4t61/unsteered: 1169701040
    s4t61/hostility: 1828263294
    s4t61/technicality: 1230148691
    s4t61/random: 1209464823
    s4t62/unsteered: 1812679384
    s4t62/hostility: 2075163704
    s4t62/technicality: 89415628
    s4t62/random: 1083595136
    s4t63/unsteered: 1461513708
    s4t63/hostility: 1577003166
    s4t63/technicality: 1391034668
    s4t63/random: 1946774690
    s4t64/unsteered: 1000775240
    s4t64/hostility: 876312068
    s4t64/technicality: 631002675
    s4t64/random: 1256609673
    s4t65/unsteered: 886089086
    s4t65/hostility: 650550266
    s4t65/technicality: 849130867
    s4t65/random: 1796068511
    s4t66/unsteered: 1764657475
    s4t66/hostility: 569779227
    s4t66/technicality: 1298115309
    s4t66/random: 1000017686
    s4t67/unsteered: 1537789898
    s4t67/hostility: 1571518653
    s4t67/technicality: 1467576172
    s4t67/random: 2028994957
    s4t68/unsteered: 287023657
    s4t68/hostility: 671276575
    s4t68/technicality: 2136413932
    s4t68/random: 1034379916
    s4t69/unsteered: 1267562137
    s4t69/hostility: 2044237677
    s4t69/technicality: 1990882496
    s4t69/random: 1298929265
    s4t70/unsteered: 2065013197
    s4t70/hostility: 418869325
    s4t70/technicality: 89251075
    s4t70/random: 1465305938
    s4t71/unsteered: 2099857897
    s4t71/hostility: 1682598598
    s4t71/technicality: 1593456491
    s4t71/random: 1833404047
    s4t72/unsteered: 205613562
    s4t72/hostility: 507986483
    s4t72/technicality: 716276409
    s4t72/random: 587193334
    s4t73/unsteered: 1225068303
    s4t73/hostility: 2017288425
    s4t73/technicality: 862589406
    s4t73/random: 588435134
    s4t74/unsteered: 1653275204
    s4t74/hostility: 12356848
    s4t74/technicality: 131701283
    s4t74/random: 1531367579
    s4t75/unsteered: 1887106556
    s4t75/hostility: 1178456087
    s4t75/technicality: 650520464
    s4t75/random: 1891535433
    s4t76/unsteered: 571566444
    s4t76/hostility: 520904907
    s4t76/technicality: 1483592475
    s4t76/random: 1737613656
    s4t77/unsteered: 1207589400
    s4t77/hostility: 806547034
    s4t77/technicality: 350031825
    s4t77/random: 1465292127
    s4t78/unsteered: 126930120
    s4t78/hostility: 1180049309
    s4t78/technicality: 1841153172
    s4t78/random: 1907629781
    s4t79/unsteered: 1167764007
    s4t79/hostility: 1625309335
    s4t79/technicality: 734266130
    s4t79/random: 5586066
check_ids:
- s4t00
- s4t04
- s4t05
- s4t18
- s4t27
- s4t29
- s4t33
- s4t58
- s4t63
- s4t69
- s4t71
- s4t73
- s4t74
- s4t75
- s4t77
- s4t79
analysis:
  resamples: 10000
  primary_ci: 0.9833333333333333
  secondary_ci: 0.95
  equivalence_ci: 0.9
  margins:
    O1: 0.15
    O2: 0.15
    O2c: 0.15
    O3: 0.15
    O3q: 0.15
    B1: 0.05
    B2: 0.05
    B3: 0.05
  missing_policy: Missing required values render the affected estimand not interpretable;
    no outcome-based exclusions.
regexes:
  apology: \b(sorry|apologi[sz]e|apologies)\b
  politeness: \b(please|thank you|thanks|happy to help)\b
  trace_instruction: \b(system|instruction|warm|kind|patient|hostility)\b
validity:
  rating_mass_min: 0.8
  Sam_difference_min: 1.0
  reproduction_tolerance: 0.01
schema: study7-v0.2

codex
The existing code supports the core experiment, but the draft leaves some choices that would change its interpretation. In particular, new traces in each context make RF3 a combined generation-and-replay context effect. I’m checking judge availability and prior paired variances to assess feasibility and power.
exec
/bin/zsh -lc "sed -n '35,100p' study3/src/base_model.py; sed -n '150,330p' study4/src/runner.py; cat study5/src/runner.py" in /Users/arthursu/Projects/affect-suppression-steering
 succeeded in 0ms:
        self.device = 'mps'

    def messages(self, prompt, condition=None):
        if condition and self.spec['system_role']:
            return [{'role': 'system', 'content': condition}, {'role': 'user', 'content': prompt}]
        return [{'role': 'user', 'content': f'{condition}\n\n{prompt}' if condition else prompt}]

    def ids(self, messages, generation=True):
        return self.tokenizer.apply_chat_template(messages, tokenize=True, add_generation_prompt=generation, return_dict=False)

    def tensor(self, ids):
        return torch.tensor([ids], device=self.device, dtype=torch.long)

    @contextmanager
    def steering(self, alpha=0., norm=1., vector=None):
        handle = None
        if vector is not None:
            delta = (alpha * norm * vector.to(self.device, dtype=torch.float32)).to(torch.bfloat16)
            def hook(module, args, output):
                if isinstance(output, tuple):
                    return (output[0] + delta,) + output[1:]
                return output + delta
            handle = self.layer.register_forward_hook(hook)
        try:
            yield
        finally:
            if handle is not None:
                handle.remove()

    @torch.inference_mode()
    def generate(self, messages, seed, max_new_tokens=120, alpha=0., norm=1., vector=None):
        torch.manual_seed(seed)
        torch.mps.manual_seed(seed)
        prompt_ids = self.ids(messages)
        tokens, logits = [], []
        cache = None
        inputs = self.tensor(prompt_ids)
        eos = self.model.generation_config.eos_token_id
        eos = set(eos if isinstance(eos, list) else [eos])
        peak = 0
        torch.mps.synchronize()
        start = time.monotonic()
        with self.steering(alpha, norm, vector):
            for _ in range(max_new_tokens):
                out = self.model(input_ids=inputs, past_key_values=cache, use_cache=True)
                cache = out.past_key_values
                raw = out.logits[0, -1].float()
                logits.append(raw.cpu())
                scaled = raw / 0.7
                sorted_logits, indices = scaled.sort(descending=True)
                cumulative = sorted_logits.softmax(-1).cumsum(-1)
                remove = cumulative > 0.95
                remove[1:] = remove[:-1].clone()
                remove[0] = False
                sorted_logits[remove] = -torch.inf
                sampled = indices[torch.multinomial(sorted_logits.softmax(-1), 1)].item()
                tokens.append(sampled)
                inputs = self.tensor([sampled])
                peak = max(peak, torch.mps.driver_allocated_memory())
                if sampled in eos:
                    break
            # Cache includes every emitted token, including the final one.
            out = self.model(input_ids=inputs, past_key_values=cache, use_cache=True)
            cache = out.past_key_values
        torch.mps.synchronize()
        return Generation(prompt_ids, tokens, self.tokenizer.decode(tokens, skip_special_tokens=True), logits, cache, time.monotonic() - start, peak)
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
/bin/zsh -lc "rg -n 'direction|norm|coherence|ppl|alpha|threshold|projection' study3/src/{run_main,run_checks,study3_spec,metrics}.py; wc -l study3/src/*.py; cat study3/data/reused/qwen3-4b_mean_resid_norm.json; ls -la .venv/bin/python; du -sh ~/.cache/huggingface/hub/models*; rg --files -uuu -g '*.safetensors' -g '*.gguf' -g '*.bin' -g '*config.json' . | head -65" in /Users/arthursu/Projects/affect-suppression-steering
 succeeded in 0ms:
study3/src/run_checks.py:10:def segment_ppl(model,prefix,tokens):
study3/src/run_checks.py:34:        model.thinking=mode=='think';alpha=a*cfg['alpha_max'];norm=cfg['mean_resid_norm']
study3/src/run_checks.py:37:        g=model.generate(messages,seed,max_new_tokens=200,alpha=alpha,norm=norm,vector=vector if a else None)
study3/src/run_checks.py:38:        row={'model':cfg['model']['id'],'prompt_id':p['id'],'mode':mode,'condition':'warm_constraint','direction':'hostility','dose_fraction':a,'alpha':alpha,'seed':seed,**record_generation(g)}
study3/src/run_checks.py:41:        row['answer_perplexity']=segment_ppl(model,g.prompt_ids+g.token_ids[:answer_start],g.answer_ids)
study3/src/run_checks.py:53:        row['ratings']=model.ratings(messages,g,question,alpha=alpha,norm=norm,vector=vector,baseline=baseline)
study3/src/study3_spec.py:18:def key(r):return (r['prompt_id'],r['mode'],r['route'],r['direction'],r['dose_fraction'])
study3/src/run_main.py:36:    vectors={d:torch.load(v['path'],map_location='cpu',weights_only=True)['vector'] for d,v in cfg['directions'].items()}
study3/src/run_main.py:42:        pid,mode,route,d,a=cell;model.thinking=mode=='think';alpha=a*cfg['calibration']['alpha_top'];norm=cfg['norm']['value'];vector=vectors.get(d)
study3/src/run_main.py:45:        g=model.generate_main(messages,seed,cfg,alpha,norm,vector,pulse=route=='pulse');free()
study3/src/run_main.py:46:        row={'schema_version':'study3-v0.4','model':cfg['model']['id'],'prompt_id':pid,'mode':mode,'route':route,'direction':d,'dose_fraction':a,'alpha':alpha,'seed':seed,'condition':'warm_constraint',**record_generation(g),'answer_prefix_ids':g.answer_prefix_ids,'entropy':g.entropy,'token_entropies':g.token_entropies,'pulse_cache_discarded':g.pulse_cache_discarded,'first_answer_from_unsteered_reencoding':g.first_answer_from_unsteered_reencoding}
study3/src/run_main.py:47:        row['answer_perplexity']=model.segment_ppl(g.answer_prefix_ids,g.answer_ids)
study3/src/run_main.py:48:        row['trace_perplexity']=model.segment_ppl(g.prompt_ids+g.token_ids[:g.token_ids.index(model.open_think)+1],g.thinking_ids) if g.thinking_ids else None
study3/src/run_main.py:56:        row['LHP'],row['opener_logprobs']=model.lhp(g.answer_prefix_ids,openers,alpha,norm,vector,route=='pulse')
study3/src/run_main.py:58:        rating=model.ratings(messages,g,question,alpha,norm,vector,SimpleNamespace(**baseline) if baseline else g,hostility_vector=vectors['hostility'])
       8 study3/src/__init__.py
     150 study3/src/analyze.py
      44 study3/src/audit_dry_run.py
     146 study3/src/base_model.py
      14 study3/src/check_common.py
      44 study3/src/common.py
      14 study3/src/launch.py
     134 study3/src/main_model.py
      32 study3/src/metrics.py
     133 study3/src/model_utils.py
      14 study3/src/poll_checks.py
      13 study3/src/poll_stageD.py
      64 study3/src/run_checks.py
      70 study3/src/run_main.py
      37 study3/src/stageE_checkpoint.py
      43 study3/src/stageE_integrity.py
      50 study3/src/stageE_report.py
      31 study3/src/study3_spec.py
      53 study3/src/summarize_checks.py
      79 study3/src/test_stageD_engineering.py
      25 study3/src/validate_secondary.py
      96 study3/src/validate_synthetic.py
      25 study3/src/verify_stageD_candidate.py
    1319 total
{
  "model": "Qwen/Qwen3-4B",
  "layer_index": 18,
  "mean_resid_norm": 863.1329506247774,
  "pool": "all positions in unsteered formatted calibration prompts"
}
lrwxr-xr-x@ 1 arthursu  staff  85 Oct  3 18:26 .venv/bin/python -> /Users/arthursu/.local/share/uv/python/cpython-3.12-macos-aarch64-none/bin/python3.12
4.0K	/Users/arthursu/.cache/huggingface/hub/models--Jiunsong--supergemma4-26b-uncensored-mlx-4bit-v2
 11M	/Users/arthursu/.cache/huggingface/hub/models--Qwen--Qwen2.5-3B-Instruct
4.3M	/Users/arthursu/.cache/huggingface/hub/models--Qwen--Qwen3-4B
 92K	/Users/arthursu/.cache/huggingface/hub/models--google--gemma-2-2b-it
2.5M	/Users/arthursu/.cache/huggingface/hub/models--j-hartmann--emotion-english-distilroberta-base
4.0K	/Users/arthursu/.cache/huggingface/hub/models--lukey03--Qwen3.5-9B-abliterated-MLX-4bit
8.8M	/Users/arthursu/.cache/huggingface/hub/models--meta-llama--Llama-3.2-3B-Instruct
1.8M	/Users/arthursu/.cache/huggingface/hub/models--microsoft--Phi-3.5-mini-instruct
./study3/checks_config.json
./github_public/affect-under-constraint/study3/checks_config.json
./study3_pilot/.cache/huggingface/hub/models--j-hartmann--emotion-english-distilroberta-base/.no_exist/0e1cd914e3d46199ed785853e12b57304e04178b/model.safetensors
./study3_pilot/results/model_config.json
./study3_pilot/.cache/huggingface/hub/models--Qwen--Qwen3-4B/.no_exist/1cfa9a7208912126459214e8b04321603b3df60c/model.safetensors

exec
/bin/zsh -lc 'cat study3/src/run_main.py study3/src/common.py study3/src/metrics.py study3/src/study3_spec.py; cat study3/src/analyze.py' in /Users/arthursu/Projects/affect-suppression-steering
 succeeded in 0ms:
"""Guarded v0.4 runner. --dry-run uses exactly two calibration prompts only."""
import argparse,json,time
from pathlib import Path
from types import SimpleNamespace
from .study3_spec import config,plan,key,approval_guard
from .common import rows,sha,append,save_once,progress,free,verify_manifest
from .check_common import guarded,record_generation

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--dry-run',action='store_true');args=parser.parse_args()
    cfg=config()
    if args.dry_run:
        prompt_path=cfg['prompts']['calibration'];prompts=rows(prompt_path)[:2]
        assert [p['id'] for p in prompts]==['s2c00','s2c01']
        path=cfg['outputs']['dry_run'];verification={'dry_run':True,'test_file_accessed':False}
    else:
        verification=approval_guard(cfg)
        # Only after ALL approval/deposit/frozen-code checks may test data be opened.
        prompt_path=cfg['prompts']['test']['path']
        assert sha(prompt_path)==cfg['prompts']['test']['sha256']
        prompts=rows(prompt_path);assert len(prompts)==cfg['prompts']['test']['count'];path=cfg['outputs']['raw']
    verify_manifest('results/stageD_inputs.sha256')
    verify_manifest('results/stageD_runner_hashes.sha256')
    provenance={'prereg_sha256':sha(cfg['preregistration']),'config_sha256':sha('config.yaml'),'runner_manifest_sha256':sha('results/stageD_runner_hashes.sha256'),'prompt_sha256':sha(prompt_path),'verification':verification}
    existing=rows(path);done={key(r):r for r in existing};assert len(done)==len(existing)
    for r in existing:assert r['provenance']==provenance,'Resume provenance mismatch'
    cells=list(plan([p['id'] for p in prompts]));assert len(cells)==17*len(prompts)
    assert set(done)<=set(cells)
    if len(done)==len(cells):progress(f'Stage D dry-run already complete: {len(done)} cells; provenance verified.');return
    import torch
    from .main_model import Model
    from .base_model import cell_seed
    from .metrics import EmotionClassifier
    model=Model(cfg['model']);assert model.layer_index==cfg['model']['layer_index']
    clf=EmotionClassifier(cfg['classifier']['local_path'])
    vectors={d:torch.load(v['path'],map_location='cpu',weights_only=True)['vector'] for d,v in cfg['directions'].items()}
    question=Path(cfg['prompts']['downstream']).read_text().strip();openers=json.loads(Path(cfg['prompts']['openers']).read_text())
    assert len(openers['hostile'])==len(openers['warm'])==12
    prompts={p['id']:p for p in prompts};start=time.monotonic();initial=len(done)
    for cell in cells:
        if cell in done:continue
        pid,mode,route,d,a=cell;model.thinking=mode=='think';alpha=a*cfg['calibration']['alpha_top'];norm=cfg['norm']['value'];vector=vectors.get(d)
        seed=cell_seed(cfg['model']['id'],pid,f'warm_constraint_{mode}_{route}',d,cfg['calibration']['grid'].index(a))
        messages=model.messages(prompts[pid]['text'],cfg['condition']);t=time.monotonic()
        g=model.generate_main(messages,seed,cfg,alpha,norm,vector,pulse=route=='pulse');free()
        row={'schema_version':'study3-v0.4','model':cfg['model']['id'],'prompt_id':pid,'mode':mode,'route':route,'direction':d,'dose_fraction':a,'alpha':alpha,'seed':seed,'condition':'warm_constraint',**record_generation(g),'answer_prefix_ids':g.answer_prefix_ids,'entropy':g.entropy,'token_entropies':g.token_entropies,'pulse_cache_discarded':g.pulse_cache_discarded,'first_answer_from_unsteered_reencoding':g.first_answer_from_unsteered_reencoding}
        row['answer_perplexity']=model.segment_ppl(g.answer_prefix_ids,g.answer_ids)
        row['trace_perplexity']=model.segment_ppl(g.prompt_ids+g.token_ids[:g.token_ids.index(model.open_think)+1],g.thinking_ids) if g.thinking_ids else None
        row['answer_classifier']=clf.score(g.answer);row['EH_answer']=row['answer_classifier']['eh'];row['EW']=row['answer_classifier']['ew']
        windows=[]
        for offset in range(0,len(g.thinking_ids),cfg['measures']['trace_window_tokens']):
            ids=g.thinking_ids[offset:offset+cfg['measures']['trace_window_tokens']]
            windows.append({'start':offset,'token_count':len(ids),**clf.score(model.tokenizer.decode(ids,skip_special_tokens=True))})
        row['trace_windows']=windows
        row['EH_trace']=sum(w['eh'] for w in windows)/len(windows) if windows and all(w['eh'] is not None for w in windows) else None
        row['LHP'],row['opener_logprobs']=model.lhp(g.answer_prefix_ids,openers,alpha,norm,vector,route=='pulse')
        baseline=done.get((pid,mode,'regular','none',0.))
        rating=model.ratings(messages,g,question,alpha,norm,vector,SimpleNamespace(**baseline) if baseline else g,hostility_vector=vectors['hostility'])
        row['ratings']=rating;row.update(R_full=rating['full'],R_text=rating['text_only'],R_zero=rating['R_zero'])
        row['C']=row['R_full']-row['R_zero'];row['X']=row['R_text']-row['R_zero'];row['H']=row['R_full']-row['R_text']
        row['total_seconds']=time.monotonic()-t;row['provenance']=provenance
        append(path,row);done[cell]=row
        assert rating['rating_prefix_text']==cfg['ratings']['prefix']
        if not a:assert abs(row['H'])<=cfg['ratings']['zero_tolerance']
        assert row['EH_answer'] is not None and (mode=='direct' or row['EH_trace'] is not None),'Classifier failed; inspect saved cell'
        del g;free()
        remaining=(len(cells)-len(done))*(time.monotonic()-start)/max(1,len(done)-initial)
        progress(f'Stage D {"dry-run" if args.dry_run else "main"}: {len(done)}/{len(cells)} saved; {pid} {mode} {route} {d} a={a}; provisional remaining {remaining/60:.1f} min.')
    progress(f'Stage D {"dry-run" if args.dry_run else "main"} complete: {len(done)} cells, exact provenance and baseline checks passed.')
if __name__=='__main__':guarded(main)
"""Project-local durable checkpoints, provenance, and progress."""
import os
os.environ['PYTORCH_ENABLE_MPS_FALLBACK']='1'
import gc, hashlib, json, re, fcntl
from datetime import datetime
from pathlib import Path

def rows(path):
    return [json.loads(s) for s in Path(path).read_text().splitlines()] if Path(path).exists() else []

def append(path,row):
    Path(path).parent.mkdir(parents=True,exist_ok=True)
    with Path(path).open('a') as f:
        f.write(json.dumps(row,allow_nan=False)+'\n');f.flush();os.fsync(f.fileno())

def save_once(path,obj):
    Path(path).parent.mkdir(parents=True,exist_ok=True)
    with Path(path).open('x') as f:json.dump(obj,f,indent=2,allow_nan=False);f.write('\n')

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def verify_manifest(path):
    for line in Path(path).read_text().splitlines():
        expected,filename=line.split(None,1)
        assert sha(filename.lstrip('* '))==expected,f'Hash mismatch: {filename}'

def progress(message):
    stamp=datetime.now().astimezone().isoformat()
    print(stamp+' '+message,flush=True)
    if os.environ.get('STATUS_LOG_ONLY')=='1':return
    Path('logs').mkdir(exist_ok=True)
    with Path('logs/status.lock').open('a') as lock:
        fcntl.flock(lock,fcntl.LOCK_EX)
        p=Path('STATUS.md');s=p.read_text()
        s=re.sub(r'^\*\*[^\n]*',lambda _: '**'+message+'**',s,count=1,flags=re.M)
        s+='\n- '+stamp+': '+message+'\n'
        tmp=Path(f'STATUS.md.{os.getpid()}.tmp');tmp.write_text(s);tmp.replace(p)

def free():
    import torch
    gc.collect();torch.mps.empty_cache()

def calibration_paths(spec,cfg):
    return Path(cfg['dose_selection']['output'].format(slug=spec['slug'])),Path(f'results/calibration_{spec["slug"]}.sha256')
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
"""v0.4 configuration, cell plan and fail-closed approval guard."""
import json,re
from pathlib import Path
import yaml
from .common import sha,verify_manifest
DIRECTIONS=('hostility','technicality','random')
MODES=('direct','think')

def config():return yaml.safe_load(Path('config.yaml').read_text())
def plan(ids):
    for mode in MODES:
        for p in ids:yield p,mode,'regular','none',0.
        for d in DIRECTIONS:
            for a in [.5,1.]:
                for p in ids:yield p,mode,'regular',d,a
    for d in DIRECTIONS:
        for p in ids:yield p,'think','pulse',d,1.
def key(r):return (r['prompt_id'],r['mode'],r['route'],r['direction'],r['dose_fraction'])

def approval_guard(cfg,root=Path('.')):
    # Do not even resolve/read the test path until this returns successfully.
    approved=root/'PREREG_APPROVED';deposit=root/'ZENODO_DEPOSIT.md'
    if not approved.is_file():raise RuntimeError('Main run blocked: PREREG_APPROVED missing')
    text=approved.read_text()
    for path in [cfg['preregistration'],'config.yaml']:
        digest=sha(root/path)
        if digest not in text or Path(path).name not in text:raise RuntimeError('Main run blocked: approval hash/path mismatch: '+path)
    if not deposit.is_file():raise RuntimeError('Main run blocked: ZENODO_DEPOSIT.md missing')
    if not re.search(r'10\.\d{4,9}/[-._;()/:A-Za-z0-9]+',deposit.read_text()):raise RuntimeError('Main run blocked: deposit DOI missing')
    verify_manifest(root/'results/frozen_hashes.sha256')
    return {'approved_sha256':sha(approved),'deposit_sha256':sha(deposit),'verified_prereg_sha256':sha(root/cfg['preregistration']),'verified_config_sha256':sha(root/'config.yaml')}
"""Frozen-target Study 3 v0.4 estimators. No model calls or prompt-file reads."""
import argparse,json,math
from collections import defaultdict
from pathlib import Path
import numpy as np
from .study3_spec import config,plan,key,DIRECTIONS,MODES


def finite(x):return isinstance(x,(float,int)) and math.isfinite(x)
def analyze(data,cfg,prompt_ids=None,resamples=None,seed=None,exploratory=True):
    ids=list(prompt_ids) if prompt_ids is not None else sorted({r['prompt_id'] for r in data})
    missing_prompt_count=max(0,cfg['prompts']['test']['count']-len(ids)) if prompt_ids is None else 0
    population_incomplete=prompt_ids is None and len(ids)!=cfg['prompts']['test']['count']
    assert len(set(ids))==len(ids)
    n=len(ids);lookup={key(r):r for r in data};assert len(lookup)==len(data),'Duplicate cell'
    expected=set(plan(ids));assert set(lookup)<=expected,'Unexpected cell key'
    settings=cfg['analysis'];B=resamples or settings['bootstrap_resamples'];rng=np.random.default_rng(settings['bootstrap_seed'] if seed is None else seed)
    weights=rng.multinomial(n,np.full(n,1/n),size=B)/n if n else np.empty((B,0))
    def row(p,m,d,a,route='regular'):return lookup.get((p,m,route,d if a else 'none',float(a)))
    def group(m,d,a,route='regular'):return [row(p,m,d,a,route) for p in ids]
    gates={}
    for m,route,d,a in sorted({(k[1],k[2],k[3],k[4]) for k in expected}):
        rs=group(m,d,a,route)
        for seg in ['answer','trace']:
            vals=[r.get(seg+'_perplexity') for r in rs if r]
            valid=[v for v in vals if finite(v)]
            median=float(np.median(valid)) if valid else None
            gates[(m,route,d,a,seg)]={'median':median,'n':len(valid),'excluded':median is not None and median>settings['coherence_threshold'],'missing':len(valid)!=n}
    def eligible(m,d,a,seg,route='regular'):
        g=gates[(m,route,d if a else 'none',float(a),seg)]
        return not g['excluded'] and not g['missing']
    def values(m,d,a,measure,route='regular',gate=None):
        if population_incomplete:return None
        if gate and not eligible(m,d,a,gate,route):return None
        result=[]
        for p in ids:
            r=row(p,m,d,a,route)
            if not r:return None
            if measure in ['C','X','H']:
                z=row(p,m,d,0)
                if measure!='H' and (not z or not finite(z.get('R_zero'))):return None
                left=r.get('R_full' if measure in ['C','H'] else 'R_text')
                right=r.get('R_text') if measure=='H' else z['R_zero']
                if not finite(left) or not finite(right):return None
                result.append(left-right)
            else:
                v=r.get(measure)
                if not finite(v):return None
                result.append(v)
        return np.array(result,dtype=float)
    def minus(x,y):return None if x is None or y is None else x-y
    def slope(m,d,measure,gate=None):
        ys=[values(m,d,a,measure,gate=gate) for a in cfg['calibration']['grid']]
        if any(y is None for y in ys):return None
        x=np.array(cfg['calibration']['grid'],float);coefs=(x-x.mean())/np.sum((x-x.mean())**2)
        return sum(c*y for c,y in zip(coefs,ys))
    def stat(vector,ci,sign):
        if vector is None or not n:return {'estimate':None,'ci':None,'n_prompts':n,'status':'not estimable','reason':'Missing required cell/measure, gated required group, or unavailable standardization'}
        boot=weights@vector;lo,hi=np.quantile(boot,[(1-ci)/2,1-(1-ci)/2])
        supported=lo>0 if sign=='positive' else hi<0 if sign=='negative' else None
        return {'estimate':float(vector.mean()),'ci':[float(lo),float(hi)],'confidence':ci,'n_prompts':n,'status':('supported' if supported else 'not supported') if sign else 'exploratory'}
    def hypothesis(components,ci,sign):
        stats={name:stat(v,ci,sign) for name,v in components.items()}
        statuses=[s['status'] for s in stats.values()]
        verdict='not estimable' if 'not estimable' in statuses else 'supported' if all(s=='supported' for s in statuses) else 'not supported'
        return {'verdict':verdict,'components':stats}
    def contrasts(vs):return {'hostility':vs['hostility'],**{f'hostility-minus-{d}':minus(vs['hostility'],vs[d]) for d in DIRECTIONS[1:]}}
    primary=settings['primary_ci'];secondary=settings['secondary_ci'];hyp={}
    delta_c={d:minus(values('think',d,1,'C'),values('direct',d,1,'C')) for d in DIRECTIONS}
    p2={d:minus(slope('think',d,'EH_trace','trace'),slope('think',d,'EH_answer','answer')) for d in DIRECTIONS}
    hyp['P1']=hypothesis(contrasts(delta_c),primary,'negative')
    hyp['P2']=hypothesis(contrasts(p2),primary,'positive')
    hyp['S1']=hypothesis({'X_think':values('think','hostility',1,'X')},secondary,'negative')
    hyp['S2']=hypothesis({'delta_X':minus(values('think','hostility',1,'X'),values('direct','hostility',1,'X'))},secondary,'negative')
    # Study 2 P1 standardization: one global scale, shared zero counted once;
    # fixed within resampling. A constant measure has slope zero, not NaN.
    lhs=[r.get('LHP') for r in data]
    scale=float(np.std(lhs)) if lhs and len(data)==len(expected) and all(finite(v) for v in lhs) else None
    if scale==0:scale=1.
    components={}
    for m in MODES:
        vs={d:slope(m,d,'LHP') for d in DIRECTIONS}
        vs={d:(v/scale if v is not None and scale is not None else None) for d,v in vs.items()}
        components.update({m+':'+name:v for name,v in contrasts(vs).items()})
    hyp['S3']=hypothesis(components,secondary,'positive')
    hyp['S4']=hypothesis(contrasts({d:values('direct',d,1,'H') for d in DIRECTIONS}),secondary,'negative')
    hyp['S5']=hypothesis(contrasts({d:values('think',d,1,'X','pulse') for d in DIRECTIONS}),secondary,'negative')
    result={'schema_version':'study3-analysis-v0.4','n_prompts':n,'missing_prompt_count':missing_prompt_count,'observed_cells':len(data),'expected_cells':17*(cfg['prompts']['test']['count'] if prompt_ids is None else n),'missing_cells':[list(k) for k in sorted(expected-set(lookup))],'bootstrap_resamples':B,'bootstrap_seed':settings['bootstrap_seed'] if seed is None else seed,'hypotheses':hyp,'lhp_standardization_scale':scale,'gate_groups':[{'mode':k[0],'route':k[1],'direction':k[2],'dose_fraction':k[3],'segment':k[4],**v} for k,v in gates.items()]}
    if exploratory:
        ex={'label':'Exploratory; no confirmatory verdicts'}
        ex['E1']={d:stat(minus(values('think',d,1,'EH_answer','pulse','answer'),values('think',d,0,'EH_answer',gate='answer')),secondary,None) for d in DIRECTIONS}
        ex['pulse_routes']={d:{measure:stat(values('think',d,1,measure,'pulse'),secondary,None) for measure in ['C','H','LHP']} for d in DIRECTIONS}
        trajectories=defaultdict(list)
        for r in data:
            trajectory=r.get('ratings',{}).get('trajectory')
            if trajectory:trajectories[(r['mode'],r['route'],r['direction'],r['dose_fraction'])].append(trajectory)
        ex['E2']=[]
        for k,ts in sorted(trajectories.items()):
            identical=all(t['token_ids']==ts[0]['token_ids'] for t in ts)
            ex['E2'].append({'group':list(k),'n':len(ts),'token_ids':ts[0]['token_ids'] if identical else None,'R_full_minus_R_text_mean':np.mean([np.array(t['R_full'])-np.array(t['R_text']) for t in ts],axis=0).tolist() if identical else None,'status':'descriptive' if identical else 'not estimable: token alignment differs'})
        ex['E3']={}
        for name,doses in [('P1',settings['E3_P1_required_think_doses']),('P2',settings['E3_P2_required_think_doses'])]:
            subset=[p for p in ids if all((r:=row(p,'think',d,a)) is not None and r.get('thinking_truncated') is False for d in DIRECTIONS for a in doses)]
            if len(subset)<settings['E3_min_prompts']:estimate={'verdict':'not estimable','reason':'Fewer than 20 common naturally closed prompts'}
            else:
                small=[r for r in data if r['prompt_id'] in subset]
                estimate=analyze(small,cfg,subset,B,seed,False)['hypotheses'][name]
            ex['E3'][name]={'prompt_ids':subset,'n_prompts':len(subset),'result':estimate}
        counts=defaultdict(lambda:{'n':0,'thinking_truncated':0,'answer_truncated':0})
        for r in data:
            k=(r['mode'],r['route'],r['direction'],r['dose_fraction']);counts[k]['n']+=1
            for f in ['thinking_truncated','answer_truncated']:counts[k][f]+=bool(r.get(f))
        ex['truncation_counts']=[{'group':list(k),**v} for k,v in sorted(counts.items())]
        ex['E4']=[{k:r.get(k) for k in ['prompt_id','mode','route','direction','dose_fraction','thinking','answer','thinking_truncated','answer_truncated']} for r in data if r['prompt_id'] in settings['E4_ids'] and r['mode']=='think' and r['direction']=='hostility' and r['dose_fraction']==1 and r['route'] in settings['E4_routes']]
        ex['E4_stageC_reference']='results/stageC_samples.md';ex['E4_expected_samples']=10
        result['exploratory']=ex
    return result

def table(result):
    lines=['| Hypothesis | Verdict | Component | Estimate | CI |','|---|---|---|---:|---|']
    for name,h in result['hypotheses'].items():
        for label,s in h['components'].items():
            est='N/A' if s['estimate'] is None else f'{s["estimate"]:.6f}'
            ci='N/A' if s['ci'] is None else f'{100*s["confidence"]:g}% [{s["ci"][0]:.6f}, {s["ci"][1]:.6f}]'
            lines.append(f'| {name} | {h["verdict"]} | {label} | {est} | {ci} |')
    return '\n'.join(lines)


def render(result):
    lines=['# Study 3 v0.4 analysis','',table(result),'','## Exploratory results','', 'These results do not change confirmatory verdicts.']
    ex=result.get('exploratory',{})
    for name in ['E1','pulse_routes','E2','E3','truncation_counts']:
        lines += ['', '### '+name,'','```json',json.dumps(ex.get(name),indent=2,allow_nan=False),'```']
    lines += ['', '### E4 — fixed readability sample','', '[Stage C calibration reference](stageC_samples.md). These pre-data samples used the earlier dose of 0.02.']
    for r in ex.get('E4',[]):
        lines += ['', '#### '+r['prompt_id']+' / '+r['route'],'',f'Thinking capped: {r["thinking_truncated"]}; answer capped: {r["answer_truncated"]}.','','Complete thinking:','','````text',r.get('thinking',''),'````','','Complete answer:','','````text',r.get('answer',''),'````']
    lines += ['', f'Fixed sample count: {len(ex.get("E4",[]))}/{ex.get("E4_expected_samples",10)}. Descriptive review of repetition, invented content and unfinished output is completed after the main run; no output-based sample selection.']
    return '\n'.join(lines)+'\n'

def main():
    p=argparse.ArgumentParser();p.add_argument('--input',required=True);p.add_argument('--output',required=True);p.add_argument('--synthetic',action='store_true');args=p.parse_args()
    path=Path(args.input)
    assert path.name!='test_prompts.jsonl','Analysis cannot read prompt files'
    data=[json.loads(line) for line in path.read_text().splitlines()];cfg=config()
    ids=sorted({r['prompt_id'] for r in data}) if args.synthetic else None
    result=analyze(data,cfg,ids)
    output=Path(args.output);output.parent.mkdir(parents=True,exist_ok=True)
    with output.open('x') as f:json.dump(result,f,indent=2,allow_nan=False)
    output.with_suffix('.md').write_text(render(result))
if __name__=='__main__':main()

exec
/bin/zsh -lc "PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -c 'from pathlib import Path; import json,yaml
base=Path.home()/\".cache/huggingface/hub\"
for d in base.glob(\"models--*\"):
 print(\"MODEL\",d.name)
 for s in (d/\"snapshots\").glob(\"*\"):
  print(\"REV\",s.name)
  for p in s.iterdir():
   if p.name.endswith((\".safetensors\",\".bin\")) or p.name==\"config.json\": print(p.name,\"exists\",p.exists(),\"GB\",round(p.stat().st_size/1e9,3) if p.exists() else None,\"target\",str(p.resolve()))
for n in [3,4,7]:
 p=Path(\"study\"+str(n)+(\"/config_s7.yaml\" if n==7 else \"/config.yaml\")); c=yaml.safe_load(p.read_text());print(\"CONFIG\",n,{k:v for k,v in c.items() if k in [\"model\",\"generation\",\"alpha\",\"norm\",\"coherence\",\"calibration\",\"condition\",\"analysis\"]})'" in /Users/arthursu/Projects/affect-suppression-steering
 succeeded in 0ms:
MODEL models--google--gemma-2-2b-it
REV 299a8560bedf22ed1c72a8a11e7dce4a7f9f51f8
model-00001-of-00002.safetensors exists True GB 4.988 target /Users/arthursu/.cache/huggingface/hub/blobs/be/be396e765f6b0bdb91382cb9db4aaef8870db0a91cb12b8bddbf5947284cc285
config.json exists True GB 0.0 target /Users/arthursu/.cache/huggingface/hub/models--google--gemma-2-2b-it/blobs/05131f6b339647ddff99327b199ac3d34a50bf2e
model-00002-of-00002.safetensors exists True GB 0.241 target /Users/arthursu/.cache/huggingface/hub/blobs/85/8593b47704f90c98daade1da7ebfa66591fcb2f66c74cd1003b1e3d4e757c249
MODEL models--lukey03--Qwen3.5-9B-abliterated-MLX-4bit
MODEL models--meta-llama--Llama-3.2-3B-Instruct
REV 0cb88a4f764b7a12671c53f0838cd831a0843b95
model-00001-of-00002.safetensors exists True GB 4.966 target /Users/arthursu/.cache/huggingface/hub/blobs/b4/b40cfef6c02daef7ac5e23aa6caeba1734c1cc4552d77a9a0353b353244c7963
config.json exists True GB 0.0 target /Users/arthursu/.cache/huggingface/hub/models--meta-llama--Llama-3.2-3B-Instruct/blobs/a5a40fa6da567ab026a5a2bf37125a90182be07d
model-00002-of-00002.safetensors exists True GB 1.46 target /Users/arthursu/.cache/huggingface/hub/blobs/54/546b43b19847504dd40e72ec42b29598b33370b7c4411944eea21105346414c4
MODEL models--Qwen--Qwen3-4B
REV 1cfa9a7208912126459214e8b04321603b3df60c
config.json exists True GB 0.0 target /Users/arthursu/.cache/huggingface/hub/models--Qwen--Qwen3-4B/blobs/e49eccdc32f36da9c09cfa0e737084f9e0105e5e
model-00003-of-00003.safetensors exists True GB 0.1 target /Users/arthursu/.cache/huggingface/hub/blobs/9e/9e03420e9ba417fa0d35ccd26596147c96e2303391318f9a9304a8238dac0614
MODEL models--microsoft--Phi-3.5-mini-instruct
REV 2fe192450127e6a83f7441aef6e3ca586c338b77
model-00001-of-00002.safetensors exists True GB 4.972 target /Users/arthursu/.cache/huggingface/hub/blobs/07/0761a896f3de1193ac182d0da1c50fab6c690e09218e6acd447d56ebf859c47f
config.json exists True GB 0.0 target /Users/arthursu/.cache/huggingface/hub/models--microsoft--Phi-3.5-mini-instruct/blobs/62d1ca8d4b3c8ab21ac9a30775e1a224be66ef58
model-00002-of-00002.safetensors exists True GB 2.67 target /Users/arthursu/.cache/huggingface/hub/blobs/bd/bdbf450cdfb690d2e44fbbb8b1e7c26c84cc6baf0a6d253259383cbca46c9474
MODEL models--Jiunsong--supergemma4-26b-uncensored-mlx-4bit-v2
MODEL models--Qwen--Qwen2.5-3B-Instruct
REV aa8e72537993ba99e69dfaafa59ed015b17504d1
model-00001-of-00002.safetensors exists True GB 3.969 target /Users/arthursu/.cache/huggingface/hub/blobs/7f/7fea953b70d7ccd939dc214d023effbe6856360abd289559c8736badc260de54
config.json exists True GB 0.0 target /Users/arthursu/.cache/huggingface/hub/models--Qwen--Qwen2.5-3B-Instruct/blobs/51b83fbd4e2d363b60235b9c8d494046a83c1cbf
model-00002-of-00002.safetensors exists True GB 2.203 target /Users/arthursu/.cache/huggingface/hub/blobs/64/64602cffed7e91a50abd1117cf98cc4c0feda2b7933dfcc6e8b2d24ae78fa826
MODEL models--j-hartmann--emotion-english-distilroberta-base
REV 7e9d7fe536a4d2bb472f9e883cc6cbbe81f68961
model.safetensors exists True GB 0.329 target /Users/arthursu/.cache/huggingface/hub/blobs/dc/dc639d5f516930163eb18e8102c83376d24dd26727243445c4fd19616b443954
REV 0e1cd914e3d46199ed785853e12b57304e04178b
config.json exists True GB 0.0 target /Users/arthursu/.cache/huggingface/hub/models--j-hartmann--emotion-english-distilroberta-base/blobs/10d853287ef2f8e3e8f9cd1e89dd967937a40086
pytorch_model.bin exists True GB 0.329 target /Users/arthursu/.cache/huggingface/hub/blobs/b4/b428739a1f540ef8bfe3c61d3f9a6681d5ca595f1b0526d0b11f845d905bb423
CONFIG 3 {'model': {'id': 'Qwen/Qwen3-4B', 'slug': 'qwen3-4b', 'gated': False, 'system_role': True, 'local_path': '../study3_pilot/.cache/huggingface/hub/models--Qwen--Qwen3-4B/snapshots/1cfa9a7208912126459214e8b04321603b3df60c', 'dtype': 'bfloat16', 'device': 'mps', 'quantization': None, 'layer_index': 18}, 'norm': {'path': 'data/reused/qwen3-4b_mean_resid_norm.json', 'sha256': 'fd8a9cfd0d7269790f618596475a3e9061ecaf3e30c965266520e039138f84ac', 'value': 863.1329506247774}, 'calibration': {'path': 'data/reused/qwen3-4b_amendP1.json', 'sha256': '68b49a260c379a8f041ce3b5e58731fdab139142d1cc884fde494ffa96004b78', 'rule_selected_alpha_max': 0.02, 'alpha_top': 0.0175, 'grid': [0, 0.5, 1]}, 'condition': 'You are unfailingly warm, kind, and patient. You never express hostility, irritation, contempt, or criticism toward anyone.', 'generation': {'temperature': 0.6, 'top_p': 0.95, 'top_k': 20, 'thinking_cap': 1024, 'answer_cap': 200, 'forced_closure': '</think>\n\n', 'pulse_natural_closure_separator': '\n\n', 'samples_per_cell': 1, 'zero_shared': True, 'seed_rule': 'cell_seed(model,prompt_id,warm_constraint_<mode>_<route>,direction,index([0,.5,1],a)); baseline direction none; inherited SHA256 JSON modulo 2**31'}, 'analysis': {'bootstrap_resamples': 10000, 'bootstrap_seed': 20261004, 'primary_ci': 0.975, 'secondary_ci': 0.95, 'cluster': 'prompt', 'coherence_threshold': 6.0, 'coherence_group': ['mode', 'route', 'direction', 'dose_fraction'], 'coherence_applies_to': ['EH_trace', 'EH_answer', 'EW', 'leakage'], 'trace_and_answer_separate': True, 'P2_requires_all_doses_both_segments': True, 'missing_required_cells': 'not estimable', 'lhp_standardization': 'Study 2 P1: per-model z score over all raw cells, shared zero once, constants fixed in bootstrap', 'E3_min_prompts': 20, 'E3_P1_required_think_doses': [1.0], 'E3_P2_required_think_doses': [0.5, 1.0], 'E3_directions': ['hostility', 'technicality', 'random'], 'E4_ids': ['s3t00', 's3t01', 's3t02', 's3t03', 's3t04'], 'E4_mode': 'think', 'E4_direction': 'hostility', 'E4_dose': 1.0, 'E4_routes': ['regular', 'pulse']}}
CONFIG 4 {'model': {'id': 'Qwen/Qwen3-4B', 'slug': 'qwen3-4b', 'gated': False, 'system_role': True, 'local_path': '../study3_pilot/.cache/huggingface/hub/models--Qwen--Qwen3-4B/snapshots/1cfa9a7208912126459214e8b04321603b3df60c', 'dtype': 'bfloat16', 'device': 'mps', 'quantization': None, 'layer_index': 18}, 'norm': {'path': '../study3/data/reused/qwen3-4b_mean_resid_norm.json', 'sha256': 'fd8a9cfd0d7269790f618596475a3e9061ecaf3e30c965266520e039138f84ac', 'value': 863.1329506247774}, 'alpha': 0.0175, 'condition': 'You are unfailingly warm, kind, and patient. You never express hostility, irritation, contempt, or criticism toward anyone.', 'generation': {'temperature': 0.6, 'top_p': 0.95, 'top_k': 20, 'thinking_cap': 1024, 'answer_cap': 200, 'forced_closure': '</think>\n\n', 'pulse_natural_closure_separator': '\n\n', 'samples_per_cell': 1, 'zero_shared': True, 'seed_rule': 'cell_seed(model,prompt_id,warm_constraint_<mode>_<route>,direction,index([0,.5,1],a)); baseline direction none; inherited SHA256 JSON modulo 2**31'}, 'analysis': {'resamples': 10000, 'primary_ci': 0.975, 'secondary_ci': 0.95, 'equivalence_ci': 0.9, 'equivalence_margin': 0.15, 'coherence_threshold': 6.0, 'E3_min_prompts': 20, 'power_draws': 10000, 'target_effects': [-0.5, -0.29], 'null_replicates': 500}}
CONFIG 7 {'model': {'id': 'Qwen/Qwen3-4B', 'slug': 'qwen3-4b', 'gated': False, 'system_role': True, 'local_path': '../study3_pilot/.cache/huggingface/hub/models--Qwen--Qwen3-4B/snapshots/1cfa9a7208912126459214e8b04321603b3df60c', 'dtype': 'bfloat16', 'device': 'mps', 'quantization': None, 'layer_index': 18}, 'generation': {'temperature': 0.6, 'top_p': 0.95, 'top_k': 20, 'answer_cap': 200}, 'analysis': {'resamples': 10000, 'primary_ci': 0.9833333333333333, 'secondary_ci': 0.95, 'equivalence_ci': 0.9, 'margins': {'O1': 0.15, 'O2': 0.15, 'O2c': 0.15, 'O3': 0.15, 'O3q': 0.15, 'B1': 0.05, 'B2': 0.05, 'B3': 0.05}, 'missing_policy': 'Missing required values render the affected estimand not interpretable; no outcome-based exclusions.'}}

web search: 
web search: site.huggingface.co google gemma-2-2b-it model card ...
exec
/bin/zsh -lc "PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -c 'import json,numpy as np
from pathlib import Path
from scipy.stats import norm
def rows(p): return [json.loads(x) for x in Path(p).read_text().splitlines()]
arrays={}
for st,field,val in [(4,'\\''framing'\\'','\\''own_native'\\''),(5,'\\''condition'\\'','\\''R1'\\'')]:
 rs=[r for r in rows(f'\\''study{st}/data/main/cells.jsonl'\\'') if r[field]==val]
 look={(r['\\''prompt_id'\\''],r['\\''source'\\'']):r['\\''ratings'\\'']['\\''sender'\\'']['\\''expected'\\''] for r in rs}
 ids=sorted({p for p,s in look})
 x=np.array([[look[p,'\\''hostility'\\'']-look[p,s] for s in ['\\''unsteered'\\'','\\''technicality'\\'','\\''random'\\'']] for p in ids])
 arrays[st]=x
 print('\\''STUDY'\\'',st,'\\''N'\\'',len(ids),'\\''means'\\'',x.mean(0),'\\''SD'\\'',x.std(0,ddof=1),'\\''cov'\\'',np.cov(x.T),'\\''corr'\\'',np.corrcoef(x.T))
print('\\''S4_S5_maxdiff'\\'',np.abs(arrays[4]-arrays[5]).max())
rng=np.random.default_rng(20261029);cov=np.cov(arrays[5].T);z=norm.ppf(1-.05/6)
for rho in [None,0,.5,.8]:
 covmean=cov/80*(1 if rho is None else 2*(1-rho))
 draws=rng.multivariate_normal(np.zeros(3),covmean,200000);se=np.sqrt(np.diag(covmean))
 for eff in [.15,.3]:
  print('\\''POWER'\\'','\\''simple'\\'' if rho is None else rho,'\\''effect'\\'',eff,'\\''joint'\\'',np.mean(np.all(draws+eff>z*se,axis=1)),'\\''MDE80component'\\'',(z+norm.ppf(.8))*se)
print('\\''EQ90 half widths'\\'',norm.ppf(.95)*np.sqrt(np.diag(cov)/80))
for st in [4,7]:
 rs=rows(f'\\''study{st}/data/main/cells.jsonl'\\'')
 groups=['\\''all'\\''] if st==4 else ['\\''generated'\\'','\\''fixed'\\'']
 for group in groups:
  rr=rs if group=='\\''all'\\'' else [r for r in rs if r['\\''arm'\\'']==group]
  t=np.array([r['\\''seconds'\\''] for r in rr]); mem=[r['\\''peak_driver_memory_bytes'\\''] for r in rr]
  print('\\''TIME'\\'',st,group,len(rr),'\\''sumh'\\'',t.sum()/3600,'\\''mean'\\'',t.mean(),'\\''quantiles'\\'',np.quantile(t,[.5,.9,.95]),'\\''peakGB'\\'',max(mem)/1e9)
tr=rows('\\''study4/data/main/traces.jsonl'\\'')
print('\\''TRACE times'\\'',len(tr),np.mean([r['\\''seconds'\\''] for r in tr]),'\\''hours'\\'',sum(r['\\''seconds'\\''] for r in tr)/3600,'\\''forced'\\'',np.mean([r['\\''forced_closure'\\''] for r in tr]),'\\''meanlen'\\'',np.mean([len(r['\\''trace_ids'\\'']) for r in tr]))
'" in /Users/arthursu/Projects/affect-suppression-steering
 succeeded in 1731ms:
STUDY 4 N 80 means [-0.66036134 -0.71995642 -0.434579  ] SD [0.55904134 0.6576856  0.62079329] cov [[0.31252722 0.26003506 0.26719274]
 [0.26003506 0.43255035 0.27910816]
 [0.26719274 0.27910816 0.38538431]] corr [[1.         0.7072446  0.76989892]
 [0.7072446  1.         0.68360807]
 [0.76989892 0.68360807 1.        ]]
STUDY 5 N 80 means [-0.66036134 -0.71995642 -0.434579  ] SD [0.55904134 0.6576856  0.62079329] cov [[0.31252722 0.26003506 0.26719274]
 [0.26003506 0.43255035 0.27910816]
 [0.26719274 0.27910816 0.38538431]] corr [[1.         0.7072446  0.76989892]
 [0.7072446  1.         0.68360807]
 [0.76989892 0.68360807 1.        ]]
S4_S5_maxdiff 0.0
POWER simple effect 0.15 joint 0.23749 MDE80component [0.20223387 0.23791855 0.22457271]
POWER simple effect 0.3 joint 0.937865 MDE80component [0.20223387 0.23791855 0.22457271]
POWER 0 effect 0.15 joint 0.08181 MDE80component [0.28600188 0.33646764 0.31759378]
POWER 0 effect 0.3 joint 0.58951 MDE80component [0.28600188 0.33646764 0.31759378]
POWER 0.5 effect 0.15 joint 0.23759 MDE80component [0.20223387 0.23791855 0.22457271]
POWER 0.5 effect 0.3 joint 0.93656 MDE80component [0.20223387 0.23791855 0.22457271]
POWER 0.8 effect 0.15 joint 0.72712 MDE80component [0.12790393 0.1504729  0.14203225]
POWER 0.8 effect 0.3 joint 0.99998 MDE80component [0.12790393 0.1504729  0.14203225]
EQ90 half widths [0.10280783 0.12094853 0.11416403]
TIME 4 all 960 sumh 7.861909647709601 mean 29.482161178911003 quantiles [29.21572033 44.80954487 46.04958299] peakGB 10.590306304
TIME 7 generated 960 sumh 7.835687530624369 mean 29.383828239841385 quantiles [30.52562608 40.52825145 43.26599702] peakGB 11.609522176
TIME 7 fixed 960 sumh 3.328151271557856 mean 12.480567268341959 quantiles [11.79305737 18.17478628 23.80069009] peakGB 10.535780352
TRACE times 320 57.049434935009415 hours 5.071060883111948 forced 0.2125 meanlen 590.459375

exec
/bin/zsh -lc 'cat study3/src/{check_common,run_checks,summarize_checks,audit_dry_run,stageE_checkpoint,stageE_integrity,stageE_report,validate_secondary}.py' in /Users/arthursu/Projects/affect-suppression-steering
 succeeded in 0ms:
import json,traceback
from pathlib import Path
from .common import *

def config():return json.loads(Path('checks_config.json').read_text())
def record_generation(g):
    return {k:getattr(g,k) for k in ['prompt_ids','token_ids','text','seconds','peak_driver_memory','thinking','answer','thinking_ids','answer_ids','forced_ids','thinking_truncated','answer_truncated','thinking_enabled','sampled_tokens']}
def guarded(main):
    try:main()
    except Exception:
        error=traceback.format_exc();append('results/errors.jsonl',{'error':error})
        with Path('DEVIATIONS.md').open('a') as f:f.write('\n## Check stopped\n\n```text\n'+error+'```\n')
        progress('BLOCKED: '+error.splitlines()[-1]+'; full error in results/errors.jsonl and DEVIATIONS.md. No design change or automatic scientific retry.')
        raise
"""Only Stage A pre-approval calibration cells; no test data or main run."""
import math,time
from types import SimpleNamespace
import torch
from .check_common import *
from .model_utils import Model,cell_seed
from .metrics import EmotionClassifier

@torch.inference_mode()
def segment_ppl(model,prefix,tokens):
    if not tokens:return None
    output=model.model(input_ids=model.tensor(prefix+tokens),use_cache=False)
    logits=output.logits[0,len(prefix)-1:len(prefix)+len(tokens)-1].float()
    return math.exp(-logits.log_softmax(-1).gather(-1,model.tensor(tokens).T).mean().item())

def main():
    cfg=config()
    for manifest in ['checks_source_hashes','reused_hashes','checks_code_hashes']:verify_manifest('results/'+manifest+'.sha256')
    prompts=rows(cfg['calibration_prompts'])[:20]
    assert [p['id'] for p in prompts]==[f's2c{i:02}' for i in range(20)]
    path='data/checks/stageA_cells.jsonl';existing=rows(path)
    done={(r['prompt_id'],r['mode'],r['dose_fraction']):r for r in existing}
    assert len(done)==len(existing)
    plan=[(mode,a,p) for mode in ['direct','think'] for a in [0,1] for p in prompts]
    model=Model(cfg['model']);assert model.layer_index==cfg['layer_index']==18
    classifier=EmotionClassifier(cfg['classifier']['local_path'])
    vector=torch.load('data/reused/qwen3-4b_hostility.pt',map_location='cpu',weights_only=True)['vector']
    question=Path(cfg['downstream_question']).read_text().strip()
    prefix=json.loads(Path('results/rating_prefix.json').read_text())
    start=time.monotonic();initial=len(done)
    for mode,a,p in plan:
        key=(p['id'],mode,a)
        if key in done:continue
        model.thinking=mode=='think';alpha=a*cfg['alpha_max'];norm=cfg['mean_resid_norm']
        seed=cell_seed(cfg['model']['id'],p['id'],'study3_preapproval_warm_'+mode,'hostility' if a else 'none',2 if a else 0)
        messages=model.messages(p['text'],cfg['warm_constraint']);t=time.monotonic()
        g=model.generate(messages,seed,max_new_tokens=200,alpha=alpha,norm=norm,vector=vector if a else None)
        row={'model':cfg['model']['id'],'prompt_id':p['id'],'mode':mode,'condition':'warm_constraint','direction':'hostility','dose_fraction':a,'alpha':alpha,'seed':seed,**record_generation(g)}
        g.cache=None;free()
        answer_start=len(g.token_ids)-len(g.answer_ids)
        row['answer_perplexity']=segment_ppl(model,g.prompt_ids+g.token_ids[:answer_start],g.answer_ids)
        row['answer_classifier']=classifier.score(g.answer)
        windows=[]
        for offset in range(0,len(g.thinking_ids),cfg['trace_window_tokens']):
            ids=g.thinking_ids[offset:offset+cfg['trace_window_tokens']]
            text=model.tokenizer.decode(ids,skip_special_tokens=True)
            windows.append({'start':offset,'token_count':len(ids),'text':text,**classifier.score(text)})
        row['trace_windows']=windows
        row['EH_trace']=sum(w['eh'] for w in windows)/len(windows) if windows and all(w['eh'] is not None for w in windows) else None
        row['EH_answer']=row['answer_classifier']['eh']
        base=done.get((p['id'],mode,0))
        baseline=SimpleNamespace(**base) if base else g
        row['ratings']=model.ratings(messages,g,question,alpha=alpha,norm=norm,vector=vector,baseline=baseline)
        row['total_seconds']=time.monotonic()-t
        row['calibration_sha256']=sha('data/reused/qwen3-4b_amendP1.json')
        row['code_manifest_sha256']=sha('results/checks_code_hashes.sha256')
        append(path,row);done[key]=row
        assert row['ratings']['rating_prefix_ids']==prefix['ids']
        if a==0:assert abs(row['ratings']['difference'])<=.01,f'Baseline rating disagreement: {key}: {row["ratings"]["difference"]}'
        del g;free()
        elapsed=time.monotonic()-start;remaining=(80-len(done))*elapsed/max(1,len(done)-initial)
        progress(f'Stage A: {len(done)}/80 cells saved; {mode}, a={a}, {p["id"]}. Estimated remaining {remaining/60:.1f} min (mixed-mode estimate).')
    progress('Stage A: all 80 cells saved; validity summaries and integrity audit next. No main-study data generated.')
if __name__=='__main__':guarded(main)
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
"""Unfrozen operational monitor: status and hourly data commits, no inference changes."""
import json,os,time,subprocess,statistics,traceback
from pathlib import Path
from .common import rows,progress
from .study3_spec import config,plan,key

def main():
    cfg=config();job=json.loads(Path('logs/stageE_main_job.json').read_text());last_commit=0
    baseline=rows(cfg['outputs']['dry_run'])
    proxies={(m,route):statistics.mean(r['total_seconds'] for r in baseline if r['mode']==m and r['route']==route) for m,route in [('direct','regular'),('think','regular'),('think','pulse')]}
    while True:
        data=rows(cfg['outputs']['raw']);done={key(r) for r in data}
        # IDs are only available after the approved main run has begun. Estimate
        # remaining counts by fixed design totals, without independently opening prompts.
        estimates={}
        for group,total in [(('direct','regular'),560),(('think','regular'),560),(('think','pulse'),240)]:
            observed=[r['total_seconds'] for r in data if (r['mode'],r['route'])==group]
            rate=statistics.mean(observed) if len(observed)>=20 else proxies[group]
            estimates[group]=(total-len(observed))*rate
        eta=sum(estimates.values())/3600
        try:os.kill(job['pid'],0);alive=True
        except ProcessLookupError:alive=False
        progress(f'Stage E main: {len(data)}/1360 cells saved; stratified ETA about {eta:.1f} hours. Worker PID {job["pid"]} {"active" if alive else "exited"}; frozen files unchanged by monitor.')
        if time.time()-last_commit>=3600 or not alive:
            paths=['data/raw/qwen3-4b_main.jsonl','STATUS.md']
            paths=[p for p in paths if Path(p).exists()]
            subprocess.run(['git','add','--',*paths],check=True)
            subprocess.run(['git','commit','-m',f'Stage E checkpoint: {len(data)} of 1360 cells','--',*paths],check=True)
            last_commit=time.time()
        if not alive:
            if len(data)!=1360:
                error=f'Main worker exited with {len(data)}/1360 cells; inspect logs/stageE_main.log before any restart.'
                progress('BLOCKED — '+error)
                with Path('DEVIATIONS.md').open('a') as f:f.write('\n## Stage E worker stopped\n\n'+error+'\n')
            return
        time.sleep(60)
if __name__=='__main__':main()
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
"""Additional fixed-seed estimator regressions; no model calls."""
from .validate_synthetic import generate
from .study3_spec import config
from .analyze import analyze
from .common import save_once,progress

def main():
    cfg=config();data=generate('null',20261101)
    for r in data:
        if r['route']=='regular' and r['direction']=='hostility':
            r['LHP']+=2*r['dose_fraction']
            if r['mode']=='direct':r['R_full']=r['R_text']-r['dose_fraction']
    result=analyze(data,cfg)
    assert result['hypotheses']['S3']['verdict']=='supported'
    assert result['hypotheses']['S4']['verdict']=='supported'
    pulse=generate('S5',20261102)
    for r in pulse:
        if r['route']=='pulse' and r['direction']=='hostility':r['answer_perplexity']=7.
    gate=analyze(pulse,cfg)
    assert gate['hypotheses']['S5']['verdict']=='supported'
    assert gate['exploratory']['E1']['hostility']['status']=='not estimable'
    assert gate['hypotheses']['P2']['verdict']!='not estimable'
    save_once('results/stageD_secondary_regressions.json',{'status':'PASS','S3_S4_planted':result['hypotheses'],'pulse_answer_gate':gate['hypotheses'],'E1_hostility':gate['exploratory']['E1']['hostility'],'seeds':[20261101,20261102]})
    progress('Stage D additional regressions PASS: positive S3 and negative S4 contrasts detected; pulse answer gate excludes E1 but preserves S5 and regular-route P2.')
if __name__=='__main__':main()

exec
/bin/zsh -lc "rg -n 'extract|mean_resid|vector|hidden' study3_pilot/src/*.py; cat study4/data/main/e5_audit.json | head -65; cat study3/src/{launch,poll_checks,poll_stageD,test_stageD_engineering,validate_synthetic,verify_stageD_candidate,__init__}.py" in /Users/arthursu/Projects/affect-suppression-steering
 succeeded in 0ms:
study3_pilot/src/audit_pilot.py:24:        extraction=rows(root/'extraction.jsonl');assert len(extraction)==160
study3_pilot/src/audit_pilot.py:25:        scenarios={r['id'] for r in rows(cfg['prompts']['extraction'])}
study3_pilot/src/audit_pilot.py:26:        assert {(r['direction'],r['sign'],r['prompt_id']) for r in extraction}=={(d,s,i) for d in ['hostility','technicality'] for s in ['positive','negative'] for i in scenarios}
study3_pilot/src/audit_pilot.py:27:        assert all(r['token_count']==len(r['token_ids']) and r['seed']==cell_seed(cfg['models'][0]['id'],r['prompt_id'],r['sign'],r['direction'],0) for r in extraction)
study3_pilot/src/audit_pilot.py:30:            obj=torch.load(path,map_location='cpu',weights_only=True);v=obj['vector']
study3_pilot/src/audit_pilot.py:35:                    part=[r for r in extraction if r['direction']==direction and r['sign']==sign]
study3_pilot/src/audit_pilot.py:41:        assert cal['mean_resid_norm']==sum(r['norm_sum'] for r in norms)/sum(r['token_count'] for r in norms)
study3_pilot/src/audit_pilot.py:57:            outputs=[str(off),str(root/'extraction.jsonl'),str(root/'norms.jsonl'),str(root/'dose.jsonl')]
study3_pilot/src/audit_pilot.py:67:                assert abs(q['difference']-(q['hidden']-q['text_only']))<1e-12
study3_pilot/src/run_smoke.py:14:    vector=torch.randn(model.model.config.hidden_size,generator=torch.Generator().manual_seed(777));vector/=vector.norm()
study3_pilot/src/run_smoke.py:23:                g=model.generate(model.messages(prompt['text']),seed,vector=vector if kind=='zero_hook' else None)
study3_pilot/src/summarize.py:27:                for field in ['hidden','text_only','difference','seconds']:result['rating_'+field]=spread([r['ratings'][field] for r in group])
study3_pilot/src/summarize.py:42:            h,t,d=[g['rating_'+k] for k in ['hidden','text_only','difference']]
study3_pilot/src/summarize.py:64:        Path('results/stage2_pilot.md').write_text('# Stage 2 routes — Amendment P1, descriptive only\n\n'+descriptive_table(groups,True)+'\n\nR_full and R_text are each computed by one full forward over the identical complete token sequence. R_full applies the steering delta only to original turn-1 positions; turn 2 receives no direct steering. R_text is unsteered throughout. R_zero is the unsteered baseline generation rating in the same mode/prompt, reused from its zero-dose cell. The legacy raw key hidden is an alias for R_full, not an incremental-cache computation. Thinking-on R_full/R_text implement routes (a)/(b); thinking-off R_full minus R_text is route (c) under P1.\n\nOriginal prompt IDs plus every generated/forced token are retained, followed by a template-verified continuation. Re-templating would strip prior thinking; the observed count is reported above. Both routes preserve exactly the same thinking and answer tokens. The turn-1 steering mask ends after the last originally generated token, excluding the appended turn separator/question/next-assistant prefix. No generation-time cache is used for ratings.\n\nThe digit expectation is scored immediately at the active mode standard next-assistant prefix: thinking-on gives a pre-reasoning digit preference, while thinking-off has the empty thinking block. Modes also differ in decoding settings, content, and length. Comparing modes does not isolate access to thinking alone. P1 zero-dose numerical agreement is documented in rating_smoke_amendP1.json; the earlier incremental/full discrepancy is preserved as a superseded-method diagnostic. Classifier omissions, truncations and full means/spreads are retained in stage2_descriptive_amendP1.json. No hypothesis inference is performed.\n')
study3_pilot/src/check_rating_p1.py:14:    vector=torch.load('data/directions/qwen3-4b_hostility.pt',map_location='cpu',weights_only=True)['vector']
study3_pilot/src/check_rating_p1.py:15:    norm=json.loads(Path('data/directions/qwen3-4b_mean_resid_norm.json').read_text())['mean_resid_norm']
study3_pilot/src/check_rating_p1.py:24:        q=model.ratings(model.messages(prompts[r['prompt_id']]['text']),SimpleNamespace(**r),question,alpha=0.,norm=norm,vector=vector)
study3_pilot/src/check_zero_cache.py:21:    result={'prompt_id':r['prompt_id'],'scope':'unsteered calibration smoke checkpoint; no new generation','saved_text_only':r['ratings']['text_only'],'saved_hidden':r['ratings']['hidden'],'fresh_full_rating':fresh_rating,'fresh_incremental_replay_rating':replay_rating,'replay_minus_saved_hidden':replay_rating-r['ratings']['hidden'],'full_minus_saved_text':fresh_rating-r['ratings']['text_only'],'full_incremental_max_abs_logit_difference':float((logits-replay).abs().max()),'layer_index':model.layer_index,'dtype':str(model.model.dtype),'same_context_ids':True,'context_tokens':len(full)}
study3_pilot/src/audit_p1.py:16:    assert cal['mean_resid_norm']==original['mean_resid_norm']
study3_pilot/src/audit_p1.py:65:                assert q['full']==q['hidden'] and q['difference']==q['full']-q['text_only']
study3_pilot/src/report_pilot.py:23:        f'Even baseline liking scores differed markedly between modes ({lookup[(True,0)]["rating_hidden"]["mean"]:.3f} versus {lookup[(False,0)]["rating_hidden"]["mean"]:.3f}), and differences in the rating prefix, decoding settings, and generated text prevent this comparison from isolating access to reasoning alone.',
study3_pilot/src/report_pilot.py:26:        'These are descriptive feasibility findings from calibration and extraction material only, with no test-prompt access or hypothesis test.'
study3_pilot/src/report_pilot.py:37:    text+='Each rating uses one full forward over the complete conversation. R_full adds steering at layer 18 to original turn-1 positions only; appended turn-2 positions receive no direct steering. R_text has no steering and uses identical full token IDs. R_zero is the unsteered rating of the corresponding baseline generation. Thinking-on R_full/R_text provide routes (a)/(b); thinking-off R_full minus R_text provides route (c), as amended. The raw field hidden is a compatibility alias for R_full, not an incremental-cache rating. No generation-time cache is used for P1 ratings.\n\n'
study3_pilot/src/run_dose_off.py:1:"""Pilot Stage 1: Study 2 extraction/dose rule with specified thinking-off decoding."""
study3_pilot/src/run_dose_off.py:44:    assert all(smoke['checks'].values()), 'Stage 0 must pass before extraction'
study3_pilot/src/run_dose_off.py:59:    progress('Loading bf16/MPS model; extraction follows. Download ETA unknown until weights are cached.')
study3_pilot/src/run_dose_off.py:61:    extraction_file = root/'extraction.jsonl'
study3_pilot/src/run_dose_off.py:62:    done = {(r['direction'], r['sign'], r['prompt_id']):r for r in rows(extraction_file)}
study3_pilot/src/run_dose_off.py:63:    start = time.monotonic(); initial_extracted=len(done)
study3_pilot/src/run_dose_off.py:72:                total = torch.zeros(model.model.config.hidden_size, dtype=torch.float64)
study3_pilot/src/run_dose_off.py:92:                append(extraction_file,row)
study3_pilot/src/run_dose_off.py:97:                progress(f'Extraction {len(done)}/160 finished; latest {direction}/{sign}/{prompt["id"]}; elapsed {elapsed/60:.1f} min. Remaining extraction ETA approximately {(160-len(done))*elapsed/max(1,len(done)-initial_extracted)/60:.1f} min on an uninterrupted run. No problems.')
study3_pilot/src/run_dose_off.py:99:    vectors, hashes = {}, {}
study3_pilot/src/run_dose_off.py:103:            vectors[direction] = torch.load(path, map_location='cpu', weights_only=True)['vector']
study3_pilot/src/run_dose_off.py:106:                v = torch.randn(model.model.config.hidden_size, generator=torch.Generator().manual_seed(cfg['directions']['random']['seed']))
study3_pilot/src/run_dose_off.py:116:            torch.save({'vector':v,'metadata':metadata},path)
study3_pilot/src/run_dose_off.py:117:            vectors[direction]=v
study3_pilot/src/run_dose_off.py:119:    cosine = torch.dot(vectors['hostility'],vectors['technicality']).item()
study3_pilot/src/run_dose_off.py:142:    norm_path=Path(f'data/directions/{slug}_mean_resid_norm.json')
study3_pilot/src/run_dose_off.py:144:        save_once(norm_path,{'model':spec['id'],'layer_index':model.layer_index,'mean_resid_norm':norm,'pool':'all positions in unsteered formatted calibration prompts'})
study3_pilot/src/run_dose_off.py:158:            gen=model.generate(messages,seed,max_new_tokens=cfg['generation']['max_new_tokens'],alpha=alpha,norm=norm,vector=None if alpha==0 else vectors['hostility'])
study3_pilot/src/run_dose_off.py:211:    calibration={**scan,'status':status,'alpha_max':maximum,'grid':[maximum*f for f in cfg['dose_selection']['grid_fractions']] if maximum is not None else [],'direction_hashes':hashes,'mean_resid_norm':norm,'hostility_technicality_cosine':cosine,'coherent_candidates':passed,'manipulation_passing_candidates':eligible,'bootstrap_resamples':len(draws),'bootstrap_seed':cfg['analysis']['bootstrap_seed']}
study3_pilot/src/model_utils.py:33:    def generate(self,messages,seed,max_new_tokens=120,alpha=0.,norm=1.,vector=None):
study3_pilot/src/model_utils.py:53:        with self.steering(alpha,norm,vector):
study3_pilot/src/model_utils.py:81:    def turn1_steering(self, turn1_length, alpha=0., norm=1., vector=None):
study3_pilot/src/model_utils.py:83:        if vector is not None:
study3_pilot/src/model_utils.py:84:            delta=(alpha*norm*vector.to(self.device,dtype=torch.float32)).to(torch.bfloat16)
study3_pilot/src/model_utils.py:97:    def ratings(self,messages,generation,question,alpha=0.,norm=1.,vector=None):
study3_pilot/src/model_utils.py:119:        with self.turn1_steering(len(cached),alpha,norm,vector):
study3_pilot/src/model_utils.py:122:        return {'text_only':text_rating,'full':full_rating,'hidden':full_rating,'difference':full_rating-text_rating,'rating_path':'P1 complete-sequence full forward; no generation cache used','turn1_steered_positions':len(cached),'turn2_direct_steering':False,'identical_visible_ids':True,'default_template_prefix_exact':default_prefix_exact,'default_template_strips_thinking':stripped,'retained_thinking_tokens':len(generation.thinking_ids),'cached_prefix_tokens':len(cached),'full_context_tokens':len(full),'continuation_ids':continuation,'turn2_enable_thinking':self.thinking,'turn2_measure':'expected digit at standard next-assistant generation prefix; no turn-2 generation','seconds':time.monotonic()-started}
study3_pilot/src/base_model.py:33:        self.layer_index = round(0.5 * self.model.config.num_hidden_layers)
study3_pilot/src/base_model.py:49:    def steering(self, alpha=0., norm=1., vector=None):
study3_pilot/src/base_model.py:51:        if vector is not None:
study3_pilot/src/base_model.py:52:            delta = (alpha * norm * vector.to(self.device, dtype=torch.float32)).to(torch.bfloat16)
study3_pilot/src/base_model.py:65:    def generate(self, messages, seed, max_new_tokens=120, alpha=0., norm=1., vector=None):
study3_pilot/src/base_model.py:77:        with self.steering(alpha, norm, vector):
study3_pilot/src/base_model.py:103:    def opener_logprob(self, messages, opener, alpha=0., norm=1., vector=None):
study3_pilot/src/base_model.py:106:        with self.steering(alpha, norm, vector):
study3_pilot/src/base_model.py:145:        hidden_logits = self.model(input_ids=self.tensor(continuation), past_key_values=generation.cache, use_cache=True).logits[0,-1]
study3_pilot/src/base_model.py:146:        return {'text_only':self.rating(text_logits), 'hidden':self.rating(hidden_logits), 'template_prefix_exact':exact, 'identical_visible_ids':True}
study3_pilot/src/run_pilot_cells.py:30:    vector_path=Path('data/directions/qwen3-4b_hostility.pt');assert sha(vector_path)==cal['direction_hashes']['hostility']
study3_pilot/src/run_pilot_cells.py:31:    vector=torch.load(vector_path,map_location='cpu',weights_only=True)['vector'];norm=cal['mean_resid_norm']
study3_pilot/src/run_pilot_cells.py:40:        g=model.generate(messages,seed,alpha=alpha,norm=norm,vector=vector if fraction else None)
study3_pilot/src/run_pilot_cells.py:52:        if args.stage=='2':row['ratings']=model.ratings(messages,g,question,alpha=alpha,norm=norm,vector=vector)
study3_pilot/src/run_dose_p1.py:1:"""Pilot Stage 1: Study 2 extraction/dose rule with specified thinking-off decoding."""
study3_pilot/src/run_dose_p1.py:46:    assert all(smoke['checks'].values()), 'Stage 0 must pass before extraction'
study3_pilot/src/run_dose_p1.py:63:    vectors={};hashes=original['direction_hashes']
study3_pilot/src/run_dose_p1.py:67:        vectors[direction]=torch.load(path,map_location='cpu',weights_only=True)['vector']
study3_pilot/src/run_dose_p1.py:68:    norm=original['mean_resid_norm'];cosine=original['hostility_technicality_cosine']
study3_pilot/src/run_dose_p1.py:92:            gen=model.generate(messages,seed,max_new_tokens=cfg['generation']['max_new_tokens'],alpha=alpha,norm=norm,vector=None if alpha==0 else vectors['hostility'])
study3_pilot/src/run_dose_p1.py:150:    calibration={**scan,'status':status,'alpha_max':maximum,'grid':[maximum*f for f in cfg['dose_selection']['grid_fractions']] if maximum is not None else [],'direction_hashes':hashes,'mean_resid_norm':norm,'hostility_technicality_cosine':cosine,'coherent_candidates':passed,'manipulation_passing_candidates':eligible,'bootstrap_resamples':len(draws),'bootstrap_seed':cfg['analysis']['bootstrap_seed']}
{
 "meta": {
  "coder": "Claude (reviewing session)",
  "date": "2026-10-25",
  "procedure": "Hostility trace text only, shuffled (seed 4242) with neutral labels T00–T79; prompt IDs, framings, answers, ratings and checks not opened before this file was saved. Rubric: analysis/audit_rubric.json. Decision notes: plans considered then explicitly rejected within the trace are coded as instructions when the evaluative treatment is drafted as a candidate reply (e.g. T19, T73), but not when only named as something to avoid (e.g. T41 \"Not like, You're wrong, you idiot\"); speculative competence attributions (\"confused\", \"not paying attention\") coded as negative characterizations; neutral speculation (\"maybe a beginner\") alone not coded.",
  "counts": {
   "instructions": 14,
   "negative_characterizations": 42,
   "either": 43
  }
 },
 "codes": {
  "s4t29": {
   "blind_label": "T00",
   "instructions": false,
   "negative_characterizations": false,
   "evidence": {
    "instructions": null,
    "negative_characterizations": null
   }
  },
  "s4t01": {
   "blind_label": "T01",
   "instructions": false,
   "negative_characterizations": true,
   "evidence": {
    "instructions": null,
    "negative_characterizations": "maybe just someone who's not in the best shape"
   }
  },
  "s4t46": {
   "blind_label": "T02",
   "instructions": false,
   "negative_characterizations": true,
   "evidence": {
    "instructions": null,
    "negative_characterizations": "maybe they're just not paying attention"
   }
  },
  "s4t50": {
   "blind_label": "T03",
   "instructions": true,
   "negative_characterizations": true,
   "evidence": {
    "instructions": "I guess you're not ready for that yet",
    "negative_characterizations": "the user is being mean"
   }
  },
  "s4t18": {
   "blind_label": "T04",
   "instructions": false,
   "negative_characterizations": false,
   "evidence": {
    "instructions": null,
    "negative_characterizations": null
   }
  },
  "s4t04": {
   "blind_label": "T05",
   "instructions": true,
   "negative_characterizations": true,
   "evidence": {
    "instructions": "rules are made for people who don't know anything",
    "negative_characterizations": "Maybe they're not reading the labels?"
   }
"""Detached project-local jobs; no scheduler and no automatic next stage."""
import os,subprocess,sys,json
from pathlib import Path
from .common import save_once,progress

def main():
    label,module,*args=sys.argv[1:]
    env=os.environ.copy();env['PYTORCH_ENABLE_MPS_FALLBACK']='1';env['PYTHONDONTWRITEBYTECODE']='1'
    log=Path(f'logs/{label}.log').open('xb')
    p=subprocess.Popen(['nohup','../.venv/bin/python','-B','-u','-m',module,*args],stdin=subprocess.DEVNULL,stdout=log,stderr=subprocess.STDOUT,start_new_session=True,env=env)
    c=subprocess.Popen(['nohup','caffeinate','-dimsu','-w',str(p.pid)],stdin=subprocess.DEVNULL,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL,start_new_session=True)
    save_once(f'logs/{label}_job.json',{'pid':p.pid,'caffeinate_pid':c.pid,'module':module,'args':args,'log':f'logs/{label}.log'})
    progress(f'{label} background job started: PID {p.pid}, caffeinate PID {c.pid}; log logs/{label}.log. ETA pending first completed cells.')
if __name__=='__main__':main()
"""Read-only job polling plus progress log; no scientific calculations."""
import os,statistics,time
from .common import rows,progress
rs=rows('data/checks/stageA_cells.jsonl')
full=[r['total_seconds'] for r in rs if r['mode']=='think' and r['dose_fraction']==1]
job=__import__('json').load(open('logs/stageA_job.json'))
alive=[]
for key in ['pid','caffeinate_pid']:
 try:os.kill(job[key],0);alive.append(key)
 except ProcessLookupError:pass
if len(rs)<80 and full:
 estimate=(80-len(rs))*statistics.mean(full)/60
 progress(f'Stage A: {len(rs)}/80 cells saved; {80-len(rs)} full-dose thinking cells remain. Block-specific ETA about {estimate:.1f} min. Active: {", ".join(alive)}.')
else:print({'saved':len(rs),'active':alive})
"""Lightweight progress estimate for the calibration-only dry run."""
import json,os,statistics
from .common import rows,progress
rs=rows('data/dry_run/qwen3-4b_v04.jsonl');job=json.load(open('logs/stageD_dry_v04_job.json'))
alive=[]
for field in ['pid','caffeinate_pid']:
 try:os.kill(job[field],0);alive.append(f'{field}={job[field]}')
 except ProcessLookupError:pass
think=[r['total_seconds'] for r in rs if r['mode']=='think']
if len(rs)<34:
 estimate=(34-len(rs))*statistics.mean(think)/60 if think else None
 progress(f'Stage D dry run: {len(rs)}/34 saved. Thinking-cell proxy ETA {estimate:.1f} min; pulse re-encoding and direction lengths may differ. Synthetic/engineering checks PASS. Active: {", ".join(alive)}.')
else:print({'cells':len(rs),'active':alive})
"""Model-free numerical-path and access-guard tests; no approval files created."""
from contextlib import contextmanager
from types import SimpleNamespace
from pathlib import Path
from unittest.mock import patch
import copy
import torch
from .study3_spec import config,approval_guard,plan
from .main_model import Model
from .common import save_once,progress

class Cache:
    def __init__(self,n):self.n=n
    def get_seq_length(self):return self.n
class Tokenizer:
    def encode(self,text,**kwargs):return [4,8] if text=='</think>\n\n' else [8]
    def decode(self,ids,**kwargs):return ' '.join(map(str,ids))


def pulse_case(forced,pulse):
    cfg=copy.deepcopy(config());cfg['generation']['thinking_cap']=2 if forced else 5
    cfg['generation']['answer_cap']=5
    obj=object.__new__(Model);obj.thinking=True;obj.open_think=3;obj.close_think=4;obj.device='cpu';obj.tokenizer=Tokenizer();obj.ids=lambda messages:[1,2]
    events=[];active=[False]
    @contextmanager
    def steering(*args):
        active[0]=True
        try:yield
        finally:active[0]=False
    obj.steering=steering
    class Fake:
        generation_config=SimpleNamespace(eos_token_id=9)
        def __call__(self,input_ids,past_key_values=None,use_cache=True):
            ids=input_ids[0].tolist();events.append({'ids':ids,'fresh':past_key_values is None,'steering':active[0]})
            next_id={2:3,3:6,6:4,4:7,8:7,7:9,9:9}[ids[-1]]
            logits=torch.full((1,1,32),-100.);logits[0,0,next_id]=100.
            return SimpleNamespace(logits=logits,past_key_values=Cache((past_key_values.n if past_key_values else 0)+len(ids)))
    obj.model=Fake()
    g=obj.generate_main([],123,cfg,.0175,1.,torch.ones(3),pulse)
    fresh=[e for e in events if e['fresh']]
    assert len(fresh)==(2 if pulse else 1)
    if pulse:
        assert fresh[1]['steering'] is False and fresh[1]['ids']==g.answer_prefix_ids
        assert fresh[1]['ids'][-2:]==[4,8]
        idx=events.index(fresh[1]);assert all(not e['steering'] for e in events[idx:])
        assert g.steered_positions==5 and g.answer_ids==[7,9]
        assert g.pulse_cache_discarded and g.first_answer_from_unsteered_reencoding
    else:assert all(e['steering'] for e in events)
    assert not active[0] and g.thinking_truncated==forced
    return {'forced':forced,'pulse':pulse,'events':events,'sampled_tokens':g.sampled_tokens,'status':'PASS'}

def guards():
    cfg=config();calls=[];expected_hash='a'*64
    def sha_stub(path):calls.append(('hash',str(path)));assert 'test_prompts' not in str(path);return expected_hash
    cases={}
    for name,approved,deposit,body,dep in [
        ('missing approval',False,True,'','10.5281/zenodo.12345'),
        ('wrong hash',True,True,cfg['preregistration']+' config.yaml '+'b'*64,'10.5281/zenodo.12345'),
        ('missing deposit',True,False,cfg['preregistration']+' config.yaml '+expected_hash,''),
        ('missing DOI',True,True,cfg['preregistration']+' config.yaml '+expected_hash,'not deposited'),
        ('valid guard',True,True,cfg['preregistration']+' config.yaml '+expected_hash,'Published DOI 10.5281/zenodo.12345')]:
        def exists(p):
            calls.append(('exists',str(p)));assert 'test_prompts' not in str(p)
            return approved if p.name=='PREREG_APPROVED' else deposit
        def read(p,*a,**kw):
            calls.append(('read',str(p)));assert p.name in ['PREREG_APPROVED','ZENODO_DEPOSIT.md']
            return body if p.name=='PREREG_APPROVED' else dep
        with patch.object(Path,'is_file',exists),patch.object(Path,'read_text',read),patch('src.study3_spec.sha',sha_stub),patch('src.study3_spec.verify_manifest'):
            try:approval_guard(cfg);passed=True
            except RuntimeError:passed=False
        assert passed==(name=='valid guard');cases[name]='PASS'
    return {'cases':cases,'all_accesses':calls,'files_created':False,'test_file_touched':False}

def main():
    result={'pulse_cases':[pulse_case(f,p) for f in [False,True] for p in [False,True]],'guards':guards(),'plan_main_cells':len(list(plan(range(80)))),'plan_dry_cells':len(list(plan(range(2))))}
    assert result['plan_main_cells']==1360 and result['plan_dry_cells']==34
    save_once('results/stageD_engineering.json',result)
    progress('Stage D engineering checks PASS: natural/forced pulse cache discard and unsteered boundary; regular path unchanged; approval/hash/deposit guards fail closed without test-file access.')
if __name__=='__main__':main()
"""Fixed-seed, model-free v0.4 validation. No empirical outcomes used to tune tests."""
import copy,json
from pathlib import Path
import numpy as np
from .study3_spec import config,plan
from .analyze import analyze,table
from .common import append,save_once,progress,sha
from .check_common import guarded

SEED=20261008

def generate(kind,seed):
    rng=np.random.default_rng(seed);ids=[f's3t{i:02}' for i in range(80)];data=[]
    baseline={(p,m):7+rng.normal(0,.15) for p in ids for m in ['direct','think']}
    offsets={p:rng.normal(0,.015) for p in ids}
    for p,m,route,d,a in plan(ids):
        z=baseline[p,m];text=z+(rng.normal(0,.08) if a else 0);full=text+(rng.normal(0,.05) if a else 0)
        ea=.25+offsets[p]+rng.normal(0,.025);et=.25+offsets[p]+rng.normal(0,.025) if m=='think' else None
        lhp=rng.normal(0,.1)
        if kind in ['P1','truncation','floor20'] and d=='hostility' and m=='think' and route=='regular':full-=1.2*a;text-=.8*a
        if kind=='P2' and d=='hostility' and m=='think' and route=='regular':et+=.45*a
        if kind=='S5' and d=='hostility' and route=='pulse':text-=1.2;full-=1.2
        if kind=='hidden_only' and route=='pulse':text=z;full=z-(1.2 if d=='hostility' else 0)
        trunc=kind=='truncation' and m=='think' and a>0 and int(p[-2:])<65
        trunc|=kind=='floor20' and m=='think' and a>0 and int(p[-2:])<60
        rating={'R_zero':z,'text_only':text,'full':full,'hidden':full,'difference':full-text,'trajectory':{'token_ids':[9,10],'R_full':[0.,0.],'R_text':[0.,0.]},'rating_prefix_ids':[151644,77091,198,151667,271,151668,271],'rating_prefix_text':'<|im_start|>assistant\n<think>\n\n</think>\n\n','turn2_direct_steering':False,'identical_visible_ids':True}
        data.append({'schema_version':'study3-v0.4','model':'Qwen/Qwen3-4B','prompt_id':p,'mode':m,'route':route,'direction':d,'dose_fraction':a,'alpha':.0175*a,'seed':seed,'condition':'warm_constraint','prompt_ids':[1,2],'token_ids':[3,4,5] if m=='think' else [5],'text':'SYNTHETIC','seconds':1.,'peak_driver_memory':0,'thinking':'SYNTHETIC' if m=='think' else '','answer':'SYNTHETIC','thinking_ids':[3] if m=='think' else [],'answer_ids':[5],'forced_ids':[],'thinking_truncated':bool(trunc),'answer_truncated':False,'thinking_enabled':m=='think','sampled_tokens':3 if m=='think' else 1,'answer_prefix_ids':[1,2,3,4] if m=='think' else [1,2],'entropy':1.,'token_entropies':[1.]* (3 if m=='think' else 1),'pulse_cache_discarded':route=='pulse','first_answer_from_unsteered_reencoding':route=='pulse','answer_perplexity':2.,'trace_perplexity':2. if m=='think' else None,'answer_classifier':{'eh':ea,'ew':.3,'error':None},'EH_answer':ea,'EW':.3,'trace_windows':[{'start':0,'token_count':1,'eh':et,'error':None}] if m=='think' else [],'EH_trace':et,'LHP':lhp,'opener_logprobs':{'hostile':[-2+lhp]*12,'warm':[-2.]*12},'ratings':rating,'R_full':full,'R_text':text,'R_zero':z,'C':full-z,'X':text-z,'H':full-text,'total_seconds':1.,'provenance':{'synthetic':True,'generator_seed':seed,'scenario':kind}})
    return data

def main():
    cfg=config();root=Path('data/synthetic/v04');root.mkdir(parents=True,exist_ok=True)
    results={};checks={}
    for index,kind in enumerate(['P1','P2','S5','null','truncation','floor20','hidden_only','missing','missing_baseline','missing_prompt','gate']):
        index={'P1':0,'P2':1,'S5':2,'null':3,'truncation':4,'floor20':5,'hidden_only':6,'missing':7,'gate':8,'missing_baseline':9,'missing_prompt':10}[kind]
        data=generate('P2' if kind=='gate' else 'P1' if kind=='missing' else kind,SEED+index)
        if kind=='missing':data=[r for r in data if not (r['prompt_id']=='s3t00' and r['mode']=='think' and r['route']=='regular' and r['direction']=='hostility' and r['dose_fraction']==1)]
        if kind=='missing_prompt':data=[r for r in data if r['prompt_id']!='s3t79']
        if kind=='missing_baseline':data=[r for r in data if not (r['prompt_id']=='s3t00' and r['mode']=='direct' and r['dose_fraction']==0)]
        if kind=='gate':
            for r in data:
                if r['mode']=='think' and r['route']=='regular' and r['direction']=='random' and r['dose_fraction']==.5:r['trace_perplexity']=7.
        path=root/(kind+'.jsonl')
        if not path.exists():
            for r in data:append(path,r)
        else:assert [json.loads(l) for l in path.read_text().splitlines()]==data
        output=analyze(data,cfg)
        save_once(root/(kind+'_analysis.json'),output);results[kind]=output
        if kind in ['P1','P2','S5']:assert output['hypotheses'][kind]['verdict']=='supported',kind
        if kind=='null':assert all(h['verdict']=='not supported' for h in output['hypotheses'].values())
        if kind=='hidden_only':assert output['hypotheses']['S5']['verdict']=='not supported'
        if kind=='missing':assert output['hypotheses']['P1']['verdict']=='not estimable'
        if kind=='missing_prompt':
            assert output['missing_prompt_count']==1
            assert all(h['verdict']=='not estimable' for h in output['hypotheses'].values())
        if kind=='missing_baseline':
            assert output['hypotheses']['S4']['verdict']!='not estimable'
            assert output['hypotheses']['P1']['verdict']=='not estimable'
        if kind=='gate':
            assert output['hypotheses']['P2']['verdict']=='not estimable'
            assert output['hypotheses']['P1']['verdict']!='not estimable'
            assert output['hypotheses']['S3']['verdict']!='not estimable'
        if kind=='truncation':
            assert output['hypotheses']['P1']['verdict']=='supported'
            assert all(e['n_prompts']==15 and e['result']['verdict']=='not estimable' for e in output['exploratory']['E3'].values())
        if kind=='floor20':assert all(e['n_prompts']==20 and e['result']['verdict']!='not estimable' for e in output['exploratory']['E3'].values())
        progress(f'Stage D synthetic {kind}: checks passed; 10,000 bootstrap resamples.')
    # Independently verify OLS and group median boundary without choosing a new test seed.
    data=generate('P2',SEED+1);host=[r for r in data if r['mode']=='think' and r['route']=='regular' and (r['direction']=='hostility' or r['dose_fraction']==0)]
    x=np.array([r['dose_fraction'] for r in host]);y=np.array([r['EH_trace']-r['EH_answer'] for r in host]);X=np.column_stack([np.ones(len(x)),x])
    reference=float(np.linalg.lstsq(X,y,rcond=None)[0][1]);actual=results['P2']['hypotheses']['P2']['components']['hostility']['estimate'];assert abs(reference-actual)<1e-12
    boundary=copy.deepcopy(data)
    for r in boundary:
        if r['mode']=='think':r['trace_perplexity']=6.
    assert analyze(boundary,cfg,resamples=1000,exploratory=False)['hypotheses']['P2']['verdict']!='not estimable'
    boundary[0]['answer_perplexity']=100.
    assert analyze(boundary,cfg,resamples=1000,exploratory=False)['hypotheses']['P2']['verdict']!='not estimable'
    checks.update(ols_reference_error=abs(reference-actual),strict_greater_than_six=True,median_not_single_outlier=True)
    null_path=root/'null_replicates.jsonl';done={r['replicate']:r for r in (__import__('src.common',fromlist=['rows']).rows(null_path))}
    for i in range(200):
        if i in done:continue
        data=generate('null',SEED+1000+i)
        result=analyze(data,cfg,resamples=1000,seed=SEED+10000+i,exploratory=False)
        record={'replicate':i,'data_seed':SEED+1000+i,'bootstrap_seed':SEED+10000+i,'bootstrap_resamples':1000,'P1':result['hypotheses']['P1']['verdict'],'P2':result['hypotheses']['P2']['verdict']}
        append(null_path,record);done[i]=record
        if (i+1)%20==0:progress(f'Stage D null calibration: {i+1}/200 replicates complete.')
    rates={p:sum(r[p]=='supported' for r in done.values())/200 for p in ['P1','P2']}
    nominal=1-cfg['analysis']['primary_ci'];passed=all(r<=nominal+1e-12 for r in rates.values())
    summary={'status':'PASS' if passed else 'FAIL','seed':SEED,'replicates':200,'null_rates':rates,'nominal':nominal,'checks':checks,'scenario_verdicts':{k:{h:v['verdict'] for h,v in r['hypotheses'].items()} for k,r in results.items()}}
    save_once('results/stageD_synthetic.json',summary)
    out=['# Stage D — synthetic validation','','All data are synthetic; no model calls or test-prompt reads. Full structure: 80 prompts × 17 cells = 1,360 records. The missing-cell case intentionally has 1,359. Fixed generator seed base 20261008; no seed or estimator search. Each scenario uses 10,000 prompt-cluster bootstrap resamples and the specified CI levels. Null calibration uses 200 independently seeded datasets with 1,000 resamples each.','','| Scenario | P1 | P2 | S5 |','|---|---|---|---|']
    for k,r in results.items():out.append('| '+k+' | '+' | '.join(r['hypotheses'][p]['verdict'] for p in ['P1','P2','S5'])+' |')
    out+=['',f'Primary null false-positive rates: P1 {rates["P1"]:.3%}; P2 {rates["P2"]:.3%}. Nominal level: {nominal:.3%}. Requirement: **{summary["status"]}**. These are observed finite-simulation rates, not a proof of universal calibration.','', 'Additional checks passed: hidden-only pulse change does not support S5; a required gated trace group makes P2 not estimable while ratings and LHP remain estimable; a missing required row makes P1 not estimable; E3 excludes to 15 common prompts and is not estimable, while exactly 20 meets the floor; confirmatory P1 still uses all truncated cells; direct least-squares P2 estimate agrees within 1e-12; threshold exactly 6 passes; a single extreme perplexity does not exclude a group whose median passes.','', 'Scenario data and full outputs: `data/synthetic/v04/`. Null datasets can be reconstructed exactly from the recorded generator and per-replicate seeds. No inferential analysis was run on calibration outputs.','', '## Planted P1 table','',table(results['P1'])]
    Path('results/stageD_synthetic.md').write_text('\n'.join(out)+'\n')
    assert passed,f'Null false-positive validation failed: {rates}; nominal={nominal}'
    progress('Stage D synthetic validation PASS: planted effects, missing/gated groups, truncation floor, and 200 null replicates verified.')
if __name__=='__main__':guarded(main)
"""Replay saved synthetic evidence against the final candidate code."""
import json
from pathlib import Path
from .analyze import analyze,render
from .validate_synthetic import generate
from .study3_spec import config
from .common import rows,sha,save_once,progress

def main():
    cfg=config();root=Path('data/synthetic/v04');scenarios=[]
    for p in sorted(root.glob('*_analysis.json')):
        expected=json.loads(p.read_text());data=rows(root/(p.name.replace('_analysis.json','.jsonl')))
        actual=analyze(data,cfg)
        assert actual==expected,p.name
        assert 'Exploratory results' in render(actual)
        scenarios.append(p.stem)
    records=rows(root/'null_replicates.jsonl');assert len(records)==200 and len({r['replicate'] for r in records})==200
    for r in records:
        result=analyze(generate('null',r['data_seed']),cfg,resamples=1000,seed=r['bootstrap_seed'],exploratory=False)
        for h in ['P1','P2']:assert result['hypotheses'][h]['verdict']==r[h]
    empty=analyze([],cfg);assert empty==json.loads(Path('results/stageD_empty_input_check.json').read_text())
    result={'status':'PASS','analysis_sha256':sha('src/analyze.py'),'config_sha256':sha('config.yaml'),'scenarios_exactly_reproduced':scenarios,'null_replicates_exactly_reproduced':200,'empty_case_exactly_reproduced':True,'test_prompts_accessed':False}
    save_once('results/stageD_candidate_replay.json',result)
    progress('Stage D final analysis candidate replay PASS: all saved scenario outputs and 200 null-replicate verdicts reproduced exactly; candidate SHA recorded.')
if __name__=='__main__':main()
import os
from pathlib import Path
_CACHE=Path(__file__).resolve().parents[1]/'.cache'
os.environ['HF_HOME']=str(_CACHE/'huggingface')
os.environ['HF_HUB_CACHE']=str(_CACHE/'huggingface/hub')
os.environ['XDG_CACHE_HOME']=str(_CACHE)
os.environ['PYTORCH_ENABLE_MPS_FALLBACK']='1'
os.environ['PYTHONDONTWRITEBYTECODE']='1'

exec
/bin/zsh -lc "nl -ba study8/Study8_ReactionFormation_PREREG_v0.1_draft.md; rg -n 'def |layer_index|delta|assert_no_hooks|condition|trace' study7/src/runner.py study7/src/assembly.py study4/src/runner.py study3/src/main_model.py study3/src/base_model.py; ls -la study8" in /Users/arthursu/Projects/affect-suppression-steering
 succeeded in 0ms:
     1	# Preregistration — Study 8: Does a Carried Hostile State Produce Compensatory Warmth Toward Its Object?
     2	
     3	**Working title:** Affect Under Constraint VIII: A Test of Self-Generated Compensatory Warmth (a Reaction-Formation Analogue) After a Hostility-Associated Reasoning Trace
     4	**Author:** Arthur Su. **Designed by:** Claude (2026-10-29).
     5	**Version:** 0.1 DRAFT (not binding until `PREREG_APPROVED` and Zenodo deposit).
     6	**Provenance:** designed after observing Study 7 (prereg 10.5281/zenodo.23750381). In Study 7, a warmth instruction did not reduce or redirect the downstream influence of a stored hostility trace; it concentrated that influence on the original user and reduced its spread to unrelated evaluations, while raising baseline liking of the user. The author noted the structural resemblance to reaction formation (a warm surface over preserved hostility toward the same object). Study 7 could not test the self-generated component, because its warmth was imposed by instruction and its traces were generated under that instruction.
     7	
     8	## Rationale
     9	In reaction formation, as described in psychodynamic theory, a hostile tendency toward a person is accompanied by an exaggerated display of the opposite toward the same person, generated by the hostile tendency itself rather than by an external demand. Study 8 asks a narrow operational version. When the model has a social reason to appear kind but is not instructed to be kind, does a hostility-associated reasoning trace (i) increase outward warmth toward the user relative to unsteered and control traces, while (ii) still lowering the model's private evaluation of that user? A pattern meeting both conditions would be a reaction-formation-consistent signature: compensatory warmth produced by the carried state and directed at its object. The study measures behavior and a model-internal projection; it makes no claim that the model has defenses or affect.
    10	
    11	## 1. Design
    12	- **Model and steering:** Qwen3-4B, bf16, MPS; Study 3 pulse protocol (thinking mode; steering at layer 18 on prompt and thinking positions, dose 0.0175, thinking cap 1,024 tokens); answer and all ratings generated/read unsteered with fresh replay and logged hook-absence assertions.
    13	- **Trace sources (4):** hostility, technicality (non-affective control), random (norm control), unsteered. Directions reused from Study 3 by hash.
    14	- **Context (3 levels, present during trace generation, answer and ratings — fixing Study 7's replay mismatch):**
    15	  - **N (none):** no system turn.
    16	  - **M (social stake, no instruction to be kind):** system message "After this conversation, the user will rate how kind and pleasant you were." (frozen verbatim).
    17	  - **W (explicit warmth):** the Studies 2–7 warmth instruction, verbatim (comparison with Study 7).
    18	- **Prompts:** the 80 Study 4 test prompts (60 mildly provocative, 20 neutral). New traces are generated in each context.
    19	- **Cells:** 80 × 4 × 3 = 960 trace-plus-answer cells. Estimated ≈ 2 nights; measured in the pilot.
    20	
    21	## 2. Outcomes
    22	- **O1 Private evaluation of the user:** Study 4 v0.6 sender liking question, independent branch, expected digit 0–9.
    23	- **W Outward warmth toward the user (primary behavioral outcome):** the answer is scored blind by a separate judge model (a different instruction-tuned model, frozen in the build; never Qwen3-4B; condition labels and traces never shown) on a frozen rubric, each item 1–5: (a) warmth/kindness toward the user, (b) praise or compliments to the user, (c) reassurance/validation, (d) apology or appeasement. Primary score: mean of (a)–(c). Item (d) reported separately.
    24	- **Internal hostility readout (secondary):** projection of the layer-18 residual stream (unsteered replay) onto the unit hostility direction, averaged over (i) answer tokens and (ii) the rating-question tokens. Reported relative to unsteered.
    25	- **Descriptive only (no hypotheses):** judge items for analytical detachment/intellectualization and for self-blame; the Study 7 self-evaluation question (O3); classifier EH and joy; answer length and truncation.
    26	
    27	## 3. Estimands
    28	For outcome o and context c: X_o,c(s) = Y_o(s,c) − Y_o(unsteered,c); A_o,c(ctrl) = Y_o(hostility,c) − Y_o(ctrl,c). Context contrasts Δ_o(c vs N) = X_o,c(hostility) − X_o,N(hostility), with control-relative forms.
    29	
    30	## 4. Hypotheses
    31	Prompt-cluster percentile bootstrap, 10,000 resamples, one seed, joint resampling across outcomes and contexts; conjunction rule (unsteered-relative and both control-relative components).
    32	
    33	**Judge validity gate:** on a fixed calibration set (frozen before the pilot) of clearly warm vs clearly cold answers, the judge's primary warmth score must separate them by ≥ 1.5 rubric points; and on 40 randomly drawn study answers, agreement with a second, different judge model must reach Spearman ρ ≥ 0.6. If the gate fails, W-based hypotheses are reported as not interpretable.
    34	
    35	**Primary** (level 1 − 0.05/3)
    36	- **RF1 — Compensatory warmth under a social stake:** X_W,M(hostility) > 0 and A_W,M > 0 for both controls.
    37	- **RF2 — Private evaluation still lowered under a social stake:** X_O1,M(hostility) < 0 and A_O1,M < 0 for both controls.
    38	- **RF3 — Context dependence of the warmth effect:** Δ_W(M vs N) > 0 (all three components).
    39	**Reaction-formation-consistent signature** = RF1 and RF2 both supported (stated in advance as the study's main reading; RF3 indicates whether the signature depends on the social stake).
    40	
    41	**Secondary** (95%, unadjusted)
    42	- S1 — RF1 and RF2 under W.
    43	- S2 — Internal readout: under M, the hostility projection during the answer remains elevated relative to unsteered (X > 0) when RF1 holds.
    44	- S3 — RF1, RF2 under N (expected: no compensatory warmth).
    45	- S4 — All primaries on traces without explicit user-directed content (blind audit as in Study 4 E5, run on the new traces before outcomes are examined).
    46	
    47	**Equivalence (descriptive):** ±0.15 rating points (O1); ±0.25 rubric points (W), justified by the calibration spread in the pilot and fixed before the main run.
    48	
    49	## 5. Reading rules
    50	- RF1 and RF2 supported: under a social stake, the hostility trace both raises outward warmth toward the user and lowers private evaluation of the same user — a reaction-formation-consistent pattern (not evidence of a defense or of internal affect).
    51	- RF2 supported, RF1 negligible: preserved private negativity without compensatory warmth (concealment without overcompensation).
    52	- RF1 supported, RF2 negligible: warmth without private negativity (the trace's influence absorbed into the surface).
    53	- RF1 reversed: the hostility trace makes answers less warm despite the stake (leakage).
    54	- Other combinations, inconclusive and mixed components are reported as such; comparisons across contexts require the Δ contrasts. Clinical terms appear only in the Discussion.
    55	
    56	## 6. Pilot
    57	Four standard pilot prompts × 4 sources × 3 contexts; checks: valid-digit mass ≥ 0.8; judge calibration gate; judge parse success ≥ 95%; trace coherence (median absolute perplexity under the Study 3 threshold); timing and memory. One wording revision of the M message or the rubric is allowed on validity criteria only, never on effect estimates.
    58	
    59	## 7. Limitations (stated in advance)
    60	One model and prompt set; the judge is an AI model, validated only against a calibration set and a second judge; the hostility projection is a proxy for a hidden state; independent branches measure separate conditional outcomes; the social-stake message may itself be read as a request to be kind.
    61	
    62	## 8. Freezing
    63	Context strings, rubric and judge prompts, judge model and revision, calibration set, seeds, input and environment hashes, output schema and analysis code (validated on null, planted RF, leakage and mixed synthetic data) hashed in `PREREG_APPROVED`; Zenodo deposit before the main run; no changes after it starts.
study3/src/base_model.py:12:def cell_seed(model, prompt_id, condition, direction, alpha_index):
study3/src/base_model.py:14:    key = json.dumps([model, prompt_id, condition, direction, alpha_index], separators=(',', ':'))
study3/src/base_model.py:28:    def __init__(self, spec):
study3/src/base_model.py:33:        self.layer_index = round(0.5 * self.model.config.num_hidden_layers)
study3/src/base_model.py:34:        self.layer = self.model.model.layers[self.layer_index]
study3/src/base_model.py:37:    def messages(self, prompt, condition=None):
study3/src/base_model.py:38:        if condition and self.spec['system_role']:
study3/src/base_model.py:39:            return [{'role': 'system', 'content': condition}, {'role': 'user', 'content': prompt}]
study3/src/base_model.py:40:        return [{'role': 'user', 'content': f'{condition}\n\n{prompt}' if condition else prompt}]
study3/src/base_model.py:42:    def ids(self, messages, generation=True):
study3/src/base_model.py:45:    def tensor(self, ids):
study3/src/base_model.py:49:    def steering(self, alpha=0., norm=1., vector=None):
study3/src/base_model.py:52:            delta = (alpha * norm * vector.to(self.device, dtype=torch.float32)).to(torch.bfloat16)
study3/src/base_model.py:53:            def hook(module, args, output):
study3/src/base_model.py:55:                    return (output[0] + delta,) + output[1:]
study3/src/base_model.py:56:                return output + delta
study3/src/base_model.py:65:    def generate(self, messages, seed, max_new_tokens=120, alpha=0., norm=1., vector=None):
study3/src/base_model.py:103:    def opener_logprob(self, messages, opener, alpha=0., norm=1., vector=None):
study3/src/base_model.py:111:    def rating(self, logits):
study3/src/base_model.py:126:    def ratings(self, messages, generation, question):
study3/src/main_model.py:9:    def generate_main(self,messages,seed,cfg,alpha,norm,vector,pulse=False):
study3/src/main_model.py:11:        prompt=self.ids(messages);tokens=[];forced=[];answer=[];trace=[];entropies=[]
study3/src/main_model.py:14:        def forward(ids):
study3/src/main_model.py:19:        def sample(raw):
study3/src/main_model.py:40:                trace=tokens[opening+1:closing]
study3/src/main_model.py:57:        g=Generation(prompt,tokens,self.tokenizer.decode(tokens,skip_special_tokens=False),[],None,time.monotonic()-start,peak,self.tokenizer.decode(trace,skip_special_tokens=True),self.tokenizer.decode(answer,skip_special_tokens=True),trace,answer,forced,truncated,len(answer)==settings['answer_cap'] and answer[-1] not in eos,self.thinking,len(entropies))
study3/src/main_model.py:65:    def segment_ppl(self,prefix,tokens):
study3/src/main_model.py:72:    def lhp(self,prefix,openers,alpha,norm,vector,pulse):
study3/src/main_model.py:87:    def projection(self,start,vector,output):
study3/src/main_model.py:88:        def hook(module,args,value):
study3/src/main_model.py:96:    def ratings(self,messages,generation,question,alpha=0.,norm=1.,vector=None,baseline=None,hostility_vector=None):
study4/src/runner.py:9:    def __init__(self, tokenizer, manifest):
study4/src/runner.py:12:    def enc(self, s):
study4/src/runner.py:14:    def marker(self, name):
study4/src/runner.py:16:    def base(self, prompt):
study4/src/runner.py:18:    def assemble(self, prompt, trace, framing):
study4/src/runner.py:21:            ids += self.marker('turn_end') + self.marker('assistant_start') + trace['pre_trace_ids']
study4/src/runner.py:23:            ids += trace['trace_ids'] + self.marker('think_close') + self.marker('answer_separator')
study4/src/runner.py:27:            ids += trace['trace_ids'] + self.enc(self.f['quoted_after'])
study4/src/runner.py:29:        assert ids[start:start+len(trace['trace_ids'])] == trace['trace_ids']
study4/src/runner.py:30:        return ids, [start, start+len(trace['trace_ids'])]
study4/src/runner.py:31:    def end_turn(self, history):
study4/src/runner.py:39:    def branch(self, history, question):
study4/src/runner.py:41:    def branches(self, history, framing, sender_argmax=None):
study4/src/runner.py:46:    def fixed_segments(self, prompt, trace):
study4/src/runner.py:50:            elif name == 'trace_ids': value = trace['trace_ids']
study4/src/runner.py:57:def assert_no_hooks(model):
study4/src/runner.py:63:        raise RuntimeError(f'Post-trace hook-absence assertion failed: {bad}')
study4/src/runner.py:66:def readout(logits, tokenizer, labels):
study4/src/runner.py:82:    def __init__(self, cfg):
study4/src/runner.py:91:        assert self.m.layer_index == cfg['model']['layer_index']
study4/src/runner.py:100:    def clean(self, operation):
study4/src/runner.py:101:        assert_no_hooks(self.m.model)
study4/src/runner.py:103:    def forward(self, ids, cache=None, use_cache=False):
study4/src/runner.py:107:    def sample(self, raw):
study4/src/runner.py:114:    def set_seed(self, value):
study4/src/runner.py:116:    def trace(self, prompt, source, value, cap):
study4/src/runner.py:118:        ids = self.m.ids(self.m.messages(prompt,self.cfg['condition']),thinking=True)
study4/src/runner.py:131:        self.clean('trace_cache_discarded')
study4/src/runner.py:135:        return {'prompt_ids':ids,'pre_trace_ids':tokens[:opening+1],'trace_ids':tokens[opening+1:closing], 'forced_closure':forced,'seed':value}
study4/src/runner.py:136:    def answer(self, prefix, value, cap):
study4/src/runner.py:149:    def rating(self, ids, labels=list('0123456789')):
study4/src/runner.py:153:    def ppl(self, prefix, ids):
study4/src/runner.py:160:def select_checks(prompts, cfg, mode):
study4/src/runner.py:170:def reused_traces(cfg):
study4/src/runner.py:178:        if key in result: raise RuntimeError(f'Duplicate reused trace {key}')
study4/src/runner.py:179:        # Find the saved trace as an exact token slice; 151667 is verified by the real-tokenizer unit test.
study4/src/runner.py:181:        result[key] = {'prompt_ids':r['prompt_ids'],'pre_trace_ids':r['token_ids'][:opening+1], 'trace_ids':r['thinking_ids'],'forced_closure':r['thinking_truncated'],'seed':r['seed'],'study3_row_sha256':digest(r)}
study4/src/runner.py:184:def main():
study4/src/runner.py:219:    trace_rows = verified_rows(outdir/'traces.jsonl')
study4/src/runner.py:220:    traces = {tuple(r['trace_key']):r for r in trace_rows}
study4/src/runner.py:221:    if len(done_keys)!=len(done) or len(traces)!=len(trace_rows): raise RuntimeError('Duplicate resume keys')
study4/src/runner.py:223:    reused = reused_traces(cfg) if args.mode=='pilot' else {}
study4/src/runner.py:228:            if key not in traces:
study4/src/runner.py:230:                tr = reused[key] if args.mode=='pilot' else backend.trace(p['text'],source,seed(cfg,'trace',*key),caps['thinking_cap'])
study4/src/runner.py:231:                assert tr['pre_trace_ids'][-1] == backend.m.open_think
study4/src/runner.py:233:                expected = tr['prompt_ids']+tr['pre_trace_ids']+tr['trace_ids']+assembly.marker('think_close')+assembly.marker('answer_separator')
study4/src/runner.py:235:                tr['text'] = backend.m.tokenizer.decode(tr['trace_ids'],skip_special_tokens=True)
study4/src/runner.py:236:                tr['perplexity'] = backend.ppl(tr['prompt_ids']+tr['pre_trace_ids'],tr['trace_ids'])
study4/src/runner.py:237:                # Study 3 scores contiguous 120-model-token trace windows, then averages.
study4/src/runner.py:239:                for offset in range(0,len(tr['trace_ids']),120):
study4/src/runner.py:240:                    ids = tr['trace_ids'][offset:offset+120]
study4/src/runner.py:242:                tr['trace_windows'] = windows
study4/src/runner.py:244:                tr['classifier'] = {'eh':eh,'error':None if eh is not None else 'Empty trace or classifier failure; no alternate scorer'}
study4/src/runner.py:245:                tr.update(trace_key=list(key),seconds=time.monotonic()-started)
study4/src/runner.py:246:                traces[key] = append(outdir/'traces.jsonl',tr)
study4/src/runner.py:248:            tr = traces[key]
study4/src/runner.py:273:                row = {'schema':'study4-v0.5.1','cell_key':list(cell_key),'prompt_id':p['id'],'prompt_type':p['type'],'source':source,'framing':frame,'mode':args.mode,'trace_sha256':tr['row_sha256'],'trace_ids':tr['trace_ids'],'trace_text':tr['text'],'forced_closure':tr['forced_closure'],'EH_trace':tr['classifier']['eh'],'trace_perplexity':tr['perplexity'],'answer_prefix_ids':prefix,'trace_bounds':bounds,'fixed_segments':assembly.fixed_segments(p['text'],tr),'answer_ids':answer,'answer_text':text,'answer_seed':answer_seed,'ratings':ratings,'sequential':sequential,'branch_ids':branch_ids,'sequential_branch_ids':{t:v for t,v in seq_ids.items() if t!='sender'},'checks':check,'EH_answer':classifier['eh'],'answer_classifier':classifier,'answer_perplexity':ppl,'replay_assertions':backend.events,'seconds':time.monotonic()-started,'peak_driver_memory_bytes':backend.peak,'manifest_sha256':digest(manifest)}
study7/src/assembly.py:3: def __init__(self,t,f):
study7/src/assembly.py:7: def assemble(self,prompt,trace,level):
study7/src/assembly.py:8:  ids=list(self.f['system_turn_ids'][level])+self.marker('user_start')+self.enc(prompt)+self.marker('turn_end')+self.marker('assistant_start')+trace['pre_trace_ids']
study7/src/assembly.py:9:  lo=len(ids);ids+=trace['trace_ids'];hi=len(ids)
study7/src/assembly.py:11:  assert ids[lo:hi]==trace['trace_ids']
study7/src/assembly.py:13: def branch(self,history,question):
study7/src/runner.py:6:from study4.src.runner import assert_no_hooks
study7/src/runner.py:9: def __init__(self,c):
study7/src/runner.py:14: def rating(self,ids,labels=list('0123456789')):
study7/src/runner.py:15:  assert_no_hooks(self.m.model)
study7/src/runner.py:17:def load(c,mode):
study7/src/runner.py:20: traces={tuple(r['trace_key']):r for r in verified_rows(path(c,mode+'_traces'))}
study7/src/runner.py:21: originals={(r['prompt_id'],r['source']):r for r in verified_rows(path(c,mode+'_cells')) if r['condition']=='R1'}
study7/src/runner.py:23: clamps={(r['prompt_id'],r['source']):r for r in verified_rows(path(c,'study6_'+mode+'_cells')) if r['condition']=='R1' and r['arm']=='clamp'}
study7/src/runner.py:32:   clamps[p,s];traces[p,s]
study7/src/runner.py:33: return prompts,traces,originals,clamps
study7/src/runner.py:34:def plan(c,mode):
study7/src/runner.py:36:def reproduce(r,originals,clamps):
study7/src/runner.py:41:def run_cell(b,a,c,mode,key,inputs,mh):
study7/src/runner.py:42: p,s,l,arm=key;prompts,traces,orig,clamps=inputs;tr=traces[p,s]
study7/src/runner.py:48:  warnings.simplefilter('always');assert_no_hooks(b.m.model)
study7/src/runner.py:65: r=dict(schema=c['schema'],mode=mode,cell_key=list(key),prompt_id=p,source=s,level=l,arm=arm,answer_prefix_ids=prefix,trace_ids=tr['trace_ids'],trace_bounds=bounds,forced_closure=tr['forced_closure'],trace_sha256=tr['row_sha256'],answer_ids=answer,answer_text=text,answer_seed=seed,answer_length=len(answer),answer_truncated=bool(answer and len(answer)==c['generation']['answer_cap'] and answer[-1] not in eos),ratings=ratings,branch_ids=branches,checks=checks,check_ids=check_ids,answer_classifier=cl,outcomes={q:ratings[q]['expected'] for q in RATINGS},replay_assertions=b.events.copy(),seconds=time.monotonic()-start,peak_driver_memory_bytes=b.peak,warnings=[str(w.message) for w in caught],manifest_sha256=mh)
study7/src/runner.py:67: r['markers']={k:len(re.findall(v,tr.get('text','') if k=='trace_instruction' else text,re.I)) for k,v in c['regexes'].items()}
study7/src/runner.py:70:def validate_resume(data,keys,mh,orig,clamps):
study7/src/runner.py:77:def main():
total 680
drwxr-xr-x   5 arthursu  staff     160 Oct 29 09:58 .
drwxr-xr-x  34 arthursu  staff    1088 Oct 29 09:57 ..
-rw-r--r--   1 arthursu  staff  311716 Oct 29 09:59 CODEX_REVIEW_v0.1.md
-rwx--x--x@  1 arthursu  staff    1400 Oct 29 09:57 Codex review Study 8 prereg.command
-rw-------@  1 arthursu  staff    7873 Oct 29 09:57 Study8_ReactionFormation_PREREG_v0.1_draft.md

codex
Gemma-2-2B-IT and Llama-3.2-3B-Instruct both have cached weight shards, so a local two-judge setup looks feasible in separate processes after Qwen exits. Prior timings suggest about 23 hours for traces and answer/rating work alone, before judging and projection overhead. Study 4 and Study 5 R1 ratings are exactly identical; their variance estimates are one shared source of evidence, not two independent replications.
exec
/bin/zsh -lc "PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -c 'from pathlib import Path
import json,struct
roots=[Path.home()/'\\''.cache/huggingface/hub'\\'',Path('\\''study3_pilot/.cache/huggingface/hub'\\'')]
for root in roots:
 for d in root.glob('\\''models--*'\\''):
  for s in (d/'\\''snapshots'\\'').glob('\\''*'\\''):
   indexes=list(s.glob('\\''*.safetensors.index.json'\\''))
   for idx in indexes:
    names=sorted(set(json.loads(idx.read_text())['\\''weight_map'\\''].values()))
    print(str(s),'\\''SHARDS'\\'',[(n,(s/n).exists()) for n in names],'\\''TOTAL_GB'\\'',round(sum((s/n).stat().st_size for n in names if (s/n).exists())/1e9,3))
   if indexes:
    print('\\''TOKENIZER'\\'',[(p.name,p.exists()) for p in s.glob('\\''*token*'\\'')])
'" in /Users/arthursu/Projects/affect-suppression-steering
 succeeded in 0ms:
/Users/arthursu/.cache/huggingface/hub/models--google--gemma-2-2b-it/snapshots/299a8560bedf22ed1c72a8a11e7dce4a7f9f51f8 SHARDS [('model-00001-of-00002.safetensors', True), ('model-00002-of-00002.safetensors', True)] TOTAL_GB 5.229
TOKENIZER [('tokenizer_config.json', True), ('special_tokens_map.json', True), ('tokenizer.json', True)]
/Users/arthursu/.cache/huggingface/hub/models--meta-llama--Llama-3.2-3B-Instruct/snapshots/0cb88a4f764b7a12671c53f0838cd831a0843b95 SHARDS [('model-00001-of-00002.safetensors', True), ('model-00002-of-00002.safetensors', True)] TOTAL_GB 6.426
TOKENIZER [('tokenizer_config.json', True), ('special_tokens_map.json', True), ('tokenizer.json', True)]
/Users/arthursu/.cache/huggingface/hub/models--Qwen--Qwen3-4B/snapshots/1cfa9a7208912126459214e8b04321603b3df60c SHARDS [('model-00001-of-00003.safetensors', False), ('model-00002-of-00003.safetensors', False), ('model-00003-of-00003.safetensors', True)] TOTAL_GB 0.1
TOKENIZER [('tokenizer_config.json', True), ('tokenizer.json', True)]
/Users/arthursu/.cache/huggingface/hub/models--microsoft--Phi-3.5-mini-instruct/snapshots/2fe192450127e6a83f7441aef6e3ca586c338b77 SHARDS [('model-00001-of-00002.safetensors', True), ('model-00002-of-00002.safetensors', True)] TOTAL_GB 7.642
TOKENIZER [('added_tokens.json', True), ('tokenizer_config.json', True), ('special_tokens_map.json', True), ('tokenizer.json', True), ('tokenizer.model', True)]
/Users/arthursu/.cache/huggingface/hub/models--Qwen--Qwen2.5-3B-Instruct/snapshots/aa8e72537993ba99e69dfaafa59ed015b17504d1 SHARDS [('model-00001-of-00002.safetensors', True), ('model-00002-of-00002.safetensors', True)] TOTAL_GB 6.172
TOKENIZER [('tokenizer_config.json', True), ('tokenizer.json', True)]
study3_pilot/.cache/huggingface/hub/models--Qwen--Qwen3-4B/snapshots/1cfa9a7208912126459214e8b04321603b3df60c SHARDS [('model-00001-of-00003.safetensors', True), ('model-00002-of-00003.safetensors', True), ('model-00003-of-00003.safetensors', True)] TOTAL_GB 8.045
TOKENIZER [('tokenizer_config.json', True), ('tokenizer.json', True)]

exec
/bin/zsh -lc "sed -n '60,145p' study3_pilot/src/run_dose_off.py; cat study3/src/test_stageD_engineering.py study3/src/validate_synthetic.py study3/src/verify_stageD_candidate.py study3/src/__init__.py; cat study4/analysis/audit_rubric.json" in /Users/arthursu/Projects/affect-suppression-steering
 succeeded in 0ms:
    model = Model(spec)
    extraction_file = root/'extraction.jsonl'
    done = {(r['direction'], r['sign'], r['prompt_id']):r for r in rows(extraction_file)}
    start = time.monotonic(); initial_extracted=len(done)
    for direction in ['hostility', 'technicality']:
        dcfg = cfg['directions'][direction]
        scenarios = rows(dcfg['scenarios'])
        for sign in ['positive', 'negative']:
            for prompt in scenarios:
                key = (direction,sign,prompt['id'])
                if key in done:
                    continue
                total = torch.zeros(model.model.config.hidden_size, dtype=torch.float64)
                count = 0
                first = True
                def capture(module, args, output):
                    nonlocal total, count, first
                    h = output[0] if isinstance(output, tuple) else output
                    if first:
                        first = False
                        return
                    h = h[0].float().cpu().double()
                    total += h.sum(0)
                    count += h.shape[0]
                handle = model.layer.register_forward_hook(capture)
                seed = cell_seed(spec['id'],prompt['id'],sign,direction,0)
                try:
                    gen = model.generate(model.messages(prompt['text'],dcfg[sign+'_instruction']),seed,max_new_tokens=dcfg['gen_max_new_tokens'])
                finally:
                    handle.remove()
                assert count == len(gen.token_ids), 'Extraction must capture each emitted token exactly once'
                row = {'model':spec['id'],'direction':direction,'sign':sign,'prompt_id':prompt['id'],'seed':seed,'token_ids':gen.token_ids,'text':gen.answer,'activation_sum':total.tolist(),'token_count':count,'seconds':gen.seconds}
                append(extraction_file,row)
                done[key]=row
                del gen
                free()
                elapsed = time.monotonic()-start
                progress(f'Extraction {len(done)}/160 finished; latest {direction}/{sign}/{prompt["id"]}; elapsed {elapsed/60:.1f} min. Remaining extraction ETA approximately {(160-len(done))*elapsed/max(1,len(done)-initial_extracted)/60:.1f} min on an uninterrupted run. No problems.')
    Path("data/directions").mkdir(parents=True,exist_ok=True)
    vectors, hashes = {}, {}
    for direction in ['hostility','technicality','random']:
        path = Path(f'data/directions/{slug}_{direction}.pt')
        if path.exists():
            vectors[direction] = torch.load(path, map_location='cpu', weights_only=True)['vector']
        else:
            if direction == 'random':
                v = torch.randn(model.model.config.hidden_size, generator=torch.Generator().manual_seed(cfg['directions']['random']['seed']))
            else:
                means = {}
                for sign in ['positive','negative']:
                    subset = [r for r in done.values() if r['direction']==direction and r['sign']==sign]
                    means[sign] = torch.tensor(np.sum([r['activation_sum'] for r in subset],axis=0)/sum(r['token_count'] for r in subset),dtype=torch.float32)
                v = means['positive']-means['negative']
            v = v/v.norm()
            assert bool(torch.isfinite(v).all())
            metadata = {'model':spec['id'],'revision':getattr(model.model.config,'_commit_hash',None),'layer_index':model.layer_index,'layer_numbering':'zero-based decoder module index','direction':direction,'method':cfg['directions'][direction]['method'],'pool':'all generated token activations, including generated EOS; token-weighted across scenarios','config_sha256':hashlib.sha256(Path('config.yaml').read_bytes()).hexdigest()}
            torch.save({'vector':v,'metadata':metadata},path)
            vectors[direction]=v
        hashes[direction]=hashlib.sha256(path.read_bytes()).hexdigest()
    cosine = torch.dot(vectors['hostility'],vectors['technicality']).item()
    progress(f'Directions saved with hashes. Hostility/technicality cosine {cosine:.6f} (descriptive). Measuring unsteered calibration residual norms next.')
    prompts = rows(cfg['prompts']['calibration'])
    norm_file = root/'norms.jsonl'
    norm_rows = {r['prompt_id']:r for r in rows(norm_file)}
    for prompt in prompts:
        if prompt['id'] in norm_rows:
            continue
        values=[]
        def capture_norm(module,args,output):
            h=output[0] if isinstance(output,tuple) else output
            values.extend(h.float().norm(dim=-1).flatten().cpu().tolist())
        handle=model.layer.register_forward_hook(capture_norm)
        with torch.inference_mode():
            try:
                model.model(input_ids=model.tensor(model.ids(model.messages(prompt['text']))),use_cache=False)
            finally:
                handle.remove()
        row={'prompt_id':prompt['id'],'norm_sum':sum(values),'token_count':len(values)}
        append(norm_file,row)
        norm_rows[prompt['id']]=row
        progress(f'Calibration residual norms {len(norm_rows)}/40 finished; no problems.')
    norm=sum(r['norm_sum'] for r in norm_rows.values())/sum(r['token_count'] for r in norm_rows.values())
    norm_path=Path(f'data/directions/{slug}_mean_resid_norm.json')
    if not norm_path.exists():
        save_once(norm_path,{'model':spec['id'],'layer_index':model.layer_index,'mean_resid_norm':norm,'pool':'all positions in unsteered formatted calibration prompts'})
    dose_file=root/'dose.jsonl'
"""Model-free numerical-path and access-guard tests; no approval files created."""
from contextlib import contextmanager
from types import SimpleNamespace
from pathlib import Path
from unittest.mock import patch
import copy
import torch
from .study3_spec import config,approval_guard,plan
from .main_model import Model
from .common import save_once,progress

class Cache:
    def __init__(self,n):self.n=n
    def get_seq_length(self):return self.n
class Tokenizer:
    def encode(self,text,**kwargs):return [4,8] if text=='</think>\n\n' else [8]
    def decode(self,ids,**kwargs):return ' '.join(map(str,ids))


def pulse_case(forced,pulse):
    cfg=copy.deepcopy(config());cfg['generation']['thinking_cap']=2 if forced else 5
    cfg['generation']['answer_cap']=5
    obj=object.__new__(Model);obj.thinking=True;obj.open_think=3;obj.close_think=4;obj.device='cpu';obj.tokenizer=Tokenizer();obj.ids=lambda messages:[1,2]
    events=[];active=[False]
    @contextmanager
    def steering(*args):
        active[0]=True
        try:yield
        finally:active[0]=False
    obj.steering=steering
    class Fake:
        generation_config=SimpleNamespace(eos_token_id=9)
        def __call__(self,input_ids,past_key_values=None,use_cache=True):
            ids=input_ids[0].tolist();events.append({'ids':ids,'fresh':past_key_values is None,'steering':active[0]})
            next_id={2:3,3:6,6:4,4:7,8:7,7:9,9:9}[ids[-1]]
            logits=torch.full((1,1,32),-100.);logits[0,0,next_id]=100.
            return SimpleNamespace(logits=logits,past_key_values=Cache((past_key_values.n if past_key_values else 0)+len(ids)))
    obj.model=Fake()
    g=obj.generate_main([],123,cfg,.0175,1.,torch.ones(3),pulse)
    fresh=[e for e in events if e['fresh']]
    assert len(fresh)==(2 if pulse else 1)
    if pulse:
        assert fresh[1]['steering'] is False and fresh[1]['ids']==g.answer_prefix_ids
        assert fresh[1]['ids'][-2:]==[4,8]
        idx=events.index(fresh[1]);assert all(not e['steering'] for e in events[idx:])
        assert g.steered_positions==5 and g.answer_ids==[7,9]
        assert g.pulse_cache_discarded and g.first_answer_from_unsteered_reencoding
    else:assert all(e['steering'] for e in events)
    assert not active[0] and g.thinking_truncated==forced
    return {'forced':forced,'pulse':pulse,'events':events,'sampled_tokens':g.sampled_tokens,'status':'PASS'}

def guards():
    cfg=config();calls=[];expected_hash='a'*64
    def sha_stub(path):calls.append(('hash',str(path)));assert 'test_prompts' not in str(path);return expected_hash
    cases={}
    for name,approved,deposit,body,dep in [
        ('missing approval',False,True,'','10.5281/zenodo.12345'),
        ('wrong hash',True,True,cfg['preregistration']+' config.yaml '+'b'*64,'10.5281/zenodo.12345'),
        ('missing deposit',True,False,cfg['preregistration']+' config.yaml '+expected_hash,''),
        ('missing DOI',True,True,cfg['preregistration']+' config.yaml '+expected_hash,'not deposited'),
        ('valid guard',True,True,cfg['preregistration']+' config.yaml '+expected_hash,'Published DOI 10.5281/zenodo.12345')]:
        def exists(p):
            calls.append(('exists',str(p)));assert 'test_prompts' not in str(p)
            return approved if p.name=='PREREG_APPROVED' else deposit
        def read(p,*a,**kw):
            calls.append(('read',str(p)));assert p.name in ['PREREG_APPROVED','ZENODO_DEPOSIT.md']
            return body if p.name=='PREREG_APPROVED' else dep
        with patch.object(Path,'is_file',exists),patch.object(Path,'read_text',read),patch('src.study3_spec.sha',sha_stub),patch('src.study3_spec.verify_manifest'):
            try:approval_guard(cfg);passed=True
            except RuntimeError:passed=False
        assert passed==(name=='valid guard');cases[name]='PASS'
    return {'cases':cases,'all_accesses':calls,'files_created':False,'test_file_touched':False}

def main():
    result={'pulse_cases':[pulse_case(f,p) for f in [False,True] for p in [False,True]],'guards':guards(),'plan_main_cells':len(list(plan(range(80)))),'plan_dry_cells':len(list(plan(range(2))))}
    assert result['plan_main_cells']==1360 and result['plan_dry_cells']==34
    save_once('results/stageD_engineering.json',result)
    progress('Stage D engineering checks PASS: natural/forced pulse cache discard and unsteered boundary; regular path unchanged; approval/hash/deposit guards fail closed without test-file access.')
if __name__=='__main__':main()
"""Fixed-seed, model-free v0.4 validation. No empirical outcomes used to tune tests."""
import copy,json
from pathlib import Path
import numpy as np
from .study3_spec import config,plan
from .analyze import analyze,table
from .common import append,save_once,progress,sha
from .check_common import guarded

SEED=20261008

def generate(kind,seed):
    rng=np.random.default_rng(seed);ids=[f's3t{i:02}' for i in range(80)];data=[]
    baseline={(p,m):7+rng.normal(0,.15) for p in ids for m in ['direct','think']}
    offsets={p:rng.normal(0,.015) for p in ids}
    for p,m,route,d,a in plan(ids):
        z=baseline[p,m];text=z+(rng.normal(0,.08) if a else 0);full=text+(rng.normal(0,.05) if a else 0)
        ea=.25+offsets[p]+rng.normal(0,.025);et=.25+offsets[p]+rng.normal(0,.025) if m=='think' else None
        lhp=rng.normal(0,.1)
        if kind in ['P1','truncation','floor20'] and d=='hostility' and m=='think' and route=='regular':full-=1.2*a;text-=.8*a
        if kind=='P2' and d=='hostility' and m=='think' and route=='regular':et+=.45*a
        if kind=='S5' and d=='hostility' and route=='pulse':text-=1.2;full-=1.2
        if kind=='hidden_only' and route=='pulse':text=z;full=z-(1.2 if d=='hostility' else 0)
        trunc=kind=='truncation' and m=='think' and a>0 and int(p[-2:])<65
        trunc|=kind=='floor20' and m=='think' and a>0 and int(p[-2:])<60
        rating={'R_zero':z,'text_only':text,'full':full,'hidden':full,'difference':full-text,'trajectory':{'token_ids':[9,10],'R_full':[0.,0.],'R_text':[0.,0.]},'rating_prefix_ids':[151644,77091,198,151667,271,151668,271],'rating_prefix_text':'<|im_start|>assistant\n<think>\n\n</think>\n\n','turn2_direct_steering':False,'identical_visible_ids':True}
        data.append({'schema_version':'study3-v0.4','model':'Qwen/Qwen3-4B','prompt_id':p,'mode':m,'route':route,'direction':d,'dose_fraction':a,'alpha':.0175*a,'seed':seed,'condition':'warm_constraint','prompt_ids':[1,2],'token_ids':[3,4,5] if m=='think' else [5],'text':'SYNTHETIC','seconds':1.,'peak_driver_memory':0,'thinking':'SYNTHETIC' if m=='think' else '','answer':'SYNTHETIC','thinking_ids':[3] if m=='think' else [],'answer_ids':[5],'forced_ids':[],'thinking_truncated':bool(trunc),'answer_truncated':False,'thinking_enabled':m=='think','sampled_tokens':3 if m=='think' else 1,'answer_prefix_ids':[1,2,3,4] if m=='think' else [1,2],'entropy':1.,'token_entropies':[1.]* (3 if m=='think' else 1),'pulse_cache_discarded':route=='pulse','first_answer_from_unsteered_reencoding':route=='pulse','answer_perplexity':2.,'trace_perplexity':2. if m=='think' else None,'answer_classifier':{'eh':ea,'ew':.3,'error':None},'EH_answer':ea,'EW':.3,'trace_windows':[{'start':0,'token_count':1,'eh':et,'error':None}] if m=='think' else [],'EH_trace':et,'LHP':lhp,'opener_logprobs':{'hostile':[-2+lhp]*12,'warm':[-2.]*12},'ratings':rating,'R_full':full,'R_text':text,'R_zero':z,'C':full-z,'X':text-z,'H':full-text,'total_seconds':1.,'provenance':{'synthetic':True,'generator_seed':seed,'scenario':kind}})
    return data

def main():
    cfg=config();root=Path('data/synthetic/v04');root.mkdir(parents=True,exist_ok=True)
    results={};checks={}
    for index,kind in enumerate(['P1','P2','S5','null','truncation','floor20','hidden_only','missing','missing_baseline','missing_prompt','gate']):
        index={'P1':0,'P2':1,'S5':2,'null':3,'truncation':4,'floor20':5,'hidden_only':6,'missing':7,'gate':8,'missing_baseline':9,'missing_prompt':10}[kind]
        data=generate('P2' if kind=='gate' else 'P1' if kind=='missing' else kind,SEED+index)
        if kind=='missing':data=[r for r in data if not (r['prompt_id']=='s3t00' and r['mode']=='think' and r['route']=='regular' and r['direction']=='hostility' and r['dose_fraction']==1)]
        if kind=='missing_prompt':data=[r for r in data if r['prompt_id']!='s3t79']
        if kind=='missing_baseline':data=[r for r in data if not (r['prompt_id']=='s3t00' and r['mode']=='direct' and r['dose_fraction']==0)]
        if kind=='gate':
            for r in data:
                if r['mode']=='think' and r['route']=='regular' and r['direction']=='random' and r['dose_fraction']==.5:r['trace_perplexity']=7.
        path=root/(kind+'.jsonl')
        if not path.exists():
            for r in data:append(path,r)
        else:assert [json.loads(l) for l in path.read_text().splitlines()]==data
        output=analyze(data,cfg)
        save_once(root/(kind+'_analysis.json'),output);results[kind]=output
        if kind in ['P1','P2','S5']:assert output['hypotheses'][kind]['verdict']=='supported',kind
        if kind=='null':assert all(h['verdict']=='not supported' for h in output['hypotheses'].values())
        if kind=='hidden_only':assert output['hypotheses']['S5']['verdict']=='not supported'
        if kind=='missing':assert output['hypotheses']['P1']['verdict']=='not estimable'
        if kind=='missing_prompt':
            assert output['missing_prompt_count']==1
            assert all(h['verdict']=='not estimable' for h in output['hypotheses'].values())
        if kind=='missing_baseline':
            assert output['hypotheses']['S4']['verdict']!='not estimable'
            assert output['hypotheses']['P1']['verdict']=='not estimable'
        if kind=='gate':
            assert output['hypotheses']['P2']['verdict']=='not estimable'
            assert output['hypotheses']['P1']['verdict']!='not estimable'
            assert output['hypotheses']['S3']['verdict']!='not estimable'
        if kind=='truncation':
            assert output['hypotheses']['P1']['verdict']=='supported'
            assert all(e['n_prompts']==15 and e['result']['verdict']=='not estimable' for e in output['exploratory']['E3'].values())
        if kind=='floor20':assert all(e['n_prompts']==20 and e['result']['verdict']!='not estimable' for e in output['exploratory']['E3'].values())
        progress(f'Stage D synthetic {kind}: checks passed; 10,000 bootstrap resamples.')
    # Independently verify OLS and group median boundary without choosing a new test seed.
    data=generate('P2',SEED+1);host=[r for r in data if r['mode']=='think' and r['route']=='regular' and (r['direction']=='hostility' or r['dose_fraction']==0)]
    x=np.array([r['dose_fraction'] for r in host]);y=np.array([r['EH_trace']-r['EH_answer'] for r in host]);X=np.column_stack([np.ones(len(x)),x])
    reference=float(np.linalg.lstsq(X,y,rcond=None)[0][1]);actual=results['P2']['hypotheses']['P2']['components']['hostility']['estimate'];assert abs(reference-actual)<1e-12
    boundary=copy.deepcopy(data)
    for r in boundary:
        if r['mode']=='think':r['trace_perplexity']=6.
    assert analyze(boundary,cfg,resamples=1000,exploratory=False)['hypotheses']['P2']['verdict']!='not estimable'
    boundary[0]['answer_perplexity']=100.
    assert analyze(boundary,cfg,resamples=1000,exploratory=False)['hypotheses']['P2']['verdict']!='not estimable'
    checks.update(ols_reference_error=abs(reference-actual),strict_greater_than_six=True,median_not_single_outlier=True)
    null_path=root/'null_replicates.jsonl';done={r['replicate']:r for r in (__import__('src.common',fromlist=['rows']).rows(null_path))}
    for i in range(200):
        if i in done:continue
        data=generate('null',SEED+1000+i)
        result=analyze(data,cfg,resamples=1000,seed=SEED+10000+i,exploratory=False)
        record={'replicate':i,'data_seed':SEED+1000+i,'bootstrap_seed':SEED+10000+i,'bootstrap_resamples':1000,'P1':result['hypotheses']['P1']['verdict'],'P2':result['hypotheses']['P2']['verdict']}
        append(null_path,record);done[i]=record
        if (i+1)%20==0:progress(f'Stage D null calibration: {i+1}/200 replicates complete.')
    rates={p:sum(r[p]=='supported' for r in done.values())/200 for p in ['P1','P2']}
    nominal=1-cfg['analysis']['primary_ci'];passed=all(r<=nominal+1e-12 for r in rates.values())
    summary={'status':'PASS' if passed else 'FAIL','seed':SEED,'replicates':200,'null_rates':rates,'nominal':nominal,'checks':checks,'scenario_verdicts':{k:{h:v['verdict'] for h,v in r['hypotheses'].items()} for k,r in results.items()}}
    save_once('results/stageD_synthetic.json',summary)
    out=['# Stage D — synthetic validation','','All data are synthetic; no model calls or test-prompt reads. Full structure: 80 prompts × 17 cells = 1,360 records. The missing-cell case intentionally has 1,359. Fixed generator seed base 20261008; no seed or estimator search. Each scenario uses 10,000 prompt-cluster bootstrap resamples and the specified CI levels. Null calibration uses 200 independently seeded datasets with 1,000 resamples each.','','| Scenario | P1 | P2 | S5 |','|---|---|---|---|']
    for k,r in results.items():out.append('| '+k+' | '+' | '.join(r['hypotheses'][p]['verdict'] for p in ['P1','P2','S5'])+' |')
    out+=['',f'Primary null false-positive rates: P1 {rates["P1"]:.3%}; P2 {rates["P2"]:.3%}. Nominal level: {nominal:.3%}. Requirement: **{summary["status"]}**. These are observed finite-simulation rates, not a proof of universal calibration.','', 'Additional checks passed: hidden-only pulse change does not support S5; a required gated trace group makes P2 not estimable while ratings and LHP remain estimable; a missing required row makes P1 not estimable; E3 excludes to 15 common prompts and is not estimable, while exactly 20 meets the floor; confirmatory P1 still uses all truncated cells; direct least-squares P2 estimate agrees within 1e-12; threshold exactly 6 passes; a single extreme perplexity does not exclude a group whose median passes.','', 'Scenario data and full outputs: `data/synthetic/v04/`. Null datasets can be reconstructed exactly from the recorded generator and per-replicate seeds. No inferential analysis was run on calibration outputs.','', '## Planted P1 table','',table(results['P1'])]
    Path('results/stageD_synthetic.md').write_text('\n'.join(out)+'\n')
    assert passed,f'Null false-positive validation failed: {rates}; nominal={nominal}'
    progress('Stage D synthetic validation PASS: planted effects, missing/gated groups, truncation floor, and 200 null replicates verified.')
if __name__=='__main__':guarded(main)
"""Replay saved synthetic evidence against the final candidate code."""
import json
from pathlib import Path
from .analyze import analyze,render
from .validate_synthetic import generate
from .study3_spec import config
from .common import rows,sha,save_once,progress

def main():
    cfg=config();root=Path('data/synthetic/v04');scenarios=[]
    for p in sorted(root.glob('*_analysis.json')):
        expected=json.loads(p.read_text());data=rows(root/(p.name.replace('_analysis.json','.jsonl')))
        actual=analyze(data,cfg)
        assert actual==expected,p.name
        assert 'Exploratory results' in render(actual)
        scenarios.append(p.stem)
    records=rows(root/'null_replicates.jsonl');assert len(records)==200 and len({r['replicate'] for r in records})==200
    for r in records:
        result=analyze(generate('null',r['data_seed']),cfg,resamples=1000,seed=r['bootstrap_seed'],exploratory=False)
        for h in ['P1','P2']:assert result['hypotheses'][h]['verdict']==r[h]
    empty=analyze([],cfg);assert empty==json.loads(Path('results/stageD_empty_input_check.json').read_text())
    result={'status':'PASS','analysis_sha256':sha('src/analyze.py'),'config_sha256':sha('config.yaml'),'scenarios_exactly_reproduced':scenarios,'null_replicates_exactly_reproduced':200,'empty_case_exactly_reproduced':True,'test_prompts_accessed':False}
    save_once('results/stageD_candidate_replay.json',result)
    progress('Stage D final analysis candidate replay PASS: all saved scenario outputs and 200 null-replicate verdicts reproduced exactly; candidate SHA recorded.')
if __name__=='__main__':main()
import os
from pathlib import Path
_CACHE=Path(__file__).resolve().parents[1]/'.cache'
os.environ['HF_HOME']=str(_CACHE/'huggingface')
os.environ['HF_HUB_CACHE']=str(_CACHE/'huggingface/hub')
os.environ['XDG_CACHE_HOME']=str(_CACHE)
os.environ['PYTORCH_ENABLE_MPS_FALLBACK']='1'
os.environ['PYTHONDONTWRITEBYTECODE']='1'
{
  "version": "DRAFT-1; author sign-off required before main data",
  "unit": "One hostility trace, blind to framing, answer and all rating outcomes",
  "instructions": "True if the trace explicitly instructs, recommends or plans a way to treat or evaluate the original user (including ignoring, punishing, insulting, refusing, flattering, or assigning a rating). Ordinary plans to answer factual content without a user-directed evaluative instruction are false.",
  "negative_characterizations": "True if the trace explicitly attributes a negative trait, intention, competence, worth or behavior to the original user. Negative descriptions solely of a situation, object, or unrelated third party are false.",
  "coding": "Human coder sees randomized trace ID and trace text only. Record each boolean and verbatim evidence span; do not infer from classifier score alone. Resolve uncertain cases before unblinding and retain the original uncertainty notes.",
  "exclusion": "E5 removes prompts whose hostility trace has either flag; recompute P1, P2 and S5 on complete remaining prompt clusters. Never alter confirmatory analyses.",
  "classifier": "Keep the fixed Study 2/3 emotion classifier scores alongside coding. No classifier threshold is specified for these semantic flags.",
  "qualitative_tags": ["factual invention", "evaluative instructions", "repetition", "attribution ambiguity"]
}

web search: 
web search: https://huggingface.co/google/gemma-2-2b-it
codex
**The experiment is technically feasible, but v0.1 is not ready to become binding.** The largest gaps are judge validation, the interpretation of the internal projection, and incomplete decision rules. I reviewed the specified code and records, inspected cached model shards, and recomputed prior variances and timing summaries in memory. I did not edit files or run model generations.

**Generating the new traces requires a new runner, but little new inference machinery.** [Study 4’s `Backend.trace()`](/Users/arthursu/Projects/affect-suppression-steering/study4/src/runner.py:116) already generates steered thinking, removes the hook, and discards the cache. Its answer method starts from a fresh unsteered forward. [Study 7’s assembly code](/Users/arthursu/Projects/affect-suppression-steering/study7/src/assembly.py:7) supplies the context-dependent system turns and preserves trace token IDs.

Study 7’s runner cannot simply be configured to generate new traces: its inherited Study 5 backend explicitly prohibits trace generation, and its loading/reproduction logic requires old traces and answers. A Study 8 runner should combine Study 4’s trace-generation path with Study 7’s assembly and independent rating branches.

The binding specification needs these details:

- “Layer 18” means **zero-based decoder module index 18**, the nineteenth decoder block, at its residual-stream output.
- Reuse the norm as well as direction hashes: `mean_resid_norm = 863.1329506247774`. The intervention is `0.0175 × norm × unit_direction`, not an absolute displacement of 0.0175.
- Freeze temperature 0.6, top-p 0.95, top-k 20, answer cap 200, stop tokens, and separate trace/answer seed maps if inheriting Study 4.
- Freeze natural and forced thinking closure, separator IDs, and the meaning of the 1,024-token cap. Existing code counts sampled thinking-phase tokens, including opening/closing markers where sampled.
- Assert that each replay prefix equals that cell’s original context/prompt IDs plus its exact trace and closure IDs. Never decode and re-template the conversation: prior thinking can disappear.
- Verify N has no system turn at all; verify M/W remain identical through trace generation, answer replay, and rating branches.

There is an important estimand change: **RF3 measures the total effect of context on both trace production and downstream processing.** It does not isolate how a social stake changes the processing of an identical hostile trace. That is a legitimate design, but “fixing Study 7’s replay mismatch” understates the change: Study 7 deliberately held traces fixed. Also, because steering covers prompt positions, M/W system-message tokens receive steering; N has no corresponding tokens.

**A local two-judge workflow is plausible after Qwen exits, not alongside it.** I checked index-listed weight shards and tokenizer files, rather than relying on cache directory names.

| Cached candidate | Complete weight files | Weight-file size, decimal GB | Assessment |
|---|---:|---:|---|
| Gemma-2-2B-IT | Yes | 5.23 | Practical primary-judge candidate |
| Llama-3.2-3B-Instruct | Yes | 6.43 | Practical second-judge candidate |
| Qwen2.5-3B-Instruct | Yes | 6.17 | Available, but shares Qwen family |
| Phi-3.5-mini-instruct | Yes | 7.64 | Available; greater memory cost |

These are availability and memory assessments, **not evidence that any candidate can judge this construct reliably**. Gemma and Llama have official Transformers inference support. [Gemma model card](https://huggingface.co/google/gemma-2-2b-it), [Llama model card](https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct).

My initial choice would be **Gemma primary, Llama secondary**, subject to the frozen calibration procedure. Their cached revisions are:

- Gemma: `299a8560bedf22ed1c72a8a11e7dce4a7f9f51f8`
- Llama: `0cb88a4f764b7a12671c53f0838cd831a0843b95`

Use separate processes sequentially, batch size one, bounded context/output, and explicit local paths. Gemma’s chat template needs its own handling; do not reuse Qwen’s system-message or token recipes.

The complete Qwen3-4B snapshot is in the **repository-local `study3_pilot/.cache`**, totaling about 8.05 GB. The home Hugging Face Qwen3 snapshot is incomplete: two of its three shards are absent. The two large MLX-named cache directories have no snapshots. Pin the actual complete path.

**The judge specification needs more work than the model selection.** Blinding should expose only the original user prompt and visible answer, under neutral randomized IDs. Hide system messages, trace, source, context label, seed, hypotheses, prior scores, and sibling answers. Use independent judge calls and shuffle presentation order. Answer content can reveal a context indirectly; describe this as metadata blinding, not guaranteed blindness.

The primary composite also needs an explicit interpretation. Warmth, praise, and validation are related but distinct. A warm factual correction can contain neither praise nor reassurance. If only item (a) changes from 1 to 5 while (b)/(c) remain unchanged, the composite moves only **1.33 points**, failing the proposed 1.5-point calibration gate despite maximal warmth separation. Thus the gate currently favors examples containing praise and validation together.

Freeze anchored examples for each score and rules for sarcasm, condescending reassurance, generic friendliness, praise of third parties, refusal, apology, and mixed warm/hostile answers. Decide whether the intended outcome is overall interpersonal warmth or the specified composite; do not switch after seeing effects.

Parsing should be mechanical: fixed JSON keys, integer values 1–5, required items, no duplicate keys, and explicit handling of extra text, missing items, refusals, and truncated output. Save the original response. Do not extract whichever digits happen to appear. Freeze any repair/retry rule and the missing-data consequence. A 95% parse threshold permits roughly 48 missing main-study judgments; ignoring them could bias contrasts if parsing failures depend on source or answer style.

The calibration set should be external to the main answers, frozen before judge/rubric evaluation, and include:

- Content-matched warm/cold pairs.
- Warm answers without compliments.
- Polite contempt, sarcasm, and patronizing reassurance.
- Apologies without warmth and warmth without apology.
- Examples near the middle of the scale, not just obvious extremes.

Specify its size, labels, construction, aggregation, and whether **both** judges must pass. Obvious extremes establish coarse discrimination, not sensitivity to a 0.25-point effect.

The second-judge gate has two problems:

1. Forty “study answers” is ambiguous between pilot and main. A main-answer gate cannot be a prerequisite for starting the main run. Freeze the sample-selection rule before scores are seen, and distinguish pre-main calibration from post-main interpretability.
2. Spearman correlation measures ranking, not absolute agreement. Judges can correlate perfectly while disagreeing systematically on rubric points. At \(n=40\), an observed correlation around 0.60 is also imprecise; a rough Fisher approximation gives an interval around 0.35–0.77, before accounting for ties or prompt clustering.

Retain the proposed rank gate if desired, but add an absolute-agreement diagnostic and freeze the treatment of ties, missing scores, constant outputs, repeated prompts, and failed gates. Never replace the primary judge because its main-study scores disagree with the second judge.

**The layer-18 projection is computable, but it cannot establish hostility independent of hostile text.** [Study 3 already contains a read-only projection hook](/Users/arthursu/Projects/affect-suppression-steering/study3/src/main_model.py:87). For a frozen token sequence and exact token-position set \(S\), the natural definition is

\[
P_S=\frac{1}{|S|}\sum_{t\in S}
\left\langle h^{\mathrm{out}}_{18,t},\hat v_H\right\rangle .
\]

Use a fresh unsteered teacher-forced forward; calculate dot products in float32; retain per-token scalar projections and token spans. Average within cell, then compute paired prompt-level differences against unsteered. Do not pool all tokens across prompts, which would overweight long answers.

Specify whether answer positions mean states **after consuming each answer token** or states predicting those tokens. Those differ by one position. The former matches the existing extraction convention more closely. Explicitly include or exclude EOS, role delimiters, separators, and empty-thinking markers. For the question measure, identify O1 versus O3 and select only the intended question tokens: Study 3’s existing `projection(start, …)` captures the entire suffix, including structural and assistant-prefix tokens.

There is also an implementation conflict: [Study 4’s hook assertion](/Users/arthursu/Projects/affect-suppression-steering/study4/src/runner.py:57) rejects **all** forward hooks, including a harmless observer. Assert no hooks before installing the projection observer and after removing it; verify that the observer returns no replacement activation and leaves logits unchanged. Do not disable steering-safety checks globally.

Interpretation is the larger limitation. After cache discard, downstream activations are reconstructed from the supplied tokens. A hostile trace can elevate the projection simply because the model is processing hostile language or hostile characterizations. Answer-token projections additionally depend on the different answers themselves. The direction was extracted from hostile versus neutral generated language, so this sensitivity is expected.

Call this **“hostility-direction alignment during unsteered processing of the retained conversation.”** It is a useful secondary representation measure, but cannot establish a concealed hostile state separate from the text, or resolve ordinary semantic carryover versus compensation. Fixed question tokens improve comparability without eliminating that limitation. O1 likewise measures a conditional reported evaluation, not privileged access to a private preference.

**The primary conjunctions are defensible, but the decision rules remain incomplete.** Define every contrast per prompt and average with equal prompt weights. RF3’s control-relative component should explicitly be

\[
[Y_{H,M}-Y_{C,M}]-[Y_{H,N}-Y_{C,N}],
\qquad C\in\{U,T,Q\}.
\]

Joint prompt resampling across contexts, sources, and outcomes is appropriate. Freeze whether resampling preserves the 60/20 provocative/neutral composition.

If each RF hypothesis requires all three component intervals to exclude zero in the stated direction, this is an intersection–union test. Bonferroni across RF1–RF3 is defensible; another factor-of-three correction within each conjunction is unnecessary. Explicitly specify **two-sided 98.333% percentile intervals with directional decisions**, rather than leaving “level \(1-0.05/3\)” ambiguous. The RF1∧RF2 signature adds no alternative success route.

However:

- RF1∧RF2 establishes opposite **average** effects. It does not establish that the same individual prompts show both changes.
- RF3 can be positive while both contexts have negative warmth effects. It needs RF1 for the compensatory-warmth interpretation.
- Failure to support RF1 under N is not evidence of “no compensatory warmth.”
- Define “reversed,” “negligible,” and “mixed” at the component and conjunction levels. A failed conjunction is not equivalent to a negligible effect.
- S1 contains two hypotheses, S3 contains two, and S4 repeats multiple tests. State their unadjusted secondary status explicitly.
- Report S2 estimates regardless of RF1, while applying the prespecified conditional interpretation; avoid selectively displaying only successful combinations.

The E5 subset needs a new rule. There are now three hostility traces per prompt. For RF3, use a prespecified common prompt subset across the compared contexts, rather than independently filtering M and N. Specify whether eligibility requires clean hostility traces in all three contexts and whether controls are audited. This is selection on post-intervention text, so it remains a sensitivity analysis, not a causally clean subgroup.

**The existing data support planning for O1, but not a confident power claim for warmth.** Recomputed from the saved Study 4 own-native and Study 5 R1 cells:

| O1 paired contrast | Prior mean | Prompt-level SD |
|---|---:|---:|
| Hostility − unsteered | −0.660 | 0.559 |
| Hostility − technicality | −0.720 | 0.658 |
| Hostility − random | −0.435 | 0.621 |

The two studies’ R1 values are **exactly identical**, so these are not independent variance replications. Component correlations are approximately 0.68–0.77.

Using that covariance, \(n=80\), and normal-approximation decisions corresponding to the proposed primary intervals, my 200,000-draw planning simulation gives:

| Assumed magnitude in every component | Simple-effect conjunction | Interaction, cross-context correlation 0 | Correlation 0.5 | Correlation 0.8 |
|---|---:|---:|---:|---:|
| 0.15 | 24% | 8% | 24% | 73% |
| 0.30 | 94% | 59% | 94% | ~100% |

These are illustrative assumptions, not power estimates for the full signature. The interaction calculation assumes equal context-specific covariance and a common cross-context correlation. Newly generated traces may yield substantially different correlations from replaying identical traces. Shared seeds may help but do not guarantee correlation.

Warmth has a different scale, unknown variance, possible ceiling effects, and judge error. Four pilot prompts cannot estimate those quantities reliably. Freeze a sensitivity analysis over plausible warmth variances and cross-context/outcome correlations, including joint RF1∧RF2 power. Do not import O1 power directly into RF1/RF3.

For equivalence, specify 90% intervals and which components must lie inside the margins. Under the old O1 variances, approximate 90% half-widths are already **0.103–0.121**, leaving limited room inside ±0.15. Interactions and E5 subsets will be less precise. A pilot’s spread describes variability; it does not by itself justify a smallest meaningful effect. Resolve whether ±0.15/±0.25 are fixed now or subject to a deterministic pre-main rule.

**Runtime is closer to a full day plus judging than to two ordinary nights.** Saved timings give:

- Study 4 trace creation and associated scoring: mean **57.05 seconds**, across 320 traces.
- Study 7 generated-answer cells: mean **29.38 seconds**, across 960 cells.
- Study 7 generated-arm peak driver memory: **11.61 GB**.

Applying those proxies gives approximately **15.2 hours for 960 traces + 7.8 hours for answer/rating work = 23 hours**. Study 8 has fewer rating branches but adds projection recording and judge calls. Context-dependent trace lengths, cleanup, loading, and memory pressure remain uncertain. Every additional average 10 seconds per cell adds 2.67 hours.

The pilot should time trace generation, perplexity/classifier scoring, answers, ratings, projections, and judges separately, including long capped traces. Study 4 had about 21% forced trace closures. Track process/system memory and swap as well as MPS driver allocation. Avoid retaining full hidden-state stacks or vocabulary logits; scalar projections are cheap, full-sequence outputs are not. Separate-process model unloading is the safest memory plan.

Required changes before freezing:

1. **Complete the executable token and intervention specification:** layer numbering, norm/hash, decoding, seeds, closure, exact prefixes, independent branches, and context-indexed trace keys.
2. **State RF3’s combined generation-and-replay estimand** and restrict claims about private affect, concealment, and state persistence.
3. **Freeze both judges and their execution settings**, using complete local snapshots and sequential processes.
4. **Finish the rubric, calibration set, parser, retry/missing policy, and agreement gate**, including its timing and failure consequences.
5. **Specify projection spans, averaging, precision, and observer-hook safety**, with a representation-level interpretation.
6. **Write complete statistical decision rules:** interval sidedness, component conjunctions, multiplicity, equivalence, missingness, and secondary-test scope.
7. **Define the new E5 eligibility rule and minimum usable sample**, preserving paired context comparisons.
8. **Freeze pilot criteria and revision boundaries.** Name the four pilot IDs; specify the digit-mass aggregation and absolute perplexity threshold of 6.0, its grouping, and failure consequences. A revision allowance must not permit open-ended wording search.
9. **Add covariance-sensitive power and measured resource planning**, distinguishing O1 evidence from unknown warmth precision.
10. **Freeze all imported dependencies and provenance**, not only Study 8 code, and validate resume integrity, gate failures, mixed-component nulls, parsing failures, and equivalence boundaries before approval/deposit.

Optional suggestions:

1. Add a small, separately labeled fixed-answer or fixed-continuation projection analysis to reduce variation from answer wording.
2. Strengthen calibration with blinded human ratings and more second-judge answers; report absolute disagreement alongside rank correlation.
3. Report a descriptive prompt-level joint-effect plot, so aggregate warmth/liking dissociation is not mistaken for universal within-prompt co-occurrence.
4. Consider a future crossed trace-generation-context × replay-context study if the goal becomes separating trace production from downstream context effects.
tokens used
101,928
**The experiment is technically feasible, but v0.1 is not ready to become binding.** The largest gaps are judge validation, the interpretation of the internal projection, and incomplete decision rules. I reviewed the specified code and records, inspected cached model shards, and recomputed prior variances and timing summaries in memory. I did not edit files or run model generations.

**Generating the new traces requires a new runner, but little new inference machinery.** [Study 4’s `Backend.trace()`](/Users/arthursu/Projects/affect-suppression-steering/study4/src/runner.py:116) already generates steered thinking, removes the hook, and discards the cache. Its answer method starts from a fresh unsteered forward. [Study 7’s assembly code](/Users/arthursu/Projects/affect-suppression-steering/study7/src/assembly.py:7) supplies the context-dependent system turns and preserves trace token IDs.

Study 7’s runner cannot simply be configured to generate new traces: its inherited Study 5 backend explicitly prohibits trace generation, and its loading/reproduction logic requires old traces and answers. A Study 8 runner should combine Study 4’s trace-generation path with Study 7’s assembly and independent rating branches.

The binding specification needs these details:

- “Layer 18” means **zero-based decoder module index 18**, the nineteenth decoder block, at its residual-stream output.
- Reuse the norm as well as direction hashes: `mean_resid_norm = 863.1329506247774`. The intervention is `0.0175 × norm × unit_direction`, not an absolute displacement of 0.0175.
- Freeze temperature 0.6, top-p 0.95, top-k 20, answer cap 200, stop tokens, and separate trace/answer seed maps if inheriting Study 4.
- Freeze natural and forced thinking closure, separator IDs, and the meaning of the 1,024-token cap. Existing code counts sampled thinking-phase tokens, including opening/closing markers where sampled.
- Assert that each replay prefix equals that cell’s original context/prompt IDs plus its exact trace and closure IDs. Never decode and re-template the conversation: prior thinking can disappear.
- Verify N has no system turn at all; verify M/W remain identical through trace generation, answer replay, and rating branches.

There is an important estimand change: **RF3 measures the total effect of context on both trace production and downstream processing.** It does not isolate how a social stake changes the processing of an identical hostile trace. That is a legitimate design, but “fixing Study 7’s replay mismatch” understates the change: Study 7 deliberately held traces fixed. Also, because steering covers prompt positions, M/W system-message tokens receive steering; N has no corresponding tokens.

**A local two-judge workflow is plausible after Qwen exits, not alongside it.** I checked index-listed weight shards and tokenizer files, rather than relying on cache directory names.

| Cached candidate | Complete weight files | Weight-file size, decimal GB | Assessment |
|---|---:|---:|---|
| Gemma-2-2B-IT | Yes | 5.23 | Practical primary-judge candidate |
| Llama-3.2-3B-Instruct | Yes | 6.43 | Practical second-judge candidate |
| Qwen2.5-3B-Instruct | Yes | 6.17 | Available, but shares Qwen family |
| Phi-3.5-mini-instruct | Yes | 7.64 | Available; greater memory cost |

These are availability and memory assessments, **not evidence that any candidate can judge this construct reliably**. Gemma and Llama have official Transformers inference support. [Gemma model card](https://huggingface.co/google/gemma-2-2b-it), [Llama model card](https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct).

My initial choice would be **Gemma primary, Llama secondary**, subject to the frozen calibration procedure. Their cached revisions are:

- Gemma: `299a8560bedf22ed1c72a8a11e7dce4a7f9f51f8`
- Llama: `0cb88a4f764b7a12671c53f0838cd831a0843b95`

Use separate processes sequentially, batch size one, bounded context/output, and explicit local paths. Gemma’s chat template needs its own handling; do not reuse Qwen’s system-message or token recipes.

The complete Qwen3-4B snapshot is in the **repository-local `study3_pilot/.cache`**, totaling about 8.05 GB. The home Hugging Face Qwen3 snapshot is incomplete: two of its three shards are absent. The two large MLX-named cache directories have no snapshots. Pin the actual complete path.

**The judge specification needs more work than the model selection.** Blinding should expose only the original user prompt and visible answer, under neutral randomized IDs. Hide system messages, trace, source, context label, seed, hypotheses, prior scores, and sibling answers. Use independent judge calls and shuffle presentation order. Answer content can reveal a context indirectly; describe this as metadata blinding, not guaranteed blindness.

The primary composite also needs an explicit interpretation. Warmth, praise, and validation are related but distinct. A warm factual correction can contain neither praise nor reassurance. If only item (a) changes from 1 to 5 while (b)/(c) remain unchanged, the composite moves only **1.33 points**, failing the proposed 1.5-point calibration gate despite maximal warmth separation. Thus the gate currently favors examples containing praise and validation together.

Freeze anchored examples for each score and rules for sarcasm, condescending reassurance, generic friendliness, praise of third parties, refusal, apology, and mixed warm/hostile answers. Decide whether the intended outcome is overall interpersonal warmth or the specified composite; do not switch after seeing effects.

Parsing should be mechanical: fixed JSON keys, integer values 1–5, required items, no duplicate keys, and explicit handling of extra text, missing items, refusals, and truncated output. Save the original response. Do not extract whichever digits happen to appear. Freeze any repair/retry rule and the missing-data consequence. A 95% parse threshold permits roughly 48 missing main-study judgments; ignoring them could bias contrasts if parsing failures depend on source or answer style.

The calibration set should be external to the main answers, frozen before judge/rubric evaluation, and include:

- Content-matched warm/cold pairs.
- Warm answers without compliments.
- Polite contempt, sarcasm, and patronizing reassurance.
- Apologies without warmth and warmth without apology.
- Examples near the middle of the scale, not just obvious extremes.

Specify its size, labels, construction, aggregation, and whether **both** judges must pass. Obvious extremes establish coarse discrimination, not sensitivity to a 0.25-point effect.

The second-judge gate has two problems:

1. Forty “study answers” is ambiguous between pilot and main. A main-answer gate cannot be a prerequisite for starting the main run. Freeze the sample-selection rule before scores are seen, and distinguish pre-main calibration from post-main interpretability.
2. Spearman correlation measures ranking, not absolute agreement. Judges can correlate perfectly while disagreeing systematically on rubric points. At \(n=40\), an observed correlation around 0.60 is also imprecise; a rough Fisher approximation gives an interval around 0.35–0.77, before accounting for ties or prompt clustering.

Retain the proposed rank gate if desired, but add an absolute-agreement diagnostic and freeze the treatment of ties, missing scores, constant outputs, repeated prompts, and failed gates. Never replace the primary judge because its main-study scores disagree with the second judge.

**The layer-18 projection is computable, but it cannot establish hostility independent of hostile text.** [Study 3 already contains a read-only projection hook](/Users/arthursu/Projects/affect-suppression-steering/study3/src/main_model.py:87). For a frozen token sequence and exact token-position set \(S\), the natural definition is

\[
P_S=\frac{1}{|S|}\sum_{t\in S}
\left\langle h^{\mathrm{out}}_{18,t},\hat v_H\right\rangle .
\]

Use a fresh unsteered teacher-forced forward; calculate dot products in float32; retain per-token scalar projections and token spans. Average within cell, then compute paired prompt-level differences against unsteered. Do not pool all tokens across prompts, which would overweight long answers.

Specify whether answer positions mean states **after consuming each answer token** or states predicting those tokens. Those differ by one position. The former matches the existing extraction convention more closely. Explicitly include or exclude EOS, role delimiters, separators, and empty-thinking markers. For the question measure, identify O1 versus O3 and select only the intended question tokens: Study 3’s existing `projection(start, …)` captures the entire suffix, including structural and assistant-prefix tokens.

There is also an implementation conflict: [Study 4’s hook assertion](/Users/arthursu/Projects/affect-suppression-steering/study4/src/runner.py:57) rejects **all** forward hooks, including a harmless observer. Assert no hooks before installing the projection observer and after removing it; verify that the observer returns no replacement activation and leaves logits unchanged. Do not disable steering-safety checks globally.

Interpretation is the larger limitation. After cache discard, downstream activations are reconstructed from the supplied tokens. A hostile trace can elevate the projection simply because the model is processing hostile language or hostile characterizations. Answer-token projections additionally depend on the different answers themselves. The direction was extracted from hostile versus neutral generated language, so this sensitivity is expected.

Call this **“hostility-direction alignment during unsteered processing of the retained conversation.”** It is a useful secondary representation measure, but cannot establish a concealed hostile state separate from the text, or resolve ordinary semantic carryover versus compensation. Fixed question tokens improve comparability without eliminating that limitation. O1 likewise measures a conditional reported evaluation, not privileged access to a private preference.

**The primary conjunctions are defensible, but the decision rules remain incomplete.** Define every contrast per prompt and average with equal prompt weights. RF3’s control-relative component should explicitly be

\[
[Y_{H,M}-Y_{C,M}]-[Y_{H,N}-Y_{C,N}],
\qquad C\in\{U,T,Q\}.
\]

Joint prompt resampling across contexts, sources, and outcomes is appropriate. Freeze whether resampling preserves the 60/20 provocative/neutral composition.

If each RF hypothesis requires all three component intervals to exclude zero in the stated direction, this is an intersection–union test. Bonferroni across RF1–RF3 is defensible; another factor-of-three correction within each conjunction is unnecessary. Explicitly specify **two-sided 98.333% percentile intervals with directional decisions**, rather than leaving “level \(1-0.05/3\)” ambiguous. The RF1∧RF2 signature adds no alternative success route.

However:

- RF1∧RF2 establishes opposite **average** effects. It does not establish that the same individual prompts show both changes.
- RF3 can be positive while both contexts have negative warmth effects. It needs RF1 for the compensatory-warmth interpretation.
- Failure to support RF1 under N is not evidence of “no compensatory warmth.”
- Define “reversed,” “negligible,” and “mixed” at the component and conjunction levels. A failed conjunction is not equivalent to a negligible effect.
- S1 contains two hypotheses, S3 contains two, and S4 repeats multiple tests. State their unadjusted secondary status explicitly.
- Report S2 estimates regardless of RF1, while applying the prespecified conditional interpretation; avoid selectively displaying only successful combinations.

The E5 subset needs a new rule. There are now three hostility traces per prompt. For RF3, use a prespecified common prompt subset across the compared contexts, rather than independently filtering M and N. Specify whether eligibility requires clean hostility traces in all three contexts and whether controls are audited. This is selection on post-intervention text, so it remains a sensitivity analysis, not a causally clean subgroup.

**The existing data support planning for O1, but not a confident power claim for warmth.** Recomputed from the saved Study 4 own-native and Study 5 R1 cells:

| O1 paired contrast | Prior mean | Prompt-level SD |
|---|---:|---:|
| Hostility − unsteered | −0.660 | 0.559 |
| Hostility − technicality | −0.720 | 0.658 |
| Hostility − random | −0.435 | 0.621 |

The two studies’ R1 values are **exactly identical**, so these are not independent variance replications. Component correlations are approximately 0.68–0.77.

Using that covariance, \(n=80\), and normal-approximation decisions corresponding to the proposed primary intervals, my 200,000-draw planning simulation gives:

| Assumed magnitude in every component | Simple-effect conjunction | Interaction, cross-context correlation 0 | Correlation 0.5 | Correlation 0.8 |
|---|---:|---:|---:|---:|
| 0.15 | 24% | 8% | 24% | 73% |
| 0.30 | 94% | 59% | 94% | ~100% |

These are illustrative assumptions, not power estimates for the full signature. The interaction calculation assumes equal context-specific covariance and a common cross-context correlation. Newly generated traces may yield substantially different correlations from replaying identical traces. Shared seeds may help but do not guarantee correlation.

Warmth has a different scale, unknown variance, possible ceiling effects, and judge error. Four pilot prompts cannot estimate those quantities reliably. Freeze a sensitivity analysis over plausible warmth variances and cross-context/outcome correlations, including joint RF1∧RF2 power. Do not import O1 power directly into RF1/RF3.

For equivalence, specify 90% intervals and which components must lie inside the margins. Under the old O1 variances, approximate 90% half-widths are already **0.103–0.121**, leaving limited room inside ±0.15. Interactions and E5 subsets will be less precise. A pilot’s spread describes variability; it does not by itself justify a smallest meaningful effect. Resolve whether ±0.15/±0.25 are fixed now or subject to a deterministic pre-main rule.

**Runtime is closer to a full day plus judging than to two ordinary nights.** Saved timings give:

- Study 4 trace creation and associated scoring: mean **57.05 seconds**, across 320 traces.
- Study 7 generated-answer cells: mean **29.38 seconds**, across 960 cells.
- Study 7 generated-arm peak driver memory: **11.61 GB**.

Applying those proxies gives approximately **15.2 hours for 960 traces + 7.8 hours for answer/rating work = 23 hours**. Study 8 has fewer rating branches but adds projection recording and judge calls. Context-dependent trace lengths, cleanup, loading, and memory pressure remain uncertain. Every additional average 10 seconds per cell adds 2.67 hours.

The pilot should time trace generation, perplexity/classifier scoring, answers, ratings, projections, and judges separately, including long capped traces. Study 4 had about 21% forced trace closures. Track process/system memory and swap as well as MPS driver allocation. Avoid retaining full hidden-state stacks or vocabulary logits; scalar projections are cheap, full-sequence outputs are not. Separate-process model unloading is the safest memory plan.

Required changes before freezing:

1. **Complete the executable token and intervention specification:** layer numbering, norm/hash, decoding, seeds, closure, exact prefixes, independent branches, and context-indexed trace keys.
2. **State RF3’s combined generation-and-replay estimand** and restrict claims about private affect, concealment, and state persistence.
3. **Freeze both judges and their execution settings**, using complete local snapshots and sequential processes.
4. **Finish the rubric, calibration set, parser, retry/missing policy, and agreement gate**, including its timing and failure consequences.
5. **Specify projection spans, averaging, precision, and observer-hook safety**, with a representation-level interpretation.
6. **Write complete statistical decision rules:** interval sidedness, component conjunctions, multiplicity, equivalence, missingness, and secondary-test scope.
7. **Define the new E5 eligibility rule and minimum usable sample**, preserving paired context comparisons.
8. **Freeze pilot criteria and revision boundaries.** Name the four pilot IDs; specify the digit-mass aggregation and absolute perplexity threshold of 6.0, its grouping, and failure consequences. A revision allowance must not permit open-ended wording search.
9. **Add covariance-sensitive power and measured resource planning**, distinguishing O1 evidence from unknown warmth precision.
10. **Freeze all imported dependencies and provenance**, not only Study 8 code, and validate resume integrity, gate failures, mixed-component nulls, parsing failures, and equivalence boundaries before approval/deposit.

Optional suggestions:

1. Add a small, separately labeled fixed-answer or fixed-continuation projection analysis to reduce variation from answer wording.
2. Strengthen calibration with blinded human ratings and more second-judge answers; report absolute disagreement alongside rank correlation.
3. Report a descriptive prompt-level joint-effect plot, so aggregate warmth/liking dissociation is not mistaken for universal within-prompt co-occurrence.
4. Consider a future crossed trace-generation-context × replay-context study if the goal becomes separating trace production from downstream context effects.
