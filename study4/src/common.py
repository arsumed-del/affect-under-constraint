import os
os.environ['PYTORCH_ENABLE_MPS_FALLBACK'] = '1'
os.environ['PYTHONDONTWRITEBYTECODE'] = '1'
os.environ['HF_HUB_OFFLINE'] = '1'
os.environ['TRANSFORMERS_OFFLINE'] = '1'
import hashlib, json
from pathlib import Path
import yaml
ROOT = Path(__file__).resolve().parents[1]
SOURCES = ('unsteered', 'hostility', 'technicality', 'random')
FRAMINGS = ('own_native', 'own_quoted', 'other_quoted')
CONTROLS = ('technicality', 'random')
def sha(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def digest(obj): return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(',',':'),allow_nan=False).encode()).hexdigest()
def config(): return yaml.safe_load((ROOT/'config.yaml').read_text())
def rows(path): return [json.loads(s) for s in Path(path).read_text().splitlines()] if Path(path).exists() else []
def output_path(path):
    p=Path(path).resolve()
    if not p.is_relative_to(ROOT): raise ValueError('Writes must remain inside study4/')
    p.parent.mkdir(parents=True,exist_ok=True)
    return p
def save(path,obj):
    p=output_path(path)
    payload=json.dumps(obj,indent=2,allow_nan=False)+'\n'
    with p.open('x') as f: f.write(payload)
def append(path,obj):
    obj=dict(obj);obj['row_sha256']=digest(obj)
    with output_path(path).open('a') as f:
        f.write(json.dumps(obj,allow_nan=False)+'\n'); f.flush();os.fsync(f.fileno())
    return obj

def verified_rows(path):
    rr=rows(path)
    for r in rr:
        payload={k:v for k,v in r.items() if k!='row_sha256'}
        if r.get('row_sha256')!=digest(payload):raise RuntimeError(f'Corrupt row in {path}; preserve and investigate')
    return rr

def seed(cfg,*parts):
    return int(digest([cfg['seeds']['generation'],*parts]),16)%2**31

def verify_reuse(cfg):
    result={}
    for label,item in {**cfg['directions'],'norm':cfg['norm'],'study3_raw':cfg['study3_raw'],'pilot_prompts':cfg['pilot_source']}.items():
        actual=sha(ROOT/item['path'])
        if actual!=item['sha256']: raise RuntimeError(f'Reused artifact hash mismatch: {label}')
        result[label]=actual
    return result
