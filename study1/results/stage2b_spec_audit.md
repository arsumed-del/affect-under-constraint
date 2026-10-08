# Stage 2b full specification audit — Amendment 2.2

The full PREREG §§7–9, §8.1 estimator definitions, config.yaml, and AGENTS.md were reviewed together before analysis implementation. The previous H6 blocker is resolved by the explicit expression gap G and specified hinge model. No further blocking ambiguity was identified in this audit. Any subsequently discovered specification issue will be collected with all remaining issues in stage2b_blocked.md before stopping.

| Area | Implementation contract |
|---|---|
| M1 | Mean token log-probability within opener; mean across each fixed set of 12; hostile minus warm. |
| M2 | Fixed classifier; anger + disgust and joy; failed scores remain missing and are never replaced. |
| M3 | Entropy from raw unfiltered next-token logits; unsteered perplexity ratio to the same prompt/condition baseline. |
| M4 | First and last floor(n/4) token slices; fewer than 8 tokens means missing time-course leakage. Case-insensitive whole-word lexicon counts, gated by full-text EH < 0.5. |
| M5 | Digit probabilities normalized over 0–9; identical visible token IDs; hidden-cache minus text-only rating; steering removed during both ratings. |
| Standardization | Fixed model-wide z-score constants from unique saved main-run cells, so the shared alpha=0 generation is counted once. Population SD (the standard z-score convention); available values used for each measure. Then expand shared baselines across directions for fitting. Constants include all cells, as §8.1 specifies, and are fixed through bootstrap. |
| Slopes | OLS with intercept over all available prompt × normalized-dose rows in each condition/direction; raw LHP slope is also reported alongside the standardized slope. |
| H2 | Difference of standardized slope ratios; no denominator clipping, pseudocount, or substitution. Exact undefined ratios remain missing. Control D skipped when its H1 slope interval includes zero. |
| H3 | Warm-minus-neutral entropy slopes, unstandardized. |
| H4 | Mean of the available high-dose leakage values within each prompt, then mean across prompts. |
| H5 | Warm carryover and paired warm-minus-neutral carryover at a=1; both negative-CI criteria and both control checks are evaluated. |
| H6 | G uses paired baseline EH/LHP, G(0)=0; fit intercept/slope versus continuous hinge at each specified interior point; choose minimum SSE; Gaussian BIC with k=3 and k=5. Report bootstrap proportion ΔBIC>6. |
| Coherence | Calibration threshold is 4.0; primary-analysis exclusion threshold remains 2.0. Gate condition × direction × dose across prompts before fitting. The resulting eligibility mask is held fixed for bootstrap; retained doses are not replaced or regridded. |
| Missingness | Available observations per statistic, paired wherever a subtraction requires corresponding values. Report missing observation/prompt counts and non-estimable bootstrap counts. Non-identifiable fits remain missing rather than being regularized. |
| Bootstrap | 10,000 shared draws of 40 prompt IDs, seed 20261003, all observations of a sampled prompt together. Fixed scaling constants; percentile intervals. |
| Specificity/verdicts | Both controls required. Positive direction for H1/H3/H4; negative for H2/H5. H2 and H6 interpretations depend on H1; H6 has no specificity test. |
| Exploratory | EW slopes/control contrasts; lexical/off-channel summaries; conventional final-norm/unembedding logit lens of the same opener scores at every decoder-layer output, labeled exploratory only. |
| Stage 3 lock | Main runner rejects test mode without an approval file containing the exact active specification hashes. This task uses calibration timing mode only. |

The floor-quarter boundary, population-SD convention, unique-baseline counting, ordinary whole-word lexical matching, and exploratory logit-lens implementation are recorded before any test outputs. They do not replace the registered estimators or depend on observed test results. The different calibration and primary-analysis thresholds are preserved exactly, even if they result in excluded high-dose primary cells.
