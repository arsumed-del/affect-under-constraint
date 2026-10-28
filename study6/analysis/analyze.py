"""Joint prompt-cluster inference for the preregistered answer-token interventions."""
import argparse
import json
import numpy as np
from study6.src.common import ROOT, SOURCES, CONDITIONS, config, verified_rows, input_path, save, output_path, verify_inputs
from study6.src.validity import mass_report
from study5.analysis.analyze import conjunction


def definitions():
    """Coefficients refer to (study/arm, source); placement is applied separately."""
    U=('study5','unsteered'); H=('study5','hostility'); h=('clamp','hostility')
    d={'TE':{H:1,U:-1},'D_U':{h:1,U:-1},'M^X':{H:1,h:-1},
       'S':{('swap','unsteered'):1,U:-1},
       'interaction':{H:1,h:-1,('swap','unsteered'):-1,U:1}}
    for label,source in [('T','technicality'),('Q','random')]:
        d['D_'+label]={h:1,('clamp',source):-1}
        d['replacement_'+label]={('study5',source):1,('clamp',source):-1}
        d['M_'+label]={H:1,h:-1,('study5',source):-1,('clamp',source):1}
    for label,source in [('U','unsteered'),('T','technicality'),('Q','random')]:
        d['G_D_'+label]={('generic','hostility'):1,('generic',source):-1}
    return d


def summarize(values,samples,level,kind='two-sided'):
    available=int(np.isfinite(values).sum())
    if not len(values) or available!=len(values) or not np.isfinite(samples).all():
        return {'status':'not estimable','n_required':len(values),'n_available':available,
                'supported':False,'negligible':False,'reversed':False}
    lo,hi=np.quantile(samples,[(1-level)/2,(1+level)/2]); elo,ehi=np.quantile(samples,[.05,.95])
    negative=bool(hi<0); positive=bool(lo>0); negligible=bool(elo>-.15 and ehi<.15)
    supported=(negative or positive) if kind=='two-sided' else negative
    reversed_=kind=='negative' and positive
    status=('small but detectable' if supported and negligible else 'supported' if supported else
            'reversed' if reversed_ else 'negligible' if negligible else 'inconclusive')
    return {'estimate':float(np.mean(values)),'ci_level':level,'ci':[float(lo),float(hi)],
            'equivalence_ci_level':.9,'equivalence_ci':[float(elo),float(ehi)],'n':len(values),
            'supported':supported,'negligible':negligible,'reversed':reversed_,
            'negative':negative,'positive':positive,'status':status}


def reading(d,m,mixed=False):
    if d['status']=='not estimable' or m['status']=='not estimable': text='Not estimable: required cells or eligible prompts missing.'
    elif d['reversed']: text='Under the fixed answer the hostility trace raises the rating; reported as reversal.'
    elif d['supported'] and d['negligible']: text='Small but detectable influence under the clamp; report magnitude and direction.'
    elif d['supported'] and m['negligible']: text='The effect persists under this clamp; replacing the answer changes it by less than the margin.'
    elif (d['supported'] or d['negligible']) and m['supported'] and m['positive']: text='The clamp amplifies the effect (the hostility answer had offset part of it).'
    elif d['supported'] and m['supported'] and m['negative']: text='The clamp attenuates the effect, with residual influence under the fixed answer.'
    elif d['negligible'] and m['supported'] and m['negative']: text='The clamp reduces the effect to within the margin; the recorded answers carried most of the total effect for these stimuli.'
    elif d['negligible'] and m['negligible']: text='Both contrasts are within the margin; negligible does not mean absent.'
    else: text='Unresolved at this sample.'
    if mixed: text+=' Mixed control-relative effects.'
    return text


def indexed(data, original=False):
    lookup={}
    for r in data:
        arm='study5' if original else r['arm']
        if arm=='sham': continue
        k=(r['prompt_id'],r['condition'],arm,r['source'])
        if k in lookup: raise ValueError(f'Duplicate analysis cell {k}')
        lookup[k]=r
    return lookup


