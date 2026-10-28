# Study 6 build log and deviations

No preregistration changes, pilot/main inference, approvals, commits, or writes outside study6/ were performed by this build.

## Engineering — 2026-10-27
- Reuse inherited assembly, hook checks, full-sequence forward and rating routines through read-only imports. The Study 6 backend omits the unused classifier and prohibits generation/cache reuse. Package bytecode is disabled to prevent writes in inherited directories.
- The first CPU suite passed 10 tests. Before finalizing, subset bootstrap implementation was reviewed and changed from filtering an 80-prompt draw (variable retained sample size) to fixed-size resampling of each eligible subset using shared master uniform draws. This preserves the standard prompt-cluster bootstrap and exact shared draws for common masks; no experimental outcomes were used.
- Preserve initial test log and any superseded synthetic artifacts; final tests add approval, hook, separate-process and heterogeneous-bootstrap checks.

- Preserved first synthetic artifacts and 13-test log in data/_superseded/20261027T210737Z before regenerating reports with explicit exploratory-interaction labels and the additional heterogeneous bootstrap test. No experimental data exist.
