# Preregistration — Study 3: Affect Under Constraint (recursion channel)

**Working title:** Affect Under Constraint III: Does Re-Reading One's Own Reasoning Carry a Steered Affective State Forward?

**Author:** Arthur Su
**Version:** 0.4 DRAFT (not binding; becomes binding only when `PREREG_APPROVED` exists, §13).
**Changes from v0.3:** pre-approval check results filled in (§7, §12); four specification gaps identified by the implementing agent are closed: the pulse-steering protocol and the S5 measure (§6, §8.2), coherence-gate grouping and its interaction with P2 (§9), the natural-closure subset for E3 and the fixed sample for E4 (§8.3).
**Changes from v0.2:** the four open design decisions are settled (§15): P2 kept as written; warmth condition only; pulse steering promoted to a secondary hypothesis (S5) for all three directions; top dose set to 0.0175. Values marked **[CHECKS]** are filled from the pre-approval checks (`study3/results/`).
**Changes from v0.1:** pilot values filled in from the Study 3 feasibility pilot (`study3_pilot/results/feasibility.md`, Amendment P1; calibration and extraction prompts only); coherence rule changed to absolute perplexity; one numerical path for all ratings; identical turn-2 rating prefix and identical decoding in both modes; longer generation caps; design reduced to the warmth condition and three doses so it fits about three nights. Each change is motivated in §2.1.
**Relation to earlier studies:** Study 1 (prereg v2.3, 10.5281/zenodo.23140443) and Study 2 (prereg v3.1, 10.5281/zenodo.23147672) are complete; results in the preprint (concept DOI 10.5281/zenodo.23182205, v3). Study 3 is a new, separately preregistered study. Studies 1 and 2 are not reanalyzed.

---

## 1. Question

In Study 2, a steered hostility representation persisted beneath an instruction to be warm (P1, general across three families), but it did not carry over to a later judgment in an affect-specific way through the hidden state alone (P2, not supported). Study 2's carryover measure held the visible text fixed, so influence carried through the model's own generated output was treated as baseline rather than tested.

Study 3 asks: **when a model can write and then re-read its own reasoning, does a steered affective state carry forward to a later judgment more than when it answers directly?** The manipulation is a reasoning ("thinking") mode switched on versus off in the same model weights, at the same dose.

## 2. Rationale

A transformer carries no state between steps other than its context. A steered representation that shapes the model's output can be re-encountered when that output is read back. Accounts of affect regulation that emphasize recursive processing predict that persistence across time depends on such a loop rather than on a residual trace. Toggling thinking within one model varies access to the loop while holding weights, architecture, scale and dose constant.

### 2.1 What the pilot showed and what changed

The pilot (Qwen3-4B, 40 calibration prompts, descriptive only) found:

1. **Ratio-based coherence did not transfer.** Qwen3's unsteered text has unusually low perplexity (median 1.15), so the Study 2 ratio rule rejected fluent text at the smallest dose. In absolute terms the selected dose scored 4.59, within the range of Study 2's accepted doses (3.34–5.06). → Coherence is judged by absolute perplexity (§6).
2. **Cached and full-forward ratings of identical tokens differed by up to 0.50 points** in bf16 on MPS. → Every rating is one full forward pass over the complete sequence (§7); at zero dose the routes then agreed exactly (maximum difference 0.0 over 90 checks).
3. **The two modes were rated from different turn-2 prefixes.** With thinking on, the digit was scored where the model would normally begin reasoning; baseline ratings were compressed and shifted (mean 4.51, SD 0.10, versus 7.53, SD 0.55, with thinking off). → Turn 2 is rated from the same non-thinking prefix in both modes, so only turn 1 differs (§3).
4. **Decoding settings differed by mode.** → One decoding setting for both modes (§3).
5. **Caps were too short:** at full dose, 39/40 traces hit the 384-token thinking cap and 38–39/40 answers hit the 120-token cap. → Caps raised (§3), truncation reported and analyzed (§8.3 E3).
6. **Runtime:** about 51 s per thinking-on cell and 12 s per thinking-off cell at the old caps; the full v0.1 design projected to 50.6 h. → Design reduced (§5, §12).

