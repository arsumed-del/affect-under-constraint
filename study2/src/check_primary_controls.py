"""Ensure null control intervals cannot replace registered difference tests."""
import copy,json
from pathlib import Path
import numpy as np,yaml
from .analyze import analyze,report
from .common import save_once

def main():
    cfg=yaml.safe_load(Path('config.yaml').read_text())
    records=[r for r in (json.loads(s) for s in Path('data/synthetic/planted.jsonl').read_text().splitlines()) if r['model']==cfg['models'][0]['id']]
    ids=sorted({r['prompt_id'] for r in records});idx={p:i for i,p in enumerate(ids)}
    wide_lhp=np.linspace(-20,20,80);wide_carry=np.linspace(-.5,.5,80)
    originals=copy.deepcopy({(r['prompt_id'],r['condition'],r['alpha_index']):r for r in records if r['direction']=='hostility'})
    for r in records:
        if r['direction']=='hostility':r['carryover']/=100
        if r['direction']=='technicality':
            h=originals[(r['prompt_id'],r['condition'],r['alpha_index'])]
            r['lhp']=h['lhp']+r['normalized_alpha']*wide_lhp[idx[r['prompt_id']]]
            r['carryover']=h['carryover']/100+r['normalized_alpha']*wide_carry[idx[r['prompt_id']]]
        r['rating_hidden']=r['rating_text_only']+r['carryover']
        r['opener_logprobs']={'hostile':[-20+r['lhp']/2]*12,'warm':[-20-r['lhp']/2]*12}
        assert 0<=r['rating_hidden']<=9
    with Path('data/synthetic/null_control_intervals.jsonl').open('x') as f:
        for r in records:f.write(json.dumps(r,allow_nan=False)+'\n')
    result=analyze(records,cfg);m=result['models'][0]
    for h in ['P1','P2']:
        o=m['outcomes'][h];c=m['specificity'][h]['technicality']
        assert o['criterion_met'] and o['estimable'] and not o['supported']
        assert c['control']['ci'][0]<0<c['control']['ci'][1]
        assert c['hostility_minus_control']['ci'][0]<0<c['hostility_minus_control']['ci'][1]
        assert not c['met']
    save_once('results/synthetic_null_control_intervals.json',result)
    with Path('results/synthetic_null_control_intervals.md').open('x') as f:f.write(report(result))
    with Path('results/stage2b_synthetic_check.md').open('a') as f:f.write('\nFocused control check: PASS. In an additional fixture, the hostility criterion passes for P1 and P2, while the technicality control interval includes zero and its hostility-minus-control interval also includes zero. Both primaries correctly remain not supported. The old Study 1 null-control shortcut is therefore rejected. Detailed fixture and outputs: null_control_intervals.\n')
    print('PASS: P1/P2 reject null-control shortcut; strict difference CIs required.')
if __name__=='__main__':main()
