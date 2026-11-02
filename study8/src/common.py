import hashlib, json, os
from pathlib import Path
import yaml
ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parent
SOURCES = ('unsteered','hostility','technicality','random')
CONTEXTS = ('N','M','P')
def sha(p):
    h=hashlib.sha256()
    with Path(p).open('rb') as f:
        for b in iter(lambda:f.read(8*1024*1024),b''): h.update(b)
    return h.hexdigest()
def digest(v): return hashlib.sha256(json.dumps(v,sort_keys=True,separators=(',',':'),allow_nan=False).encode()).hexdigest()
def output(p):
    p=Path(p).resolve()
    if not p.is_relative_to(ROOT): raise ValueError('Writes restricted to study8/')
    p.parent.mkdir(parents=True,exist_ok=True)
    return p
def save(p,v):
    with output(p).open('x') as f: json.dump(v,f,indent=2,allow_nan=False); f.write('\n')
def ensure(p,v):
    if Path(p).exists():
        if json.loads(Path(p).read_text())!=json.loads(json.dumps(v,allow_nan=False)): raise RuntimeError('Existing artifact differs: '+str(p))
    else: save(p,v)
def rows(p):
    if not Path(p).exists(): return []
    data=Path(p).read_bytes()
    if data and not data.endswith(b'\n'): raise RuntimeError('Incomplete row; preserve and investigate: '+str(p))
    return [json.loads(l) for l in data.splitlines()]
def verified(p,key):
    rr=rows(p); seen=set()
    for r in rr:
        if r.get('row_sha256')!=digest({k:v for k,v in r.items() if k!='row_sha256'}): raise RuntimeError('Corrupt row: '+str(p))
        k=json.dumps(r[key],sort_keys=True)
        if k in seen: raise RuntimeError('Duplicate row: '+k)
        seen.add(k)
    return rr
def append(p,v):
    v=dict(v,row_sha256=digest(v))
    with output(p).open('a') as f:
        f.write(json.dumps(v,allow_nan=False)+'\n'); f.flush(); os.fsync(f.fileno())
    return v
def config(): return yaml.safe_load((ROOT/'config_s8.yaml').read_text())
def seed(stage,p,s): return int(digest([20261029,stage,p,s]),16)%2**31
def prompts(mode):
    c=config(); rr=rows(REPO/c['prompts'][mode])
    if mode=='pilot': rr=[p for p in rr if p['id'] in c['pilot_ids']]
    assert len(rr)==(4 if mode=='pilot' else 80)
    return rr
def verify(c):
    if sha(ROOT/c['preregistration'])!=c['preregistration_sha256']: raise RuntimeError('Preregistration changed')
    import importlib.metadata
    current={d.metadata['Name']:d.version for d in importlib.metadata.distributions()}
    if current!=c['environment']: raise RuntimeError('Pinned Python package environment changed')
    for p,h in c['input_hashes'].items():
        if sha(REPO/p)!=h: raise RuntimeError('Input changed: '+p)
    for spec in [c['model'],*c['judges'].values(),c['classifier']]:
        for p,h in spec['files'].items():
            if sha(Path(spec['local_path'])/p)!=h: raise RuntimeError('Model file changed: '+p)
def freeze_hashes():
    paths=[ROOT/'config_s8.yaml',ROOT/'framings_s8.json',ROOT/config()['preregistration']]
    for folder in ('src','analysis','tests','judges','calibration','imported'):
        paths += [p for p in (ROOT/folder).rglob('*') if p.is_file() and '__pycache__' not in str(p)]
    paths+=list(ROOT.glob('*.command'))+[ROOT/'build_artifacts.py',ROOT/'results/output_schema.json']
    return {str(p.relative_to(ROOT)):sha(p) for p in sorted(set(paths))}
def require_approval():
    a=json.loads((ROOT/'PREREG_APPROVED').read_text())
    if a.get('status')!='APPROVED' or not all(a.get(k) for k in ('author','date','zenodo_deposit')) or a.get('hashes')!=freeze_hashes():
        raise RuntimeError('Approval absent or stale')
    v=json.loads((ROOT/'data/pilot/validity.json').read_text())
    if v.get('passed') is not True or v.get('freeze_hashes')!=freeze_hashes(): raise RuntimeError('Pilot absent, failed, or stale')
    for name,h in v['input_hashes'].items():
        if sha(ROOT/'data/pilot'/name)!=h: raise RuntimeError('Pilot data changed after validity gate')
def process_lock():
    """Hold an exclusive model-process lock until interpreter exit."""
    import fcntl, atexit
    f=output(ROOT/'logs/model_process.lock').open('a')
    try: fcntl.flock(f,fcntl.LOCK_EX|fcntl.LOCK_NB)
    except BlockingIOError:
        f.close(); raise RuntimeError('Another Study 8 model process is active')
    atexit.register(f.close)
    return f
def status(text): output(ROOT/'STATUS.md').write_text('# Study 8\n\n'+text+'\n')
