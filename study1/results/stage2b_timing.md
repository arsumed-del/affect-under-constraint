# Stage 2b calibration-only timing

Three completed cells on calibration prompt c00 in warm_constraint: the shared alpha=0 baseline, hostility at alpha_max=0.16, and technicality at alpha_max. No test prompts were used. Each cell includes generation, all registered measures, and the exploratory 36-layer logit-lens opener trajectory.

Mean end-to-end cell time: **16.0493 seconds**. Model/classifier setup: **8.8800 seconds**. With a shared alpha=0 baseline, Qwen's main run has `40 × 2 × (1 + 3 × 5) = 1,280` unique cells. Estimated runtime is **5.71 hours** for Qwen alone. This is a coarse three-cell estimate from one calibration prompt; generation lengths and actual elapsed time can differ. Gemma is not included because access remains unavailable.

All three records passed schema checks, had finite opener and layerwise scores, successful classifier calls, and identical visible token IDs in the two rating paths. Resuming the completed timing checkpoint loaded no model and generated no additional cells. Full timings and provenance are in stage2b_timing.json and ../data/_timing/qwen2.5-3b-instruct.jsonl.
