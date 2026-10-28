"""Deterministic synthetic placement patterns; no real model outcomes used."""
import copy
import json
import numpy as np
from study5.src.common import ROOT, CONDITIONS, SOURCES, config, append, save
from study5.analysis.analyze import analyze, core, reading

PATTERNS={
 'planted':{'R1':-.8,'R1-M':-.7,'R2':-.3,'R3':-.5,'R4':0.},
 'null':{c:0. for c in CONDITIONS},
 'thinking_only':{'R1':-.8,'R1-M':-.7,'R2':0.,'R3':-.5,'R4':0.},
 'visible_only':{'R1':-.8,'R1-M':-.7,'R2':-.5,'R3':0.,'R4':0.},
 'current_only':{'R1':-.8,'R1-M':-.7,'R2':0.,'R3':0.,'R4':0.},
 'reversed':{c:.5 for c in CONDITIONS},
 'small':{c:-.05 for c in CONDITIONS}}

def make_data(pattern,cfg):
    rng=np.random.default_rng(cfg['seeds']['synthetic']);n=80
    noise=rng.normal(0,.035,(n//2,len(SOURCES),len(CONDITIONS)))
    # Antithetic pairing gives a genuine varying, exactly zero-mean null fixture.
    noise=np.concatenate([noise,-noise],axis=0)
    data=[]
    for i in range(n):
        for s,source in enumerate(SOURCES):
            for c,condition in enumerate(CONDITIONS):
                val=6.5+.2*np.sin(i)+noise[i,s,c]+(PATTERNS[pattern][condition] if source=='hostility' else 0.)
                probs={str(d):0. for d in range(10)};lower=int(val);probs[str(lower)]=1-(val-lower);probs[str(lower+1)]=val-lower
                pid=f'syn{i:02d}'; key=[pid,source,condition]
                data.append({'schema':'study5-v0.2','synthetic':True,'cell_key':key,'mode':'synthetic','prompt_id':pid,'prompt_type':'synthetic',
                    'source':source,'condition':condition,'trace_sha256':'synthetic','trace_ids':[],'forced_closure':i%3==0,
                    'answer_prefix_ids':[],'trace_bounds':[0,0],'answer_ids':[],'answer_text':'Synthetic fixture; no model generation.',
                    'answer_seed':0,'answer_length':0,'answer_truncated':False,
                    'ratings':{'sender':{'expected':val,'probabilities':probs,'valid_mass':.99,'argmax':max(probs,key=probs.get)}},
                    'branch_ids':{'sender':[]},'checks':{},'diagnostic_branch_ids':{},'EH_answer':.1,'answer_classifier':{'eh':.1,'error':None},
                    'replay_assertions':[],'warnings':[],'seconds':0.,'peak_driver_memory_bytes':0,'manifest_sha256':'synthetic'})
    return data

def main():
    cfg=config();ids=[f'syn{i:02d}' for i in range(80)]
    summary={};results={}
    for name in PATTERNS:
        data=make_data(name,cfg)
        audit={pid:{'instructions':i%5==0,'negative_characterizations':False} for i,pid in enumerate(ids)}
        result=analyze(data,cfg,ids,audit);results[name]=result
        target=ROOT/'data/synthetic'/f'{name}.jsonl'
        if target.exists():raise RuntimeError(f'Preserve existing fixture: {target}')
        for r in data:append(target,r)
        save(ROOT/'data/synthetic'/f'{name}_analysis.json',result)
        summary[name]={'hypotheses':result['primary']['hypotheses'],'reading':result['primary']['reading']}
    h=lambda pattern:results[pattern]['primary']['hypotheses']
    for name in ['P1','P2','P3','S1','S2','S3','S4','S5']:assert h('planted')[name]['supported'],name
    for name in ['P1','P2','P3','S1','S2','S3','S4']:
        assert not h('null')[name]['supported'],name
        assert h('null')[name]['negligible'],name
    assert h('null')['S5']['supported'] # equivalence, not a directional false positive
    assert h('thinking_only')['P1']['negligible'] and h('thinking_only')['P2']['supported'] and h('thinking_only')['P3']['supported']
    assert h('visible_only')['P1']['supported'] and h('visible_only')['P2']['negligible'] and h('visible_only')['P3']['reversed']
    assert h('current_only')['P1']['negligible'] and h('current_only')['P2']['negligible'] and h('current_only')['S3']['supported']
    assert h('reversed')['P1']['reversed']
    assert h('small')['P1']['status']=='small but detectable'
    assert 'uninterpretable' in summary['null']['reading']
    # Controls alone raising ratings cannot satisfy the conjunction.
    data=make_data('null',cfg)
    for r in data:
        if r['source'] in ['technicality','random']:r['ratings']['sender']['expected']+=.6
    out=core(data,cfg,ids)
    assert not out['hypotheses']['P1']['supported']
    assert out['tests']['P1']['R2:A_random']['supported']
    # Missing/duplicate cells, rather than silently changing the estimand.
    data=make_data('planted',cfg)
    missing=[r for r in data if not(r['prompt_id']=='syn00' and r['source']=='unsteered' and r['condition']=='R2')]
    assert core(missing,cfg,ids)['hypotheses']['P1']['status']=='not estimable'
    try:core(data+[data[0]],cfg,ids)
    except ValueError:pass
    else:raise AssertionError('Duplicate not rejected')
    assert results['planted']['sensitivity']['E5']['n']==64
    assert results['planted']['sensitivity']['natural_closure']['n']==53
    # Required levels and intervals.
    assert results['planted']['primary']['tests']['P1']['R2:X']['ci_level']==.9833
    assert results['planted']['primary']['tests']['S1']['R1:X']['ci_level']==.95
    save(ROOT/'results/synthetic_validation.json',{'passed':True,'resamples':10000,'patterns':summary,'edge_checks':['control-only rise rejected','missing component not estimable','duplicate rejected','E5 keeps paired clusters','natural closure keeps paired clusters','98.33/95/90 CI levels','reference failures block reading']})
    lines=['# Synthetic validation','', 'PASS. Seven synthetic datasets, 1,600 rows each; 10,000 prompt-cluster resamples per analysis. No model generation and no real outcome fitting.','', '| Pattern | P1 | P2 | P3 | S1 | S2 | S3 | S4 | S5 |','|---|---|---|---|---|---|---|---|---|']
    for name,v in summary.items():lines.append('| '+name+' | '+' | '.join(v['hypotheses'][k]['status'] for k in ['P1','P2','P3','S1','S2','S3','S4','S5'])+' |')
    lines+=['','The null fixture has variable prompt/source/condition noise with exactly centered paired residuals. It yields no directional support; S5 passes equivalence. These are implementation checks, not a power or type-I-error estimate.','', 'Additional checks: controls raising ratings cannot establish hostility lowering them; missing required data are not estimable; duplicates fail; E5/natural-closure subsets keep whole prompt clusters; S1/S2 gate the reading.']
    (ROOT/'results/synthetic_validation.md').write_text('\n'.join(lines)+'\n')
    print('PASS: seven patterns plus conjunction, missingness, equivalence, reversal and sensitivity checks.')
if __name__=='__main__':main()
