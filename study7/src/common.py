import sys, os
sys.dont_write_bytecode=True
os.environ.update(PYTORCH_ENABLE_MPS_FALLBACK='1',HF_HUB_OFFLINE='1',TRANSFORMERS_OFFLINE='1')
import json
from pathlib import Path
import yaml
from study5.src.common import sha,digest,verified_rows,SOURCES
from study6.src.common import environment
ROOT=Path(__file__).resolve().parents[1]
def config(): return yaml.safe_load((ROOT/'config_s7.yaml').read_text())
def path(c,n): return ROOT/c['inputs'][n]['path']
def output(p):
 p=Path(p).resolve()
 if not p.is_relative_to(ROOT): raise ValueError('Writes restricted to study7')
 p.parent.mkdir(parents=True,exist_ok=True)
 return p
def save(p,v):
 with output(p).open('x') as f: json.dump(v,f,indent=2,allow_nan=False);f.write('\n')
def append(p,v):
 v=dict(v,row_sha256=digest(v))
 with output(p).open('a') as f: f.write(json.dumps(v,allow_nan=False)+'\n');f.flush();os.fsync(f.fileno())
 return v
def status(s): (ROOT/'STATUS.md').write_text('# Study 7\n'+s+'\n')
def verify(c):
 for n,v in c['inputs'].items():
  if sha(ROOT/v['path'])!=v['sha256']: raise RuntimeError('Input hash mismatch: '+n)
 for n,h in c['model_files'].items():
  if sha(ROOT/c['model']['local_path']/n)!=h: raise RuntimeError('Model hash mismatch: '+n)
 if environment()!=c['environment']['software']: raise RuntimeError('Pinned environment mismatch')
def freeze_hashes():
 paths=[ROOT/'config_s7.yaml',ROOT/'framings_s7.json',ROOT/config()['preregistration'],ROOT/'build_artifacts.py',ROOT/'results/output_schema.json']
 for folder in ['src','analysis','tests']: paths+=sorted((ROOT/folder).glob('*.py'))
 paths+=sorted(ROOT.glob('*.command'))
 return {str(p.relative_to(ROOT)):sha(p) for p in paths}
def require_approval():
 a=json.loads((ROOT/'PREREG_APPROVED').read_text())
 if not all(a.get(k) for k in ['author','date','zenodo_deposit']) or a.get('hashes')!=freeze_hashes(): raise RuntimeError('Approval absent or stale')
