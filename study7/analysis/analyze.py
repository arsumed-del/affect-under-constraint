"""Joint prompt-cluster bootstrap with outlet-specific directional conjunctions."""
import argparse,json
import numpy as np
from study7.src.common import *
from study5.analysis.analyze import add
OUTLETS=('O1','O2','O2c','O3','O3q','B1','B2','B3')
CONTROLS=('unsteered','technicality','random')
def definitions():
 d={}
 for o in OUTLETS:
  for l in ['G','S','N']:
   for ctrl in CONTROLS:d[f'{o}:{l}:{ctrl}']={(o,'hostility',l):1,(o,ctrl,l):-1}
  for i,j in [('G','N'),('S','N'),('S','G')]:
   for ctrl in CONTROLS:d[f'{o}:{i}-{j}:{ctrl}']=add(d[f'{o}:{i}:{ctrl}'],d[f'{o}:{j}:{ctrl}'])
 for i,j in [('G','N'),('S','N'),('S','G')]:
  for o,q in [('O2','O2c'),('O3','O3q')]:
   for ctrl in CONTROLS:d[f'{o}-{q}:{i}-{j}:{ctrl}']=add(d[f'{o}:{i}-{j}:{ctrl}'],d[f'{q}:{i}-{j}:{ctrl}'])
 return d
def tests():
 triple=lambda o,l,sign:[(f'{o}:{l}:{c}',sign) for c in CONTROLS]
 return {'EH':triple('B1','G-N',-1),'P1':triple('O1','G-N',1)+[('O1:N:unsteered',-1)],'P2_core':triple('O2','S-N',-1)+[('O2:S:unsteered',-1)],'P2':triple('O2','S-N',-1)+[('O2:S:unsteered',-1),('O2-O2c:S-N:unsteered',-1)],'P3':triple('O2','S-G',-1),'S1':triple('O1','S-N',1),'S2_G':triple('O3','G-N',-1),'S2_S':triple('O3','S-N',-1),'S2_G_net':triple('O3-O3q','G-N',-1),'S2_S_net':triple('O3-O3q','S-N',-1),'S3':triple('B2','G',1)}
def summarize(v,b,level,sign,margin):
 n=int(np.isfinite(v).sum())
 if not len(v) or n!=len(v):return dict(status='not interpretable',n=n,n_required=len(v),supported=False,reversed=False,negligible=False)
 lo,hi=np.quantile(b,[(1-level)/2,(1+level)/2]);el,eh=np.quantile(b,[.05,.95])
 support=bool(lo>0 if sign>0 else hi<0);reverse=bool(hi<0 if sign>0 else lo>0);eq=bool(el>-margin and eh<margin)
 label='small but detectable' if eq and (support or reverse) else 'supported' if support else 'reversed' if reverse else 'negligible' if eq else 'inconclusive'
 return dict(estimate=float(v.mean()),ci_level=level,ci=[float(lo),float(hi)],equivalence_ci=[float(el),float(eh)],margin=margin,n=n,status=label,supported=support,reversed=reverse,negligible=eq)
def conjunction(parts):
 valid=all(p['status']!='not interpretable' for p in parts)
 sup=valid and all(p['supported'] for p in parts);rev=valid and all(p['reversed'] for p in parts);eq=valid and all(p['negligible'] for p in parts)
 return dict(supported=sup,reversed=rev,negligible=eq,mixed_components=any(p['supported'] for p in parts) and any(p['reversed'] for p in parts),status='not interpretable' if not valid else 'small but detectable' if eq and (sup or rev) else 'supported' if sup else 'reversed' if rev else 'negligible' if eq else 'inconclusive')
def reading(h,gate):
 out=[]
 if h['P1']['supported']:
  out.append('Global warmth attenuates the hostility-trace effect on original-target evaluation.' if gate else 'O1 suppression-based reading withheld: EH interaction gate failed.')
 if h['P2']['supported'] and h['P3']['supported']:out.append('Redistribution-consistent bystander pattern; independent branches do not establish causal transfer or a defense.')
 elif h['P2_core']['supported'] and not h['P2']['supported']:out.append('Bystander component passes but target specificity is not established; inspect O2c and the direct specificity contrast. Equal O2/O2c movement is generalized negative evaluation.')
 if gate and h['P1']['supported'] and h['P2']['negligible'] and h['P3']['negligible']:out.append('Attenuation without a detected shift to the measured bystander; equivalence is descriptive.')
 out.append('Reversed, mixed and inconclusive components remain outlet-specific. Detectability and descriptive equivalence may overlap.')
 return out
