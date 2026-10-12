# Study 3 v0.4 analysis

| Hypothesis | Verdict | Component | Estimate | CI |
|---|---|---|---:|---|
| P1 | supported | hostility | -1.236446 | 97.5% [-1.272471, -1.200086] |
| P1 | supported | hostility-minus-technicality | -1.233691 | 97.5% [-1.282587, -1.186687] |
| P1 | supported | hostility-minus-random | -1.231959 | 97.5% [-1.278076, -1.184633] |
| P2 | not supported | hostility | -0.003544 | 97.5% [-0.016613, 0.009325] |
| P2 | not supported | hostility-minus-technicality | -0.002611 | 97.5% [-0.015498, 0.009549] |
| P2 | not supported | hostility-minus-random | -0.006891 | 97.5% [-0.019695, 0.005649] |
| S1 | supported | X_think | -0.812810 | 95% [-0.830342, -0.795092] |
| S2 | supported | delta_X | -0.831296 | 95% [-0.855518, -0.807379] |
| S3 | not supported | direct:hostility | -0.112978 | 95% [-0.432845, 0.202682] |
| S3 | not supported | direct:hostility-minus-technicality | 0.169522 | 95% [-0.147631, 0.476908] |
| S3 | not supported | direct:hostility-minus-random | 0.013184 | 95% [-0.292101, 0.330018] |
| S3 | not supported | think:hostility | 0.121194 | 95% [-0.188538, 0.433009] |
| S3 | not supported | think:hostility-minus-technicality | 0.158442 | 95% [-0.133220, 0.454460] |
| S3 | not supported | think:hostility-minus-random | 0.074028 | 95% [-0.251237, 0.393956] |
| S4 | not supported | hostility | -0.000723 | 95% [-0.011632, 0.009784] |
| S4 | not supported | hostility-minus-technicality | -0.006133 | 95% [-0.021739, 0.009513] |
| S4 | not supported | hostility-minus-random | 0.000454 | 95% [-0.014182, 0.014610] |
| S5 | not supported | hostility | 0.006815 | 95% [-0.012193, 0.025471] |
| S5 | not supported | hostility-minus-technicality | 0.007291 | 95% [-0.018259, 0.032690] |
| S5 | not supported | hostility-minus-random | 0.009258 | 95% [-0.015171, 0.033077] |

## Exploratory results

These results do not change confirmatory verdicts.

### E1

```json
{
  "hostility": {
    "estimate": -0.0031199014903659232,
    "ci": [
      -0.011253586209129963,
      0.005083513385368876
    ],
    "confidence": 0.95,
    "n_prompts": 80,
    "status": "exploratory"
  },
  "technicality": {
    "estimate": -0.003160478181532092,
    "ci": [
      -0.0101494114120123,
      0.0037907718448291832
    ],
    "confidence": 0.95,
    "n_prompts": 80,
    "status": "exploratory"
  },
  "random": {
    "estimate": -0.002643084756774808,
    "ci": [
      -0.010373528438067008,
      0.005437804709718695
    ],
    "confidence": 0.95,
    "n_prompts": 80,
    "status": "exploratory"
  }
}
```

### pulse_routes

