# Stage A — pre-approval validity check

All 80 specified calibration cells are present. No test prompts were accessed. The fixed pilot P1 dose, vectors and residual norm were reused by verified hash. These are descriptive calibration checks, not hypothesis tests.

## Required rating checks

PASS: the maximum |R_full − R_text| across all 40 zero-dose cells is 0.000000000, within 0.01. All 80 cells used the identical turn-2 prefix shown below; the digit is scored immediately after it.

```text
<|im_start|>assistant
<think>

</think>


```

Token IDs: `[151644, 77091, 198, 151667, 271, 151668, 271]`. Each cell used three fresh complete-sequence full forwards, with exact generated turn-1 IDs preserved. Only R_full applies steering, on turn-1 positions only. No generation cache was used for ratings.

## Baseline ratings

| Mode | n | R_zero mean | Sample SD |
|---|---:|---:|---:|
| direct | 20 | 7.841716 | 0.298742 |
| think | 20 | 7.803700 | 0.324713 |

Thinking-mode SD / direct-mode SD = 1.086934. The two baseline SDs are descriptively comparable: thinking-mode SD is 8.7% higher, rather than compressed near the old pilot value of approximately 0.10. This comparison is descriptive: no SD acceptance threshold or inference test was specified.

## Output descriptions

| Mode | a | n | Mean EH_trace | Mean EH_answer | Thinking capped | Answer capped | Median absolute answer perplexity |
|---|---:|---:|---:|---:|---:|---:|---:|
| direct | 0 | 20 | N/A | 0.016233 | 0 | 0 | 1.156300 |
| direct | 1 | 20 | N/A | 0.256400 | 0 | 19 | 4.284269 |
| think | 0 | 20 | 0.124462 | 0.018588 | 0 | 0 | 1.202922 |
| think | 1 | 20 | 0.396721 | 0.475709 | 18 | 20 | 1.832579 |

Trace EH is the equal-weight mean of consecutive 120-model-token windows, including the final partial window; direct mode has no trace (N/A). Answer EH uses the fixed classifier on the answer. Absolute answer perplexity is scored unsteered, conditional on the exact preceding prompt and any generated thinking. No coherence exclusions were applied. Truncation counts denote reaching the generation cap, not a classifier cutoff.

Classifier errors: 0. Classifier inputs truncated at its inherited 512-token limit: 0. If any trace window failed, the whole trace EH would be missing; none are silently omitted.

Provenance: original `results/checks_source_hashes.sha256` and authorized-extension completion manifest `results/checks_source_hashes_completed.sha256`, `results/reused_hashes.sha256`, `results/checks_code_hashes.sha256`; complete cells: `data/checks/stageA_cells.jsonl`.
