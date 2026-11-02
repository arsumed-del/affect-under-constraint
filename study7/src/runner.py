"""Unsteered replay, inherited sampler, independent fresh rating branches."""
import argparse,fcntl,gc,json,time,warnings,re
from .common import *
from .assembly import Assembly
from study5.src.runner import Backend as BaseBackend
from study4.src.runner import assert_no_hooks
RATINGS=('O1','O2','O2c','O3','O3q')
class Backend(BaseBackend):
 def __init__(self,c):
  # Study 5 resolves paths from its own directory (same parent as study7).
  super().__init__(c)
  if self.m.model.config._attn_implementation!=c['environment']['attention_implementation']: raise RuntimeError('Attention pin mismatch')
  if any(p.dtype!=self.torch.bfloat16 or p.device.type!='mps' for p in self.m.model.parameters()): raise RuntimeError('Precision/device pin mismatch')
 def rating(self,ids,labels=list('0123456789')):
  assert_no_hooks(self.m.model)
  return super().rating(ids,labels)
def load(c,mode):
 ids=c[mode+'_prompt_ids']
 prompts={r['id']:r for r in (json.loads(l) for l in path(c,mode+'_prompts').read_text().splitlines())}
 traces={tuple(r['trace_key']):r for r in verified_rows(path(c,mode+'_traces'))}
 originals={(r['prompt_id'],r['source']):r for r in verified_rows(path(c,mode+'_cells')) if r['condition']=='R1'}
 old4={(r['prompt_id'],r['source']):r for r in verified_rows(path(c,'study4_'+mode+'_cells')) if r['framing']=='own_native'}
 clamps={(r['prompt_id'],r['source']):r for r in verified_rows(path(c,'study6_'+mode+'_cells')) if r['condition']=='R1' and r['arm']=='clamp'}
 v06={(r['prompt_id'],r['source']):r for r in verified_rows(path(c,'pilot_v06_ratings')) if r['framing']=='own_native'} if mode=='pilot' else {}
 for p in ids:
  for s in SOURCES:
   r=originals[p,s];q=old4[p,s]
   for k in ['answer_prefix_ids','answer_ids','answer_seed']:
    if r[k]!=q[k]: raise RuntimeError('Study 4/5 reference disagreement '+k)
   if abs(r['ratings']['sender']['expected']-(v06[p,s]['sender_clear']['expected'] if mode=='pilot' else q['ratings']['sender']['expected']))>.01: raise RuntimeError('Study 4/5 reference rating disagreement')
   if c['answer_seeds'][mode][p+'/'+s]!=r['answer_seed']: raise RuntimeError('Seed mismatch')
   clamps[p,s];traces[p,s]
 return prompts,traces,originals,clamps
def plan(c,mode):
 return [(p,s,l,a) for p in c[mode+'_prompt_ids'] for s in SOURCES for l in c['levels'] for a in c['arms']]
def reproduce(r,originals,clamps):
 if r['level']!='G': return
 k=(r['prompt_id'],r['source']);ref=originals[k] if r['arm']=='generated' else clamps[k]
 if r['answer_ids']!=ref['answer_ids'] or abs(r['ratings']['O1']['expected']-ref['ratings']['sender']['expected'])>.01:
  raise RuntimeError('Reproduction failure: '+str(r['cell_key']))
