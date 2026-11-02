"""Validity only: no instruction-effect estimates."""
import numpy as np,json
from study7.src.common import *
from study7.src.runner import plan,load,validate_resume,RATINGS

def evaluate(data,c):
 groups={};passed=True
 for arm in c['arms']:
  for level in c['levels']:
   for source in SOURCES:
    rows=[r for r in data if (r['arm'],r['level'],r['source'])==(arm,level,source)]
    masses={q:[r['ratings'][q]['valid_mass'] for r in rows] for q in RATINGS}
    sam=[r['checks']['Sam_friendly']['expected']-r['checks']['Sam_rude']['expected'] for r in rows]
    valid=len(rows)==4 and all(v>=.8 for values in masses.values() for v in values)
    passed &=valid
    groups['/'.join([arm,level,source])]=dict(pass_=valid,mass=masses,Sam_friendly_minus_rude=sam,baseline_sd={q:float(np.std([r['ratings'][q]['expected'] for r in rows],ddof=1)) for q in RATINGS[1:]} if source=='unsteered' and len(rows)>1 else {},referent=[r['checks'] for r in rows])
 sam_levels={level:float(np.mean([r['checks']['Sam_friendly']['expected']-r['checks']['Sam_rude']['expected'] for r in data if r['level']==level])) for level in c['levels']}
 passed &= all(v>=1. for v in sam_levels.values())
 return {'Sam_by_level':sam_levels,'pass':bool(passed),'groups':groups,'estimated_main_hours':sum(r['seconds'] for r in data)/len(data)*1920/3600 if data else None,'peak_memory':max((r['peak_driver_memory_bytes'] for r in data),default=None),'margin_disposition':'Provisional margins retained; author may resolve pilot spread before freezing. No automated wording or margin revision.'}
def require_pilot(c,hashes):
 directory=ROOT/'data/pilot';manifest=json.loads((directory/'manifest.json').read_text())
 if manifest!={'mode':'pilot','hashes':hashes}:raise RuntimeError('Pilot build is stale')
 data=verified_rows(directory/'cells.jsonl');inputs=load(c,'pilot');expected=set(plan(c,'pilot'))
 if validate_resume(data,expected,digest(manifest),inputs[2],inputs[3])!=expected:raise RuntimeError('Incomplete pilot')
 ref=verified_rows(directory/'referent.jsonl')
 expected_ref={(p,s,l) for p in c['check_ids'] for s in SOURCES for l in c['levels']}
 if len(ref)!=len(expected_ref) or {tuple(r['cell_key']) for r in ref}!=expected_ref or any(r['manifest_sha256']!=digest(manifest) for r in ref):raise RuntimeError('Incomplete/stale 16-prompt referent diagnostic')
 if not evaluate(data,c)['pass']:raise RuntimeError('Pilot validity failed; no main run')
