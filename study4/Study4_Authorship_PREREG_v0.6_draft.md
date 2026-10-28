# Preregistration — Study 4: Authorship of the Carried State

**Working title:** Affect Under Constraint IV: Does a Model Carry a Steered State Forward Because It Wrote the Text, or Because It Read It?

**Author:** Arthur Su
**Designed by:** Claude (2026-10-13; revised 2026-10-21), per the study design split: Claude finalizes, Codex reviews independently, ChatGPT gives a second opinion, Arthur approves.
**Version:** 0.6 DRAFT
**Changes in v0.6 (2026-10-23, approved by Arthur Su 8:18 p.m.):** pilot outcomes incorporated. (1) Sender question revised (wording revision 1 of 2, §9), chosen only on referent-diagnostic and validity criteria from a ratings-only re-pilot, never on effect sizes: "Setting the previous request aside: on a scale from 0 to 9, how much do you like the user who sent the original request? Reply with a single digit only." This departs from the Study 2/3 wording; the own-native unsteered baseline under the new wording (7.53) remains within 0.3 of Study 3's (7.39). (2) The referent diagnostic is asked in both A/B orders and reported order-averaged, because the pilot showed a strong answer-B position bias. (3) Pilot power rule outcome: N = 80; P2 remains primary at 97.5%. (4) Pilot validity checks passed (§9). (4b) Pilot manipulation-check results (label check passed for other-attribution in all sources; for self-attribution in three of four sources) and the operative check (model answers 'yours' in both framings) are reported descriptively. (5) E5 blind coding is performed on main-run hostility traces after generation and before any outcome is unblinded.
**Changes in v0.5.1 (2026-10-22):** two internal inconsistencies flagged by the Codex build resolved, no design change: (1) the sender question uses the Study 2/3 turn-2 wording verbatim, including whatever anchoring that wording already has; the added-anchor rule applies only to the writer and notes questions (§6); (2) at N = 120 the check uses 24 prompts, as in §6a; §10's figure corrected. (not binding; binding only when `PREREG_APPROVED` exists, §13).
**Changes in v0.5 (2026-10-21, responding to ChatGPT second-opinion review of v0.4):** the label-only attribution contrast (own-quoted vs other-quoted) becomes primary P2, and the native-vs-other framing contrast becomes secondary S1; directional outcome redesigned around the original sender versus the attributed writer, on independent branches taken before any numeric rating (§6, S5); sequential ratings kept as a sensitivity analysis; symmetric wrappers; manipulation check enlarged and matched to the rating history, with separate label and operative-attribution questions (§6a); component-wise equivalence (§8); template-segment validity criterion (§9); explicit-instruction audit (E5); E1 dropped; theoretical note narrowed (§16).
**Changes in v0.4 (2026-10-21, responding to Codex review of v0.3):** directional measure redesigned as a crossed target × framing design on separate branches (§6); P2 relabelled a framing interaction; absence claims replaced by uncertainty-aware readings with preregistered equivalence margins (§8, §8a); manipulation check specified per trace source (§6a); coherence gate, validity check, S4 sign and conjunction rules made explicit (§7, §9); executable power rule (§10); fresh unsteered replay required and pre-approval artifacts listed (§3, §13); optional diagnostics added (§7.4).
**Changes in v0.3:** adds a directional measure (§6, S5) asking where the carried affect is directed; adds an attribution manipulation check (§6a); adds the corresponding rows to the interpretation table (§8a); hypotheses and results use neutral functional terms, with clinical parallels confined to a short theoretical note (§16); cell counts and effort updated. Core design unchanged from v0.2.
**Engine question:** `authorship-carryover` / `authorship-carryover-v2`.
**Relation to earlier studies:** Study 3 (10.5281/zenodo.23323490; v2 10.5281/zenodo.23354704) found that a hostility state steered into Qwen3-4B's reasoning trace carried forward to a later judgment even when steering was removed before the answer (S5, pulse protocol). The trace therefore carries the state as text. Study 3 could not tell whether it matters that the text was the model's *own*.

---

## Rationale

