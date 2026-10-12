# Study 3 pre-approval checks — implementation log

## Engineering — cache snapshot discovery

Initial setup assumed one cached classifier snapshot and stopped with:

```text
AssertionError: Expected one frozen cached snapshot for j-hartmann/emotion-english-distilroberta-base: ['7e9d7fe536a4d2bb472f9e883cc6cbbe81f68961', '0e1cd914e3d46199ed785853e12b57304e04178b']
```

No generations ran. Inspecting the frozen cache main reference to identify the revision used by the pilot; no model choice or setting changes.

Resolved cache discovery by reading the frozen main refs. The classifier has a main PyTorch checkpoint and an auto-converted safetensors snapshot; all 106 state tensors are bit-identical. Use the main local snapshot with local_files_only=True. No external cache writes or generation occurred during setup.

## Implementation of the required checks

P1 calibration verified against its SHA-256 manifest; direction hashes verified against that calibration. Residual norm matches the verified calibration, and all copied artifacts match source hashes. No re-extraction or dose selection. Shared environment unchanged. Model and classifier load from explicit read-only pilot snapshot paths; writable caches are study3/.cache.

Both modes use .6/.95/top-k20, 1024 thinking tokens and 200 answer tokens. Only turn-1 thinking mode changes. Turn-2 prefix always uses the non-thinking template and is verified token-identical across modes. Three full-forward ratings are timed per cell, including a fresh unsteered R_zero on the saved baseline sequence; no generation cache is used for ratings.

Trace EH uses non-overlapping 120-token model-ID windows, including a final partial window, with an arithmetic mean across windows. Answer EH uses the full answer and the fixed Study 2 classifier. No coherence exclusions or inferential tests are applied to these descriptive checks. Only Stage A–C code is implemented, not main-study analysis.

Engineering: unused per-token raw-logit arrays and generation caches are released before the full-forward ratings to limit memory. Sampling and every specified measure are unchanged. No raw-logit measure is requested in checks A–C. Tokenizer-only check verified the shared empty-thinking rating prefix before generation.

Engineering check: a CPU toy tensor confirms the rating hook modifies only the specified turn-1 positions and is removed after the context exits. Actual zero-dose agreement is checked on every finished calibration cell. Inference source hashes were fixed before launch; the subsequently written descriptive report renderer has a separate hash manifest.

## Author-approved Stage D extension

During the final Stage A cell, the reviewer appended Stage D and supplied draft v0.3. Stages A–C remain under v0.2 and alpha=0.02 exactly as requested. The original A–C AGENTS bytes were recovered from the unchanged prefix and verified against their pre-run hash; they are preserved in results/stageABC_AGENTS_snapshot.md. The original source manifest and inference-code manifest remain unchanged. A completion manifest verifies both that snapshot and the appended AGENTS.md. Only the descriptive reporter was updated to use the completion manifest; no inference code or data changed. Stage D uses v0.3 only after A–C finish.

Stage A completed 80 cells with no runtime errors and no logged CPU-fallback warning. The worker and its attached keep-awake process exited normally. Original source artifacts, inference code, all cell keys, shared rating prefixes and zero-dose agreement were verified. The original mixed-mode ETA understated the final block; a separate polling helper recorded block-specific estimates without changing the running inference code.

## Stage D specification block

SpecificationError: v0.3 does not fully determine the pulse numerical path, coherence-gate aggregation, or exploratory sample/subset rules; completing and freezing these choices would require scientific design decisions.

Read the complete appended AGENTS.md and v0.3 draft, and checked the inherited Study 2 measure/hypothesis definitions and existing generation/cache and rating code. These resolve S3/S4 but do not uniquely resolve the pulse cache transition, pulse rating/LHP masks, gate aggregation/eligibility, E3 subset or E4 sample. Full audit: results/stageD_blocked.md. No scientific workaround, Stage D model call, test-file access, approval marker or analysis freeze was made. Stages A–C remain complete and separately committed.

## Stage D v0.4 resolution implementation

Read AGENTS.md and v0.4 completely. The reviewer resolved all four earlier blocks. A–C and their code/data remain unchanged. Stage D is implemented in separate modules using alpha_top=0.0175, unsteered pulse re-encoding and S5=X_pulse. Shared zero records are expanded virtually for direction-specific estimators, never regenerated. Seeds and LHP standardization follow the inherited Study 2 definitions and are fixed before synthetic checks. The test-set hash is copied from the author only; the test file remains unopened.

### Engineering — toy cache-test fixture

The model-free pulse test initially failed with `KeyError: 9` at test_stageD_engineering.py Fake.__call__: the fixture omitted the terminal-token forward that the real runner correctly performs to complete its cache. Added the EOS self-transition to the fake model. No production code, settings, data, or synthetic estimators changed. The detached dry run continued unchanged.

