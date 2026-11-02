import argparse,json,math
import numpy as np
from scipy.stats import spearmanr
from .common import *
from .judge import valid_scores

def agreement(a,b):
    if len(a)!=len(b):raise ValueError('Agreement vectors differ in length')
    valid=[(x,y) for x,y in zip(a,b) if x is not None and y is not None and math.isfinite(x) and math.isfinite(y)]
    if len(valid)<2:return {'n':len(valid),'missing_pairs':len(a)-len(valid),'rho':None,'mean_absolute_difference':None,'passed':False}
    x,y=np.array(valid).T
    rho=float(spearmanr(x,y).statistic) if np.std(x)>0 and np.std(y)>0 else None
    mad=float(np.mean(np.abs(x-y)));gate=config()['judge_gate']
    return {'n':len(valid),'missing_pairs':len(a)-len(valid),'rho':rho,'mean_signed_difference':float(np.mean(x-y)),'mean_absolute_difference':mad,'passed':rho is not None and rho>=gate['agreement_rho_min'] and mad<=gate['agreement_mean_absolute_difference_max']}

def calibration_gate(judgments,labels,judge='gemma'):
    gate=config()['judge_gate'];scores={rid:valid_scores(row) for rid,row in judgments.items()}
    pairs={}
    for rid,l in labels.items():pairs.setdefault((l['type'],l['pair']),{})[l['role']]=scores.get(rid,{})
    separations=[];lengths=[];flattery=[]
    for (kind,_),pair in pairs.items():
        if kind=='content_matched':
            a,b=pair['warm'].get('a'),pair['cold'].get('a');separations.append(None if a is None or b is None else a-b)
        elif kind=='length':
            a,b=pair['short'].get('a'),pair['long'].get('a');lengths.append(None if a is None or b is None else abs(a-b))
        elif kind=='flattery':
            a,b=pair['flattery'],pair['polite_disagreement'];ok=all(r.get(k) is not None for r in (a,b) for k in 'ae');flattery.append(ok and a['a']<=b['a'] and a['e']<b['e'])
    complete=len(separations)==15 and len(lengths)==5 and all(x is not None for x in separations+lengths)
    sep=float(np.mean(separations)) if separations and all(x is not None for x in separations) else None
    length=float(np.mean(lengths)) if lengths and all(x is not None for x in lengths) else None
    count=sum(x is not None and x>0 for x in separations)
    masses=[judgments.get(rid,{}).get('items',{}).get(k,{}).get('digit_mass') for rid in labels for k in config()['judges'][judge]['items']]
    minimum=min(masses) if masses and all(m is not None and math.isfinite(m) for m in masses) else None
    return {'warm_higher_pairs':count,'mean_separation':sep,'mean_abs_length_difference':length,'flattery_joint_pass_pairs':sum(flattery),'minimum_digit_mass':minimum,'separation_threshold':gate['mean_separation_min'][judge],'passed':complete and count>=gate['warm_higher_pairs_min'] and sep>=gate['mean_separation_min'][judge] and length<=gate['mean_abs_length_difference_max'] and sum(flattery)>=gate['flattery_joint_pass_pairs_min'] and minimum is not None and minimum>=gate['digit_mass_min']}

def evaluate(d):
    c=config();cells=verified(d/'cells.jsonl','cell_key');traces=verified(d/'traces.jsonl','trace_key')
    expected=set(__import__('study8.src.runner',fromlist=['plan']).plan(prompts('pilot')))
    if {tuple(r['cell_key']) for r in cells}!=expected:raise RuntimeError('Incomplete pilot')
    judges={j:{r['id']:r for r in verified(d/f'judge_{j}.jsonl','id')} for j in ('gemma','llama')}
    labels=json.loads((ROOT/'calibration/calibration_labels.json').read_text())['labels']
    sample=json.loads((d/'agreement_sample.json').read_text());assert len(sample)==48
    inputs=json.loads((d/'judge_inputs.json').read_text())
    for j,rr in judges.items():
        selected=inputs if j=='gemma' else [r for r in inputs if r['id'] in sample]
        expected_inputs=rows(ROOT/'calibration/calibration_items.jsonl')+selected
        provenance=digest({'inputs':expected_inputs,'freeze_hashes':freeze_hashes(),'judge':j})
        if set(rr)!={r['id'] for r in expected_inputs}:raise RuntimeError('Incomplete judge output: '+j)
        if any(r['provenance']!=provenance for r in rr.values()):raise RuntimeError('Stale judge output: '+j)
    gates={j:calibration_gate(judges[j],labels,j) for j in judges}
    agree=agreement(*[[valid_scores(judges[j][i]).get('a') for i in sample] for j in judges])
    missing={j:{k:sum(valid_scores(row).get(k) is None for rid,row in rr.items() if rid not in labels) for k in c['judges'][j]['items']} for j,rr in judges.items()}
    mass={k:min(q['valid_mass'] for r in cells if r['context']==k for q in r['ratings'].values()) for k in CONTEXTS}
    ppl={f'{s}/{k}':[t['perplexity'] for t in traces if t['trace_key'][1:]==[s,k]] for s in SOURCES for k in CONTEXTS}
    med={k:float(np.median(v)) if len(v)==4 and all(x is not None and math.isfinite(x) for x in v) else None for k,v in ppl.items()}
    judge_pass=all(v['passed'] for v in gates.values()) and agree['passed']
    passed=judge_pass and all(v>=.8 for v in mass.values()) and all(v is not None and v<=6 for v in med.values())
    timing={name:sum(r['timings'].get(name,0) for r in cells) for name in set().union(*(r['timings'] for r in cells))}
    return {'passed':passed,'judge_gate_passed':judge_pass,'calibration':gates,'pilot_agreement':agree,'pilot_missing_items':missing,'minimum_digit_mass_by_context':mass,'median_trace_perplexity_by_source_context':med,'timing_totals_seconds':timing,'judge_seconds':{j:sum(r['seconds'] for r in rr.values()) for j,rr in judges.items()},'estimated_main_qwen_hours':sum(r['seconds'] for r in cells)*20/3600,'freeze_hashes':freeze_hashes(),'input_hashes':{p.name:sha(p) for p in [d/'cells.jsonl',d/'traces.jsonl',d/'judge_gemma.jsonl',d/'judge_llama.jsonl']},'failure_policy':'No automatic revision. Failure makes W not interpretable; O1 remains reportable. Main launcher requires passing pilot.'}
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--mode',choices=['pilot'],default='pilot');ap.parse_args()
    d=ROOT/'data/pilot';v=evaluate(d);ensure(d/'validity.json',v);print(json.dumps(v,indent=2))
if __name__=='__main__':main()