def core(data,c,ids):
 defs=definitions();names=list(defs);lookup={}
 for r in data:
  k=(r['prompt_id'],r['source'],r['level'],r['arm'])
  if k in lookup:raise ValueError('Duplicate cell')
  lookup[k]=r
 # One draw matrix for all outcomes and both arms, reused for every estimand.
 draws=np.random.default_rng(c['bootstrap_seed']).integers(0,len(ids),size=(c['analysis']['resamples'],len(ids))) if ids else np.empty((c['analysis']['resamples'],0),int)
 result={'n':len(ids),'prompt_ids':ids,'arms':{}}
 for arm in c['arms']:
  mat=np.full((len(ids),len(names)),np.nan)
  for j,terms in enumerate(defs.values()):
   for i,p in enumerate(ids):
    vals=[lookup.get((p,s,l,arm),{}).get('outcomes',{}).get(o) for o,s,l in terms]
    if all(v is not None and np.isfinite(v) for v in vals):mat[i,j]=sum(v*w for v,w in zip(vals,terms.values()))
  # Chunk draws to avoid a 10000 x 80 x all-estimands temporary.
  samples=np.empty((len(draws),len(names)))
  for k in range(0,len(draws),100):samples[k:k+100]=mat[draws[k:k+100]].mean(axis=1) if ids else np.nan
  estimates={};components={};hs={}
  def summary(name,level,sign):
   j=names.index(name);o=name.split(':')[0].split('-')[0]
   return summarize(mat[:,j],samples[:,j],level,sign,c['analysis']['margins'][o])
  for name in names:
   if arm=='fixed' and name.startswith('B'):continue
   estimates[name]=summary(name,.95,1)
  for h,parts in tests().items():
   if arm=='fixed' and h in ['EH','S3']:continue
   level=c['analysis']['primary_ci'] if h.startswith('P') and arm=='generated' else .95
   components[h]={name:summary(name,level,sign) for name,sign in parts};hs[h]=conjunction(list(components[h].values()))
  result['arms'][arm]={'estimands':estimates,'components':components,'hypotheses':hs,'interval_label':'Primary P1–P3 adjusted; secondary 95% unadjusted' if arm=='generated' else 'S4 secondary: 95% unadjusted; classifier outcomes unavailable'}
 gate=result['arms']['generated']['hypotheses']['EH']['supported']
 result['EH_gate']=gate
 for arm,r in result['arms'].items():
  r['reading']=reading(r['hypotheses'],gate)
  for h in ['P1','S1']:r['hypotheses'][h]['interpretation_status']=r['hypotheses'][h]['status'] if gate else 'not interpretable'
 result['answer_dependence']={h:('agreement: pattern does not require answer differences' if result['arms']['generated']['hypotheses'][h]['supported'] and result['arms']['fixed']['hypotheses'][h]['supported'] else 'disagreement: report as answer-dependent' if result['arms']['generated']['hypotheses'][h]['supported']!=result['arms']['fixed']['hypotheses'][h]['supported'] else 'neither arm supports the pattern; agreement alone is not evidence') for h in ['P1','P2','P3']}
 return result
def analyze(data,c,ids,audit):
 result={'primary':core(data,c,ids),'sensitivity':{},'diagnostics':{}}
 natural=[p for p in ids if all(any(r['prompt_id']==p and r['source']==s and not r['forced_closure'] for r in data) for s in SOURCES)]
 e5=[p for p in ids if p in audit and not(audit[p]['instructions'] or audit[p]['negative_characterizations'])]
 for name,subset in [('E5',e5),('natural_trace_closure',natural)]:
  result['sensitivity'][name]=core([r for r in data if r['prompt_id'] in subset],c,subset)
  result['sensitivity'][name]['label']='Exploratory, not confirmatory'
 for arm in c['arms']:
  for level in c['levels']:
   for source in SOURCES:
    g=[r for r in data if (r['arm'],r['level'],r['source'])==(arm,level,source)]
    result['diagnostics']['/'.join([arm,level,source])]=[{'prompt_id':r['prompt_id'],'ratings':r.get('ratings'),'answer_length':r.get('answer_length'),'answer_truncated':r.get('answer_truncated'),'classifier':r.get('answer_classifier'),'markers':r.get('markers'),'checks':r.get('checks')} for r in g]
 return result
def report(result):
 lines=['# Study 7 analysis','','Independent branches support instruction-dependent moderation; no causal transfer claim. Secondary intervals are 95% unadjusted. Equivalence intervals are 90% descriptive.']
 for section,core_result in [('Full sample',result['primary']),*result['sensitivity'].items()]:
  lines+=['',f'## {section} (n={core_result["n"]})','',f'EH interaction gate: {core_result["EH_gate"]}']
  for arm,a in core_result['arms'].items():
   lines+=['',f'### {arm}', '',*a['reading'],'','| Test / component | Estimate | CI level | CI | Status |','|---|---:|---:|---|---|']
   for h,parts in a['components'].items():
    lines.append(f'| {h} conjunction | | | | {a["hypotheses"][h]["status"]} |')
    for n,v in parts.items():lines.append(f'| {h}/{n} | {v.get("estimate","—")} | {v.get("ci_level","—")} | {v.get("ci","—")} | {v["status"]} |')
 return '\n'.join(lines)+'\n'
def main():
 p=argparse.ArgumentParser();p.add_argument('--input',default=str(ROOT/'data/main/cells.jsonl'));p.add_argument('--output',default=str(ROOT/'data/main'));args=p.parse_args()
 c=config();data=verified_rows(args.input)
 if not data or any(r['mode']!='main' for r in data):raise ValueError('Main rows required')
 require_approval();verify(c)
 from study7.src.runner import load,plan,validate_resume
 manifest=json.loads((ROOT/'data/main/manifest.json').read_text())
 if manifest!={'mode':'main','hashes':freeze_hashes()}:raise RuntimeError('Main manifest mismatch')
 inputs=load(c,'main');expected=set(plan(c,'main'))
 if validate_resume(data,expected,digest(manifest),inputs[2],inputs[3])!=expected:raise RuntimeError('Main incomplete; preserve data and resume')
 result=analyze(data,c,c['main_prompt_ids'],json.loads(path(c,'e5_audit').read_text()))
 dest=output(Path(args.output)/'analysis.json');save(dest,result)
 with output(dest.with_suffix('.md')).open('x') as f:f.write(report(result))
if __name__=='__main__':main()
