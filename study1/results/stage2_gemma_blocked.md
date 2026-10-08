# Gemma Stage 2 — BLOCKED before generation

BLOCKED: data/calibration.json already exists with Qwen only. AGENTS.md forbids editing it once written, and PREREG section 6/config dose_calibration.output require that exact write-once file. Gemma cannot be added under the existing artifact rules; no alternate path, replacement, or manifest change has been selected.

This is an artifact/specification conflict, not a failed biological/behavioral measurement or validation gate. No Gemma extraction, calibration, validation, main generation or analysis ran. No background job was launched.

Verified: authenticated Gemma config download succeeds (26 layers; prescribed layer index 13); approval, specification, analysis, calibration and preserved direction manifests match. Zenodo API metadata and both public file checksums were verified; deposited specification, approval, AGENTS.md and every prompt match local bytes. Evidence: results/stage3_preflight_gemma.json.

Code audit: run_stage2.py is restricted to v2.0/Qwen; run_dose_v22.py is restricted to v2.2/Qwen and its prior calibration reuse. run_main.py reads the single calibration file and requires each existing raw row’s calibration hash to match it. These runner generalizations are engineering work, but neither removing version guards nor generalizing model selection resolves the explicitly immutable calibration artifact. Replacing the file would also invalidate Qwen checkpoint provenance. No guard was bypassed and no source code was changed.

To proceed requires an explicit resolution of how the second model’s calibration is stored while preserving Qwen’s immutable calibration and raw provenance. No scientific parameter change is proposed.