def analyze(originals,data,cfg,ids,audit=None,dropped=()):
    """One global draw matrix, also shared by every sensitivity statistic.

    Missing required cells make the affected estimand nonestimable, as in Study 5.
    Subsets reuse the same master uniform draws, resampling exactly their retained n clusters.
    """
    lookup=indexed(originals,True); lookup.update(indexed(data))
    ids=list(ids)
    if len(ids)!=len(set(ids)): raise ValueError('Duplicate prompt IDs')
    n=len(ids); B=cfg['analysis']['resamples']
    uniforms=np.random.default_rng(cfg['bootstrap_seed']).random((B,n))
    draws=(uniforms*n).astype(int)
    draw_cache={}
    definitions_=definitions(); primary_ci=1-.05/3
    def get(p,c,arm,s): return lookup.get((p,c,arm,s))
    natural={p for p in ids if all(get(p,c,'study5',s) is not None and not get(p,c,'study5',s)['forced_closure'] for c in CONDITIONS for s in SOURCES)}
    e5=None if audit is None or any(p not in audit for p in ids) else {p for p in ids if not (audit[p]['instructions'] or audit[p]['negative_characterizations'])}

    def eligible(p,c,name,subset):
        if subset=='natural_closure': return p in natural
        if subset=='E5': return e5 is not None and p in e5
        if subset=='completed_answer':
            sources=['unsteered']
            if name in ('M^X','M_T','M_Q','replacement_T','replacement_Q','S','interaction','TE'): sources+=['hostility']
            return all(get(p,c,'study5',s) is not None and not get(p,c,'study5',s)['answer_truncated'] for s in sources)
        return True

    def core(subset):
        out={'placements':{},'label':'Primary analysis' if subset=='all' else 'Descriptive sensitivity; paired prompt clusters retained'}
        for c in CONDITIONS:
            if c in dropped:
                out['placements'][c]={'status':'dropped','reason':'Valid-digit mass below 0.8 in at least one source group'}; continue
            if subset=='E5' and e5 is None:
                out['placements'][c]={'status':'not estimable','reason':'E5 audit missing or incomplete'}; continue
            estimates={}; samples={}; arrays={}; masks={}
            for name,terms in definitions_.items():
                if name.startswith('G_') and c not in ('R1','R3'): continue
                mask=np.array([eligible(p,c,name,subset) for p in ids],bool); masks[name]=mask
                vals=np.full(n,np.nan)
                for i,p in enumerate(ids):
                    if not mask[i]: continue
                    values=[]
                    for (arm,s),weight in terms.items():
                        r=get(p,c,arm,s)
                        value=None if r is None else r.get('ratings',{}).get('sender',{}).get('expected')
                        if value is None or not np.isfinite(value): break
                        values.append(weight*value)
                    else: vals[i]=sum(values)
                # D_U + M^X is the shared-baseline TE, up to floating point roundoff.
                arrays[name]=vals
                mask_key=mask.tobytes()
                if mask_key not in draw_cache:
                    retained=np.flatnonzero(mask); size=len(retained)
                    draw_cache[mask_key]=retained[(uniforms[:,:size]*size).astype(int)] if size else np.empty((B,0),int)
                selected_draws=draw_cache[mask_key]
                boot=vals[selected_draws].mean(axis=1) if selected_draws.shape[1] else np.full(B,np.nan)
                samples[name]=boot
                level=primary_ci if (c in ('R1','R3') and name in ('D_U','D_T','D_Q')) or (c=='R1' and name=='M^X') else .95
                kind='negative' if name.startswith(('D_','G_D_')) or name in ('TE','S') else 'two-sided'
                estimates[name]=summarize(vals[mask],boot,level,kind)
                estimates[name]['inference']=('primary' if level==primary_ci else 'exploratory, 95% unadjusted' if name=='interaction' and c not in ('R1','R3') else 'descriptive specificity/baseline, 95% unadjusted' if name in ('TE','M_T','M_Q','replacement_T','replacement_Q') else 'secondary, 95% unadjusted')
            d=conjunction([estimates[k] for k in ('D_U','D_T','D_Q')])
            if 'G_D_U' in estimates: generic=conjunction([estimates[k] for k in ('G_D_U','G_D_T','G_D_Q')])
            else: generic=None
            mt,mq=estimates['M_T'],estimates['M_Q']
            mixed=bool(mt.get('estimate',0)*mq.get('estimate',0)<0)
            proportion={'status':'not reported','rule':'TE supported; >=97.5% of bootstrap denominators strictly on the point-estimate side of zero; no clipping'}
            te=estimates['TE']; mx=estimates['M^X']
            if te['supported'] and mx['status']!='not estimable' and np.array_equal(masks['TE'],masks['M^X']):
                same=float(np.mean(samples['TE']*te['estimate']>0)); proportion['denominator_same_sign_fraction']=same
                if same>=.975 and np.all(samples['TE']!=0):
                    ratio=samples['M^X']/samples['TE']
                    proportion.update(status='descriptive',estimate=mx['estimate']/te['estimate'],ci_level=.95,ci=np.quantile(ratio,[.025,.975]).tolist())
            # Cancellation audit only where all three share the same eligible prompt mask.
            mask=masks['TE'] & masks['D_U'] & masks['M^X']
            err=arrays['TE'][mask]-(arrays['D_U'][mask]+arrays['M^X'][mask])
            finite=err[np.isfinite(err)]
            if finite.size and not np.allclose(finite,0,atol=1e-12,rtol=0): raise AssertionError('Shared-baseline identity failed')
            out['placements'][c]={'estimands':estimates,'D':d,'generic_D':generic,
                 'M_control_label':'mixed control-relative effects' if mixed else 'control-relative effects not mixed',
                 'reading':reading(d,mx,mixed),'proportion':proportion,
                 'identity_max_abs_error':float(np.max(np.abs(finite))) if finite.size else None,
                 'n_by_estimand':{k:int(v.sum()) for k,v in masks.items()}}
        return out
    result={'primary_ci':primary_ci,'secondary_ci':.95,'bootstrap_seed':cfg['bootstrap_seed'],
            'bootstrap_resamples':B,'bootstrap_draws_sha256':__import__('hashlib').sha256(draws.tobytes()).hexdigest(),
            'prompt_ids':ids,'missing_policy':cfg['analysis']['missing_policy'],
            'dropped_placements':list(dropped),'primary':core('all'),
            'sensitivity':{name:core(name) for name in ('completed_answer','natural_closure','E5')},
            'descriptive':descriptive(data)}
    result['hypotheses']={}
    for h,c in [('D1','R1'),('D2','R3'),('M1','R1')]:
        entry=result['primary']['placements'][c]
        result['hypotheses'][h]=entry.get('D',{'status':entry.get('status')}) if h!='M1' else entry.get('estimands',{}).get('M^X',{'status':entry.get('status')})
    return result


