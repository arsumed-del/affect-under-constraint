# Study 2 report

This report covers 3 model(s): Qwen/Qwen2.5-3B-Instruct, meta-llama/Llama-3.2-3B-Instruct, microsoft/Phi-3.5-mini-instruct.
The first primary prediction asks whether steering toward hostility still changes fixed reply preferences under the warmth instruction.
The second asks whether the saved hidden state changes a later rating more than either control direction does.
The preregistered overall verdict for persistence is general.
The preregistered overall verdict for hidden carryover is not general.
The tables below retain every model-specific estimate and verdict, including unsupported or unavailable results.
These findings concern the registered model behaviors and do not establish human-like feelings.

Primary intervals are 97.5%; secondary intervals are 95%. Verdicts and statistics below are copied from the frozen analysis output.

## Qwen/Qwen2.5-3B-Instruct

| Prediction / component | Estimate | Interval | Verdict |
|---|---:|---|---|
| P1 / hostility | 1.498125846664302 | 97.5%: [1.3769539920061238, 1.6204054932213081] | supported |
| P1 / hostility_minus_technicality | 1.0860784455306578 | 97.5%: [0.9404766239003091, 1.2320172900389899] | supported |
| P1 / hostility_minus_random | 0.8833998646549664 | 97.5%: [0.7527191869392995, 1.0107099607521632] | supported |
| P2 / hostility | -0.4106688439846039 | 97.5%: [-0.5738679261133075, -0.26875615261495117] | not supported |
| P2 / hostility_minus_technicality | 0.11500992476940156 | 97.5%: [-0.034299886375665646, 0.2828900025784973] | not supported |
| P2 / hostility_minus_random | -0.13943710625171662 | 97.5%: [-0.28520461697131394, 0.006986314803361918] | not supported |
| S1 / S1 | -0.4396089047193527 | 95%: [-0.5880201113224028, -0.3064832675457001] | supported |
| S2 / S2 | -0.4115119905387039 | 95%: [-0.6790682600088708, -0.1439017074610035] | supported |
| S3 / S3 | 0.01925539588830768 | 95%: [-0.016647718336587528, 0.051809318608674805] | not supported |
| S4 / S4 | -0.27218893712674924 | 95%: [-0.3491951135644801, -0.1925864629927567] | not supported |
| S5 / delta_bic | -11.67391132958348 | 95%: [-12.243695984187498, -7.070964012773961] | not supported |

### Specificity controls

| Primary / control | Control estimate and interval | Hostility minus control and interval | Contrast met |
|---|---|---|---|
| P1 / technicality | 0.41204740113364413; [0.30037272423936523, 0.5147683163464054] | 1.0860784455306578; [0.9404766239003091, 1.2320172900389899] | True |
| P1 / random | 0.6147259820093355; [0.471341201946247, 0.7614798806098014] | 0.8833998646549664; [0.7527191869392995, 1.0107099607521632] | True |
| P2 / technicality | -0.5256787687540054; [-0.7524717762693762, -0.33558477651327845] | 0.11500992476940156; [-0.034299886375665646, 0.2828900025784973] | False |
| P2 / random | -0.2712317377328873; [-0.41211152538657186, -0.14766515858471382] | -0.13943710625171662; [-0.28520461697131394, 0.006986314803361918] | False |

### Coherence exclusions

```json
[
  {
    "condition": "neutral",
    "direction": "technicality",
    "normalized_alpha": 1.0,
    "median_ppl_ratio": 5.19943381558565
  },
  {
    "condition": "warm_constraint",
    "direction": "technicality",
    "normalized_alpha": 1.0,
    "median_ppl_ratio": 7.38053422471847
  }
]
```

### Missing observations

```json
{
  "neutral|hostility": {
    "lhp": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "eh": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "entropy": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "leak_timecourse": {
      "missing_observations": 6,
      "observed_by_dose": [
        80,
        80,
        79,
        78,
        78,
        79
      ],
      "prompts_without_observations": 0
    },
    "carryover": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "ew": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "S2_eh_component": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "S5_eh_component": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "eh_z": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "lhp_z": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "S2_eh_component_z": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "S5_eh_component_z": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    }
  },
  "neutral|technicality": {
    "lhp": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "eh": {
      "missing_observations": 80,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        0
      ],
      "prompts_without_observations": 0
    },
    "entropy": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "leak_timecourse": {
      "missing_observations": 82,
      "observed_by_dose": [
        80,
        80,
        80,
        79,
        79,
        0
      ],
      "prompts_without_observations": 0
    },
    "carryover": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "ew": {
      "missing_observations": 80,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        0
      ],
      "prompts_without_observations": 0
    },
    "S2_eh_component": {
      "missing_observations": 80,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        0
      ],
      "prompts_without_observations": 0
    },
    "S5_eh_component": {
      "missing_observations": 80,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        0
      ],
      "prompts_without_observations": 0
    },
    "eh_z": {
      "missing_observations": 80,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        0
      ],
      "prompts_without_observations": 0
    },
    "lhp_z": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "S2_eh_component_z": {
      "missing_observations": 80,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        0
      ],
      "prompts_without_observations": 0
    },
    "S5_eh_component_z": {
      "missing_observations": 80,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        0
      ],
      "prompts_without_observations": 0
    }
  },
  "neutral|random": {
    "lhp": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "eh": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "entropy": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "leak_timecourse": {
      "missing_observations": 4,
      "observed_by_dose": [
        80,
        80,
        80,
        79,
        79,
        78
      ],
      "prompts_without_observations": 0
    },
    "carryover": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "ew": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "S2_eh_component": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "S5_eh_component": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "eh_z": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "lhp_z": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "S2_eh_component_z": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "S5_eh_component_z": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    }
  },
  "warm_constraint|hostility": {
    "lhp": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "eh": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "entropy": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "leak_timecourse": {
      "missing_observations": 8,
      "observed_by_dose": [
        79,
        79,
        79,
        78,
        78,
        79
      ],
      "prompts_without_observations": 0
    },
    "carryover": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "ew": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "S2_eh_component": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "S5_eh_component": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "eh_z": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "lhp_z": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "S2_eh_component_z": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "S5_eh_component_z": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    }
  },
  "warm_constraint|technicality": {
    "lhp": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "eh": {
      "missing_observations": 80,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        0
      ],
      "prompts_without_observations": 0
    },
    "entropy": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "leak_timecourse": {
      "missing_observations": 84,
      "observed_by_dose": [
        79,
        79,
        79,
        79,
        80,
        0
      ],
      "prompts_without_observations": 0
    },
    "carryover": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "ew": {
      "missing_observations": 80,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        0
      ],
      "prompts_without_observations": 0
    },
    "S2_eh_component": {
      "missing_observations": 80,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        0
      ],
      "prompts_without_observations": 0
    },
    "S5_eh_component": {
      "missing_observations": 80,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        0
      ],
      "prompts_without_observations": 0
    },
    "eh_z": {
      "missing_observations": 80,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        0
      ],
      "prompts_without_observations": 0
    },
    "lhp_z": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "S2_eh_component_z": {
      "missing_observations": 80,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        0
      ],
      "prompts_without_observations": 0
    },
    "S5_eh_component_z": {
      "missing_observations": 80,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        0
      ],
      "prompts_without_observations": 0
    }
  },
  "warm_constraint|random": {
    "lhp": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "eh": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "entropy": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "leak_timecourse": {
      "missing_observations": 6,
      "observed_by_dose": [
        79,
        79,
        79,
        79,
        79,
        79
      ],
      "prompts_without_observations": 1
    },
    "carryover": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "ew": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "S2_eh_component": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "S5_eh_component": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "eh_z": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "lhp_z": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "S2_eh_component_z": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "S5_eh_component_z": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    }
  }
}
```

