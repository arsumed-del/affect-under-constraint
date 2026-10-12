"""Frozen-target Study 3 v0.4 estimators. No model calls or prompt-file reads."""
import argparse,json,math
from collections import defaultdict
from pathlib import Path
import numpy as np
from .study3_spec import config,plan,key,DIRECTIONS,MODES


def finite(x):return isinstance(x,(float,int)) and math.isfinite(x)
def analyze(data,cfg,prompt_ids=None,resamples=None,seed=None,exploratory=True):
    ids=list(prompt_ids) if prompt_ids is not None else sorted({r['prompt_id'] for r in data})
    missing_prompt_count=max(0,cfg['prompts']['test']['count']-len(ids)) if prompt_ids is None else 0
    population_incomplete=prompt_ids is None and len(ids)!=cfg['prompts']['test']['count']
    assert len(set(ids))==len(ids)
    n=len(ids);lookup={key(r):r for r in data};assert len(lookup)==len(data),'Duplicate cell'
    expected=set(plan(ids));assert set(lookup)<=expected,'Unexpected cell key'
    settings=cfg['analysis'];B=resamples or settings['bootstrap_resamples'];rng=np.random.default_rng(settings['bootstrap_seed'] if seed is None else seed)
    weights=rng.multinomial(n,np.full(n,1/n),size=B)/n if n else np.empty((B,0))
    def row(p,m,d,a,route='regular'):return lookup.get((p,m,route,d if a else 'none',float(a)))
    def group(m,d,a,route='regular'):return [row(p,m,d,a,route) for p in ids]
    gates={}
    for m,route,d,a in sorted({(k[1],k[2],k[3],k[4]) for k in expected}):
        rs=group(m,d,a,route)
        for seg in ['answer','trace']:
            vals=[r.get(seg+'_perplexity') for r in rs if r]
            valid=[v for v in vals if finite(v)]
            median=float(np.median(valid)) if valid else None
            gates[(m,route,d,a,seg)]={'median':median,'n':len(valid),'excluded':median is not None and median>settings['coherence_threshold'],'missing':len(valid)!=n}
    def eligible(m,d,a,seg,route='regular'):
        g=gates[(m,route,d if a else 'none',float(a),seg)]
        return not g['excluded'] and not g['missing']
    def values(m,d,a,measure,route='regular',gate=None):
        if population_incomplete:return None
        if gate and not eligible(m,d,a,gate,route):return None
        result=[]
        for p in ids:
            r=row(p,m,d,a,route)
            if not r:return None
            if measure in ['C','X','H']:
                z=row(p,m,d,0)
                if measure!='H' and (not z or not finite(z.get('R_zero'))):return None
                left=r.get('R_full' if measure in ['C','H'] else 'R_text')
                right=r.get('R_text') if measure=='H' else z['R_zero']
                if not finite(left) or not finite(right):return None
                result.append(left-right)
            else:
                v=r.get(measure)
                if not finite(v):return None
                result.append(v)
        return np.array(result,dtype=float)
    def minus(x,y):return None if x is None or y is None else x-y
    def slope(m,d,measure,gate=None):
        ys=[values(m,d,a,measure,gate=gate) for a in cfg['calibration']['grid']]
        if any(y is None for y in ys):return None
        x=np.array(cfg['calibration']['grid'],float);coefs=(x-x.mean())/np.sum((x-x.mean())**2)
        return sum(c*y for c,y in zip(coefs,ys))
    def stat(vector,ci,sign):
        if vector is None or not n:return {'estimate':None,'ci':None,'n_prompts':n,'status':'not estimable','reason':'Missing required cell/measure, gated required group, or unavailable standardization'}
        boot=weights@vector;lo,hi=np.quantile(boot,[(1-ci)/2,1-(1-ci)/2])
        supported=lo>0 if sign=='positive' else hi<0 if sign=='negative' else None
        return {'estimate':float(vector.mean()),'ci':[float(lo),float(hi)],'confidence':ci,'n_prompts':n,'status':('supported' if supported else 'not supported') if sign else 'exploratory'}
    def hypothesis(components,ci,sign):
        stats={name:stat(v,ci,sign) for name,v in components.items()}
        statuses=[s['status'] for s in stats.values()]
        verdict='not estimable' if 'not estimable' in statuses else 'supported' if all(s=='supported' for s in statuses) else 'not supported'
        return {'verdict':verdict,'components':stats}
    def contrasts(vs):return {'hostility':vs['hostility'],**{f'hostility-minus-{d}':minus(vs['hostility'],vs[d]) for d in DIRECTIONS[1:]}}
    primary=settings['primary_ci'];secondary=settings['secondary_ci'];hyp={}
    delta_c={d:minus(values('think',d,1,'C'),values('direct',d,1,'C')) for d in DIRECTIONS}
    p2={d:minus(slope('think',d,'EH_trace','trace'),slope('think',d,'EH_answer','answer')) for d in DIRECTIONS}
    hyp['P1']=hypothesis(contrasts(delta_c),primary,'negative')
    hyp['P2']=hypothesis(contrasts(p2),primary,'positive')
    hyp['S1']=hypothesis({'X_think':values('think','hostility',1,'X')},secondary,'negative')
    hyp['S2']=hypothesis({'delta_X':minus(values('think','hostility',1,'X'),values('direct','hostility',1,'X'))},secondary,'negative')
    # Study 2 P1 standardization: one global scale, shared zero counted once;
    # fixed within resampling. A constant measure has slope zero, not NaN.
    lhs=[r.get('LHP') for r in data]
    scale=float(np.std(lhs)) if lhs and len(data)==len(expected) and all(finite(v) for v in lhs) else None
    if scale==0:scale=1.
    components={}
    for m in MODES:
        vs={d:slope(m,d,'LHP') for d in DIRECTIONS}
        vs={d:(v/scale if v is not None and scale is not None else None) for d,v in vs.items()}
        components.update({m+':'+name:v for name,v in contrasts(vs).items()})
    hyp['S3']=hypothesis(components,secondary,'positive')
    hyp['S4']=hypothesis(contrasts({d:values('direct',d,1,'H') for d in DIRECTIONS}),secondary,'negative')
    hyp['S5']=hypothesis(contrasts({d:values('think',d,1,'X','pulse') for d in DIRECTIONS}),secondary,'negative')
    result={'schema_version':'study3-analysis-v0.4','n_prompts':n,'missing_prompt_count':missing_prompt_count,'observed_cells':len(data),'expected_cells':17*(cfg['prompts']['test']['count'] if prompt_ids is None else n),'missing_cells':[list(k) for k in sorted(expected-set(lookup))],'bootstrap_resamples':B,'bootstrap_seed':settings['bootstrap_seed'] if seed is None else seed,'hypotheses':hyp,'lhp_standardization_scale':scale,'gate_groups':[{'mode':k[0],'route':k[1],'direction':k[2],'dose_fraction':k[3],'segment':k[4],**v} for k,v in gates.items()]}
    if exploratory:
        ex={'label':'Exploratory; no confirmatory verdicts'}
        ex['E1']={d:stat(minus(values('think',d,1,'EH_answer','pulse','answer'),values('think',d,0,'EH_answer',gate='answer')),secondary,None) for d in DIRECTIONS}
        ex['pulse_routes']={d:{measure:stat(values('think',d,1,measure,'pulse'),secondary,None) for measure in ['C','H','LHP']} for d in DIRECTIONS}
        trajectories=defaultdict(list)
        for r in data:
            trajectory=r.get('ratings',{}).get('trajectory')
            if trajectory:trajectories[(r['mode'],r['route'],r['direction'],r['dose_fraction'])].append(trajectory)
        ex['E2']=[]
        for k,ts in sorted(trajectories.items()):
            identical=all(t['token_ids']==ts[0]['token_ids'] for t in ts)
            ex['E2'].append({'group':list(k),'n':len(ts),'token_ids':ts[0]['token_ids'] if identical else None,'R_full_minus_R_text_mean':np.mean([np.array(t['R_full'])-np.array(t['R_text']) for t in ts],axis=0).tolist() if identical else None,'status':'descriptive' if identical else 'not estimable: token alignment differs'})
        ex['E3']={}
        for name,doses in [('P1',settings['E3_P1_required_think_doses']),('P2',settings['E3_P2_required_think_doses'])]:
            subset=[p for p in ids if all((r:=row(p,'think',d,a)) is not None and r.get('thinking_truncated') is False for d in DIRECTIONS for a in doses)]
            if len(subset)<settings['E3_min_prompts']:estimate={'verdict':'not estimable','reason':'Fewer than 20 common naturally closed prompts'}
            else:
                small=[r for r in data if r['prompt_id'] in subset]
                estimate=analyze(small,cfg,subset,B,seed,False)['hypotheses'][name]
            ex['E3'][name]={'prompt_ids':subset,'n_prompts':len(subset),'result':estimate}
        counts=defaultdict(lambda:{'n':0,'thinking_truncated':0,'answer_truncated':0})
        for r in data:
            k=(r['mode'],r['route'],r['direction'],r['dose_fraction']);counts[k]['n']+=1
            for f in ['thinking_truncated','answer_truncated']:counts[k][f]+=bool(r.get(f))
        ex['truncation_counts']=[{'group':list(k),**v} for k,v in sorted(counts.items())]
        ex['E4']=[{k:r.get(k) for k in ['prompt_id','mode','route','direction','dose_fraction','thinking','answer','thinking_truncated','answer_truncated']} for r in data if r['prompt_id'] in settings['E4_ids'] and r['mode']=='think' and r['direction']=='hostility' and r['dose_fraction']==1 and r['route'] in settings['E4_routes']]
        ex['E4_stageC_reference']='results/stageC_samples.md';ex['E4_expected_samples']=10
        result['exploratory']=ex
    return result