```json
{
  "hostility": {
    "C": {
      "estimate": -0.0036637349176547153,
      "ci": [
        -0.02596477734666843,
        0.0183548792651227
      ],
      "confidence": 0.95,
      "n_prompts": 80,
      "status": "exploratory"
    },
    "H": {
      "estimate": -0.010478523064540723,
      "ci": [
        -0.01975051680690473,
        -0.001133611335623716
      ],
      "confidence": 0.95,
      "n_prompts": 80,
      "status": "exploratory"
    },
    "LHP": {
      "estimate": -0.010850570789821545,
      "ci": [
        -0.03212863030492132,
        0.01057590965097507
      ],
      "confidence": 0.95,
      "n_prompts": 80,
      "status": "exploratory"
    }
  },
  "technicality": {
    "C": {
      "estimate": 0.0035157704938667657,
      "ci": [
        -0.012894566487781789,
        0.020138404853065568
      ],
      "confidence": 0.95,
      "n_prompts": 80,
      "status": "exploratory"
    },
    "H": {
      "estimate": 0.003991963857451697,
      "ci": [
        -0.006464357028009461,
        0.014672995719997473
      ],
      "confidence": 0.95,
      "n_prompts": 80,
      "status": "exploratory"
    },
    "LHP": {
      "estimate": 0.0012610507692348782,
      "ci": [
        -0.0217842079149547,
        0.025323706455124
      ],
      "confidence": 0.95,
      "n_prompts": 80,
      "status": "exploratory"
    }
  },
  "random": {
    "C": {
      "estimate": 0.0048557228596919355,
      "ci": [
        -0.0136747933943358,
        0.023512446618425966
      ],
      "confidence": 0.95,
      "n_prompts": 80,
      "status": "exploratory"
    },
    "H": {
      "estimate": 0.0072985311292606435,
      "ci": [
        -0.0034282284897448594,
        0.017809564314347694
      ],
      "confidence": 0.95,
      "n_prompts": 80,
      "status": "exploratory"
    },
    "LHP": {
      "estimate": 0.014607044556451801,
      "ci": [
        -0.007755101274209997,
        0.0362428015115015
      ],
      "confidence": 0.95,
      "n_prompts": 80,
      "status": "exploratory"
    }
  }
}
```

### E2

```json
[
  {
    "group": [
      "direct",
      "regular",
      "hostility",
      0.5
    ],
    "n": 80,
    "token_ids": [
      9,
      10
    ],
    "R_full_minus_R_text_mean": [
      0.0,
      0.0
    ],
    "status": "descriptive"
  },
  {
    "group": [
      "direct",
      "regular",
      "hostility",
      1.0
    ],
    "n": 80,
    "token_ids": [
      9,
      10
    ],
    "R_full_minus_R_text_mean": [
      0.0,
      0.0
    ],
    "status": "descriptive"
  },
  {
    "group": [
      "direct",
      "regular",
      "none",
      0.0
    ],
    "n": 80,
    "token_ids": [
      9,
      10
    ],
    "R_full_minus_R_text_mean": [
      0.0,
      0.0
    ],
    "status": "descriptive"
  },
  {
    "group": [
      "direct",
      "regular",
      "random",
      0.5
    ],
    "n": 80,
    "token_ids": [
      9,
      10
    ],
    "R_full_minus_R_text_mean": [
      0.0,
      0.0
    ],
    "status": "descriptive"
  },
  {
    "group": [
      "direct",
      "regular",
      "random",
      1.0
    ],
    "n": 80,
    "token_ids": [
      9,
      10
    ],
    "R_full_minus_R_text_mean": [
      0.0,
      0.0
    ],
    "status": "descriptive"
  },
  {
    "group": [
      "direct",
      "regular",
      "technicality",
      0.5
    ],
    "n": 80,
    "token_ids": [
      9,
      10
    ],
    "R_full_minus_R_text_mean": [
      0.0,
      0.0
    ],
    "status": "descriptive"
  },
  {
    "group": [
      "direct",
      "regular",
      "technicality",
      1.0
    ],
    "n": 80,
    "token_ids": [
      9,
      10
    ],
    "R_full_minus_R_text_mean": [
      0.0,
      0.0
    ],
    "status": "descriptive"
  },
  {
    "group": [
      "think",
      "pulse",
      "hostility",
      1.0
    ],
    "n": 80,
    "token_ids": [
      9,
      10
    ],
    "R_full_minus_R_text_mean": [
      0.0,
      0.0
    ],
    "status": "descriptive"
  },
  {
    "group": [
      "think",
      "pulse",
      "random",
      1.0
    ],
    "n": 80,
    "token_ids": [
      9,
      10
    ],
    "R_full_minus_R_text_mean": [
      0.0,
      0.0
    ],
    "status": "descriptive"
  },
  {
    "group": [
      "think",
      "pulse",
      "technicality",
      1.0
    ],
    "n": 80,
    "token_ids": [
      9,
      10
    ],
    "R_full_minus_R_text_mean": [
      0.0,
      0.0
    ],
    "status": "descriptive"
  },
  {
    "group": [
      "think",
      "regular",
      "hostility",
      0.5
    ],
    "n": 80,
    "token_ids": [
      9,
      10
    ],
    "R_full_minus_R_text_mean": [
      0.0,
      0.0
    ],
    "status": "descriptive"
  },
  {
    "group": [
      "think",
      "regular",
      "hostility",
      1.0
    ],
    "n": 80,
    "token_ids": [
      9,
      10
    ],
    "R_full_minus_R_text_mean": [
      0.0,
      0.0
    ],
    "status": "descriptive"
  },
  {
    "group": [
      "think",
      "regular",
      "none",
      0.0
    ],
    "n": 80,
    "token_ids": [
      9,
      10
    ],
    "R_full_minus_R_text_mean": [
      0.0,
      0.0
    ],
    "status": "descriptive"
  },
  {
    "group": [
      "think",
      "regular",
      "random",
      0.5
    ],
    "n": 80,
    "token_ids": [
      9,
      10
    ],
    "R_full_minus_R_text_mean": [
      0.0,
      0.0
    ],
    "status": "descriptive"
  },
  {
    "group": [
      "think",
      "regular",
      "random",
      1.0
    ],
    "n": 80,
    "token_ids": [
      9,
      10
    ],
    "R_full_minus_R_text_mean": [
      0.0,
      0.0
    ],
    "status": "descriptive"
  },
  {
    "group": [
      "think",
      "regular",
      "technicality",
      0.5
    ],
    "n": 80,
    "token_ids": [
      9,
      10
    ],
    "R_full_minus_R_text_mean": [
      0.0,
      0.0
    ],
    "status": "descriptive"
  },
  {
    "group": [
      "think",
      "regular",
      "technicality",
      1.0
    ],
    "n": 80,
    "token_ids": [
      9,
      10
    ],
    "R_full_minus_R_text_mean": [
      0.0,
      0.0
    ],
    "status": "descriptive"
  }
]
```

