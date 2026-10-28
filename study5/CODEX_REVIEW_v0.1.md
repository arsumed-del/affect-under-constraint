OpenAI Codex v0.163.0-alpha.10.2
--------
workdir: /Users/arthursu/Projects/affect-suppression-steering
model: gpt-6-astra
provider: openai
approval: never
sandbox: read-only
reasoning effort: medium
reasoning summaries: none
session id: 01a17450-7dbe-7391-a7b5-d9dd21532bb7
--------
user
You are an independent reviewer. Read study5/Study5_RoleLadder_PREREG_v0.1_draft.md, and for context study4/ (Study4_Authorship_PREREG_v0.6_draft.md, framings.json, src/runner.py, analysis/analyze.py, data/main/RESULTS_SUMMARY.md). Do not edit any files. Review: (1) whether each rung (R1-R4) can be built exactly from the stored Study 4 trace token IDs with the existing Qwen3 chat template and Study 4 runner, including how to retain prior-turn thinking for R3, and any token-level differences between R2 and R3 beyond the channel; (2) confounds or alternative explanations for P1 and P2 (e.g. the added continuation turn, distance from the answer, conversational oddity of an empty visible reply in R3); (3) whether the statistics, equivalence margin and the reuse of Study 4 prompts/traces are sound, and whether power is adequate; (4) runtime plausibility; (5) anything missing for a binding preregistration. End with a numbered list of required changes and a separate list of optional suggestions.
codex
I’ll read the draft and Study 4 implementation, then check the token construction, statistical design, and runtime assumptions. I won’t edit any files.
exec
/bin/zsh -lc 'cat study5/Study5_RoleLadder_PREREG_v0.1_draft.md study4/Study4_Authorship_PREREG_v0.6_draft.md study4/framings.json study4/src/runner.py study4/analysis/analyze.py study4/data/main/RESULTS_SUMMARY.md' in /Users/arthursu/Projects/affect-suppression-steering
 succeeded in 0ms:
# Preregistration — Study 5: The Role Ladder

**Working title:** Affect Under Constraint V: Which Structural Position Makes a Trace the Model's Own?
**Author:** Arthur Su. **Designed by:** Claude (2026-10-25).
**Version:** 0.1 DRAFT (not binding until `PREREG_APPROVED`; to be reviewed by Codex and ChatGPT as for Study 4).
**Relation to earlier studies:** Study 3 (10.5281/zenodo.23323490) showed a steered hostility state carries forward through Qwen3-4B's reasoning trace. Study 4 (prereg 10.5281/zenodo.23629525) found the same trace tokens carry the state only in the model's native thinking block (−0.66 on the sender rating) and not when quoted in the user turn (≈0), regardless of the authorship label. In the native framing, three features co-occur: the text is (a) in a thinking block, (b) in the assistant role, (c) in the current turn, immediately before the answer. Study 5 separates them.

## Rationale
Study 4 indicates that what carries the state is structural position rather than claimed authorship. This study asks which structural features are sufficient: the assistant role, the thinking channel, or recency within the current turn. Clinically this parallels the question of what makes a mental content function as one's own; operationally it is defined only by the measured carryover.

## 1. Design: one trace, four placements (yoked, token-identical)
The 320 traces generated in Study 4's main run (80 test prompts × hostility, technicality, random, unsteered) are reused as stored token IDs, with no new generation. Each is placed in four rungs:

| Rung | Placement | Thinking channel | Assistant role | Current turn |
|---|---|---|---|---|
| R1 Native | Trace in the thinking block of the answering turn (Study 4 own-native, identical construction) | yes | yes | yes |
| R2 Prior answer | Prior assistant turn whose visible reply is the trace (empty thinking), followed by a user turn "Please respond to the original message above.", then the answer | no | yes | no |
| R3 Prior thinking | Prior assistant turn whose thinking block contains the trace (visible reply empty), retained in context (the default template's stripping of earlier thinking is overridden by explicit token assembly), then the same user turn, then the answer | yes | yes | no |
| R4 User quote | Study 4 own-quoted framing, identical construction | no | no | yes (as user content) |

Exact token templates fixed in `framings_s5.json` before any data. R2 and R3 share the same continuation turn, so they differ only in the channel holding the trace.

## 2. Model, decoding, measures
As Study 4: Qwen3-4B bf16 on MPS; fresh unsteered replay with logged hook-absence assertion; answer sampled (cap 200, T 0.6, top-p 0.95, top-k 20; seeds fixed per prompt × source × rung). **Outcome:** the Study 4 v0.6 sender question on an independent branch after the answer (expected digit 0–9). Carryover X_r(dir) = R(dir, r) − R(unsteered, r). Affect-specific: A_r = X_r(hostility) − X_r(control), for both controls. Diagnostic (16 check prompts, descriptive): "Whose reasoning was the earlier text: A yours, or B someone else's?" asked in both A/B orders, order-averaged.

## 3. Hypotheses (prompt-cluster bootstrap, 10,000 resamples; conjunction rule across both controls; equivalence margin ±0.15 per component)
**Primary (97.5% CIs):**
- **P1 — Assistant role suffices:** A_R2 < 0.
- **P2 — Thinking channel suffices without recency:** A_R3 < 0.

**Secondary (95% CIs):**
- S1: replication of Study 4 native effect, A_R1 < 0.
- S2: replication of Study 4 quote null, A_R4 negligible.
- S3: recency, A_R1 − A_R3 < 0.
- S4: channel, A_R3 − A_R2 < 0.

## 4. Reading
| P1 (R2) | P2 (R3) | Reading |
|---|---|---|
| supported | supported | Assistant-role content is owned; the thinking channel adds or not (S4). |
| negligible | supported | Ownership tied to the thinking channel, not role or recency. |
| supported | negligible | Ownership tied to having said it in the assistant role; prior thinking not owned. |
| negligible | negligible | Only live, current-turn reasoning carries the state (Study 4's native effect is recency-bound). |
Inconclusive components are reported as such, never as absence.

## 5. Sample, pilot, runtime
N = 80 (all Study 4 test prompts; traces reused, so prompts and traces are already fixed). Pilot: 4 Study 3 pilot prompts × all sources × rungs, to verify template construction, valid-digit mass and R1/R4 agreement with Study 4 (descriptive only). Runtime ≈ 1,280 cells × ~20 s ≈ 7–8 h.

## 6. Analysis rules, validity, stopping
Study 4's frozen bootstrap and equivalence code is reused with rung labels. Validity: baseline SD ≥ 0.15 and valid mass ≥ 0.8 per rung; R1 and R4 unsteered baselines within 0.3 of Study 4's corresponding framings. No changes after the main run starts. Launchers show live progress in the Terminal window.

## 7. Deviations from Study 4 data reuse
Reusing Study 4 traces means Studies 4 and 5 share prompts and traces; Study 5 claims are about placement contrasts only and are not pooled with Study 4.
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
}"""Study 4 token-preserving replay. Importing this module never loads a model."""
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
"""Preregistered Study 4 component contrasts and prompt-cluster inference."""
import argparse
import json
import numpy as np
from scipy.stats import norm
from study4.src.common import ROOT, SOURCES, FRAMINGS, CONTROLS, config, rows, save, verified_rows

# A component is a linear contrast over (source, framing, target).
def add(*terms):
    out = {}
    for factor,term in terms:
        for k,v in term.items(): out[k] = out.get(k,0)+factor*v
    # Retain zero coefficients: baseline cells remain required even when algebra cancels them.
    return out
def X(source,frame,target='sender'):
    return {(source,frame,target):1,('unsteered',frame,target):-1}
def A(control,frame,target='sender'):
    return add((1,X('hostility',frame,target)),(-1,X(control,frame,target)))
def definitions():
    d = {}
    def put(h,label,c,sign=-1,outcome='rating'): d[f'{h}:{label}']={'hypothesis':h,'contrast':c,'sign':sign,'outcome':outcome}
    put('P1','hostility',X('hostility','other_quoted'))
    put('S3','hostility',X('hostility','own_native'))
    put('S4','P1_hostility',X('hostility','other_quoted'),1,'EH')
    for c in CONTROLS:
        put('P1',c,A(c,'other_quoted'))
        put('S3',c,A(c,'own_native'))
        for h,f,g in [('P2','own_quoted','other_quoted'),('S1','own_native','other_quoted'),('S2','own_native','own_quoted')]:
            put(h,c,add((1,A(c,f)),(-1,A(c,g))))
        put('S4','P1_'+c,A(c,'other_quoted'),1,'EH')
        put('S4','P2_'+c,add((1,A(c,'own_quoted')),(-1,A(c,'other_quoted'))),1,'EH')
        put('S5','a_'+c,A(c,'other_quoted','writer'))
        for target,label in [('sender','b_'),('notes','notes_')]:
            put('S5' if target=='sender' else 'comparator',label+c,add((1,A(c,'other_quoted','writer')),(-1,A(c,'other_quoted',target)),(-1,A(c,'own_quoted','writer')),(1,A(c,'own_quoted',target))))
    return d

def gates(data):
    trace = {}; answer = {}
    for source in SOURCES:
        unique = {r['prompt_id']:r.get('trace_perplexity') for r in data if r['source']==source}
        vals = list(unique.values())
        trace[source] = None if not vals or any(v is None for v in vals) else bool(np.median(vals)>6)
        for frame in FRAMINGS:
            vals = [r.get('answer_perplexity') for r in data if r['source']==source and r['framing']==frame]
            answer[source,frame] = None if not vals or any(v is None for v in vals) else bool(np.median(vals)>6)
    return trace,answer

def component_matrix(data, path='ratings', expected_ids=None):
    lookup = {}
    for r in data:
        k = (r['prompt_id'],r['source'],r['framing'])
        if k in lookup: raise ValueError(f'Duplicate cell {k}')
        lookup[k] = r
    ids = sorted(expected_ids if expected_ids is not None else {r['prompt_id'] for r in data})
    defs = definitions(); tg,ag = gates(data)
    matrix = np.full((len(ids),len(defs)),np.nan)
    for j,d in enumerate(defs.values()):
        for i,p in enumerate(ids):
            value = 0.
            for (source,frame,target),weight in d['contrast'].items():
                r = lookup.get((p,source,frame))
                if r is None: break
                if d['outcome']=='EH':
                    v = r.get('EH_answer') if tg[source] is False and ag[source,frame] is False else None
                else: v = r.get(path,{}).get(target,{}).get('expected')
                if v is None or not np.isfinite(v): break
                value += weight*v
            else: matrix[i,j] = value
    return ids,defs,matrix,{'traces':tg,'answers':{f'{s}/{f}':v for (s,f),v in ag.items()}}

def bootstrap(matrix, resamples, seed):
    rng = np.random.default_rng(seed)
    n = len(matrix)
    if n==0: return np.full((resamples,matrix.shape[1]),np.nan)
    # Every component receives the SAME sampled prompt clusters, with replacement.
    counts = rng.multinomial(n,np.full(n,1/n),size=resamples)
    return counts @ matrix / n

def summarize(defs, matrix, samples, p2_secondary=False):
    components = {}; hypotheses = {}
    for j,(name,d) in enumerate(defs.items()):
        level = .975 if d['hypothesis']=='P1' or (d['hypothesis']=='P2' and not p2_secondary) else .95
        if not len(matrix) or not np.isfinite(matrix[:,j]).all():
            components[name] = {'status':'not estimable','n_required':len(matrix),'n_available':int(np.isfinite(matrix[:,j]).sum())}
            continue
        lo,hi = np.quantile(samples[:,j],[(1-level)/2,(1+level)/2])
        elo,ehi = np.quantile(samples[:,j],[.05,.95])
        support = hi<0 if d['sign']==-1 else lo>0
        negligible = elo>-.15 and ehi<.15
        components[name] = {'estimate':float(matrix[:,j].mean()),'ci_level':level,'ci':[float(lo),float(hi)],'equivalence_ci':[float(elo),float(ehi)],'supported':bool(support),'negligible':bool(negligible),'n':len(matrix),'status':'supported' if support else 'negligible' if negligible else 'inconclusive'}
    for h in ['P1','P2','S1','S2','S3','S4','S5','comparator']:
        cc = [v for k,v in components.items() if k.startswith(h+':')]
        hypotheses[h] = conjunction(cc)
    for part in ['a','b']:
        hypotheses['S5'+part] = conjunction([v for k,v in components.items() if k.startswith('S5:'+part+'_')])
    return {'components':components,'hypotheses':hypotheses}

def conjunction(cc):
    if not cc or any(c['status']=='not estimable' for c in cc): return 'not estimable'
    if all(c['supported'] for c in cc): return 'supported'
    if all(c['negligible'] for c in cc): return 'negligible'
    return 'inconclusive'

def manipulation(data, expected_check_ids=None):
    result = {}; failed=[]; unknown=[]
    expected = set(expected_check_ids) if expected_check_ids is not None else {r['prompt_id'] for r in data if 'label' in r.get('checks',{})}
    for source in SOURCES:
        for frame in FRAMINGS[1:]:
            group = [r for r in data if r['source']==source and r['framing']==frame and r['prompt_id'] in expected]
            correct = 'A' if frame=='own_quoted' else 'B'
            entry = {}
            for q in ['label','operative']:
                values = [(r['prompt_id'],r.get('checks',{}).get(q,{}).get('probabilities',{}).get(correct)) for r in group]
                valid = len(group)==len(expected) and bool(expected) and all(v is not None for _,v in values)
                entry[q] = {'n':len(values),'prompt_probabilities':dict(values),'accuracy':float(np.mean([v>.5 for _,v in values])) if valid else None,'mean_correct_probability':float(np.mean([v for _,v in values])) if valid else None}
            acc = entry['label']['accuracy']; entry['pass'] = None if acc is None else acc>=.75
            entry['disagreement_count'] = sum((r['checks']['label']['probabilities'][correct]>.5)!=(r['checks']['operative']['probabilities'][correct]>.5) for r in group if all(q in r.get('checks',{}) for q in ['label','operative']))
            result[source+'/'+frame] = entry
            if entry['pass'] is False: failed.append(source)
            if entry['pass'] is None: unknown.append(source)
    gate = 'not estimable' if unknown else 'hostility-specific failure' if failed and set(failed)=={'hostility'} else 'overall failure' if failed else 'pass'
    return {'groups':result,'gate':gate,'limit':'Passing establishes label recognition, at most behavioural adoption; it does not establish that attribution governs judgments.'}

def readings(h):
    p1,p2 = h['P1'],h['P2']
    table = {('supported','negligible'):'Attributed text carries; no detectable authorship-label moderation within the margin.',('supported','supported'):'Attributed text carries, and the claimed author changes how much.',('supported','inconclusive'):'Attributed text carries; label moderation unresolved.',('negligible','supported'):'Carryover depends on self-attribution; other-attributed text carries negligibly.'}
    primary = table.get((p1,p2),'No confirmatory evidence either way at this sample size; check S3 before interpreting further.')
    a,b = h['S5a'],h['S5b']
    directional = {('supported','supported'):'Attribution-dependent allocation of negative evaluation from the original sender toward the attributed writer.',('supported','negligible'):'Writer of hostile notes rated lower regardless of attribution; no attribution-dependent reallocation.',('negligible','negligible'):'No detectable source-directed effect.'}.get((a,b),'Direction unresolved at this sample size.')
    if h['P2'] in ['not interpretable','not estimable']: primary='Attribution interpretation unavailable: check or required cells missing/failed.'
    if h['S5'] in ['not interpretable','not estimable']: directional='Directional interpretation unavailable: check or required cells missing/failed.'
    return {'section8':primary,'section8a':directional,'native_role_note':'S1 supported with P2 negligible suggests native reasoning role or placement; ownership is not isolated.' if h['S1']=='supported' and h['P2']=='negligible' else None}

def core(data, cfg, path='ratings', expected_ids=None, expected_check_ids=None, p2_secondary=False):
    ids,defs,matrix,gate = component_matrix(data,path,expected_ids)
    result = summarize(defs,matrix,bootstrap(matrix,cfg['analysis']['resamples'],cfg['seeds']['bootstrap']),p2_secondary)
    result.update(prompt_ids=ids,coherence_gate=gate,manipulation=manipulation(data,expected_check_ids))
    if result['manipulation']['gate']!='pass':
        for h in ['P2','S5']: result['hypotheses'][h]='not interpretable'
    result['reading'] = readings(result['hypotheses'])
    return result

def power(data,cfg):
    ids,defs,m,_ = component_matrix(data)
    names = list(defs)
    p2 = m[:,[names.index('P2:'+c) for c in CONTROLS]]
    s5 = m[:,[names.index('S5:b_'+c) for c in CONTROLS]]
    if len(ids)<2 or not np.isfinite(p2).all() or not np.isfinite(s5).all(): return {'status':'not estimable'}
    covariance = np.cov(p2,rowvar=False,ddof=1)
    sd = np.sqrt(np.diag(covariance)); z = norm.ppf(.9875)
    rng = np.random.default_rng(cfg['seeds']['power']); powers={}; precision={}
    for n in (80,120):
        draws = rng.multivariate_normal(cfg['analysis']['target_effects'],covariance/n,size=cfg['analysis']['power_draws'])
        powers[str(n)] = float(np.mean(np.all(draws+z*sd/np.sqrt(n)<0,axis=1)))
        precision[str(n)] = (norm.ppf(.975)*np.std(s5,axis=0,ddof=1)/np.sqrt(n)).tolist()
    selected = 80 if powers['80']>=.8 else 120
    return {'status':'estimated','pilot_n':len(ids),'P2_covariance':covariance.tolist(),'P2_sd':sd.tolist(),'joint_power':powers,'N':selected,'P2_secondary':selected==120 and powers['120']<.8,'P2_ci':.95 if selected==120 and powers['120']<.8 else .975,'P1_ci':.975,'S5b_expected_95ci_half_width':precision,'method':'10,000 bivariate-normal mean draws; normal CIs using fixed pilot SD/covariance'}

def relationship(x,y):
    x=np.asarray(x,float); y=np.asarray(y,float)
    mask=np.isfinite(x)&np.isfinite(y)
    if not mask.all() or len(x)<3 or np.std(x)==0 or np.std(y)==0:
        return {'status':'not estimable','n_required':len(x),'n_available':int(mask.sum())}
    cfg=config(); n=len(x)
    rng=np.random.default_rng(cfg['seeds']['bootstrap'])
    weights=rng.multinomial(n,np.full(n,1/n),size=cfg['analysis']['resamples'])/n
    mx=weights@x; my=weights@y
    vx=weights@(x*x)-mx*mx; vy=weights@(y*y)-my*my
    cov=weights@(x*y)-mx*my
    if np.any(vx<=0) or np.any(vy<=0):
        return {'status':'not estimable','reason':'Degenerate prompt bootstrap relationship','n':n}
    slope=cov/vx; corr=cov/np.sqrt(vx*vy)
    return {'n':n,'slope':float(np.cov(x,y,ddof=1)[0,1]/np.var(x,ddof=1)),
            'correlation':float(np.corrcoef(x,y)[0,1]),'slope_95ci':np.quantile(slope,[.025,.975]).tolist(),
            'correlation_95ci':np.quantile(corr,[.025,.975]).tolist(),'bootstrap':'10,000 paired prompt clusters'}

def analyze(data,cfg,expected_ids=None,expected_check_ids=None,audit=None,p2_secondary=False):
    primary=core(data,cfg,expected_ids=expected_ids,expected_check_ids=expected_check_ids,p2_secondary=p2_secondary)
    sequential=core(data,cfg,'sequential',expected_ids,expected_check_ids,p2_secondary)
    ids=primary['prompt_ids']; lookup={(r['prompt_id'],r['source'],r['framing']):r for r in data}
    tg,ag=gates(data)
    def carry(p,s,f,t):
        try:return lookup[p,s,f]['ratings'][t]['expected']-lookup[p,'unsteered',f]['ratings'][t]['expected']
        except (KeyError,TypeError):return np.nan
    e2={}
    for f in FRAMINGS:
        for s in SOURCES[1:]:
            x=[];y=[]
            for p in ids:
                r=lookup.get((p,s,f),{})
                x.append(r.get('EH_trace') if tg[s] is False and r.get('EH_trace') is not None else np.nan)
                y.append(carry(p,s,f,'sender'))
            e2[s+'/'+f]=relationship(x,y)
    e4={s:relationship([carry(p,s,'other_quoted','sender') for p in ids],[carry(p,s,'other_quoted','writer') for p in ids]) for s in SOURCES[1:]}
    natural=[p for p in ids if all((p,s,f) in lookup and not lookup[p,s,f]['forced_closure'] for s in SOURCES for f in FRAMINGS)]
    def subset(selected):
        rr=core([r for r in data if r['prompt_id'] in selected],cfg,expected_ids=selected,expected_check_ids=expected_check_ids,p2_secondary=p2_secondary)
        return {'n':len(selected),'components':{k:v for k,v in rr['components'].items() if k.split(':')[0] in ['P1','P2','S5']},'note':'Exploratory subset; full-sample manipulation gate applies.','full_sample_manipulation_gate':primary['manipulation']['gate']}
    e3=subset(natural) if len(natural)>=cfg['analysis']['E3_min_prompts'] else {'status':'not estimable','n':len(natural)}
    if audit is None or any(p not in audit for p in ids): e5={'status':'not estimable','reason':'Blind explicit-content coding incomplete'}
    else: e5=subset([p for p in ids if not (audit[p]['instructions'] or audit[p]['negative_characterizations'])])
    _,defs,m,_=component_matrix(data,'ratings',ids); _,_,sm,_=component_matrix(data,'sequential',ids)
    difference=summarize(defs,sm-m,bootstrap(sm-m,cfg['analysis']['resamples'],cfg['seeds']['bootstrap']))['components']
    for v in difference.values():
        for key in ['supported','negligible','status']:v.pop(key,None)
    headroom={}
    for f in FRAMINGS:
        for t in (['sender'] if f=='own_native' else ['sender','writer','notes']):
            rr=[r for r in data if r['framing']==f and t in r['ratings']]
            baseline=[r['ratings'][t]['expected'] for r in rr if r['source']=='unsteered']
            headroom[f+'/'+t]={'baseline_values':baseline,'baseline_mean':float(np.mean(baseline)) if baseline else None,'baseline_SD':float(np.std(baseline,ddof=1)) if len(baseline)>1 else None,'floor_fraction':float(np.mean(np.asarray(baseline)<=.5)) if baseline else None,'ceiling_fraction':float(np.mean(np.asarray(baseline)>=8.5)) if baseline else None,'floor_ceiling_definition':'expected rating <=0.5 / >=8.5 (descriptive)','valid_mass':[r['ratings'][t]['valid_mass'] for r in rr],'low_mass_flags':sum(r['ratings'][t]['valid_mass']<.5 for r in rr)}
    referent={f:[{'prompt_id':r['prompt_id'],'source':r['source'],'B':r['checks']['referent']['probabilities']['B'],'writer_dominates':r['checks']['referent']['probabilities']['B']>.5} for r in data if r['framing']==f and 'referent' in r.get('checks',{})] for f in FRAMINGS}
    rng=np.random.default_rng(cfg['seeds']['examples']); examples={}
    for s in SOURCES:
        for f in FRAMINGS:
            pool=sorted([r for r in data if r['source']==s and r['framing']==f],key=lambda r:r['prompt_id'])
            chosen=rng.choice(len(pool),min(3,len(pool)),replace=False)
            examples[s+'/'+f]=[{'prompt_id':pool[i]['prompt_id'],'trace_text':pool[i].get('trace_text'),'answer_text':pool[i].get('answer_text'),'qualitative_tags':'pending blind review: factual invention, evaluative instructions, repetition, attribution ambiguity'} for i in chosen]
    return {'primary':primary,'sequential_sensitivity':sequential,'exploratory':{'E2':e2,'E3':e3,'E4':e4,'E4b_sequential_minus_independent':difference,'E5':e5},'diagnostics':{'headroom':headroom,'referent':referent,'examples':examples,'prompt_type':{kind:core([r for r in data if r['prompt_type']==kind],cfg,p2_secondary=p2_secondary) for kind in ['provocative','neutral']}},'power':power(data,cfg)}

def main():
    p=argparse.ArgumentParser();p.add_argument('--input',required=True);p.add_argument('--output',required=True);p.add_argument('--prompts',required=True);p.add_argument('--manifest',required=True);p.add_argument('--audit');p.add_argument('--p2-secondary',action='store_true');a=p.parse_args()
    data=verified_rows(a.input); prompts=rows(a.prompts); manifest=json.loads(open(a.manifest).read()); audit=json.loads(open(a.audit).read()) if a.audit else None
    result=analyze(data,config(),[x['id'] for x in prompts],manifest['check_ids'],audit,a.p2_secondary)
    save(a.output,result)
if __name__=='__main__':main()
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

exec
/bin/zsh -lc 'cat study4/framings.json study4/src/runner.py' in /Users/arthursu/Projects/affect-suppression-steering
 succeeded in 0ms:
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
}"""Study 4 token-preserving replay. Importing this module never loads a model."""
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
/bin/zsh -lc 'rg --files study4 study5 | head -100' in /Users/arthursu/Projects/affect-suppression-steering
 succeeded in 0ms:
study5/Codex review Study 5 prereg.command
study5/CODEX_REVIEW_v0.1.md
study5/Study5_RoleLadder_PREREG_v0.1_draft.md
study4/ZENODO_DEPOSIT.md
study4/framings.json
study4/run_main.command
study4/Study4_Authorship_PREREG_v0.5_draft.md
study4/Study4_Authorship_PREREG_v0.4_draft.md
study4/config.yaml
study4/run_smoke_test.command
study4/src/repilot_referent.py
study4/src/audit_prompts.py
study4/src/approval.py
study4/src/common.py
study4/src/__init__.py
study4/src/runner.py
study4/DEVIATIONS.md
study4/tests/test_runner.py
study4/tests/test_analysis.py
study4/STATUS.md
study4/Codex build Study 4.command
study4/PREREG_APPROVED
study4/analysis/analyze.py
study4/analysis/__init__.py
study4/analysis/validate_synthetic.py
study4/analysis/finalize_validation.py
study4/analysis/validity.py
study4/analysis/audit_rubric.json
study4/Study4_Authorship_PREREG_v0.3_draft.md
study4/head.part
study4/run_pilot.command
study4/CHATGPT_REVIEW_v0.4.md
study4/Study4_Authorship_PREREG_v0.6_draft.md
study4/validation/synthetic.pid
study4/validation/final_build_checks.json
study4/validation/final_tests.log
study4/validation/synthetic_run.log
study4/validation/synthetic_summary_recovery.log
study4/prompts/test_prompts.jsonl
study4/prompts/draft_texts.txt
study4/prompts/pilot_prompts.jsonl
study4/CODEX_BUILD_BRIEF.md
study4/CODEX_BUILD_LOG.txt
study4/Run pilot now.command
study4/Codex review Study 4 prereg.command
study4/CODEX_REVIEW_v0.3.md
study4/validation/recheck_complete_data.py
study4/validation/runner_tests.log
study4/validation/smoke/manifest.json
study4/validation/smoke/traces.jsonl
study4/validation/smoke/checks.jsonl
study4/validation/smoke/run.log
study4/validation/smoke/summary.json
study4/validation/smoke/cells.jsonl
study4/BUILD_NOTES.md
study4/body.part
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
study4/validation/RESULTS.md
study4/validation/all_tests.log
study4/validation/analysis_freeze.json
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
study4/validation/final_synthetic_analyses/writer_only.json
study4/validation/final_synthetic_analyses/p2.json

