"""Study 2 v3.1 estimators; fixed before main-run outcomes."""
import os
os.environ['PYTORCH_ENABLE_MPS_FALLBACK']='1'
import argparse
import json
from pathlib import Path
import numpy as np
import yaml
from .schema import validate

DIRECTIONS=['hostility','technicality','random']
CONDITIONS=['neutral','warm_constraint']
DOSES=np.array([0,.125,.25,.5,.75,1.])
FIELDS=['lhp','eh','entropy','leak_timecourse','carryover','ew']

def finite(value):
    return None if not np.isfinite(value) else float(value)

def ratio(numerator,denominator):
    out=np.full(np.broadcast_shapes(np.shape(numerator),np.shape(denominator)),np.nan)
    np.divide(numerator,denominator,out=out,where=np.isfinite(denominator)&(denominator!=0))
    return out

def summary(values,level=.95):
    valid=values[1:][np.isfinite(values[1:])]
    tail=(1-level)/2
    ci=np.quantile(valid,[tail,1-tail]).tolist() if len(valid) else [None,None]
    return {'estimate':finite(values[0]),'ci':ci,'confidence_level':level,'bootstrap_valid':len(valid),'bootstrap_missing':len(values)-1-len(valid)}

def interval(values,sign,level=.95):
    ci=summary(values,level)['ci']
    return bool(np.isfinite(values[0]) and ci[0] is not None and (ci[0]>0 if sign>0 else ci[1]<0))

def mean_stat(y,weights):
    mask=np.isfinite(y)
    return ratio(weights@np.where(mask,y,0),weights@mask.astype(float))

def slope(y,weights):
    x=np.broadcast_to(DOSES,y.shape)
    mask=np.isfinite(y)
    yy=np.where(mask,y,0)
    sufficient=np.stack([mask.sum(1),(x*mask).sum(1),yy.sum(1),(x*x*mask).sum(1),(x*yy).sum(1)],axis=1)
    n,sx,sy,sxx,sxy=(weights@sufficient).T
    return ratio(n*sxy-sx*sy,n*sxx-sx*sx)

def prompt_mean(y):
    valid=np.isfinite(y)
    return ratio(np.where(valid,y,0).sum(1),valid.sum(1))

def bic_gap(g,weights):
    """Weighted sufficient statistics exactly reproduce cluster-resampled OLS."""
    p=len(g)
    x=np.tile(DOSES,p)
    y=g.ravel()
    good=np.isfinite(y)
    yy=np.where(good,y,0)
    n=weights@good.reshape(p,6).sum(1)
    yty=weights@(yy*yy).reshape(p,6).sum(1)
    designs=[np.column_stack([np.ones(len(x)),x])]
    designs += [np.column_stack([np.ones(len(x)),x,np.maximum(x-b,0)]) for b in DOSES[1:-1]]
    sse=[]
    for design in designs:
        d=design.shape[1]
        xm=(design*good[:,None]).reshape(p,6,d)
        gram=np.einsum('pni,pnj->pij',xm,xm)
        rhs=np.einsum('pni,pn->pi',xm,yy.reshape(p,6))
        gram=np.einsum('bp,pij->bij',weights,gram)
        rhs=weights@rhs
        rank=np.linalg.matrix_rank(gram)
        beta=np.einsum('bij,bj->bi',np.linalg.pinv(gram),rhs)
        residual=yty-np.einsum('bi,bi->b',rhs,beta)
        residual[(rank<d)|(n<=d+1)|(residual<=0)]=np.nan
        sse.append(residual)
    hinges=np.stack(sse[1:],axis=1)
    safe=np.where(np.isfinite(hinges),hinges,np.inf)
    selected=safe.argmin(1)
    best=safe[np.arange(len(weights)),selected]
    best[~np.isfinite(best)]=np.nan
    with np.errstate(divide='ignore',invalid='ignore'):
        delta=n*np.log(sse[0]/best)-2*np.log(n)
    breakpoint=DOSES[1:-1][selected]
    breakpoint[~np.isfinite(delta)]=np.nan
    return delta,breakpoint

