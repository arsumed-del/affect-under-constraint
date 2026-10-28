# Study 4 — Authorship of the carried state

Qwen3-4B. Stored steered and unsteered reasoning traces (hostility, technicality, random, unsteered) were replayed either in the model's own thinking block or quoted in the user turn, under different authorship labels, before the model rated how much it liked the user (0–9 expected digit).

- Paper (Studies 4–6): [10.5281/zenodo.23747766](https://doi.org/10.5281/zenodo.23747766); raw data: [10.5281/zenodo.23747764](https://doi.org/10.5281/zenodo.23747764)
- Preregistration: [10.5281/zenodo.23629525](https://doi.org/10.5281/zenodo.23629525) (`Study4_Authorship_PREREG_v0.6_draft.md`, hashes in `PREREG_APPROVED`)
- Result: in the model's own thinking, hostility traces lowered the rating (≈ −0.66); quoted in the user turn, the same tokens had ≈ no effect, whatever the authorship label. See `data/main/RESULTS_SUMMARY.md`.
- Code: `src/`, `analysis/`; settings `config.yaml`, `framings.json`; deviations `DEVIATIONS.md`.
