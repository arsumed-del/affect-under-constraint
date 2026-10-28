"""Study 4 persistence conventions, restricted to Study 5 writes."""
import os
os.environ['PYTHONDONTWRITEBYTECODE'] = '1'
os.environ['PYTORCH_ENABLE_MPS_FALLBACK'] = '1'
os.environ['HF_HUB_OFFLINE'] = '1'
os.environ['TRANSFORMERS_OFFLINE'] = '1'
import hashlib
import json
from pathlib import Path
import yaml
ROOT = Path(__file__).resolve().parents[1]
SOURCES = ('unsteered', 'hostility', 'technicality', 'random')
CONDITIONS = ('R1', 'R1-M', 'R2', 'R3', 'R4')
CONTROLS = ('technicality', 'random')
def sha(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def digest(obj): return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(',', ':'), allow_nan=False).encode()).hexdigest()
def config(): return yaml.safe_load((ROOT/'config_s5.yaml').read_text())
def rows(path): return [json.loads(s) for s in Path(path).read_text().splitlines()] if Path(path).exists() else []
def output_path(path):
    p = Path(path).resolve()
    if not p.is_relative_to(ROOT): raise ValueError('Writes must remain inside study5/')
    p.parent.mkdir(parents=True, exist_ok=True)
    return p
def save(path, obj):
    with output_path(path).open('x') as f: f.write(json.dumps(obj, indent=2, allow_nan=False)+'\n')
def append(path, obj):
    obj = dict(obj); obj['row_sha256'] = digest(obj)
    with output_path(path).open('a') as f:
        f.write(json.dumps(obj, allow_nan=False)+'\n'); f.flush(); os.fsync(f.fileno())
    return obj
def verified_rows(path):
    data = rows(path)
    for r in data:
        if r.get('row_sha256') != digest({k:v for k,v in r.items() if k!='row_sha256'}):
            raise RuntimeError(f'Corrupt row in {path}; preserve and investigate')
    return data

def verify_inputs(cfg):
    for name, item in cfg['inputs'].items():
        if sha(ROOT/item['path']) != item['sha256']: raise RuntimeError(f'Input hash mismatch: {name}')
    for name, expected in cfg['model_files'].items():
        if sha(ROOT/cfg['model']['local_path']/name) != expected: raise RuntimeError(f'Model/tokenizer hash mismatch: {name}')

def input_path(cfg, name): return ROOT/cfg['inputs'][name]['path']