def prepare(records,cfg):
    ids=sorted({r['prompt_id'] for r in records})
    index={p:i for i,p in enumerate(ids)}
    assert len(ids)==80,'Confirmatory/bootstrap datasets must contain exactly 80 prompts'
    keys=[(r['prompt_id'],r['condition'],r['direction'],r['alpha_index']) for r in records]
    assert len(keys)==len(set(keys)),'Duplicate raw cells'
    constants={}
    for field in ['eh','lhp']:
        v=np.array([r[field] for r in records if r[field] is not None],float)
        constants[field]={'mean':float(v.mean()) if len(v) else None,'sd':float(v.std(ddof=0)) if len(v) else None,'unique_cell_count':len(v)}
    arrays={(c,d):{f:np.full((len(ids),6),np.nan) for f in FIELDS} for c in CONDITIONS for d in DIRECTIONS}
    ppls={(c,d):np.full((len(ids),6),np.nan) for c in CONDITIONS for d in DIRECTIONS}
    for row in records:
        ds=DIRECTIONS if row['direction']=='none' else [row['direction']]
        i,j=index[row['prompt_id']],row['alpha_index']
        assert np.isclose(row['normalized_alpha'],DOSES[j])
        for direction in ds:
            a=arrays[(row['condition'],direction)]
            for f in FIELDS:
                a[f][i,j]=np.nan if row[f] is None else row[f]
            if row['n_tokens']<8:
                a['leak_timecourse'][i,j]=np.nan
            ppls[(row['condition'],direction)][i,j]=row['ppl_ratio'] if row['ppl_ratio'] is not None else np.nan
    gate_fields=set(cfg['analysis']['coherence_gate_applies_to'])
    allowed=set(FIELDS)|{'leak_lexical','offchannel','S2_eh_component','S5_eh_component'}
    assert gate_fields<=allowed, f'Unknown coherence-gated measures: {gate_fields-allowed}'
    excluded=[]
    for key,a in arrays.items():
        for component in ['S2_eh_component','S5_eh_component']:
            a[component]=a['eh'].copy()
        for j,dose in enumerate(DOSES):
            finite_ppl=ppls[key][:,j][np.isfinite(ppls[key][:,j])]
            median=float(np.median(finite_ppl)) if len(finite_ppl) else None
            if median is not None and median>cfg['analysis']['coherence_gate_ppl_ratio']:
                excluded.append({'condition':key[0],'direction':key[1],'normalized_alpha':float(dose),'median_ppl_ratio':median})
                for f in gate_fields:
                    if f in a:a[f][:,j]=np.nan
        for f in ['eh','lhp','S2_eh_component','S5_eh_component']:
            source='eh' if f.endswith('_eh_component') else f
            center,sd=constants[source]['mean'],constants[source]['sd']
            a[f+'_z']=(a[f]-center)/sd if sd is not None and sd>0 else np.full_like(a[f],np.nan)
    return ids,arrays,constants,excluded