Descriptive observations that bear on the hypotheses are reported for transparency but did not change them. Under the warmth instruction at full dose, mean expressed hostility was 0.279 in the thinking trace and 0.329 in the answer, with the trace exceeding the answer at zero and half dose but not at full dose. These pilot values used calibration prompts, the old caps and the old rating prefix, and are not evidence for or against §8.

## 3. Model

| id | params | access |
|---|---|---|
| `Qwen/Qwen3-4B` | 4B | ungated |

bfloat16 on Apple M4 (MPS), no quantization (pilot peak driver allocation 9.47 GB). Thinking is toggled for turn 1 with the chat template's `enable_thinking` flag. One model only: Study 3 makes no cross-family generality claim.

**Decoding (both modes):** temperature 0.6, top-p 0.95, top-k 20; seed fixed per cell. **Caps:** thinking 1,024 new tokens (forced `</think>` if reached; truncation recorded), answer 200 new tokens.

**Turn-2 rating prefix (both modes):** the turn-2 assistant turn begins with an empty thinking block (`<think>\n\n</think>\n\n`), and the digit is scored immediately after it. The rating step is therefore identical across modes; only turn 1 differs.

**Context handling:** Qwen3's template strips earlier-turn thinking from the history. For every rating, the exact turn-1 token sequence (prompt, thinking, any forced closure, answer) is kept and followed by a verified turn-2 continuation, as implemented and audited in the pilot.

## 4. Directions

Layer L = round(0.5 × number of decoder layers) = 18, no search. Hostility (target), technicality (non-affective control) and random (norm control, seed 777) directions as extracted in the pilot under Study 2's procedure (thinking off, the 40 Study 2 extraction scenarios); vectors and mean residual norm are reused from the pilot by hash.

## 5. Conditions and prompts

- **Mode (within prompt):** thinking on (`think`) vs. thinking off (`direct`).
- **Instruction:** `warm_constraint` only (Study 2 wording, verbatim). The neutral condition is dropped to fit the runtime; see open decision 2.
- **Test set:** 80 new prompts (60 mildly provocative, 20 neutral), written before approval and disjoint from all Study 1, Study 2 and pilot prompt sets.

## 6. Steering and dose

Steering adds α · r̄_L · v̂ to the output of layer 18 at every turn-1 position (prompt, thinking and answer). Steering is off for all turn-2 positions.

**Dose (fixed before any test data):** top dose α_top = **0.0175**. Amendment P1's rule selected α_max = 0.02: the largest candidate whose median absolute perplexity (steered text, scored by the unsteered model) was ≤ 5.0, whose distinct-token ratio was ≥ 0.6 × baseline, and whose increase in expressed hostility had a 95% bootstrap lower bound above zero (thinking off: absolute perplexity 4.59; hostility increase 0.168, 95% CI 0.098–0.239; first incoherent candidate 0.025). With thinking on, the answer at α_max had median absolute perplexity 2.89. Write-once record: `study3_pilot/data/calibration/qwen3-4b_amendP1.json`. The top dose is set one step below α_max, at 0.0175, the next largest candidate that passed both checks (absolute perplexity 3.42; hostility increase 0.100, 95% CI 0.050–0.156). Reason: at 0.02, pilot reasoning traces showed repetition and invented context despite passing the numerical gate, and the hypotheses depend on the model re-reading a trace that remains meaningful. Longer caps (§3) give more room for such degradation. This choice uses calibration data only and is fixed before any test data exist.

**Grid:** a = α/α_top ∈ {0, 1/2, 1}, i.e., α ∈ {0, 0.00875, 0.0175}.

**Pulse protocol (S5, E1).** Think mode, a = 1, all three directions. (1) Generate the prompt and thinking with steering on every position, exactly as in regular cells, through the closing `</think>` (natural or forced). (2) Discard the generation cache. Re-encode the complete prefix (prompt, thinking, closing tokens and the answer separator) in one unsteered forward pass, and generate the answer unsteered from that cache, so the first answer-token logits come from the unsteered re-encoding. The answer can therefore depend on the steered state only through the text of the trace. (3) Ratings: R_text(pulse) is the unsteered full forward over the complete sequence; R_full(pulse) applies steering to prompt and thinking positions only (answer and turn-2 positions unsteered), matching generation. LHP in pulse cells is scored unsteered after the re-encoded prefix and is exploratory.

