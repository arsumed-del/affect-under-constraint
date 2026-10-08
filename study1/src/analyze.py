"""Preregistered Amendment 2.2 estimators. No fitting or tuning to test outcomes."""
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

def summary(values):
    valid=values[1:][np.isfinite(values[1:])]
    ci=np.quantile(valid,[.025,.975]).tolist() if len(valid) else [None,None]
    return {'estimate':finite(values[0]),'ci95':ci,'bootstrap_valid':len(valid),'bootstrap_missing':len(values)-1-len(valid)}

def interval(values,sign):
    ci=summary(values)['ci95']
    return bool(ci[0] is not None and (ci[0]>0 if sign>0 else ci[1]<0))

def includes_zero(values):
    ci=summary(values)['ci95']
    return bool(ci[0] is not None and ci[0]<=0<=ci[1])

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
    assert len(ids)==40,'Confirmatory/bootstrap datasets must contain exactly 40 prompts'
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
    excluded=[]
    for key,a in arrays.items():
        for j,dose in enumerate(DOSES):
            finite_ppl=ppls[key][:,j][np.isfinite(ppls[key][:,j])]
            median=float(np.median(finite_ppl)) if len(finite_ppl) else None
            if median is not None and median>cfg['analysis']['coherence_gate_ppl_ratio']:
                excluded.append({'condition':key[0],'direction':key[1],'normalized_alpha':float(dose),'median_ppl_ratio':median})
                for f in FIELDS:
                    a[f][:,j]=np.nan
        for f in ['eh','lhp']:
            center,sd=constants[f]['mean'],constants[f]['sd']
            a[f+'_z']=(a[f]-center)/sd if sd is not None and sd>0 else np.full_like(a[f],np.nan)
    return ids,arrays,constants,excluded