def analyze_model(records,cfg):
    ids,arrays,constants,excluded=prepare(records,cfg)
    b=cfg['analysis']['bootstrap_resamples']
    rng=np.random.default_rng(cfg['analysis']['bootstrap_seed'])
    draws=rng.integers(0,len(ids),size=(b,len(ids)))
    weights=np.zeros((b+1,len(ids)));weights[0]=1
    np.add.at(weights,(np.arange(1,b+1)[:,None],draws),1)
    slopes={d:{c:{f:slope(arrays[(c,d)][f],weights) for f in ['lhp','lhp_z','eh_z','S2_eh_component_z','entropy','ew']} for c in CONDITIONS} for d in DIRECTIONS}
    carries={d:mean_stat(arrays[('warm_constraint',d)]['carryover'][:,-1],weights) for d in DIRECTIONS}
    outcomes={};controls={}
    primary_level=cfg['analysis']['primary_ci'];secondary_level=cfg['analysis']['secondary_ci']
    for h,sign,values in [('P1',1,{d:slopes[d]['warm_constraint']['lhp_z'] for d in DIRECTIONS}),('P2',-1,carries)]:
        controls[h]={}
        statistics={'hostility':summary(values['hostility'],primary_level)}
        for d in DIRECTIONS[1:]:
            # P2 contrasts are paired by prompt (missing excluded pairwise).
            difference=values['hostility']-values[d] if h=='P1' else mean_stat(arrays[('warm_constraint','hostility')]['carryover'][:,-1]-arrays[('warm_constraint',d)]['carryover'][:,-1],weights)
            controls[h][d]={'control':summary(values[d],primary_level),'hostility_minus_control':summary(difference,primary_level),'met':interval(difference,sign,primary_level)}
            statistics['hostility_minus_'+d]=controls[h][d]['hostility_minus_control']
        estimable=all(s['estimate'] is not None and s['ci'][0] is not None for s in statistics.values())
        criterion=interval(values['hostility'],sign,primary_level)
        specific=all(c['met'] for c in controls[h].values())
        support=estimable and criterion and specific
        outcomes[h]={'verdict':'not estimable' if not estimable else 'supported' if support else 'not supported','supported':bool(support),'estimable':bool(estimable),'criterion_met':criterion,'specificity_met':specific,'required_gate_exclusions':[],'statistics':statistics}
    warm=arrays[('warm_constraint','hostility')];neutral=arrays[('neutral','hostility')]
    dw=ratio(slopes['hostility']['warm_constraint']['S2_eh_component_z'],slopes['hostility']['warm_constraint']['lhp_z'])
    dn=ratio(slopes['hostility']['neutral']['S2_eh_component_z'],slopes['hostility']['neutral']['lhp_z'])
    paired=warm['carryover'][:,-1]-neutral['carryover'][:,-1]
    high=prompt_mean(warm['leak_timecourse'][:,3:])
    secondary={'S1':(mean_stat(paired,weights),-1),'S2':(dw-dn,-1),'S3':(mean_stat(high,weights),1),'S4':(slopes['hostility']['warm_constraint']['entropy']-slopes['hostility']['neutral']['entropy'],1)}
    for h,(v,sign) in secondary.items():
        stat=summary(v,secondary_level);estimable=stat['estimate'] is not None and stat['ci'][0] is not None
        supported=interval(v,sign,secondary_level)
        outcomes[h]={'verdict':'not estimable' if not estimable else 'supported' if supported else 'not supported','supported':supported,'estimable':estimable,'statistics':{h:stat}}
    g=(warm['lhp_z']-warm['lhp_z'][:,[0]])-(warm['S5_eh_component_z']-warm['S5_eh_component_z'][:,[0]])
    delta,breakpoints=bic_gap(g,weights)
    valid=delta[1:][np.isfinite(delta[1:])]
    estimable=bool(np.isfinite(delta[0]));supported=bool(estimable and delta[0]>cfg['analysis']['breakpoint_delta_bic'])
    outcomes['S5']={'verdict':'not estimable' if not estimable else 'supported' if supported else 'not supported','supported':supported,'estimable':estimable,'statistics':{'delta_bic':{**summary(delta,secondary_level),'selected_breakpoint':finite(breakpoints[0]),'bootstrap_share_delta_bic_gt_6':float(np.mean(valid>6)) if len(valid) else None}}}
    missing={}
    for (condition,direction),a in arrays.items():
        missing[condition+'|'+direction]={f:{'missing_observations':int((~np.isfinite(v)).sum()),'observed_by_dose':np.isfinite(v).sum(0).tolist(),'prompts_without_observations':int((~np.isfinite(v).any(1)).sum())} for f,v in a.items()}
    paired_missing={'S1_missing_prompt_pairs':int((~np.isfinite(paired)).sum()),'S3_missing_prompt_means':int((~np.isfinite(high)).sum()),'S5_missing_gap_observations':int((~np.isfinite(g)).sum()),'P2_control_missing_prompt_pairs':{d:int((~np.isfinite(warm['carryover'][:,-1]-arrays[('warm_constraint',d)]['carryover'][:,-1])).sum()) for d in DIRECTIONS[1:]}}
    groups={}
    for r in records:groups.setdefault(f"{r['condition']}|{r['direction']}|{r['normalized_alpha']}",[]).append(r)
    descriptions={}
    for key,group in groups.items():
        row=group[0]
        gated=any(e['condition']==row['condition'] and (row['direction']=='none' or e['direction']==row['direction']) and e['normalized_alpha']==row['normalized_alpha'] for e in excluded)
        gate_fields=set(cfg['analysis']['coherence_gate_applies_to'])
        lex_gated=gated and 'leak_lexical' in gate_fields
        off_gated=gated and 'offchannel' in gate_fields
        lex=[r['leak_lexical'] for r in group if not lex_gated and r['leak_lexical'] is not None]
        descriptions[key]={'n':len(group),'lexical_eligible':len(lex),'mean_lexical_hits':float(np.mean(lex)) if lex else None,'lexical_coherence_excluded':lex_gated,'offchannel_coherence_excluded':off_gated,'emoji_total':None if off_gated else sum(r['offchannel']['emoji_count'] for r in group),'non_latin_token_total':None if off_gated else sum(r['offchannel']['non_latin_token_count'] for r in group)}
    ew=slopes['hostility']['warm_constraint']['ew']
    return {'model':records[0]['model'],'prompt_count':len(ids),'unique_raw_cells':len(records),'standardization':constants,'coherence_threshold':cfg['analysis']['coherence_gate_ppl_ratio'],'coherence_gate_applies_to':cfg['analysis']['coherence_gate_applies_to'],'excluded_cells':excluded,'outcomes':outcomes,'specificity':controls,'missingness':missing,'paired_missingness':paired_missing,'component_slopes':{d:{c:{f:summary(v,primary_level if f=='lhp_z' and c=='warm_constraint' else secondary_level) for f,v in fields.items()} for c,fields in conditions.items()} for d,conditions in slopes.items()},'dissociation_components':{'warm':summary(dw),'neutral':summary(dn)},'exploratory':{'label':'Exploratory only; not confirmatory','warmth_slope':summary(ew),'warmth_hostility_minus_control':{d:summary(ew-slopes[d]['warm_constraint']['ew']) for d in DIRECTIONS[1:]},'all_raw_group_summaries':descriptions}}