### Paired missing observations

```json
{
  "S1_missing_prompt_pairs": 0,
  "S3_missing_prompt_means": 1,
  "S5_missing_gap_observations": 0,
  "P2_control_missing_prompt_pairs": {
    "technicality": 0,
    "random": 0
  }
}
```

### Exploratory results (not confirmatory)

```json
{
  "label": "Exploratory only; not confirmatory",
  "warmth_slope": {
    "estimate": 0.0035227990852313507,
    "ci": [
      -0.05130051269365692,
      0.05807476464718402
    ],
    "confidence_level": 0.95,
    "bootstrap_valid": 10000,
    "bootstrap_missing": 0
  },
  "warmth_hostility_minus_control": {
    "technicality": {
      "estimate": 0.04832305990685467,
      "ci": [
        -0.004966140757772846,
        0.10824989332090386
      ],
      "confidence_level": 0.95,
      "bootstrap_valid": 10000,
      "bootstrap_missing": 0
    },
    "random": {
      "estimate": -0.07365964434036103,
      "ci": [
        -0.14256478878056575,
        -0.005976244906691151
      ],
      "confidence_level": 0.95,
      "bootstrap_valid": 10000,
      "bootstrap_missing": 0
    }
  },
  "all_raw_group_summaries": {
    "neutral|none|0": {
      "n": 80,
      "lexical_eligible": 77,
      "mean_lexical_hits": 0.012987012987012988,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 0,
      "non_latin_token_total": 0
    },
    "neutral|hostility|0.125": {
      "n": 80,
      "lexical_eligible": 79,
      "mean_lexical_hits": 0.012658227848101266,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 0,
      "non_latin_token_total": 0
    },
    "neutral|hostility|0.25": {
      "n": 80,
      "lexical_eligible": 74,
      "mean_lexical_hits": 0.04054054054054054,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 1,
      "non_latin_token_total": 0
    },
    "neutral|hostility|0.5": {
      "n": 80,
      "lexical_eligible": 79,
      "mean_lexical_hits": 0.0,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 0,
      "non_latin_token_total": 0
    },
    "neutral|hostility|0.75": {
      "n": 80,
      "lexical_eligible": 79,
      "mean_lexical_hits": 0.012658227848101266,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 2,
      "non_latin_token_total": 0
    },
    "neutral|hostility|1.0": {
      "n": 80,
      "lexical_eligible": 73,
      "mean_lexical_hits": 0.0136986301369863,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 2,
      "non_latin_token_total": 0
    },
    "neutral|technicality|0.125": {
      "n": 80,
      "lexical_eligible": 78,
      "mean_lexical_hits": 0.01282051282051282,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 0,
      "non_latin_token_total": 0
    },
    "neutral|technicality|0.25": {
      "n": 80,
      "lexical_eligible": 78,
      "mean_lexical_hits": 0.0,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 0,
      "non_latin_token_total": 0
    },
    "neutral|technicality|0.5": {
      "n": 80,
      "lexical_eligible": 78,
      "mean_lexical_hits": 0.0,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 0,
      "non_latin_token_total": 0
    },
    "neutral|technicality|0.75": {
      "n": 80,
      "lexical_eligible": 76,
      "mean_lexical_hits": 0.013157894736842105,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 0,
      "non_latin_token_total": 0
    },
    "neutral|technicality|1.0": {
      "n": 80,
      "lexical_eligible": 0,
      "mean_lexical_hits": null,
      "lexical_coherence_excluded": true,
      "offchannel_coherence_excluded": true,
      "emoji_total": null,
      "non_latin_token_total": null
    },
    "neutral|random|0.125": {
      "n": 80,
      "lexical_eligible": 78,
      "mean_lexical_hits": 0.01282051282051282,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 0,
      "non_latin_token_total": 0
    },
    "neutral|random|0.25": {
      "n": 80,
      "lexical_eligible": 78,
      "mean_lexical_hits": 0.02564102564102564,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 0,
      "non_latin_token_total": 0
    },
    "neutral|random|0.5": {
      "n": 80,
      "lexical_eligible": 77,
      "mean_lexical_hits": 0.0,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 0,
      "non_latin_token_total": 0
    },
    "neutral|random|0.75": {
      "n": 80,
      "lexical_eligible": 80,
      "mean_lexical_hits": 0.025,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 0,
      "non_latin_token_total": 0
    },
    "neutral|random|1.0": {
      "n": 80,
      "lexical_eligible": 77,
      "mean_lexical_hits": 0.025974025974025976,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 0,
      "non_latin_token_total": 0
    },
    "warm_constraint|none|0": {
      "n": 80,
      "lexical_eligible": 73,
      "mean_lexical_hits": 0.0136986301369863,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 0,
      "non_latin_token_total": 0
    },
    "warm_constraint|hostility|0.125": {
      "n": 80,
      "lexical_eligible": 73,
      "mean_lexical_hits": 0.0136986301369863,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 0,
      "non_latin_token_total": 0
    },
    "warm_constraint|hostility|0.25": {
      "n": 80,
      "lexical_eligible": 76,
      "mean_lexical_hits": 0.013157894736842105,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 0,
      "non_latin_token_total": 0
    },
    "warm_constraint|hostility|0.5": {
      "n": 80,
      "lexical_eligible": 76,
      "mean_lexical_hits": 0.02631578947368421,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 0,
      "non_latin_token_total": 0
    },
    "warm_constraint|hostility|0.75": {
      "n": 80,
      "lexical_eligible": 78,
      "mean_lexical_hits": 0.0,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 1,
      "non_latin_token_total": 0
    },
    "warm_constraint|hostility|1.0": {
      "n": 80,
      "lexical_eligible": 76,
      "mean_lexical_hits": 0.013157894736842105,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 7,
      "non_latin_token_total": 0
    },
    "warm_constraint|technicality|0.125": {
      "n": 80,
      "lexical_eligible": 76,
      "mean_lexical_hits": 0.0,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 0,
      "non_latin_token_total": 0
    },
    "warm_constraint|technicality|0.25": {
      "n": 80,
      "lexical_eligible": 77,
      "mean_lexical_hits": 0.0,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 0,
      "non_latin_token_total": 0
    },
    "warm_constraint|technicality|0.5": {
      "n": 80,
      "lexical_eligible": 76,
      "mean_lexical_hits": 0.0,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 0,
      "non_latin_token_total": 0
    },
    "warm_constraint|technicality|0.75": {
      "n": 80,
      "lexical_eligible": 78,
      "mean_lexical_hits": 0.01282051282051282,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 0,
      "non_latin_token_total": 0
    },
    "warm_constraint|technicality|1.0": {
      "n": 80,
      "lexical_eligible": 0,
      "mean_lexical_hits": null,
      "lexical_coherence_excluded": true,
      "offchannel_coherence_excluded": true,
      "emoji_total": null,
      "non_latin_token_total": null
    },
    "warm_constraint|random|0.125": {
      "n": 80,
      "lexical_eligible": 77,
      "mean_lexical_hits": 0.025974025974025976,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 0,
      "non_latin_token_total": 0
    },
    "warm_constraint|random|0.25": {
      "n": 80,
      "lexical_eligible": 76,
      "mean_lexical_hits": 0.0,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 0,
      "non_latin_token_total": 0
    },
    "warm_constraint|random|0.5": {
      "n": 80,
      "lexical_eligible": 77,
      "mean_lexical_hits": 0.0,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 0,
      "non_latin_token_total": 0
    },
    "warm_constraint|random|0.75": {
      "n": 80,
      "lexical_eligible": 78,
      "mean_lexical_hits": 0.0,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 0,
      "non_latin_token_total": 0
    },
    "warm_constraint|random|1.0": {
      "n": 80,
      "lexical_eligible": 79,
      "mean_lexical_hits": 0.0,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 0,
      "non_latin_token_total": 0
    }
  }
}
```
## meta-llama/Llama-3.2-3B-Instruct

