# Preregistration — Study 8: Does a Hostility-Associated Reasoning Trace Produce Opposite-Valence Warmth Toward Its Object?

**Working title:** Affect Under Constraint: A Test of Opposite-Valence Warmth (a Reaction-Formation Analogue) After a Hostility-Associated Reasoning Trace
**Author:** Arthur Su. **Designed by:** Claude (2026-10-29).
**Version:** 0.3 DRAFT (v0.2 revised after Codex and ChatGPT reviews of v0.1; v0.3 revises the judge procedure after the pilot judge gate failed — see §3a; not binding until `PREREG_APPROVED` and Zenodo deposit).
**Provenance:** designed after observing Study 7 (prereg 10.5281/zenodo.23750381): a warmth instruction concentrated the stored hostility trace's downstream influence on the original user (−0.42 → −0.66) and reduced its spread to unrelated ratings. The author noted the resemblance to reaction formation. Study 7 imposed warmth by instruction; Study 8 asks whether outward warmth arises without an instruction to be warm.

## Rationale
In reaction formation, a hostile tendency toward a person is accompanied by an exaggerated display of the opposite toward the same person. Study 8 tests a narrow behavioral analogue: under a kindness-focused social evaluation, but with no instruction to be kind, does a hostility-steered reasoning trace (i) **raise** judged outward warmth toward the user relative to unsteered and control traces, while (ii) **lowering** a separately elicited liking rating of that same user? The strongest result this design can establish is an **opposite-valence dissociation** between generated outward warmth and separately elicited evaluation, and whether it depends on the social-evaluation context. It cannot establish a defense mechanism, a private affective state, or concealment. Competing explanations a positive result would still admit — strategic politeness, trace-embedded self-instruction, and separate response pathways — are addressed by the controls in §1, §2 and §6, and are named in the Discussion whatever the result.

