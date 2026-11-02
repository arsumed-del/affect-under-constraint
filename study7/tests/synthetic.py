"""No model: validate null, directional, specificity, and conjunction logic."""
import json
import numpy as np
from study7.src.common import *
from study7.analysis.analyze import core,analyze,report

def fixture(kind,c):
 rng=np.random.default_rng(771);data=[]
 for i in range(80):
  p=f'syn{i:02}';noise=float(rng.normal(0,.035))
  for arm in c['arms']:
   for level in c['levels']:
    for source in SOURCES:
     outcomes={o:(.3 if o.startswith('B') else 6.) for o in ['O1','O2','O2c','O3','O3q','B1','B2','B3']}
     if kind!='null':
      if source=='hostility':
       outcomes['O1']+= {'N':-1.,'S':-.2,'G':-.2}[level]+noise
       outcomes['O2']+= {'N':0.,'S':-.8,'G':0.}[level]+noise
       outcomes['O3']+= {'N':0.,'S':-.6,'G':-.6}[level]+noise
       outcomes['B1']+= {'N':.2,'S':0.,'G':0.}[level]+noise/10
       outcomes['B2']+=.2+noise/10 if level=='G' else 0
       if kind=='generalized':outcomes['O2c']=outcomes['O2']
       if kind=='reversed':
        for o in ['O1','O2','O3']:outcomes[o]=12-outcomes[o]
      if kind=='mixed' and source=='technicality':
       outcomes['O1']+= {'N':-2.,'S':0.,'G':0.}[level]
       outcomes['O2']+= {'N':0.,'S':-1.6,'G':0.}[level]
     if arm=='fixed':outcomes={k:v for k,v in outcomes.items() if not k.startswith('B')}
     data.append(dict(schema=c['schema'],mode='synthetic',cell_key=[p,source,level,arm],prompt_id=p,source=source,level=level,arm=arm,outcomes=outcomes,forced_closure=i%5==0))
 return data

def main():
 c=config();results={}
 for kind in ['null','planted','generalized','reversed','mixed']:
  data=fixture(kind,c);ids=sorted({r['prompt_id'] for r in data});r=core(data,c,ids);h=r['arms']['generated']['hypotheses']
  if kind=='null':assert all(not h[p]['supported'] and h[p]['negligible'] for p in ['P1','P2','P3'])
  if kind=='planted':assert all(h[p]['supported'] for p in ['P1','P2','P3']) and r['EH_gate']
  if kind=='generalized':assert not h['P2']['supported'] and h['P2_core']['supported']
  if kind=='reversed':assert all(h[p]['reversed'] for p in ['P1','P2','P3'])
  if kind=='mixed':assert all(not h[p]['supported'] and h[p]['mixed_components'] for p in ['P1','P2','P3'])
  dest=ROOT/'data/synthetic'/kind
  for row in data:append(dest/'cells.jsonl',row)
  save(dest/'analysis.json',r)
  results[kind]={'passed':True,'hypotheses':h}
 # Missing outcomes must never silently shrink a prompt cluster.
 data=fixture('planted',c);data[0]['outcomes']['O1']=None
 r=core(data,c,sorted({x['prompt_id'] for x in data}))
 assert r['arms']['generated']['hypotheses']['P1']['status']=='not interpretable'
 results['missing']={'passed':True}
 save(ROOT/'results/synthetic_validation.json',results)
 with output(ROOT/'results/synthetic_validation.md').open('x') as f:
  f.write('# Synthetic validation\n\nAll six checks passed with 10,000 joint prompt-cluster draws and exact primary coverage 1 − 0.05/3. No model calls.\n\n'+ '\n'.join('- '+k+': PASS' for k in results)+'\n')
 print('Synthetic validation passed:',', '.join(results))
if __name__=='__main__':main()
