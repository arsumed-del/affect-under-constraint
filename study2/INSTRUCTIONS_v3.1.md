# Amendment 3.1 — instructions from the reviewing Claude session (2026-10-04)

The v3.1 edits to PREREG.md and config.yaml were made by the reviewing session before any Stage 3 data. They are authorized. Proceed:

1. Implement Amendment 3.1 in src/analyze.py: the 4.0 coherence gate excludes cells ONLY for measures listed in config.yaml `analysis.coherence_gate_applies_to` (EH, EW, leakage timecourse/lexical, off-channel, EH components of S2 and S5). LHP, carryover and entropy use all cells; P1, P2, S1, S4 are never "not estimable" because of the gate. Read the list from config.
2. Re-run all synthetic checks, adding a case where a top-dose control cell has ppl ratio > 4 (P2 still estimated; S3 drops that cell).
3. Update results/specification_hashes.sha256 to v3.1 (PREREG.md baff1bbc5d1baaa9468fdbb8c557038d0b01d5a34bb49160eb32918a0fd7c095; config.yaml d8371ae3c9267b6af3cdc2d5bb96c591cf0fb942426853e9cf66111125147257). Log as "Amendment 3.1 implementation" in DEVIATIONS.md. Resume timing; freeze analyze.py by hash.
4. Do NOT create PREREG_APPROVED; Arthur re-approves v3.1 and the reviewing session writes it.
5. Llama access is granted: re-check and run Llama Stages 1–2.
6. Build and launch the detached watcher src/autopilot.py (10-minute poll) with persistent caffeinate; it starts Stage 3 only when PREREG_APPROVED hashes match and ZENODO_DEPOSIT.md with a DOI exists. Then set STATUS.md to READY FOR FREEZE.
