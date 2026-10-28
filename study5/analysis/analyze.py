"""Study 5 prompt-cluster inference; no Study 4 outcome pooling or coherence exclusions."""
import argparse
import json
import numpy as np
from study4.analysis.analyze import bootstrap
from study5.src.common import ROOT, SOURCES, CONDITIONS, CONTROLS, config, verified_rows, input_path, save

def add(a,b,weight=-1):
    out=dict(a)
    for k,v in b.items():out[k]=out.get(k,0)+weight*v
    return out

def contrasts():
    d={}
    for c in CONDITIONS:
        d[c+':X']={('hostility',c):1,('unsteered',c):-1}
        for ctrl in CONTROLS:d[c+':A_'+ctrl]={('hostility',c):1,(ctrl,c):-1}
    for h,a,b in [('P3','R3','R2'),('S3','R1-M','R3'),('S4','R1','R1-M')]:
        for ctrl in CONTROLS:d[h+':'+ctrl]=add(d[a+':A_'+ctrl],d[b+':A_'+ctrl])
    return d

def hypotheses():
    d={h:[c+':X']+[c+':A_'+ctrl for ctrl in CONTROLS] for h,c in [('P1','R2'),('P2','R3'),('S1','R1'),('S2','R1-M'),('S5','R4')]}
    d.update({h:[h+':'+ctrl for ctrl in CONTROLS] for h in ['P3','S3','S4']})
    return d

def summarize(values,samples,level,kind='negative'):
    available=int(np.isfinite(values).sum())
    if not len(values) or available!=len(values):return {'status':'not estimable','n_required':len(values),'n_available':available,'supported':False,'negligible':False,'reversed':False}
    lo,hi=np.quantile(samples,[(1-level)/2,(1+level)/2]); elo,ehi=np.quantile(samples,[.05,.95])
    negative=bool(hi<0); positive=bool(lo>0); negligible=bool(elo>-.15 and ehi<.15)
    supported=(negative or positive) if kind=='two-sided' else negligible if kind=='equivalence' else negative
    reversed_=positive if kind=='negative' else False
    detectable=negative or positive
    status='small but detectable' if negligible and detectable else 'supported' if supported else 'reversed' if reversed_ else 'negligible' if negligible else 'inconclusive'
    return {'estimate':float(np.mean(values)),'ci_level':level,'ci':[float(lo),float(hi)],'equivalence_ci_level':.9,'equivalence_ci':[float(elo),float(ehi)],'n':len(values),'supported':supported,'negligible':negligible,'reversed':reversed_,'negative':negative,'positive':positive,'status':status}

def conjunction(parts,kind='negative'):
    estimable=bool(parts) and all(v['status']!='not estimable' for v in parts)
    support=estimable and all(v['supported'] for v in parts)
    negligible=estimable and all(v['negligible'] for v in parts)
    reversed_=estimable and all(v['reversed'] for v in parts)
    overlap=support and negligible and kind!='equivalence'
    return {'supported':support,'negligible':negligible,'reversed':reversed_,
            'status':'not estimable' if not estimable else 'small but detectable' if overlap else 'supported' if support else 'reversed' if reversed_ else 'negligible' if negligible else 'inconclusive'}

def reading(h):
    if not all(h[k]['supported'] for k in ['S1','S2']):return 'Historical nulls uninterpretable: S1 and S2 are not both supported.'
    p1,p2,p3=h['P1'],h['P2'],h['P3']
    if any(h[k]['supported'] and h[k]['negligible'] for k in ['P1','P2']):
        return 'Small but detectable historical influence overlaps equivalence; report direction and magnitude separately, without an exclusive placement reading.'
    if p1['supported'] and p2['supported']:return 'Both historical placements retain influence. Direct P3 contrast: '+p3['status']+'.'
    if p1['negligible'] and p2['supported'] and p3['supported']:return 'Retained historical thinking retains influence; visible historical reply is negligible; direct channel contrast supported.'
    if p1['supported'] and p2['negligible'] and p3['reversed']:return 'Visible historical reply retains influence; retained thinking is negligible; direct channel contrast reversed.'
    if p1['negligible'] and p2['negligible']:
        return 'Both historical placements are negligible; '+('S3 supports a drop from matched current thinking to retained historical thinking under these framings.' if h['S3']['supported'] else 'S3 does not establish a current-versus-historical thinking drop.')
    return 'Placement interpretation inconclusive; comparative claims require direct P3 or S3 evidence.'

def core(data,cfg,ids):
    lookup={}
    for r in data:
        k=(r['prompt_id'],r['source'],r['condition'])
        if k in lookup:raise ValueError(f'Duplicate cell {k}')
        lookup[k]=r
    defs=contrasts(); matrix=np.full((len(ids),len(defs)),np.nan)
    for j,terms in enumerate(defs.values()):
        for i,pid in enumerate(ids):
            value=0.
            for (source,c),weight in terms.items():
                v=lookup.get((pid,source,c),{}).get('ratings',{}).get('sender',{}).get('expected')
                if v is None or not np.isfinite(v):break
                value+=weight*v
            else:matrix[i,j]=value
    samples=bootstrap(matrix,cfg['analysis']['resamples'],cfg['seeds']['bootstrap'])
    names=list(defs); estimates={}; tests={}; hs={}
    for j,name in enumerate(names):estimates[name]=summarize(matrix[:,j],samples[:,j],.95,'two-sided')
    for h,components in hypotheses().items():
        level=cfg['analysis']['primary_ci'] if h.startswith('P') else .95
        kind='two-sided' if h=='S4' else 'equivalence' if h=='S5' else 'negative'
        tests[h]={name:summarize(matrix[:,names.index(name)],samples[:,names.index(name)],level,kind) for name in components}
        hs[h]=conjunction(list(tests[h].values()),kind)
    return {'prompt_ids':ids,'n':len(ids),'estimands':estimates,'tests':tests,'hypotheses':hs,'reading':reading(hs),'missing_policy':cfg['analysis']['missing_policy'],'bootstrap_resamples':cfg['analysis']['resamples']}

