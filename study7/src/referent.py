"""Pilot-only 16-prompt referent diagnostic; stored a_U, no generated answers."""
import json,gc,time
from .common import *
from .runner import load

def run(b,a,c,mh):
 prompts,traces,orig,clamps=load(c,'main');file=ROOT/'data/pilot/referent.jsonl'
 expected={(p,s,l) for p in c['check_ids'] for s in SOURCES for l in c['levels']};done=set()
 for r in verified_rows(file):
  k=tuple(r['cell_key'])
  if k in done or k not in expected or r['manifest_sha256']!=mh:raise RuntimeError('Referent resume mismatch')
  done.add(k)
 for p,s,l in sorted(expected):
  if (p,s,l) in done:continue
  try:
   start=time.monotonic();prefix,_=a.assemble(prompts[p]['text'],traces[p,s],l)
   branch=a.branch(prefix+orig[p,'unsteered']['answer_ids'],'O2');rating=b.rating(branch)
   history=branch+a.enc(rating['argmax'])
   branches={q:a.branch(history,q) for q in ['referent','referent_swap']}
   checks={q:b.rating(ids,list('AB')) for q,ids in branches.items()}
   append(file,dict(cell_key=[p,s,l],prompt_id=p,source=s,level=l,arm='fixed_diagnostic',O2=rating,branch_ids=branches,checks=checks,manifest_sha256=mh,seconds=time.monotonic()-start))
  finally:gc.collect();b.torch.mps.empty_cache()
 return verified_rows(file)
