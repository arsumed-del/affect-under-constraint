# Study 6 build — steps 1–7 complete

This is a build, not a pilot or experiment run. No model weights were loaded, no model inference was performed, no approval was created, and no commits were made. All changes and outputs are inside `study6/`. The preregistration and prior studies remain unchanged.

## Built

- `config_s6.yaml`: Qwen3-4B and tokenizer revision, model-file hashes, Study 5 main/pilot cells and framing/config hashes, inherited code and E5 audit hashes, exact software versions, MPS/bfloat16/SDPA, batch size one, no padding, no cache, seed 20261027, and all arm counts.
- `generic_answer.json`: the exact preregistered G and its real-tokenizer IDs, stored once. Runtime checks its tokenization; it never replaces the stored IDs with retokenized answers.
- `src/assembly.py`: stored prefix + replayed answer + inherited Study 4 answer closure + Study 5 sender branch. All original branches are checked before loading the inference backend. U-with-a_U must be token-identical to Study 5.
- `src/runner.py`: inherited Study 5 `Backend.rating()` and Study 4 forward/hook checks; fresh full-sequence forward, no generation, steering or KV reuse. Saves hashes, answer provenance/IDs, digit probabilities, unconditional and digit-conditional log probabilities, expected digit, mass, replay difference, timing, memory, warnings and process ID. Garbage collection and MPS cache clearing follow every cell. Append-only checksummed rows, file lock, exact manifest/resume verification, and immediate numerical-failure stop preserve evidence.
- `src/validity.py`: 0.01 per-cell replay tolerance; two distinct pilot process starts; group and per-arm valid mass; placement exclusions; longest-prefix timings and a measured runtime estimate once the pilot runs. Main requires both approval and recomputed, matching pilot validity. If no placement survives, main is blocked.
- `src/approval.py`: author/date/Zenodo record and exact freeze hashes. The candidate manifest is explicitly **NOT APPROVAL**.
- `analysis/analyze.py`: TE, D_U/D_T/D_Q, M^X, separate control replacement brackets, M_T/M_Q, swap, interaction, generic effects and guarded descriptive proportion. The stored Study 5 U rating is the shared baseline; rerated U cells are validation only. Primary confidence level is exactly `1 - 0.05/3`; secondary intervals are labelled unadjusted. Includes conjunction decisions, equivalence/overlap/reversal and mixed-control labels, the Section 4 readings, answer/rating descriptives, and completed-answer/natural-closure/E5 subsets with counts.
- `run_pilot.command` and `run_main.command`: executable zsh launchers with caffeinate, unbuffered project Python, fallback/offline/bytecode settings and live `tee` logs. Written and syntax-checked, **not launched**.

## Validation results

The real CPU tokenizer reconstructed every one of the **1,600 main and 80 pilot** original Study 5 branches exactly. All **400 main U-with-a_U** inputs matched their stored branches. The generated plans have exactly **2,640 main** cells and **212 first-start pilot** cells (132 arms + 80 sham), followed by **80 second-start sham** cells.

The final test suite covers 14 tests: branch reconstruction across all sources/placements; natural, emitted-end-token and truncated closure; G insertion; malformed/duplicate/missing input rejection; numerical tolerance and resume hash failures; absent approval; hook detection and inherited rating-path identity; two-process sham gate; planted no-change, partial attenuation, full attenuation, amplification, reversal, mixed-control and missing-cell patterns; exact shared-baseline cancellation on dyadic fixtures; primary/secondary CI levels; unclipped proportions and null denominator suppression; heterogeneous joint-bootstrap CIs; subset counts and invalid-placement exclusions.

See `results/final_build_tests.log` and `results/synthetic_validation.md`. Each scenario has `analysis.json` and `analysis.md` under `data/synthetic/<scenario>/`, prominently labelled synthetic. No real Study 6 analysis result is claimed. Initial build artifacts were preserved under `data/_superseded/` with the reason in `DEVIATIONS.md`.

A metadata-only model construction on PyTorch's `meta` device confirmed the inherited model loader's default attention implementation is **SDPA**, with bfloat16 parameter metadata. This loaded no weights and performed no forward pass. Runtime independently asserts actual MPS, bfloat16 and SDPA. Shell syntax checks passed. Input/model hashes are checked by `build_artifacts.py` when producing the candidate manifest.

