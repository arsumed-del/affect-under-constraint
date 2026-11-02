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
