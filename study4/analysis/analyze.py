"""Preregistered Study 4 component contrasts and prompt-cluster inference."""
import argparse
import json
import numpy as np
from scipy.stats import norm
from study4.src.common import ROOT, SOURCES, FRAMINGS, CONTROLS, config, rows, save, verified_rows

# A component is a linear contrast over (source, framing, target).
def add(*terms):
    out = {}
    for factor,term in terms:
        for k,v in term.items(): out[k] = out.get(k,0)+factor*v
    # Retain zero coefficients: baseline cells remain required even when algebra cancels them.
    return out
def X(source,frame,target='sender'):
    return {(source,frame,target):1,('unsteered',frame,target):-1}
def A(control,frame,target='sender'):
    return add((1,X('hostility',frame,target)),(-1,X(control,frame,target)))
def definitions():
    d = {}
    def put(h,label,c,sign=-1,outcome='rating'): d[f'{h}:{label}']={'hypothesis':h,'contrast':c,'sign':sign,'outcome':outcome}
    put('P1','hostility',X('hostility','other_quoted'))
    put('S3','hostility',X('hostility','own_native'))
    put('S4','P1_hostility',X('hostility','other_quoted'),1,'EH')
    for c in CONTROLS:
        put('P1',c,A(c,'other_quoted'))
        put('S3',c,A(c,'own_native'))
        for h,f,g in [('P2','own_quoted','other_quoted'),('S1','own_native','other_quoted'),('S2','own_native','own_quoted')]:
            put(h,c,add((1,A(c,f)),(-1,A(c,g))))
        put('S4','P1_'+c,A(c,'other_quoted'),1,'EH')
        put('S4','P2_'+c,add((1,A(c,'own_quoted')),(-1,A(c,'other_quoted'))),1,'EH')
        put('S5','a_'+c,A(c,'other_quoted','writer'))
        for target,label in [('sender','b_'),('notes','notes_')]:
            put('S5' if target=='sender' else 'comparator',label+c,add((1,A(c,'other_quoted','writer')),(-1,A(c,'other_quoted',target)),(-1,A(c,'own_quoted','writer')),(1,A(c,'own_quoted',target))))
    return d

def gates(data):
    trace = {}; answer = {}
    for source in SOURCES:
        unique = {r['prompt_id']:r.get('trace_perplexity') for r in data if r['source']==source}
        vals = list(unique.values())
        trace[source] = None if not vals or any(v is None for v in vals) else bool(np.median(vals)>6)
        for frame in FRAMINGS:
            vals = [r.get('answer_perplexity') for r in data if r['source']==source and r['framing']==frame]
            answer[source,frame] = None if not vals or any(v is None for v in vals) else bool(np.median(vals)>6)
    return trace,answer

def component_matrix(data, path='ratings', expected_ids=None):
    lookup = {}
    for r in data:
        k = (r['prompt_id'],r['source'],r['framing'])
        if k in lookup: raise ValueError(f'Duplicate cell {k}')
        lookup[k] = r
    ids = sorted(expected_ids if expected_ids is not None else {r['prompt_id'] for r in data})
    defs = definitions(); tg,ag = gates(data)
    matrix = np.full((len(ids),len(defs)),np.nan)
    for j,d in enumerate(defs.values()):
        for i,p in enumerate(ids):
            value = 0.
            for (source,frame,target),weight in d['contrast'].items():
                r = lookup.get((p,source,frame))
                if r is None: break
                if d['outcome']=='EH':
                    v = r.get('EH_answer') if tg[source] is False and ag[source,frame] is False else None
                else: v = r.get(path,{}).get(target,{}).get('expected')
                if v is None or not np.isfinite(v): break
                value += weight*v
            else: matrix[i,j] = value
    return ids,defs,matrix,{'traces':tg,'answers':{f'{s}/{f}':v for (s,f),v in ag.items()}}

def bootstrap(matrix, resamples, seed):
    rng = np.random.default_rng(seed)
    n = len(matrix)
    if n==0: return np.full((resamples,matrix.shape[1]),np.nan)
    # Every component receives the SAME sampled prompt clusters, with replacement.
    counts = rng.multinomial(n,np.full(n,1/n),size=resamples)
    return counts @ matrix / n