def descriptive(data):
    output={}
    for arm in ('clamp','swap','generic'):
        for c in CONDITIONS:
            group=[r for r in data if r['arm']==arm and r['condition']==c]
            if not group: continue
            entry={'n':len(group)}
            for name in ('answer_length','answer_truncated','EH_answer'):
                values=[r[name] for r in group if r.get(name) is not None]
                entry[name]={'n':len(values),'mean':float(np.mean(values)) if values else None,'values':values}
            entry['expected_digit_distribution']=[r['ratings']['sender']['expected'] for r in group]
            entry['mean_digit_probabilities']={d:float(np.mean([r['ratings']['sender']['probabilities'][d] for r in group])) for d in '0123456789'}
            output[arm+'/'+c]=entry
    return output


def report(result):
    lines=['# Study 6 answer-token intervention analysis','',
           'Conditional on the recorded Study 4 stimuli and Study 5 answers. Uncertainty is across prompts, not generation seeds; this is not an independent replication.',
           '', 'D1 (R1), D2 (R3), and M1 (R1 M^X) use the exact primary CI level 1 − 0.05/3. Other intervals are 95%, unadjusted. Equivalence uses 90% intervals inside ±0.15, descriptively and outside familywise control.',
           '', 'The stored Study 5 unsteered rating is the shared baseline. TE = D_U + M^X. M_T = M^X − replacement_T and M_Q = M^X − replacement_Q; both bracketed terms are listed. Generic effects compare sources under G, including the generic U baseline.',
           '', '| Primary hypothesis | Status |','|---|---|']
    for h,v in result['hypotheses'].items(): lines.append(f'| {h} | {v["status"]} |')
    for label,analysis in [('All prompts',result['primary']),*result['sensitivity'].items()]:
        lines+=['',f'## {label}','']
        for c,entry in analysis['placements'].items():
            lines += [f'### {c}','']
            if 'estimands' not in entry:
                lines += [entry['status']+': '+entry.get('reason',''),'']; continue
            lines += [entry['reading'],'', '| Estimand | n | Estimate | CI level | CI | 90% equivalence CI | Status |', '|---|---|---|---|---|---|---|']
            for name,v in entry['estimands'].items():
                lines.append(f'| {name} | {v.get("n",v.get("n_available",0))}/{entry["n_by_estimand"][name]} | {v.get("estimate","—")} | {v.get("ci_level","—")} | {v.get("ci","—")} | {v.get("equivalence_ci","—")} | {v["status"]} |')
            lines+=['', 'D conjunction: '+entry['D']['status']+'. '+entry['M_control_label']+'.',
                    'Generic D conjunction: '+(entry['generic_D']['status'] if entry['generic_D'] else 'not planned')+'.',
                    'Proportion (descriptive): '+json.dumps(entry['proportion']), '']
    lines+=['## Descriptive answer and rating summaries','',
            '| Arm/placement | n | Mean answer tokens | Truncated fraction | Mean stored EH | Mean expected digit |',
            '|---|---|---|---|---|---|']
    for k,v in result['descriptive'].items():
        lines.append(f'| {k} | {v["n"]} | {v["answer_length"]["mean"]} | {v["answer_truncated"]["mean"]} | {v["EH_answer"]["mean"]} | {np.mean(v["expected_digit_distribution"])} |')
    lines+=['','Interactions outside R1/R3 are exploratory. Full 0–9 digit probability distributions and observed expected ratings are in analysis.json. Generic EH is unavailable because G has no stored Study 5 classifier score. R2 contains visible assistant text. Between-placement claims require direct contrasts; none are inferred from differing significance. Negligible never means absent.']
    return '\n'.join(lines)+'\n'


