"""Crash recovery checks on derived synthetic outputs, never main data."""
import io,json,os
from pathlib import Path
from unittest.mock import patch
from . import autopilot as a
from .analyze import report
from .common import save_once

def main():
    root=Path.cwd();result=json.loads(Path('results/synthetic_planted.json').read_text())
    fixture=root/'data/synthetic/autopilot_recovery';(fixture/'results').mkdir(parents=True,exist_ok=True)
    (fixture/'results/analysis.json').write_text(json.dumps(result))
    (fixture/'results/analysis.md').write_text(report(result))
    os.chdir(fixture)
    try:
        job={'id':'recovery-fixture','label':'analysis','module':'src.analyze','args':[],'input_hashes':{}}
        with patch.object(a,'append'):
            assert a.recover_completed_output(job)
        with patch.object(a,'rows',return_value=[]),patch.object(a,'alive',return_value=False),patch.object(a,'recover_completed_output',return_value=False),patch.object(a,'append'),patch.object(a,'write_state'),patch.object(a,'launch') as launch,patch.object(Path,'open',return_value=io.StringIO()):
            state={'job':dict(job,label='main_qwen',module='src.run_main',args=['--mode','main'])}
            assert a.job_status(state)=='running'
            assert launch.call_args.args[1:] == ('main_qwen','src.run_main',['--mode','main'])
    finally:os.chdir(root)
    save_once('results/autopilot_recovery_checks.json',{'complete_derived_output_adopted':'PASS','interrupted_job_same_command_resume':'PASS','no_main_data_access':True})
    print('PASS: interrupted job resumes same command; complete derived outputs adopted')
if __name__=='__main__':main()
