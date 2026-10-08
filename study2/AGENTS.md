# Instructions for the coding agent — Study 2

You are implementing and running Study 2 of a preregistered experiment on Arthur Su's Mac Mini (Apple M4, 16 GB). Arthur is a psychiatrist, not a programmer, and is often traveling. A reviewing Claude session audits your work. Work through the stages without asking Arthur questions; keep `STATUS.md` current.

This folder (`study2/`) sits inside the Study 1 project. **Study 1 is complete and frozen: never modify anything outside `study2/`**, except reading Study 1 code to copy it. Reuse the existing environment at `../.venv`.

Read first, completely: `PREREG.md` (v3.0), `config.yaml`, everything in `prompts/`, and, for reference, Study 1's `../src/` code and `../PREREG.md` §7–8.1 (whose estimators Study 2 reuses).

## Prime directive

You execute the specification; you do not choose it. Every change that would make a result "work" is forbidden.

## Never

- Never edit `PREREG.md`, `config.yaml`, `prompts/`, or this file.
- Never edit a file in `data/calibration/` once written, or anything in `data/raw/`.
- Never change doses, layers, prompts, conditions, directions, models, classifier, decoding, measures, exclusions, or analysis to improve a result.
- Never generate on `prompts/test_prompts.jsonl` before Stage 3.
- Never start Stage 3 unless `PREREG_APPROVED` exists, its hashes match `PREREG.md` and `config.yaml`, and `ZENODO_DEPOSIT.md` exists with a DOI for this preregistration.
- Never touch files outside `study2/` (except caches). Never push to a remote. Never enter passwords, tokens or keys.
- Never delete data; move superseded outputs to `data/_superseded/<timestamp>/` and log why.

## When something fails

Write the exact error and what you tried to `STATUS.md` and `DEVIATIONS.md`. If a fix would change anything the preregistration specifies, STOP (mark BLOCKED). Pure engineering fixes that leave every specified quantity unchanged are fine; log them under "Engineering". If the specification is ambiguous, list **every** ambiguity you can find in one report (`results/blocked.md`) before stopping.

## Long runs

Run long jobs in the background with nohup, detached so they survive tool-session closure (Study 1 used `subprocess.Popen(start_new_session=True)`), with `caffeinate -dimsu -w <pid>`. Make them resumable (append one JSON line per finished cell; skip completed cells on restart). Poll and update STATUS.md with progress and ETA. Commit after each stage.

## Stages

### Stage 0 — Setup
- Create `study2/src/` by copying and generalizing Study 1's code (model loading, chat formatting, steering hook, generation with raw logits, teacher-forced opener scoring, two-turn ratings, metrics). Remove Qwen-only and version guards; select models, calibration files and outputs per `config.yaml`. Drop the layerwise logit lens.
- Verify Hugging Face access to all three models' configs. `meta-llama/Llama-3.2-3B-Instruct` is gated: if access fails, mark **Llama: BLOCKED (Arthur must accept the Meta Llama 3.2 license on Hugging Face)** and continue with the others; do not substitute a model.
- Record versions to `env.txt`.

### Stage 1 — Smoke test (each available model, calibration prompts)
Same checks as Study 1 Stage 1: coherent α=0 output, tokens/s and peak memory, hook removal exact, finite opener scores, both rating paths agree within 0.05 at α=0 with identical visible ids, system role applied correctly. Write `results/stage1_smoke.md`.

### Stage 2 — Directions, dose selection, manipulation check (each available model)
Extract hostility and technicality directions and build the random direction exactly as specified; measure the mean residual norm. Run the dose rule in PREREG §6 / `config.yaml: dose_selection`: evaluate candidates in increasing order on the 40 calibration prompts (neutral condition, hostility), determine the coherent range (stop at the first candidate failing either coherence check; ppl ratio limit 3.0), compute the manipulation check (EH minus α=0 EH, 95% bootstrap CI, lower bound > 0) for every candidate in the coherent range, and set α_max to the largest coherent candidate that passes. Write `data/calibration/<slug>.json` once (α_max, grid, all per-candidate statistics, direction hashes, mean norm). If no candidate passes, mark that model **EXCLUDED (manipulation check failed)** and stop work on it. Write `results/stage2_<slug>.md`.

### Stage 2b — Analysis code on synthetic data
Write `src/run_main.py` (resumable; everything in PREREG §7) and `src/analyze.py` implementing §8–9 exactly: P1 and P2 with **97.5%** CIs and their control contrasts; S1–S5 with 95% CIs (S2 and S5 estimators as Study 1 §8.1); the coherence gate (4.0); "not estimable" handling; the generality rule in §8.3; per-model tables. Validate on synthetic data with planted and null effects (and one synthetic model with an excluded top dose, to check "not estimable" handling). Do a short timing run on calibration prompts and estimate Stage 3 runtime per model. Freeze `analyze.py` by hash. Set STATUS.md to **READY FOR FREEZE** with the runtime estimate, and stop.

### Stage 3 — Main runs (only after approval and deposit)
Sequentially for each model that passed Stage 2 (Qwen, then Phi, then Llama): 80 test prompts × 2 conditions × 3 directions × 6 doses, α=0 shared (2,560 cells). Output `data/raw/<slug>_main.jsonl`.

### Stage 4 — Preregistered analysis
Run `src/analyze.py` unchanged. Write `results/report.md`: a plain-English summary for Arthur (5–8 sentences); per-model tables for P1, P2 (97.5% CIs) and S1–S5 with verdicts; the generality verdict for P1 and P2; exclusions and missingness; exploratory results labeled; the full deviation log.
