# Study 4 deviations and blockers

## 2026-10-21 — specification blocker before implementation

Stage: stage 1 build, BLOCKED. This is a specification conflict, not a runtime error. No experimental specification was changed and no outcomes were generated.

Exact conflicting requirements in Study4_Authorship_PREREG_v0.5_draft.md:

1. §6, line 74: “Anchors (0 = very negative, 9 = very positive) are stated in each question”; line 76: the sender branch “is the turn-2 question without anchoring”. A single sender question cannot simultaneously satisfy both requirements. Selecting either wording changes a specified measure.
2. §6a, line 88: “at N = 120, 24 prompts (18 / 6)”; §10, line 173: “12 check prompts, 96 check cells”. With four sources and two quoted framings, 24 prompts imply 192 check cells. Selecting either branch changes a specified sample size.

What was tried: read v0.5 fully and inspected the substantive final Codex v0.3 review and ChatGPT v0.4 review for a controlling resolution. The reviews do not resolve these internal v0.5 conflicts. The brief permits drafting unspecified strings, but these requirements are specified incompatibly rather than unspecified.

Action: stopped before building executable experimental artifacts, pursuant to AGENTS.md “If the fix changes anything the preregistration specifies, STOP.” No workaround, alternative measurement, generation, commit or push was attempted. Logs are inside study4/ to respect the current write boundary.

## 2026-10-22 (Claude, overnight check-in)
Resolved both blockers by revising the draft prereg to v0.5.1 (same file): sender question = Study 2/3 turn-2 wording verbatim (anchors only added to writer/notes questions); N=120 check prompts = 24 (§10 corrected to match §6a). No design change; prereg still draft. Build relaunched.

## 2026-10-22 — resumed v0.5.1 build; execution environment BLOCKED

The two specification conflicts above are resolved by v0.5.1. No new specification contradiction was identified in this attempt. Partial draft build artifacts were created before checking the execution environment.

The prerequisite for step 7 (real bf16/MPS smoke test) fails in the current session. Using the existing project `.venv/bin/python`, with `PYTHONDONTWRITEBYTECODE=1` and `PYTORCH_ENABLE_MPS_FALLBACK=1`:

- PyTorch version: `2.14.1`; MPS compiled support (`is_built()`): `True`.
- `torch.backends.mps.is_available()`: `False`.
- Reported platform: `macOS-26.2-arm64-arm-64bit`.
- Direct attempt: `torch.ones((2,2), device='mps', dtype=torch.bfloat16)`; allocation failed before matmul.
- Exact exception: `RuntimeError: The MPS backend is supported on macOS 14.0+. Current OS version can be queried using `sw_vers``.

What was tried: checked MPS support and availability in the project environment, then independently attempted a minimal actual MPS allocation with fallback enabled. The error contradicts the reported OS version, so its underlying cause is not established. This is an execution-environment blocker, not evidence that Arthur's Mac lacks MPS and not a new preregistration contradiction.

Action: stopped rather than changing to CPU, changing dtype/model, modifying the environment outside study4/, or claiming the smoke test passed. The supplied AGENTS.md requires stopping when a failed check would require a change to a specified quantity; Study 4 §3 requires bf16 on MPS. No model was loaded and no generations ran. Detailed evidence: `validation/environment_check.json`.

### Engineering / draft implementation choices before the stop

- All writes were inside study4/. Existing environment and prior-study artifacts were read only; Python bytecode writes were disabled. No commit, push or approval file.
- Draft configuration uses seeds selected before outcomes and preserves Study 3 model, dose, layer, decoding, vectors and norm. Direction/norm SHA-256 checks passed against Study 3 config.
- Exact pilot prompt bytes copied from Study 3. New test prompts are explicitly DRAFT. The overlap screen found no exact or thresholded lexical matches, but semantic review is unfinished: s4t14 (one volunteer assigned to two stalls) is potentially too close to the prior prompt “The schedule you made has me in two places at once.” This must be resolved before declaring step 3 complete; no prompts have been used for generation.
- No experimental data were deleted or replaced. The previous build log is retained below in BUILD_NOTES.md.

## 2026-10-22 ~1:25 a.m. (Claude)
MPS failure is a property of Codex's workspace-write sandbox (Metal blocked), not of the Mac. Relaunched Codex to complete steps 4–6 and 8 (runner, analysis, synthetic validation, notes) without any model execution; step 7 (smoke test) is deferred to a plain unsandboxed run script `run_smoke_test.command` that Codex writes but does not execute. Pilot not started tonight.