### Engineering — required-input audit before freeze

Found an unnecessary baseline dependency in H retrieval: H=R_full−R_text needs no R_zero. Restricted the baseline requirement to C and X. Exact diff: results/stageD_analysis_engineering.diff. This restores the specified S4 estimator rather than changing it. Original synthetic validation outputs are retained under data/_superseded; rerunning the unchanged seeds plus a missing-baseline regression.

Stage D conventions implementing the resolved text: pulse natural closure receives the canonical two-newline answer separator before the unsteered re-encoding; the full-rating pulse mask stops at the closing thinking token, leaving separator/answer/turn 2 unsteered. Entropy is accumulated from raw logits at sampled tokens only, without retaining large vocabulary arrays; forced tokens do not count as sampling steps. Regular LHP uses the exact prefix immediately before its answer phase; pulse LHP is unsteered. These choices are recorded in config.yaml and checked with natural and forced toy paths. Gate medians are fixed for each analyzed dataset, not recomputed in bootstrap resamples. E3 reruns the same estimators and gates on its specified common prompt subset.

### Engineering — complete-prompt accounting before freeze

Removed an unnecessary assumption that all 80 main prompt IDs follow a particular spelling (only E4 IDs are specified). The analyzer uses IDs in raw records and enforces the specified 80-prompt count; if an entire prompt is absent, all confirmatory hypotheses are not estimable. Explicit prompt lists remain available for synthetic and E3 subsets. Exact diff: results/stageD_prompt_integrity.diff. Complete-dataset estimators are unchanged. Repeating the same fixed-seed suite with an additional missing-whole-prompt regression; previous outputs preserved under data/_superseded. No test prompt was read to make this correction.

Engineering edge check: an entirely empty input now reports 80 missing prompts and all hypotheses not estimable, using `None` for the unavailable LHP scale rather than taking the standard deviation of an empty array. The one-line scale guard adds `lhs and` before the complete-data test; no nonempty-input calculation changes. Verified without model calls.

## Stage D completion and freeze

All 34 dry-run cells completed (28 regular, 6 pulse), using s2c00 and s2c01 only. Zero-dose agreement and repeated R_zero scores match exactly. Full integrity and no-op resume checks pass; no dry-run inference code changed during execution. Final analysis candidate reproduced all saved synthetic scenario outputs and 200 null-replicate verdicts exactly. Both primary false-positive rates are 0/200 at a nominal 2.5% requirement. Secondary, gate, missing-data, truncation-floor and pulse-path regressions pass. All project Stage D background workers and their attached caffeinate processes exited. No runtime error or CPU-fallback warning was reported in the dry-run log. Code, config, preregistration and runtime dependencies are frozen in results/frozen_hashes.sha256. No test file was opened, read, hashed or generated on; no PREREG_APPROVED was created and no main run started.

## Stage E preflight

Author approval and the local deposit record were read completely. The unchanged approval guard passed before test-file access; every frozen and runner/input manifest hash matched. The web tool could not access https://zenodo.org/records/23247883 (URL not accessible via this tool). The local deposit record and explicit author/reviewer publication attestation satisfy the implemented guard; no frozen file was changed.

Stage E operational monitoring: an unfrozen checkpoint helper updates counts/stratified ETA and commits saved raw rows hourly. It does not alter model calls, frozen files, scientific quantities or outputs. The frozen runner retains its historical "Stage D main" log label; STATUS monitoring identifies the task as Stage E. Main worker PID 17388, caffeinate PID 17389; monitor PID 17447, monitor caffeinate PID 17448.

### Stage E engineering: durable continuation and post-run audit

An hourly same-task Codex heartbeat (study-3-stage-e-follow-through) is active to continue monitoring and perform the approved integrity audit, unchanged analysis, and report after generation completes. The detached checkpoint monitor independently updates STATUS every minute and commits progress hourly. Added src/stageE_integrity.py as an operational read-only audit of completeness, provenance, and numerical consistency; it does not alter the frozen analysis, gates, or raw data. Frozen hash verification still passes.

## Stage E completion

All 1,360 cells completed at 2026-10-09 16:51 PT, without a restart or frozen-file change. The post-run integrity audit passed: 80 unique prompts, exact planned cell keys, complete numerical measures, provenance, rating masks, and zero-dose agreement. The unchanged analyzer ran detached with caffeinate (PID 65425; caffeinate 65426) and completed. Added an unfrozen formatting-only report renderer, src/stageE_report.py, which consumes saved analysis output, adds the required plain-English summary and fixed-sample descriptive notes, and reproduces the full Stage C reference and deviation log. No estimator or exclusion rule changed.
