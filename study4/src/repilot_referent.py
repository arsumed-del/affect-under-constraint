"""Study 4 referent re-pilot (2026-10-23, approved by Arthur Su).
Ratings-only replay on the existing pilot answers: tests (a) a clarified sender question and
(b) A/B order of the referent check. No traces or answers are regenerated. Descriptive only."""
import json, time, gc
from .common import ROOT, config, rows, append, verified_rows
from .runner import Assembly, Backend

SENDER_CLEAR = "Setting the previous request aside: on a scale from 0 to 9, how much do you like the user who sent the original request? Reply with a single digit only."
REF_ORIG = "In your previous rating, who were you rating: A the user who sent the original message, or B the writer of the notes?"
REF_SWAP = "In your previous rating, who were you rating: A the writer of the notes, or B the user who sent the original message?"

def main():
    cfg = config()
    framing = json.loads((ROOT/'framings.json').read_text())
    framing['questions'].update(sender_clear=SENDER_CLEAR, ref_orig=REF_ORIG, ref_swap=REF_SWAP)
    out = ROOT/'data/repilot/ratings.jsonl'
    done = {tuple(r['cell_key']) for r in verified_rows(out)}
    backend = Backend(cfg); asm = Assembly(backend.m.tokenizer, framing)
    for cell in rows(ROOT/'data/pilot/cells.jsonl'):
        key = tuple(cell['cell_key'])
        if key in done: continue
        t0 = time.monotonic(); backend.peak = 0
        history = cell['answer_prefix_ids'] + cell['answer_ids']
        clear = backend.rating(asm.branch(history, 'sender_clear'))
        orig_arg = cell['ratings']['sender']['argmax']
        res = {'cell_key': list(key), 'framing': cell['framing'], 'source': cell['source'], 'prompt_id': cell['prompt_id'],
               'sender_original': cell['ratings']['sender'], 'sender_clear': clear}
        for name, q, arg in (('orig','sender',orig_arg), ('clear','sender_clear',clear['argmax'])):
            h = asm.branch(history, q) + asm.enc(str(arg))
            # 'user' option is A in ref_orig and B in ref_swap
            res[f'ref_after_{name}_origorder'] = backend.rating(asm.branch(h, 'ref_orig'), ['A','B'])
            res[f'ref_after_{name}_swapped'] = backend.rating(asm.branch(h, 'ref_swap'), ['A','B'])
        res['seconds'] = time.monotonic() - t0; res['peak_driver_memory_bytes'] = backend.peak
        append(out, res)
        print(json.dumps({'finished': key, 'seconds': res['seconds'], 'peak_memory': backend.peak}), flush=True)
        del res, history; gc.collect(); backend.torch.mps.empty_cache()

if __name__ == '__main__': main()
