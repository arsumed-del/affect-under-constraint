# Stage D — synthetic validation

All data are synthetic; no model calls or test-prompt reads. Full structure: 80 prompts × 17 cells = 1,360 records. The missing-cell case intentionally has 1,359. Fixed generator seed base 20261008; no seed or estimator search. Each scenario uses 10,000 prompt-cluster bootstrap resamples and the specified CI levels. Null calibration uses 200 independently seeded datasets with 1,000 resamples each.

| Scenario | P1 | P2 | S5 |
|---|---|---|---|
| P1 | supported | not supported | not supported |
| P2 | not supported | supported | not supported |
| S5 | not supported | not supported | supported |
| null | not supported | not supported | not supported |
| truncation | supported | not supported | not supported |
| floor20 | supported | not supported | not supported |
| hidden_only | not supported | not supported | not supported |
| missing | not estimable | not estimable | not supported |
| missing_baseline | not estimable | not supported | not supported |
| missing_prompt | not estimable | not estimable | not estimable |
| gate | not supported | not estimable | not supported |

Primary null false-positive rates: P1 0.000%; P2 0.000%. Nominal level: 2.500%. Requirement: **PASS**. These are observed finite-simulation rates, not a proof of universal calibration.

Additional checks passed: hidden-only pulse change does not support S5; a required gated trace group makes P2 not estimable while ratings and LHP remain estimable; a missing required row makes P1 not estimable; E3 excludes to 15 common prompts and is not estimable, while exactly 20 meets the floor; confirmatory P1 still uses all truncated cells; direct least-squares P2 estimate agrees within 1e-12; threshold exactly 6 passes; a single extreme perplexity does not exclude a group whose median passes.

Scenario data and full outputs: `data/synthetic/v04/`. Null datasets can be reconstructed exactly from the recorded generator and per-replicate seeds. No inferential analysis was run on calibration outputs.

## Planted P1 table

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
