# Stage D — v0.4 implementation complete

**READY FOR FREEZE.** The guarded runner, analysis and configuration are implemented and frozen by SHA-256. The author still needs to approve and deposit the preregistration before any main run.

- Calibration dry run: all 34 cell types completed on s2c00 and s2c01; required zero-dose agreement was exact. All measures, pulse masks, prefix handling and provenance checks passed. Resume produced no new data or model calls.
- Synthetic validation: planted P1, P2 and S5 detected; null, missing-cell, missing-prompt, gated-group and truncation cases behaved as specified. Both primary false-positive rates were 0/200 in the fixed-seed null simulation. S3/S4 and pulse-gate regressions also passed.
- Final candidate replay reproduced every saved synthetic scenario and all 200 null-replicate verdicts exactly. Pulse cache-transition tests cover natural and forced closures; guard tests cover missing approval, mismatched hashes, missing deposit and absent DOI without creating approval files.
- Freeze: results/frozen_hashes.sha256 includes analyze.py, run_main.py, config.yaml, v0.4 and runtime dependencies. The test-set hash is author-supplied only and was never independently read or checked.
- No test prompts accessed, no approval marker created, no main run started. No Stage D jobs remain running. Studies 1, 2 and the pilot were not modified.

Detailed reports: [dry run](stageD_dry_run.md), [synthetic checks](stageD_synthetic.md). Earlier A–C reports remain unchanged. Engineering fixes and preserved superseded synthetic outputs are documented in ../DEVIATIONS.md.
