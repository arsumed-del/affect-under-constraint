# Preregistration — Study 6: The Answer Clamp

**Working title:** Affect Under Constraint VI: Does a Steered Reasoning Trace Shape Later Judgment When the Answer Is Held Fixed?
**Author:** Arthur Su. **Designed by:** Claude (2026-10-27).
**Version:** 0.2 DRAFT (not binding until `PREREG_APPROVED` and Zenodo deposit).
**Changes in v0.2:** incorporates Codex (CODEX_REVIEW_v0.1.md) and ChatGPT (CHATGPT_REVIEW_v0.1.md) reviews: exact token construction and end-token rule; Study 5 unsteered ratings as the shared analytic baseline after validation; sham-replay validation of all sources; estimands renamed as answer-token interventions ("effect under clamp", "answer-replacement contrast") with M^X principal; reciprocal answer swap added (2×2 trace × answer per placement); prespecified generic-answer sensitivity for R1/R3; exhaustive reading table without mediation-by-disappearance claims; equivalence outside familywise control; power from Study 5 paired variances; truncation and valid-mass rules; measured runtime.
**Provenance:** designed after observing Study 5 outcomes (prereg 10.5281/zenodo.23674222). Earlier: Study 4 10.5281/zenodo.23629525; Study 3 10.5281/zenodo.23323490.

## Rationale
Studies 3–5 found that a hostility state steered into Qwen3-4B's reasoning trace lowers the model's later rating of the user; that the effect is carried by the trace text once steering is removed (Study 3); that it requires the text to sit in the model's own turn rather than be quoted by the user (Study 4); and that it persists, attenuated, when the trace sits in a previous assistant turn as visible reply or retained thinking (Study 5). In every study the order was trace → freshly generated answer → rating, and answers after hostility traces were more hostile. The rating effect may therefore act on the judgment with the answer held fixed, or depend on the answer the trace produced.

Study 6 intervenes on the answer at the token level. It replaces each source's answer with a common answer and, reciprocally, gives the unsteered trace the hostility trace's answer. The study tests effects of these answer-token interventions on the recorded stimuli. It does not identify mediation through expressed hostility as such (the answer differs in content, length, stance and termination as well as tone), and it makes no claim about internal states.

## 1. Design (yoked replay of stored tokens; no generation)
**Stimuli:** the 80 Study 4 test prompts, the 320 stored traces (sources U unsteered, H hostility, T technicality, Q random), the five Study 5 placements (R1, R1-M, R2, R3, R4; Study 5 prereg Section 1), and Study 5's stored answers. Rating branches in Study 5 were verified to contain the trace for all placements.

**Construction (exact):** for source s, prompt p, placement c and answer a:
`Study5[s,p,c].answer_prefix_ids + a + closure + sender-rating branch`,
where closure follows Study 4 `Assembly.end_turn()` applied to a (keeps a complete delimiter, adds a newline after an emitted `<|im_end|>`, else appends the full delimiter), and the rating branch is Study 5's. Answers are replayed exactly, including truncated ones (forced closure).

**Arms:**
| Arm | Answer a | Sources | Placements | Cells |
|---|---|---|---|---|
| Clamp (primary) | a_U: the unsteered answer for (p, c) | U, H, T, Q | all five | 1,600 |
| Reciprocal swap | a_H: the hostility answer for (p, c) | U | all five | 400 |
| Generic clamp (sensitivity) | fixed text G: "Thanks for your message. I've considered your request carefully, and I'm happy to help with it." | U, H, T, Q | R1, R3 | 640 |
Total 2,640 rating-only cells.

**Shared baseline:** U-with-a_U cells are token-identical to Study 5. They are re-rated as validation; the analytic baseline is the stored Study 5 rating, so Y_U(a_U) is a single quantity shared by both studies.

## 2. Estimands (per prompt, then averaged; Y_s(a) = rating after source s's trace with answer a)
- **Total effect (Study 5):** TE = Y_H(a_H) − Y_U(a_U).
- **Effect under clamp:** D_U = Y_H(a_U) − Y_U(a_U). Control-relative: D_C = Y_H(a_U) − Y_C(a_U), C ∈ {T, Q}.
- **Answer-replacement contrast (principal):** M^X = TE − D_U = Y_H(a_H) − Y_H(a_U): the change from replacing the hostility answer with the unsteered answer, under the hostility trace. TE = D_U + M^X exactly.
- **Control-relative replacement difference:** M_C = [Y_H(a_H) − Y_H(a_U)] − [Y_C(a_C) − Y_C(a_U)], with both bracketed terms reported separately.
- **Answer effect under unsteered trace (swap):** S = Y_U(a_H) − Y_U(a_U). Together with M^X this gives a 2×2 (trace U/H × answer a_U/a_H) per placement; interaction = M^X − S.
- **Proportion (descriptive):** M^X / TE, reported only where TE is supported and the bootstrap denominator excludes zero in ≥ 97.5% of draws; not clipped.

## 3. Hypotheses and inference
Prompt-cluster bootstrap: 10,000 resamples of the 80 prompt IDs, one fixed seed, the same draws for every estimand, Study 5 and Study 6 values resampled jointly. Percentile CIs. Conjunction (intersection–union) rule: supported only if every listed component excludes zero in the stated direction.

