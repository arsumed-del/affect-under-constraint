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
