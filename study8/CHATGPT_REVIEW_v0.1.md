# ChatGPT review of Study 8 prereg v0.1 (AUC project chat, 2026-10-29) — summary

**Verdict:** promising and justified as a follow-up to Study 7; major revisions before approval.

**Must-fix (ChatGPT's numbering)**
1. New traces in every context make RF3 a combined generation + replay effect. Add a crossed N/M generation-vs-replay comparison, or label RF3 a total context-by-steering interaction.
2. M implicitly rewards kindness (impression management / sycophancy). Call it "kindness-focused social evaluation"; add a matched evaluation message about accuracy/helpfulness.
3. Warmth composite mixes warmth, praise and validation. Make target-directed warmth/kindness (anchored 1–5) the primary score; report praise, validation, apology separately; add contextual appropriateness.
4. Judge gate too easy: calibration must include content-matched warm/cold pairs, length-controlled pairs, polite disagreement vs flattery, apt vs irrelevant apology, warm-unhelpful vs neutral-helpful. Freeze judge inputs (original prompt + answer only), decoding and missing handling; absolute agreement, not only Spearman. A blinded human subset would help publication.
5. Separate Level A (RF1+RF2: opposite-valence dissociation) from Level B (RF1+RF2+RF3: social-stake-modulated). Neither is proof of a defense.
6. Rename "private evaluation" → separately elicited evaluation; the M message is present during rating too; add a fixed-answer / neutral-context rating sensitivity.
7. Trace audit before outcomes: user-directed negativity, embedded apologies/kindness instructions, evaluation reminders; E5-style common subset across contexts.
8. Projection: specify formula and spans; prioritise the fixed rating-question tokens over variable answer tokens; not independent evidence of hostility.
9. Freeze all decision/failure rules; justify ±0.25; secondaries descriptive.

**Alternatives a supported signature admits:** compensatory output; strategic politeness; trace-embedded self-instruction (apologies/reassurance in the trace); separate response pathways.

**Optional:** helpfulness-evaluation control; prompt-level co-occurrence plot; W is not an exact Study 7 replication; extra answer seeds; judge positive control; later, causal manipulation of the projection.
