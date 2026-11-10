# Exploratory analysis: reasoning-trace length as a signal of the steered state

Status: EXPLORATORY, hypothesis-generating. Not preregistered. Written and saved 2026-11-09
before any trace-length data from Studies 4 or 8 were examined. (Study 3 length summaries were
already published in its report and are treated as the observation that prompted this question,
not as evidence.)

## Question
Does the length of the model's reasoning trace behave like a marker of the hostility-steered
state — i.e. does it (1) distinguish hostility traces from controls, (2) depend on the context or
constraint the model is under, and (3) track the later liking rating?

## Data (existing, no new runs)
- Study 4 stored traces (Qwen3-4B, warmth instruction, pulse protocol; sources: hostility,
  technicality, random, unsteered; 80 prompts). Rating: liking of the user in the own-native
  (current-thinking) placement.
- Study 8 generated traces (Qwen3-4B; contexts N = no message, M = kindness rating stake,
  P = accuracy rating stake; same four sources; 80 prompts). Rating: liking of the user (O1) in the
  generated-answer arm.

## Measure
Trace length = number of thinking tokens. Capped = reached the 1,024-token limit (reported; a
sensitivity analysis excludes capped traces).

## Analyses (fixed in advance)
A1 Discrimination. For each dataset (and each Study 8 context): mean length by source; paired
   (by prompt) difference hostility minus each other source; AUC for hostility vs each other source.
A2 Constraint dependence (Study 8 only). Difference-in-differences: (hostility − unsteered length)
   under M minus the same under N; and P minus N. Same against technicality and random.
A3 Association with the rating. Within hostility traces: slope of liking on length (per 100 tokens).
   Across all sources: slope of liking on length adjusting for source.
A4 Descriptive attenuation. Hostility effect on liking (vs unsteered) with and without adjusting for
   length. Length is itself an outcome of steering, so this is descriptive, not a mediation test.

## Statistics
Prompt-level cluster bootstrap, 10,000 resamples, seed 20261109, 95% percentile intervals,
no multiplicity correction (exploratory). All results reported, including nulls.

## What would count against the idea
- A1: hostility traces no longer than controls (intervals including 0 vs both controls).
- A2: no difference in the hostility length effect between contexts.
- A3: no association of length with liking within hostility traces.

## Next step if supported
A preregistered study that manipulates or caps trace length directly (e.g. matched-length traces,
forced caps) and tests length as a marker across a second model family.

## Addendum (2026-11-09, written before running these)
A5 Content vs amount. Repeat A3/A4 adding the trace's expressed-hostility score (classifier EH on
   the trace) as a covariate, to ask whether length relates to the rating beyond hostile content.
A6 Study 7 warmth compliance (continuous). Using the answers' expressed-warmth score (classifier EW)
   and EH, report the warmth instruction's effect on answer tone by trace source (G minus N), as a
   continuous alternative to the failed binary gate.
A7 Pooled estimate. Descriptive inverse-variance pooled hostility-vs-unsteered liking effect across
   the Studies 3-8 primary estimates, with the caveat that the studies share prompts and traces and
   are therefore not independent. Not a formal meta-analysis.
Same bootstrap settings; all results reported.
