# Deviations — Study 2

## Affecting specified quantities
(none)

## Engineering

- Stage 0: copied Study 1 inference and metrics into Study 2; removed the exploratory layerwise logit lens as specified. All execution uses Study 2 as its working directory and the shared environment without modifying it. Bytecode writes are disabled. Study 1 files are read only.

### Model access — meta-llama/Llama-3.2-3B-Instruct

Attempted the configured model config using existing library authentication for gated models. Exact error:

```text
GatedRepoError: 403 Client Error. (Request ID: Root=1-6ac2c3b8-766b4dcc0ead2fc203dff064;8b6320a1-a72a-441a-a6ca-054a8bf3cf42)

Cannot access gated repo for url https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct/resolve/main/config.json.
Access to model meta-llama/Llama-3.2-3B-Instruct is restricted and you are not in the authorized list. Visit https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct to ask for access.
```

### Stage 1 stopped

```text
Traceback (most recent call last):
  File "/Users/arthursu/Projects/affect-suppression-steering/study2/src/run_smoke.py", line 91, in <module>
    main()
  File "/Users/arthursu/Projects/affect-suppression-steering/study2/src/run_smoke.py", line 86, in main
    run(spec)
  File "/Users/arthursu/Projects/affect-suppression-steering/study2/src/run_smoke.py", line 48, in run
    row['ratings'] = model.ratings(messages, generation, question)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/arthursu/Projects/affect-suppression-steering/.venv/lib/python3.12/site-packages/torch/utils/_contextlib.py", line 124, in decorate_context
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/arthursu/Projects/affect-suppression-steering/study2/src/model_utils.py", line 139, in ratings
    return {'text_only':self.rating(text_logits), 'hidden':self.rating(hidden_logits), 'template_prefix_exact':exact, 'identical_visible_ids':True}
                        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/arthursu/Projects/affect-suppression-steering/study2/src/model_utils.py", line 114, in rating
    raise RuntimeError('A rating digit does not have a single token')
RuntimeError: A rating digit does not have a single token
```
No scientific parameter changed; no automatic retry.

### Engineering — Phi isolated-digit tokenizer prefix

Phi smoke encountered `RuntimeError: A rating digit does not have a single token`. Tokenizer-only inspection (results/phi_digit_tokenization.json) showed each isolated digit encodes as `[29871, digit_id]`, where 29871 is SentencePiece `▁` and the second token is the literal digit `0`–`9`. The measure requires next-token probabilities of those literal digit tokens; the shared helper now removes only this verified tokenizer-added dummy prefix when resolving digit IDs. No conversation tokens, forward passes, logits, probability normalization, precision, or generation settings change. Exact source diff: results/phi_digit_engineering.diff. The original error is preserved at data/_superseded/20261004T143055_phi_smoke_tokenizer/stage1_error.txt. Qwen completed records remain unchanged. Phi had no completed saved smoke cell; resume uses its identical original prompt and seed.

### Engineering — Study 2 runner generalization

Copied and generalized Study 1 extraction, norm measurement, generation and checkpoint logic. Model IDs, slugs and per-model immutable output paths come from Study 2 config. The new dose-selection implementation evaluates coherence in increasing order until first failure, then scores saved generations at every coherent candidate, using the fixed classifier and 10,000 paired prompt resamples. It selects the largest candidate with a positive CI lower bound, or records the specified exclusion. Baseline generations and classifier scores are checkpointed once. No Study 1 data or directions are reused. Runner and analysis drafts were prepared while Phi downloaded; none were executed before Stage 1 completion.

### Engineering — independent synthetic checks during calibration

The CPU-only Stage 2b synthetic checks run while Stage 2 Qwen calibration proceeds, without accessing its outputs or test prompts. Model generations remain sequential. Synthetic progress is logged separately to avoid concurrent STATUS.md rewrites; the agent records completion in STATUS.md. Analysis freezing and timing remain after model dose selection.

### Stage 2 completion audit

Both available models passed their registered manipulation-based selection rule. Read-only checks reproduced directions from saved extraction sums, checked residual-norm pooling, all cell seeds and counts, coherent-range stopping, bootstrap intervals, selected maxima and immutable hashes. Qwen: 400 dose cells, 360 fixed-classifier scores, alpha_max 0.16, first coherence failure 0.18. Phi: 160 dose cells, 120 scores, alpha_max 0.04, first failure 0.06. No scientific setting or data record was changed.

## Amendment 3.1 implementation

The reviewer changed PREREG.md and config.yaml externally during Stage 2b timing. The agent detected `AssertionError: Hash mismatch: PREREG.md`, attempted to stop the known timing job, and found that it had already completed all six calibration-only cells. No Stage 3 data exist. The reviewer then explicitly authorized Amendment 3.1 in conversation. The v3.0 approval was intentionally renamed by the reviewer; the agent did not create or alter any approval.

