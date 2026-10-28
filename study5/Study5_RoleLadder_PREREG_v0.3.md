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