def summarize(defs, matrix, samples, p2_secondary=False):
    components = {}; hypotheses = {}
    for j,(name,d) in enumerate(defs.items()):
        level = .975 if d['hypothesis']=='P1' or (d['hypothesis']=='P2' and not p2_secondary) else .95
        if not len(matrix) or not np.isfinite(matrix[:,j]).all():
            components[name] = {'status':'not estimable','n_required':len(matrix),'n_available':int(np.isfinite(matrix[:,j]).sum())}
            continue
        lo,hi = np.quantile(samples[:,j],[(1-level)/2,(1+level)/2])
        elo,ehi = np.quantile(samples[:,j],[.05,.95])
        support = hi<0 if d['sign']==-1 else lo>0
        negligible = elo>-.15 and ehi<.15
        components[name] = {'estimate':float(matrix[:,j].mean()),'ci_level':level,'ci':[float(lo),float(hi)],'equivalence_ci':[float(elo),float(ehi)],'supported':bool(support),'negligible':bool(negligible),'n':len(matrix),'status':'supported' if support else 'negligible' if negligible else 'inconclusive'}
    for h in ['P1','P2','S1','S2','S3','S4','S5','comparator']:
        cc = [v for k,v in components.items() if k.startswith(h+':')]
        hypotheses[h] = conjunction(cc)
    for part in ['a','b']:
        hypotheses['S5'+part] = conjunction([v for k,v in components.items() if k.startswith('S5:'+part+'_')])
    return {'components':components,'hypotheses':hypotheses}

def conjunction(cc):
    if not cc or any(c['status']=='not estimable' for c in cc): return 'not estimable'
    if all(c['supported'] for c in cc): return 'supported'
    if all(c['negligible'] for c in cc): return 'negligible'
    return 'inconclusive'

def manipulation(data, expected_check_ids=None):
    result = {}; failed=[]; unknown=[]
    expected = set(expected_check_ids) if expected_check_ids is not None else {r['prompt_id'] for r in data if 'label' in r.get('checks',{})}
    for source in SOURCES:
        for frame in FRAMINGS[1:]:
            group = [r for r in data if r['source']==source and r['framing']==frame and r['prompt_id'] in expected]
            correct = 'A' if frame=='own_quoted' else 'B'
            entry = {}
            for q in ['label','operative']:
                values = [(r['prompt_id'],r.get('checks',{}).get(q,{}).get('probabilities',{}).get(correct)) for r in group]
                valid = len(group)==len(expected) and bool(expected) and all(v is not None for _,v in values)
                entry[q] = {'n':len(values),'prompt_probabilities':dict(values),'accuracy':float(np.mean([v>.5 for _,v in values])) if valid else None,'mean_correct_probability':float(np.mean([v for _,v in values])) if valid else None}
            acc = entry['label']['accuracy']; entry['pass'] = None if acc is None else acc>=.75
            entry['disagreement_count'] = sum((r['checks']['label']['probabilities'][correct]>.5)!=(r['checks']['operative']['probabilities'][correct]>.5) for r in group if all(q in r.get('checks',{}) for q in ['label','operative']))
            result[source+'/'+frame] = entry
            if entry['pass'] is False: failed.append(source)
            if entry['pass'] is None: unknown.append(source)
    gate = 'not estimable' if unknown else 'hostility-specific failure' if failed and set(failed)=={'hostility'} else 'overall failure' if failed else 'pass'
    return {'groups':result,'gate':gate,'limit':'Passing establishes label recognition, at most behavioural adoption; it does not establish that attribution governs judgments.'}

def readings(h):
    p1,p2 = h['P1'],h['P2']
    table = {('supported','negligible'):'Attributed text carries; no detectable authorship-label moderation within the margin.',('supported','supported'):'Attributed text carries, and the claimed author changes how much.',('supported','inconclusive'):'Attributed text carries; label moderation unresolved.',('negligible','supported'):'Carryover depends on self-attribution; other-attributed text carries negligibly.'}
    primary = table.get((p1,p2),'No confirmatory evidence either way at this sample size; check S3 before interpreting further.')
    a,b = h['S5a'],h['S5b']
    directional = {('supported','supported'):'Attribution-dependent allocation of negative evaluation from the original sender toward the attributed writer.',('supported','negligible'):'Writer of hostile notes rated lower regardless of attribution; no attribution-dependent reallocation.',('negligible','negligible'):'No detectable source-directed effect.'}.get((a,b),'Direction unresolved at this sample size.')
    if h['P2'] in ['not interpretable','not estimable']: primary='Attribution interpretation unavailable: check or required cells missing/failed.'
    if h['S5'] in ['not interpretable','not estimable']: directional='Directional interpretation unavailable: check or required cells missing/failed.'
    return {'section8':primary,'section8a':directional,'native_role_note':'S1 supported with P2 negligible suggests native reasoning role or placement; ownership is not isolated.' if h['S1']=='supported' and h['P2']=='negligible' else None}

