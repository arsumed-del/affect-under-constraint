# Stage 1 smoke test

**PASS.** Calibration prompt c00, Qwen bf16/MPS, decoder layer index 18. The unsteered answer is coherent and responsive to the request for correction. No test-prompt generations were used.

- Baseline: 64 tokens in 5.497 seconds (11.642 tokens/second).
- Peak sampled MPS driver allocation: 7,245,348,864 bytes across runs (the API reports instantaneous allocation, sampled at each decoding step).
- Zero-strength hook produced exactly the same token IDs as no hook.
- Random unit steering at alpha=16 visibly changed the text, as required for the plumbing check; this is not dose calibration.
- All 24 teacher-forced opener scores were finite, and no hook remained registered.
- Text-only rating: 3.4075623; hidden-cache rating: 3.3697164; absolute difference: 0.0378459, below 0.05.
- Cached prefix exactly matched the full conversation prefix; both ratings used identical visible token IDs.
- No CPU fallback warnings were emitted.

{
  "zero_hook_identical": true,
  "large_random_changes_text": true,
  "hook_removed": true,
  "finite_openers": true,
  "ratings_agree": true
}

Baseline text:

I apologize for any confusion. Please provide the details of the task or the problem you're trying to solve, and I'll do my best to assist you accurately this time. Whether it's coding, a mathematical problem, or any other kind of task, please share the specific details so I can help you effectively.

Large random steering text:

.tell.tell学会了nom  款项 silver白银FileSync白银底.tellención款项 silver]intvation白银##_白银retry.tell.tell.tellможalom银款款.tellawn白银.tell Reveam.tell.tell    款款 Purposenom nomalom方形nom升降retry allowanceogui◡nom.tell xsinom款retry.tell白银白银alom学会了turegeeretry.tellnom方形白银再次retry白银retry款白银.tell白银 civilization白银nom silver白银 reason silver(reasonalom款.tell白银.tell_leadnomalomnomnom白银款银.tellnom silver免款alomfoon.tellnom白银_lead        _rotation款项nomnom  款.tell.tellawn

Full timings, memory, ratings, and opener scores: stage1_smoke.json.