def generality(models,statuses):
    by_id={m['model']:m for m in models};out={}
    for h in ['P1','P2']:
        passed=[m for m,s in statuses.items() if s=='PASS']
        unresolved=[m for m in passed if m not in by_id]
        eligible=[m for m in passed if m in by_id and by_id[m]['outcomes'][h]['estimable']]
        not_estimable=[m for m in passed if m in by_id and not by_id[m]['outcomes'][h]['estimable']]
        supported=not unresolved and len(eligible)>=2 and all(by_id[m]['outcomes'][h]['supported'] for m in eligible)
        verdict='general' if supported else 'pending model data' if unresolved else 'no generality claim (fewer than two estimable models)' if len(eligible)<2 else 'not general'
        out[h]={'verdict':verdict,'general':supported,'eligible_models':eligible,'not_estimable_models':not_estimable,'missing_passed_models':unresolved,'model_statuses':statuses}
    return out

def analyze(records,cfg,statuses=None):
    for r in records:validate(r)
    models=[analyze_model([r for r in records if r['model']==m],cfg) for m in sorted({r['model'] for r in records})]
    if statuses is None:statuses={m['model']:'PASS' for m in models}
    return {'prereg_version':cfg['experiment']['prereg_version'],'bootstrap_resamples':cfg['analysis']['bootstrap_resamples'],'bootstrap_seed':cfg['analysis']['bootstrap_seed'],'models':models,'generality':generality(models,statuses)}

def report(result):
    lines=['# Study 2 preregistered analysis','']
    for m in result['models']:
        lines += [f"## {m['model']}",'',f"{m['prompt_count']} prompts; {m['unique_raw_cells']} unique saved cells.",'','| Hypothesis/statistic | Estimate | CI level | Percentile CI | Verdict |','|---|---:|---:|---|---|']
        for h,o in m['outcomes'].items():
            for name,s in o['statistics'].items():lines.append(f"| {h}: {name} | {s['estimate']} | {100*s['confidence_level']:.1f}% | {s['ci']} | {o['verdict']} |")
        lines+=['','Coherence exclusions: '+json.dumps(m['excluded_cells']), '', 'All component estimates, control intervals, missingness counts, and labeled exploratory results are retained in the accompanying JSON.']
    lines+=['','## Generality','',json.dumps(result['generality'],indent=2)]
    return '\n'.join(lines)+'\n'

def main():
    from .common import calibration_paths,verify_manifest
    parser=argparse.ArgumentParser();parser.add_argument('--input',required=True,nargs='+');parser.add_argument('--output',required=True);args=parser.parse_args()
    cfg=yaml.safe_load(Path('config.yaml').read_text())
    records=[json.loads(s) for p in args.input for s in Path(p).read_text().splitlines()]
    statuses={}
    for spec in cfg['models']:
        path,manifest=calibration_paths(spec,cfg)
        if path.exists():verify_manifest(manifest);statuses[spec['id']]=json.loads(path.read_text())['status']
        else:statuses[spec['id']]='unavailable / no calibration'
    assert all(statuses[r['model']]=='PASS' for r in records),'Only manipulation-passing model data analyzed'
    result=analyze(records,cfg,statuses)
    prefix=Path(args.output);prefix.parent.mkdir(parents=True,exist_ok=True)
    with Path(str(prefix)+'.json').open('x') as f:json.dump(result,f,indent=2,allow_nan=False)
    with Path(str(prefix)+'.md').open('x') as f:f.write(report(result))
    print(json.dumps(result['generality']),flush=True)
if __name__=='__main__':main()