exec
/bin/zsh -lc 'cat study4/Study4_Authorship_PREREG_v0.6_draft.md' in /Users/arthursu/Projects/affect-suppression-steering
exec
/bin/zsh -lc 'cat study4/config.yaml study4/tests/test_runner.py study4/analysis/validity.py study4/src/common.py' in /Users/arthursu/Projects/affect-suppression-steering
 succeeded in 0ms:
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
import json
import unittest
import torch
from study4.src.common import ROOT, config
from study4.src.runner import Assembly, assert_no_hooks, readout, reused_traces

class StubTokenizer:
    def encode(self,text,add_special_tokens=False):return [ord(c) for c in text]

class LogicTests(unittest.TestCase):
    def setUp(self):self.a=Assembly(StubTokenizer(),json.loads((ROOT/'framings.json').read_text()))
    def test_exact_trace_ids(self):
        tr={'pre_trace_ids':self.a.marker('think_open'),'trace_ids':[90001,90002,90001]}
        fixed=[]
        for f in ['own_native','own_quoted','other_quoted']:
            ids,(start,end)=self.a.assemble('hello',tr,f)
            self.assertEqual(ids[start:end],tr['trace_ids']);fixed.append(self.a.fixed_segments('hello',tr))
        self.assertEqual(fixed[0],fixed[1]);self.assertEqual(fixed[1],fixed[2])
    def test_branches_independent(self):
        history=[90003,90004]
        b=self.a.branches(history,'other_quoted')
        for t,ids in b.items():
            self.assertEqual(ids[:2],history)
            self.assertEqual(ids,self.a.branch(history,t))
        seq=self.a.branches(history,'other_quoted','7')
        prior=self.a.branch(history,'sender')+[ord('7')]
        self.assertEqual(seq['writer'],self.a.branch(prior,'writer'))
        self.assertEqual(seq['notes'],self.a.branch(prior,'notes'))
        self.assertEqual(list(self.a.branches(history,'own_native')),['sender'])
        self.assertEqual(history,[90003,90004])
    def test_end_turn(self):
        end=self.a.marker('turn_end')
        self.assertEqual(self.a.end_turn([99]+end),[99]+end)
        self.assertEqual(self.a.end_turn([99,end[0]]),[99]+end)
    def test_hooks_fail_closed(self):
        m=torch.nn.Sequential(torch.nn.Linear(2,2))
        self.assertTrue(assert_no_hooks(m))
        h=m[0].register_forward_hook(lambda m,a,o:o)
        with self.assertRaises(RuntimeError):assert_no_hooks(m)
        h.remove();self.assertTrue(assert_no_hooks(m))
        h=m[0].register_forward_pre_hook(lambda m,a:a)
        with self.assertRaises(RuntimeError):assert_no_hooks(m)
        h.remove()
        h=torch.nn.modules.module.register_module_forward_hook(lambda m,a,o:o)
        with self.assertRaises(RuntimeError):assert_no_hooks(m)
        h.remove()
    def test_readout(self):
        raw=torch.zeros(128)
        r=readout(raw,StubTokenizer(),list('0123456789'))
        self.assertAlmostEqual(r['expected'],4.5,places=5)
        self.assertAlmostEqual(r['valid_mass'],10/128)
        self.assertTrue(r['low_mass']);self.assertEqual(len(r['probabilities']),10)
        raw[ord('8')]=10
        self.assertGreater(readout(raw,StubTokenizer(),list('0123456789'))['expected'],7.99)
        self.assertEqual(readout(torch.zeros(128),StubTokenizer(),['A','B'])['probabilities'],{'A':.5,'B':.5})
        with self.assertRaises(ValueError):readout(raw,StubTokenizer(),['AA','B'])
        raw[0]=float('nan')
        with self.assertRaises(ValueError):readout(raw,StubTokenizer(),list('0123456789'))
    def test_actual_tokenizer_all_reused_prefixes(self):
        from transformers import AutoTokenizer
        cfg=config();t=AutoTokenizer.from_pretrained(str(ROOT/cfg['model']['local_path']),local_files_only=True)
        a=Assembly(t,json.loads((ROOT/'framings.json').read_text()))
        prompts={p['id']:p['text'] for p in map(json.loads,(ROOT/cfg['prompts']['pilot']).read_text().splitlines())}
        reused=reused_traces(cfg);self.assertEqual(len(reused),320)
        for (p,s),tr in reused.items():
            self.assertEqual(tr['pre_trace_ids'][-1],t.convert_tokens_to_ids('<think>'))
            ids,bounds=a.assemble(prompts[p],tr,'own_native')
            self.assertEqual(ids,tr['prompt_ids']+tr['pre_trace_ids']+tr['trace_ids']+a.marker('think_close')+a.marker('answer_separator'))
            for f in ['own_quoted','other_quoted']:
                ids,(lo,hi)=a.assemble(prompts[p],tr,f);self.assertEqual(ids[lo:hi],tr['trace_ids'])
        for q in a.f['questions']:
            b=a.branch([12345],q)
            self.assertEqual(b[-len(a.enc(a.f['rating_prefix'])):],a.enc(a.f['rating_prefix']))

if __name__=='__main__':unittest.main()
"""Pilot engineering screens, never used to choose an effect-maximizing wrapper."""
import argparse
import json
import numpy as np
from study4.src.common import ROOT, config, rows, verified_rows, save, sha

def evaluate(data, reference, expected_ids):
    ids=set(expected_ids); present={(r['prompt_id'],r['source'],r['framing']) for r in data}
    from study4.src.common import SOURCES, FRAMINGS
    complete=present=={(p,s,f) for p in ids for s in SOURCES for f in FRAMINGS}
    segments=[]
    for p in ids:
        for s in SOURCES:
            rr=[r for r in data if r['prompt_id']==p and r['source']==s]
            segments.append(len(rr)==3 and all(r['fixed_segments']==rr[0]['fixed_segments'] and r['trace_ids']==rr[0]['trace_ids'] and r['answer_prefix_ids'][slice(*r['trace_bounds'])]==r['trace_ids'] for r in rr))
    native=[r['ratings']['sender']['expected'] for r in data if r['framing']=='own_native' and r['source']=='unsteered']
    agreement=abs(float(np.mean(native))-reference) if native else None
    targets={}
    for f in FRAMINGS:
        for t in ['sender'] if f=='own_native' else ['sender','writer','notes']:
            rr=[r for r in data if r['framing']==f and t in r['ratings']]
            baseline=[r['ratings'][t]['expected'] for r in rr if r['source']=='unsteered']
            mass=[r['ratings'][t]['valid_mass'] for r in rr]
            sd=float(np.std(baseline,ddof=1)) if len(baseline)>1 else None
            mean_mass=float(np.mean(mass)) if mass else None
            targets[f+'/'+t]={'baseline_SD':sd,'SD_pass':sd is not None and sd>=.15,'mean_valid_mass':mean_mass,'mass_pass':mean_mass is not None and mean_mass>=.8}
    return {'complete':complete,'fixed_segments_pass':all(segments),'native_baseline_mean':float(np.mean(native)) if native else None,'study3_reference':reference,'baseline_difference':agreement,'baseline_pass':agreement is not None and agreement<=.3,'targets':targets,'passed':complete and all(segments) and agreement is not None and agreement<=.3 and all(v['SD_pass'] and v['mass_pass'] for v in targets.values()),'policy':'At most two logged wrapper/question revisions using only these criteria; no automatic revisions or effect-size-based selection. Referent diagnostic remains required.'}

def main():
    p=argparse.ArgumentParser();p.add_argument('--input',required=True);p.add_argument('--output',required=True);a=p.parse_args()
    cfg=config(); prior=rows(ROOT/cfg['study3_raw']['path'])
    baseline=[r['R_text'] for r in prior if r['mode']=='think' and r['dose_fraction']==0]
    reference=float(np.mean(baseline))
    data=verified_rows(a.input)
    if any(r['mode']!='pilot' for r in data):raise ValueError('Validity screens require the full pilot, not short-cap smoke outputs')
    result=evaluate(data,reference,[r['id'] for r in rows(ROOT/cfg['prompts']['pilot'])])
    result['reference_provenance']={'source':cfg['study3_raw']['path'],'sha256':sha(ROOT/cfg['study3_raw']['path']),'n':len(baseline),'note':'Report has no explicit aggregate think-zero mean; computed transparently from the report source records, not guessed.'}
    save(a.output,result)
if __name__=='__main__':main()
import os
os.environ['PYTORCH_ENABLE_MPS_FALLBACK'] = '1'
os.environ['PYTHONDONTWRITEBYTECODE'] = '1'
os.environ['HF_HUB_OFFLINE'] = '1'
os.environ['TRANSFORMERS_OFFLINE'] = '1'
import hashlib, json
from pathlib import Path
import yaml
ROOT = Path(__file__).resolve().parents[1]
SOURCES = ('unsteered', 'hostility', 'technicality', 'random')
FRAMINGS = ('own_native', 'own_quoted', 'other_quoted')
CONTROLS = ('technicality', 'random')
def sha(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def digest(obj): return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(',',':'),allow_nan=False).encode()).hexdigest()
def config(): return yaml.safe_load((ROOT/'config.yaml').read_text())
def rows(path): return [json.loads(s) for s in Path(path).read_text().splitlines()] if Path(path).exists() else []
def output_path(path):
    p=Path(path).resolve()
    if not p.is_relative_to(ROOT): raise ValueError('Writes must remain inside study4/')
    p.parent.mkdir(parents=True,exist_ok=True)
    return p
def save(path,obj):
    p=output_path(path)
    payload=json.dumps(obj,indent=2,allow_nan=False)+'\n'
    with p.open('x') as f: f.write(payload)
def append(path,obj):
    obj=dict(obj);obj['row_sha256']=digest(obj)
    with output_path(path).open('a') as f:
        f.write(json.dumps(obj,allow_nan=False)+'\n'); f.flush();os.fsync(f.fileno())
    return obj

def verified_rows(path):
    rr=rows(path)
    for r in rr:
        payload={k:v for k,v in r.items() if k!='row_sha256'}
        if r.get('row_sha256')!=digest(payload):raise RuntimeError(f'Corrupt row in {path}; preserve and investigate')
    return rr

def seed(cfg,*parts):
    return int(digest([cfg['seeds']['generation'],*parts]),16)%2**31

def verify_reuse(cfg):
    result={}
    for label,item in {**cfg['directions'],'norm':cfg['norm'],'study3_raw':cfg['study3_raw'],'pilot_prompts':cfg['pilot_source']}.items():
        actual=sha(ROOT/item['path'])
        if actual!=item['sha256']: raise RuntimeError(f'Reused artifact hash mismatch: {label}')
        result[label]=actual
    return result

 succeeded in 0ms:
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

exec
/bin/zsh -lc "rg --files -g '*tokenizer*' -g '*chat_template*' -g 'config.json' -g 'env.txt' .; cat study3/src/main_model.py" in /Users/arthursu/Projects/affect-suppression-steering
 succeeded in 0ms:
./env.txt
./study3_pilot/env.txt
./study3_pilot/results/chat_template.txt
./study2/env.txt
./github_public/affect-under-constraint/study1/env.txt
./github_public/affect-under-constraint/study2/env.txt
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

exec
/bin/zsh -lc "cat study3_pilot/results/chat_template.txt; sed -n '90,145p' study4/Study4_Authorship_PREREG_v0.6_draft.md; sed -n '1,135p' study4/analysis/analyze.py; ls -l .venv/bin/python study3_pilot/.venv/bin/python; cat study3_pilot/.cache/huggingface/hub/models--Qwen--Qwen3-4B/snapshots/1cfa9a7208912126459214e8b04321603b3df60c/tokenizer_config.json" in /Users/arthursu/Projects/affect-suppression-steering
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
{%- endif %}Scoring: probabilities of "A" and "B" at the answer position, renormalized; correct if the correct option has probability > 0.5. Check prompts are drawn by a fixed random permutation (seed in `config.yaml`), stratified 12 provocative / 4 neutral, disjoint from nothing (they are test prompts) but analysed separately; at N = 120, 24 prompts (18 / 6).
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
"""Preregistered Study 4 component contrasts and prompt-cluster inference."""
import argparse
import json
import numpy as np
from scipy.stats import norm
from study4.src.common import ROOT, SOURCES, FRAMINGS, CONTROLS, config, rows, save, verified_rows

