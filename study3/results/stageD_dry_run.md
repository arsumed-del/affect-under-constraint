# Stage D — calibration-only dry run

PASS: both calibration prompts s2c00 and s2c01 completed every specified cell type: 28 regular and six pulse records (34 total). All cell keys are unique, source/provenance hashes match, all required numerical measures are finite, and all shared rating prefixes match. No test prompts were accessed.

Maximum zero-dose |R_full−R_text|: 0.000000000. Maximum change across fresh repeated baseline scores: 0.000000000.

Pulse metadata confirms cache discard and unsteered prefix re-encoding. Independent model-free instrumentation also verifies natural and forced closures, fresh first-answer logits, and no steering on answer steps. R_full uses the prompt/thinking-only pulse mask; S5 uses R_text−R_zero.

All trace-window coverage, entropy accumulations, C=X+H identities, rating masks and trajectory lengths passed the integrity audit. No calibration hypothesis tests were performed.

| Mode | Route | n | Mean cell seconds |
|---|---|---:|---:|
| direct | regular | 14 | 17.710 |
| think | regular | 14 | 96.886 |
| think | pulse | 6 | 95.832 |

The timings cover the full Stage D measure set, including 24 teacher-forced opener forwards. They are not a representative main-run runtime estimate: only two calibration prompts were used. Stage B projections and their caveats remain separately preserved.

Approval/hash/deposit guard tests used in-memory fixtures and created no approval file. Completed-run resume is tested separately before freeze.

Completed-run resume: PASS. The runner verified provenance and returned before model loading; the raw-file SHA-256 was identical before and after.
