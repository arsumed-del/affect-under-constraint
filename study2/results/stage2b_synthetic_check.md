# Study 2 Stage 2b synthetic checks

**PASS.** Planted and null fixtures each have three model IDs, 80 synthetic prompt IDs per model, and 2,560 cells per model in the Stage 3 schema. No test-prompt generations were performed.

| Fixture | P1 | P2 | S1–S5 | Generality |
|---|---|---|---|
| Planted | supported in all three | supported in all three | all supported | both general |
| Null | not supported in all three | not supported in all three | none supported | neither general |
| Incoherent top-dose technicality, one model | supported | supported | text leakage cell excluded | three eligible models support both |

All fixtures used 10,000 prompt-cluster bootstrap resamples. Primary intervals are 97.5%; secondary intervals are 95%. Independent direct least-squares calculations matched the weighted OLS and BIC estimators. Amendment 3.1 checks confirm that an incoherent top-dose control retains P2, an incoherent hostility top dose is excluded from S3, and P1/P2/S1/S4 are unchanged by that gate. The field list is read from config. Genuine missing required measurements remain not estimable. Additional checks covered identical-strength controls (primary verdicts fail), pairwise missingness, fewer-than-eight-token leakage, and the fewer-than-two-eligible-model generality rule. The absent-approval guard refused Stage 3. Detailed estimates, intervals and omissions are saved in the accompanying JSON files.

Synthetic behavior validates implementation, not the experimental predictions.

Focused control check: PASS. In an additional fixture, the hostility criterion passes for P1 and P2, while the technicality control interval includes zero and its hostility-minus-control interval also includes zero. Both primaries correctly remain not supported. The old Study 1 null-control shortcut is therefore rejected. Detailed fixture and outputs: null_control_intervals.
