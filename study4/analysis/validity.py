"""Pilot engineering screens, never used to choose an effect-maximizing wrapper."""
import argparse
import json
import numpy as np
from study4.src.common import ROOT, config, rows, verified_rows, save, sha

def evaluate(data, reference, expected_ids):
    ids=set(expected_ids); present={(r['prompt_id'],r['source'],r['framing']) for r in data}
    from study4.src.common import SOURCES, FRAMINGS
    complete=present=={(p,s,f) for p in ids for s in SOURCES for f in FRAMINGS}
    segments=[]
    for p in ids:
        for s in SOURCES:
            rr=[r for r in data if r['prompt_id']==p and r['source']==s]
            segments.append(len(rr)==3 and all(r['fixed_segments']==rr[0]['fixed_segments'] and r['trace_ids']==rr[0]['trace_ids'] and r['answer_prefix_ids'][slice(*r['trace_bounds'])]==r['trace_ids'] for r in rr))
    native=[r['ratings']['sender']['expected'] for r in data if r['framing']=='own_native' and r['source']=='unsteered']
    agreement=abs(float(np.mean(native))-reference) if native else None
    targets={}
    for f in FRAMINGS:
        for t in ['sender'] if f=='own_native' else ['sender','writer','notes']:
            rr=[r for r in data if r['framing']==f and t in r['ratings']]
            baseline=[r['ratings'][t]['expected'] for r in rr if r['source']=='unsteered']
            mass=[r['ratings'][t]['valid_mass'] for r in rr]
            sd=float(np.std(baseline,ddof=1)) if len(baseline)>1 else None
            mean_mass=float(np.mean(mass)) if mass else None
            targets[f+'/'+t]={'baseline_SD':sd,'SD_pass':sd is not None and sd>=.15,'mean_valid_mass':mean_mass,'mass_pass':mean_mass is not None and mean_mass>=.8}
    return {'complete':complete,'fixed_segments_pass':all(segments),'native_baseline_mean':float(np.mean(native)) if native else None,'study3_reference':reference,'baseline_difference':agreement,'baseline_pass':agreement is not None and agreement<=.3,'targets':targets,'passed':complete and all(segments) and agreement is not None and agreement<=.3 and all(v['SD_pass'] and v['mass_pass'] for v in targets.values()),'policy':'At most two logged wrapper/question revisions using only these criteria; no automatic revisions or effect-size-based selection. Referent diagnostic remains required.'}

def main():
    p=argparse.ArgumentParser();p.add_argument('--input',required=True);p.add_argument('--output',required=True);a=p.parse_args()
    cfg=config(); prior=rows(ROOT/cfg['study3_raw']['path'])
    baseline=[r['R_text'] for r in prior if r['mode']=='think' and r['dose_fraction']==0]
    reference=float(np.mean(baseline))
    data=verified_rows(a.input)
    if any(r['mode']!='pilot' for r in data):raise ValueError('Validity screens require the full pilot, not short-cap smoke outputs')
    result=evaluate(data,reference,[r['id'] for r in rows(ROOT/cfg['prompts']['pilot'])])
    result['reference_provenance']={'source':cfg['study3_raw']['path'],'sha256':sha(ROOT/cfg['study3_raw']['path']),'n':len(baseline),'note':'Report has no explicit aggregate think-zero mean; computed transparently from the report source records, not guessed.'}
    save(a.output,result)
if __name__=='__main__':main()