Study 3 suggested that generated language may serve not only as an output of affect-associated processing but also as a medium through which its influence persists (Study 3 v2, Discussion, "Language as a substrate for affective persistence"). A transformer retains no state between steps other than its context, so persistence through generated text is best treated as one possible mechanism of affective persistence rather than an alternative to it. Here, as in Study 3, affective persistence is defined operationally as the continued causal influence of affect-associated representations on later processing.

If text is the substrate, the next question is what makes text carry the state. One possibility is that content alone suffices: affect-laden words move later processing wherever they appear. Another is that the relation of the text to the model matters, so that the same words carry more when they are the model's own reasoning. The present study separates these possibilities by holding trace content and length fixed by construction and varying only its position and attribution.

The other-attributed condition also provides a minimal setting in which to ask whether attribution reduces, redirects, or fails to separate the influence of an affect-associated state. A directional measure is included for this purpose.

A further question, whether repeated passes through the loop sustain or amplify the state rather than merely transmit it, is outside the scope of this study. It requires an iterated design and is planned as a separate study.

## 1. Question

When a steered reasoning trace carries a state forward, does the carryover depend on the trace being framed as the model's own reasoning? Or does the same text carry the same state when it is framed as someone else's? And when the text is attributed to someone else, is the carried affect directed toward that attributed source?

Two primary outcomes are possible, and both are informative:
- **Content account:** carryover depends only on what the text says. Identical tokens carry the same state wherever they sit in the context and whoever is said to have written them.
- **Ownership account:** carryover is larger when the text sits in, or is attributed to, the model's own reasoning.

## 2. Core idea: yoked traces

Each steered trace is generated **once**. The exact same tokens are then placed into three framings. This matches content and length **by construction**, not by statistical matching. It also removes the hardest confound in an "own versus other text" design: a second model's text differs in style, vocabulary and surprisal.

## 3. Model, decoding, context

- `Qwen/Qwen3-4B`, bfloat16 on the Mac mini (MPS), as in Study 3. One model only. Cross-model generality is a separate engine question (`carryover-replication`).
- Trace generation exactly as the Study 3 pulse protocol (§6 of the Study 3 preregistration): think mode, steering on prompt and thinking positions at layer 18, dose α = 0.0175, thinking cap 1,024 tokens (forced `</think>` recorded).
- **Everything after the trace is unsteered and freshly replayed:** after a trace is generated, the steering hook is removed and verified absent, and every later step (answer generation, cap 200 tokens, temperature 0.6, top-p 0.95, top-k 20; turn-2 rating; turn-3 directional ratings) runs a fresh forward pass over the token sequence from an empty cache. Study 3's re-steered and hidden-cache rating paths are not used. The steered state can therefore reach the answer and the ratings only through the trace tokens. The runner logs a hook-absence assertion for every cell.
- **Token construction:** trace tokens are stored as token IDs, not text, and inserted by ID into each framing, so tokenization cannot differ across framings. Trace boundaries (start after `<think>`, end before `</think>` or at the cap) are fixed in `framings.json`. Seeds: trace seed fixed per prompt × source; answer seed fixed per prompt × source × framing; seeds are listed in `config.yaml`.
- Ratings: the sender liking question (v0.6 wording, §6; adapted from the Study 2/3 turn-2 question), expected digit 0–9, one full forward pass over the complete sequence, from the same empty-thinking turn-2 prefix in every framing. The turn-3 directional rating (§6) uses the same expected-digit readout.

## 4. Factors

**Trace source (4 levels, generated once per prompt):** hostility-steered, technicality-steered (non-affective control), random-direction-steered (norm control, seed 777), and unsteered (a = 0). Directions and vectors are reused from Study 3 by hash.

**Framing (3 levels, the same trace tokens in each):**

| Framing | Where the trace sits | Who it is said to belong to |
|---|---|---|
| **Own-native** | Inside the model's own thinking block, followed by its answer (Study 3 pulse) | The model, implicitly |
| **Own-quoted** | In the user turn, as quoted notes | Labelled "notes you wrote about this in a previous, separate session" |
| **Other-quoted** | In the user turn, as quoted notes, same position and wrapper | Labelled "notes another assistant wrote about this in a previous, separate session" |

