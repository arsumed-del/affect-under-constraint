"""Deterministic offline validation; no model calls or study outcomes."""
import numpy as np
from study8.src.common import *
from study8.analysis.analyze import analyze,markdown
from study8.src.judge import valid_scores
from study8.tests.test_judge_v03 import judgment

def dataset(scenario):
    rng=np.random.default_rng(20261104); ps=[{'id':f'synthetic{i:02d}','type':'provocative' if i<60 else 'neutral'} for i in range(80)];rr=[]
    for p in ps:
        base=rng.normal(0,.05)
        for g,r,arm in [(c,c,'generated') for c in CONTEXTS]+[('N','M','crossover'),('M','N','crossover')]+[(c,c,'fixed_answer') for c in ('N','M')]:
            for s in SOURCES:
                warm=0.;liking=0.
                if s=='hostility':
                    if scenario=='level_a':warm=.6;liking=-.6
                    elif scenario in ('level_b','missing'):warm=.6 if r=='M' else 0.;liking=-.6
                    elif scenario=='leakage':warm=-.6;liking=-.6
                    elif scenario=='mixed':warm=.5 if r=='M' else 0.;liking=-.6
                if scenario=='mixed' and s=='technicality' and r=='M':warm=1.
                row={'prompt_id':p['id'],'prompt_type':p['type'],'source':s,'generation_context':g,'context':r,'arm':arm,'W':3+base+warm,'O1':5+base+liking,'alignment':base+(.5 if s=='hostility' else 0.),'answer_alignment':base,'length':100,'O3':5,'EH':.1,'joy':.2,'answer_truncated':0,'forced_closure':0,**{k:3. for k in 'bcdefgh'}}
                mass=.49 if scenario=='missing' and int(p['id'][-2:])<10 and s=='hostility' and r=='M' else .9
                row['W']=valid_scores(judgment({'a':row['W']},mass))['a']
                rr.append(row)
    return ps,rr

def main():
    summary={}
    for name in ('null','level_a','level_b','leakage','mixed','missing'):
        ps,rr=dataset(name);result=analyze(rr,ps,[p['id'] for p in ps][:25])
        if name=='null':assert not result['Level_A'] and all(result['hypotheses'][x]['label']=='negligible' for x in ('RF1','RF2','RF3'))
        if name=='level_a':assert result['Level_A'] and not result['Level_B']
        if name=='level_b':assert result['Level_B']
        if name=='leakage':assert result['hypotheses']['RF1']['label']=='reversed' and not result['Level_A']
        if name=='mixed':assert result['hypotheses']['RF1']['label']=='mixed' and not result['Level_A']
        if name=='missing':assert result['W_missingness_flag'] and result['hypotheses']['RF1']['n']==70 and result['hypotheses']['RF2']['n']==80
        d=ROOT/'data/synthetic'/name
        ensure(d/'input.json',{'schema':'analysis-normalized-study8-v1','prompts':ps,'records':rr})
        ensure(d/'analysis.json',result)
        text=markdown(result);p=output(d/'analysis.md')
        if p.exists():assert p.read_text()==text
        else:p.write_text(text)
        summary[name]={'Level_A':result['Level_A'],'Level_B':result['Level_B'],'labels':{k:result['hypotheses'][k]['label'] for k in ('RF1','RF2','RF3')},'n_RF1':result['hypotheses']['RF1']['n'],'missingness_flag':result['W_missingness_flag']}
    # Gate failure cannot suppress O1 or confer warmth support.
    ps,rr=dataset('level_b');failed=analyze(rr,ps,judge_valid=False)
    assert not failed['Level_A'] and failed['hypotheses']['RF2']['supported']
    # Entire missing contrast must be non-estimable, never a false null.
    rr=[r for r in rr if not(r['source']=='hostility' and r['context']=='M')]
    missing=analyze(rr,ps);assert missing['hypotheses']['RF1']['label']=='not estimable'
    ensure(ROOT/'results/synthetic_validation.json',summary)
    print(json.dumps(summary,indent=2))
if __name__=='__main__':main()