| Prediction / component | Estimate | Interval | Verdict |
|---|---:|---|---|
| P1 / hostility | 2.7623959398849487 | 97.5%: [2.693944463594816, 2.8292104149061275] | supported |
| P1 / hostility_minus_technicality | 1.1768309083406499 | 97.5%: [1.108421855854212, 1.2468493642726657] | supported |
| P1 / hostility_minus_random | 2.7236825808686587 | 97.5%: [2.6470310209364785, 2.8030927830603147] | supported |
| P2 / hostility | 0.226273201033473 | 97.5%: [0.19121632932685317, 0.26230420966632667] | not supported |
| P2 / hostility_minus_technicality | -0.20049953646957874 | 97.5%: [-0.2530166625091806, -0.1464203460048881] | not supported |
| P2 / hostility_minus_random | -0.05029960162937641 | 97.5%: [-0.10737152892164885, 0.007726757507771262] | not supported |
| S1 / S1 | 0.14724787138402462 | 95%: [0.10224350982345642, 0.19144221150316298] | not supported |
| S2 / S2 | -0.04402355982311967 | 95%: [-0.18445420161034567, 0.09326569788862646] | not supported |
| S3 / S3 | 0.05279475852936836 | 95%: [0.014935921926353343, 0.08952422899213464] | supported |
| S4 / S4 | 0.17493999933555227 | 95%: [0.08367015053824105, 0.2626492395182734] | supported |
| S5 / delta_bic | -6.747770765324082 | 95%: [-10.341113263830199, 2.1370320964637775] | not supported |

### Specificity controls

| Primary / control | Control estimate and interval | Hostility minus control and interval | Contrast met |
|---|---|---|---|
| P1 / technicality | 1.5855650315442988; [1.5131417171508699, 1.6562313986597532] | 1.1768309083406499; [1.108421855854212, 1.2468493642726657] | True |
| P1 / random | 0.03871335901628992; [0.0043293301008375164, 0.07190615589306418] | 2.7236825808686587; [2.6470310209364785, 2.8030927830603147] | True |
| P2 / technicality | 0.4267727375030518; [0.38643917025066915, 0.46741077765822414] | -0.20049953646957874; [-0.2530166625091806, -0.1464203460048881] | True |
| P2 / random | 0.27657280266284945; [0.2229984567500651, 0.3306853646039966] | -0.05029960162937641; [-0.10737152892164885, 0.007726757507771262] | False |

### Coherence exclusions

```json
[
  {
    "condition": "neutral",
    "direction": "technicality",
    "normalized_alpha": 0.75,
    "median_ppl_ratio": 4.816605121241157
  },
  {
    "condition": "neutral",
    "direction": "technicality",
    "normalized_alpha": 1.0,
    "median_ppl_ratio": 12.350587674101085
  },
  {
    "condition": "warm_constraint",
    "direction": "technicality",
    "normalized_alpha": 0.75,
    "median_ppl_ratio": 7.4289280654918475
  },
  {
    "condition": "warm_constraint",
    "direction": "technicality",
    "normalized_alpha": 1.0,
    "median_ppl_ratio": 14.400149914593074
  }
]
```

### Missing observations

