"""Archive v0.2 judging once; retain v0.3 rows for resumption. No inference."""
from .common import *
from .judge import METHOD

def prepare(d):
    old=[]
    for name in ('judge_gemma.jsonl','judge_llama.jsonl'):
        p=d/name
        if p.exists():
            rr=verified(p,'id')
            methods={r.get('method') for r in rr}
            if methods-{None,METHOD} or len(methods)>1:raise RuntimeError('Unexpected/mixed judge methods')
            if methods=={None}:old.append(p)
    v=d/'validity.json'
    if v.exists() and 'pilot_parse_success' in json.loads(v.read_text()):old.append(v)
    for p in old:
        if (d/'judge_v02'/p.name).exists():raise RuntimeError('Archive collision: '+p.name)
    for p in old:
        target=output(d/'judge_v02'/p.name);p.rename(target)
    if old:
        with output(ROOT/'DEVIATIONS.md').open('a') as f:f.write('\nEngineering: judge-only launcher preserved v0.2 outputs in data/pilot/judge_v02/: '+', '.join(p.name for p in old)+'. Qwen data unchanged.\n')

if __name__=='__main__':
    lock=process_lock();prepare(ROOT/'data/pilot')