def diagnostic_summary(data):
    output={}
    for c in CONDITIONS:
        for source in SOURCES:
            group=[r for r in data if r['condition']==c and r['source']==source]
            def mean(key):
                vals=[r.get(key) for r in group]; vals=[v for v in vals if v is not None]
                return {'n':len(vals),'mean':float(np.mean(vals)) if vals else None}
            base=[r['ratings']['sender']['expected'] for r in group if r['source']=='unsteered']
            entry={'EH_answer':mean('EH_answer'),'answer_length':mean('answer_length'),'answer_truncated':mean('answer_truncated'),
                   'valid_digit_mass': [r['ratings']['sender']['valid_mass'] for r in group],
                   'baseline_mean':float(np.mean(base)) if base else None,'baseline_sd':float(np.std(base,ddof=1)) if len(base)>1 else None}
            for q in ['structural','source']:
                correct=('A' if c=='R2' else 'C' if c=='R4' else 'B') if q=='structural' else 'A'
                swap={'A':'B','B':'A','C':'C'}[correct]
                records=[]
                for r in group:
                    checks=r.get('checks',{})
                    if q not in checks or q+'_swap' not in checks:continue
                    a,b=checks[q],checks[q+'_swap']
                    # Report mapped categories as well as target probability.
                    mapped={label:(a['probabilities'][label]+b['probabilities'][{'A':'B','B':'A','C':'C'}[label]])/2 for label in a['probabilities']}
                    records.append({'prompt_id':r['prompt_id'],'order_averaged_probabilities':mapped,'correct_probability':mapped[correct],
                                    'correct_argmax':max(mapped,key=mapped.get)==correct,'valid_mass':[a['valid_mass'],b['valid_mass']]})
                entry[q]={'n':len(records),'records':records,'mean_correct_probability':float(np.mean([v['correct_probability'] for v in records])) if records else None}
            output[c+'/'+source]=entry
    return output

def analyze(data,cfg,ids,audit=None):
    result={'primary':core(data,cfg,ids),'descriptive':diagnostic_summary(data),'sensitivity':{}}
    lookup={(r['prompt_id'],r['source'],r['condition']):r for r in data}
    natural=[p for p in ids if all((p,s,c) in lookup and not lookup[p,s,c]['forced_closure'] for s in SOURCES for c in CONDITIONS)]
    def subset(selected):
        out=core([r for r in data if r['prompt_id'] in selected],cfg,selected)
        out['label']='Descriptive sensitivity; complete prompt clusters retained, not confirmatory.'
        return out
    result['sensitivity']['natural_closure']=subset(natural)
    if audit is None or any(p not in audit for p in ids):result['sensitivity']['E5']={'status':'not estimable','reason':'Audit missing or incomplete'}
    else:
        selected=[p for p in ids if not(audit[p]['instructions'] or audit[p]['negative_characterizations'])]
        result['sensitivity']['E5']=subset(selected)
    return result

def report(result):
    primary=result['primary']
    lines=['# Study 5 placement analysis','',primary['reading'],'',
           'Within-stimulus placement comparisons, conditional on Study 4 traces; no pooling with Study 4. Answers may mediate rating differences.',
           '', '| Hypothesis | Status | Supported | Negligible | Reversed |',
           '|---|---|---|---|---|']
    for h in ['P1','P2','P3','S1','S2','S3','S4','S5']:
        v=primary['hypotheses'][h]
        lines.append(f'| {h} | {v["status"]} | {v["supported"]} | {v["negligible"]} | {v["reversed"]} |')
    lines+=['', '| Test/component | Estimate | CI level | CI | 90% equivalence CI | Status |',
            '|---|---|---|---|---|---|']
    for h,components in primary['tests'].items():
        for name,v in components.items():
            if 'estimate' not in v:
                lines.append(f'| {h}/{name} | — | — | — | — | not estimable |')
            else:
                fmt=lambda x:f'[{x[0]:.4f}, {x[1]:.4f}]'
                lines.append(f'| {h}/{name} | {v["estimate"]:.4f} | {100*v["ci_level"]:.2f}% | {fmt(v["ci"])} | {fmt(v["equivalence_ci"])} | {v["status"]} |')
    lines+=['','P1–P3 are primary; S1–S5 are secondary. Equivalence requires the entire 90% interval inside ±0.15. Directional and equivalence evidence can overlap. Descriptive diagnostics, answer hostility, natural-closure sensitivity and E5 sensitivity are in the companion JSON.']
    return '\n'.join(lines)+'\n'

def main():
    p=argparse.ArgumentParser();p.add_argument('--input',required=True);p.add_argument('--output',required=True);args=p.parse_args()
    cfg=config();data=verified_rows(args.input)
    if any(r.get('mode')!='main' for r in data):raise ValueError('Only main rows accepted; synthetic tests call analyze directly')
    from study5.src.common import verify_inputs
    verify_inputs(cfg)
    result=analyze(data,cfg,cfg['main_prompt_ids'],json.loads(input_path(cfg,'e5_audit').read_text()))
    save(args.output,result)
    from study5.src.common import output_path
    with output_path(args.output).with_suffix('.md').open('x') as f:f.write(report(result))
if __name__=='__main__':main()