**Primary** (CI level 1 − 0.05/3, two-sided intervals, directional decisions)
- **D1 — Effect under clamp, current thinking (R1):** D_U < 0 and D_T < 0 and D_Q < 0.
- **D2 — Effect under clamp, retained historical thinking (R3):** same components in R3.
- **M1 — Answer-replacement contrast, current thinking (R1):** M^X ≠ 0 (two-sided). M_T and M_Q are reported as specificity evidence; if their signs disagree with each other, the result is labelled "mixed control-relative effects."

**Secondary** (95%, unadjusted, labelled as such): effects under clamp in R1-M, R2 (note: R2's trace is itself visible assistant text) and R4; M^X in R1-M, R2, R3, R4; swap S in every placement; 2×2 interaction in R1 and R3; generic-clamp effects under clamp in R1 and R3.

**Status labels:** supported; reversed (excludes zero in the opposite direction); negligible (90% CI within ±0.15); small but detectable (supported and negligible); inconclusive (otherwise). Equivalence statements are descriptive and outside familywise control.
**Margin:** ±0.15 on the 0–9 expected-digit scale, carried from Studies 4–5 for comparability. Relative to historical effects (≈ −0.24), a "negligible" residual can still be a sizeable fraction; "negligible" is never reported as "absent".
**Precision** (normal approximation from Study 5 prompt-level SD of X, used as a proxy for the clamped contrasts): R1 SD 0.56 → power ≈ 0.50 for −0.15 and 0.93 for −0.24 at the primary level; R3 SD 0.30 → ≈ 0.98 and > 0.99. Conjunction and M-contrast power may be lower; R1 equivalence is unlikely to be established for small residuals.

## 4. Reading (answer-token intervention terms)
| D (effect under clamp) | M^X | Reading |
|---|---|---|
| supported | negligible | The effect persists under this clamp; replacing the answer changes it by less than the margin. |
| supported | negative, supported | The clamp attenuates the effect, with residual influence under the fixed answer. |
| negligible | negative, supported | The clamp reduces the effect to within the margin; the recorded answers carried most of the total effect for these stimuli. |
| supported or negligible | positive, supported | The clamp amplifies the effect (the hostility answer had offset part of it). |
| reversed | any | Under the fixed answer the hostility trace raises the rating; reported as reversal. |
| inconclusive | any | Unresolved at this sample. |
| supported, small but detectable | any | Reported as small but detectable. |
The swap S reports whether the hostility answer alone (under an unsteered trace) lowers the rating. D2 is read with R3's M^X (secondary). Comparisons between placements require direct contrasts. Clinical "projection analog" language, if used, is confined to the Discussion.

## 5. Pilot and validity
Pilot: prompts s3t00, s3t01, s3t02, s3t60 (Study 5 pilot), using the Study 5 pilot answers, all arms (132 cells), plus a sham replay: every Study 5 pilot cell (all sources, own answers, 80 cells) re-rated.
- (a) Token check: every rebuilt original branch equals Study 5's stored `branch_ids` exactly; any mismatch is a build error.
- (b) Numerical check: sham-replay ratings reproduce Study 5 within 0.01 per cell, on two separate process starts. If tokens match but a rating differs by more than 0.01, the run is blocked and the environment is investigated; the tolerance is not changed after inspection.
- (c) Valid-digit mass ≥ 0.8 by placement × source; a failing placement is dropped from all estimands and reported.
- (d) Runtime and peak memory measured on the longest prefixes; the main-run estimate is replaced by this measurement.
The main run repeats (a) for all 1,600 original branches before any inference and (b) for all 400 U-with-a_U cells; failure stops the run.

## 6. Descriptive and sensitivity
- Per arm and placement: answer length, truncation, expressed hostility (stored Study 5 classifier scores for replayed answers), and the 0–9 rating distribution.
- Completed-answer subset: estimands repeated on prompts whose clamp answer a_U (and a_H for swap/M^X) ended naturally; n reported per placement (Study 5 unsteered answers truncated: R1 28/80, R1-M 30, R2 27, R3 29, R4 26).
- Natural-closure and Study 4 E5 subsets as in Study 5, paired clusters preserved.
- No no-answer arm.

## 7. Freezing, reporting, stopping
Hashed in `PREREG_APPROVED`: this preregistration, framings and config, Study 6 runner and analysis (validated on synthetic data with planted no-change, partial-attenuation, full-attenuation, amplification and missing-cell patterns, and exact shared-baseline cancellation), inherited Study 4/5 code, Study 5 cell file, model/tokenizer files, and the execution environment (torch version, device, dtype, attention implementation, batch size 1, no padding). Zenodo deposit before the main run; no changes after it starts. Output is resumable, one row per cell, with full rating-input hashes and digit log-probabilities. A bug fix after the start is logged and, if it changes any rating, all affected cells are rerun. Scope: conditional on the Study 4 stimuli and the recorded Study 5 answers; uncertainty is across prompts, not generation seeds; not an independent replication.
