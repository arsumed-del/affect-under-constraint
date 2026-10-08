# Preregistered analysis output

## Qwen/Qwen2.5-3B-Instruct

40 prompts; 1280 unique saved cells. Primary coherence threshold: 4.0.

| Hypothesis/statistic | Estimate | 95% CI | Verdict |
|---|---:|---|---|
| H1: H1 | 1.6833 | [1.51815, 1.8591] | supported |
| H2: H2 | 0.0567838 | [-0.207516, 0.332745] | not supported |
| H3: H3 | -0.0161444 | [-0.131781, 0.0952213] | not supported |
| H4: H4 | 0.0234644 | [-0.00609429, 0.0511967] | not supported |
| H5: H5_warm | -0.358749 | [-0.526262, -0.208241] | not supported |
| H5: H5_difference | missing | missing | not supported |
| H6: delta_bic | -10.7034 | [-10.757, -3.75195] | not supported |

H2: criterion failed or statistic not estimable.


H3: criterion failed or statistic not estimable.


H4: criterion failed or statistic not estimable.


H5: criterion failed or statistic not estimable; specificity failed.


H6: delta BIC criterion failed or fit not estimable.


## Specificity

| Statistic | Control | Met | Reason |
|---|---|---|---|
| H1 | technicality | True | difference in predicted direction |
| H1 | random | True | difference in predicted direction |
| H2 | technicality | True | control CI includes zero |
| H2 | random | True | control CI includes zero |
| H3 | technicality | True | control CI includes zero |
| H3 | random | True | control CI includes zero |
| H4 | technicality | True | control CI includes zero |
| H4 | random | True | control CI includes zero |
| H5_warm | technicality | False | specificity not established |
| H5_warm | random | True | difference in predicted direction |
| H5_difference | technicality | False | specificity not established |
| H5_difference | random | False | specificity not established |

## Coherence exclusions

[
  {
    "condition": "neutral",
    "direction": "hostility",
    "normalized_alpha": 1.0,
    "median_ppl_ratio": 4.048909456901408
  },
  {
    "condition": "neutral",
    "direction": "technicality",
    "normalized_alpha": 1.0,
    "median_ppl_ratio": 5.280839806551425
  },
  {
    "condition": "warm_constraint",
    "direction": "technicality",
    "normalized_alpha": 1.0,
    "median_ppl_ratio": 6.110677614404121
  }
]

All missing counts, control estimates, paired contrasts, exploratory warmth/lexical/off-channel summaries, and logit-lens trajectories are retained in the accompanying JSON. Exploratory outputs do not determine confirmatory verdicts.
