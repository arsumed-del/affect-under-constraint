"""Resumable main runner, with a separate calibration-only three-cell timing mode."""
import os
os.environ['PYTORCH_ENABLE_MPS_FALLBACK']='1'
import argparse
import hashlib
import json
import re
import time
from datetime import datetime,timedelta
import unicodedata
from pathlib import Path
import emoji
import numpy as np
import torch
import yaml
from .model_utils import Model,cell_seed
from .metrics import EmotionClassifier,perplexity,entropy
from .common import rows,append,progress,free,verify_manifest,calibration_paths
from .schema import SCHEMA_VERSION,validate

def main_progress(completed,total,run_start,initial_count,key,model_id):
    """Operational progress only; never alters generation or analysis."""
    now=datetime.now().astimezone()
    elapsed=time.monotonic()-run_start
    per_cell=elapsed/max(1,completed-initial_count)
    remaining=max(0,total-completed)*per_cell
    eta=now+timedelta(seconds=remaining)
    message=f'Stage 3 {model_id}: {completed}/{total} cells saved ({100*completed/total:.1f}%); latest {key}; remaining {remaining/3600:.2f} h; ETA {eta.strftime("%Y-%m-%d %H:%M %Z")}.'
    progress(message)

def approval_check():
    path=Path('PREREG_APPROVED')
    if not path.exists():
        raise RuntimeError('Stage 3 locked: PREREG_APPROVED is absent')
    approval=path.read_text()
    for filename in ['PREREG.md','config.yaml']:
        digest=hashlib.sha256(Path(filename).read_bytes()).hexdigest()
        if digest not in approval:
            raise RuntimeError(f'Stage 3 locked: approval does not contain current {filename} SHA-256')
    if not re.search(r'Arthur\s+Su',approval,re.I) or not re.search(r'\d{4}[-/]\d{1,2}[-/]\d{1,2}',approval):
        raise RuntimeError('Stage 3 locked: approval must contain Arthur Su and a date')
    deposit=Path('ZENODO_DEPOSIT.md')
    if not deposit.exists() or not re.search(r'10\.5281/zenodo\.\d+',deposit.read_text()):
        raise RuntimeError('Stage 3 locked: Study 2 Zenodo deposit with DOI required')
    verify_manifest('results/analysis_frozen.sha256')


def intrusions(text,token_ids,tokenizer,lexicon,eh):
    words=re.findall(r"\b\w+\b",text.lower())
    hits=sum(w in lexicon for w in words) if eh is not None and eh<.5 else None
    nonlatin=0
    for tid in token_ids:
        decoded=tokenizer.decode([tid],skip_special_tokens=True)
        if any(unicodedata.category(c).startswith('L') and 'LATIN' not in unicodedata.name(c,'') for c in decoded):
            nonlatin+=1
    return hits,{'emoji_count':len(emoji.emoji_list(text)),'non_latin_token_count':nonlatin}