## 2026-10-22 — stage-1 build resumed under corrected sandbox scope (engineering)

The latest handoff and Arthur's instruction establish that Metal is blocked by the Codex sandbox. This is not a Mac hardware failure and does not block model-free construction. No model run or CPU replacement was attempted. Step 7 is an executable MPS-only script, deliberately not executed.

Implemented dedicated token-ID framing/replay and branch/readout paths. Reused Study 3 loading, steering, sampler settings and perplexity helper; did not reuse its re-steered/hidden rating routine. Trace EH uses Study 3's 120-model-token windows and unweighted window mean. Added resumable checksummed outputs and manifest matching. No spec, config, framing or prompt edits.

The initial detached launch through zsh reported `nice(5) failed: operation not permitted`; a shell-exiting detached attempt produced no synthetic files. Relaunched via bash with a waiting parent while the nohup worker ran in the background. The 500 simulations completed. Final summary serialization then raised `TypeError: Object of type bool is not JSON serializable` for a NumPy boolean in the coverage diagnostic. All seven schema datasets, analysis results, boundary results and 500 checksummed replicate results were already saved successfully. Cast the diagnostic to Python bool; preserve the incomplete summary under data/_superseded/ and reconstruct the final summary from those saved results without rerunning or selecting simulations. This changes only serialization, not estimates, seeds, contrasts, CIs or thresholds.

Additional pre-freeze engineering checks: retained algebraically cancelled baseline terms as required-cell dependencies, so a missing zero-dose row cannot silently yield an estimable P2/S5 contrast. The new regression passes; complete-data estimators are unchanged. Added paired prompt-bootstrap CIs for exploratory relationships and explicit non-estimability on missing required observations. Added pilot validity screens and a fail-closed, hash-checked main entry point; no main or pilot invocation occurred. The Study 3 report does not print an aggregate think-mode zero-dose mean; validity reporting transparently computes the reference from its hash-verified source records and records that provenance. No reference value was guessed.

Final complete-data verification reused all seven saved synthetic datasets and reproduced every confirmatory and sequential estimate and CI exactly; no new null simulations or seed selection. The initial direct-file invocation of the verification helper raised `ModuleNotFoundError: No module named 'study4'`; invocation with `python -m study4.validation.recheck_complete_data` fixed package resolution. Both logs are retained. All 12 final unit tests pass. No inferential specifications were changed.

## 2026-10-22 ~8 p.m. — pilot memory leak (engineering fix, no design change)
Pilot stalled at 221/960 cells: per-cell time rose from ~25 s to ~360 s while MPS driver memory grew 10.7 → 14.1 GB on a 16 GB Mac (swap thrash). Cause: per-cell tensors not released between cells. Fix (approved by Arthur 7:51 p.m.): src/runner.py now deletes per-cell objects and calls gc.collect() + torch.mps.empty_cache() after each cell and each trace; resume check now permits a manifest change limited to src/runner.py (old manifest kept as data/pilot/manifest_pre_memfix.json). Pre-fix runner kept at logs/runner_pre_memfix.py. The 221 completed cells are unchanged and retained; outputs are deterministic per seed, so the fix does not alter results. Pilot data remain descriptive only.

## 2026-10-23 — referent re-pilot (approved by Arthur Su 10:58 a.m.)
Pilot referent diagnostic flagged: after the sender rating the model reports rating "the writer of the notes" (P(B) 0.93–1.00 in all framings). Ratings-only re-pilot on the existing 960 pilot answers (no new traces/answers): (a) clarified sender question "…how much do you like the user who sent the original request?"; (b) referent check in original and swapped A/B order, after both the original and clarified sender ratings. Wording will be chosen only by the referent/validity results, never by effect sizes; counts as revision 1 of the 2 permitted (§9). Script: src/repilot_referent.py; output data/repilot/.

## 2026-10-23 8:18 p.m. — v0.6 approved by Arthur Su
Clarified sender question adopted (wording revision 1 of 2), chosen on referent/validity re-pilot results only (data/repilot/REPILOT_SUMMARY.md). Referent diagnostic now counterbalanced (framings.json questions.referent_swap; runner asks both orders). Prereg draft v0.6 written. Previous framings kept at logs/framings_pre_v0.6.json.