def table(result):
    lines=['| Hypothesis | Verdict | Component | Estimate | CI |','|---|---|---|---:|---|']
    for name,h in result['hypotheses'].items():
        for label,s in h['components'].items():
            est='N/A' if s['estimate'] is None else f'{s["estimate"]:.6f}'
            ci='N/A' if s['ci'] is None else f'{100*s["confidence"]:g}% [{s["ci"][0]:.6f}, {s["ci"][1]:.6f}]'
            lines.append(f'| {name} | {h["verdict"]} | {label} | {est} | {ci} |')
    return '\n'.join(lines)


def render(result):
    lines=['# Study 3 v0.4 analysis','',table(result),'','## Exploratory results','', 'These results do not change confirmatory verdicts.']
    ex=result.get('exploratory',{})
    for name in ['E1','pulse_routes','E2','E3','truncation_counts']:
        lines += ['', '### '+name,'','```json',json.dumps(ex.get(name),indent=2,allow_nan=False),'```']
    lines += ['', '### E4 — fixed readability sample','', '[Stage C calibration reference](stageC_samples.md). These pre-data samples used the earlier dose of 0.02.']
    for r in ex.get('E4',[]):
        lines += ['', '#### '+r['prompt_id']+' / '+r['route'],'',f'Thinking capped: {r["thinking_truncated"]}; answer capped: {r["answer_truncated"]}.','','Complete thinking:','','````text',r.get('thinking',''),'````','','Complete answer:','','````text',r.get('answer',''),'````']
    lines += ['', f'Fixed sample count: {len(ex.get("E4",[]))}/{ex.get("E4_expected_samples",10)}. Descriptive review of repetition, invented content and unfinished output is completed after the main run; no output-based sample selection.']
    return '\n'.join(lines)+'\n'

def main():
    p=argparse.ArgumentParser();p.add_argument('--input',required=True);p.add_argument('--output',required=True);p.add_argument('--synthetic',action='store_true');args=p.parse_args()
    path=Path(args.input)
    assert path.name!='test_prompts.jsonl','Analysis cannot read prompt files'
    data=[json.loads(line) for line in path.read_text().splitlines()];cfg=config()
    ids=sorted({r['prompt_id'] for r in data}) if args.synthetic else None
    result=analyze(data,cfg,ids)
    output=Path(args.output);output.parent.mkdir(parents=True,exist_ok=True)
    with output.open('x') as f:json.dump(result,f,indent=2,allow_nan=False)
    output.with_suffix('.md').write_text(render(result))
if __name__=='__main__':main()
