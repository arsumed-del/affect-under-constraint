# Stage 2 — microsoft/Phi-3.5-mini-instruct

**PASS**. Selected alpha_max: 0.04. Grid: [0.0, 0.005, 0.01, 0.02, 0.03, 0.04].

| Candidate | Median perplexity ratio | Median distinct-token ratio | Coherent | Mean EH difference | 95% CI | Manipulation passes |
|---:|---:|---:|---|---:|---|---|
| 0.02 | 1.15914107 | 0.69583333 | True | 0.043429188980371694 | [-0.0002356012260861445, 0.09803747725825815] | False |
| 0.04 | 2.14640221 | 0.70416667 | True | 0.05967969026532956 | [0.01921759266551817, 0.10688858445020742] | True |
| 0.06 | 4.07113452 | 0.71666667 | False | None | None | outside coherent range |

Baseline median distinct-token ratio: 0.6958333333333333. First coherence failure: 0.06. Unrun candidates: [0.08, 0.1, 0.12, 0.14, 0.16, 0.18, 0.2, 0.23, 0.26, 0.3, 0.35, 0.4, 0.45, 0.5]. Every coherent candidate was checked with 10,000 prompt bootstraps; largest passing candidate selected. No test-prompt generations. Hostility/technicality cosine 0.11816530 (descriptive).
