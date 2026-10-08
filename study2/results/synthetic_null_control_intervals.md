# Study 2 preregistered analysis

## Qwen/Qwen2.5-3B-Instruct

80 prompts; 2560 unique saved cells.

| Hypothesis/statistic | Estimate | CI level | Percentile CI | Verdict |
|---|---:|---:|---|---|
| P1: hostility | 0.3608547324353348 | 97.5% | [0.3479586597113806, 0.3735638781450929] | not supported |
| P1: hostility_minus_technicality | -1.7763568394002505e-15 | 97.5% | [-0.735218719507051, 0.6977563394891766] | not supported |
| P1: hostility_minus_random | 0.3608547324353349 | 97.5% | [0.34806353172416066, 0.37363160889238944] | not supported |
| P2: hostility | -0.009000000000000001 | 97.5% | [-0.009327248358537725, -0.008672733461607407] | not supported |
| P2: hostility_minus_technicality | 5.551115123125783e-18 | 97.5% | [-0.07452729430379744, 0.07072982594936722] | not supported |
| P2: hostility_minus_random | -0.009000000000000001 | 97.5% | [-0.012754566203679828, -0.0052146128763624604] | not supported |
| S1: S1 | -0.008 | 95.0% | [-0.008257303994733596, -0.007740053910930109] | supported |
| S2: S2 | -9.204044803117982 | 95.0% | [-9.3429609446053, -9.065241590613986] | supported |
| S3: S3 | 0.10500000000000001 | 95.0% | [0.10155213884681492, 0.10839163708245245] | supported |
| S4: S4 | 0.6999999999999958 | 95.0% | [0.6764833854265615, 0.7234966258983362] | supported |
| S5: delta_bic | -8.181461894344723 | 95.0% | [-11.711691776258277, 0.6691954381309334] | not supported |

Coherence exclusions: []

All component estimates, control intervals, missingness counts, and labeled exploratory results are retained in the accompanying JSON.

## Generality

{
  "P1": {
    "verdict": "no generality claim (fewer than two estimable models)",
    "general": false,
    "eligible_models": [
      "Qwen/Qwen2.5-3B-Instruct"
    ],
    "not_estimable_models": [],
    "missing_passed_models": [],
    "model_statuses": {
      "Qwen/Qwen2.5-3B-Instruct": "PASS"
    }
  },
  "P2": {
    "verdict": "no generality claim (fewer than two estimable models)",
    "general": false,
    "eligible_models": [
      "Qwen/Qwen2.5-3B-Instruct"
    ],
    "not_estimable_models": [],
    "missing_passed_models": [],
    "model_statuses": {
      "Qwen/Qwen2.5-3B-Instruct": "PASS"
    }
  }
}