```json
{
  "neutral|hostility": {
    "lhp": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "eh": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "entropy": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "leak_timecourse": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "carryover": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "ew": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "S2_eh_component": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "S5_eh_component": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "eh_z": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "lhp_z": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "S2_eh_component_z": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "S5_eh_component_z": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    }
  },
  "neutral|technicality": {
    "lhp": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "eh": {
      "missing_observations": 160,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        0,
        0
      ],
      "prompts_without_observations": 0
    },
    "entropy": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "leak_timecourse": {
      "missing_observations": 161,
      "observed_by_dose": [
        80,
        80,
        79,
        80,
        0,
        0
      ],
      "prompts_without_observations": 0
    },
    "carryover": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "ew": {
      "missing_observations": 160,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        0,
        0
      ],
      "prompts_without_observations": 0
    },
    "S2_eh_component": {
      "missing_observations": 160,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        0,
        0
      ],
      "prompts_without_observations": 0
    },
    "S5_eh_component": {
      "missing_observations": 160,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        0,
        0
      ],
      "prompts_without_observations": 0
    },
    "eh_z": {
      "missing_observations": 160,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        0,
        0
      ],
      "prompts_without_observations": 0
    },
    "lhp_z": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "S2_eh_component_z": {
      "missing_observations": 160,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        0,
        0
      ],
      "prompts_without_observations": 0
    },
    "S5_eh_component_z": {
      "missing_observations": 160,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        0,
        0
      ],
      "prompts_without_observations": 0
    }
  },
  "neutral|random": {
    "lhp": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "eh": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "entropy": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "leak_timecourse": {
      "missing_observations": 1,
      "observed_by_dose": [
        80,
        79,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "carryover": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "ew": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "S2_eh_component": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "S5_eh_component": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "eh_z": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "lhp_z": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "S2_eh_component_z": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "S5_eh_component_z": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    }
  },
  "warm_constraint|hostility": {
    "lhp": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "eh": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "entropy": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "leak_timecourse": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "carryover": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "ew": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "S2_eh_component": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "S5_eh_component": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "eh_z": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "lhp_z": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "S2_eh_component_z": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "S5_eh_component_z": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    }
  },
  "warm_constraint|technicality": {
    "lhp": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "eh": {
      "missing_observations": 160,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        0,
        0
      ],
      "prompts_without_observations": 0
    },
    "entropy": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "leak_timecourse": {
      "missing_observations": 160,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        0,
        0
      ],
      "prompts_without_observations": 0
    },
    "carryover": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "ew": {
      "missing_observations": 160,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        0,
        0
      ],
      "prompts_without_observations": 0
    },
    "S2_eh_component": {
      "missing_observations": 160,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        0,
        0
      ],
      "prompts_without_observations": 0
    },
    "S5_eh_component": {
      "missing_observations": 160,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        0,
        0
      ],
      "prompts_without_observations": 0
    },
    "eh_z": {
      "missing_observations": 160,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        0,
        0
      ],
      "prompts_without_observations": 0
    },
    "lhp_z": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "S2_eh_component_z": {
      "missing_observations": 160,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        0,
        0
      ],
      "prompts_without_observations": 0
    },
    "S5_eh_component_z": {
      "missing_observations": 160,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        0,
        0
      ],
      "prompts_without_observations": 0
    }
  },
  "warm_constraint|random": {
    "lhp": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "eh": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "entropy": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "leak_timecourse": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "carryover": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "ew": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "S2_eh_component": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "S5_eh_component": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "eh_z": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "lhp_z": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "S2_eh_component_z": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "S5_eh_component_z": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    }
  }
}
```

### Paired missing observations

```json
{
  "S1_missing_prompt_pairs": 0,
  "S3_missing_prompt_means": 0,
  "S5_missing_gap_observations": 0,
  "P2_control_missing_prompt_pairs": {
    "technicality": 0,
    "random": 0
  }
}
```

### Exploratory results (not confirmatory)

