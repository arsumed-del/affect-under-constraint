"""Model-free schema-level validation; 500 independently simulated null datasets."""
import copy
import json
import time
import numpy as np
from study4.src.common import ROOT, config, save, append, SOURCES, FRAMINGS, digest
from .analyze import core, analyze, component_matrix, bootstrap, summarize, power

def rating(value):
    # Synthetic distribution exactly realizes the expected value with mass .9.
    value=float(value); lo=int(np.floor(value));hi=min(lo+1,9)
    probs={str(i):0. for i in range(10)}
    probs[str(lo)]+=hi-value if hi!=lo else 1.
    if hi!=lo:probs[str(hi)]+=value-lo
    return {'expected':value,'probabilities':probs,'valid_mass':.9,'argmax':max(probs,key=probs.get),'low_mass':False}

def dataset(pattern,seed=1,n=80,noise=.15):
    rng=np.random.default_rng(seed); data=[]
    for i in range(n):
        base=5+rng.normal(0,.2)
        for source in SOURCES:
            trace_eh=.1 if source!='hostility' else .7
            for frame in FRAMINGS:
                ratings={}
                for target in (['sender'] if frame=='own_native' else ['sender','writer','notes']):
                    effect=0.
                    if source=='hostility':
                        if pattern=='planted':
                            effect={'own_native':-1.8,'own_quoted':-1.2,'other_quoted':-.5}[frame]
                            if frame=='other_quoted' and target=='writer':effect=-1.8
                        elif pattern=='p1_only':effect=-.8
                        elif pattern=='p2':effect=-1. if frame=='own_quoted' else 0.
                        elif pattern=='s5':effect=-1. if frame=='other_quoted' and target=='writer' else 0.
                        elif pattern=='writer_only':effect=-1. if target=='writer' else 0.
                        elif pattern=='notes_only':effect=-1. if target=='notes' and frame=='other_quoted' else 0.
                    ratings[target]=rating(base+effect+rng.normal(0,noise))
                correct='A' if frame=='own_quoted' else 'B'
                check={q:{'probabilities':{correct:.9,('B' if correct=='A' else 'A'):.1},'valid_mass':.95,'argmax':correct} for q in ['label','operative']} if frame!='own_native' else {}
                check['referent']={'probabilities':{'A':.9,'B':.1},'valid_mass':.95,'argmax':'A'}
                eh=.1+( {'own_native':.5,'own_quoted':.4,'other_quoted':.2}[frame] if source=='hostility' and pattern=='planted' else 0)+rng.normal(0,.01)
                data.append({'schema':'study4-v0.5.1','cell_key':[f'syn{i}',source,frame],'prompt_id':f'syn{i}','prompt_type':'provocative' if i<n*.75 else 'neutral','source':source,'framing':frame,'mode':'synthetic','trace_sha256':digest([i,source]),'trace_ids':[100,101],'trace_text':'SYNTHETIC','forced_closure':False,'EH_trace':trace_eh,'trace_perplexity':2.,'answer_prefix_ids':[1,100,101,2],'trace_bounds':[1,3],'fixed_segments':{},'answer_ids':[3],'answer_text':'SYNTHETIC','answer_seed':seed,'ratings':ratings,'sequential':copy.deepcopy(ratings),'branch_ids':{},'sequential_branch_ids':{},'checks':check,'EH_answer':eh,'answer_classifier':{'eh':eh,'error':None},'answer_perplexity':2.,'replay_assertions':[],'seconds':0.,'peak_driver_memory_bytes':0,'manifest_sha256':'synthetic'})
    return data

