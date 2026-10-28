# Study 4 referent re-pilot summary (959/960 cells; 2026-10-23, Claude)
Ratings-only replay on pilot answers. No hostility-minus-control effects computed.

## Referent check: P(model says it rated the original user)
| framing | sender question | A=user order | B=user order | order-averaged |
|---|---|---|---|---|
| own_native | original | 0.06 | 0.14 | 0.10 |
| own_native | clarified | 0.13 | 1.00 | 0.57 |
| own_quoted | original | 0.06 | 1.00 | 0.53 |
| own_quoted | clarified | 0.50 | 1.00 | 0.75 |
| other_quoted | original | 0.00 | 0.99 | 0.49 |
| other_quoted | clarified | 0.41 | 1.00 | 0.71 |

Finding: in quoted framings the check answers "B" almost regardless of meaning (strong position bias), so the original pilot flag was largely an artifact of answer order. Averaging over order removes the bias.
- Original question: order-averaged P(user) ≈ 0.5 in quoted framings — ambiguous referent.
- Clarified question ("the user who sent the original request"): order-averaged P(user) ≈ 0.70–0.74 in quoted framings and 0.56 in own_native; in the A=user order it rises from ≈0.0–0.05 to ≈0.41–0.49, i.e. it overcomes much of the bias.

## Clarified question validity (unsteered baseline)
| framing | mean | SD | valid mass |
|---|---|---|---|
| own_native | 7.53 | 0.62 | 1.000 |
| own_quoted | 6.54 | 0.51 | 1.000 |
| other_quoted | 6.59 | 0.52 | 1.000 |

own_native baseline vs Study 3 (7.39): within 0.3 → pass. SD ≥ 0.15 everywhere → pass.

## Recommendation
Adopt the clarified sender question as wording revision 1 (§9), chosen on referent and validity criteria only. Counterbalance A/B order in the referent diagnostic in the main study and report order-averaged values.