```json
{
  "label": "Exploratory only; not confirmatory",
  "warmth_slope": {
    "estimate": -0.10622435853663391,
    "ci": [
      -0.18025833050118859,
      -0.03425825922498418
    ],
    "confidence_level": 0.95,
    "bootstrap_valid": 10000,
    "bootstrap_missing": 0
  },
  "warmth_hostility_minus_control": {
    "technicality": {
      "estimate": -0.17079564587766727,
      "ci": [
        -0.35233681628135827,
        0.01165056850889324
      ],
      "confidence_level": 0.95,
      "bootstrap_valid": 10000,
      "bootstrap_missing": 0
    },
    "random": {
      "estimate": -0.031853349643612375,
      "ci": [
        -0.09978456642776329,
        0.037176476480699695
      ],
      "confidence_level": 0.95,
      "bootstrap_valid": 10000,
      "bootstrap_missing": 0
    }
  },
  "all_raw_group_summaries": {
    "neutral|none|0": {
      "n": 80,
      "lexical_eligible": 79,
      "mean_lexical_hits": 0.0,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 0,
      "non_latin_token_total": 0
    },
    "neutral|hostility|0.125": {
      "n": 80,
      "lexical_eligible": 78,
      "mean_lexical_hits": 0.01282051282051282,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 0,
      "non_latin_token_total": 0
    },
    "neutral|hostility|0.25": {
      "n": 80,
      "lexical_eligible": 75,
      "mean_lexical_hits": 0.0,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 0,
      "non_latin_token_total": 0
    },
    "neutral|hostility|0.5": {
      "n": 80,
      "lexical_eligible": 76,
      "mean_lexical_hits": 0.09210526315789473,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 0,
      "non_latin_token_total": 0
    },
    "neutral|hostility|0.75": {
      "n": 80,
      "lexical_eligible": 74,
      "mean_lexical_hits": 0.02702702702702703,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 0,
      "non_latin_token_total": 0
    },
    "neutral|hostility|1.0": {
      "n": 80,
      "lexical_eligible": 72,
      "mean_lexical_hits": 0.1111111111111111,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 0,
      "non_latin_token_total": 0
    },
    "neutral|technicality|0.125": {
      "n": 80,
      "lexical_eligible": 78,
      "mean_lexical_hits": 0.0,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 0,
      "non_latin_token_total": 0
    },
    "neutral|technicality|0.25": {
      "n": 80,
      "lexical_eligible": 78,
      "mean_lexical_hits": 0.01282051282051282,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 0,
      "non_latin_token_total": 0
    },
    "neutral|technicality|0.5": {
      "n": 80,
      "lexical_eligible": 79,
      "mean_lexical_hits": 0.0,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 0,
      "non_latin_token_total": 0
    },
    "neutral|technicality|0.75": {
      "n": 80,
      "lexical_eligible": 0,
      "mean_lexical_hits": null,
      "lexical_coherence_excluded": true,
      "offchannel_coherence_excluded": true,
      "emoji_total": null,
      "non_latin_token_total": null
    },
    "neutral|technicality|1.0": {
      "n": 80,
      "lexical_eligible": 0,
      "mean_lexical_hits": null,
      "lexical_coherence_excluded": true,
      "offchannel_coherence_excluded": true,
      "emoji_total": null,
      "non_latin_token_total": null
    },
    "neutral|random|0.125": {
      "n": 80,
      "lexical_eligible": 79,
      "mean_lexical_hits": 0.0,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 0,
      "non_latin_token_total": 0
    },
    "neutral|random|0.25": {
      "n": 80,
      "lexical_eligible": 78,
      "mean_lexical_hits": 0.01282051282051282,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 0,
      "non_latin_token_total": 0
    },
    "neutral|random|0.5": {
      "n": 80,
      "lexical_eligible": 77,
      "mean_lexical_hits": 0.0,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 0,
      "non_latin_token_total": 0
    },
    "neutral|random|0.75": {
      "n": 80,
      "lexical_eligible": 78,
      "mean_lexical_hits": 0.0,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 0,
      "non_latin_token_total": 0
    },
    "neutral|random|1.0": {
      "n": 80,
      "lexical_eligible": 78,
      "mean_lexical_hits": 0.01282051282051282,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 0,
      "non_latin_token_total": 0
    },
    "warm_constraint|none|0": {
      "n": 80,
      "lexical_eligible": 77,
      "mean_lexical_hits": 0.012987012987012988,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 0,
      "non_latin_token_total": 0
    },
    "warm_constraint|hostility|0.125": {
      "n": 80,
      "lexical_eligible": 72,
      "mean_lexical_hits": 0.0,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 0,
      "non_latin_token_total": 0
    },
    "warm_constraint|hostility|0.25": {
      "n": 80,
      "lexical_eligible": 74,
      "mean_lexical_hits": 0.05405405405405406,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 0,
      "non_latin_token_total": 0
    },
    "warm_constraint|hostility|0.5": {
      "n": 80,
      "lexical_eligible": 74,
      "mean_lexical_hits": 0.05405405405405406,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 0,
      "non_latin_token_total": 0
    },
    "warm_constraint|hostility|0.75": {
      "n": 80,
      "lexical_eligible": 76,
      "mean_lexical_hits": 0.14473684210526316,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 0,
      "non_latin_token_total": 0
    },
    "warm_constraint|hostility|1.0": {
      "n": 80,
      "lexical_eligible": 67,
      "mean_lexical_hits": 0.1791044776119403,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 0,
      "non_latin_token_total": 0
    },
    "warm_constraint|technicality|0.125": {
      "n": 80,
      "lexical_eligible": 74,
      "mean_lexical_hits": 0.013513513513513514,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 0,
      "non_latin_token_total": 0
    },
    "warm_constraint|technicality|0.25": {
      "n": 80,
      "lexical_eligible": 74,
      "mean_lexical_hits": 0.0,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 0,
      "non_latin_token_total": 0
    },
    "warm_constraint|technicality|0.5": {
      "n": 80,
      "lexical_eligible": 77,
      "mean_lexical_hits": 0.012987012987012988,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 0,
      "non_latin_token_total": 0
    },
    "warm_constraint|technicality|0.75": {
      "n": 80,
      "lexical_eligible": 0,
      "mean_lexical_hits": null,
      "lexical_coherence_excluded": true,
      "offchannel_coherence_excluded": true,
      "emoji_total": null,
      "non_latin_token_total": null
    },
    "warm_constraint|technicality|1.0": {
      "n": 80,
      "lexical_eligible": 0,
      "mean_lexical_hits": null,
      "lexical_coherence_excluded": true,
      "offchannel_coherence_excluded": true,
      "emoji_total": null,
      "non_latin_token_total": null
    },
    "warm_constraint|random|0.125": {
      "n": 80,
      "lexical_eligible": 75,
      "mean_lexical_hits": 0.02666666666666667,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 0,
      "non_latin_token_total": 0
    },
    "warm_constraint|random|0.25": {
      "n": 80,
      "lexical_eligible": 72,
      "mean_lexical_hits": 0.0,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 0,
      "non_latin_token_total": 0
    },
    "warm_constraint|random|0.5": {
      "n": 80,
      "lexical_eligible": 74,
      "mean_lexical_hits": 0.0,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 0,
      "non_latin_token_total": 0
    },
    "warm_constraint|random|0.75": {
      "n": 80,
      "lexical_eligible": 77,
      "mean_lexical_hits": 0.012987012987012988,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 0,
      "non_latin_token_total": 0
    },
    "warm_constraint|random|1.0": {
      "n": 80,
      "lexical_eligible": 76,
      "mean_lexical_hits": 0.039473684210526314,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 0,
      "non_latin_token_total": 0
    }
  }
}
```
## microsoft/Phi-3.5-mini-instruct

| Prediction / component | Estimate | Interval | Verdict |
|---|---:|---|---|
| P1 / hostility | 1.5459393004491817 | 97.5%: [1.436365162748615, 1.6495213619578324] | supported |
| P1 / hostility_minus_technicality | 0.3362958939010523 | 97.5%: [0.2718187103594518, 0.40251000860136443] | supported |
| P1 / hostility_minus_random | 1.6682752572074364 | 97.5%: [1.545848922763362, 1.7796882908904614] | supported |
| P2 / hostility | 0.1032272469252348 | 97.5%: [0.03613741606473923, 0.18153846321161834] | not supported |
| P2 / hostility_minus_technicality | 0.0807686384767294 | 97.5%: [0.011037249825894832, 0.16159221744164823] | not supported |
| P2 / hostility_minus_random | 0.10740934945642948 | 97.5%: [0.034879150204360485, 0.18970255175139764] | not supported |
| S1 / S1 | 0.09495686292648316 | 95%: [0.037279142523184434, 0.15934732764959333] | not supported |
| S2 / S2 | -0.5012435541426338 | 95%: [-0.8175922694372628, -0.2015031413677272] | supported |
| S3 / S3 | 0.040502342491587726 | 95%: [0.01424484302218086, 0.06652494874204269] | supported |
| S4 / S4 | 0.05977487030940487 | 95%: [0.007416003664637454, 0.11073790761395258] | supported |
| S5 / delta_bic | -8.045745172111754 | 95%: [-10.964834833650192, -1.5503825344809357] | not supported |

### Specificity controls

| Primary / control | Control estimate and interval | Hostility minus control and interval | Contrast met |
|---|---|---|---|
| P1 / technicality | 1.2096434065481294; [1.111821894398165, 1.3010186799768488] | 0.3362958939010523; [0.2718187103594518, 0.40251000860136443] | True |
| P1 / random | -0.1223359567582548; [-0.1676920178907337, -0.0764847785827209] | 1.6682752572074364; [1.545848922763362, 1.7796882908904614] | True |
| P2 / technicality | 0.0224586084485054; [0.0012090576067566876, 0.0405888565815986] | 0.0807686384767294; [0.011037249825894832, 0.16159221744164823] | False |
| P2 / random | -0.004182102531194687; [-0.029938552547246214, 0.015885666674003034] | 0.10740934945642948; [0.034879150204360485, 0.18970255175139764] | False |

