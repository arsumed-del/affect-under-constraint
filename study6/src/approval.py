"""Author-created approval only; candidate manifest is never approval."""
import json
from .common import ROOT, config, sha, verify_inputs, verify_environment

def freeze_hashes():
    cfg = config()
    files = [ROOT/cfg['preregistration'],ROOT/'config_s6.yaml',ROOT/'generic_answer.json',
             ROOT/'run_pilot.command',ROOT/'run_main.command',ROOT/'build_artifacts.py',ROOT/'__init__.py']
    for folder in ('src','analysis','tests'): files.extend(sorted((ROOT/folder).glob('*.py')))
    hashes = {str(p.relative_to(ROOT)):sha(p) for p in files}
    hashes.update({v['path']:v['sha256'] for v in cfg['inputs'].values()})
    hashes.update({cfg['model']['local_path']+'/'+k:v for k,v in cfg['model_files'].items()})
    return hashes

def require_approval():
    cfg = config(); verify_inputs(cfg); verify_environment(cfg)
    path = ROOT/'PREREG_APPROVED'
    if not path.exists(): raise RuntimeError('Main requires author-created PREREG_APPROVED and prior Zenodo deposit')
    obj = json.loads(path.read_text())
    if not all(obj.get(k) for k in ('author','date','zenodo_deposit')): raise RuntimeError('Incomplete approval/deposit record')
    if obj.get('hashes') != freeze_hashes(): raise RuntimeError('Approval hashes do not match complete build and inputs')
    return obj