def analyze_model(records,cfg):
    ids,arrays,constants,excluded=prepare(records,cfg)
    b=cfg['analysis']['bootstrap_resamples']
    rng=np.random.default_rng(cfg['experiment']['seed'])
    draws=rng.integers(0,len(ids),size=(b,len(ids)))
    weights=np.zeros((b+1,len(ids)))
    weights[0]=1
    np.add.at(weights,(np.arange(1,b+1)[:,None],draws),1)
    stats={}
    missing={}
    component_slopes={}
    for d in DIRECTIONS:
        neutral,warm=arrays[('neutral',d)],arrays[('warm_constraint',d)]
        slopes={c:{f:slope(arrays[(c,d)][f],weights) for f in ['lhp','lhp_z','eh_z','entropy','ew']} for c in CONDITIONS}
        component_slopes[d]=slopes
        d_neutral=ratio(slopes['neutral']['eh_z'],slopes['neutral']['lhp_z'])
        d_warm=ratio(slopes['warm_constraint']['eh_z'],slopes['warm_constraint']['lhp_z'])
        h4=prompt_mean(warm['leak_timecourse'][:,3:])
        warm_carry=warm['carryover'][:,-1]
        carry_difference=warm_carry-neutral['carryover'][:,-1]
        stats[d]={'H1':slopes['warm_constraint']['lhp_z'],'H2':d_warm-d_neutral,'H3':slopes['warm_constraint']['entropy']-slopes['neutral']['entropy'],'H4':mean_stat(h4,weights),'H5_warm':mean_stat(warm_carry,weights),'H5_difference':mean_stat(carry_difference,weights)}
        missing[d]={
            'H1':{'observations':int((~np.isfinite(warm['lhp_z'])).sum()),'prompts':int((~np.isfinite(warm['lhp_z']).any(1)).sum())},
            'H2':{'measure_observations':sum(int((~np.isfinite(a[f])).sum()) for a in [neutral,warm] for f in ['eh_z','lhp_z'])},
            'H3':{'observations':sum(int((~np.isfinite(a['entropy'])).sum()) for a in [neutral,warm])},
            'H4':{'observations':int((~np.isfinite(warm['leak_timecourse'][:,3:])).sum()),'prompts':int((~np.isfinite(h4)).sum())},
            'H5_warm':{'prompts':int((~np.isfinite(warm_carry)).sum())},
            'H5_difference':{'prompt_pairs':int((~np.isfinite(carry_difference)).sum())}}
    # Control H2 is not evaluated when its H1 interval includes zero.
    h2_skipped={d:includes_zero(stats[d]['H1']) for d in DIRECTIONS[1:]}
    for d,skip in h2_skipped.items():
        if skip:
            stats[d]['H2']=np.full(b+1,np.nan)
    specificity={}
    signs={'H1':1,'H2':-1,'H3':1,'H4':1,'H5_warm':-1,'H5_difference':-1}
    for hypothesis,sign in signs.items():
        specificity[hypothesis]={}
        for d in DIRECTIONS[1:]:
            if hypothesis=='H2' and h2_skipped[d]:
                specificity[hypothesis][d]={'met':True,'reason':'control H1 CI includes zero; D not computed','control':None,'hostility_minus_control':None}
                continue
            difference=stats['hostility'][hypothesis]-stats[d][hypothesis]
            absent=includes_zero(stats[d][hypothesis])
            smaller=interval(difference,sign)
            specificity[hypothesis][d]={'met':absent or smaller,'reason':'control CI includes zero' if absent else 'difference in predicted direction' if smaller else 'specificity not established','control':summary(stats[d][hypothesis]),'hostility_minus_control':summary(difference)}
    outcomes={}
    for hypothesis in ['H1','H2','H3','H4','H5']:
        components=['H5_warm','H5_difference'] if hypothesis=='H5' else [hypothesis]
        criterion=all(interval(stats['hostility'][h],signs[h]) for h in components)
        specific=all(specificity[h][d]['met'] for h in components for d in DIRECTIONS[1:])
        prerequisite=hypothesis!='H2' or outcomes['H1']['supported']
        reasons=[]
        if not criterion: reasons.append('criterion failed or statistic not estimable')
        if not specific: reasons.append('specificity failed')
        if not prerequisite: reasons.append('H1 not supported; H2 not interpreted')
        outcomes[hypothesis]={'supported':bool(criterion and specific and prerequisite),'criterion_met':criterion,'specificity_met':specific,'reasons':reasons,'statistics':{h:{**summary(stats['hostility'][h]),'missing':missing['hostility'][h]} for h in components}}
    warm=arrays[('warm_constraint','hostility')]
    g=(warm['lhp_z']-warm['lhp_z'][:,[0]])-(warm['eh_z']-warm['eh_z'][:,[0]])
    delta,breakpoints=bic_gap(g,weights)
    valid=delta[1:][np.isfinite(delta[1:])]
    h6_criterion=bool(np.isfinite(delta[0]) and delta[0]>cfg['analysis']['breakpoint_delta_bic'])
    h6_reasons=[]
    if not h6_criterion: h6_reasons.append('delta BIC criterion failed or fit not estimable')
    if not outcomes['H1']['supported']: h6_reasons.append('H1 not supported; H6 not interpreted')
    outcomes['H6']={
        'supported':bool(h6_criterion and outcomes['H1']['supported']),
        'criterion_met':h6_criterion,'specificity_met':True,'reasons':h6_reasons,
        'statistics':{'delta_bic':{
            **summary(delta),'selected_breakpoint':finite(breakpoints[0]),
            'bootstrap_share_delta_bic_gt_6':float(np.mean(valid>6)) if len(valid) else None,
            'missing':{'observations':int((~np.isfinite(g)).sum()),'prompts':int((~np.isfinite(g).any(1)).sum())}
        }}
    }
    groups={}
    for r in records:
        key=f"{r['condition']}|{r['direction']}|{r['normalized_alpha']}"
        groups.setdefault(key,[]).append(r)
    exploratory_groups={}
    for key,group in groups.items():
        lex=[r['leak_lexical'] for r in group if r['leak_lexical'] is not None]
        lenses=np.array([r['layerwise_lhp'] for r in group],float)
        exploratory_groups[key]={'n':len(group),'lexical_eligible':len(lex),'mean_lexical_hits':float(np.mean(lex)) if lex else None,'emoji_total':sum(r['offchannel']['emoji_count'] for r in group),'non_latin_token_total':sum(r['offchannel']['non_latin_token_count'] for r in group),'layerwise_lhp_mean':lenses.mean(0).tolist()}
    ew=component_slopes['hostility']['warm_constraint']['ew']
    return {'model':records[0]['model'],'prompt_count':len(ids),'unique_raw_cells':len(records),'standardization':constants,'coherence_threshold':cfg['analysis']['coherence_gate_ppl_ratio'],'excluded_cells':excluded,'outcomes':outcomes,'specificity':specificity,'direction_statistics':{d:{h:{**summary(v),'missing':missing[d][h]} for h,v in hs.items()} for d,hs in stats.items()},'raw_lhp_slope':{d:summary(component_slopes[d]['warm_constraint']['lhp']) for d in DIRECTIONS},'exploratory':{'label':'Exploratory only; not confirmatory','warmth_slope':summary(ew),'warmth_hostility_minus_control':{d:summary(ew-component_slopes[d]['warm_constraint']['ew']) for d in DIRECTIONS[1:]},'all_raw_group_summaries':exploratory_groups}}

