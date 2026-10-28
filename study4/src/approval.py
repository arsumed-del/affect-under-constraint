"""Fail-closed main-run guard, before test prompts are read."""
import json
from .common import ROOT, sha

def require_approval():
    approval=json.loads((ROOT/'PREREG_APPROVED').read_text())
    if not approval.get('name') or not approval.get('date'):raise RuntimeError('Approval needs name and date')
    for name in ['Study4_Authorship_PREREG_v0.6_draft.md','framings.json','config.yaml']:
        if approval.get('sha256',{}).get(name)!=sha(ROOT/name):raise RuntimeError('Approval hash mismatch: '+name)
    freeze=json.loads((ROOT/'validation/analysis_freeze.json').read_text())
    actual={str(p.relative_to(ROOT)):sha(p) for p in sorted((ROOT/'analysis').glob('*.py'))}
    if freeze['files']!=actual:raise RuntimeError('Analysis changed since synthetic validation freeze')
    if not json.loads((ROOT/'validation/synthetic/summary.json').read_text())['passed']:raise RuntimeError('Synthetic validation has not passed')
    return approval
