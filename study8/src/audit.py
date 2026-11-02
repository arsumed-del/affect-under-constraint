"""Commit clean subset before the analysis process opens outcomes."""
import argparse,json
from .common import *
FIELDS=('negative_user','hostile_instruction','kindness_strategy','rating_reference')
def finalize(mode):
    d=ROOT/'data'/mode
    codes=json.loads((d/'audit_codes.json').read_text());mapping=json.loads((d/'audit_map.json').read_text())
    lookup={r['id']:r for r in codes}
    if len(lookup)!=len(codes) or set(lookup)!=set(mapping):raise ValueError('Audit must contain every trace exactly once')
    joined=[]
    for rid,row in lookup.items():
        if any(type(row.get(k)) is not bool for k in FIELDS):raise ValueError('Audit booleans missing')
        if not isinstance(row.get('notes'),str) or not isinstance(row.get('evidence'),dict):raise ValueError('Audit evidence/notes required')
        for k in FIELDS:
            if not isinstance(row['evidence'].get(k),str) or row[k] and not row['evidence'][k].strip():raise ValueError('Evidence required for positive flags')
        joined.append(dict(row,**mapping[rid]))
    clean=[]
    for p in prompts(mode):
        rr=[r for r in joined if r['trace_key'][0]==p['id'] and r['trace_key'][1]=='hostility']
        if len(rr)!=3:raise ValueError('Missing H contexts')
        if not any(r[k] for r in rr for k in FIELDS[:3]):clean.append(p['id'])
    result={'clean_prompt_ids':clean,'n_clean':len(clean),'underpowered':len(clean)<20,'codes_sha256':sha(d/'audit_codes.json'),'map_sha256':sha(d/'audit_map.json'),'traces_sha256':sha(d/'traces.jsonl'),'joined':joined,'outcomes_opened_by_this_process':False}
    ensure(d/'audit_receipt.json',result)
    print(json.dumps({'n_clean':len(clean),'underpowered':len(clean)<20,'receipt':str(d/'audit_receipt.json')}))
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--mode',choices=['pilot','main'],required=True);finalize(ap.parse_args().mode)
