# Study 4 build notes — stage 1, steps 4–8

2026-10-22. **Requested model-free build complete. Real MPS smoke test is deferred to the executable launcher, which was not run. No pilot or main study ran.**

The prior MPS error was caused by the execution sandbox blocking Metal, per the corrected handoff. It is not evidence of a Mac failure and was not treated as a blocker. All writes in this continuation stayed inside study4/. No environment modification, model loading, CPU inference substitution, approval file, commit or push.

## Build inventory

| Step | State | Artifact |
|---|---|---|
| 1–3, prior drafts | Unchanged; author review still needed | framings.json, config.yaml, prompts/, prior overlap audit |
| 4. Runner | Implemented; model-free tests pass | src/runner.py, src/common.py, src/approval.py |
| 5. Analysis | Implemented and hash-frozen | analysis/analyze.py, analysis/validity.py; validation/analysis_freeze.json |
| 6. Synthetic validation | Passed, actually executed | validation/RESULTS.md, synthetic/summary.json, final_synthetic_analyses/ |
| 7. MPS smoke | Launcher written, executable, syntax checked; deliberately unrun | run_smoke_test.command |
| 8. Handoff notes | Complete | This file and STATUS.md |

## Runner

Trace generation preserves Study 3 pulse semantics at layer 18, bf16/MPS, dose 0.0175, specified sampling and caps. Pilot mode reuses exactly 320 Study 3 traces, generating no new traces. Smoke mode uses only s3t00 and s3t60, all four sources and three framings, with explicitly labelled 32/16 thinking/answer caps. Main mode reads test prompts only after a matching approval and analysis-freeze guard.

Trace IDs are never decoded and retokenized for insertion. All 320 saved native prefixes match exactly; quoted frames retain the same trace IDs. Every post-trace operation asserts that module and global forward/pre-forward hooks are absent. Answer generation starts with no cache; each rating, check and perplexity calculation gets a complete fresh unsteered forward. Only incremental answer decoding uses its own newly created unsteered cache. Independent sender/writer/notes branches share identical post-answer history; sequential writer/notes branches separately append the sender argmax. Native framing has sender only. Label/operative branches use post-answer history; referent uses sender plus argmax as declared in framings.json.

Outputs are append-only checksummed traces.jsonl and cells.jsonl. A separate checks.jsonl links checks to the exact main-cell/post-answer history, without regenerating an answer. Main and check analyses are separate. Resume validates row checksums, rejects duplicate keys and mismatching config/prompt/code manifests, and skips completed cells. A partial/corrupt line causes a stop for preservation/investigation rather than silent repair. Trace classifier scoring follows Study 3's contiguous 120-model-token windows and unweighted mean; answers use the fixed full-answer classifier. Failed classifier measures remain missing. Per-cell token IDs, branches, distributions, valid mass, seeds, timing, sampled peak driver memory, replay assertions, trace references and template-segment hashes are recorded.

Main approval guard expects JSON with name, date and a sha256 mapping keyed by the prereg filename, framings.json and config.yaml. No such file was created. Main analysis also accepts an explicitly recorded pilot-based P2 downgrade via --p2-secondary; it never decides that downgrade from test outcomes.

## Analysis and evidence

P1/P2, S1–S5 and the notes comparator use explicit within-prompt contrasts. Shared prompt-cluster draws provide 10,000 percentile-bootstrap samples; primary CIs are 97.5%, secondary 95%, equivalence CIs 90% with ±0.15 component margins. Conjunctions require every component. Missing required cells, including baselines that cancel algebraically, make the statistic not estimable. Coherence gates remove only affected text outcomes and preserve ratings. Manipulation failures prevent P2/S5 interpretation; operative checks remain descriptive. Reading tables in §§8/8a are emitted with these restrictions.

Implemented E2 content relationships, E3 naturally closed complete-prompt subset (minimum 20), E4 sender/writer relationship, E4b sequential estimates and component differences, E5 blind-audit exclusions, headroom/digit-mass diagnostics, provocative/neutral splits, referent diagnostics and fixed random qualitative examples. Semantic coding and qualitative tags require human review, not fabricated automated judgments. The fixed draft rubric is analysis/audit_rubric.json; --audit accepts a prompt-ID mapping with instructions and negative_characterizations booleans. Missing audit coding makes E5 not estimable.

