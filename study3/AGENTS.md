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

---

## Stage D — Main-run code and analysis code (added 2026-10-08 10:05 PT, author-approved)

Do this after Stage C passes. The specification is now `study3/Study3_PREREG_v0.3_draft.md` (v0.3 supersedes v0.2: top dose α_top = 0.0175, grid a ∈ {0, 1/2, 1}, warmth only, pulse steering is secondary hypothesis S5). Still no test-prompt access.

1. **`study3/config.yaml`** — machine-readable copy of every setting in v0.3 §3–§7 and §9: model, layer, direction and norm file hashes, α_top = 0.0175 and the grid, decoding, caps, forced closure, turn-2 prefix, system message, gates, bootstrap settings, seeds. For the test set, record only the path `prompts/test_prompts.jsonl` and the author-supplied hash `2890b24bf683ffc5f3704eeebb2e246b383c44e5cdb5e0605b1f174ac908be97` (do not open the file to verify it).
2. **`src/run_main.py`** (resumable, one JSON line per cell): 80 prompts × 2 modes × (3 directions × a ∈ {1/2, 1} + shared a = 0) = 1,120 cells, plus 240 pulse cells (think mode, a = 1, three directions; steering on prompt + thinking positions only, off for the answer). Each cell stores: all token IDs, thinking/answer text, truncation flags, EH_trace (120-token windows, averaged), EH_answer, LHP, entropy, absolute perplexity of answer and trace, R_full, R_text, and (for a = 0) R_zero, all from single full forwards as in Stages A–C. A `--dry-run` flag runs 2 calibration prompts through every cell type; run the dry run and report it. **Do not run on test prompts.** The real run will start only after `PREREG_APPROVED` exists and matches the hashes of the prereg and `config.yaml`, and `ZENODO_DEPOSIT.md` exists; build that guard into `run_main.py`.
3. **`src/analyze.py`** implementing v0.3 §8.1–§8.2 and §9 exactly: P1 (ΔC with 97.5% CIs and both control contrasts), P2 (trace-minus-answer slope difference, 97.5%, both control contrasts), S1–S5 (95%), prompt-level cluster bootstrap with 10,000 resamples, percentile intervals; the coherence gate (absolute perplexity > 6.0 excluded for text-scored measures only; trace gated on its own perplexity); "not estimable" for missing required cells; exploratory E1–E4 clearly labeled; a per-hypothesis verdict table.
4. **Synthetic validation** (no model calls): simulate data with the real cell structure and (a) a planted P1 effect, (b) a planted P2 effect, (c) a planted S5 effect, (d) all-null data, (e) a truncation-heavy think mode, (f) a missing required cell. Show that planted effects are detected, (f) returns "not estimable", and the false-positive rate on (d) over at least 200 null replicates (1,000 bootstrap resamples each is fine for this check) is at or below the nominal level for each primary. Write `results/stageD_synthetic.md`.
5. Freeze `analyze.py`, `run_main.py` and `config.yaml` by SHA-256 in `results/frozen_hashes.sha256`. Set `STATUS.md` to **READY FOR FREEZE** and stop. Do not create `PREREG_APPROVED` and do not start the main run.

---

## Stage D resolution (2026-10-08 10:55 PT, author-delegated decisions by the reviewing session)

The four gaps in `results/stageD_blocked.md` are closed in **`study3/Study3_PREREG_v0.4_draft.md`**, which supersedes v0.3 for Stage D. Summary:

1. **Pulse (§6, S5):** generate prompt + thinking steered through the closing `</think>` (natural or forced); discard the generation cache; re-encode the complete prefix (prompt, thinking, closing tokens, answer separator) in one unsteered forward; generate the answer unsteered from that cache (first answer logits from the unsteered re-encoding). R_text(pulse) = unsteered full forward; R_full(pulse) = steering on prompt + thinking positions only. Pulse LHP scored unsteered after the re-encoded prefix (exploratory). **S5 is now text-route carryover:** X_pulse = R_text(pulse) − R_zero(think) < 0 for hostility and more negative than each control; C_pulse and H_pulse exploratory.
2. **Gate (§9):** grouping unit = mode × route × direction × dose, median over prompts; answer and trace gated separately on their own perplexity; text-scored measures only. P2 needs all three doses for both segments in think mode for each direction; a gated-out required group → that statistic is not estimable.
3. **E3:** common prompt subset where every think-mode trace the statistic requires closed naturally (P1: three directions at a = 1; P2: three directions at a ∈ {1/2, 1}); keep direct cells and zero-dose baselines for those prompts; fewer than 20 prompts → not estimable; always report counts.
4. **E4:** test prompts s3t00–s3t04 by ID, think mode, hostility, a = 1, regular and pulse routes, reported after the main run (no test-prompt access before then); Stage C samples reported alongside.

Proceed with Stage D items 1–5 against v0.4 and stop at READY FOR FREEZE. Include a planted S5 effect in the synthetic validation under the new X_pulse definition, and a synthetic case where a P2 dose group is gated out (must return not estimable). If anything else is underdetermined, list it all in one report and stop BLOCKED as before.

---

## Stage E — Main run and preregistered analysis (approved 2026-10-08 13:11 PT; deposited 10.5281/zenodo.23247883)

`PREREG_APPROVED` and `ZENODO_DEPOSIT.md` now exist. Commit them (and `DEPOSIT_NOTE.md`, `zenodo_deposit/`) first. Then:

1. Run `src/run_main.py` unchanged on the test set (1,360 cells), detached with `caffeinate -dimsu -w <pid>`, resumable. The approval guard must pass before the test file is opened; if it fails, stop BLOCKED and report the exact message. Keep STATUS.md updated with cell counts and ETA at least hourly. Commit raw data periodically.
2. Never change any frozen file (`results/frozen_hashes.sha256`). Pure engineering problems (crash, out-of-memory, restart) may be fixed only in ways that leave every frozen file and specified quantity unchanged; log them in DEVIATIONS.md. If a fix would require changing a frozen file, stop BLOCKED.
3. When all 1,360 cells exist and pass integrity checks, run `src/analyze.py` unchanged and write `results/report.md`: a 5–8 sentence plain-English summary for Arthur; the verdict table for P1, P2 (97.5%) and S1–S5 (95%); exclusions, gating and missingness; exploratory E1–E4 clearly labeled; the full deviation log. Set STATUS.md to **STUDY 3 COMPLETE** and stop.