### Coherence exclusions

```json
[]
```

### Missing observations

```json
{
  "neutral|hostility": {
    "lhp": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "eh": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "entropy": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "leak_timecourse": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "carryover": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "ew": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "S2_eh_component": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "S5_eh_component": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "eh_z": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "lhp_z": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "S2_eh_component_z": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "S5_eh_component_z": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    }
  },
  "neutral|technicality": {
    "lhp": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "eh": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "entropy": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "leak_timecourse": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "carryover": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "ew": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "S2_eh_component": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "S5_eh_component": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "eh_z": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "lhp_z": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "S2_eh_component_z": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "S5_eh_component_z": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    }
  },
  "neutral|random": {
    "lhp": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "eh": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "entropy": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "leak_timecourse": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "carryover": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "ew": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "S2_eh_component": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "S5_eh_component": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "eh_z": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "lhp_z": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "S2_eh_component_z": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "S5_eh_component_z": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    }
  },
  "warm_constraint|hostility": {
    "lhp": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "eh": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "entropy": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "leak_timecourse": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "carryover": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "ew": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "S2_eh_component": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "S5_eh_component": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "eh_z": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "lhp_z": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "S2_eh_component_z": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "S5_eh_component_z": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    }
  },
  "warm_constraint|technicality": {
    "lhp": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "eh": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "entropy": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "leak_timecourse": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "carryover": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "ew": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "S2_eh_component": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "S5_eh_component": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "eh_z": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "lhp_z": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "S2_eh_component_z": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "S5_eh_component_z": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    }
  },
  "warm_constraint|random": {
    "lhp": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "eh": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "entropy": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "leak_timecourse": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "carryover": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "ew": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "S2_eh_component": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "S5_eh_component": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "eh_z": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "lhp_z": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "S2_eh_component_z": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    },
    "S5_eh_component_z": {
      "missing_observations": 0,
      "observed_by_dose": [
        80,
        80,
        80,
        80,
        80,
        80
      ],
      "prompts_without_observations": 0
    }
  }
}
```

### Paired missing observations

```json
{
  "S1_missing_prompt_pairs": 0,
  "S3_missing_prompt_means": 0,
  "S5_missing_gap_observations": 0,
  "P2_control_missing_prompt_pairs": {
    "technicality": 0,
    "random": 0
  }
}
```

### Exploratory results (not confirmatory)

```json
{
  "label": "Exploratory only; not confirmatory",
  "warmth_slope": {
    "estimate": 0.060879823908356855,
    "ci": [
      -0.0018904564210357575,
      0.12665384028241264
    ],
    "confidence_level": 0.95,
    "bootstrap_valid": 10000,
    "bootstrap_missing": 0
  },
  "warmth_hostility_minus_control": {
    "technicality": {
      "estimate": 0.11777991738954657,
      "ci": [
        0.05568949616644961,
        0.18679537926552855
      ],
      "confidence_level": 0.95,
      "bootstrap_valid": 10000,
      "bootstrap_missing": 0
    },
    "random": {
      "estimate": 0.08047870317348402,
      "ci": [
        0.008968764831596913,
        0.1561651555888361
      ],
      "confidence_level": 0.95,
      "bootstrap_valid": 10000,
      "bootstrap_missing": 0
    }
  },
  "all_raw_group_summaries": {
    "neutral|none|0": {
      "n": 80,
      "lexical_eligible": 77,
      "mean_lexical_hits": 0.025974025974025976,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 0,
      "non_latin_token_total": 0
    },
    "neutral|hostility|0.125": {
      "n": 80,
      "lexical_eligible": 75,
      "mean_lexical_hits": 0.013333333333333334,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 0,
      "non_latin_token_total": 0
    },
    "neutral|hostility|0.25": {
      "n": 80,
      "lexical_eligible": 75,
      "mean_lexical_hits": 0.0,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 0,
      "non_latin_token_total": 0
    },
    "neutral|hostility|0.5": {
      "n": 80,
      "lexical_eligible": 77,
      "mean_lexical_hits": 0.012987012987012988,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 0,
      "non_latin_token_total": 0
    },
    "neutral|hostility|0.75": {
      "n": 80,
      "lexical_eligible": 71,
      "mean_lexical_hits": 0.0,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 0,
      "non_latin_token_total": 0
    },
    "neutral|hostility|1.0": {
      "n": 80,
      "lexical_eligible": 67,
      "mean_lexical_hits": 0.014925373134328358,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 0,
      "non_latin_token_total": 0
    },
    "neutral|technicality|0.125": {
      "n": 80,
      "lexical_eligible": 74,
      "mean_lexical_hits": 0.02702702702702703,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 0,
      "non_latin_token_total": 0
    },
    "neutral|technicality|0.25": {
      "n": 80,
      "lexical_eligible": 76,
      "mean_lexical_hits": 0.013157894736842105,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 0,
      "non_latin_token_total": 0
    },
    "neutral|technicality|0.5": {
      "n": 80,
      "lexical_eligible": 73,
      "mean_lexical_hits": 0.0136986301369863,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 0,
      "non_latin_token_total": 0
    },
    "neutral|technicality|0.75": {
      "n": 80,
      "lexical_eligible": 78,
      "mean_lexical_hits": 0.0,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 0,
      "non_latin_token_total": 0
    },
    "neutral|technicality|1.0": {
      "n": 80,
      "lexical_eligible": 75,
      "mean_lexical_hits": 0.013333333333333334,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 0,
      "non_latin_token_total": 0
    },
    "neutral|random|0.125": {
      "n": 80,
      "lexical_eligible": 77,
      "mean_lexical_hits": 0.012987012987012988,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 0,
      "non_latin_token_total": 0
    },
    "neutral|random|0.25": {
      "n": 80,
      "lexical_eligible": 76,
      "mean_lexical_hits": 0.0,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 0,
      "non_latin_token_total": 0
    },
    "neutral|random|0.5": {
      "n": 80,
      "lexical_eligible": 76,
      "mean_lexical_hits": 0.02631578947368421,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 0,
      "non_latin_token_total": 0
    },
    "neutral|random|0.75": {
      "n": 80,
      "lexical_eligible": 75,
      "mean_lexical_hits": 0.013333333333333334,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 0,
      "non_latin_token_total": 0
    },
    "neutral|random|1.0": {
      "n": 80,
      "lexical_eligible": 74,
      "mean_lexical_hits": 0.013513513513513514,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 0,
      "non_latin_token_total": 0
    },
    "warm_constraint|none|0": {
      "n": 80,
      "lexical_eligible": 78,
      "mean_lexical_hits": 0.01282051282051282,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 0,
      "non_latin_token_total": 0
    },
    "warm_constraint|hostility|0.125": {
      "n": 80,
      "lexical_eligible": 74,
      "mean_lexical_hits": 0.0,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 0,
      "non_latin_token_total": 0
    },
    "warm_constraint|hostility|0.25": {
      "n": 80,
      "lexical_eligible": 77,
      "mean_lexical_hits": 0.0,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 0,
      "non_latin_token_total": 0
    },
    "warm_constraint|hostility|0.5": {
      "n": 80,
      "lexical_eligible": 79,
      "mean_lexical_hits": 0.012658227848101266,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 0,
      "non_latin_token_total": 0
    },
    "warm_constraint|hostility|0.75": {
      "n": 80,
      "lexical_eligible": 78,
      "mean_lexical_hits": 0.01282051282051282,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 0,
      "non_latin_token_total": 0
    },
    "warm_constraint|hostility|1.0": {
      "n": 80,
      "lexical_eligible": 76,
      "mean_lexical_hits": 0.013157894736842105,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 0,
      "non_latin_token_total": 0
    },
    "warm_constraint|technicality|0.125": {
      "n": 80,
      "lexical_eligible": 76,
      "mean_lexical_hits": 0.013157894736842105,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 0,
      "non_latin_token_total": 0
    },
    "warm_constraint|technicality|0.25": {
      "n": 80,
      "lexical_eligible": 75,
      "mean_lexical_hits": 0.0,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 0,
      "non_latin_token_total": 0
    },
    "warm_constraint|technicality|0.5": {
      "n": 80,
      "lexical_eligible": 75,
      "mean_lexical_hits": 0.0,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 0,
      "non_latin_token_total": 0
    },
    "warm_constraint|technicality|0.75": {
      "n": 80,
      "lexical_eligible": 73,
      "mean_lexical_hits": 0.0,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 0,
      "non_latin_token_total": 0
    },
    "warm_constraint|technicality|1.0": {
      "n": 80,
      "lexical_eligible": 75,
      "mean_lexical_hits": 0.0,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 0,
      "non_latin_token_total": 2
    },
    "warm_constraint|random|0.125": {
      "n": 80,
      "lexical_eligible": 75,
      "mean_lexical_hits": 0.0,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 0,
      "non_latin_token_total": 0
    },
    "warm_constraint|random|0.25": {
      "n": 80,
      "lexical_eligible": 74,
      "mean_lexical_hits": 0.0,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 0,
      "non_latin_token_total": 0
    },
    "warm_constraint|random|0.5": {
      "n": 80,
      "lexical_eligible": 77,
      "mean_lexical_hits": 0.0,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 0,
      "non_latin_token_total": 0
    },
    "warm_constraint|random|0.75": {
      "n": 80,
      "lexical_eligible": 76,
      "mean_lexical_hits": 0.0,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 0,
      "non_latin_token_total": 0
    },
    "warm_constraint|random|1.0": {
      "n": 80,
      "lexical_eligible": 76,
      "mean_lexical_hits": 0.0,
      "lexical_coherence_excluded": false,
      "offchannel_coherence_excluded": false,
      "emoji_total": 0,
      "non_latin_token_total": 0
    }
  }
}
```

