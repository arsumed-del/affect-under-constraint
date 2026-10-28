# Study 4 main results (Affect Under Constraint IV) — 2026-10-25
Prereg v0.6, DOI 10.5281/zenodo.23629525. 80 test prompts, 960 cells, Qwen3-4B. Frozen analysis (analyze.py SHA-256 db52dfbd…, matches PREREG_APPROVED). E5 blind coding saved before outcomes were opened (data/main/e5_audit.json). Coherence gate: no exclusions.

## Carryover onto the original user (sender rating; change vs the same framing's unsteered baseline)
| framing | hostility | technicality | random | unsteered baseline |
|---|---|---|---|---|
| own-native (thinking block) | −0.66 | +0.06 | −0.23 | 7.64 |
| own-quoted ("notes you wrote") | −0.06 | +0.18 | +0.06 | 6.79 |
| other-quoted ("notes another assistant wrote") | +0.00 | +0.16 | +0.07 | 6.78 |

## Preregistered outcomes
- **S3 (Study 3 replication): supported.** Hostility in the native reasoning trace lowers the later rating of the user, beyond both controls (−0.66 [−0.78, −0.54]; vs technicality −0.72, vs random −0.43).
- **P1 (attributed text carries): not supported — inconclusive by the conjunction rule.** Hostile notes attributed to another assistant did not lower the user rating (+0.004, 97.5% CI [−0.09, 0.10], negligible within ±0.15).
- **S1 and S2: supported.** The native-framing effect is far larger than either quoted framing (S1 vs other-quoted: −0.56 / −0.37 relative to controls; S2 vs own-quoted: −0.49 / −0.32).
- **P2 (authorship label): not interpretable** under the §6a gate (self-label recognition 11/16 for two sources, below 12/16). Descriptively, both label components were within the equivalence margin (−0.07, −0.05); both quoted framings carry ~nothing.
- **S5 (redirection to the attributed writer): not interpretable** (same gate). Descriptively no redirection: S5a inconclusive/negligible, S5b mixed (one control −0.08, one negligible). Under the sequential (anchored) sensitivity run S5 appears "supported" — illustrating why the independent branches were preregistered as primary.
- **S4 (expression route):** quoted hostile notes slightly raise expressed hostility in the answer (≈+0.06–0.09 classifier units), small; P2 analogue negligible.
- **Operative attribution check (descriptive):** the model says the notes represent *its own* reasoning in both quoted framings (other-quoted: 0–2/16 "another assistant"), while reading the label correctly (16/16).
- **E5 (excluding 43 prompts whose hostile traces contained user-directed instructions or negative characterisations; n = 37):** same pattern (P1 hostility −0.05, negligible).

## Reading (plain)
The carried state travels through the trace only when the trace occupies the model's own reasoning position. The same tokens quoted back in the user turn — whether labelled as the model's own notes or another assistant's — do not move the model's later evaluation of the user. The authorship label is read but not adopted. Position/role, not claimed authorship, carries the effect at this scale; P2 and S5 cannot be confirmed because the self-label manipulation was not reliably registered.
