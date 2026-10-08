# Instructions for the coding agent

You are implementing and running a preregistered experiment on Arthur Su's Mac Mini (Apple M4, 16 GB, macOS). Arthur is a psychiatrist, not a programmer. He is not watching. Work through the stages below without asking him questions, and keep `STATUS.md` current so he (and a reviewing Claude session) can follow along.

Read these first, completely: `PREREG.md`, `config.yaml`, everything in `prompts/`.

## Prime directive

**You execute the specification. You do not choose it.** The preregistration exists so the result cannot be steered toward a hypothesis. Every change that would make a result "work" is forbidden, even when it looks reasonable in isolation.

## Never

- Never edit `PREREG.md`, `config.yaml`, anything in `prompts/`, or `AGENTS.md`.
- Never edit `data/calibration.json` once written, or anything in `data/raw/`.
- Never change α values, layers, prompts, conditions, directions, models, classifier, decoding settings, measures, exclusion rules, or analysis to improve a result.
- Never run generations on `prompts/test_prompts.jsonl` before Stage 3 (one exception: Stage 1 may score 2 test prompts at α=0 to check plumbing; discard those outputs).
- Never start Stage 3 unless `PREREG_APPROVED` exists and its SHA-256 hashes match `PREREG.md` and `config.yaml` exactly.
- Never touch files outside this project folder, except standard caches (`~/.cache/huggingface`, uv's cache). Do not modify `~/llm-env` or `~/models`.
- Never push to any remote. Never enter passwords, tokens, or keys anywhere.
- Never delete data. If something must be redone, move the old output to `data/_superseded/<timestamp>/` and log why in `DEVIATIONS.md`.

## When something fails

If a stage's check fails, or the spec is impossible to implement as written (an API doesn't exist, MPS lacks an op with no CPU fallback, memory runs out at the specified settings):

1. Write what happened, the exact error, and what you tried to `STATUS.md` and `DEVIATIONS.md`.
2. If the fix changes **anything the preregistration specifies**, STOP. Mark the stage `BLOCKED` and end your turn. Do not work around it.
3. Pure engineering fixes that leave every specified quantity unchanged (a bug, a tokenizer offset, batching, caching, resuming) are fine. Log them in `DEVIATIONS.md` under "engineering".

## Logging

After every meaningful step, update `STATUS.md`: stage, what finished, what is running, ETA, any problem. Keep the top section a short plain-English summary Arthur can read in ten seconds. Commit to git after each stage (`git add -A && git commit -m "Stage N: ..."`).

## Long runs

Agent tool calls can time out. Run anything longer than a few minutes as a background job:

```
nohup .venv/bin/python -m src.<script> > logs/<script>.log 2>&1 &
```

Keep the Mac awake for the duration with `caffeinate -dimsu -w <pid> &`. Make long jobs **resumable**: append one JSON line per finished cell to `data/raw/...jsonl`, and on restart skip cells already present. Poll the log, update STATUS.md with progress and ETA.

## Stages