## Generality and model inclusion

```json
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
```

## Full deviation log

# Deviations — Study 2

## Affecting specified quantities
(none)

## Engineering

- Stage 0: copied Study 1 inference and metrics into Study 2; removed the exploratory layerwise logit lens as specified. All execution uses Study 2 as its working directory and the shared environment without modifying it. Bytecode writes are disabled. Study 1 files are read only.

### Model access — meta-llama/Llama-3.2-3B-Instruct

Attempted the configured model config using existing library authentication for gated models. Exact error:

```text
GatedRepoError: 403 Client Error. (Request ID: Root=1-6ac2c3b8-766b4dcc0ead2fc203dff064;8b6320a1-a72a-441a-a6ca-054a8bf3cf42)

Cannot access gated repo for url https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct/resolve/main/config.json.
Access to model meta-llama/Llama-3.2-3B-Instruct is restricted and you are not in the authorized list. Visit https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct to ask for access.
```

### Stage 1 stopped

```text
Traceback (most recent call last):
  File "/Users/arthursu/Projects/affect-suppression-steering/study2/src/run_smoke.py", line 91, in <module>
    main()
  File "/Users/arthursu/Projects/affect-suppression-steering/study2/src/run_smoke.py", line 86, in main
    run(spec)
  File "/Users/arthursu/Projects/affect-suppression-steering/study2/src/run_smoke.py", line 48, in run
    row['ratings'] = model.ratings(messages, generation, question)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/arthursu/Projects/affect-suppression-steering/.venv/lib/python3.12/site-packages/torch/utils/_contextlib.py", line 124, in decorate_context
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/arthursu/Projects/affect-suppression-steering/study2/src/model_utils.py", line 139, in ratings
    return {'text_only':self.rating(text_logits), 'hidden':self.rating(hidden_logits), 'template_prefix_exact':exact, 'identical_visible_ids':True}
                        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/arthursu/Projects/affect-suppression-steering/study2/src/model_utils.py", line 114, in rating
    raise RuntimeError('A rating digit does not have a single token')
RuntimeError: A rating digit does not have a single token
```
No scientific parameter changed; no automatic retry.

### Engineering — Phi isolated-digit tokenizer prefix

Phi smoke encountered `RuntimeError: A rating digit does not have a single token`. Tokenizer-only inspection (results/phi_digit_tokenization.json) showed each isolated digit encodes as `[29871, digit_id]`, where 29871 is SentencePiece `▁` and the second token is the literal digit `0`–`9`. The measure requires next-token probabilities of those literal digit tokens; the shared helper now removes only this verified tokenizer-added dummy prefix when resolving digit IDs. No conversation tokens, forward passes, logits, probability normalization, precision, or generation settings change. Exact source diff: results/phi_digit_engineering.diff. The original error is preserved at data/_superseded/20261004T143055_phi_smoke_tokenizer/stage1_error.txt. Qwen completed records remain unchanged. Phi had no completed saved smoke cell; resume uses its identical original prompt and seed.

### Engineering — Study 2 runner generalization

Copied and generalized Study 1 extraction, norm measurement, generation and checkpoint logic. Model IDs, slugs and per-model immutable output paths come from Study 2 config. The new dose-selection implementation evaluates coherence in increasing order until first failure, then scores saved generations at every coherent candidate, using the fixed classifier and 10,000 paired prompt resamples. It selects the largest candidate with a positive CI lower bound, or records the specified exclusion. Baseline generations and classifier scores are checkpointed once. No Study 1 data or directions are reused. Runner and analysis drafts were prepared while Phi downloaded; none were executed before Stage 1 completion.