The authorized amendment limits the 4.0 gate to the configured text-scored fields; LHP, carryover and entropy remain available. The agent will implement this list-driven rule, repeat all synthetic checks, and freeze the new analysis by hash. Old analysis source, synthetic inputs/results, specification bytes, and manifest are preserved at data/_superseded/20261004T162639_v3.0_analysis. The new supplied SHA-256 hashes were independently verified before updating the specification manifest.

Comparing v3.0 and v3.1 YAML after removing only the analysis section and preregistration-version label confirmed exact equality of all generation, extraction, dose-selection, model, prompt, classifier and measure settings. Qwen and Phi directions, norms and write-once calibrations are retained unchanged. Completed timing cells are retained byte-for-byte; their mixed file-hash provenance reflects the external edit during the run, not a change in their generation settings. Details: results/amendment3_1_compatibility.json.

Engineering: Stage 1 accepts an explicit configured model slug after a fresh access check, preserving the historical Stage 0 access record. Llama config access succeeded on 2026-10-04 at 16:31 local time; model_access_updates.jsonl records the check. No inference settings changed.

Engineering: The first v3.1 synthetic run passed estimator assertions but its final guard assertion failed with `AssertionError: assert not Path('PREREG_APPROVED').exists()` because the reviewer created the new matching approval concurrently. The absent-approval guard now runs in an isolated empty fixture directory; no approval file is created or edited. Earlier check outputs preserved at data/_superseded/20261004T163319_v31_guard_fixture. All checks rerun. Deposit remains absent.

Engineering: Check rerun stopped with `FileExistsError: data/synthetic/excluded_top.jsonl`: a write-once fixture from the first attempt remained. All previous synthetic fixtures and partial outputs preserved in data/_superseded/20261004T163347_synthetic_rerun_checkpoint before a clean full rerun. No scientific data or estimator changes.

Amendment 3.1 implementation complete: analyze.py reads analysis.coherence_gate_applies_to, masks only listed measures, handles S2/S5 EH components separately, and retains all LHP/carryover/entropy observations. Exact change: results/amendment3_1_analysis.diff. All planted/null, independent OLS/BIC, top-control, hostility leakage, configuration-driven mask, true missingness, strict control contrast, and confidence-interval checks passed with 10,000 resamples. Timing resumed and skipped all six complete Qwen/Phi calibration cells without loading a model or regenerating; mixed historical hashes accepted only in timing mode after archived/current non-analysis config equality. Qwen and Phi immutable calibration hashes independently reverified unchanged.

Additional independent checks passed for lexical/off-channel gate omissions and config-driven separate S2/S5 EH masks. analyze.py frozen by SHA-256 in results/analysis_frozen.sha256 after successful checks and Qwen/Phi timing resume. The new reviewer-created approval hashes match; it was not created or edited by this agent. Llama remains in Stage 1 download.

### Engineering — detached follow-through

Added project-local autopilot, durable detached worker wrapper, and a format-only report renderer. Every ten minutes, the watcher checks access/approval/deposit readiness; main runs are sequential, only for manipulation-passing models. Public Zenodo files must match the approved PREREG/config hashes (including archive members); the verification is recorded before main dispatch. Saved successful cells remain immutable and are skipped on resume. Worker exit records and locks prevent duplicate jobs; recorded failures block. Interrupted complete analysis/report artifacts are verified and adopted; incomplete derived outputs are preserved before rerunning unchanged code. Main-run approval/specification/calibration checks occur before and after each cell; an interrupted-specification cell is preserved outside main raw data. STATUS writes now use a shared lock. No scientific quantity or frozen analyze.py changed. Project-local launchd services will restart crashes within the current login session; automatic registration after reboot would require writing outside study2, which is prohibited, so reboot requires re-running the local starter.

Watcher verification: offline guard/dispatch tests passed, public archive byte-matching test passed (wrong config rejected), and interrupted-job/derived-output recovery tests passed. These tests mock dispatch and never create PREREG_APPROVED or run main generations. Results: results/autopilot_checks.json, deposit_verification_checks.json, autopilot_recovery_checks.json.

Independent deposit verification (2026-10-04 17:57 PDT): reviewer-created ZENODO_DEPOSIT.md identifies Study 2 DOI 10.5281/zenodo.23147672. Zenodo API confirms published record 23147672; downloaded archive PREREG.md/config.yaml SHA-256 values match the approved local files exactly. Saved evidence: results/deposit_independent_verification.json. No Stage 3 data exist. Frozen analysis still d1aaedc674314fff939fecb85dec454fd4a7e5c93ad4c6fc3c282af899f89564; Qwen/Phi calibration hashes unchanged.

Detached services launched and independently verified at 2026-10-04T17:59:50.993901-07:00: watcher PID 81631, persistent caffeinate PID 81626. Both have parent PID 1 and independent process groups. macOS power assertions confirm indefinite prevention of system/display idle sleep. Project-local launchd crash restart is registered; reboot/login re-registration remains manual because no outside-study2 files may be installed. No Stage 3 data at handoff. Evidence: results/autopilot_service_verification.json.