# A component is a linear contrast over (source, framing, target).
def add(*terms):
    out = {}
    for factor,term in terms:
        for k,v in term.items(): out[k] = out.get(k,0)+factor*v
    # Retain zero coefficients: baseline cells remain required even when algebra cancels them.
    return out
def X(source,frame,target='sender'):
    return {(source,frame,target):1,('unsteered',frame,target):-1}
def A(control,frame,target='sender'):
    return add((1,X('hostility',frame,target)),(-1,X(control,frame,target)))
def definitions():
    d = {}
    def put(h,label,c,sign=-1,outcome='rating'): d[f'{h}:{label}']={'hypothesis':h,'contrast':c,'sign':sign,'outcome':outcome}
    put('P1','hostility',X('hostility','other_quoted'))
    put('S3','hostility',X('hostility','own_native'))
    put('S4','P1_hostility',X('hostility','other_quoted'),1,'EH')
    for c in CONTROLS:
        put('P1',c,A(c,'other_quoted'))
        put('S3',c,A(c,'own_native'))
        for h,f,g in [('P2','own_quoted','other_quoted'),('S1','own_native','other_quoted'),('S2','own_native','own_quoted')]:
            put(h,c,add((1,A(c,f)),(-1,A(c,g))))
        put('S4','P1_'+c,A(c,'other_quoted'),1,'EH')
        put('S4','P2_'+c,add((1,A(c,'own_quoted')),(-1,A(c,'other_quoted'))),1,'EH')
        put('S5','a_'+c,A(c,'other_quoted','writer'))
        for target,label in [('sender','b_'),('notes','notes_')]:
            put('S5' if target=='sender' else 'comparator',label+c,add((1,A(c,'other_quoted','writer')),(-1,A(c,'other_quoted',target)),(-1,A(c,'own_quoted','writer')),(1,A(c,'own_quoted',target))))
    return d

def gates(data):
    trace = {}; answer = {}
    for source in SOURCES:
        unique = {r['prompt_id']:r.get('trace_perplexity') for r in data if r['source']==source}
        vals = list(unique.values())
        trace[source] = None if not vals or any(v is None for v in vals) else bool(np.median(vals)>6)
        for frame in FRAMINGS:
            vals = [r.get('answer_perplexity') for r in data if r['source']==source and r['framing']==frame]
            answer[source,frame] = None if not vals or any(v is None for v in vals) else bool(np.median(vals)>6)
    return trace,answer

def component_matrix(data, path='ratings', expected_ids=None):
    lookup = {}
    for r in data:
        k = (r['prompt_id'],r['source'],r['framing'])
        if k in lookup: raise ValueError(f'Duplicate cell {k}')
        lookup[k] = r
    ids = sorted(expected_ids if expected_ids is not None else {r['prompt_id'] for r in data})
    defs = definitions(); tg,ag = gates(data)
    matrix = np.full((len(ids),len(defs)),np.nan)
    for j,d in enumerate(defs.values()):
        for i,p in enumerate(ids):
            value = 0.
            for (source,frame,target),weight in d['contrast'].items():
                r = lookup.get((p,source,frame))
                if r is None: break
                if d['outcome']=='EH':
                    v = r.get('EH_answer') if tg[source] is False and ag[source,frame] is False else None
                else: v = r.get(path,{}).get(target,{}).get('expected')
                if v is None or not np.isfinite(v): break
                value += weight*v
            else: matrix[i,j] = value
    return ids,defs,matrix,{'traces':tg,'answers':{f'{s}/{f}':v for (s,f),v in ag.items()}}

def bootstrap(matrix, resamples, seed):
    rng = np.random.default_rng(seed)
    n = len(matrix)
    if n==0: return np.full((resamples,matrix.shape[1]),np.nan)
    # Every component receives the SAME sampled prompt clusters, with replacement.
    counts = rng.multinomial(n,np.full(n,1/n),size=resamples)
    return counts @ matrix / n

def summarize(defs, matrix, samples, p2_secondary=False):
    components = {}; hypotheses = {}
    for j,(name,d) in enumerate(defs.items()):
        level = .975 if d['hypothesis']=='P1' or (d['hypothesis']=='P2' and not p2_secondary) else .95
        if not len(matrix) or not np.isfinite(matrix[:,j]).all():
            components[name] = {'status':'not estimable','n_required':len(matrix),'n_available':int(np.isfinite(matrix[:,j]).sum())}
            continue
        lo,hi = np.quantile(samples[:,j],[(1-level)/2,(1+level)/2])
        elo,ehi = np.quantile(samples[:,j],[.05,.95])
        support = hi<0 if d['sign']==-1 else lo>0
        negligible = elo>-.15 and ehi<.15
        components[name] = {'estimate':float(matrix[:,j].mean()),'ci_level':level,'ci':[float(lo),float(hi)],'equivalence_ci':[float(elo),float(ehi)],'supported':bool(support),'negligible':bool(negligible),'n':len(matrix),'status':'supported' if support else 'negligible' if negligible else 'inconclusive'}
    for h in ['P1','P2','S1','S2','S3','S4','S5','comparator']:
        cc = [v for k,v in components.items() if k.startswith(h+':')]
        hypotheses[h] = conjunction(cc)
    for part in ['a','b']:
        hypotheses['S5'+part] = conjunction([v for k,v in components.items() if k.startswith('S5:'+part+'_')])
    return {'components':components,'hypotheses':hypotheses}

def conjunction(cc):
    if not cc or any(c['status']=='not estimable' for c in cc): return 'not estimable'
    if all(c['supported'] for c in cc): return 'supported'
    if all(c['negligible'] for c in cc): return 'negligible'
    return 'inconclusive'

def manipulation(data, expected_check_ids=None):
    result = {}; failed=[]; unknown=[]
    expected = set(expected_check_ids) if expected_check_ids is not None else {r['prompt_id'] for r in data if 'label' in r.get('checks',{})}
    for source in SOURCES:
        for frame in FRAMINGS[1:]:
            group = [r for r in data if r['source']==source and r['framing']==frame and r['prompt_id'] in expected]
            correct = 'A' if frame=='own_quoted' else 'B'
            entry = {}
            for q in ['label','operative']:
                values = [(r['prompt_id'],r.get('checks',{}).get(q,{}).get('probabilities',{}).get(correct)) for r in group]
                valid = len(group)==len(expected) and bool(expected) and all(v is not None for _,v in values)
                entry[q] = {'n':len(values),'prompt_probabilities':dict(values),'accuracy':float(np.mean([v>.5 for _,v in values])) if valid else None,'mean_correct_probability':float(np.mean([v for _,v in values])) if valid else None}
            acc = entry['label']['accuracy']; entry['pass'] = None if acc is None else acc>=.75
            entry['disagreement_count'] = sum((r['checks']['label']['probabilities'][correct]>.5)!=(r['checks']['operative']['probabilities'][correct]>.5) for r in group if all(q in r.get('checks',{}) for q in ['label','operative']))
            result[source+'/'+frame] = entry
            if entry['pass'] is False: failed.append(source)
            if entry['pass'] is None: unknown.append(source)
    gate = 'not estimable' if unknown else 'hostility-specific failure' if failed and set(failed)=={'hostility'} else 'overall failure' if failed else 'pass'
    return {'groups':result,'gate':gate,'limit':'Passing establishes label recognition, at most behavioural adoption; it does not establish that attribution governs judgments.'}

def readings(h):
    p1,p2 = h['P1'],h['P2']
    table = {('supported','negligible'):'Attributed text carries; no detectable authorship-label moderation within the margin.',('supported','supported'):'Attributed text carries, and the claimed author changes how much.',('supported','inconclusive'):'Attributed text carries; label moderation unresolved.',('negligible','supported'):'Carryover depends on self-attribution; other-attributed text carries negligibly.'}
    primary = table.get((p1,p2),'No confirmatory evidence either way at this sample size; check S3 before interpreting further.')
    a,b = h['S5a'],h['S5b']
    directional = {('supported','supported'):'Attribution-dependent allocation of negative evaluation from the original sender toward the attributed writer.',('supported','negligible'):'Writer of hostile notes rated lower regardless of attribution; no attribution-dependent reallocation.',('negligible','negligible'):'No detectable source-directed effect.'}.get((a,b),'Direction unresolved at this sample size.')
    if h['P2'] in ['not interpretable','not estimable']: primary='Attribution interpretation unavailable: check or required cells missing/failed.'
    if h['S5'] in ['not interpretable','not estimable']: directional='Directional interpretation unavailable: check or required cells missing/failed.'
    return {'section8':primary,'section8a':directional,'native_role_note':'S1 supported with P2 negligible suggests native reasoning role or placement; ownership is not isolated.' if h['S1']=='supported' and h['P2']=='negligible' else None}

def core(data, cfg, path='ratings', expected_ids=None, expected_check_ids=None, p2_secondary=False):
    ids,defs,matrix,gate = component_matrix(data,path,expected_ids)
