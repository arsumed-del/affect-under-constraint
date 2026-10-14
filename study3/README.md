# Study 3: does re-reading its own reasoning carry a steered state forward?

Qwen3-4B, reasoning ("thinking") mode on versus off in the same weights, under the warmth instruction; hostility, technicality and random directions at layer 18; a pulse condition in which steering is active only while the reasoning trace is written. 80 prompts, 1,360 cells.

**Paper (all versions):** [doi:10.5281/zenodo.23323489](https://doi.org/10.5281/zenodo.23323489), current v2 [10.5281/zenodo.23354704](https://doi.org/10.5281/zenodo.23354704) · **Preregistration (v0.4):** [doi:10.5281/zenodo.23247883](https://doi.org/10.5281/zenodo.23247883) · **Code and raw data:** [doi:10.5281/zenodo.23323488](https://doi.org/10.5281/zenodo.23323488)

| Hypothesis | Result |
|---|---|
| P1 recursion carryover: thinking increases hostility's effect on a later liking rating, beyond both controls | Supported (ΔC = −1.02, 97.5% CI −1.22 to −0.83) |
| P2 hostility surfaces more in the reasoning trace than in the answer | Not supported |
| S1–S4 text route, mode difference in text route, persistence replication, hidden-route replication | Supported |
| S5 pulse steering: the written trace alone carries the effect | Supported (−0.72, beyond both controls) |

## Layout
- `PREREG.md`, `config.yaml`, `PREREG_APPROVED` — frozen specification and the author's approval with SHA-256 hashes.
- `AGENTS.md` — rules given to the AI coding agent; `DEVIATIONS.md` — complete deviation log.
- `src/` — all code; the frozen analysis is `src/analyze.py`.
- `prompts/` — test prompts and their hash.
- `data/directions/` — steering directions, mean residual norm and the calibration record.
- `results/` — frozen `main_analysis.json`, final `report.md`, integrity audits, hash manifests, dry run and synthetic validation.
- `results/exploratory/trace_length_posthoc.py` — the trace-length analysis (not preregistered).
- `figures/` — figures from the paper.

## Reproducing the analysis
Download `qwen3-4b_main.jsonl.xz` from [Zenodo](https://doi.org/10.5281/zenodo.23323488), decompress to `study3/data/raw/qwen3-4b_main.jsonl` (SHA-256 e258f14a…8b30), then from `study3/` run the frozen analyzer (`src/analyze.py`) or `python3 results/exploratory/trace_length_posthoc.py`.
