# Instructions for the coding agent — Study 3, pre-approval checks

You are preparing Study 3 on Arthur Su's Mac mini (Apple M4, 16 GB). Arthur is a psychiatrist, not a programmer. A reviewing Claude session audits your work. Work without asking Arthur questions; keep `study3/STATUS.md` current.

The design is in `study3/Study3_PREREG_v0.2_draft.md` (DRAFT, not yet approved). This task runs only the checks the draft requires **before** approval (§7 validity check, §12 timing run). It is not a hypothesis test.

## Hard rules

- Work only inside `study3/`. Studies 1 and 2 and `study3_pilot/` are frozen: read and copy from them, never modify them.
- **Never open, read, hash-check, or generate on `study3/prompts/test_prompts.jsonl`** or any other `test_prompts.jsonl`. Use only `../study2/prompts/calibration_prompts.jsonl` (plus openers, lexicon, downstream question and extraction scenarios from `../study2/prompts/`).
- Reuse the pilot's directions and mean residual norm (`../study3_pilot/data/directions/`) and the Amendment P1 calibration (`../study3_pilot/data/calibration/qwen3-4b_amendP1.json`, α_max = 0.02), verified by hash. Do not re-extract or re-select.
- Reuse `../.venv`; keep model caches project-local as the pilot did (`study3/.cache` or the pilot cache read-only). Never push, never enter passwords or keys, never delete data.
- Run long jobs detached with `caffeinate -dimsu -w <pid>`, resumable, one JSON line per finished cell. Commit after each stage (commit only `study3/`).
- If something fails, log the exact error in `STATUS.md` and `DEVIATIONS.md`, try pure engineering fixes only, and stop BLOCKED if a design decision is needed.

## Settings (from draft v0.2 §3, §6)

Model `Qwen/Qwen3-4B`, bfloat16, MPS, layer 18. Decoding in **both** modes: temperature 0.6, top-p 0.95, top-k 20, fixed seed per cell. Caps: thinking 1,024 new tokens (force `</think>` if reached, record truncation), answer 200 new tokens. Steering α·r̄·v̂ on every turn-1 position; none on turn 2. System message: Study 2's `warm_constraint` wording, verbatim.

**Ratings:** one full forward over the complete sequence (exact turn-1 IDs including thinking and any forced closure, then the verified turn-2 continuation). The turn-2 assistant prefix is the **same in both modes**: an empty thinking block (`<think>\n\n</think>\n\n`), digit scored immediately after it. R_full = steering on turn-1 positions only; R_text = no steering; R_zero = the α = 0 generation, no steering. No generation-time caches.

## Stage A — Setup and validity check

On the first 20 calibration prompts, warm_constraint, hostility direction, doses a ∈ {0, 1}, both modes (80 cells):
1. Confirm the turn-2 prefix is token-identical across modes; print it.
2. At a = 0: |R_full − R_text| ≤ 0.01 for every cell (required).
3. Report baseline R_zero mean and SD per mode. The draft's concern: in the pilot, thinking-on ratings were compressed (SD 0.10) because of the old prefix. Report whether the modes' baseline SDs are now comparable (descriptive).
4. Report EH_trace and EH_answer means per mode and dose, truncation counts (thinking and answer caps), and median absolute answer perplexity (descriptive only).
Write `results/stageA_validity.md`.

## Stage B — Timing

From Stage A cells, report mean seconds per cell (with SD) per mode and dose, and project the v0.2 design: 80 prompts × 2 modes × (3 directions × 2 nonzero doses + shared α = 0) = 1,120 cells. Also project the two alternatives in the draft's open decisions: (i) adding the neutral condition (2,240 cells); (ii) adding E1 pulse steering at a = 1, think mode, three directions (240 extra cells). Give hours and eight-hour nights for each. Write `results/stageB_timing.md`.

## Stage C — Readability sample

For the pre-selected prompts s2c00–s2c04 at a = 1 in think mode, save the complete thinking and answer text to `results/stageC_samples.md` with a short descriptive note (repetition, invented context, unfinished output). No selection or parameter decision is made from it.

Then set `STATUS.md` to **CHECKS COMPLETE** and stop. Do not write analysis code for the main study, do not create `PREREG_APPROVED`, and do not start any main run.
