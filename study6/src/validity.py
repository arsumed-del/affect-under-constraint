"""Numerical replay and placement-level digit-mass validity."""
import math
from .common import CONDITIONS, SOURCES, digest, verified_rows, ROOT, save

def numerical_check(row, originals):
    p,s,c,arm = row['cell_key']
    if arm=='sham' or (arm=='clamp' and s=='unsteered'):
        old = originals[p,s,c]['ratings']['sender']['expected']
        delta = row['ratings']['sender']['expected']-old
        if not math.isfinite(delta) or abs(delta) > .01:
            raise RuntimeError(f'Numerical replay BLOCKED: {row["cell_key"]}: difference {delta!r}, tolerance 0.01; investigate environment')
        return delta
    return None

def mass_report(data):
    groups = {}; dropped = set()
    for c in CONDITIONS:
        for s in SOURCES:
            group = [r for r in data if r['condition']==c and r['source']==s]
            vals = [r['ratings']['sender']['valid_mass'] for r in group]
            value = sum(vals)/len(vals) if vals else None
            passed = value is not None and math.isfinite(value) and value>=.8
            if value is not None and not passed: dropped.add(c)
            groups[c+'/'+s] = {'n':len(vals),'mean_valid_mass':value,'pass':passed}
    arm_groups={}
    for arm in sorted({r['arm'] for r in data}):
        for c in CONDITIONS:
            for s in SOURCES:
                vals=[r['ratings']['sender']['valid_mass'] for r in data if r['arm']==arm and r['condition']==c and r['source']==s]
                if vals: arm_groups[arm+'/'+c+'/'+s]={'n':len(vals),'mean_valid_mass':sum(vals)/len(vals)}
    return {'groups':groups,'per_arm_groups':arm_groups,'dropped_placements':sorted(dropped),
            'rule':'Mean valid-digit mass >= 0.8 by placement x source; failure drops entire placement from all estimands.'}

def validate_rows(data, expected, manifest_hash, originals, assembly, generic_ids):
    from .assembly import answer_for
    seen = set()
    for r in data:
        k = tuple(r['cell_key'])
        if k in seen or k not in expected: raise RuntimeError(f'Duplicate/unexpected cell: {k}')
        if r['manifest_sha256'] != manifest_hash: raise RuntimeError('Stale resume provenance')
        if (r['prompt_id'],r['source'],r['condition'],r['arm']) != k: raise RuntimeError('Inconsistent cell metadata')
        answer,_ = answer_for(k,originals,generic_ids)
        ids = assembly.rating_input(originals[k[:3]],answer)
        if r['input_ids_sha256'] != digest(ids): raise RuntimeError('Resume input token hash mismatch')
        rating=r['ratings']['sender']; probs=rating['probabilities']
        if set(probs)!=set('0123456789') or not all(math.isfinite(v) and 0<=v<=1 for v in probs.values()): raise RuntimeError('Invalid digit probabilities')
        if abs(sum(probs.values())-1)>1e-5 or abs(sum(int(k)*v for k,v in probs.items())-rating['expected'])>1e-6: raise RuntimeError('Inconsistent digit readout')
        if not math.isfinite(rating['valid_mass']) or not 0<=rating['valid_mass']<=1.00001: raise RuntimeError('Invalid digit mass')
        numerical_check(r,originals); seen.add(k)
    return seen

def pilot_evaluation(first, second, cfg, manifest_hash, originals, assembly, generic_ids):
    from .assembly import plan
    ids=cfg['pilot_prompt_ids']; expected=set(plan(ids,'pilot'))
    sham={k for k in expected if k[-1]=='sham'}
    if validate_rows(first,expected,manifest_hash,originals,assembly,generic_ids)!=expected: raise RuntimeError('First pilot start incomplete')
    if validate_rows(second,sham,manifest_hash,originals,assembly,generic_ids)!=sham: raise RuntimeError('Second sham replay incomplete')
    processes1={r['process_start_id'] for r in first}
    processes2={r['process_start_id'] for r in second}
    if processes1 & processes2 or len(processes2)!=1: raise RuntimeError('Sham replay needs a separate process start')
    mass=mass_report(first+second)
    arms=[r for r in first if r['arm']!='sham']
    longest=sorted(arms,key=lambda r:r['input_length'],reverse=True)[:10]
    return {'pass':len(mass['dropped_placements'])<len(CONDITIONS),'numerical_replay_pass':True,'manifest_sha256':manifest_hash,'numerical_tolerance':.01,
            'first_cells':len(first),'second_sham_cells':len(second),
            'mass':mass,'seconds_per_arm_cell':sum(r['seconds'] for r in arms)/len(arms),
            'estimated_main_hours':sum(r['seconds'] for r in arms)/len(arms)*2640/3600,
            'longest_prefix_timings':[{k:r[k] for k in ('cell_key','input_length','seconds','peak_driver_memory_bytes')} for r in longest],
            'peak_driver_memory_bytes':max(r['peak_driver_memory_bytes'] for r in first+second)}

def require_pilot(cfg, hashes, originals, assembly, generic_ids):
    import json
    from .common import sha
    path=ROOT/'data/pilot/validity.json'
    if not path.exists(): raise RuntimeError('Main requires passing pilot validity from two process starts')
    v=json.loads(path.read_text())
    first=ROOT/'data/pilot/cells.jsonl'; second=ROOT/v['second_replay_path']
    if not second.resolve().is_relative_to((ROOT/'data/pilot').resolve()): raise RuntimeError('Invalid second replay path')
    if v['first_sha256']!=sha(first) or v['second_sha256']!=sha(second): raise RuntimeError('Pilot data changed')
    mh=digest({'mode':'pilot','hashes':hashes})
    fresh=pilot_evaluation(verified_rows(first),verified_rows(second),cfg,mh,originals,assembly,generic_ids)
    if any(v.get(k)!=value for k,value in fresh.items()): raise RuntimeError('Pilot validity is stale or inconsistent')
    if not fresh['pass']: raise RuntimeError('Pilot has no valid placements; main blocked')
    return fresh