def analyze(records,cfg):
    for r in records: validate(r)
    return {'prereg_version':cfg['experiment']['prereg_version'],'bootstrap_resamples':cfg['analysis']['bootstrap_resamples'],'bootstrap_seed':cfg['experiment']['seed'],'models':[analyze_model([r for r in records if r['model']==m],cfg) for m in sorted({r['model'] for r in records})]}

def report(result):
    lines=['# Preregistered analysis output','']
    for m in result['models']:
        lines += [f'## {m["model"]}','',f'{m["prompt_count"]} prompts; {m["unique_raw_cells"]} unique saved cells. Primary coherence threshold: {m["coherence_threshold"]}.','', '| Hypothesis/statistic | Estimate | 95% CI | Verdict |','|---|---:|---|---|']
        for h,outcome in m['outcomes'].items():
            for component,s in outcome['statistics'].items():
                est='missing' if s['estimate'] is None else f'{s["estimate"]:.6g}'
                ci='missing' if s['ci95'][0] is None else f'[{s["ci95"][0]:.6g}, {s["ci95"][1]:.6g}]'
                lines.append(f'| {h}: {component} | {est} | {ci} | {"supported" if outcome["supported"] else "not supported"} |')
        for h,outcome in m['outcomes'].items():
            if outcome['reasons']:
                lines.append(f'\n{h}: '+ '; '.join(outcome['reasons'])+'.\n')
        lines += ['','## Specificity','', '| Statistic | Control | Met | Reason |','|---|---|---|---|']
        for h,controls in m['specificity'].items():
            for d,s in controls.items():
                lines.append(f'| {h} | {d} | {s["met"]} | {s["reason"]} |')
        lines += ['','## Coherence exclusions','',json.dumps(m['excluded_cells'],indent=2),'','All missing counts, control estimates, paired contrasts, exploratory warmth/lexical/off-channel summaries, and logit-lens trajectories are retained in the accompanying JSON. Exploratory outputs do not determine confirmatory verdicts.','']
    return '\n'.join(lines)

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--input',required=True)
    parser.add_argument('--output',required=True,help='Output prefix; files must not already exist')
    args=parser.parse_args()
    cfg=yaml.safe_load(Path('config.yaml').read_text())
    records=[json.loads(s) for s in Path(args.input).read_text().splitlines()]
    result=analyze(records,cfg)
    prefix=Path(args.output)
    prefix.parent.mkdir(parents=True,exist_ok=True)
    with Path(str(prefix)+'.json').open('x') as f: json.dump(result,f,indent=2,allow_nan=False)
    with Path(str(prefix)+'.md').open('x') as f: f.write(report(result))
    print(json.dumps({m['model']:{h:r['supported'] for h,r in m['outcomes'].items()} for m in result['models']}),flush=True)

if __name__=='__main__': main()