## Explicit choices where the draft is abbreviated

1. **Bootstrap seed:** 20261027, fixed before any Study 6 inference. One master matrix of 10,000 uniform prompt draws drives every statistic. Common prompt masks use identical draws. Sensitivity subsets resample exactly their retained n clusters from the same master uniforms, jointly across studies/arms; they do not drop individual cells within a sampled prompt.
2. **Missing data:** inherit Study 5's fail-closed analysis rule: a missing required cell makes the affected estimand not estimable, while unaffected estimands remain available. There is no silent complete-case primary analysis. Numerical/token failures instead block execution.
3. **Valid mass aggregation:** mean by placement × source, pooling planned arms (and sham replays in the pilot), matching Study 5's mean-mass convention. Per-arm groups are also reported. Any failing source group drops that entire placement from all estimands; pilot and main exclusion sets are combined. Missing groups are reported incomplete, not treated as observed low mass. At least one placement must survive pilot validity.
4. **Two process starts:** first process runs 132 intervention cells plus 80 sham cells. A second process repeats all 80 sham cells. These repeats are validation overhead, not additions to the 132-cell pilot arm design. Each interrupted second-start attempt is preserved and a new process repeats all 80, so the final second replay is one intact process-start set. Main approval rechecks both sets, hashes and per-cell tolerances.
5. **Completed-answer subset:** D contrasts use naturally ended a_U. TE, M^X, control replacement contrasts, swap and interaction use both naturally ended a_U and a_H; this keeps the TE/replacement/swap comparisons paired. Control-relative replacements retain their recorded a_C without adding an unstated control-answer truncation exclusion. Generic sensitivity uses the same a_U eligibility for comparability. Counts are reported for every estimand/placement.
6. **Inherited subsets:** natural closure requires all four source traces to close naturally, retaining entire prompt clusters across placements exactly as Study 5. E5 uses its frozen audit map: neither instructions nor negative characterizations. Neither subset changes the primary analysis.
7. **Proportion denominator:** interpret “denominator excludes zero in ≥97.5% of draws” as at least 97.5% of bootstrap TE values lying strictly on the point-estimate side of zero, plus supported negative TE at its descriptive 95% interval. Exact-zero bootstrap denominators suppress the ratio rather than being discarded. Ratios are not clipped.
8. **Specificity and readings:** M1 is decided by the two-sided M^X criterion; opposite point-estimate signs for M_T/M_Q receive the separate “mixed control-relative effects” label. Reversed directional effects retain the reversal label even if within the equivalence margin. Small-but-detectable takes precedence over the broader reading-table rows. Both-negligible and otherwise unresolved combinations are stated explicitly. R3 uses its own secondary M^X. Interactions outside R1/R3 are exploratory, not extra secondary hypotheses.
9. **Generic hostility:** G has no stored Study 5 classifier score, so its EH is unavailable, not newly scored. Replayed answers use their donor's stored EH.
10. **Memory:** peak driver allocation is sampled by the inherited forward wrapper, as in Study 5; it is not an independent profiler of transient kernel allocations. CPU fallback warnings are captured and printed; the code does not pretend to enumerate silent backend-internal fallbacks.

## Remaining matters for Arthur before freezing/running

- Pilot numerical reproducibility on actual MPS remains untested, including the second process start. The 0.01 threshold will not be changed if it fails.
- Main runtime and memory estimates await the authorized pilot, particularly its longest prefixes. The build intentionally supplies no invented hours estimate.
- Review the explicit operational choices above, especially mass pooling, completed-answer eligibility and the denominator rule, before approving the freeze. No clarification or decision was needed to perform the authorized CPU build.
- The candidate manifest is not consent or a Zenodo deposit. An author-created `PREREG_APPROVED` and passing pilot validity are required for main. This build stops at step 7.

## Commands for a later authorized session (not executed here)

CPU-only tests: `PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B -m unittest study6.tests.test_build -v`.

Pilot launcher: `study6/run_pilot.command` (two successive process starts). Main launcher: `study6/run_main.command` (fails closed without approval and pilot validity). After a completed approved main run, `.venv/bin/python -B -m study6.analysis.analyze` writes `study6/results/analysis.json` and `analysis.md`.
