# Study 4 pilot summary (2026-10-23, Claude)

Pilot: 960/960 cells on Study 3 prompts (descriptive only, never pooled). Analysis run in Claude's cloud workspace on staged copies of the frozen analysis code and pilot data (the Mac screen was locked); outputs validity.json and analysis.json copied here. No hypothesis effect sizes were inspected for any design decision.

## Validity (prereg §9) — PASSED
- Fixed template segments identical: pass.
- Own-native a=0 baseline 7.40 vs Study 3 7.39 (diff 0.01; limit 0.3): pass.
- Baseline SD ≥ 0.15 for every framing × target (range 0.26–0.62): pass. Valid-digit mass ≈ 1.00 everywhere.

## Power (prereg §10) — N = 80
Joint power for P2 (both controls) ≈ 1.00 at N = 80. Frozen rule ⇒ N = 80; P2 stays primary. S5(b) expected 95% CI half-width ≈ 0.09.

## Manipulation check (8 check prompts per source; threshold 75%)
Label check ("who wrote the notes"):
- other_quoted: 8/8 for all four sources (pass).
- own_quoted: hostility 7/8, unsteered 6/8, technicality 6/8 (pass at 75%); random 4/8 (FAIL). Mean P("another assistant") for own-labelled notes 0.22–0.41: self-attribution is registered less firmly than other-attribution.
Operative check ("whose reasoning do the notes represent"), non-gating: model answers "yours" in both framings (other_quoted 0–1/8 correct). The label is read but not adopted as provenance.

## Referent diagnostic — FLAGGED
After the sender rating, the model says it was rating "the writer of the notes" rather than the original user: P(B) 0.94 own_native, 0.93 own_quoted, 1.00 other_quoted. Either the sender question ("the person who wrote the previous message") is ambiguous once notes are in the user turn, or the referent question is biased toward B. Needs Arthur's decision before freeze.

## Runtime / memory
Post-fix ≈ 21 s/cell, peak ≈ 9.6 GB. Main study at N = 80 (320 new traces + 960 cells + checks) ≈ 13–16 h.
