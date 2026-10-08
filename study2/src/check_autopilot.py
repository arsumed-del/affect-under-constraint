"""Operational checks with mocked dispatch; never launches main runs or creates approval."""
import copy,io,json
from pathlib import Path
from unittest.mock import patch
from . import autopilot as a
from .run_main import approval_check
from .render_report import render
from .common import save_once

def main():
    # Missing approval and missing deposit both block before any scientific dispatch.
    for files in [set(),{'PREREG_APPROVED'}]:
        with patch.object(Path,'exists',lambda p:str(p) in files),patch.object(a,'launch') as launch:
            assert not a.freeze_ready({});launch.assert_not_called()
    # The actual runner refuses a stale approval, with no fixture approval written.
    with patch.object(Path,'exists',return_value=True),patch.object(Path,'read_text',return_value='Arthur Su 2026-10-04 stale hashes'),patch.object(Path,'read_bytes',return_value=b'current specification'):
        try:approval_check()
        except RuntimeError as e:assert 'current PREREG.md SHA-256' in str(e)
        else:raise AssertionError('Stale approval accepted')
    # A valid local gate is insufficient if public-deposit verification fails.
    with patch.object(Path,'exists',return_value=True),patch.object(a,'validate_local_freeze',return_value={'doi':'10.5281/zenodo.1'}),patch.object(a,'verify_public_deposit',side_effect=RuntimeError('unpublished')),patch.object(a,'progress'),patch.object(a,'append'),patch.object(a,'write_state'):
        state={};assert not a.freeze_ready(state);assert 'unpublished' in state['gate_message'];assert 'freeze' not in state
    cfg={'models':[{'id':'Qwen','slug':'qwen'},{'id':'Phi','slug':'phi'},{'id':'Llama','slug':'llama'}]}
    # Sequential model order and audits; no dispatch without the gate.
    with patch.object(a,'verify_manifest'),patch.object(a,'access_retry',return_value=False),patch.object(a,'freeze_ready',return_value=False),patch.object(a,'launch') as launch:
        a.advance({},cfg);launch.assert_not_called()
    with patch.object(a,'verify_manifest'),patch.object(a,'access_retry',return_value=False),patch.object(a,'freeze_ready',return_value=True),patch.object(a,'passed_models',return_value=cfg['models']),patch.object(a,'launch') as launch:
        a.advance({},cfg);assert launch.call_args.args[1]=='main_qwen'
        a.advance({'main_finished':['qwen']},cfg);assert launch.call_args.args[1]=='audit_qwen'
        a.advance({'main_finished':['qwen'],'audited':['qwen']},cfg);assert launch.call_args.args[1]=='main_phi'
    # A living detached child is adopted rather than duplicated.
    job={'id':'test','pid':123,'log':'test.log','label':'main_qwen','module':'src.run_main','args':['--mode','main']}
    with patch.object(a,'rows',return_value=[{'id':'test','event':'child','pid':456}]),patch.object(a,'alive',side_effect=lambda p:p==456),patch.object(a,'launch') as launch:
        assert a.job_status({'job':job})=='running';launch.assert_not_called()
    with patch.object(a,'rows',return_value=[{'id':'test','event':'finished','returncode':1}]):
        try:a.job_status({'job':job})
        except RuntimeError as e:assert 'No scientific retry' in str(e)
        else:raise AssertionError('Recorded failure retried')
    # Renderer uses only existing estimates, intervals, verdicts and deviation text.
    result=json.loads(Path('results/synthetic_planted.json').read_text());snapshot=copy.deepcopy(result)
    formatted=render(result,'Exact deviation sentinel')
    assert result==snapshot and 'Exact deviation sentinel' in formatted
    for model in result['models']:
        for outcome in model['outcomes'].values():
            for statistic in outcome['statistics'].values():assert str(statistic['estimate']) in formatted and str(statistic['ci']) in formatted
    save_once('results/autopilot_checks.json',{'missing_approval_and_deposit_lock':'PASS','stale_hash_lock':'PASS','unpublished_deposit_lock':'PASS','sequential_dispatch':'PASS','living_child_adoption':'PASS','recorded_failure_blocks':'PASS','format_only_report':'PASS','no_main_generation_or_approval_creation':True})
    print('PASS: watcher gates, sequential dispatch, child adoption, failure block, format-only report')
if __name__=='__main__':main()