### Engineering — independent synthetic checks during calibration

The CPU-only Stage 2b synthetic checks run while Stage 2 Qwen calibration proceeds, without accessing its outputs or test prompts. Model generations remain sequential. Synthetic progress is logged separately to avoid concurrent STATUS.md rewrites; the agent records completion in STATUS.md. Analysis freezing and timing remain after model dose selection.

### Stage 2 completion audit

Both available models passed their registered manipulation-based selection rule. Read-only checks reproduced directions from saved extraction sums, checked residual-norm pooling, all cell seeds and counts, coherent-range stopping, bootstrap intervals, selected maxima and immutable hashes. Qwen: 400 dose cells, 360 fixed-classifier scores, alpha_max 0.16, first coherence failure 0.18. Phi: 160 dose cells, 120 scores, alpha_max 0.04, first failure 0.06. No scientific setting or data record was changed.

## Amendment 3.1 implementation

The reviewer changed PREREG.md and config.yaml externally during Stage 2b timing. The agent detected `AssertionError: Hash mismatch: PREREG.md`, attempted to stop the known timing job, and found that it had already completed all six calibration-only cells. No Stage 3 data exist. The reviewer then explicitly authorized Amendment 3.1 in conversation. The v3.0 approval was intentionally renamed by the reviewer; the agent did not create or alter any approval.

The authorized amendment limits the 4.0 gate to the configured text-scored fields; LHP, carryover and entropy remain available. The agent will implement this list-driven rule, repeat all synthetic checks, and freeze the new analysis by hash. Old analysis source, synthetic inputs/results, specification bytes, and manifest are preserved at data/_superseded/20261004T162639_v3.0_analysis. The new supplied SHA-256 hashes were independently verified before updating the specification manifest.

Comparing v3.0 and v3.1 YAML after removing only the analysis section and preregistration-version label confirmed exact equality of all generation, extraction, dose-selection, model, prompt, classifier and measure settings. Qwen and Phi directions, norms and write-once calibrations are retained unchanged. Completed timing cells are retained byte-for-byte; their mixed file-hash provenance reflects the external edit during the run, not a change in their generation settings. Details: results/amendment3_1_compatibility.json.

Engineering: Stage 1 accepts an explicit configured model slug after a fresh access check, preserving the historical Stage 0 access record. Llama config access succeeded on 2026-10-04 at 16:31 local time; model_access_updates.jsonl records the check. No inference settings changed.

Engineering: The first v3.1 synthetic run passed estimator assertions but its final guard assertion failed with `AssertionError: assert not Path('PREREG_APPROVED').exists()` because the reviewer created the new matching approval concurrently. The absent-approval guard now runs in an isolated empty fixture directory; no approval file is created or edited. Earlier check outputs preserved at data/_superseded/20261004T163319_v31_guard_fixture. All checks rerun. Deposit remains absent.

Engineering: Check rerun stopped with `FileExistsError: data/synthetic/excluded_top.jsonl`: a write-once fixture from the first attempt remained. All previous synthetic fixtures and partial outputs preserved in data/_superseded/20261004T163347_synthetic_rerun_checkpoint before a clean full rerun. No scientific data or estimator changes.

Amendment 3.1 implementation complete: analyze.py reads analysis.coherence_gate_applies_to, masks only listed measures, handles S2/S5 EH components separately, and retains all LHP/carryover/entropy observations. Exact change: results/amendment3_1_analysis.diff. All planted/null, independent OLS/BIC, top-control, hostility leakage, configuration-driven mask, true missingness, strict control contrast, and confidence-interval checks passed with 10,000 resamples. Timing resumed and skipped all six complete Qwen/Phi calibration cells without loading a model or regenerating; mixed historical hashes accepted only in timing mode after archived/current non-analysis config equality. Qwen and Phi immutable calibration hashes independently reverified unchanged.

Additional independent checks passed for lexical/off-channel gate omissions and config-driven separate S2/S5 EH masks. analyze.py frozen by SHA-256 in results/analysis_frozen.sha256 after successful checks and Qwen/Phi timing resume. The new reviewer-created approval hashes match; it was not created or edited by this agent. Llama remains in Stage 1 download.

### Engineering — detached follow-through

Added project-local autopilot, durable detached worker wrapper, and a format-only report renderer. Every ten minutes, the watcher checks access/approval/deposit readiness; main runs are sequential, only for manipulation-passing models. Public Zenodo files must match the approved PREREG/config hashes (including archive members); the verification is recorded before main dispatch. Saved successful cells remain immutable and are skipped on resume. Worker exit records and locks prevent duplicate jobs; recorded failures block. Interrupted complete analysis/report artifacts are verified and adopted; incomplete derived outputs are preserved before rerunning unchanged code. Main-run approval/specification/calibration checks occur before and after each cell; an interrupted-specification cell is preserved outside main raw data. STATUS writes now use a shared lock. No scientific quantity or frozen analyze.py changed. Project-local launchd services will restart crashes within the current login session; automatic registration after reboot would require writing outside study2, which is prohibited, so reboot requires re-running the local starter.

Watcher verification: offline guard/dispatch tests passed, public archive byte-matching test passed (wrong config rejected), and interrupted-job/derived-output recovery tests passed. These tests mock dispatch and never create PREREG_APPROVED or run main generations. Results: results/autopilot_checks.json, deposit_verification_checks.json, autopilot_recovery_checks.json.

Independent deposit verification (2026-10-04 17:57 PDT): reviewer-created ZENODO_DEPOSIT.md identifies Study 2 DOI 10.5281/zenodo.23147672. Zenodo API confirms published record 23147672; downloaded archive PREREG.md/config.yaml SHA-256 values match the approved local files exactly. Saved evidence: results/deposit_independent_verification.json. No Stage 3 data exist. Frozen analysis still d1aaedc674314fff939fecb85dec454fd4a7e5c93ad4c6fc3c282af899f89564; Qwen/Phi calibration hashes unchanged.

Detached services launched and independently verified at 2026-10-04T17:59:50.993901-07:00: watcher PID 81631, persistent caffeinate PID 81626. Both have parent PID 1 and independent process groups. macOS power assertions confirm indefinite prevention of system/display idle sleep. Project-local launchd crash restart is registered; reboot/login re-registration remains manual because no outside-study2 files may be installed. No Stage 3 data at handoff. Evidence: results/autopilot_service_verification.json.