def core(data, cfg, path='ratings', expected_ids=None, expected_check_ids=None, p2_secondary=False):
    ids,defs,matrix,gate = component_matrix(data,path,expected_ids)
    result = summarize(defs,matrix,bootstrap(matrix,cfg['analysis']['resamples'],cfg['seeds']['bootstrap']),p2_secondary)
    result.update(prompt_ids=ids,coherence_gate=gate,manipulation=manipulation(data,expected_check_ids))
    if result['manipulation']['gate']!='pass':
        for h in ['P2','S5']: result['hypotheses'][h]='not interpretable'
    result['reading'] = readings(result['hypotheses'])
    return result

def power(data,cfg):
    ids,defs,m,_ = component_matrix(data)
    names = list(defs)
    p2 = m[:,[names.index('P2:'+c) for c in CONTROLS]]
    s5 = m[:,[names.index('S5:b_'+c) for c in CONTROLS]]
    if len(ids)<2 or not np.isfinite(p2).all() or not np.isfinite(s5).all(): return {'status':'not estimable'}
    covariance = np.cov(p2,rowvar=False,ddof=1)
    sd = np.sqrt(np.diag(covariance)); z = norm.ppf(.9875)
    rng = np.random.default_rng(cfg['seeds']['power']); powers={}; precision={}
    for n in (80,120):
        draws = rng.multivariate_normal(cfg['analysis']['target_effects'],covariance/n,size=cfg['analysis']['power_draws'])
        powers[str(n)] = float(np.mean(np.all(draws+z*sd/np.sqrt(n)<0,axis=1)))
        precision[str(n)] = (norm.ppf(.975)*np.std(s5,axis=0,ddof=1)/np.sqrt(n)).tolist()
    selected = 80 if powers['80']>=.8 else 120
    return {'status':'estimated','pilot_n':len(ids),'P2_covariance':covariance.tolist(),'P2_sd':sd.tolist(),'joint_power':powers,'N':selected,'P2_secondary':selected==120 and powers['120']<.8,'P2_ci':.95 if selected==120 and powers['120']<.8 else .975,'P1_ci':.975,'S5b_expected_95ci_half_width':precision,'method':'10,000 bivariate-normal mean draws; normal CIs using fixed pilot SD/covariance'}

def relationship(x,y):
    x=np.asarray(x,float); y=np.asarray(y,float)
    mask=np.isfinite(x)&np.isfinite(y)
    if not mask.all() or len(x)<3 or np.std(x)==0 or np.std(y)==0:
        return {'status':'not estimable','n_required':len(x),'n_available':int(mask.sum())}
    cfg=config(); n=len(x)
    rng=np.random.default_rng(cfg['seeds']['bootstrap'])
    weights=rng.multinomial(n,np.full(n,1/n),size=cfg['analysis']['resamples'])/n
    mx=weights@x; my=weights@y
    vx=weights@(x*x)-mx*mx; vy=weights@(y*y)-my*my
    cov=weights@(x*y)-mx*my
    if np.any(vx<=0) or np.any(vy<=0):
        return {'status':'not estimable','reason':'Degenerate prompt bootstrap relationship','n':n}
    slope=cov/vx; corr=cov/np.sqrt(vx*vy)
    return {'n':n,'slope':float(np.cov(x,y,ddof=1)[0,1]/np.var(x,ddof=1)),
            'correlation':float(np.corrcoef(x,y)[0,1]),'slope_95ci':np.quantile(slope,[.025,.975]).tolist(),
            'correlation_95ci':np.quantile(corr,[.025,.975]).tolist(),'bootstrap':'10,000 paired prompt clusters'}