### E3

```json
{
  "P1": {
    "prompt_ids": [
      "s3t00",
      "s3t01",
      "s3t02",
      "s3t03",
      "s3t04",
      "s3t05",
      "s3t06",
      "s3t07",
      "s3t08",
      "s3t09",
      "s3t10",
      "s3t11",
      "s3t12",
      "s3t13",
      "s3t14",
      "s3t15",
      "s3t16",
      "s3t17",
      "s3t18",
      "s3t19",
      "s3t20",
      "s3t21",
      "s3t22",
      "s3t23",
      "s3t24",
      "s3t25",
      "s3t26",
      "s3t27",
      "s3t28",
      "s3t29",
      "s3t30",
      "s3t31",
      "s3t32",
      "s3t33",
      "s3t34",
      "s3t35",
      "s3t36",
      "s3t37",
      "s3t38",
      "s3t39",
      "s3t40",
      "s3t41",
      "s3t42",
      "s3t43",
      "s3t44",
      "s3t45",
      "s3t46",
      "s3t47",
      "s3t48",
      "s3t49",
      "s3t50",
      "s3t51",
      "s3t52",
      "s3t53",
      "s3t54",
      "s3t55",
      "s3t56",
      "s3t57",
      "s3t58",
      "s3t59",
      "s3t60",
      "s3t61",
      "s3t62",
      "s3t63",
      "s3t64",
      "s3t65",
      "s3t66",
      "s3t67",
      "s3t68",
      "s3t69",
      "s3t70",
      "s3t71",
      "s3t72",
      "s3t73",
      "s3t74",
      "s3t75",
      "s3t76",
      "s3t77",
      "s3t78",
      "s3t79"
    ],
    "n_prompts": 80,
    "result": {
      "verdict": "supported",
      "components": {
        "hostility": {
          "estimate": -1.2364459280603668,
          "ci": [
            -1.27247074652219,
            -1.2000862937832906
          ],
          "confidence": 0.975,
          "n_prompts": 80,
          "status": "supported"
        },
        "hostility-minus-technicality": {
          "estimate": -1.2336912063979262,
          "ci": [
            -1.2825870649172875,
            -1.1866865841472103
          ],
          "confidence": 0.975,
          "n_prompts": 80,
          "status": "supported"
        },
        "hostility-minus-random": {
          "estimate": -1.2319592031524162,
          "ci": [
            -1.2780762774961445,
            -1.184633400321341
          ],
          "confidence": 0.975,
          "n_prompts": 80,
          "status": "supported"
        }
      }
    }
  },
  "P2": {
    "prompt_ids": [
      "s3t00",
      "s3t01",
      "s3t02",
      "s3t03",
      "s3t04",
      "s3t05",
      "s3t06",
      "s3t07",
      "s3t08",
      "s3t09",
      "s3t10",
      "s3t11",
      "s3t12",
      "s3t13",
      "s3t14",
      "s3t15",
      "s3t16",
      "s3t17",
      "s3t18",
      "s3t19",
      "s3t20",
      "s3t21",
      "s3t22",
      "s3t23",
      "s3t24",
      "s3t25",
      "s3t26",
      "s3t27",
      "s3t28",
      "s3t29",
      "s3t30",
      "s3t31",
      "s3t32",
      "s3t33",
      "s3t34",
      "s3t35",
      "s3t36",
      "s3t37",
      "s3t38",
      "s3t39",
      "s3t40",
      "s3t41",
      "s3t42",
      "s3t43",
      "s3t44",
      "s3t45",
      "s3t46",
      "s3t47",
      "s3t48",
      "s3t49",
      "s3t50",
      "s3t51",
      "s3t52",
      "s3t53",
      "s3t54",
      "s3t55",
      "s3t56",
      "s3t57",
      "s3t58",
      "s3t59",
      "s3t60",
      "s3t61",
      "s3t62",
      "s3t63",
      "s3t64",
      "s3t65",
      "s3t66",
      "s3t67",
      "s3t68",
      "s3t69",
      "s3t70",
      "s3t71",
      "s3t72",
      "s3t73",
      "s3t74",
      "s3t75",
      "s3t76",
      "s3t77",
      "s3t78",
      "s3t79"
    ],
    "n_prompts": 80,
    "result": {
      "verdict": "not supported",
      "components": {
        "hostility": {
          "estimate": -0.0035441484067714976,
          "ci": [
            -0.016613058569562238,
            0.00932467526778345
          ],
          "confidence": 0.975,
          "n_prompts": 80,
          "status": "not supported"
        },
        "hostility-minus-technicality": {
          "estimate": -0.002611271474599175,
          "ci": [
            -0.015498100075790822,
            0.009549415741155858
          ],
          "confidence": 0.975,
          "n_prompts": 80,
          "status": "not supported"
        },
        "hostility-minus-random": {
          "estimate": -0.006890776795078724,
          "ci": [
            -0.019695142330814167,
            0.005648780070897463
          ],
          "confidence": 0.975,
          "n_prompts": 80,
          "status": "not supported"
        }
      }
    }
  }
}
```

