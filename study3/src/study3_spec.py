"""v0.4 configuration, cell plan and fail-closed approval guard."""
import json,re
from pathlib import Path
import yaml
from .common import sha,verify_manifest
DIRECTIONS=('hostility','technicality','random')
MODES=('direct','think')

def config():return yaml.safe_load(Path('config.yaml').read_text())
def plan(ids):
    for mode in MODES:
        for p in ids:yield p,mode,'regular','none',0.
        for d in DIRECTIONS:
            for a in [.5,1.]:
                for p in ids:yield p,mode,'regular',d,a
    for d in DIRECTIONS:
        for p in ids:yield p,'think','pulse',d,1.
def key(r):return (r['prompt_id'],r['mode'],r['route'],r['direction'],r['dose_fraction'])

def approval_guard(cfg,root=Path('.')):
    # Do not even resolve/read the test path until this returns successfully.
    approved=root/'PREREG_APPROVED';deposit=root/'ZENODO_DEPOSIT.md'
    if not approved.is_file():raise RuntimeError('Main run blocked: PREREG_APPROVED missing')
    text=approved.read_text()
    for path in [cfg['preregistration'],'config.yaml']:
        digest=sha(root/path)
        if digest not in text or Path(path).name not in text:raise RuntimeError('Main run blocked: approval hash/path mismatch: '+path)
    if not deposit.is_file():raise RuntimeError('Main run blocked: ZENODO_DEPOSIT.md missing')
    if not re.search(r'10\.\d{4,9}/[-._;()/:A-Za-z0-9]+',deposit.read_text()):raise RuntimeError('Main run blocked: deposit DOI missing')
    verify_manifest(root/'results/frozen_hashes.sha256')
    return {'approved_sha256':sha(approved),'deposit_sha256':sha(deposit),'verified_prereg_sha256':sha(root/cfg['preregistration']),'verified_config_sha256':sha(root/'config.yaml')}
