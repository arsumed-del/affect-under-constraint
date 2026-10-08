"""Read-only completeness/provenance audit before the frozen analysis runs."""
import os
os.environ['PYTORCH_ENABLE_MPS_FALLBACK']='1'
import argparse
import hashlib
import json
import math
from pathlib import Path
import yaml
from .schema import validate
from .model_utils import cell_seed
from .run_main import approval_check
from .common import verify_manifest,calibration_paths
from transformers import AutoConfig

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--model',required=True)
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    model_id=args.model
    cfg=yaml.safe_load(Path('config.yaml').read_text())
    spec=next(s for s in cfg['models'] if s['id']==model_id)
    calibration_path,calibration_manifest=calibration_paths(spec,cfg)
    verify_manifest(calibration_manifest)
    layers=AutoConfig.from_pretrained(model_id,token=None if spec['gated'] else False).num_hidden_layers
    approval_check()
    for manifest in ['results/specification_hashes.sha256','results/analysis_frozen.sha256']:
        verify_manifest(manifest)
    cfg=yaml.safe_load(Path('config.yaml').read_text())
    path=Path(cfg["outputs"]["raw"])/f"{spec['slug']}_main.jsonl"
    contents=path.read_bytes()
    assert contents.endswith(b'\n'),'Incomplete trailing record'
    records=[validate(json.loads(line)) for line in contents.splitlines()]
    prompts={r['id']:r for r in (json.loads(s) for s in Path(cfg['prompts']['test']).read_text().splitlines())}
    expected={(p,c,d,i) for p in prompts for c in cfg['conditions'] for d,i in [('none',0)]+[(d,i) for d in ['hostility','technicality','random'] for i in range(1,6)]}
    actual={(r['prompt_id'],r['condition'],r['direction'],r['alpha_index']) for r in records}
    assert len(records)==len(actual)==2560 and actual==expected
    baselines={(r['prompt_id'],r['condition']):r for r in records if r['alpha_index']==0}
    assert len(baselines)==160
    cal=json.loads(calibration_path.read_text())
    hashes={k:hashlib.sha256(Path(f).read_bytes()).hexdigest() for k,f in [('prereg_sha256','PREREG.md'),('config_sha256','config.yaml'),('calibration_sha256',calibration_path)]}
    missing={'full_classifier':0,'first_quarter_classifier':0,'last_quarter_classifier':0,'timecourse_short_outputs':0,'prefix_template_fallbacks':0}
    for r in records:
        assert r['origin']=='main' and r['model']==model_id
        assert r['prompt_text']==prompts[r['prompt_id']]['text']
        assert r['prompt_type']==prompts[r['prompt_id']]['type']
        assert all(r['provenance'][k]==v for k,v in hashes.items())
        assert r['provenance']['direction_hashes']==cal['direction_hashes']
        assert r['seed']==cell_seed(r['model'],r['prompt_id'],r['condition'],r['direction'],r['alpha_index'])
        assert r['alpha']==cal['grid'][r['alpha_index']]
        assert r['normalized_alpha']==cfg['dose_selection']['grid_fractions'][r['alpha_index']]
        assert math.isclose(r['ppl_ratio'],r['perplexity']/baselines[(r['prompt_id'],r['condition'])]['perplexity'],rel_tol=1e-12)
        assert r['n_tokens']==len(r['entropy_per_token'])
        assert math.isclose(r['entropy'],sum(r['entropy_per_token'])/r['n_tokens'],rel_tol=1e-12)
        assert all(len(r['opener_logprobs'][k])==12 for k in ['hostile','warm'])
        lhp=sum(r['opener_logprobs']['hostile'])/12-sum(r['opener_logprobs']['warm'])/12
        assert abs(lhp-r['lhp'])<1e-12
        assert r['provenance']['layer_index']==round(.5*layers)
        assert 'layerwise_lhp' not in r
        assert r['rating_prefix']['identical_visible_ids']
        missing['prefix_template_fallbacks']+=not r['rating_prefix']['template_prefix_exact']
        assert math.isclose(r['carryover'],r['rating_hidden']-r['rating_text_only'],abs_tol=1e-12)
        assert 0<=r['rating_hidden']<=9 and 0<=r['rating_text_only']<=9
        for key,countkey in [('full','full_classifier'),('first_quarter','first_quarter_classifier'),('last_quarter','last_quarter_classifier')]:
            score=r['classifier'][key]
            if score['error']=='fewer_than_8_tokens':
                continue
            if score['error'] is not None:
                missing[countkey]+=1
                assert score['eh'] is None and score['ew'] is None
        if r['n_tokens']<8:
            missing['timecourse_short_outputs']+=1
            assert r['leak_timecourse'] is None
    result={'status':'PASS','scope':model_id,'raw_path':str(path),'raw_sha256':hashlib.sha256(contents).hexdigest(),'records':len(records),'unique_cells':len(actual),'prompts':len(prompts),'shared_baselines':len(baselines),'provenance_hashes':hashes,'operational_missing_counts':missing,'no_raw_edits':True}
    with Path(args.output).open('x') as f:json.dump(result,f,indent=2)
    print(json.dumps(result,indent=2),flush=True)

if __name__=='__main__':main()