def main():
    p=argparse.ArgumentParser(); p.add_argument('--input',default=str(ROOT/'data/main/cells.jsonl')); p.add_argument('--output',default=str(ROOT/'results/analysis.json')); args=p.parse_args()
    cfg=config(); verify_inputs(cfg)
    from study6.src.approval import require_approval,freeze_hashes
    from study6.src.runner import prepare
    from study6.src.validity import validate_rows,require_pilot
    from study6.src.assembly import plan
    from study6.src.common import digest
    from transformers import AutoTokenizer
    require_approval()
    tokenizer=AutoTokenizer.from_pretrained(ROOT/cfg['model']['local_path'],local_files_only=True)
    assembly,original,generic=prepare(cfg,'main',tokenizer)
    pa,po,pg=prepare(cfg,'pilot',tokenizer)
    pilot=require_pilot(cfg,freeze_hashes(),po,pa,pg)
    data=verified_rows(args.input)
    if any(r.get('mode')!='main' for r in data): raise ValueError('Analysis CLI accepts only main rows')
    # Missing rows remain explicit nonestimable components; duplicates/stale rows fail closed.
    validate_rows(data,set(plan(cfg['main_prompt_ids'],'main')),digest({'mode':'main','hashes':freeze_hashes()}),original,assembly,generic)
    mass=mass_report(data)
    dropped=sorted(set(mass['dropped_placements']) | set(pilot['mass']['dropped_placements']))
    result=analyze(list(original.values()),data,cfg,cfg['main_prompt_ids'],json.loads(input_path(cfg,'e5_audit').read_text()),dropped)
    result['validity']={'main':mass,'pilot':pilot}
    save(args.output,result)
    with output_path(args.output).with_suffix('.md').open('x') as f: f.write(report(result))
if __name__=='__main__': main()
