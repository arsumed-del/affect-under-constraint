# Stage 2 — Qwen/Qwen2.5-3B-Instruct

**PASS**. Selected alpha_max: 0.16. Grid: [0.0, 0.02, 0.04, 0.08, 0.12, 0.16].

| Candidate | Median perplexity ratio | Median distinct-token ratio | Coherent | Mean EH difference | 95% CI | Manipulation passes |
|---:|---:|---:|---|---:|---|---|
| 0.02 | 1.02228090 | 0.71130952 | True | -0.009425552291213534 | [-0.03353012157931517, 0.012688456817340894] | False |
| 0.04 | 1.04366853 | 0.74245495 | True | 0.004885392193682492 | [-0.027205212200133246, 0.038370976713631516] | False |
| 0.06 | 1.14952758 | 0.71547619 | True | 0.0012459001096431165 | [-0.029395802891085624, 0.03368567814904961] | False |
| 0.08 | 1.23566955 | 0.70993590 | True | 0.005481076083378866 | [-0.027134603484300895, 0.04067145318811525] | False |
| 0.1 | 1.36795614 | 0.71805556 | True | 0.0046410676615778355 | [-0.026618555965542325, 0.034637245116318806] | False |
| 0.12 | 1.52440879 | 0.73333333 | True | -0.006542533462925349 | [-0.03225138405905455, 0.016732738488499304] | False |
| 0.14 | 2.32481963 | 0.70176519 | True | 0.05094829524750821 | [0.008733034562901594, 0.09893110405508194] | True |
| 0.16 | 2.96328069 | 0.71250000 | True | 0.0926916778262239 | [0.026030411043029746, 0.16361672541243022] | True |
| 0.18 | 3.98476996 | 0.70416667 | False | None | None | outside coherent range |

Baseline median distinct-token ratio: 0.706439393939394. First coherence failure: 0.18. Unrun candidates: [0.2, 0.23, 0.26, 0.3, 0.35, 0.4, 0.45, 0.5]. Every coherent candidate was checked with 10,000 prompt bootstraps; largest passing candidate selected. No test-prompt generations. Hostility/technicality cosine -0.05473277 (descriptive).