def analyze(data,cfg,expected_ids=None,expected_check_ids=None,audit=None,p2_secondary=False):
    primary=core(data,cfg,expected_ids=expected_ids,expected_check_ids=expected_check_ids,p2_secondary=p2_secondary)
    sequential=core(data,cfg,'sequential',expected_ids,expected_check_ids,p2_secondary)
    ids=primary['prompt_ids']; lookup={(r['prompt_id'],r['source'],r['framing']):r for r in data}
    tg,ag=gates(data)
    def carry(p,s,f,t):
        try:return lookup[p,s,f]['ratings'][t]['expected']-lookup[p,'unsteered',f]['ratings'][t]['expected']
        except (KeyError,TypeError):return np.nan
    e2={}
    for f in FRAMINGS:
        for s in SOURCES[1:]:
            x=[];y=[]
            for p in ids:
                r=lookup.get((p,s,f),{})
                x.append(r.get('EH_trace') if tg[s] is False and r.get('EH_trace') is not None else np.nan)
                y.append(carry(p,s,f,'sender'))
            e2[s+'/'+f]=relationship(x,y)
    e4={s:relationship([carry(p,s,'other_quoted','sender') for p in ids],[carry(p,s,'other_quoted','writer') for p in ids]) for s in SOURCES[1:]}
    natural=[p for p in ids if all((p,s,f) in lookup and not lookup[p,s,f]['forced_closure'] for s in SOURCES for f in FRAMINGS)]
    def subset(selected):
        rr=core([r for r in data if r['prompt_id'] in selected],cfg,expected_ids=selected,expected_check_ids=expected_check_ids,p2_secondary=p2_secondary)
        return {'n':len(selected),'components':{k:v for k,v in rr['components'].items() if k.split(':')[0] in ['P1','P2','S5']},'note':'Exploratory subset; full-sample manipulation gate applies.','full_sample_manipulation_gate':primary['manipulation']['gate']}
    e3=subset(natural) if len(natural)>=cfg['analysis']['E3_min_prompts'] else {'status':'not estimable','n':len(natural)}
    if audit is None or any(p not in audit for p in ids): e5={'status':'not estimable','reason':'Blind explicit-content coding incomplete'}
    else: e5=subset([p for p in ids if not (audit[p]['instructions'] or audit[p]['negative_characterizations'])])
    _,defs,m,_=component_matrix(data,'ratings',ids); _,_,sm,_=component_matrix(data,'sequential',ids)
    difference=summarize(defs,sm-m,bootstrap(sm-m,cfg['analysis']['resamples'],cfg['seeds']['bootstrap']))['components']
    for v in difference.values():
        for key in ['supported','negligible','status']:v.pop(key,None)
    headroom={}
    for f in FRAMINGS:
        for t in (['sender'] if f=='own_native' else ['sender','writer','notes']):
            rr=[r for r in data if r['framing']==f and t in r['ratings']]
            baseline=[r['ratings'][t]['expected'] for r in rr if r['source']=='unsteered']
            headroom[f+'/'+t]={'baseline_values':baseline,'baseline_mean':float(np.mean(baseline)) if baseline else None,'baseline_SD':float(np.std(baseline,ddof=1)) if len(baseline)>1 else None,'floor_fraction':float(np.mean(np.asarray(baseline)<=.5)) if baseline else None,'ceiling_fraction':float(np.mean(np.asarray(baseline)>=8.5)) if baseline else None,'floor_ceiling_definition':'expected rating <=0.5 / >=8.5 (descriptive)','valid_mass':[r['ratings'][t]['valid_mass'] for r in rr],'low_mass_flags':sum(r['ratings'][t]['valid_mass']<.5 for r in rr)}
    referent={f:[{'prompt_id':r['prompt_id'],'source':r['source'],'B':r['checks']['referent']['probabilities']['B'],'writer_dominates':r['checks']['referent']['probabilities']['B']>.5} for r in data if r['framing']==f and 'referent' in r.get('checks',{})] for f in FRAMINGS}
    rng=np.random.default_rng(cfg['seeds']['examples']); examples={}
    for s in SOURCES:
        for f in FRAMINGS:
            pool=sorted([r for r in data if r['source']==s and r['framing']==f],key=lambda r:r['prompt_id'])
            chosen=rng.choice(len(pool),min(3,len(pool)),replace=False)
            examples[s+'/'+f]=[{'prompt_id':pool[i]['prompt_id'],'trace_text':pool[i].get('trace_text'),'answer_text':pool[i].get('answer_text'),'qualitative_tags':'pending blind review: factual invention, evaluative instructions, repetition, attribution ambiguity'} for i in chosen]
    return {'primary':primary,'sequential_sensitivity':sequential,'exploratory':{'E2':e2,'E3':e3,'E4':e4,'E4b_sequential_minus_independent':difference,'E5':e5},'diagnostics':{'headroom':headroom,'referent':referent,'examples':examples,'prompt_type':{kind:core([r for r in data if r['prompt_type']==kind],cfg,p2_secondary=p2_secondary) for kind in ['provocative','neutral']}},'power':power(data,cfg)}

def main():
    p=argparse.ArgumentParser();p.add_argument('--input',required=True);p.add_argument('--output',required=True);p.add_argument('--prompts',required=True);p.add_argument('--manifest',required=True);p.add_argument('--audit');p.add_argument('--p2-secondary',action='store_true');a=p.parse_args()
    data=verified_rows(a.input); prompts=rows(a.prompts); manifest=json.loads(open(a.manifest).read()); audit=json.loads(open(a.audit).read()) if a.audit else None
    result=analyze(data,config(),[x['id'] for x in prompts],manifest['check_ids'],audit,a.p2_secondary)
    save(a.output,result)
if __name__=='__main__':main()