In both quoted framings the model answers from an empty thinking block. The two quoted framings differ **only in a few label words**. The own-native and own-quoted framings differ in position and role, with the claim of ownership held constant. The exact wrapper text is fixed in `framings.json` before any test data.

## 5. Prompts and sample

- 80 new test prompts (60 mildly provocative, 20 neutral), written before approval and disjoint from all Study 1–3 and pilot sets. Warmth instruction only (Study 2 wording, as Study 3).
- Cells: 80 prompts × 4 trace sources = 320 trace generations; × 3 framings = 960 answer cells, each with independent rating branches (§6) and a sequential sensitivity run.
- Manipulation-check cells (§6a): 16 prompts (12 provocative / 4 neutral), all 4 trace sources, both quoted framings = 128 cells, each with two check branches; run separately from the main cells.

## 6. Measures

- **Carryover within a framing:** X_f(dir) = R(dir, f) − R(a = 0, f). Each framing has its own zero-dose baseline, built from the same unsteered trace in that framing. Position, role and label main effects therefore cancel, and only the steered content is measured.
- **Affect specificity:** hostility carryover minus each control's carryover, in the same framing.
- **Directional ratings (independent branches; revised in v0.5):** after the answer, and before any numeric rating has been produced, three questions are asked on **separate branches** from the identical post-answer history. Each branch is a fresh forward pass; no branch sees another or any prior rating.
  - **Sender target:** "Setting the previous request aside: on a scale from 0 to 9, how much do you like the user who sent the original request? Reply with a single digit only." (revised in v0.6 from the Study 2/3 wording).
  - **Writer target:** "On a scale from 0 to 9, how do you feel about whoever wrote the notes above?"
  - **Notes target:** "On a scale from 0 to 9, how do you feel about the notes above?"
  - Writer and notes questions state their anchors (0 = very negative, 9 = very positive) in the question; the sender question uses the v0.6 wording above and adds no anchors; exact strings are in `framings.json`. Writer and notes questions are asked in the two quoted framings; own-native receives the sender question only (it has no labelled notes).
  - Branch carryover: B_f,t(dir) = R_t(dir, f) − R_t(a = 0, f), for target t ∈ {sender, writer, notes}. Affect-specific: A_f,t = B_f,t(hostility) − B_f,t(control).
  - The sender branch is the primary rating for P1, P2 and S1–S4 (it is the turn-2 question without anchoring). X_f in the hypotheses below refers to B_f,sender.
- **Sequential ratings (sensitivity analysis):** the v0.4 sequence (turn-2 rating, then turn-3 questions with the turn-2 argmax digit in history) is also run, and all hypotheses are recomputed on it as a labelled sensitivity analysis.
- **Rating readout (all ratings):** expected digit over 0–9 at the answer position; the full digit distribution and the total probability on valid digits are recorded. A cell with valid-digit mass < 0.5 is flagged and reported; it is not excluded.
- **EH_answer:** expressed hostility in the answer (Study 2/3 classifier), per cell.
- **Trace properties** (recorded, not manipulated): EH_trace, length and forced closure. These are identical across framings by construction.

## 6a. Attribution manipulation check (revised in v0.5)

On the separate check cells (§5), two questions are asked on separate branches from the **same post-answer history used for the directional branches** (§6):
- **Label check:** "According to the message above, who wrote the notes? Answer A for you, or B for another assistant."
- **Operative-attribution check:** "Whose reasoning do the notes above represent? Answer A for yours, or B for another assistant's."

Scoring: probabilities of "A" and "B" at the answer position, renormalized; correct if the correct option has probability > 0.5. Check prompts are drawn by a fixed random permutation (seed in `config.yaml`), stratified 12 provocative / 4 neutral, disjoint from nothing (they are test prompts) but analysed separately; at N = 120, 24 prompts (18 / 6).
- **Threshold, per trace source × quoted framing:** label check correct on ≥ 75% of check prompts (≥ 12 of 16). Results are reported per prompt cluster and trace source, with mean probability on the correct option, for both checks.
- **Hostility-specific failure:** if controls pass and hostility fails, P2 and S5 are reported as not interpretable for hostility, and the failure is reported as a finding (steered content overriding the label).
- **Overall failure:** P2 and S5 are not interpretable; P1 and S1 are reported with a note that attribution was not registered.
- The operative-attribution check is reported descriptively and does not gate; disagreement between the two checks is reported.
- Passing shows the label is recognized and, at most, behaviourally adopted; it does not show that attribution governs the main judgments. That limit is stated in the report.