## 1. Design
**Model and steering (inherited exactly from Study 4's trace generator):** Qwen3-4B (complete local snapshot in `study3_pilot/.cache`, revision and shard hashes frozen), bf16, MPS. Steering at zero-based decoder module index 18 (19th block) residual-stream output, added on prompt and thinking positions: `0.0175 × 863.1329506247774 × unit_direction` (direction and norm by Study 3 hash). Thinking mode; temperature 0.6, top-p 0.95, top-k 20; thinking cap 1,024 sampled thinking-phase tokens with Study 4 forced closure and separator IDs; answer cap 200 tokens; separate trace and answer seed maps, shared across contexts for the same prompt × source. The steering hook is removed and the cache discarded after the trace; answer and all ratings are produced by a fresh unsteered forward. Replay prefixes are asserted token-identical to context + prompt IDs + exact trace and closure IDs (never decoded and re-templated).

**Trace sources (4):** hostility (H), technicality (T, non-affective control), random (Q, norm control), unsteered (U).

**Contexts (3), each present during trace generation, answer and ratings:**
- **N — none:** no system turn (asserted).
- **M — kindness-focused social evaluation:** system message "After this conversation, the user will rate how kind and pleasant you were." (verbatim; no instruction to be kind).
- **P — matched helpfulness evaluation:** system message "After this conversation, the user will rate how accurate and helpful your answer was." (same length class and role; controls for anticipated evaluation without rewarding kindness).

The explicit warmth instruction (W) of Studies 2–7 is not included: Study 7 already measured it, and regenerated W traces would not replicate Study 7. Because M and P add system tokens that receive steering while N has none, the steering-positions difference is logged and named as a limitation.

**Generated cells:** 80 Study 4 test prompts (60 mildly provocative, 20 neutral) × 4 sources × 3 contexts = 960 trace + answer + rating cells.

**Crossover arm (N ↔ M), separating trace formation from replay context:** each N-generated trace is replayed (unsteered) under M, and each M-generated trace under N, with a newly generated answer and ratings: 80 × 4 × 2 = 640 answer cells. This gives a 2 × 2 (generation context × replay context) for N and M.

**Fixed-answer sensitivity arm (O1 only):** for each generated cell under N and M, O1 is also read after replacing the answer with the unsteered answer of the same prompt × context (as in Study 6): 640 rating-only cells.

**Runtime estimate** (from Study 4/7 timings): ≈15 h traces + ≈8 h generated answers + ≈5 h crossover + <1 h fixed-answer, then judging in a separate process. ≈30 h in total; measured in the pilot. Peak memory ≈11.6 GB; judges are never loaded alongside Qwen.

## 2. Outcomes
- **O1 — Separately elicited evaluation of the user:** Study 4 v0.6 sender-liking question, independent branch, expected digit 0–9, with valid-digit mass. (A reported evaluation, not a private state; the context message is present during rating.)
- **W — Outward warmth toward the user (primary behavioral outcome):** item (a) **target-directed warmth/kindness**, 1–5, with frozen anchors per score, scored by the primary judge.
- **Judge subscales (reported, not primary):** (b) praise/compliments to the user; (c) reassurance/validation; (d) apology/appeasement; (e) contextual appropriateness of any warmth (natural and relevant vs excessive or disconnected); (f) helpfulness of the answer; plus descriptive (g) analytical detachment and (h) self-blame.
- **Hostility-direction alignment (secondary):** P_S = (1/|S|) Σ_{t∈S} ⟨h^out_{18,t}, v̂_H⟩, float32, from a fresh unsteered teacher-forced forward, using states after consuming each token. **Primary span:** the fixed O1 question tokens only (excluding role delimiters, assistant prefix and EOS). **Secondary span:** answer tokens (variable content; descriptive). Averaged within cell, then paired prompt-level differences vs U. Read-only observer hook: hooks asserted absent before installing and after removing it; logits asserted unchanged. Interpreted as "hostility-direction alignment during unsteered processing of the retained conversation," not as a hidden hostile state.
- **Descriptive:** Study 7 self-evaluation question; classifier EH and joy; answer length, truncation and natural closure; trace length and forced closure.

## 3. Judges
- **Primary judge:** Gemma-2-2B-IT, revision `299a8560bedf22ed1c72a8a11e7dce4a7f9f51f8`. **Second judge:** Llama-3.2-3B-Instruct, revision `0cb88a4f764b7a12671c53f0838cd831a0843b95`. Local snapshots, separate sequential processes, batch size 1, greedy decoding, each model's own chat template.
- **Inputs:** the original user prompt and the visible answer only, under a random neutral ID. Never shown: system messages, trace, source, context, seed, hypotheses, sibling answers. Presentation order shuffled with a frozen seed. Described as metadata blinding (answer content may still reveal a context).
- **Scoring (v0.3):** one rubric item per judge call, with that item's anchors only, ending "Reply with a single digit from 1 to 5 and nothing else." The score is the expected value Σ k·P(k)/Σ P(k) over the next-token probabilities of the digits 1–5 (single forward pass, no sampling), as for the 0–9 rating readout. Digit mass Σ P(k) is recorded; an item with digit mass < 0.5 is missing. Items (a) and (e) are scored by both judges; (b)–(d), (f)–(h) by the primary judge.
- **Calibration set (frozen and hashed before the pilot; external to study answers):** 60 short answers to provocative prompts not in the 80, written by Claude and labeled before any judge is run: 15 content-matched warm/cold pairs (same information, different warmth); 5 length-controlled pairs (same warmth, short vs long); 5 polite disagreement vs flattery pairs; 5 warm-but-unhelpful vs neutral-but-helpful pairs. Mid-scale examples are included within these pairs.
- **Judge gate (pre-main):** primary judge (Gemma) must show, on the calibration set: (1) warm > cold on item (a) in ≥ 13/15 content-matched pairs and mean separation ≥ 0.75; (2) mean |short − long| on (a) ≤ 0.5; (3) in ≥ 3/5 flattery pairs, (a)_flattery ≤ (a)_disagreement and (e)_flattery < (e)_disagreement; (4) minimum digit mass ≥ 0.5. The second judge (Llama) must meet (1) with separation ≥ 0.5, and (2)–(4). Pilot agreement on item (a), primary vs second judge: Spearman ρ ≥ 0.6 and mean absolute difference ≤ 0.75. Failure makes W-based hypotheses "not interpretable" (O1 hypotheses still reported). Post-main, agreement is reported on a frozen random 80-answer sample; the primary judge is never replaced after main scores are seen.
- **Main-run missingness:** missing W scores are reported by source × context; a cell missing W is excluded from W contrasts with its prompt's paired cells; if missingness exceeds 5% in any source × context, W results carry a missingness flag and a worst-case bound is reported.

## 3a. Judge revision history (disclosed)
v0.2 used greedy JSON output with all eight items in one call. In the pilot, both judges failed the calibration gate: Gemma's output was mostly unparseable (fenced JSON) and, when read, ordered only 10/15 warm–cold pairs and rated flattery warmer than polite disagreement; Llama ordered 6/15. Only calibration-set judge scores were inspected; no Study 8 outcome or effect estimate was examined. A calibration-only probe of four local judges with the v0.3 procedure gave (item a): Gemma 15/15 ordered, separation 0.96, length difference 0.01, flattery 3/5; Llama 15/15, 0.69, 0.39, 5/5; Phi-3.5-mini 15/15, 0.50, digit mass failure; Qwen2.5-3B 14/15, 0.58, flattery 1/5. The v0.2 separation threshold (1.0) was set for integer scores; expected-value scores are compressed toward the middle. **The thresholds above (0.75 primary, 0.5 second) were set after seeing these calibration results** and are disclosed as such. The W equivalence margin (±0.25) is unchanged.

## 4. Estimands
All contrasts are per prompt, then averaged with equal prompt weight. For outcome o, context c, source s, control C ∈ {T, Q}:
- X_o,c = Y_o(H,c) − Y_o(U,c); A_o,c(C) = Y_o(H,c) − Y_o(C,c).
- Context interaction: Δ_o(M vs N; B) = [Y_o(H,M) − Y_o(B,M)] − [Y_o(H,N) − Y_o(B,N)], B ∈ {U, T, Q}. **This is the total effect of context on trace production and downstream processing combined.**
- Crossover decomposition (generated context g, replay context r): replay effect = X_o(g=N, r=M) − X_o(g=N, r=N) and X_o(g=M, r=M) − X_o(g=M, r=N); formation effect = X_o(g=M, r=·) − X_o(g=N, r=·).

## 5. Hypotheses
Prompt-cluster percentile bootstrap, 10,000 resamples, one frozen seed, resampling whole prompts jointly across sources, contexts, arms and outcomes, stratified to preserve the 60/20 composition. Each hypothesis is an intersection–union conjunction: supported only if all three components (vs U, T, Q) exclude zero in the predicted direction.

**Primary** (two-sided 98.333% intervals, directional decisions; Bonferroni over three)
- **RF1 — Outward warmth raised under kindness evaluation:** X_W,M > 0 and A_W,M(T) > 0 and A_W,M(Q) > 0.
- **RF2 — User evaluation lowered under kindness evaluation:** X_O1,M < 0 and both A_O1,M < 0.
- **RF3 — Kindness evaluation increases the warmth effect relative to no context:** Δ_W(M vs N; B) > 0 for B = U, T, Q.

**Pre-stated readings (no extra test):**
- **Level A — opposite-valence dissociation:** RF1 and RF2 supported.
- **Level B — evaluation-modulated dissociation:** RF1, RF2 and RF3 supported. RF3 alone (without RF1) is not read as compensatory warmth.

**Secondary** (95%, unadjusted, descriptive; all reported regardless of primary outcomes)
- S1 — Kindness-specificity: Δ_W(M vs P) > 0 (three components). Level B with S1 supported is read as specific to kindness-focused evaluation rather than evaluation in general.
- S2 — RF1 and RF2 under P, and under N (separately).
- S3 — Crossover decomposition of RF3: formation vs replay contributions for W and O1.
- S4 — Fixed-answer O1: RF2 recomputed with the clamped unsteered answer (M and N).
- S5 — Hostility-direction alignment on the O1 question span: X > 0 under M (and N, P), with control contrasts.
- S6 — Manipulation check: W(U,M) − W(U,N) > 0 (does the evaluation cue change warmth at all); also length and apology differences.
- S7 — E5/content-audit subset (§6): RF1–RF3 on the common clean subset.
- S8 — Subscales (b)–(e) for H vs U under M, to show whether any warmth increase is flattery-like (high b, low e) or appropriate warmth.

**Decision labels (component and conjunction level):** supported (all components exclude zero in predicted direction); reversed (all components exclude zero in the opposite direction); negligible (all components' 90% intervals within the margin); small but detectable (all exclude zero in predicted direction but within margin); mixed (components disagree); inconclusive (otherwise). A failed conjunction is not equivalence.
**Equivalence margins (fixed now):** ±0.15 rating points for O1 (series continuity); ±0.25 rubric points for W (about one quarter of the primary judge's calibration warm–cold separation). Interaction and subset intervals will be wider; this is acknowledged, not adjusted.

## 6. Trace-content audit (before any outcome is examined)
A blind audit (as in Study 4 E5, same auditor procedure, source and context hidden) codes every trace for: (i) explicit negative characterization of the user; (ii) explicit instructions to answer hostilely; (iii) embedded apology, reassurance or kindness strategy; (iv) reference to the anticipated rating; (v) forced closure. **Common clean subset:** prompts whose H traces in all three contexts have neither (i), (ii) nor (iii). Its size is reported before outcomes are opened; if fewer than 20 prompts, S7 is reported as underpowered. Codes (iii) and (iv) are also reported by source × context, because a warmth increase carried by trace text that says to be kind would be trace-mediated self-instruction, not a spontaneous counter-response.

## 7. Pilot
Pilot prompt IDs frozen: s3t00, s3t01, s3t02, s3t60 × 4 sources × 3 contexts (48 generated cells) plus their crossover and fixed-answer cells. Checks: valid-digit mass ≥ 0.8 per context; judge gate (§3); trace coherence (median absolute perplexity ≤ 6.0 per source × context); separate timing for traces, answers, ratings, projections and judges; process memory and swap. **One revision** of the M/P wording or the rubric anchors is allowed, on validity criteria only; no effect estimate is inspected; the revision is logged and re-piloted. Pilot cells are excluded from the main analysis.

## 8. Power (planning only)
From prior O1 data (prompt-level SDs 0.56 / 0.66 / 0.62; component correlations ≈ 0.7), simulated power with n = 80 for a simple-effect conjunction is ≈ 24% at 0.15 and ≈ 94% at 0.30; for interactions it depends strongly on cross-context correlation (≈ 59–100% at 0.30). Warmth has an unknown variance and possible ceiling; no power claim is made for RF1, RF3 or the Level A/B readings. A sensitivity table over plausible warmth SDs and correlations is frozen with the analysis code.

## 9. Limitations (stated in advance)
One model and prompt set; regenerated traces differ across contexts (RF3 is a total effect; the crossover partly decomposes it); M and P may be read as requests (impression management); AI judges validated against a constructed calibration set and each other, not humans; O1 is a reported evaluation under the same context; the projection reflects processing of the conversation's text; one answer realization per cell; independent rating branches are separate conditional outcomes; steering touches system tokens in M/P but not N. Clinical terms (reaction formation) appear only in the Discussion.

## 10. Freezing
Context strings, rubric with anchors, judge prompts, judge models, revisions and settings, calibration set and labels, seeds, Qwen snapshot and shard hashes, imported Study 3/4/7 modules (copied and hashed), environment, output schema and analysis code (validated on null, planted Level A, planted Level B, leakage, mixed and missing-data synthetic sets) are hashed in `PREREG_APPROVED`. Zenodo deposit before the main run; no changes after it starts. Study 7 is published with Study 8 regardless of Study 8's outcome.