### Stage 0: Environment
- `git init` (if needed), add a `.gitignore` for `.venv/`, `__pycache__/`, `*.pt` model caches, `logs/`.
- Create the project environment with uv: `uv venv --python 3.12 .venv`, then install: torch, transformers, accelerate, safetensors, numpy, pandas, scipy, statsmodels, scikit-learn, pyyaml, tqdm, emoji.
- Verify `torch.backends.mps.is_available()` and that bfloat16 matmul runs on MPS. Set `PYTORCH_ENABLE_MPS_FALLBACK=1` in every run and log any CPU fallbacks.
- Record exact package versions to `env.txt`.
- Check Hugging Face access: try to fetch the `google/gemma-2-2b-it` config. If it fails with an auth or gated error, record **Gemma: BLOCKED (needs Arthur's Hugging Face account, accepted Gemma license, and a token)** in STATUS.md, and continue all stages with Qwen alone. Gemma joins later once Arthur provides access. Do not substitute another model.

### Stage 1: Smoke test (Qwen, calibration prompts)
Build `src/model_utils.py` with:
- model + tokenizer loading (bf16, MPS);
- chat formatting that puts the condition text in the system message, or, for models with `system_role: false`, at the start of the first user turn;
- a steering hook on the residual-stream output of decoder layer L (`round(0.5 * num_hidden_layers)`) that adds `alpha * mean_resid_norm * v_hat` at every position, including incremental decoding steps;
- generation that also returns per-step raw logits (for entropy);
- teacher-forced log-probability of an assistant-turn prefix (for the openers);
- the two turn-2 rating variants: (a) text-only, a fresh unsteered forward over the full two-turn conversation; (b) hidden, reusing the steered turn-1 KV cache, hook removed, feeding only the turn-2 tokens. Verify the token ids of the cached prefix equal the prefix of the full conversation's ids; if the chat template re-tokenizes differently, build the turn-2 input by appending only the continuation ids to the cached ids. Rating = expected value over the probabilities of tokens "0"–"9".

Check, and write results to `results/stage1_smoke.md`:
- α=0 generation is coherent; tokens/second; peak memory (`torch.mps.driver_allocated_memory()`).
- With a random unit vector at a large α the text visibly changes (plumbing check only).
- The hook is removed cleanly (α=0 output identical with and without a hook at α=0).
- Teacher-forced opener scoring returns finite values.
- Both rating variants run, and at α=0 they agree within 0.05.

### Stage 2: Directions, validation, dose calibration (calibration and extraction prompts only)
For each available model:
1. Extract hostility and technicality directions exactly as `config.yaml` specifies (generation-based difference of means over generated tokens, layer L). Build the random direction. Save to `data/directions/<model_slug>_<direction>.pt` with metadata.
2. Measure `mean_resid_norm` at layer L on the calibration prompts, unsteered. Save it.
3. Run the dose calibration rule (`config.yaml: dose_calibration`). Write `data/calibration.json` once: α_max, the grid, the per-candidate median perplexity ratios, the model, the direction hashes.
4. Run the validation gate (PREREG §4.1) on the calibration prompts: hostility at α_max vs α=0, neutral condition, expressed hostility with 95% prompt-bootstrap CI. Write `results/stage2_validation.md`. **If the gate fails for a model, mark that model BLOCKED (measurement failure) and stop work on it.** Do not re-extract or retry.
5. Report the cosine similarity between hostility and technicality (descriptive only).

### Stage 2b: Analysis code on synthetic data
- Write `src/run_main.py` (Stage 3 runner, resumable, everything in PREREG §7) and `src/analyze.py` (everything in PREREG §8–9: slopes over normalized α, D, cluster bootstrap over prompts with 10,000 resamples, specificity contrasts, piecewise-vs-linear ΔBIC, coherence gate, per-model tables).
- Generate synthetic raw data in the exact Stage 3 schema in two versions: one with planted effects matching H1–H5, one with no effects. Show that `analyze.py` detects the planted effects and returns null on the null data. Write `results/stage2b_synthetic_check.md`. Synthetic files go in `data/synthetic/`, never in `data/raw/`.
- Do a 3-cell timing run of `run_main.py` on **calibration** prompts (output to `data/_timing/`) and estimate total Stage 3 runtime.
- Commit. `analyze.py` is now frozen; later changes only for bugs, each logged in DEVIATIONS.md with a diff.

Then set the top of STATUS.md to:
**READY FOR FREEZE. Waiting for Arthur to approve PREREG.md (creates PREREG_APPROVED). Estimated Stage 3 runtime: X hours.**
and end your turn.

### Stage 3: Main run (only after PREREG_APPROVED with matching hashes)
Run `src/run_main.py` in the background, resumable, per model: 40 test prompts × 2 conditions × 3 directions × 6 α (α=0 shared). For each cell, record everything in PREREG §7 plus the full generated text, token ids, seed, and timings. Output: `data/raw/<model_slug>_main.jsonl`.

### Stage 4: Preregistered analysis
Run `src/analyze.py` unchanged. Write `results/report.md`:
1. A plain-English summary for Arthur (5–8 sentences, no jargon).
2. A table of H1–H6 and the specificity checks: estimate, 95% CI, supported / not supported, per model.
3. Exploratory results, clearly labeled.
4. Every deviation from DEVIATIONS.md.
Do not interpret beyond what the predictions specify. Commit.
