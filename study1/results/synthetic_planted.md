# Preregistered analysis output

## Qwen/Qwen2.5-3B-Instruct

40 prompts; 1280 unique saved cells. Primary coherence threshold: 2.0.

| Hypothesis/statistic | Estimate | 95% CI | Verdict |
|---|---:|---|---|
| H1: H1 | 3.34689 | [3.17189, 3.51872] | supported |
| H2: H2 | -0.988927 | [-1.01059, -0.966228] | supported |
| H3: H3 | 0.7 | [0.663473, 0.736147] | supported |
| H4: H4 | 0.105 | [0.0989057, 0.110934] | supported |
| H5: H5_warm | -0.9 | [-0.944292, -0.854656] | supported |
| H5: H5_difference | -0.8 | [-0.840061, -0.759697] | supported |
| H6: delta_bic | 51.263 | [32.3153, 82.6478] | supported |

## Specificity

| Statistic | Control | Met | Reason |
|---|---|---|---|
| H1 | technicality | True | control CI includes zero |
| H1 | random | True | control CI includes zero |
| H2 | technicality | True | control H1 CI includes zero; D not computed |
| H2 | random | True | control H1 CI includes zero; D not computed |
| H3 | technicality | True | control CI includes zero |
| H3 | random | True | control CI includes zero |
| H4 | technicality | True | control CI includes zero |
| H4 | random | True | control CI includes zero |
| H5_warm | technicality | True | control CI includes zero |
| H5_warm | random | True | control CI includes zero |
| H5_difference | technicality | True | control CI includes zero |
| H5_difference | random | True | control CI includes zero |

## Coherence exclusions

[]

All missing counts, control estimates, paired contrasts, exploratory warmth/lexical/off-channel summaries, and logit-lens trajectories are retained in the accompanying JSON. Exploratory outputs do not determine confirmatory verdicts.