def run_cell(b,a,c,mode,key,inputs,mh):
 p,s,l,arm=key;prompts,traces,orig,clamps=inputs;tr=traces[p,s]
 start=time.monotonic();b.events=[];b.peak=0
 prefix,bounds=a.assemble(prompts[p]['text'],tr,l)
 if l=='G' and prefix!=orig[p,s]['answer_prefix_ids']: raise RuntimeError('G prefix mismatch')
 seed=c['answer_seeds'][mode][p+'/'+s]
 with warnings.catch_warnings(record=True) as caught:
  warnings.simplefilter('always');assert_no_hooks(b.m.model)
  answer=b.answer(prefix,seed,c['generation']['answer_cap']) if arm=='generated' else list(orig[p,'unsteered']['answer_ids'])
  history=prefix+answer
  branches={q:a.branch(history,q) for q in RATINGS}
  ratings={q:b.rating(v) for q,v in branches.items()}
  checks={};check_ids={}
  if mode=='pilot':
   for q in ['Sam_friendly','Sam_rude']:
    check_ids[q]=a.branch(history,q);checks[q]=b.rating(check_ids[q])
  if p in c['check_ids'] or mode=='pilot':
   h=branches['O2']+a.enc(ratings['O2']['argmax'])
   for q in ['referent','referent_swap']:
    check_ids[q]=a.branch(h,q);checks[q]=b.rating(check_ids[q],list('AB'))
  text=b.m.tokenizer.decode(answer,skip_special_tokens=True)
  cl=b.classifier.score(text) if arm=='generated' else None
  b.torch.mps.synchronize()
 eos=b.m.model.generation_config.eos_token_id;eos=eos if isinstance(eos,list) else [eos]
 r=dict(schema=c['schema'],mode=mode,cell_key=list(key),prompt_id=p,source=s,level=l,arm=arm,answer_prefix_ids=prefix,trace_ids=tr['trace_ids'],trace_bounds=bounds,forced_closure=tr['forced_closure'],trace_sha256=tr['row_sha256'],answer_ids=answer,answer_text=text,answer_seed=seed,answer_length=len(answer),answer_truncated=bool(answer and len(answer)==c['generation']['answer_cap'] and answer[-1] not in eos),ratings=ratings,branch_ids=branches,checks=checks,check_ids=check_ids,answer_classifier=cl,outcomes={q:ratings[q]['expected'] for q in RATINGS},replay_assertions=b.events.copy(),seconds=time.monotonic()-start,peak_driver_memory_bytes=b.peak,warnings=[str(w.message) for w in caught],manifest_sha256=mh)
 if cl:r['outcomes'].update(B1=cl['eh'],B2=cl['ew'],B3=(cl['probabilities'] or {}).get('neutral'))
 r['markers']={k:len(re.findall(v,tr.get('text','') if k=='trace_instruction' else text,re.I)) for k,v in c['regexes'].items()}
 for w in r['warnings']:print(w,flush=True)
 return r
def validate_resume(data,keys,mh,orig,clamps):
 done=set()
 for r in data:
  k=tuple(r['cell_key'])
  if k not in keys or k in done or r['manifest_sha256']!=mh:raise RuntimeError('Resume provenance/key failure')
  reproduce(r,orig,clamps);done.add(k)
 return done
def main():
 parser=argparse.ArgumentParser();parser.add_argument('--mode',choices=['pilot','main'],required=True);mode=parser.parse_args().mode
 c=config()
 if mode=='main':require_approval()
 verify(c);inputs=load(c,mode);hashes=freeze_hashes()
 if mode=='main':
  from study7.analysis.pilot import require_pilot
  require_pilot(c,hashes)
 manifest={'mode':mode,'hashes':hashes};mh=digest(manifest);directory=ROOT/'data'/mode
 with output(directory/'run.lock').open('a') as lock:
  fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
  mp=directory/'manifest.json'
  if mp.exists():
   if json.loads(mp.read_text())!=manifest:raise RuntimeError('Resume manifest mismatch')
  else:save(mp,manifest)
  keys=plan(c,mode);file=directory/'cells.jsonl';done=validate_resume(verified_rows(file),set(keys),mh,inputs[2],inputs[3])
  if len(done)<len(keys):
   b=Backend(c);a=Assembly(b.m.tokenizer,json.loads((ROOT/'framings_s7.json').read_text()))
   for key in keys:
    if key in done:continue
    try:
     r=append(file,run_cell(b,a,c,mode,key,inputs,mh));reproduce(r,inputs[2],inputs[3]);done.add(key)
     msg=f'{mode}: {len(done)}/{len(keys)}; last {r["seconds"]:.1f}s; ETA {(len(keys)-len(done))*r["seconds"]/3600:.2f} hours.';print(msg,flush=True);status(msg)
    finally:gc.collect();b.torch.mps.empty_cache()
  if mode=='pilot':
   from .referent import run as run_referent
   if 'b' not in locals():
    b=Backend(c);a=Assembly(b.m.tokenizer,json.loads((ROOT/'framings_s7.json').read_text()))
   referent=run_referent(b,a,c,mh)
   from study7.analysis.pilot import evaluate
   result=evaluate(verified_rows(file),c);result.update(hashes=hashes,cells_sha256=sha(file),referent_check_rows=len(referent),referent_checks=referent);save(directory/'validity.json',result)
  status(mode+' complete. No automatic analysis or next-stage run.')
if __name__=='__main__':
 try:main()
 except Exception as e:
  status('BLOCKED: '+repr(e)+' Existing data preserved.')
  with (ROOT/'DEVIATIONS.md').open('a') as f:f.write('\n## Run stopped\n'+repr(e)+'\n')
  raise
