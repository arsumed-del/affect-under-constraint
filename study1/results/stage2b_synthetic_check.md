# Stage 2b synthetic checks

**PASS.** Each fixture contains 40 synthetic prompt IDs and 1,280 unique raw cells in the same schema used by the main runner. No test-prompt outcomes were generated.

| Dataset | H1 | H2 | H3 | H4 | H5 | H6 |
|---|---|---|---|---|---|---|
| planted | supported | supported | supported | supported | supported | supported |
| null | not supported | not supported | not supported | not supported | not supported | not supported |

Both fixtures used the registered 10,000 paired prompt-cluster bootstrap resamples. Planted H1–H5 were detected; the null fixture supported no hypothesis. A hinge was also planted for the H6 implementation check. All estimates, percentile intervals, specificity contrasts, missing counts, coherence exclusions and exploratory outputs are in synthetic_planted.json and synthetic_null.json (with Markdown tables).

Independent checks compared the vectorized OLS slopes and H6 BIC to direct least-squares fits on explicit duplicated-prompt samples. Checks also confirmed primary exclusion at a median ratio of 2.01 and missing time-course leakage below 8 tokens. The approval guard refused a missing PREREG_APPROVED without invoking main mode.

These fixtures validate code behavior, not experimental hypotheses.
