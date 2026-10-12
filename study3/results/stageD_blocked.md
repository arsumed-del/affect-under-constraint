# Stage D — specification audit: BLOCKED

Stages A, B and C finished exactly under v0.2 before this audit. Their commits are `c6ccc72`, `6580055`, and `a2bbb74`. Stage A contains all 80 calibration cells; every zero-dose agreement check passed exactly. No test-prompt file was opened, read, hashed or used. The author-supplied test-set hash has not been independently verified, as instructed.

The author-approved v0.3 top dose of 0.0175 and promotion of pulse steering to S5 are accepted. The agent has not substituted the v0.2 dose for Stage D. No Stage D model calls, main-run code, analysis freeze, approval file or main run have been produced.

## Blocking error

`SpecificationError: v0.3 does not fully determine the pulse numerical path, coherence-gate aggregation, or exploratory sample/subset rules; completing and freezing these choices would require scientific design decisions.`

AGENTS.md requires: “If something fails, log the exact error in STATUS.md and DEVIATIONS.md, try pure engineering fixes only, and stop BLOCKED if a design decision is needed.” The following items are recorded together so the reviewer can settle them in one pass. No choice below has been silently implemented.

## 1. Pulse transition and rating mask (S5; sections 6–8)

The pulse instruction specifies steering on prompt and thinking positions, off for the answer. It also calls the condition “loop only” and says that carryover must travel through the trace. The existing generation path carries `past_key_values` from the steered prefix into subsequent generation. Merely removing the hook preserves those altered cached representations. Rebuilding the complete prefix unsteered before answering removes that hidden route, but is a different numerical intervention. The draft does not say which transition to use.

The boundary also determines how to obtain the first answer-token logits: the logits after the closing thinking token were produced while that thinking position was steered. Recomputing that boundary unsteered differs from continuing from those logits. This matters for both natural and forced closure.

Finally, section 7 describes R_full as steering active on turn-1 positions, while S5 turns steering off for the answer. The pulse full-forward rating needs an explicit mask: reproduce the prompt/thinking-only pulse, or apply the general all-turn-1 R_full definition. The definition affects C_pulse directly. This is not a cache optimization or a floating-point implementation detail.

**Needed resolution:** the pulse cache/re-encoding protocol and exact boundary, plus its R_full mask and teacher-forced LHP mask. LHP is otherwise inherited as steering-active opener scoring; the pulse answer is specified to be unsteered.

## 2. Coherence-gate aggregation and eligibility (section 9)

The rule uses “cells with median absolute perplexity > 6.0.” A generated prompt-level record has one sequence perplexity for each segment; a median needs an aggregation population. Study 2 explicitly used condition × direction × dose groups across prompts. Study 3 introduces mode and pulse route and does not explicitly identify the median's grouping keys, or say whether it instead means a prompt-level gate (or a median over trace windows).

**Needed resolution:** specify the grouping unit for each segment, including mode and regular/pulse route; confirm that answer and trace are gated separately. Also specify whether P2 fits each segment's slope on its independently retained dose groups, or requires a common retained grid for the difference of slopes, and how the “missing required cells → not estimable” rule applies when a dose group is deliberately gated rather than absent from raw data. These alternatives change P2 estimates and estimability.

## 3. Natural-closure sensitivity analysis (E3)

E3 asks for P1 and P2 to be recomputed on cells whose trace closed naturally. P1 combines direct and thinking cells, baseline ratings, hostility and both controls; different traces can truncate for the same prompt at different directions and doses.

**Needed resolution:** specify whether the restriction is row-wise, component-specific paired complete cases, or a common prompt subset complete across the required directions/doses. Specify how direct cells and zero-dose baselines are retained and how intentional truncation exclusions interact with “missing required cells → not estimable.” P2's retained grids and sample sizes depend on the same choice.

## 4. Fixed readability sample (E4)

Stage C explicitly identifies s2c00–s2c04 from the calibration set at v0.2 full dose. E4 in the main-study draft refers to a fixed, preselected sample without identifying its prompts, count, direction or regular/pulse route.

**Needed resolution:** state whether E4 is the already completed Stage C calibration sample, a new v0.3 calibration sample, or a main-run sample. For a new sample, supply fixed IDs or a deterministic pre-data selection rule and the intended direction/route. The agent cannot select favorable outputs or inspect the test file to resolve this.

## Items resolved by existing text, not additional blocks

- Stage D dose is 0.0175, grid 0/0.00875/0.0175, warmth only, 1,120 regular plus 240 pulse cells.
- Both modes use the specified .6/.95/top-k20 decoding and 1,024/200 caps; all ratings use the shared empty-thinking prefix and complete-sequence forwards.
- S3 refers to Study 2 P1: positive hostility LHP slope and both positive hostility-minus-control slope contrasts. S4 refers to Study 2 P2: negative hostility H and both negative hostility-minus-control H contrasts.
- Primary intervals are 97.5%, secondary intervals 95%, prompt-cluster percentile bootstrap with 10,000 resamples. The 200-null-replicate check is a validation requirement, not permission to tune seeds or analysis to pass it.
- Real-run approval/deposit guards must execute before any access to the test set. Calibration dry runs must use a separate output namespace and cannot bypass the guard to select a test path.

## Preserved work and next authorized action

All A–C outputs and their inference provenance remain intact. Stage D's source hashes are recorded in `results/stageD_specification_hashes.sha256`, excluding the forbidden test file. No config.yaml or frozen_hashes.sha256 is claimed complete. After the reviewer supplies the missing protocol/estimator definitions, implementation, guarded calibration dry run, synthetic checks and freeze can proceed without repeating or altering A–C.