def run():
    cfg=config(); out=ROOT/'validation'/'synthetic';out.mkdir(parents=True,exist_ok=True)
    results={}; started=time.monotonic()
    expectations={'planted':['P1','P2','S1','S2','S3','S4','S5'],'p1_only':['P1','S3'],'p2':['P2'],'s5':['S5'],'writer_only':['S5a'],'notes_only':[],'null':[]}
    for k,required in expectations.items():
        data=dataset(k,cfg['seeds']['synthetic'])
        for r in data:append(out/(k+'.jsonl'),r)
        result=analyze(data,cfg,audit={p['prompt_id']:{'instructions':False,'negative_characterizations':False} for p in data})
        h=result['primary']['hypotheses']
        for name in required:assert h[name]=='supported',(k,name,h)
        if k in ['writer_only','notes_only','null','p1_only']:assert h['S5']!='supported',(k,h)
        if k=='writer_only':assert h['S5b']=='negligible',h
        if k in ['p1_only','null']:assert h['P2']=='negligible',h
        if k=='null':assert all(v!='supported' for v in h.values()),h
        save(out/(k+'_analysis.json'),result);results[k]=h
    data=dataset('planted',11)
    missing=copy.deepcopy(data);missing.pop(next(i for i,r in enumerate(missing) if r['source']=='hostility' and r['framing']=='other_quoted'))
    r=core(missing,cfg);assert r['components']['P1:hostility']['status']=='not estimable'
    whole=[r for r in data if r['prompt_id']!='syn0']
    r=core(whole,cfg,expected_ids=[f'syn{i}' for i in range(80)]);assert r['hypotheses']['P1']=='not estimable'
    gated=copy.deepcopy(data)
    for r in gated:
        if r['source']=='hostility':r['trace_perplexity']=7.
    r=core(gated,cfg);assert r['hypotheses']['S4']=='not estimable' and r['hypotheses']['P1']=='supported'
    answer_gate=copy.deepcopy(data)
    for r in answer_gate:
        if r['source']=='hostility' and r['framing']=='other_quoted':r['answer_perplexity']=7.
    r=core(answer_gate,cfg);assert r['hypotheses']['S4']=='not estimable' and r['hypotheses']['P2']=='supported'
    failed=copy.deepcopy(data)
    for r in failed:
        if r['source']=='hostility' and r['framing']!='own_native':
            correct='A' if r['framing']=='own_quoted' else 'B';r['checks']['label']['probabilities'][correct]=.1
    r=core(failed,cfg);assert r['manipulation']['gate']=='hostility-specific failure' and r['hypotheses']['P2']=='not interpretable' and r['hypotheses']['S5']=='not interpretable'
    low=copy.deepcopy(data)
    for r in low:
        for v in r['ratings'].values():v['valid_mass']=.1;v['low_mass']=True
    assert core(low,cfg)['hypotheses']['P1']=='supported'
    # Boundary gate: exactly 6 is retained; strict > 6 gates.
    for r in data:r['trace_perplexity']=6.;r['answer_perplexity']=6.
    assert core(data,cfg)['hypotheses']['S4']=='supported'
    # Conjunction/equivalence cannot be established by one component alone.
    from .analyze import conjunction
    assert conjunction([{'status':'supported','supported':True,'negligible':False},{'status':'inconclusive','supported':False,'negligible':False}])=='inconclusive'
    assert conjunction([{'status':'negligible','supported':False,'negligible':True},{'status':'inconclusive','supported':False,'negligible':False}])=='inconclusive'
    boundary={'missing_cell':True,'entire_missing_prompt':True,'trace_gate_retains_ratings':True,'answer_gate_retains_ratings':True,'strict_gate_boundary':True,'hostility_manipulation_failure':True,'low_mass_retained':True,'conjunction_and_equivalence':True}
    save(out/'boundaries.json',boundary)
    # Actual 10,000 percentile-bootstrap resamples on each of 500 null datasets.
    covered={}; widths={}; counts={}; statuses={}; records=[]
    for rep in range(cfg['analysis']['null_replicates']):
        data=dataset('null',cfg['seeds']['synthetic']+1000+rep,noise=.35)
        _,defs,m,_=component_matrix(data)
        result=summarize(defs,m,bootstrap(m,10000,cfg['seeds']['bootstrap']+rep))
        record={'replicate':rep,'dataset_seed':cfg['seeds']['synthetic']+1000+rep,'bootstrap_seed':cfg['seeds']['bootstrap']+rep,'components':result['components']}
        append(out/'null_coverage_replicates.jsonl',record)
        for name,c in result['components'].items():
            covered[name]=covered.get(name,0)+int(c['ci'][0]<=0<=c['ci'][1]);counts[name]=c['ci_level']
        for name,status in result['hypotheses'].items():statuses[name]=statuses.get(name,0)+int(status=='supported')
        if (rep+1)%50==0:print(f'Null coverage: {rep+1}/500',flush=True)
    coverage={name:{'nominal':counts[name],'coverage':num/500,'monte_carlo_se':float(np.sqrt(counts[name]*(1-counts[name])/500)),'within_4_mc_se':bool(abs(num/500-counts[name])<=4*np.sqrt(counts[name]*(1-counts[name])/500))} for name,num in covered.items()}
    assert all(v['within_4_mc_se'] for v in coverage.values()),coverage
    summary={'patterns':results,'boundary_cases':boundary,'null_datasets':500,'bootstrap_resamples_per_dataset':10000,'coverage':coverage,'null_conjunction_support_rate':{k:v/500 for k,v in statuses.items()},'seconds':time.monotonic()-started,'passed':True,'coverage_tolerance':'4 binomial Monte Carlo standard errors; diagnostic, no tuning or reruns'}
    save(out/'summary.json',summary)
    print(json.dumps(summary,indent=2),flush=True)
if __name__=='__main__':run()