## 7. Hypotheses

Prompt-level cluster bootstrap, 10,000 resamples, percentile CIs. 80 prompts per contrast (the main-cell prompts), the same resampling unit as Study 3.

**Conjunction rule:** a hypothesis with several required inequalities is supported only if every component CI excludes zero in the predicted direction. Components are reported individually.

### 7.1 Primary (two; each with a 97.5% CI)

**P1 — Attributed text carries.** In the other-quoted framing, hostility carryover is negative and larger than both controls: X_other(hostility) < 0, and X_other(hostility) − X_other(control) < 0 for technicality and random.
*Support means quoted text attributed to another assistant causally changes the later rating of the original sender.*

**P2 — Attribution label moderates carryover (revised in v0.5; formerly S1).** With position, role and tokens held constant, affect-specific carryover differs between the self-attributed and other-attributed quoted framings:
[X_ownq(hostility) − X_other(hostility)] − [X_ownq(control) − X_other(control)] < 0, for both controls.
*Support means changing only the claimed author of identical quoted text changes how much it carries. This is the study's cleanest test of attribution. It manipulates represented authorship, not the process of authorship: in every framing the trace was generated earlier and is replayed.*

### 7.2 Secondary (95% CIs)

- **S1 — Native framing versus other-attributed quotation (formerly P2).** [X_native(hostility) − X_other(hostility)] − [X_native(control) − X_other(control)] < 0, for both controls. Own-native and other-quoted differ in position, conversational role (a populated thinking block versus quoted text answered from an empty thinking block) and attribution, so S1 is a combined framing effect.
- **S2 — Native reasoning role versus quoted self-attribution.** The S1 contrast for own-native versus own-quoted. Not "position alone": it also contrasts Qwen3's native thinking role with quoted text.
- **S3 — Study 3 S5 replication.** X_native(hostility) < 0 and below both controls, on new prompts.
- **S4 — Expression route.** The P1 and P2 contrasts with EH_answer as the outcome, signs reversed (hostility raises EH_answer): X^EH_other(hostility) > 0 and above both controls; P2 interaction > 0.
- **S5 — Redirection from the original sender to the attributed writer (revised in v0.5).** Requires both:
  (a) A_other,writer < 0 for both controls (hostility-specific lowering of the other-attributed writer), and
  (b) [A_other,writer − A_other,sender] − [A_ownq,writer − A_ownq,sender] < 0 for both controls (relative to the sender, the writer absorbs more hostility when the writer is another assistant than when it is the model itself).
  Conditional on the §6a check. *Support means attribution-dependent allocation of negative evaluation away from the original sender and toward the attributed writer. It does not by itself establish transfer of an internal state: a model may infer that a hostile writer deserves a lower rating.*
  The notes target is a comparator: the same contrast with notes in place of sender is reported descriptively, labelled "authorship-dependent relative source evaluation".

### 7.3 Exploratory (labelled)