def cell(model,classifier,cfg,prompt,condition,direction,index,calibration,baseline,origin):
    start=time.monotonic()
    alpha=calibration['grid'][index]
    spec=model.spec
    slug=spec['slug']
    norm=calibration['mean_resid_norm']
    vector=None
    if direction!='none':
        path=Path(f'data/directions/{slug}_{direction}.pt')
        assert hashlib.sha256(path.read_bytes()).hexdigest()==calibration['direction_hashes'][direction]
        vector=torch.load(path,map_location='cpu',weights_only=True)['vector']
    seed=cell_seed(spec['id'],prompt['id'],condition,direction,index)
    messages=model.messages(prompt['text'],cfg['conditions'][condition])
    gen=model.generate(messages,seed,max_new_tokens=cfg['generation']['max_new_tokens'],alpha=alpha,norm=norm,vector=vector)
    generation_seconds=gen.seconds
    rating_start=time.monotonic()
    ratings=model.ratings(messages,gen,Path(cfg['prompts']['downstream']).read_text().strip())
    rating_seconds=time.monotonic()-rating_start
    ppl=perplexity(model,messages,gen.token_ids)
    full=classifier.score(gen.text)
    first=last={'eh':None,'ew':None,'error':'fewer_than_8_tokens'}
    if len(gen.token_ids)>=8:
        quarter=len(gen.token_ids)//4
        first=classifier.score(model.tokenizer.decode(gen.token_ids[:quarter],skip_special_tokens=True))
        last=classifier.score(model.tokenizer.decode(gen.token_ids[-quarter:],skip_special_tokens=True))
    leak=None if first['eh'] is None or last['eh'] is None else last['eh']-first['eh']
    lexical,offchannel=intrusions(gen.text,gen.token_ids,model.tokenizer,set(Path(cfg['prompts']['lexicon']).read_text().split()),full['eh'])
    entropies=[float(-(v.float().softmax(-1)*v.float().log_softmax(-1)).sum()) for v in gen.logits]
    record={'schema_version':SCHEMA_VERSION,'origin':origin,'model':spec['id'],'prompt_id':prompt['id'],'prompt_type':prompt['type'],'prompt_text':prompt['text'],'condition':condition,'direction':direction,'alpha':alpha,'alpha_index':index,'normalized_alpha':cfg['dose_selection']['grid_fractions'][index],'seed':seed,'text':gen.text,'prompt_token_ids':gen.prompt_ids,'token_ids':gen.token_ids,'n_tokens':len(gen.token_ids),'eh':full['eh'],'ew':full['ew'],'classifier':{'full':full,'first_quarter':first,'last_quarter':last},'entropy':float(np.mean(entropies)),'entropy_per_token':entropies,'perplexity':ppl,'ppl_ratio':1. if index==0 else ppl/baseline['perplexity'],'eh_first_quarter':first['eh'],'eh_last_quarter':last['eh'],'leak_timecourse':leak,'leak_lexical':lexical,'offchannel':offchannel,'rating_text_only':ratings['text_only'],'rating_hidden':ratings['hidden'],'carryover':ratings['hidden']-ratings['text_only'],'rating_prefix':{k:v for k,v in ratings.items() if k not in ['text_only','hidden']},'peak_driver_memory':gen.peak_driver_memory,'provenance':{'prereg_sha256':hashlib.sha256(Path('PREREG.md').read_bytes()).hexdigest(),'config_sha256':hashlib.sha256(Path('config.yaml').read_bytes()).hexdigest(),'calibration_sha256':hashlib.sha256(calibration_paths(spec,cfg)[0].read_bytes()).hexdigest(),'direction_hashes':calibration['direction_hashes'],'layer_index':model.layer_index,'mean_resid_norm':norm}}
    del gen
    free()
    opener_start=time.monotonic()
    openers=json.loads(Path(cfg['prompts']['openers']).read_text())
    scores={}
    for kind,texts in openers.items():
        scores[kind]=[model.opener_logprob(messages,t,alpha,norm,vector) for t in texts]
    record['opener_logprobs']=scores
    record['lhp']=float(np.mean(scores['hostile'])-np.mean(scores['warm']))
    record['timings']={'generation_seconds':generation_seconds,'ratings_seconds':rating_seconds,'openers_seconds':time.monotonic()-opener_start,'cell_total_seconds':time.monotonic()-start}
    record['peak_driver_memory']=max(record['peak_driver_memory'],torch.mps.driver_allocated_memory())
    return validate(record)

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--mode',choices=['timing','main'],required=True)
    parser.add_argument('--model',help='Run only this configured model')
    args=parser.parse_args()
    # Check before even reading test prompts or loading a model.
    if args.mode=='main':
        approval_check()
    verify_manifest('results/specification_hashes.sha256')
    cfg=yaml.safe_load(Path('config.yaml').read_text())
    if args.model and args.model not in [s['id'] for s in cfg['models']]:
        raise ValueError('Model is not in the frozen configuration')
    for spec in cfg['models']:
        if args.model and spec['id']!=args.model:continue
        calibration_path,calibration_manifest=calibration_paths(spec,cfg)
        if not calibration_path.exists():
            if args.model:raise RuntimeError('Missing model calibration')
            continue
        verify_manifest(calibration_manifest)
        cal=json.loads(calibration_path.read_text())
        if cal['status']!='PASS':
            if args.model:raise RuntimeError('Model excluded by manipulation check; no further generation allowed')
            continue
        slug=spec['slug']
        if args.mode=='timing':
            prompt=rows(cfg['prompts']['calibration'])[0]
            plan=[(prompt,'warm_constraint','none',0),(prompt,'warm_constraint','hostility',5),(prompt,'warm_constraint','technicality',5)]
            path=Path(f'data/_timing/{slug}.jsonl')
        else:
            prompts=rows(cfg['prompts']['test'])
            plan=[]
            for prompt in prompts:
                for condition in cfg['conditions']:
                    plan.append((prompt,condition,'none',0))
                    plan.extend((prompt,condition,d,i) for d in ['hostility','technicality','random'] for i in range(1,6))
            path=Path(cfg['outputs']['raw'])/f'{slug}_main.jsonl'
        path.parent.mkdir(parents=True,exist_ok=True)
        existing=rows(path)
        done={(r['prompt_id'],r['condition'],r['direction'],r['alpha_index']):validate(r) for r in existing}
        assert len(done)==len(existing),'Duplicate existing cells'
        for row in existing:
            for key,filename in [('prereg_sha256','PREREG.md'),('config_sha256','config.yaml'),('calibration_sha256',calibration_path)]:
                current=hashlib.sha256(Path(filename).read_bytes()).hexdigest()
                if row['provenance'][key]!=current:
                    assert args.mode=='timing' and key in ['prereg_sha256','config_sha256'],f'Checkpoint provenance differs: {filename}'
                    amendment=json.loads(Path('results/amendment3_1_compatibility.json').read_text())
                    assert row['provenance']['prereg_sha256']==amendment['old_prereg_sha256'] and row['provenance']['config_sha256']==amendment['old_config_sha256']
                    assert current==amendment['new_'+key]
                    previous=yaml.safe_load((Path(amendment['archive'])/'config.yaml').read_text())
                    present=yaml.safe_load(Path('config.yaml').read_text())
                    for config in [previous,present]:
                        config.pop('analysis');config['experiment'].pop('prereg_version')
                    assert previous==present,'Generation settings changed; old timing cannot be reused'
        expected={(p['id'],c,d,i) for p,c,d,i in plan}
        assert set(done)<=expected,'Unexpected cells in checkpoint'
        if set(done)==expected and (args.mode!='timing' or Path(f'results/stage2b_timing_{slug}.json').exists()):
            progress(f'{args.mode} checkpoint already complete: {len(done)} cells; no model loaded and no generation performed.')
            continue
        setup_start=time.monotonic()
        model=Model(spec)
        classifier=EmotionClassifier(cfg['classifier']['id'])
        setup_seconds=time.monotonic()-setup_start
        run_start=time.monotonic()
        initial_count=len(done)
        for prompt,condition,direction,index in plan:
            key=(prompt['id'],condition,direction,index)
            if key in done:
                continue
            baseline=done.get((prompt['id'],condition,'none',0))
            if index and baseline is None:
                raise RuntimeError('Missing shared alpha-zero baseline')
            if args.mode=='main':
                approval_check();verify_manifest('results/specification_hashes.sha256');verify_manifest(calibration_manifest)
            record=cell(model,classifier,cfg,prompt,condition,direction,index,cal,baseline,args.mode)
            if args.mode=='main':
                try:
                    approval_check();verify_manifest('results/specification_hashes.sha256');verify_manifest(calibration_manifest)
                except Exception:
                    preserved=Path('data/_superseded')/(datetime.now().strftime('%Y%m%dT%H%M%S%f')+'_specification_changed_during_cell.jsonl')
                    append(preserved,record)
                    raise
            append(path,record)
            done[key]=record
            if args.mode=='main':
                main_progress(len(done),len(plan),run_start,initial_count,key,spec['id'])
            else:
                progress(f'Stage 2b {args.mode}: {len(done)}/{len(plan)} cells saved; {key}; cell time {record["timings"]["cell_total_seconds"]:.1f}s.')
            free()
        if args.mode=='timing':
            totals=[r['timings']['cell_total_seconds'] for r in done.values()]
            result={'model':spec['id'],'cells':len(totals),'planned_main_cells':80*2*(1+3*5),'setup_seconds':setup_seconds,'mean_cell_seconds':float(np.mean(totals)),'estimated_main_hours':(setup_seconds+float(np.mean(totals))*2560)/3600,'timing_cells':[[p['id'],c,d,i] for p,c,d,i in plan]}
            with Path(f'results/stage2b_timing_{slug}.json').open('x') as f:
                json.dump(result,f,indent=2)
            progress(f'Stage 2b timing finished: estimated {spec["id"]} Stage 3 runtime {result["estimated_main_hours"]:.2f} hours from three calibration-only cells.')
        del model,classifier
        free()

if __name__=='__main__':
    try:main()
    except Exception:
        import traceback
        error=traceback.format_exc()
        append('results/runner_errors.jsonl',{'error':error})
        with Path('DEVIATIONS.md').open('a') as f:f.write('\n### Runner stopped\n\n```text\n'+error+'```\n')
        progress('Runner BLOCKED: exact error saved in results/runner_errors.jsonl and DEVIATIONS.md. No automatic retry; no ETA.')
        raise
