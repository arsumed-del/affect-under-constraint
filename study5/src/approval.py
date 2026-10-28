"""Fail-closed approval check. This module never creates approval."""
import json
from .common import ROOT, sha, config, verify_inputs

def freeze_hashes():
    cfg = config()
    files = [ROOT/cfg['preregistration'], ROOT/'framings_s5.json', ROOT/'config_s5.yaml',
             ROOT/'run_pilot.command', ROOT/'run_main.command', ROOT/'build_artifacts.py']
    for folder in ['src','analysis','tests']:
        files += sorted((ROOT/folder).glob('*.py'))
    hashes = {str(p.relative_to(ROOT)):sha(p) for p in files}
    hashes.update({v['path']:v['sha256'] for v in cfg['inputs'].values()})
    hashes.update({cfg['model']['local_path']+'/'+name:value for name,value in cfg['model_files'].items()})
    return hashes

def require_approval():
    cfg = config(); verify_inputs(cfg)
    path = ROOT/'PREREG_APPROVED'
    if not path.exists(): raise RuntimeError('Main run requires author-created PREREG_APPROVED and prior Zenodo deposit')
    obj = json.loads(path.read_text())
    if not all(obj.get(k) for k in ['author','date','zenodo_deposit']): raise RuntimeError('Incomplete approval/deposit record')
    if obj.get('hashes') != freeze_hashes(): raise RuntimeError('Approval hashes do not match the complete build and inputs')
    return obj