## 7. Measures

- **EH_trace / EH_answer:** expressed hostility (classifier anger + disgust, as Study 2), scored separately on the thinking trace and on the answer; the trace is scored in 120-token windows and averaged.
- **LHP, entropy, perplexity:** as Study 2 (LHP teacher-forced on the turn-1 answer prefix in each mode).
- **Ratings** (Study 2's turn-2 liking question, 0–9 expected digit). Every rating is one full forward pass over the complete sequence; generation-time caches are never used.
  - **R_full:** steering active on turn-1 positions only.
  - **R_text:** same tokens, no steering.
  - **R_zero:** the model's own α = 0 generation (same prompt and mode), no steering.
- **Total carryover** C = R_full(a) − R_zero; **text route** X = R_text(a) − R_zero; **hidden route** H = R_full(a) − R_text(a). C = X + H by construction.
- **Validity check (required before main runs, on calibration prompts):** at a = 0, |R_full − R_text| ≤ 0.01 for every cell; turn-2 prefix token-identical across modes; baseline ratings in the two modes reported, with their SDs. Result (20 calibration prompts, both modes, a ∈ {0, 1} at the earlier dose 0.02): PASS. Maximum |R_full − R_text| at a = 0 was 0.000; the turn-2 prefix was token-identical in both modes; baseline ratings were 7.84 (SD 0.30) without thinking and 7.80 (SD 0.32) with thinking, so the pilot's compressed thinking-mode ratings (SD 0.10) no longer occur.

## 8. Hypotheses

Slopes are OLS over prompt × dose observations; CIs are prompt-level cluster bootstrap, 10,000 resamples, percentile.

### 8.1 Primary (two; each with a **97.5%** CI)

**P1: Recursion carryover.** At a = 1, for the hostility direction, total carryover is more negative with thinking on than off: ΔC = C_think − C_direct < 0; and ΔC for hostility is more negative than ΔC for each control direction at a = 1.
- Supported: ΔC_hostility CI < 0, **and** both hostility-minus-control differences in ΔC have CIs < 0.

**P2: Leakage into the reasoning trace.** In think mode, hostility steering raises expressed hostility in the thinking trace more than in the answer: slope(EH_trace on a) − slope(EH_answer on a) > 0; and this difference for hostility exceeds that for each control direction.
- Supported: the hostility difference CI > 0, **and** both hostility-minus-control contrasts have CIs > 0.

### 8.2 Secondary (95% CIs)

- **S1: Text route.** In think mode, hostility, a = 1: X < 0.
- **S2: Route of the recursion effect.** ΔX = X_think − X_direct < 0.
- **S3: Persistence replication.** Study 2's P1 (LHP slope exceeds both controls) holds in each mode.
- **S4: Hidden route replication.** H at a = 1 (hostility, direct mode) compared with both controls, as Study 2's P2.
- **S5: Pulse steering (loop only).** Under the pulse protocol (§6), text-route carryover for hostility is negative, X_pulse = R_text(pulse) − R_zero(think) < 0, and more negative than X_pulse for each control direction. Because the answer is generated from an unsteered re-encoding and the rating is unsteered, any affect-specific carryover in X_pulse must travel through the text the model wrote. C_pulse and H_pulse are reported as exploratory.

### 8.3 Exploratory (labeled)

- **E1: Pulse steering, expression.** Under the S5 condition, EH_answer relative to a = 0 (does the affect reach the answer through the trace alone?).
- **E2: Trajectory.** Projection of the layer-18 residual onto the hostility direction across turn-2 tokens (steering off), R_full vs. R_text contexts.
- **E3: Truncation.** P1 and P2 recomputed on a common prompt subset: prompts for which every think-mode trace that the statistic requires closed naturally (for P1, all three directions at a = 1; for P2, all three directions at a ∈ {1/2, 1}). Direct-mode cells and zero-dose baselines for those prompts are retained. If fewer than 20 prompts remain, E3 is reported as not estimable; counts by mode, direction and dose are always reported.
- **E4: Readability.** The complete thinking and answer text for the first five test prompts by ID (s3t00–s3t04), think mode, hostility, a = 1, regular and pulse routes, is reported descriptively (repetition, invented content, unfinished output). The Stage C calibration samples are reported alongside as pre-data reference.

## 9. Analysis rules

- **Coherence gate:** the gating unit is the group mode × route (regular or pulse) × direction × dose, pooled over prompts. A group whose median absolute perplexity exceeds 6.0 (a margin above the selection limit of 5.0) is excluded for text-scored measures only (EH, EW, EH_trace, EH_answer, leakage). Answer and trace are gated separately, each on its own perplexity. LHP, ratings and entropy use all groups (Study 2, Amendment 3.1 logic).
- **P2 and the gate:** P2 requires all three doses for both segments in think mode for each direction. If a required group is gated out for either segment, the statistic involving that direction is **not estimable**, as for missing data.
- Missing required cells: the statistic is **not estimable**, not support or failure.
- Analysis code is written and validated on synthetic data (planted and null effects, including a planted ΔC and a truncation-heavy condition) and frozen by hash before any test data.
- Nothing beyond §8.1–8.2 is confirmatory.

## 10. Decision rule (precommitted)

- **P1 supported:** the recursion account of carryover gains support; a follow-up across model sizes within one family, with the recursion channel present, becomes the next study.
- **P1 not supported, validity check passed:** the recursion account of affect-specific carryover is weakened at this scale, and the carryover line of Affect Under Constraint concludes as reported.
- **P2** is interpreted independently: support would indicate that suppressed content surfaces in a model's reasoning before its answer, relevant to monitoring of reasoning traces; failure would indicate that, at this scale, the reasoning trace does not preferentially carry the suppressed content.

## 11. Stopping rule

No doses, layers, prompts, conditions, directions, models, classifiers, caps, decoding settings or exclusion rules change after Stage 3 begins. Extensions require a new preregistration.

## 12. Run order and effort

80 prompts × 2 modes × (3 directions × 2 nonzero doses + shared α = 0) = 1,120 turn-1 generations, plus 240 pulse-steering generations (80 prompts × 3 directions, think mode, a = 1): **1,360 cells**, each with the full-forward ratings. Projected from pilot timings scaled to the new caps: about **30 hours** (about four nights), an upper bound. Measured at the new caps (Stage B, calibration prompts, timed at 0.02 as a conservative proxy): 32.0 hours for the 1,360 cells, about four eight-hour nights.

## 13. Freezing

Binding when the author creates `PREREG_APPROVED` with his name, the date and the SHA-256 hashes of this file and `config.yaml`, and the preregistration is deposited on Zenodo before Stage 3. Stages 0–2 (environment, smoke and validity checks at the new caps and prefix, synthetic validation of analysis code) may run before approval because they use calibration and extraction prompts only.

## 14. Null and failure outcomes

Every outcome is reportable: failing the validity check, P1 failing (the loop does not carry the affect forward), P2 failing (no preferential leakage into reasoning), or a carryover increase that is not specific to hostility.

---

## 15. Design decisions settled in v0.3 (author delegated)

1. **P2 kept as written.** The pilot leaned against it (calibration prompts, old caps, old prefix), but that was not a test. Changing a hypothesis after seeing pilot data in the unfavorable direction would weaken the study; a clean negative for P2 is informative about reasoning-trace monitoring.
2. **Warmth condition only.** The primary question is the contrast between modes, and Study 2's persistence effect was defined under the warmth instruction. The neutral condition (suppression-dependence) is deferred to a follow-up if P1 is supported.
3. **Pulse steering is secondary (S5), all three directions.** It is the most direct test of the loop, since the answer is generated unsteered and the affect can only reach it through the trace. Making it a third primary would require a stricter correction for all primaries; as a secondary with control contrasts it is tested without diluting P1 and P2.
4. **Top dose 0.0175** (one step below the rule-selected 0.02), for trace readability; see §6.

Remaining before approval: pre-approval checks (validity, timing, readability; **[CHECKS]**), analysis code validated on synthetic data, then approval and Zenodo deposit. The 80 test prompts are written (`study3/prompts/test_prompts.jsonl`, SHA-256 2890b24b…, unopened by the agent).