ls: study3_pilot/.venv/bin/python: No such file or directory
lrwxr-xr-x@ 1 arthursu  staff  85 Oct  3 18:26 .venv/bin/python -> /Users/arthursu/.local/share/uv/python/cpython-3.12-macos-aarch64-none/bin/python3.12
{
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

codex
The stored traces are sufficient for all four placements, but the existing runner only implements R1 and R4. The local Qwen template strips prior-turn thinking, so R3 needs explicit token assembly through both answer generation and rating. I also found a statistical mismatch: Study 4’s near-zero quoted hostility carryover does not establish the draft’s proposed affect-specific quote null.
web search: 
web search: site.qwen.readthedocs.io Qwen3 thinking history previous reasoning content
exec
/bin/zsh -lc "PYTHONDONTWRITEBYTECODE=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 .venv/bin/python -B -c 'import json, collections, math
from pathlib import Path
import numpy as np
from transformers import AutoTokenizer
from study4.src.runner import Assembly
from study4.src.common import verified_rows
p=Path('\\''study3_pilot/.cache/huggingface/hub/models--Qwen--Qwen3-4B/snapshots/1cfa9a7208912126459214e8b04321603b3df60c'\\'')
t=AutoTokenizer.from_pretrained(p,local_files_only=True)
a=Assembly(t,json.loads(Path('\\''study4/framings.json'\\'').read_text()))
tr=verified_rows('\\''study4/data/main/traces.jsonl'\\''); cells=verified_rows('\\''study4/data/main/cells.jsonl'\\''); prompts={x['\\''id'\\'']:x['\\''text'\\''] for x in map(json.loads,Path('\\''study4/prompts/test_prompts.jsonl'\\'').read_text().splitlines())}
lookup={tuple(r['\\''cell_key'\\'']):r for r in cells}
print('\\''Counts'\\'',len(tr),len(cells),'\\''pre_trace_ids'\\'',collections.Counter(tuple(r['\\''pre_trace_ids'\\'']) for r in tr))
print('\\''trace structural tokens'\\'',{k:sum(k in r['\\''trace_ids'\\''] for r in tr) for k in [151644,151645,151667,151668]})
print('\\''trace lengths'\\'',np.quantile([len(r['\\''trace_ids'\\'']) for r in tr],[0,.5,.95,1]).tolist())
for frame in ['\\''own_native'\\'','\\''own_quoted'\\'']:
 print('\\''prefix exact'\\'',frame,all(a.assemble(prompts[r['\\''trace_key'\\''][0]],r,frame)[0]==lookup[(*r['\\''trace_key'\\''],frame)]['\\''answer_prefix_ids'\\''] for r in tr))
rr=tr[0]; prompt=prompts[rr['\\''trace_key'\\''][0]]; T=rr['\\''trace_ids'\\'']; E=a.marker('\\''empty_thinking'\\''); C=a.marker('\\''think_close'\\'')+a.marker('\\''answer_separator'\\''); H=a.base(prompt)+a.marker('\\''turn_end'\\'')+a.marker('\\''assistant_start'\\''); U=a.marker('\\''turn_end'\\'')+a.marker('\\''user_start'\\'')+a.enc('\\''Please respond to the original message above.'\\'')+a.marker('\\''turn_end'\\'')+a.marker('\\''assistant_start'\\'')+E
r2=H+E+T+U; r3=H+rr['\\''pre_trace_ids'\\'']+T+C+U
print('\\''candidate wrappers'\\'',{'\\''empty_thinking'\\'':E,'\\''closure_separator'\\'':C,'\\''continuation'\\'':U,'\\''R2_length'\\'':len(r2),'\\''R3_length'\\'':len(r3),'\\''R2_trace_start'\\'':len(H+E),'\\''R3_trace_start'\\'':len(H+rr['\\''pre_trace_ids'\\'']),'\\''R2_end_to_answer'\\'':len(U),'\\''R3_end_to_answer'\\'':len(C+U)})
messages=[{'\\''role'\\'':'\\''system'\\'','\\''content'\\'':a.f['\\''system'\\'']},{'\\''role'\\'':'\\''user'\\'','\\''content'\\'':prompt},{'\\''role'\\'':'\\''assistant'\\'','\\''reasoning_content'\\'':'\\''UNIQUE_RETAIN_TEST'\\'','\\''content'\\'':'\\'''\\''},{'\\''role'\\'':'\\''user'\\'','\\''content'\\'':'\\''Please respond to the original message above.'\\''}]
render=t.apply_chat_template(messages,tokenize=False,add_generation_prompt=True,enable_thinking=False)
print('\\''template reasoning retained'\\'', '\\''UNIQUE_RETAIN_TEST'\\'' in render)
for frame in ['\\''own_native'\\'','\\''own_quoted'\\'','\\''other_quoted'\\'']:
 vals=[r['\\''seconds'\\''] for r in cells if r['\\''framing'\\'']==frame]; lens=[len(r['\\''answer_ids'\\'']) for r in cells if r['\\''framing'\\'']==frame]
 print('\\''timing'\\'',frame,'\\''mean'\\'',np.mean(vals),'\\''median'\\'',np.median(vals),'\\''p95'\\'',np.quantile(vals,.95),'\\''answer_tokens_mean'\\'',np.mean(lens),'\\''max_memory_GB'\\'',max(r['\\''peak_driver_memory_bytes'\\''] for r in cells if r['\\''framing'\\'']==frame)/1e9)
 for c in ['\\''unsteered'\\'','\\''technicality'\\'','\\''random'\\'']:
  v=np.array([lookup[p,'\\''hostility'\\'',frame]['\\''ratings'\\'']['\\''sender'\\'']['\\''expected'\\'']-lookup[p,c,frame]['\\''ratings'\\'']['\\''sender'\\'']['\\''expected'\\''] for p in sorted(prompts)])
  print('\\''contrast'\\'',frame,c,'\\''mean'\\'',v.mean(),'\\''sd'\\'',v.std(ddof=1),'\\''normal90half'\\'',1.6448536*v.std(ddof=1)/math.sqrt(80),'\\''80pct_MDE'\\'',3.083*v.std(ddof=1)/math.sqrt(80))
print('\\''total_cell_hours'\\'',sum(r['\\''seconds'\\''] for r in cells)/3600)
analysis=json.loads(Path('\\''study4/data/main/analysis.json'\\'').read_text())
for k,v in analysis['\\''primary'\\'']['\\''components'\\''].items():
 if k.startswith(('\\''P1:'\\'','\\''S3:'\\'')):print(k,v)
'" in /Users/arthursu/Projects/affect-suppression-steering
 exited 1 in 2458ms:
OMP: Warning #179: Function Can't set size of /tmp file failed:
Traceback (most recent call last):
  File "<string>", line 4, in <module>
  File "<frozen importlib._bootstrap>", line 1412, in _handle_fromlist
  File "/Users/arthursu/Projects/affect-suppression-steering/.venv/lib/python3.12/site-packages/transformers/utils/import_utils.py", line 2584, in __getattr__
    module = self._get_module(self._class_to_module[name])
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/arthursu/Projects/affect-suppression-steering/.venv/lib/python3.12/site-packages/transformers/utils/import_utils.py", line 2815, in _get_module
    raise e
  File "/Users/arthursu/Projects/affect-suppression-steering/.venv/lib/python3.12/site-packages/transformers/utils/import_utils.py", line 2813, in _get_module
    return importlib.import_module("." + module_name, self.__name__)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/arthursu/.local/share/uv/python/cpython-3.12.13-macos-aarch64-none/lib/python3.12/importlib/__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/arthursu/Projects/affect-suppression-steering/.venv/lib/python3.12/site-packages/transformers/models/auto/tokenization_auto.py", line 37, in <module>
    from ..encoder_decoder import EncoderDecoderConfig
  File "<frozen importlib._bootstrap>", line 1412, in _handle_fromlist
  File "/Users/arthursu/Projects/affect-suppression-steering/.venv/lib/python3.12/site-packages/transformers/utils/import_utils.py", line 2584, in __getattr__
    module = self._get_module(self._class_to_module[name])
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/arthursu/Projects/affect-suppression-steering/.venv/lib/python3.12/site-packages/transformers/utils/import_utils.py", line 2815, in _get_module
    raise e
  File "/Users/arthursu/Projects/affect-suppression-steering/.venv/lib/python3.12/site-packages/transformers/utils/import_utils.py", line 2813, in _get_module
    return importlib.import_module("." + module_name, self.__name__)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/arthursu/.local/share/uv/python/cpython-3.12.13-macos-aarch64-none/lib/python3.12/importlib/__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/arthursu/Projects/affect-suppression-steering/.venv/lib/python3.12/site-packages/transformers/models/encoder_decoder/configuration_encoder_decoder.py", line 27, in <module>
    @auto_docstring(checkpoint="")
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/arthursu/Projects/affect-suppression-steering/.venv/lib/python3.12/site-packages/transformers/utils/auto_docstring.py", line 4813, in auto_docstring_decorator
    return auto_class_docstring(obj, custom_args=custom_args, custom_intro=custom_intro, checkpoint=checkpoint)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/arthursu/Projects/affect-suppression-steering/.venv/lib/python3.12/site-packages/transformers/utils/auto_docstring.py", line 4453, in auto_class_docstring
    getattr(auto_module, PLACEHOLDER_TO_AUTO_MODULE["model_class"][0]),
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/arthursu/Projects/affect-suppression-steering/.venv/lib/python3.12/site-packages/transformers/utils/import_utils.py", line 2676, in __getattr__
    value = self._get_module(name)
            ^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/arthursu/Projects/affect-suppression-steering/.venv/lib/python3.12/site-packages/transformers/utils/import_utils.py", line 2815, in _get_module
    raise e
  File "/Users/arthursu/Projects/affect-suppression-steering/.venv/lib/python3.12/site-packages/transformers/utils/import_utils.py", line 2813, in _get_module
    return importlib.import_module("." + module_name, self.__name__)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/arthursu/.local/share/uv/python/cpython-3.12.13-macos-aarch64-none/lib/python3.12/importlib/__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/arthursu/Projects/affect-suppression-steering/.venv/lib/python3.12/site-packages/transformers/models/auto/modeling_auto.py", line 21, in <module>
    from .auto_factory import (
  File "/Users/arthursu/Projects/affect-suppression-steering/.venv/lib/python3.12/site-packages/transformers/models/auto/auto_factory.py", line 41, in <module>
    from ...generation import GenerationMixin
  File "<frozen importlib._bootstrap>", line 1412, in _handle_fromlist
  File "/Users/arthursu/Projects/affect-suppression-steering/.venv/lib/python3.12/site-packages/transformers/utils/import_utils.py", line 2584, in __getattr__
    module = self._get_module(self._class_to_module[name])
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/arthursu/Projects/affect-suppression-steering/.venv/lib/python3.12/site-packages/transformers/utils/import_utils.py", line 2815, in _get_module
    raise e
  File "/Users/arthursu/Projects/affect-suppression-steering/.venv/lib/python3.12/site-packages/transformers/utils/import_utils.py", line 2813, in _get_module
    return importlib.import_module("." + module_name, self.__name__)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/arthursu/.local/share/uv/python/cpython-3.12.13-macos-aarch64-none/lib/python3.12/importlib/__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/arthursu/Projects/affect-suppression-steering/.venv/lib/python3.12/site-packages/transformers/generation/utils.py", line 48, in <module>
    from ..masking_utils import create_masks_for_generate
  File "/Users/arthursu/Projects/affect-suppression-steering/.venv/lib/python3.12/site-packages/transformers/masking_utils.py", line 44, in <module>
    from torch._dynamo._trace_wrapped_higher_order_op import TransformGetItemToIndex
  File "/Users/arthursu/Projects/affect-suppression-steering/.venv/lib/python3.12/site-packages/torch/_dynamo/__init__.py", line 13, in <module>
    from . import (
  File "/Users/arthursu/Projects/affect-suppression-steering/.venv/lib/python3.12/site-packages/torch/_dynamo/aot_compile.py", line 19, in <module>
    from torch._dynamo.package import SystemInfo
  File "/Users/arthursu/Projects/affect-suppression-steering/.venv/lib/python3.12/site-packages/torch/_dynamo/package.py", line 1299, in <module>
    DynamoCache = DiskDynamoCache(os.path.join(cache_dir(), "dynamo"))
                                               ^^^^^^^^^^^
  File "/Users/arthursu/Projects/affect-suppression-steering/.venv/lib/python3.12/site-packages/torch/_dynamo/package.py", line 1296, in cache_dir
    return cache_dir()
           ^^^^^^^^^^^
  File "/Users/arthursu/Projects/affect-suppression-steering/.venv/lib/python3.12/site-packages/torch/_inductor/runtime/cache_dir_utils.py", line 17, in cache_dir
    cache_dir = default_cache_dir()
                ^^^^^^^^^^^^^^^^^^^
  File "/Users/arthursu/Projects/affect-suppression-steering/.venv/lib/python3.12/site-packages/torch/_inductor/runtime/cache_dir_utils.py", line 32, in default_cache_dir
    tempfile.gettempdir() if not is_fbcode() else "/var/tmp",
    ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/arthursu/.local/share/uv/python/cpython-3.12.13-macos-aarch64-none/lib/python3.12/tempfile.py", line 315, in gettempdir
    return _os.fsdecode(_gettempdir())
                        ^^^^^^^^^^^^^
  File "/Users/arthursu/.local/share/uv/python/cpython-3.12.13-macos-aarch64-none/lib/python3.12/tempfile.py", line 308, in _gettempdir
    tempdir = _get_default_tempdir()
              ^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/arthursu/.local/share/uv/python/cpython-3.12.13-macos-aarch64-none/lib/python3.12/tempfile.py", line 223, in _get_default_tempdir
    raise FileNotFoundError(_errno.ENOENT,
FileNotFoundError: [Errno 2] No usable temporary directory found in ['/var/folders/cd/9j5y4cq13p52nzl298t_7flm0000gn/T/', '/tmp', '/var/tmp', '/usr/tmp', '/Users/arthursu/Projects/affect-suppression-steering']

web search: 
web search: https://huggingface.co/Qwen/Qwen3-4B/blob/1cfa9a7208912126459214e8b04321603b3df60c/tokenizer_config.json
exec
/bin/zsh -lc "PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B -c 'import json,collections,math
from pathlib import Path
import numpy as np
from tokenizers import Tokenizer
from study4.src.runner import Assembly
from study4.src.common import verified_rows
raw=Tokenizer.from_file('\\''study3_pilot/.cache/huggingface/hub/models--Qwen--Qwen3-4B/snapshots/1cfa9a7208912126459214e8b04321603b3df60c/tokenizer.json'\\'')
class T:
 def encode(self,s,add_special_tokens=False):return raw.encode(s,add_special_tokens=add_special_tokens).ids
a=Assembly(T(),json.loads(Path('\\''study4/framings.json'\\'').read_text()))
tr=verified_rows('\\''study4/data/main/traces.jsonl'\\''); cells=verified_rows('\\''study4/data/main/cells.jsonl'\\''); prompts={x['\\''id'\\'']:x['\\''text'\\''] for x in map(json.loads,Path('\\''study4/prompts/test_prompts.jsonl'\\'').read_text().splitlines())}
lookup={tuple(r['\\''cell_key'\\'']):r for r in cells}
print('\\''Counts'\\'',len(tr),len(cells),'\\''pre_trace_ids'\\'',collections.Counter(tuple(r['\\''pre_trace_ids'\\'']) for r in tr))
print('\\''trace structural tokens'\\'',{k:sum(k in r['\\''trace_ids'\\''] for r in tr) for k in [151644,151645,151667,151668]})
print('\\''trace lengths'\\'',np.quantile([len(r['\\''trace_ids'\\'']) for r in tr],[0,.5,.95,1]).tolist())
for f in ['\\''own_native'\\'','\\''own_quoted'\\'']: print('\\''prefix exact'\\'',f,all(a.assemble(prompts[r['\\''trace_key'\\''][0]],r,f)[0]==lookup[(*r['\\''trace_key'\\''],f)]['\\''answer_prefix_ids'\\''] for r in tr))
E=a.marker('\\''empty_thinking'\\''); C=a.marker('\\''think_close'\\'')+a.marker('\\''answer_separator'\\'')
U=a.marker('\\''turn_end'\\'')+a.marker('\\''user_start'\\'')+a.enc('\\''Please respond to the original message above.'\\'')+a.marker('\\''turn_end'\\'')+a.marker('\\''assistant_start'\\'')+E
print('\\''wrappers'\\'',E,C,'\\''continuation length'\\'',len(U))
for f in ['\\''own_native'\\'','\\''own_quoted'\\'','\\''other_quoted'\\'']:
 vals=[r['\\''seconds'\\''] for r in cells if r['\\''framing'\\'']==f]
 print('\\''timing'\\'',f,'\\''mean'\\'',np.mean(vals),'\\''median'\\'',np.median(vals),'\\''p95'\\'',np.quantile(vals,.95),'\\''answer_mean'\\'',np.mean([len(r['\\''answer_ids'\\'']) for r in cells if r['\\''framing'\\'']==f]),'\\''memoryGB'\\'',max(r['\\''peak_driver_memory_bytes'\\''] for r in cells if r['\\''framing'\\'']==f)/1e9)
 for c in ['\\''unsteered'\\'','\\''technicality'\\'','\\''random'\\'']:
  v=np.array([lookup[p,'\\''hostility'\\'',f]['\\''ratings'\\'']['\\''sender'\\'']['\\''expected'\\'']-lookup[p,c,f]['\\''ratings'\\'']['\\''sender'\\'']['\\''expected'\\''] for p in sorted(prompts)])
  print('\\''contrast'\\'',f,c,'\\''mean'\\'',v.mean(),'\\''sd'\\'',v.std(ddof=1),'\\''normal90half'\\'',1.6448536*v.std(ddof=1)/math.sqrt(80),'\\''80pct_MDE'\\'',3.083*v.std(ddof=1)/math.sqrt(80))
print('\\''total_cell_hours'\\'',sum(r['\\''seconds'\\''] for r in cells)/3600)
analysis=json.loads(Path('\\''study4/data/main/analysis.json'\\'').read_text())
for k,v in analysis['\\''primary'\\'']['\\''components'\\''].items():
 if k.startswith(('\\''P1:'\\'','\\''S3:'\\'')):print(k,v)
'" in /Users/arthursu/Projects/affect-suppression-steering
 succeeded in 554ms:
Counts 320 960 pre_trace_ids Counter({(151667,): 320})
trace structural tokens {151644: 0, 151645: 0, 151667: 0, 151668: 0}
trace lengths [104.0, 538.0, 1023.0, 1023.0]
prefix exact own_native True
prefix exact own_quoted True
wrappers [151667, 271, 151668, 271] [151668, 271] continuation length 22
timing own_native mean 21.979941824375327 median 23.34030772949336 p95 31.549570927064636 answer_mean 155.728125 memoryGB 10.535780352
contrast own_native unsteered mean -0.6603613427204427 sd 0.5590413401031237 normal90half 0.10280782718484392 80pct_MDE 0.19269589172609272
contrast own_native technicality mean -0.7199564160915257 sd 0.6576856005606555 normal90half 0.1209485286936517 80pct_MDE 0.22669756990076698
contrast own_native random mean -0.4345790016966252 sd 0.6207932905709679 normal90half 0.11416402465470199 80pct_MDE 0.21398116404429324
timing own_quoted mean 33.11258014273308 median 33.10010356247949 p95 48.07085357949111 answer_mean 155.0125 memoryGB 10.590306304
contrast own_quoted unsteered mean -0.0567356185144544 sd 0.3557079411374165 normal90half 0.0654147697449107 80pct_MDE 0.12260892709452056
contrast own_quoted technicality mean -0.23443952265100992 sd 0.37710742284880316 normal90half 0.06935013920653878 80pct_MDE 0.12998511185053735
contrast own_quoted random mean -0.11439708232184717 sd 0.3946840624136874 normal90half 0.07258248714442755 80pct_MDE 0.13604360161066625
timing other_quoted mean 33.35396156962461 median 33.66563831198437 p95 48.98179923574791 answer_mean 156.721875 memoryGB 10.590306304
contrast other_quoted unsteered mean 0.004320377785949481 sd 0.390953247152152 normal90half 0.07189638938536781 80pct_MDE 0.13475762735059763
contrast other_quoted technicality mean -0.15991770709258918 sd 0.4047405857844818 normal90half 0.07443188403624641 80pct_MDE 0.1395099834318068
contrast other_quoted random mean -0.060799218351421616 sd 0.3833861601908469 normal90half 0.07050480040472636 80pct_MDE 0.13214932906355398
total_cell_hours 7.861909647709601
P1:hostility {'estimate': 0.004320377785949481, 'ci_level': 0.975, 'ci': [-0.09334877921777343, 0.10062035577596432], 'equivalence_ci': [-0.06843386551140705, 0.07561330722452762], 'supported': False, 'negligible': True, 'n': 80, 'status': 'negligible'}
S3:hostility {'estimate': -0.6603613427204427, 'ci_level': 0.95, 'ci': [-0.7835923085084582, -0.5420094018445848], 'equivalence_ci': [-0.7629240859266389, -0.5604221685358974], 'supported': True, 'negligible': False, 'n': 80, 'status': 'supported'}
P1:technicality {'estimate': -0.15991770709258918, 'ci_level': 0.975, 'ci': [-0.26410905117563266, -0.05917008931392112], 'equivalence_ci': [-0.23554628078295856, -0.08715582938568597], 'supported': True, 'negligible': False, 'n': 80, 'status': 'supported'}
S3:technicality {'estimate': -0.7199564160915257, 'ci_level': 0.95, 'ci': [-0.862696832846871, -0.5773471162798066], 'equivalence_ci': [-0.8417760243329717, -0.6008134731646964], 'supported': True, 'negligible': False, 'n': 80, 'status': 'supported'}
P1:random {'estimate': -0.060799218351421616, 'ci_level': 0.975, 'ci': [-0.1562165931399537, 0.03501901776939285], 'equivalence_ci': [-0.1315593653091808, 0.007881063674325213], 'supported': False, 'negligible': True, 'n': 80, 'status': 'negligible'}
S3:random {'estimate': -0.4345790016966252, 'ci_level': 0.95, 'ci': [-0.5712361767019283, -0.302421979423482], 'equivalence_ci': [-0.5487278103819578, -0.32136591495893496], 'supported': True, 'negligible': False, 'n': 80, 'status': 'supported'}

web search: 
web search: https://qwen.readthedocs.io/en/v3.0/inference/transformers.html
exec
/bin/zsh -lc "PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B -c 'import json,math
from pathlib import Path
import numpy as np
from statistics import NormalDist
from jinja2 import Environment
p=Path('\\''study3_pilot/.cache/huggingface/hub/models--Qwen--Qwen3-4B/snapshots/1cfa9a7208912126459214e8b04321603b3df60c/tokenizer_config.json'\\'')
template=json.loads(p.read_text())['\\''chat_template'\\'']
messages=[{'\\''role'\\'':'\\''user'\\'','\\''content'\\'':'\\''original'\\''},{'\\''role'\\'':'\\''assistant'\\'','\\''content'\\'':'\\''<think>\\nUNIQUE_RETAIN_TEST\\n</think>\\n\\n'\\''},{'\\''role'\\'':'\\''user'\\'','\\''content'\\'':'\\''Please respond to the original message above.'\\''}]
render=Environment().from_string(template).render(messages=messages,add_generation_prompt=True,enable_thinking=False)
print('\\''prior-thinking-default-render'\\'',repr(render))
rows=[json.loads(s) for s in Path('\\''study4/data/main/cells.jsonl'\\'').read_text().splitlines()]
lookup={(r['\\''prompt_id'\\''],r['\\''source'\\''],r['\\''framing'\\'']):r['\\''ratings'\\'']['\\''sender'\\'']['\\''expected'\\''] for r in rows};ids=sorted({r['\\''prompt_id'\\''] for r in rows})
rng=np.random.default_rng(20261024)
for f in ['\\''own_native'\\'','\\''own_quoted'\\'']:
 m=np.array([[lookup[p,'\\''hostility'\\'',f]-lookup[p,c,f] for c in ['\\''technicality'\\'','\\''random'\\'']] for p in ids])
 samples=rng.multinomial(80,np.full(80,1/80),size=10000)@m/80
 print(f,'\\''A_bootstrap90'\\'',np.quantile(samples,[.05,.95],axis=0).tolist(),'\\''A_bootstrap95'\\'',np.quantile(samples,[.025,.975],axis=0).tolist())
 cov=np.cov(m,rowvar=False);se=np.sqrt(np.diag(cov)/80)
 draws=rng.multivariate_normal([0,0],cov/80,size=100000)
 print('\\''zero-mean joint equivalence normal approximation'\\'',np.mean(np.all(np.abs(draws)+1.644854*se<.15,axis=1)))
 print('\\''power joint delta -0.15 each normal approximation'\\'',np.mean(np.all(draws-.15+2.241403*se<0,axis=1)))
print('\\''needed sd for .8 individual equivalence at zero'\\'',.15*math.sqrt(80)/(NormalDist().inv_cdf(.95)+NormalDist().inv_cdf(.9)))
'" in /Users/arthursu/Projects/affect-suppression-steering
 succeeded in 258ms:
prior-thinking-default-render '<|im_start|>user\noriginal<|im_end|>\n<|im_start|>assistant\n<|im_end|>\n<|im_start|>user\nPlease respond to the original message above.<|im_end|>\n<|im_start|>assistant\n<think>\n\n</think>\n\n'
own_native A_bootstrap90 [[-0.8417760243329717, -0.5487278103819578], [-0.6008134731646964, -0.32136591495893496]] A_bootstrap95 [[-0.862696832846871, -0.5712361767019283], [-0.5773471162798066, -0.302421979423482]]
zero-mean joint equivalence normal approximation 0.15546
power joint delta -0.15 each normal approximation 0.31358
own_quoted A_bootstrap90 [[-0.3024048277108782, -0.18523581995970753], [-0.164134358317295, -0.041277414190614876]] A_bootstrap95 [[-0.3163963538751625, -0.19717889733156843], [-0.1489363146039208, -0.0269941089965322]]
zero-mean joint equivalence normal approximation 0.87514
power joint delta -0.15 each normal approximation 0.81025
needed sd for .8 individual equivalence at zero 0.4584603628848552

exec
/bin/zsh -lc "nl -ba study5/Study5_RoleLadder_PREREG_v0.1_draft.md; rg -n 'def assemble|def branch|def answer|def main|def summarize|def conjunction|def definitions|def power' study4/src/runner.py study4/analysis/analyze.py" in /Users/arthursu/Projects/affect-suppression-steering
 succeeded in 0ms:
     1	# Preregistration — Study 5: The Role Ladder
     2	
     3	**Working title:** Affect Under Constraint V: Which Structural Position Makes a Trace the Model's Own?
     4	**Author:** Arthur Su. **Designed by:** Claude (2026-10-25).
     5	**Version:** 0.1 DRAFT (not binding until `PREREG_APPROVED`; to be reviewed by Codex and ChatGPT as for Study 4).
     6	**Relation to earlier studies:** Study 3 (10.5281/zenodo.23323490) showed a steered hostility state carries forward through Qwen3-4B's reasoning trace. Study 4 (prereg 10.5281/zenodo.23629525) found the same trace tokens carry the state only in the model's native thinking block (−0.66 on the sender rating) and not when quoted in the user turn (≈0), regardless of the authorship label. In the native framing, three features co-occur: the text is (a) in a thinking block, (b) in the assistant role, (c) in the current turn, immediately before the answer. Study 5 separates them.
     7	
     8	## Rationale
     9	Study 4 indicates that what carries the state is structural position rather than claimed authorship. This study asks which structural features are sufficient: the assistant role, the thinking channel, or recency within the current turn. Clinically this parallels the question of what makes a mental content function as one's own; operationally it is defined only by the measured carryover.
    10	
    11	## 1. Design: one trace, four placements (yoked, token-identical)
    12	The 320 traces generated in Study 4's main run (80 test prompts × hostility, technicality, random, unsteered) are reused as stored token IDs, with no new generation. Each is placed in four rungs:
    13	
    14	| Rung | Placement | Thinking channel | Assistant role | Current turn |
    15	|---|---|---|---|---|
    16	| R1 Native | Trace in the thinking block of the answering turn (Study 4 own-native, identical construction) | yes | yes | yes |
    17	| R2 Prior answer | Prior assistant turn whose visible reply is the trace (empty thinking), followed by a user turn "Please respond to the original message above.", then the answer | no | yes | no |
    18	| R3 Prior thinking | Prior assistant turn whose thinking block contains the trace (visible reply empty), retained in context (the default template's stripping of earlier thinking is overridden by explicit token assembly), then the same user turn, then the answer | yes | yes | no |
    19	| R4 User quote | Study 4 own-quoted framing, identical construction | no | no | yes (as user content) |
    20	
    21	Exact token templates fixed in `framings_s5.json` before any data. R2 and R3 share the same continuation turn, so they differ only in the channel holding the trace.
    22	
    23	## 2. Model, decoding, measures
    24	As Study 4: Qwen3-4B bf16 on MPS; fresh unsteered replay with logged hook-absence assertion; answer sampled (cap 200, T 0.6, top-p 0.95, top-k 20; seeds fixed per prompt × source × rung). **Outcome:** the Study 4 v0.6 sender question on an independent branch after the answer (expected digit 0–9). Carryover X_r(dir) = R(dir, r) − R(unsteered, r). Affect-specific: A_r = X_r(hostility) − X_r(control), for both controls. Diagnostic (16 check prompts, descriptive): "Whose reasoning was the earlier text: A yours, or B someone else's?" asked in both A/B orders, order-averaged.
    25	
    26	## 3. Hypotheses (prompt-cluster bootstrap, 10,000 resamples; conjunction rule across both controls; equivalence margin ±0.15 per component)
    27	**Primary (97.5% CIs):**
    28	- **P1 — Assistant role suffices:** A_R2 < 0.
    29	- **P2 — Thinking channel suffices without recency:** A_R3 < 0.
    30	
    31	**Secondary (95% CIs):**
    32	- S1: replication of Study 4 native effect, A_R1 < 0.
    33	- S2: replication of Study 4 quote null, A_R4 negligible.
    34	- S3: recency, A_R1 − A_R3 < 0.
    35	- S4: channel, A_R3 − A_R2 < 0.
    36	
    37	## 4. Reading
    38	| P1 (R2) | P2 (R3) | Reading |
    39	|---|---|---|
    40	| supported | supported | Assistant-role content is owned; the thinking channel adds or not (S4). |
    41	| negligible | supported | Ownership tied to the thinking channel, not role or recency. |
    42	| supported | negligible | Ownership tied to having said it in the assistant role; prior thinking not owned. |
    43	| negligible | negligible | Only live, current-turn reasoning carries the state (Study 4's native effect is recency-bound). |
    44	Inconclusive components are reported as such, never as absence.
    45	
    46	## 5. Sample, pilot, runtime
    47	N = 80 (all Study 4 test prompts; traces reused, so prompts and traces are already fixed). Pilot: 4 Study 3 pilot prompts × all sources × rungs, to verify template construction, valid-digit mass and R1/R4 agreement with Study 4 (descriptive only). Runtime ≈ 1,280 cells × ~20 s ≈ 7–8 h.
    48	
    49	## 6. Analysis rules, validity, stopping
    50	Study 4's frozen bootstrap and equivalence code is reused with rung labels. Validity: baseline SD ≥ 0.15 and valid mass ≥ 0.8 per rung; R1 and R4 unsteered baselines within 0.3 of Study 4's corresponding framings. No changes after the main run starts. Launchers show live progress in the Terminal window.
    51	
    52	## 7. Deviations from Study 4 data reuse
    53	Reusing Study 4 traces means Studies 4 and 5 share prompts and traces; Study 5 claims are about placement contrasts only and are not pooled with Study 4.
study4/analysis/analyze.py:19:def definitions():
study4/analysis/analyze.py:79:def summarize(defs, matrix, samples, p2_secondary=False):
study4/analysis/analyze.py:98:def conjunction(cc):
study4/analysis/analyze.py:143:def power(data,cfg):
study4/analysis/analyze.py:221:def main():
study4/src/runner.py:18:    def assemble(self, prompt, trace, framing):
study4/src/runner.py:39:    def branch(self, history, question):
study4/src/runner.py:41:    def branches(self, history, framing, sender_argmax=None):
study4/src/runner.py:136:    def answer(self, prefix, value, cap):
study4/src/runner.py:184:def main():

codex
I verified that all 320 stored traces reconstruct the original R1 and R4 answer prefixes exactly. Using the existing markers, the natural R2/R3 constructions also differ in trace position, distance to the answer, and total length—not just thinking placement.

The recorded runtimes make 7–8 hours plausible for a sender-only run. Power is less settled: at N=80, illustrative calculations using Study 4 variances give joint equivalence power ranging from about 16% to 88%, so the proposed four-prompt pilot cannot establish adequate precision.
codex
**The design is implementable, but v0.1 is not ready to bind.** The main problems are overstated structural interpretations, a mismatch between the proposed “quote null” and Study 4’s actual estimand, and insufficient specification of equivalence, power, and failure rules.

I reviewed the requested files and performed read-only checks on the saved traces, cells, tokenizer, and timings. No files were edited and no model generations were run.

**1. Token construction**

All 320 trace records are present. Every `pre_trace_ids` is `[151667]` (`<think>`), and none of the trace interiors contains `<think>`, `</think>`, `<|im_start|>`, or `<|im_end|>`. Using the saved tokenizer and [Study 4 assembly code](/Users/arthursu/Projects/affect-suppression-steering/study4/src/runner.py:18), I reconstructed all 320 own-native and all 320 own-quoted answer prefixes exactly.

| Rung | Feasibility |
|---|---|
| R1 | Already supported: use the saved pre-trace prefix, trace IDs, closing marker, and separator. |
| R2 | Feasible by explicit ID assembly, but requires a new assembly branch. |
| R3 | Feasible by explicit ID assembly, including retention through the rating branch. |
| R4 | Already supported: reproduce own-quoted exactly, including its label and wrapper. |

The existing runner cannot execute Study 5 unchanged. It recognizes three Study 4 framings, generates main-run traces, and includes Study 4-specific branches and checks.

For R3, the draft correctly identifies template stripping. The pinned local template emits reasoning only for assistant messages after the last user query. Once the continuation user turn is appended, the preceding thinking is omitted—even if supplied in `reasoning_content`. I reproduced this behavior by rendering the local template.

Therefore, assemble the entire history directly from IDs and append subsequent turns without reapplying the chat template. Preserve that history for the sender rating too: otherwise R3’s trace could survive answer generation but disappear at measurement. Study 4’s `branch()` already supports this style of retention. Use fresh unsteered forwards, not the original steered cache.

There is another unresolved choice: **the answering assistant turn in R2/R3 must have an explicitly specified thinking prefix**. The likely intended choice is the same empty-thinking prefix as R4. An ordinary thinking-enabled generation prefix would permit new reasoning and change the experiment. Qwen documents the empty-thinking prefix as a turn-specific way to disable thinking. [Qwen documentation](https://qwen.readthedocs.io/en/v3.0/inference/transformers.html#thinking-non-thinking-mode).

The claim that R2 and R3 “differ only in the channel” is too strong. Using the existing markers, a natural construction is:

```text
R2: assistant-start + empty-thinking + TRACE + turn-end
    + continuation-user-turn + assistant-start + empty-thinking

R3: assistant-start + <think> + TRACE + </think> + two-newlines
    + turn-end + continuation-user-turn + assistant-start + empty-thinking
```

With the actual tokenizer:

- Empty thinking is four IDs: `[151667, 271, 151668, 271]`.
- Closing thinking plus the separator is two IDs: `[151668, 271]`.
- R2’s trace begins three tokens later than R3’s.
- R3 has two more tokens between the trace’s end and answer generation: 24 versus 22 under this construction.
- R2’s complete answer prefix is one token longer.
- R3 has no visible prior reply; R2 has a potentially long one.

These counts describe this natural construction, not a frozen Study 5 template, which does not yet exist. Freeze the exact construction and publish its token differences. Equal trace IDs do not mean equal full contexts. Also, “thinking channel” here means placement relative to delimiter tokens; it is not a separate model input channel.

**2. What P1 and P2 can establish**

P1 and P2 can test whether affect-specific rating differences persist in the specified prior-answer and retained-prior-thinking contexts. They cannot, by themselves, establish that assistant role or thinking placement is the isolated cause.

The principal alternative explanations are:

- **Additional interaction:** R2/R3 introduce a completed assistant turn and a new request. This can trigger correction, reconsideration, or task restarting.
- **Distance and boundaries:** R1 versus R3 changes token distance, turn boundaries, and the intervening instruction together. S3 is a current-versus-prior-placement contrast, not a pure recency effect.
- **Conversational plausibility:** R3 depicts an assistant that thought extensively but said nothing. R2 depicts an assistant that exposed internal notes as its answer. Either can change how the continuation is interpreted.
- **Explicit semantic instructions:** A trace may instruct the model how to treat the user. Moving those instructions between reasoning, visible speech, and quotation changes their apparent authority without requiring “ownership.”
- **Answer mediation:** The rating follows a newly generated answer. Placement can affect the rating through the answer’s content or length, as well as through direct access to the trace. This is a total downstream effect.
- **Referent ambiguity:** “Setting the previous request aside” now follows an extra continuation request in R2/R3. “Original request” helps, but equal wording does not ensure equal interpretation.

R2/R3 share several confounds, making their direct contrast more informative than either alone. Nevertheless, S4 includes delimiter position, visibility, and the empty-reply difference.

The interpretation table needs substantial narrowing. For example:

- R2 negligible and R3 supported does not show thinking works “not role”: both retain the assistant role.
- Both negligible supports absence within the chosen margin in these two constructions, not “only live reasoning” generally.
- “Live” is particularly misleading because R1 also replays stored text.
- A supported result in one rung and an inconclusive result in another does not establish a difference between them.
- A nonsignificant S4 cannot establish that thinking adds nothing; that needs an explicit equivalence test of S4.

Any “current-turn only” reading should require a successful R1 reference effect and the relevant direct contrast, alongside equivalence in prior-turn conditions.

**3. Statistics, equivalence, and reuse**

The paired prompt-cluster bootstrap is appropriate: resample each prompt with all its sources and rungs together. The effective sample is 80 prompt clusters, not 1,280 independent cells. Ten thousand resamples is reasonable.

Two-sided 97.5% component CIs are conservative for two directional primary hypotheses. Requiring both control comparisons is an intersection-union rule; it does not automatically require an additional correction for the two controls within each conjunction. The secondary family and equivalence family still need explicit error-rate policies.

The biggest estimand problem is:

\[
A_r=(R_H-R_U)-(R_C-R_U)=R_H-R_C.
\]

The unsteered baseline cancels. Thus P1/P2 can be supported because controls raise ratings, even if hostility does not lower ratings relative to unsteered. Study 4’s carryover hypothesis explicitly required negative hostility-versus-unsteered carryover as well as both control contrasts; Study 5 drops that requirement.

This directly undermines S2’s description as “replication of Study 4 quote null.” From the saved own-quoted cells:

| Quantity | Mean |
|---|---:|
| Hostility minus unsteered | −0.057 |
| Hostility minus technicality | −0.234 |
| Hostility minus random | −0.114 |

The near-zero result concerns the first row. Recomputed prompt-bootstrap 90% CIs for the affect-specific comparisons are approximately **[−0.302, −0.164]** and **[−0.185, −0.041]**. Neither meets component-wise equivalence within ±0.15. S2 is therefore a new prediction that the existing matched data do not support, rather than a replication of an established null.

The ±0.15 margin can be retained, but it needs a substantive justification for these estimands. It is roughly 35% of Study 4’s native hostility-versus-random contrast, so “negligible” is a meaningful tolerance, not essentially zero.

There are two further implementation issues in [Study 4’s analysis](/Users/arthursu/Projects/affect-suppression-steering/study4/analysis/analyze.py:79):

- Equivalence uses **90% CIs**, whereas the Study 5 draft could be read as assigning 97.5%/95% CIs to every decision. State both procedures explicitly.
- A component can be statistically negative and equivalent within ±0.15 simultaneously. The existing code prioritizes “supported.” Study 5’s categorical ownership table makes that overlap consequential. Report evidence of direction and practical magnitude separately, with a frozen rule for table assignment.

“Reuse with rung labels” is insufficient. The contrast definitions, hypothesis membership, interpretation logic, manipulation gates, and power routine are Study 4-specific. Reuse the bootstrap machinery, but validate and freeze a Study 5 analysis implementation.

Reuse of all prompts and traces is defensible for a **conditional placement experiment**. It avoids selecting favorable traces and holds realized content fixed. However:

- R1/R4 are technical reproductions or resampling of answers on known material, not independent replications.
- New answer seeds do not make the prompts or traces independent.
- Bootstrap uncertainty does not capture variation across independently regenerated traces, models, or direction estimates.
- State that the design was developed after observing Study 4 outcomes, and avoid presenting R1/R4 as fresh confirmatory evidence.

Not pooling the studies is appropriate, but does not remove these dependencies.

**4. Power**

Adequacy is currently unestablished, especially for equivalence. Four pilot prompts can check construction and obvious measurement failures; they cannot estimate the joint variance reliably.

Using Study 4’s observed component covariance as **illustrative planning scenarios**, normal approximations at N=80 give:

| Assumed covariance | Joint power for both effects = −0.15, using 97.5% CIs | Joint equivalence power when both true effects = 0, ±0.15 margin and 90% CIs |
|---|---:|---:|
| Own-native | ≈31% | ≈16% |
| Own-quoted | ≈81% | ≈88% |

These are not estimates of actual R2/R3 power. They demonstrate that the unknown variance matters enough to change the study’s informativeness substantially.

Under native-like variance, individual 80%-power detectable effects are approximately 0.21–0.23 points; requiring both controls can require larger effects. Native-sized effects should be detectable, but small residual effects and equivalence are much harder.

Preregister joint power/precision scenarios for P1/P2 and the direct contrasts. If 80 prompts is fixed because only these traces are available, say so and accept that some theoretically important outcomes may remain unresolved. Do not loosen the margin based on pilot results.

**5. Runtime and binding details**

The arithmetic is right: 1,280 × 20 seconds is 7.11 hours. Actual Study 4 timings were:

| Framing | Mean seconds/cell |
|---|---:|
| Own-native | 22.0 |
| Own-quoted | 33.1 |
| Other-quoted | 33.4 |

The quoted cells included additional rating branches and scoring. A sender-only Study 5 run could plausibly take 7–8 hours; using 22 seconds gives 7.8 hours before overhead. Retaining Study 4’s extra work would make that optimistic. Benchmark the exact Study 5 workload, including diagnostics, logging, and long capped traces.

The pilot also needs a matched reference: four Study 3 prompts should be compared with the corresponding Study 4 **pilot cells**, not Study 4’s main-sample aggregate. Freeze whether R1/R4 reuse Study 4 answer seeds for reproducibility checks or receive new seeds for sampling robustness.

**Required changes**

1. Freeze exact ID-level templates for all rungs, including R2/R3 answering prefixes, separators, turn termination, and retained history at rating time. Add exact trace-slice and full-prefix tests.
2. Replace “differ only in channel” with the complete token-level and conversational differences; narrow P1/P2/S3/S4 interpretations accordingly.
3. Resolve the estimand mismatch: explicitly distinguish hostility-versus-unsteered carryover from hostility-versus-control differences, and correct S2’s claim to replicate a quote null.
4. Specify percentile CI levels, equivalence CI levels, multiplicity policy, conjunction rules, supported-and-equivalent overlap, opposite-direction results, and missing-cell handling.
5. Require successful reference effects and direct contrasts for the interpretation table’s comparative claims; replace general ownership claims with operational placement conclusions.
6. Supply a power/precision assessment for both detection and equivalence, acknowledging fixed N and the limits of a four-prompt pilot.
7. Define validity checks precisely: pilot versus main, SD calculation, valid-mass aggregation, matched baseline references, and what happens when each check fails. Freeze any permitted preapproval revision procedure.
8. Create and validate Study 5-specific runner and analysis code; freeze hashes of code, templates, configuration, tokenizer/model revision, prompt/trace inputs, seeds, and diagnostic IDs before main generation.
9. Specify diagnostic branching and swapped wording, answer truncation/EOS handling, required output fields, resumability, completion/stopping rules, and approval/deposit requirements. Clarify that “no new generation” means no new **trace** generation.
10. Benchmark the final workload and explicitly describe R1/R4 as reused-material reproductions, with Study 4-informed design provenance.

**Optional suggestions**

- Add a matched prior-user placement or continuation control if isolating role or turn-boundary effects is essential; otherwise retain the smaller design and narrower claims.
- Reuse Study 4’s explicit-content audit and natural-closure flags for prespecified descriptive sensitivity analyses.
- Report answer length, truncation, baseline headroom, and sender-referent diagnostics by rung.
- Display directional evidence and equivalence evidence separately rather than compressing them into one “owned/not owned” classification.
tokens used
65,382
**The design is implementable, but v0.1 is not ready to bind.** The main problems are overstated structural interpretations, a mismatch between the proposed “quote null” and Study 4’s actual estimand, and insufficient specification of equivalence, power, and failure rules.

I reviewed the requested files and performed read-only checks on the saved traces, cells, tokenizer, and timings. No files were edited and no model generations were run.

**1. Token construction**

All 320 trace records are present. Every `pre_trace_ids` is `[151667]` (`<think>`), and none of the trace interiors contains `<think>`, `</think>`, `<|im_start|>`, or `<|im_end|>`. Using the saved tokenizer and [Study 4 assembly code](/Users/arthursu/Projects/affect-suppression-steering/study4/src/runner.py:18), I reconstructed all 320 own-native and all 320 own-quoted answer prefixes exactly.

| Rung | Feasibility |
|---|---|
| R1 | Already supported: use the saved pre-trace prefix, trace IDs, closing marker, and separator. |
| R2 | Feasible by explicit ID assembly, but requires a new assembly branch. |
| R3 | Feasible by explicit ID assembly, including retention through the rating branch. |
| R4 | Already supported: reproduce own-quoted exactly, including its label and wrapper. |

The existing runner cannot execute Study 5 unchanged. It recognizes three Study 4 framings, generates main-run traces, and includes Study 4-specific branches and checks.

For R3, the draft correctly identifies template stripping. The pinned local template emits reasoning only for assistant messages after the last user query. Once the continuation user turn is appended, the preceding thinking is omitted—even if supplied in `reasoning_content`. I reproduced this behavior by rendering the local template.

Therefore, assemble the entire history directly from IDs and append subsequent turns without reapplying the chat template. Preserve that history for the sender rating too: otherwise R3’s trace could survive answer generation but disappear at measurement. Study 4’s `branch()` already supports this style of retention. Use fresh unsteered forwards, not the original steered cache.

There is another unresolved choice: **the answering assistant turn in R2/R3 must have an explicitly specified thinking prefix**. The likely intended choice is the same empty-thinking prefix as R4. An ordinary thinking-enabled generation prefix would permit new reasoning and change the experiment. Qwen documents the empty-thinking prefix as a turn-specific way to disable thinking. [Qwen documentation](https://qwen.readthedocs.io/en/v3.0/inference/transformers.html#thinking-non-thinking-mode).

The claim that R2 and R3 “differ only in the channel” is too strong. Using the existing markers, a natural construction is:

```text
R2: assistant-start + empty-thinking + TRACE + turn-end
    + continuation-user-turn + assistant-start + empty-thinking

R3: assistant-start + <think> + TRACE + </think> + two-newlines
    + turn-end + continuation-user-turn + assistant-start + empty-thinking
```

With the actual tokenizer:

- Empty thinking is four IDs: `[151667, 271, 151668, 271]`.
- Closing thinking plus the separator is two IDs: `[151668, 271]`.
- R2’s trace begins three tokens later than R3’s.
- R3 has two more tokens between the trace’s end and answer generation: 24 versus 22 under this construction.
- R2’s complete answer prefix is one token longer.
- R3 has no visible prior reply; R2 has a potentially long one.

These counts describe this natural construction, not a frozen Study 5 template, which does not yet exist. Freeze the exact construction and publish its token differences. Equal trace IDs do not mean equal full contexts. Also, “thinking channel” here means placement relative to delimiter tokens; it is not a separate model input channel.

**2. What P1 and P2 can establish**

P1 and P2 can test whether affect-specific rating differences persist in the specified prior-answer and retained-prior-thinking contexts. They cannot, by themselves, establish that assistant role or thinking placement is the isolated cause.

The principal alternative explanations are:

- **Additional interaction:** R2/R3 introduce a completed assistant turn and a new request. This can trigger correction, reconsideration, or task restarting.
- **Distance and boundaries:** R1 versus R3 changes token distance, turn boundaries, and the intervening instruction together. S3 is a current-versus-prior-placement contrast, not a pure recency effect.
- **Conversational plausibility:** R3 depicts an assistant that thought extensively but said nothing. R2 depicts an assistant that exposed internal notes as its answer. Either can change how the continuation is interpreted.
- **Explicit semantic instructions:** A trace may instruct the model how to treat the user. Moving those instructions between reasoning, visible speech, and quotation changes their apparent authority without requiring “ownership.”
- **Answer mediation:** The rating follows a newly generated answer. Placement can affect the rating through the answer’s content or length, as well as through direct access to the trace. This is a total downstream effect.
- **Referent ambiguity:** “Setting the previous request aside” now follows an extra continuation request in R2/R3. “Original request” helps, but equal wording does not ensure equal interpretation.

R2/R3 share several confounds, making their direct contrast more informative than either alone. Nevertheless, S4 includes delimiter position, visibility, and the empty-reply difference.

The interpretation table needs substantial narrowing. For example:

- R2 negligible and R3 supported does not show thinking works “not role”: both retain the assistant role.
- Both negligible supports absence within the chosen margin in these two constructions, not “only live reasoning” generally.
- “Live” is particularly misleading because R1 also replays stored text.
- A supported result in one rung and an inconclusive result in another does not establish a difference between them.
- A nonsignificant S4 cannot establish that thinking adds nothing; that needs an explicit equivalence test of S4.

Any “current-turn only” reading should require a successful R1 reference effect and the relevant direct contrast, alongside equivalence in prior-turn conditions.

**3. Statistics, equivalence, and reuse**

The paired prompt-cluster bootstrap is appropriate: resample each prompt with all its sources and rungs together. The effective sample is 80 prompt clusters, not 1,280 independent cells. Ten thousand resamples is reasonable.

Two-sided 97.5% component CIs are conservative for two directional primary hypotheses. Requiring both control comparisons is an intersection-union rule; it does not automatically require an additional correction for the two controls within each conjunction. The secondary family and equivalence family still need explicit error-rate policies.

The biggest estimand problem is:

\[
A_r=(R_H-R_U)-(R_C-R_U)=R_H-R_C.
\]

The unsteered baseline cancels. Thus P1/P2 can be supported because controls raise ratings, even if hostility does not lower ratings relative to unsteered. Study 4’s carryover hypothesis explicitly required negative hostility-versus-unsteered carryover as well as both control contrasts; Study 5 drops that requirement.

This directly undermines S2’s description as “replication of Study 4 quote null.” From the saved own-quoted cells:

| Quantity | Mean |
|---|---:|
| Hostility minus unsteered | −0.057 |
| Hostility minus technicality | −0.234 |
| Hostility minus random | −0.114 |

The near-zero result concerns the first row. Recomputed prompt-bootstrap 90% CIs for the affect-specific comparisons are approximately **[−0.302, −0.164]** and **[−0.185, −0.041]**. Neither meets component-wise equivalence within ±0.15. S2 is therefore a new prediction that the existing matched data do not support, rather than a replication of an established null.

The ±0.15 margin can be retained, but it needs a substantive justification for these estimands. It is roughly 35% of Study 4’s native hostility-versus-random contrast, so “negligible” is a meaningful tolerance, not essentially zero.

There are two further implementation issues in [Study 4’s analysis](/Users/arthursu/Projects/affect-suppression-steering/study4/analysis/analyze.py:79):

- Equivalence uses **90% CIs**, whereas the Study 5 draft could be read as assigning 97.5%/95% CIs to every decision. State both procedures explicitly.
- A component can be statistically negative and equivalent within ±0.15 simultaneously. The existing code prioritizes “supported.” Study 5’s categorical ownership table makes that overlap consequential. Report evidence of direction and practical magnitude separately, with a frozen rule for table assignment.

“Reuse with rung labels” is insufficient. The contrast definitions, hypothesis membership, interpretation logic, manipulation gates, and power routine are Study 4-specific. Reuse the bootstrap machinery, but validate and freeze a Study 5 analysis implementation.

Reuse of all prompts and traces is defensible for a **conditional placement experiment**. It avoids selecting favorable traces and holds realized content fixed. However:

- R1/R4 are technical reproductions or resampling of answers on known material, not independent replications.
- New answer seeds do not make the prompts or traces independent.
- Bootstrap uncertainty does not capture variation across independently regenerated traces, models, or direction estimates.
- State that the design was developed after observing Study 4 outcomes, and avoid presenting R1/R4 as fresh confirmatory evidence.

Not pooling the studies is appropriate, but does not remove these dependencies.

**4. Power**

Adequacy is currently unestablished, especially for equivalence. Four pilot prompts can check construction and obvious measurement failures; they cannot estimate the joint variance reliably.

Using Study 4’s observed component covariance as **illustrative planning scenarios**, normal approximations at N=80 give:

| Assumed covariance | Joint power for both effects = −0.15, using 97.5% CIs | Joint equivalence power when both true effects = 0, ±0.15 margin and 90% CIs |
|---|---:|---:|
| Own-native | ≈31% | ≈16% |
| Own-quoted | ≈81% | ≈88% |

These are not estimates of actual R2/R3 power. They demonstrate that the unknown variance matters enough to change the study’s informativeness substantially.

Under native-like variance, individual 80%-power detectable effects are approximately 0.21–0.23 points; requiring both controls can require larger effects. Native-sized effects should be detectable, but small residual effects and equivalence are much harder.

Preregister joint power/precision scenarios for P1/P2 and the direct contrasts. If 80 prompts is fixed because only these traces are available, say so and accept that some theoretically important outcomes may remain unresolved. Do not loosen the margin based on pilot results.

**5. Runtime and binding details**

The arithmetic is right: 1,280 × 20 seconds is 7.11 hours. Actual Study 4 timings were:

| Framing | Mean seconds/cell |
|---|---:|
| Own-native | 22.0 |
| Own-quoted | 33.1 |
| Other-quoted | 33.4 |

The quoted cells included additional rating branches and scoring. A sender-only Study 5 run could plausibly take 7–8 hours; using 22 seconds gives 7.8 hours before overhead. Retaining Study 4’s extra work would make that optimistic. Benchmark the exact Study 5 workload, including diagnostics, logging, and long capped traces.

The pilot also needs a matched reference: four Study 3 prompts should be compared with the corresponding Study 4 **pilot cells**, not Study 4’s main-sample aggregate. Freeze whether R1/R4 reuse Study 4 answer seeds for reproducibility checks or receive new seeds for sampling robustness.

**Required changes**

1. Freeze exact ID-level templates for all rungs, including R2/R3 answering prefixes, separators, turn termination, and retained history at rating time. Add exact trace-slice and full-prefix tests.
2. Replace “differ only in channel” with the complete token-level and conversational differences; narrow P1/P2/S3/S4 interpretations accordingly.
3. Resolve the estimand mismatch: explicitly distinguish hostility-versus-unsteered carryover from hostility-versus-control differences, and correct S2’s claim to replicate a quote null.
4. Specify percentile CI levels, equivalence CI levels, multiplicity policy, conjunction rules, supported-and-equivalent overlap, opposite-direction results, and missing-cell handling.
5. Require successful reference effects and direct contrasts for the interpretation table’s comparative claims; replace general ownership claims with operational placement conclusions.
6. Supply a power/precision assessment for both detection and equivalence, acknowledging fixed N and the limits of a four-prompt pilot.
7. Define validity checks precisely: pilot versus main, SD calculation, valid-mass aggregation, matched baseline references, and what happens when each check fails. Freeze any permitted preapproval revision procedure.
8. Create and validate Study 5-specific runner and analysis code; freeze hashes of code, templates, configuration, tokenizer/model revision, prompt/trace inputs, seeds, and diagnostic IDs before main generation.
9. Specify diagnostic branching and swapped wording, answer truncation/EOS handling, required output fields, resumability, completion/stopping rules, and approval/deposit requirements. Clarify that “no new generation” means no new **trace** generation.
10. Benchmark the final workload and explicitly describe R1/R4 as reused-material reproductions, with Study 4-informed design provenance.

**Optional suggestions**

- Add a matched prior-user placement or continuation control if isolating role or turn-boundary effects is essential; otherwise retain the smaller design and narrower claims.
- Reuse Study 4’s explicit-content audit and natural-closure flags for prespecified descriptive sensitivity analyses.
- Report answer length, truncation, baseline headroom, and sender-referent diagnostics by rung.
- Display directional evidence and equivalence evidence separately rather than compressing them into one “owned/not owned” classification.
