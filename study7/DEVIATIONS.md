# Study 7 deviations

## Engineering — build tokenizer check
Initial no-system assertion raised `AssertionError`: the pinned transformers version returns BatchEncoding from apply_chat_template, not a list. Inspected template text and IDs; selected input_ids explicitly. No stimulus or token recipe changed.

## Engineering — v0.6 pilot reference
Real-row preflight stopped with `RuntimeError: Study 4/5 reference rating disagreement`. Study 4's original pilot cells used the old sender wording (15/16 differing), whereas the spec explicitly requires v0.6. Inspected Study 5's pilot validation and Study 4's repilot: `data/repilot/ratings.jsonl`, field `sender_clear`, matches all 16 Study 5 R1 pilot ratings exactly (maximum difference 0). The build now pins and uses that existing v0.6 reference for pilot ratings; original Study 4 cells remain the answer/seed reference. Main references already agree. No wording, tolerance, data, or scientific specification changed.