### truncation_counts

```json
[
  {
    "group": [
      "direct",
      "regular",
      "hostility",
      0.5
    ],
    "n": 80,
    "thinking_truncated": 0,
    "answer_truncated": 0
  },
  {
    "group": [
      "direct",
      "regular",
      "hostility",
      1.0
    ],
    "n": 80,
    "thinking_truncated": 0,
    "answer_truncated": 0
  },
  {
    "group": [
      "direct",
      "regular",
      "none",
      0.0
    ],
    "n": 80,
    "thinking_truncated": 0,
    "answer_truncated": 0
  },
  {
    "group": [
      "direct",
      "regular",
      "random",
      0.5
    ],
    "n": 80,
    "thinking_truncated": 0,
    "answer_truncated": 0
  },
  {
    "group": [
      "direct",
      "regular",
      "random",
      1.0
    ],
    "n": 80,
    "thinking_truncated": 0,
    "answer_truncated": 0
  },
  {
    "group": [
      "direct",
      "regular",
      "technicality",
      0.5
    ],
    "n": 80,
    "thinking_truncated": 0,
    "answer_truncated": 0
  },
  {
    "group": [
      "direct",
      "regular",
      "technicality",
      1.0
    ],
    "n": 80,
    "thinking_truncated": 0,
    "answer_truncated": 0
  },
  {
    "group": [
      "think",
      "pulse",
      "hostility",
      1.0
    ],
    "n": 80,
    "thinking_truncated": 0,
    "answer_truncated": 0
  },
  {
    "group": [
      "think",
      "pulse",
      "random",
      1.0
    ],
    "n": 80,
    "thinking_truncated": 0,
    "answer_truncated": 0
  },
  {
    "group": [
      "think",
      "pulse",
      "technicality",
      1.0
    ],
    "n": 80,
    "thinking_truncated": 0,
    "answer_truncated": 0
  },
  {
    "group": [
      "think",
      "regular",
      "hostility",
      0.5
    ],
    "n": 80,
    "thinking_truncated": 0,
    "answer_truncated": 0
  },
  {
    "group": [
      "think",
      "regular",
      "hostility",
      1.0
    ],
    "n": 80,
    "thinking_truncated": 0,
    "answer_truncated": 0
  },
  {
    "group": [
      "think",
      "regular",
      "none",
      0.0
    ],
    "n": 80,
    "thinking_truncated": 0,
    "answer_truncated": 0
  },
  {
    "group": [
      "think",
      "regular",
      "random",
      0.5
    ],
    "n": 80,
    "thinking_truncated": 0,
    "answer_truncated": 0
  },
  {
    "group": [
      "think",
      "regular",
      "random",
      1.0
    ],
    "n": 80,
    "thinking_truncated": 0,
    "answer_truncated": 0
  },
  {
    "group": [
      "think",
      "regular",
      "technicality",
      0.5
    ],
    "n": 80,
    "thinking_truncated": 0,
    "answer_truncated": 0
  },
  {
    "group": [
      "think",
      "regular",
      "technicality",
      1.0
    ],
    "n": 80,
    "thinking_truncated": 0,
    "answer_truncated": 0
  }
]
```

