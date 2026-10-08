# Stage 2 validation — Amendment 2.2

Qwen: PASS.

Alpha_max=0.16; neutral-condition expressed-hostility difference 0.12126166; 95% prompt-bootstrap CI [0.05151885, 0.20367575], 10,000 resamples, 20/20 complete pairs. The EH gate requires the lower bound to exceed zero.

| Candidate | Median perplexity ratio | Median distinct-token ratio | Both checks pass |
|---:|---:|---:|:---|
| 0.02 | 1.04022405 | 0.71689723 | True |
| 0.04 | 1.07675396 | 0.73912338 | True |
| 0.06 | 1.11386894 | 0.74213548 | True |
| 0.08 | 1.21418631 | 0.74856322 | True |
| 0.1 | 1.39004997 | 0.70985061 | True |
| 0.13 | 1.60740815 | 0.79057540 | True |
| 0.16 | 2.30178599 | 0.74456522 | True |
| 0.2 | 6.12656380 | 0.69748168 | False |

Baseline median distinct-token ratio: 0.70980235; required minimum: 0.42588141. First failure: 0.2. Unrun larger candidates: [0.25, 0.3, 0.35, 0.4, 0.45, 0.5].

Directions and residual norms were reused unchanged from v2.0, verified by hashes. Hostility/technicality cosine: -0.05473277 (descriptive only). Existing calibration generations were scored once for the validation gate; no additional generations or re-extraction. Missing classifier scores remain missing. Gemma remains blocked by gated access. No test-prompt generations were used.
