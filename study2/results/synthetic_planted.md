# Study 2 preregistered analysis

## Qwen/Qwen2.5-3B-Instruct

80 prompts; 2560 unique saved cells.

| Hypothesis/statistic | Estimate | CI level | Percentile CI | Verdict |
|---|---:|---:|---|---|
| P1: hostility | 3.3349709030464254 | 97.5% | [3.2157871334233827, 3.4524271183455153] | supported |
| P1: hostility_minus_technicality | 3.3349709030464263 | 97.5% | [3.2159185894193416, 3.452162841143811] | supported |
| P1: hostility_minus_random | 3.3349709030464263 | 97.5% | [3.216756346460453, 3.453053076802404] | supported |
| P2: hostility | -0.9 | 97.5% | [-0.9327248358537727, -0.8672733461607404] | supported |
| P2: hostility_minus_technicality | -0.9 | 97.5% | [-0.9324198864585143, -0.8677104663825086] | supported |
| P2: hostility_minus_random | -0.9 | 97.5% | [-0.9319357858125661, -0.8675387061201942] | supported |
| S1: S1 | -0.8 | 95.0% | [-0.8257303994733594, -0.7740053910930109] | supported |
| S2: S2 | -0.9959076769509485 | 95.0% | [-1.010938856689749, -0.9808887164965896] | supported |
| S3: S3 | 0.10500000000000001 | 95.0% | [0.10155213884681492, 0.10839163708245245] | supported |
| S4: S4 | 0.6999999999999958 | 95.0% | [0.6764833854265615, 0.7234966258983362] | supported |
| S5: delta_bic | 119.88992855812988 | 95.0% | [92.0571966849612, 158.25824322815507] | supported |

Coherence exclusions: []

All component estimates, control intervals, missingness counts, and labeled exploratory results are retained in the accompanying JSON.
## meta-llama/Llama-3.2-3B-Instruct

80 prompts; 2560 unique saved cells.

| Hypothesis/statistic | Estimate | CI level | Percentile CI | Verdict |
|---|---:|---:|---|---|
| P1: hostility | 3.3349709030464254 | 97.5% | [3.2157871334233827, 3.4524271183455153] | supported |
| P1: hostility_minus_technicality | 3.3349709030464263 | 97.5% | [3.2159185894193416, 3.452162841143811] | supported |
| P1: hostility_minus_random | 3.3349709030464263 | 97.5% | [3.216756346460453, 3.453053076802404] | supported |
| P2: hostility | -0.9 | 97.5% | [-0.9327248358537727, -0.8672733461607404] | supported |
| P2: hostility_minus_technicality | -0.9 | 97.5% | [-0.9324198864585143, -0.8677104663825086] | supported |
| P2: hostility_minus_random | -0.9 | 97.5% | [-0.9319357858125661, -0.8675387061201942] | supported |
| S1: S1 | -0.8 | 95.0% | [-0.8257303994733594, -0.7740053910930109] | supported |
| S2: S2 | -0.9959076769509485 | 95.0% | [-1.010938856689749, -0.9808887164965896] | supported |
| S3: S3 | 0.10500000000000001 | 95.0% | [0.10155213884681492, 0.10839163708245245] | supported |
| S4: S4 | 0.6999999999999958 | 95.0% | [0.6764833854265615, 0.7234966258983362] | supported |
| S5: delta_bic | 119.88992855812988 | 95.0% | [92.0571966849612, 158.25824322815507] | supported |

Coherence exclusions: []

All component estimates, control intervals, missingness counts, and labeled exploratory results are retained in the accompanying JSON.
## microsoft/Phi-3.5-mini-instruct

80 prompts; 2560 unique saved cells.

| Hypothesis/statistic | Estimate | CI level | Percentile CI | Verdict |
|---|---:|---:|---|---|
| P1: hostility | 3.3349709030464254 | 97.5% | [3.2157871334233827, 3.4524271183455153] | supported |
| P1: hostility_minus_technicality | 3.3349709030464263 | 97.5% | [3.2159185894193416, 3.452162841143811] | supported |
| P1: hostility_minus_random | 3.3349709030464263 | 97.5% | [3.216756346460453, 3.453053076802404] | supported |
| P2: hostility | -0.9 | 97.5% | [-0.9327248358537727, -0.8672733461607404] | supported |
| P2: hostility_minus_technicality | -0.9 | 97.5% | [-0.9324198864585143, -0.8677104663825086] | supported |
| P2: hostility_minus_random | -0.9 | 97.5% | [-0.9319357858125661, -0.8675387061201942] | supported |
| S1: S1 | -0.8 | 95.0% | [-0.8257303994733594, -0.7740053910930109] | supported |
| S2: S2 | -0.9959076769509485 | 95.0% | [-1.010938856689749, -0.9808887164965896] | supported |
| S3: S3 | 0.10500000000000001 | 95.0% | [0.10155213884681492, 0.10839163708245245] | supported |
| S4: S4 | 0.6999999999999958 | 95.0% | [0.6764833854265615, 0.7234966258983362] | supported |
| S5: delta_bic | 119.88992855812988 | 95.0% | [92.0571966849612, 158.25824322815507] | supported |

Coherence exclusions: []

All component estimates, control intervals, missingness counts, and labeled exploratory results are retained in the accompanying JSON.

## Generality

{
  "P1": {
    "verdict": "general",
    "general": true,
    "eligible_models": [
      "Qwen/Qwen2.5-3B-Instruct",
      "meta-llama/Llama-3.2-3B-Instruct",
      "microsoft/Phi-3.5-mini-instruct"
    ],
    "not_estimable_models": [],
    "missing_passed_models": [],
    "model_statuses": {
      "Qwen/Qwen2.5-3B-Instruct": "PASS",
      "meta-llama/Llama-3.2-3B-Instruct": "PASS",
      "microsoft/Phi-3.5-mini-instruct": "PASS"
    }
  },
  "P2": {
    "verdict": "general",
    "general": true,
    "eligible_models": [
      "Qwen/Qwen2.5-3B-Instruct",
      "meta-llama/Llama-3.2-3B-Instruct",
      "microsoft/Phi-3.5-mini-instruct"
    ],
    "not_estimable_models": [],
    "missing_passed_models": [],
    "model_statuses": {
      "Qwen/Qwen2.5-3B-Instruct": "PASS",
      "meta-llama/Llama-3.2-3B-Instruct": "PASS",
      "microsoft/Phi-3.5-mini-instruct": "PASS"
    }
  }
}
