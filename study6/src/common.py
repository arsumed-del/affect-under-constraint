"""Read-only inherited helpers; all output is restricted to Study 6."""
import os
import sys
sys.dont_write_bytecode = True
os.environ['PYTORCH_ENABLE_MPS_FALLBACK'] = '1'
os.environ['HF_HUB_OFFLINE'] = '1'
os.environ['TRANSFORMERS_OFFLINE'] = '1'
import json
import platform
import importlib.metadata
from pathlib import Path
import yaml
from study5.src.common import sha, digest, rows, verified_rows, SOURCES, CONDITIONS
ROOT = Path(__file__).resolve().parents[1]
def config(): return yaml.safe_load((ROOT/'config_s6.yaml').read_text())
def input_path(cfg, name): return ROOT/cfg['inputs'][name]['path']
def output_path(path):
    p = Path(path).resolve()
    if not p.is_relative_to(ROOT): raise ValueError('Writes must remain inside study6/')
    p.parent.mkdir(parents=True, exist_ok=True)
    return p

def save(path, obj):
    with output_path(path).open('x') as f:
        f.write(json.dumps(obj, indent=2, allow_nan=False)+'\n')

def append(path, obj):
    obj = dict(obj); obj['row_sha256'] = digest(obj)
    with output_path(path).open('a') as f:
        f.write(json.dumps(obj, allow_nan=False)+'\n'); f.flush(); os.fsync(f.fileno())
    return obj

def verify_inputs(cfg):
    for name, item in cfg['inputs'].items():
        if sha(ROOT/item['path']) != item['sha256']: raise RuntimeError('Input hash mismatch: '+name)
    for name, value in cfg['model_files'].items():
        if sha(ROOT/cfg['model']['local_path']/name) != value: raise RuntimeError('Model/tokenizer hash mismatch: '+name)

def environment():
    names = ['torch','transformers','numpy','scipy','PyYAML','tokenizers','safetensors','accelerate']
    return {'python':platform.python_version(), 'platform':platform.platform(),
            'packages':{n:importlib.metadata.version(n) for n in names}}

def verify_environment(cfg):
    if environment() != cfg['environment']['software']:
        raise RuntimeError('Execution environment differs from config; investigate without changing tolerance')

def status(message): (ROOT/'STATUS.md').write_text('# Study 6\n'+message+'\n')