### E4 — fixed readability sample

[Stage C calibration reference](stageC_samples.md). These pre-data samples used the earlier dose of 0.02.

#### s3t00 / regular

Thinking capped: False; answer capped: False.

Complete thinking:

````text
SYNTHETIC
````

Complete answer:

````text
SYNTHETIC
````

#### s3t01 / regular

Thinking capped: False; answer capped: False.

Complete thinking:

````text
SYNTHETIC
````

Complete answer:

````text
SYNTHETIC
````

#### s3t02 / regular

Thinking capped: False; answer capped: False.

Complete thinking:

````text
SYNTHETIC
````

Complete answer:

````text
SYNTHETIC
````

#### s3t03 / regular

Thinking capped: False; answer capped: False.

Complete thinking:

````text
SYNTHETIC
````

Complete answer:

````text
SYNTHETIC
````

#### s3t04 / regular

Thinking capped: False; answer capped: False.

Complete thinking:

````text
SYNTHETIC
````

Complete answer:

````text
SYNTHETIC
````

#### s3t00 / pulse

Thinking capped: False; answer capped: False.

Complete thinking:

````text
SYNTHETIC
````

Complete answer:

````text
SYNTHETIC
````

#### s3t01 / pulse

Thinking capped: False; answer capped: False.

Complete thinking:

````text
SYNTHETIC
````

Complete answer:

````text
SYNTHETIC
````

#### s3t02 / pulse

Thinking capped: False; answer capped: False.

Complete thinking:

````text
SYNTHETIC
````

Complete answer:

````text
SYNTHETIC
````

#### s3t03 / pulse

Thinking capped: False; answer capped: False.

Complete thinking:

````text
SYNTHETIC
````

Complete answer:

````text
SYNTHETIC
````

#### s3t04 / pulse

Thinking capped: False; answer capped: False.

Complete thinking:

````text
SYNTHETIC
````

Complete answer:

````text
SYNTHETIC
````

Fixed sample count: 10/10. Descriptive review of repetition, invented content and unfinished output is completed after the main run; no output-based sample selection.
