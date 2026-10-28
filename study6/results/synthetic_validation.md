# Synthetic build validation

All fixtures are synthetic; no model inference was performed. Every scenario used 10,000 paired prompt-cluster bootstrap draws.

| Pattern | D1 | D2 | M1 | Maximum identity error (R1) |
|---|---|---|---|---|
| no_change | supported | supported | negligible | 0.0 |
| partial_attenuation | supported | supported | supported | 0.0 |
| full_attenuation | negligible | negligible | supported | 0.0 |
| amplification | supported | supported | supported | 0.0 |
| reversal | reversed | reversed | supported | 0.0 |
| mixed_controls | supported | supported | supported | 0.0 |
| missing_cells | not estimable | supported | not estimable | 0.0 |

Exact shared-baseline cancellation passed on dyadic planted fixtures. All original 1,600 main and 80 pilot branches reconstructed with the real CPU tokenizer; all 400 main U-with-a_U inputs matched Study 5. Closures, generic insertion, missing cells, mixed controls, approval, two-process replay, hook assertions, low-mass placement exclusions and subset counts passed.
