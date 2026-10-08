# Study 2 preregistered analysis

## Qwen/Qwen2.5-3B-Instruct

80 prompts; 2560 unique saved cells.

| Hypothesis/statistic | Estimate | CI level | Percentile CI | Verdict |
|---|---:|---:|---|---|
| P1: hostility | 1.498125846664302 | 97.5% | [1.3769539920061238, 1.6204054932213081] | supported |
| P1: hostility_minus_technicality | 1.0860784455306578 | 97.5% | [0.9404766239003091, 1.2320172900389899] | supported |
| P1: hostility_minus_random | 0.8833998646549664 | 97.5% | [0.7527191869392995, 1.0107099607521632] | supported |
| P2: hostility | -0.4106688439846039 | 97.5% | [-0.5738679261133075, -0.26875615261495117] | not supported |
| P2: hostility_minus_technicality | 0.11500992476940156 | 97.5% | [-0.034299886375665646, 0.2828900025784973] | not supported |
| P2: hostility_minus_random | -0.13943710625171662 | 97.5% | [-0.28520461697131394, 0.006986314803361918] | not supported |
| S1: S1 | -0.4396089047193527 | 95.0% | [-0.5880201113224028, -0.3064832675457001] | supported |
| S2: S2 | -0.4115119905387039 | 95.0% | [-0.6790682600088708, -0.1439017074610035] | supported |
| S3: S3 | 0.01925539588830768 | 95.0% | [-0.016647718336587528, 0.051809318608674805] | not supported |
| S4: S4 | -0.27218893712674924 | 95.0% | [-0.3491951135644801, -0.1925864629927567] | not supported |
| S5: delta_bic | -11.67391132958348 | 95.0% | [-12.243695984187498, -7.070964012773961] | not supported |

Coherence exclusions: [{"condition": "neutral", "direction": "technicality", "normalized_alpha": 1.0, "median_ppl_ratio": 5.19943381558565}, {"condition": "warm_constraint", "direction": "technicality", "normalized_alpha": 1.0, "median_ppl_ratio": 7.38053422471847}]

All component estimates, control intervals, missingness counts, and labeled exploratory results are retained in the accompanying JSON.
## meta-llama/Llama-3.2-3B-Instruct

80 prompts; 2560 unique saved cells.

| Hypothesis/statistic | Estimate | CI level | Percentile CI | Verdict |
|---|---:|---:|---|---|
| P1: hostility | 2.7623959398849487 | 97.5% | [2.693944463594816, 2.8292104149061275] | supported |
| P1: hostility_minus_technicality | 1.1768309083406499 | 97.5% | [1.108421855854212, 1.2468493642726657] | supported |
| P1: hostility_minus_random | 2.7236825808686587 | 97.5% | [2.6470310209364785, 2.8030927830603147] | supported |
| P2: hostility | 0.226273201033473 | 97.5% | [0.19121632932685317, 0.26230420966632667] | not supported |
| P2: hostility_minus_technicality | -0.20049953646957874 | 97.5% | [-0.2530166625091806, -0.1464203460048881] | not supported |
| P2: hostility_minus_random | -0.05029960162937641 | 97.5% | [-0.10737152892164885, 0.007726757507771262] | not supported |
| S1: S1 | 0.14724787138402462 | 95.0% | [0.10224350982345642, 0.19144221150316298] | not supported |
| S2: S2 | -0.04402355982311967 | 95.0% | [-0.18445420161034567, 0.09326569788862646] | not supported |
| S3: S3 | 0.05279475852936836 | 95.0% | [0.014935921926353343, 0.08952422899213464] | supported |
| S4: S4 | 0.17493999933555227 | 95.0% | [0.08367015053824105, 0.2626492395182734] | supported |
| S5: delta_bic | -6.747770765324082 | 95.0% | [-10.341113263830199, 2.1370320964637775] | not supported |

Coherence exclusions: [{"condition": "neutral", "direction": "technicality", "normalized_alpha": 0.75, "median_ppl_ratio": 4.816605121241157}, {"condition": "neutral", "direction": "technicality", "normalized_alpha": 1.0, "median_ppl_ratio": 12.350587674101085}, {"condition": "warm_constraint", "direction": "technicality", "normalized_alpha": 0.75, "median_ppl_ratio": 7.4289280654918475}, {"condition": "warm_constraint", "direction": "technicality", "normalized_alpha": 1.0, "median_ppl_ratio": 14.400149914593074}]

All component estimates, control intervals, missingness counts, and labeled exploratory results are retained in the accompanying JSON.
## microsoft/Phi-3.5-mini-instruct

80 prompts; 2560 unique saved cells.

| Hypothesis/statistic | Estimate | CI level | Percentile CI | Verdict |
|---|---:|---:|---|---|
| P1: hostility | 1.5459393004491817 | 97.5% | [1.436365162748615, 1.6495213619578324] | supported |
| P1: hostility_minus_technicality | 0.3362958939010523 | 97.5% | [0.2718187103594518, 0.40251000860136443] | supported |
| P1: hostility_minus_random | 1.6682752572074364 | 97.5% | [1.545848922763362, 1.7796882908904614] | supported |
| P2: hostility | 0.1032272469252348 | 97.5% | [0.03613741606473923, 0.18153846321161834] | not supported |
| P2: hostility_minus_technicality | 0.0807686384767294 | 97.5% | [0.011037249825894832, 0.16159221744164823] | not supported |
| P2: hostility_minus_random | 0.10740934945642948 | 97.5% | [0.034879150204360485, 0.18970255175139764] | not supported |
| S1: S1 | 0.09495686292648316 | 95.0% | [0.037279142523184434, 0.15934732764959333] | not supported |
| S2: S2 | -0.5012435541426338 | 95.0% | [-0.8175922694372628, -0.2015031413677272] | supported |
| S3: S3 | 0.040502342491587726 | 95.0% | [0.01424484302218086, 0.06652494874204269] | supported |
| S4: S4 | 0.05977487030940487 | 95.0% | [0.007416003664637454, 0.11073790761395258] | supported |
| S5: delta_bic | -8.045745172111754 | 95.0% | [-10.964834833650192, -1.5503825344809357] | not supported |

Coherence exclusions: []

All component estimates, control intervals, missingness counts, and labeled exploratory results are retained in the accompanying JSON.

## Generality

{
  "P1": {
    "verdict": "general",
    "general": true,
    "eligible_models": [
      "Qwen/Qwen2.5-3B-Instruct",
      "microsoft/Phi-3.5-mini-instruct",
      "meta-llama/Llama-3.2-3B-Instruct"
    ],
    "not_estimable_models": [],
    "missing_passed_models": [],
    "model_statuses": {
      "Qwen/Qwen2.5-3B-Instruct": "PASS",
      "microsoft/Phi-3.5-mini-instruct": "PASS",
      "meta-llama/Llama-3.2-3B-Instruct": "PASS"
    }
  },
  "P2": {
    "verdict": "not general",
    "general": false,
    "eligible_models": [
      "Qwen/Qwen2.5-3B-Instruct",
      "microsoft/Phi-3.5-mini-instruct",
      "meta-llama/Llama-3.2-3B-Instruct"
    ],
    "not_estimable_models": [],
    "missing_passed_models": [],
    "model_statuses": {
      "Qwen/Qwen2.5-3B-Instruct": "PASS",
      "microsoft/Phi-3.5-mini-instruct": "PASS",
      "meta-llama/Llama-3.2-3B-Instruct": "PASS"
    }
  }
}
