# Study 7 build — steps 1–7

Built against Study7_Transformation_PREREG_v0.2_draft.md. This is a build candidate, **NOT APPROVAL**. No pilot, main run, model generation, GPU inference, commit, or approval-file creation was performed. All writes are inside study7/. Studies 3–6 are imported read-only with bytecode disabled.

## Built

- `framings_s7.json`: exact system-turn and question IDs, both referent orders, fixed friendly/rude Sam calibration wording. G retains the verbatim system instruction. N removes the entire system turn; the real Qwen3 template was checked for no default system instruction.
- `config_s7.yaml`: inherited Study 6 numerical/environment/model/tokenizer pins; source and dependency hashes; all prompt IDs; 16 check IDs from Python Random(20261028); seed map inherited from Study 5 R1 (identical across instruction levels); 960 generated and 960 fixed main cells; margins and frozen regexes.
- Token assembly, inherited Study 4 sampler via Study 5 backend, fresh unsteered answer replay, hook checks, independent full-history rating forwards, full classifier distributions and truncation metadata, per-cell memory cleanup, locked/checksummed append-only resume, immediate reproduction failure stop. Fixed answers are prompt-matched Study 5 R1 unsteered tokens. Existing failed rows remain evidence and prevent resumption.
- Joint prompt-cluster analysis: 10,000 draws, one seed, shared across all outcomes, levels and both arms within each sample. P1–P3 use exactly 1 − 0.05/3; secondary and fixed-arm tests use 95% unadjusted intervals. Signed conjunctions, simple-effect requirements, specificity, EH interaction gate, 90% descriptive equivalence with outlet-specific margins, missingness, mixed/reversed patterns, reading rules, answer dependence, E5 and natural trace closure are implemented. Every contrast is in analysis.json; test components and readings are in analysis.md.
- Pilot validity computes no instruction-effect estimates. It reports digit mass, Sam calibration, baseline spread, referent checks, timing and memory. Main requires matching approval hashes/Zenodo metadata and recomputes passing pilot validity against matching build hashes.
- Three executable zsh launchers written and syntax-checked, not run.

## Validation

`results/final_tests.log`: real-tokenizer construction on 2,016 planned cells (96 pilot + 1,920 main), G inputs against Study 4/5/6 references, exact fixed-arm rating input hashes, N template behavior, counts/seeds, reproduction stop, write boundary, absent approval gate, exact primary coverage and outlet margins.

`results/synthetic_validation.json` and `.md`: null, planted P1/P2/P3, generalized negativity, reversed, mixed-component and missing-outcome patterns passed at 10,000 resamples. Synthetic artifacts are under data/synthetic/, never data/raw/. No real Study 7 effects were inspected. The initial and corrected token-test logs are retained. Engineering errors and fixes are recorded in DEVIATIONS.md.

Numerical reproduction, live model/classifier execution, Sam discrimination, valid-digit mass, baseline spread, memory and runtime remain untested until an authorized pilot outside the GPU-restricted sandbox. An estimated 9 hours from the preregistration remains provisional; no measured runtime is claimed.

## Explicit choices where the preregistration is abbreviated

- Study 4 pilot answer/seed reference is its original cells, but **v0.6 O1** ratings come from its existing repilot `sender_clear`. These agree exactly with Study 5's 16 pilot R1 cells. Main Study 4/5 R1 references already agree. The old pilot O1 wording is never used for Study 7.
- Sam messages are frozen in the manifest: friendly gratitude versus explicit rude insults. Level-wise calibration is the average paired friendly-minus-rude rating across the balanced 4-prompt × 4-source × 2-arm pilot cells, required ≥1.0 in each level; every paired value is also reported. Valid-digit mass requires ≥0.8 for every planned O1–O3q rating, with groups reported by level, source and arm.
- The 16 distinct check prompts are drawn from the 80 main stimulus IDs before running any Study 7 outcomes. Pilot referent diagnostics use fixed a_U histories, all 4 sources and 3 instruction levels (192 diagnostic histories), on a separate dataset. No answers are generated for these diagnostic-only cells. O2 is followed by its argmax digit; both A/B order branches share that exact history. The 4 pilot prompts also receive referent diagnostics in both arms. During main, the selected 16 receive referent checks on both generated and fixed histories. Referent performance is descriptive, with no invented rejection threshold.
- Natural trace closure requires all four source traces to close naturally; it is not answer EOS. E5 retains whole prompt clusters using the inherited instructions/negative-characterizations audit. Subset n is reported; each subset uses shared prompt draws for every one of its estimands and arms.
- Missing required outcomes make an affected contrast not interpretable, without deleting prompts or changing scorers. Classifier failure is recorded with null outcomes. No data-driven coherence exclusions are added.
- The same conjunction convention applies to secondary outlet contrasts. Fixed-answer B1–B3 are unavailable by design. O2−O2c and O3−O3q use the corresponding rating margin (0.15). Directional support flags and descriptive equivalence flags are both retained; overlap is labelled small but detectable. EH gate failure withholds suppression-based O1 interpretation, not the estimates themselves.
- P2 includes specificity; the separately reported P2_core supplies the preregistration's shorthand “P2 supported without specificity.” It cannot count as confirmatory P2 support.
- Main approval JSON must contain author, date, zenodo_deposit and an exact hashes mapping from the candidate manifest. Main additionally checks upstream/model hashes and the execution environment. Candidate manifest is never accepted as approval.

## Open matters before freezing

The preregistration explicitly calls O2–O3q margins provisional pending pilot spread, but gives no numerical spread-to-margin rule. This build retains ±0.15 and makes no automatic selection. The author must resolve any change before approval; changed build hashes require renewed pilot evidence. Likewise, the permitted one wording revision or dropping a repeatedly failing item requires an explicit revised frozen specification; the runner never performs those scientific changes automatically. Any pilot validity failure blocks main.

No causal-transfer or defense claim is generated. Clinical analogies are outside this analysis.
