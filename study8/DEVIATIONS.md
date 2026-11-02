# Study 8 deviations and blockers

## 2026-10-29 — Build blocked: missing specified calibration authorship

**Status:** BLOCKED; no specification deviation implemented.

**Requirement:** Build brief step 2 requires the judge calibration set per preregistration §3. That section requires 60 external answers “written by Claude and labeled before any judge is run.”

**Observed problem:** No Study 8 calibration answers or separate label file are present in the available Study 8 files. A repository filename search for calibration and rubric artifacts found earlier-study material but no Study 8 calibration source. Available tool metadata contained no Claude capability. This is a missing-input/provenance blocker, not an inference exception; there is no runtime stack trace.

**Checks attempted:** Read the build brief and complete v0.2 specification; inventoried `study8/`; searched repository filenames for calibration/rubric material; checked available tools for Claude. No judges or model generations were run.

**Why work stopped:** Creating the set as Codex and calling it Claude-written would misrepresent provenance; creating it as Codex with accurate attribution would still change a specified study quantity (the calibration-set author). The project instructions say: “If the fix changes anything the preregistration specifies, STOP.” No workaround was applied.

**Required input for resumption:** The specified Claude-authored set with separate pre-judge labels, or an explicit author amendment permitting Codex authorship. No amendment, approval, or commit was made by this session.

## Engineering

None implemented. Only this blocker log and `STATUS.md` were created.

## 2026-10-29 — Engineering build resumed

The supplied Claude calibration set resolves the previous missing-input blocker. No calibration files were edited. Implemented Study 8 only. A first successful synthetic result set was preserved at `data/_superseded/20261029T122148` before rerunning after adding crossover missingness reporting; no experimental data exist. No hypothesis, threshold, prompt, direction or model was changed.

## 2026-10-30 — Authorized v0.3 judge update (steps 1–5)

Implemented the author-approved v0.3 procedure and thresholds exactly as §3, including Gemma separation ≥0.75, Llama ≥0.5, and agreement mean absolute difference ≤0.75. The probe’s historical ≥1.0 threshold was not reused; its a/e prompts and digit-ID logic were reused verbatim. Added b/c/d/f/g/h from the existing rubric anchors. No models or study outcome analyses were run, no commits or approval file created.

Engineering: first synthetic rerun stopped with `RuntimeError: Existing artifact differs: /Users/arthursu/Projects/affect-suppression-steering/study8/data/synthetic/null/analysis.json`. Inspection found Python tuple versus JSON list differences in contrast terms, not numerical or decision differences. Fixed `common.ensure` to compare JSON-normalized values (still rejecting changed data); rerunning existing synthetic fixtures preserves their contents. Failed run log retained as `logs/synthetic_tests_v03.log`; subsequent run uses a separate log. No data deleted or overwritten.

Engineering: the judge-only launcher archives v0.2 judge rows and validity receipt to `data/pilot/judge_v02/` on execution, refuses archive collisions and retains v0.3 rows on restart. It has not been executed. Existing pilot exports retain identical neutral IDs and order. The legacy v0.2 artifact constructor now refuses to regenerate v0.3 artifacts with stale defaults.

Engineering completion: 14 unit tests and all six 10,000-resample synthetic scenarios pass. Prior freeze candidate and one-time migration script preserved in `data/_superseded/v03_build_20261030T075543Z`. No experimental data modified. Stopped after v0.3 step 5.

Engineering: judge-only launcher preserved v0.2 outputs in data/pilot/judge_v02/: judge_gemma.jsonl, judge_llama.jsonl, validity.json. Qwen data unchanged.

## 2026-11-01 — Trace-content audit method (main run)
The blind audit of all 960 main traces (prereg §6) was done by Claude, blind to source and context (audit_inputs.json only; audit_map, cells and judge scores not opened), as a lexical screen followed by manual review of every negative_user, hostile_instruction and rating_reference hit and a sample of kindness_strategy hits, rather than full reading of every trace. Rules: negative_user = pejorative characterization of the user's character, attitude or competence (descriptions of the user as confused, upset or frustrated, or statements that a claim is wrong, are not counted); hostile_instruction = plan to answer sarcastically, mockingly or harshly (negated plans not counted); kindness_strategy = the assistant's own plan to apologize, reassure, empathize, thank, or be polite/kind/friendly; rating_reference = explicit reference to the anticipated rating or its "kind and pleasant" criterion. Counts: 13, 5, 269, 19. Screening scripts in data/main/audit_tools/. Codes committed before any outcome was opened. Recall of the lexical screen is not validated; this is a sensitivity subset only.
