# Study 5 build decisions and unresolved specifications

## Engineering
- Build only, per CODEX_BUILD_BRIEF and the user's explicit step-7 stop. All writes confined to study5/. No commits, approval file, model generation, pilot, or main run.
- Study 4 Assembly/Backend and bootstrap are reused through read-only imports. Backend initialization omits direction loading, and trace generation is explicitly disabled. Input code hashes are pinned.
- R2/R3 recipes preserve identical whitespace and differ only by moving the prior closing thinking delimiter across TRACE. In R2 the trace starts directly after that delimiter. All five prefixes and rating continuations were tested with the real tokenizer. This is a draft serialization choice required by step 1, not an outcome-selected revision.
- Required missing cells make the affected component not estimable (Study 4 fail-closed convention); duplicates and corrupt rows fail. No coherence or diagnostic exclusion gate was added to Study 5.
- Pilot references use Study 4's v0.6 repilot sender_clear readouts on the same saved pilot answers, because the original pilot sender question predates v0.6.

## Unresolved before pilot/freeze
- The v0.2 specification names “the 4 Study 3 pilot prompts.” Study 4's pilot prompt, trace, cell and v0.6 repilot files cover 80 prompts; no four-prompt list is provided in the Study 5 draft/brief. No subset was invented. config_s5.yaml records pilot_prompt_ids: null. The pilot runner stops before model loading until the author specifies the four IDs. The main build and CPU validation are complete; experimental execution is not ready.
- The draft does not define whether pilot baseline agreement within 0.3 applies to the mean or every paired cell. The draft implementation reports both and gates on the absolute paired mean difference; this convention needs author review before freeze.
- Per-condition dropping after a second validity failure is not automated. The build fails closed on any failed pilot criterion; a documented pre-freeze author disposition and corresponding implementation update are required if a condition must be dropped. Nothing silently changes the five-condition main design.

## 2026-10-25 8:25 p.m. — pilot details approved by Arthur Su
Pilot prompt IDs: s3t00, s3t01, s3t02 (first three provocative) and s3t60 (first neutral) in Study 3 list order, chosen by order only. Pilot agreement rule: absolute mean unsteered-baseline difference ≤ 0.3 vs the corresponding Study 4 v0.6 repilot values (per-prompt values reported). Codex's serialization and diagnostic conventions in BUILD_NOTES.md accepted.

## 2026-10-26 — pilot disposition by Arthur Su (before freeze, before main data)
Pilot: valid mass ≈1.00 everywhere; R1/R4 reference mean differences 0.00. Unsteered-baseline SD < 0.15 for R1-M (0.13), R2 (0.09), R4 (0.13). Accepted without template revision (one-revision allowance unused): readout not compressed (baselines ≈7.9/9; steered cells move), and a 4-prompt SD is imprecise. All five conditions retained; main-run 80-prompt baseline SDs reported per condition. Implemented as config `pilot_disposition` + runner gate that admits only SD-only shortfalls for the listed conditions. Prereg updated to v0.3 with this disposition. No effect estimates used.