Power uses 10,000 bivariate-normal mean draws with the pilot P2 component covariance, targets −0.50/−0.29, normal 97.5% CI half-widths, and the fixed 80/120/downgrade rule. S5(b) expected 95% CI half-widths are reported. Pilot validity reports fixed-token segments, native baseline agreement, baseline SD and valid mass; it never revises a wrapper automatically. The reference mean computed from the 80 hash-verified Study 3 think-zero source records is 7.3921980202 (SD 0.6200515616). The Study 3 report does not print this aggregate; validity output records its source rather than guessing a report value.

12 unit tests pass. Seven synthetic patterns pass, including writer-inference-only and notes-only counterexamples. All 500 null simulations ran with 10,000 resamples each. Component coverage: 93.4–96.2% for nominal 95%; 96.2–98.2% for nominal 97.5%. See validation/RESULTS.md and final_tests.log. The final code reproduces saved confirmatory/sequential component results exactly. Hash freeze covers analysis Python files; the manifest also records the rubric and evidence hashes.

## Real-run commands (not executed here)

Run the short smoke test outside the sandbox:

```bash
/Users/arthursu/Projects/affect-suppression-steering/study4/run_smoke_test.command
```

It changes to the project directory, launches the two-prompt MPS-only smoke run, keeps the Mac awake with caffeinate, and writes validation/smoke/run.log, traces.jsonl, cells.jsonl, checks.jsonl and summary.json. Summary and cell rows contain timings and sampled peak driver memory. **No real timings or memory numbers are available yet.** A successful short-cap smoke is not a full-context benchmark.

Exact full pilot launch command, for a later authorized session after smoke review:

```bash
cd /Users/arthursu/Projects/affect-suppression-steering
mkdir -p study4/data/pilot
PYTHONDONTWRITEBYTECODE=1 PYTORCH_ENABLE_MPS_FALLBACK=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 nohup .venv/bin/python -B -u -m study4.src.runner --mode pilot --output data/pilot > study4/data/pilot/run.log 2>&1 &
pid=$!
caffeinate -dimsu -w "$pid" &
```

After that pilot finishes, run the validity and descriptive analysis:

```bash
.venv/bin/python -B -m study4.analysis.validity --input study4/data/pilot/cells.jsonl --output study4/data/pilot/validity.json
.venv/bin/python -B -m study4.analysis.analyze --input study4/data/pilot/cells.jsonl --prompts study4/prompts/pilot_prompts.jsonl --manifest study4/data/pilot/manifest.json --output study4/data/pilot/analysis.json
```

These commands were not executed. Pilot data must not be pooled with the main study. Review the resulting power decision, complete-context timings and peak memory before approval.

## Open review items and limitations

- Existing test-prompt draft s4t14 has the previously documented semantic overlap concern. Step 3 remains incomplete; no prompts were changed in this continuation.
- Author sign-off remains needed for the drafted quoted wrappers, writer/notes anchor and digit suffix, referent placement, and explicit-content rubric.
- No real model execution, pilot validity decision, manipulation-check result, full-context benchmark or sample-size decision exists yet. The project is not ready for approval/main execution merely because model-free tests pass.
- Draft choices for descriptive headroom use expected rating ≤0.5 / ≥8.5; raw baseline values are also reported. This is labelled in output and does not affect hypothesis decisions.
- Launch and serialization errors, preserved partial outputs, fixes and verification are recorded in DEVIATIONS.md. No statistical or experimental specification was changed.

Stopping after step 8 as requested.


## Test prompts approved (2026-10-22)
Arthur Su approved the 80 test prompts on 2026-10-22, with s4t14 replaced by: "The packing list you wrote puts the fragile items at the bottom of the box." (prior s4t14 was conceptually close to Study 2 s2t55). File frozen: study4/prompts/test_prompts.jsonl, SHA-256 14ac0de7f734b42a2208c39b39877abe79110c67a7892e9465fc82a6644e01d5. Do not edit; any change requires Arthur's re-approval.

## Wording and rubric approved (2026-10-22)
Arthur Su approved draft strings 1–5 as written: quoted_before/quoted_after wrappers, own/other labels, writer/notes anchor and digit-only suffix, referent-branch placement, and the E5 explicit-content rubric. E5 coder: Claude, blind to framing, answers and all outcomes, coding completed before unblinding (Arthur did not specify a coder; default recorded here, revisable by Arthur).
Hashes at approval:
89506dfde9b15b81347d896b6534f0de4df8f96948b7ba5d994121afd34870ef  framings.json
831a646bd87e64b2685c50da5be735be858d65ec2ccf1c52fc03b7d479e2c913  analysis/audit_rubric.json
