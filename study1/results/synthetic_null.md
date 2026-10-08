# Preregistered analysis output

## Qwen/Qwen2.5-3B-Instruct

40 prompts; 1280 unique saved cells. Primary coherence threshold: 2.0.

| Hypothesis/statistic | Estimate | 95% CI | Verdict |
|---|---:|---|---|
| H1: H1 | 1.90725e-16 | [-0.123528, 0.123287] | not supported |
| H2: H2 | 3.17267 | [-74.7914, 63.2008] | not supported |
| H3: H3 | -6.12712e-15 | [-0.0127577, 0.012456] | not supported |
| H4: H4 | 3.46945e-19 | [-0.00210888, 0.00201361] | not supported |
| H5: H5_warm | -1.73472e-19 | [-0.00475177, 0.00484208] | not supported |
| H5: H5_difference | -6.93889e-19 | [-0.00555032, 0.00618039] | not supported |
| H6: delta_bic | -10.9613 | [-10.885, -7.32889] | not supported |

H1: criterion failed or statistic not estimable.


H2: criterion failed or statistic not estimable; H1 not supported; H2 not interpreted.


H3: criterion failed or statistic not estimable.


H4: criterion failed or statistic not estimable.


H5: criterion failed or statistic not estimable.


H6: delta BIC criterion failed or fit not estimable; H1 not supported; H6 not interpreted.


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

