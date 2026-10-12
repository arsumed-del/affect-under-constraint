"""Project-local durable checkpoints, provenance, and progress."""
import os
os.environ['PYTORCH_ENABLE_MPS_FALLBACK']='1'
import gc, hashlib, json, re, fcntl
from datetime import datetime
from pathlib import Path

def rows(path):
    return [json.loads(s) for s in Path(path).read_text().splitlines()] if Path(path).exists() else []

def append(path,row):
    Path(path).parent.mkdir(parents=True,exist_ok=True)
    with Path(path).open('a') as f:
        f.write(json.dumps(row,allow_nan=False)+'\n');f.flush();os.fsync(f.fileno())

def save_once(path,obj):
    Path(path).parent.mkdir(parents=True,exist_ok=True)
    with Path(path).open('x') as f:json.dump(obj,f,indent=2,allow_nan=False);f.write('\n')

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def verify_manifest(path):
    for line in Path(path).read_text().splitlines():
        expected,filename=line.split(None,1)
        assert sha(filename.lstrip('* '))==expected,f'Hash mismatch: {filename}'

def progress(message):
    stamp=datetime.now().astimezone().isoformat()
    print(stamp+' '+message,flush=True)
    if os.environ.get('STATUS_LOG_ONLY')=='1':return
    Path('logs').mkdir(exist_ok=True)
    with Path('logs/status.lock').open('a') as lock:
        fcntl.flock(lock,fcntl.LOCK_EX)
        p=Path('STATUS.md');s=p.read_text()
        s=re.sub(r'^\*\*[^\n]*',lambda _: '**'+message+'**',s,count=1,flags=re.M)
        s+='\n- '+stamp+': '+message+'\n'
        tmp=Path(f'STATUS.md.{os.getpid()}.tmp');tmp.write_text(s);tmp.replace(p)

def free():
    import torch
    gc.collect();torch.mps.empty_cache()

def calibration_paths(spec,cfg):
    return Path(cfg['dose_selection']['output'].format(slug=spec['slug'])),Path(f'results/calibration_{spec["slug"]}.sha256')
