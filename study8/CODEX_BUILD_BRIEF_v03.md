# Codex build brief — Study 8 v0.3 judge update
Spec: study8/Study8_ReactionFormation_PREREG_v0.3_draft.md (§3 and §3a changed; everything else as v0.2). Author approved v0.3 on 2026-10-30. Reference implementation of the scoring: study8/judges/judge_probe.py (results in study8/results/judge_probe_v03.json). Write only inside study8/. No commits, no PREREG_APPROVED, no model runs.

1. Update config_s8.yaml preregistration path/hash to v0.3; record the judge method (single item per call, expected digit score, digit-mass floor 0.5), items scored by each judge (gemma: a–h; llama: a, e), and the v0.3 gate thresholds.
2. Rewrite study8/src/judge.py scoring to the v0.3 procedure, reusing judge_probe.py's prompt template, item anchors (extend to b, c, d, f, g, h using judges/rubric.md anchors, same template style) and digit-id logic (including the "▁k" sentencepiece form). Keep blinding, shuffled neutral IDs, provenance, raw per-digit probabilities and digit mass per item, resumability, sequential processes. Remove JSON parsing/retry from the active path.
3. Update study8/src/validity.py judge gate and agreement statistics to v0.3 (§3), and analysis to read continuous W scores with digit-mass missingness.
4. Add study8/run_pilot_judges.command: rerun ONLY the pilot judge stage (export, gemma, llama) and validity on the existing pilot Qwen data, writing new judge files (move the v0.2 judge outputs to data/pilot/judge_v02/ — do not delete). zsh, live tee to study8/logs/pilot_judges_v03.log. Write but do not run.
5. Update tests (parser tests → expected-score tests with fake logits; gate tests) and synthetic validation; run them. Update BUILD_NOTES.md, DEVIATIONS.md, results/freeze_manifest_candidate.json (NOT APPROVAL).
Stop after 5.