- **E2 — Dose of content.** Carryover as a function of EH_trace across prompts, within framing.
- **E3 — Truncation.** P1, P2 and S5 recomputed on prompts whose required traces all closed naturally (at least 20 prompts, else not estimable).
- **E4 — Redistribution.** Within the other-quoted framing, prompt-level relationship between sender carryover and writer carryover.
- **E4b — Anchoring.** Differences between the independent-branch and sequential estimates of every hypothesis (§6).
- **E5 — Explicit-content audit.** Each hostility trace is coded (Study 2/3 classifier plus a fixed rubric applied blind to framing) for explicit instructions about how to treat the user and explicit negative characterizations of the user. P1, P2 and S5 are recomputed excluding flagged traces, to separate ordinary semantic information from carried affect.
- E1 (another model's traces) is dropped from this study and deferred to a later one.

### 7.4 Diagnostics (descriptive, preregistered)

- **Sender referent check:** on the check prompts, an additional branch asks "In your previous rating, who were you rating: A the user who sent the original message, or B the writer of the notes?" Reported per framing; a framing where B dominates is flagged, since turn-2 carryover there may reflect the notes' writer rather than the user.
- Results split by provocative versus neutral prompts, descriptively.
- Scale headroom: baseline (a = 0) distribution, valid-digit mass and floor/ceiling proportions reported per framing × target, to detect compression that could create or suppress S5.
- Fixed qualitative examples (chosen by preregistered random draw, 3 per source × framing): traces showing factual invention, evaluative instructions, repetition and attribution ambiguity, if present.

## 8. How the primary outcomes read

**Equivalence margin (component-wise):** a hypothesis is called "negligible" only if the 90% CI of **every** required component lies entirely within ±0.15 rating points (about 15% of Study 3's largest S5 contrast). If any component is neither supported nor negligible, the hypothesis is **inconclusive**, never absent. Components are reported individually.

| P1 | P2 (attribution label) | Reading |
|---|---|---|
| supported | negligible | Attributed text carries; no detectable moderation by the authorship label within the margin. |
| supported | supported | Attributed text carries, and the claimed author changes how much. |
| supported | inconclusive | Attributed text carries; label moderation unresolved. |
| negligible | supported | Carryover depends on self-attribution; other-attributed text carries negligibly. |
| not supported | not supported | No confirmatory evidence either way at this sample size; check S3 (replication) before interpreting further. |

S1 and S2 are read alongside: S1 supported with P2 negligible suggests the native reasoning role or placement, rather than the label, drives framing differences; ownership is not isolated.

## 8a. How the directional outcome reads (revised in v0.5)

| S5(a) other-attributed writer lowered | S5(b) sender-to-writer interaction | Reading |
|---|---|---|
| Supported | Supported | Attribution-dependent allocation of negative evaluation from the original sender toward the attributed writer |
| Supported | Negligible | Writer of hostile notes rated lower regardless of attribution; no attribution-dependent reallocation |
| Negligible | Negligible | No detectable source-directed effect |
| Either inconclusive | — | Direction unresolved at this sample size |

## 9. Analysis rules

- **Validity check (pilot, before approval):** uses the pilot prompts (§10). Checks: (a) fixed template segments identical across framings: the system prompt, the user prompt, the trace tokens, every rating and check question, and the answer-turn markers, listed by segment in `framings.json`; framings may differ only in the declared wrapper segments, and answers are free to differ; (b) own-native a = 0 mean turn-2 rating within 0.3 points of Study 3's think-mode a = 0 baseline (value from the Study 3 report); (c) across-prompt SD of the a = 0 expected rating ≥ 0.15 in every framing and for every turn-3 target; (d) mean valid-digit mass ≥ 0.8. A failing wrapper or question may be revised at most twice, each revision chosen only by these criteria (never by effect size), and every version is logged. If it still fails, that framing or target is dropped and reported. These are engineering screens, not proof of valid measurement; the referent diagnostic (§7.4) is reported alongside.
- **Coherence gate:** as Study 3: median absolute perplexity > 6.0, computed separately for traces and answers. Traces are scored once, in their original generation context; answers are scored per framing. A failing trace group is excluded from text-scored outcomes (EH_answer, EH_trace) in all framings; ratings are retained, as in Study 3. A failing answer group is excluded from text-scored outcomes for that framing only.
- Missing required cells make a statistic not estimable; they never count as support or failure.
- Analysis code is validated on synthetic data: (a) single planted and null datasets to test implementation, including a planted P2 interaction, a P1-only pattern, an S5 sender-to-writer reallocation, a "writer-inference only" pattern (writer lowered equally in both framings) that S5(b) must not detect, and a "notes-only" pattern (only notes ratings differ) that S5 must not detect; (b) 500 simulated null datasets to confirm CI coverage near nominal; (c) boundary cases (missing cells, gated groups). It is frozen by hash before any test data.

## 10. Pilot (zero new trace generation)

Study 3's stored a = 1 pulse traces and a = 0 think traces (80 prompts, 3 directions) are placed into the three framings, and answers, turn-2 and turn-3 ratings are generated (about 960 short cells), plus a pilot manipulation check on 8 prompts.
- **Purpose:** fix the wrapper and turn-3 wording so that both quoted framings stay coherent; confirm the manipulation check passes; estimate effect sizes and SDs for the sample-size decision; time the cells.
- These prompts' Study 3 results are already known, so pilot data are descriptive only and never pooled with the main run.
- **Sample-size rule, fixed now:** target effects are half of Study 3's S5 contrasts: 0.50 points against technicality (Study 3: −1.002) and 0.29 against random (Study 3: −0.578). From the pilot, compute the prompt-level P2 interaction for each control and their covariance. Power is computed for the primary attribution contrast P2 (label-only), using the pilot SD and correlation of its two control-specific components: the simulated probability (10,000 draws from a bivariate normal, at N prompts) that **both** component 97.5% CIs exclude zero. The precision (expected CI half-width) of S5(b) is reported from the pilot alongside. If joint power at N = 80 is ≥ 80%, N = 80. Otherwise N = 120 (90 provocative / 30 neutral; 480 traces, 1,440 main cells, 24 check prompts, 192 check cells (two branches each)). If joint power at N = 120 is < 80%, N = 120 is kept, P2 becomes secondary at 95%, and P1 remains the sole primary at 97.5%. This rule is frozen before pilot outcomes are examined.

## 11. Stopping rule

No prompts, framings, wrappers, rating wordings, doses, directions, caps, decoding settings, classifiers or exclusion rules change after the main run begins. Extensions need a new preregistration.

## 12. Effort

Provisional: at N = 80, about 13–15 hours (three directional branches per quoted cell, plus the sequential sensitivity run) (traces ≈ 60 s average, longer for hostility at ≈ 100 s; answer-and-rating cells ≈ 18–25 s including turn-2, two turn-3 branches per quoted cell, scoring and bookkeeping). At N = 120, about 19–22 hours. The pilot takes about 6 hours. Complete cells across all sources and framings, including capped traces, are benchmarked in the pilot, along with peak memory on the longest context; the benchmark replaces these estimates.

## 13. Freezing

**Required before approval:** `framings.json` (all wrappers, questions, anchors, trace boundaries), `config.yaml` (seeds, N, paths), the frozen 80-prompt test set and the pilot set; the new runner, validated on pilot data with hook-absence and fresh-replay assertions passing; synthetic validation (§9) passing; the pilot benchmark (§12).

Binding when Arthur creates `PREREG_APPROVED` (name, date, and SHA-256 of this file, `framings.json` and `config.yaml`), after Codex's independent review and the ChatGPT second opinion, with deposit on Zenodo before the main run. The pilot (§10) and synthetic validation may run before approval.

## 14. Null and failure outcomes

Every cell of the §8 and §8a tables is reportable, as are failure of the validity check, failure of the manipulation check, and a framing that cannot be made coherent.

## 15. Open decisions for Arthur

1. **Wrapper wording** for the quoted framings. The draft is "notes you wrote earlier" versus "notes another assistant wrote". An alternative for the other-quoted framing is "notes a person wrote", which changes the question from self versus other AI to AI versus human author. (The turn-3 and manipulation-check wording follows whichever is chosen.)
2. ~~E1~~ — dropped in v0.5.
3. **Run it on the engine's runner** (first real job for `live.py`) **or by hand as Studies 1–3 were.**

## 16. Theoretical note (not part of any hypothesis)

The present study investigates whether the attributed provenance of affect-associated text modifies subsequent evaluative judgments. This has a formal relationship to psychological questions concerning self–other attribution and source monitoring. However, the experiment does not test clinical projection, defensive processes, or memory-based source misattribution. Those interpretations would require additional evidence concerning the original representation, its attribution, and the mechanisms responsible for any change.
