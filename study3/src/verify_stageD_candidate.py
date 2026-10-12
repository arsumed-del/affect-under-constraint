"""Replay saved synthetic evidence against the final candidate code."""
import json
from pathlib import Path
from .analyze import analyze,render
from .validate_synthetic import generate
from .study3_spec import config
from .common import rows,sha,save_once,progress

def main():
    cfg=config();root=Path('data/synthetic/v04');scenarios=[]
    for p in sorted(root.glob('*_analysis.json')):
        expected=json.loads(p.read_text());data=rows(root/(p.name.replace('_analysis.json','.jsonl')))
        actual=analyze(data,cfg)
        assert actual==expected,p.name
        assert 'Exploratory results' in render(actual)
        scenarios.append(p.stem)
    records=rows(root/'null_replicates.jsonl');assert len(records)==200 and len({r['replicate'] for r in records})==200
    for r in records:
        result=analyze(generate('null',r['data_seed']),cfg,resamples=1000,seed=r['bootstrap_seed'],exploratory=False)
        for h in ['P1','P2']:assert result['hypotheses'][h]['verdict']==r[h]
    empty=analyze([],cfg);assert empty==json.loads(Path('results/stageD_empty_input_check.json').read_text())
    result={'status':'PASS','analysis_sha256':sha('src/analyze.py'),'config_sha256':sha('config.yaml'),'scenarios_exactly_reproduced':scenarios,'null_replicates_exactly_reproduced':200,'empty_case_exactly_reproduced':True,'test_prompts_accessed':False}
    save_once('results/stageD_candidate_replay.json',result)
    progress('Stage D final analysis candidate replay PASS: all saved scenario outputs and 200 null-replicate verdicts reproduced exactly; candidate SHA recorded.')
if __name__=='__main__':main()
