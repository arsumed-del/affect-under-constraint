# Stage 2 validation — google/gemma-2-2b-it

BLOCKED (measurement failure). Alpha_max=0.2; neutral-condition expressed-hostility difference 0.02738631; 95% prompt-bootstrap CI [-0.12573303, 0.18706261], 10,000 resamples, 20/20 complete pairs.

| Candidate | Median perplexity ratio | Median distinct-token ratio | Both checks pass |
|---:|---:|---:|:---|
| 0.02 | 0.98344556 | 0.65000000 | True |
| 0.04 | 1.03399535 | 0.63333333 | True |
| 0.06 | 1.06175868 | 0.66250000 | True |
| 0.08 | 1.24215482 | 0.64166667 | True |
| 0.1 | 1.35691594 | 0.67028986 | True |
| 0.13 | 1.33467913 | 0.66079932 | True |
| 0.16 | 2.18773306 | 0.66176471 | True |
| 0.2 | 3.23862591 | 0.65000000 | True |
| 0.25 | 5.26624664 | 0.63750000 | False |

Baseline median distinct-token ratio: 0.64583333; required minimum: 0.38750000. First failure: 0.25. Unrun larger candidates: [0.3, 0.35, 0.4, 0.45, 0.5].

Hostility/technicality cosine: 0.02533472 (descriptive only). Validation used saved calibration generations once; no additional generations or re-extraction. No test data used.
