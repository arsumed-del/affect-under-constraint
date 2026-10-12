"""Guarded v0.4 runner. --dry-run uses exactly two calibration prompts only."""
import argparse,json,time
from pathlib import Path
from types import SimpleNamespace
from .study3_spec import config,plan,key,approval_guard
from .common import rows,sha,append,save_once,progress,free,verify_manifest
from .check_common import guarded,record_generation

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--dry-run',action='store_true');args=parser.parse_args()
    cfg=config()
    if args.dry_run:
        prompt_path=cfg['prompts']['calibration'];prompts=rows(prompt_path)[:2]
        assert [p['id'] for p in prompts]==['s2c00','s2c01']
        path=cfg['outputs']['dry_run'];verification={'dry_run':True,'test_file_accessed':False}
    else:
        verification=approval_guard(cfg)
        # Only after ALL approval/deposit/frozen-code checks may test data be opened.
        prompt_path=cfg['prompts']['test']['path']
        assert sha(prompt_path)==cfg['prompts']['test']['sha256']
        prompts=rows(prompt_path);assert len(prompts)==cfg['prompts']['test']['count'];path=cfg['outputs']['raw']
    verify_manifest('results/stageD_inputs.sha256')
    verify_manifest('results/stageD_runner_hashes.sha256')
    provenance={'prereg_sha256':sha(cfg['preregistration']),'config_sha256':sha('config.yaml'),'runner_manifest_sha256':sha('results/stageD_runner_hashes.sha256'),'prompt_sha256':sha(prompt_path),'verification':verification}
    existing=rows(path);done={key(r):r for r in existing};assert len(done)==len(existing)
    for r in existing:assert r['provenance']==provenance,'Resume provenance mismatch'
    cells=list(plan([p['id'] for p in prompts]));assert len(cells)==17*len(prompts)
    assert set(done)<=set(cells)
    if len(done)==len(cells):progress(f'Stage D dry-run already complete: {len(done)} cells; provenance verified.');return
    import torch
    from .main_model import Model
    from .base_model import cell_seed
    from .metrics import EmotionClassifier
    model=Model(cfg['model']);assert model.layer_index==cfg['model']['layer_index']
    clf=EmotionClassifier(cfg['classifier']['local_path'])
    vectors={d:torch.load(v['path'],map_location='cpu',weights_only=True)['vector'] for d,v in cfg['directions'].items()}
    question=Path(cfg['prompts']['downstream']).read_text().strip();openers=json.loads(Path(cfg['prompts']['openers']).read_text())
    assert len(openers['hostile'])==len(openers['warm'])==12
    prompts={p['id']:p for p in prompts};start=time.monotonic();initial=len(done)
    for cell in cells:
        if cell in done:continue
        pid,mode,route,d,a=cell;model.thinking=mode=='think';alpha=a*cfg['calibration']['alpha_top'];norm=cfg['norm']['value'];vector=vectors.get(d)
        seed=cell_seed(cfg['model']['id'],pid,f'warm_constraint_{mode}_{route}',d,cfg['calibration']['grid'].index(a))
        messages=model.messages(prompts[pid]['text'],cfg['condition']);t=time.monotonic()
        g=model.generate_main(messages,seed,cfg,alpha,norm,vector,pulse=route=='pulse');free()
        row={'schema_version':'study3-v0.4','model':cfg['model']['id'],'prompt_id':pid,'mode':mode,'route':route,'direction':d,'dose_fraction':a,'alpha':alpha,'seed':seed,'condition':'warm_constraint',**record_generation(g),'answer_prefix_ids':g.answer_prefix_ids,'entropy':g.entropy,'token_entropies':g.token_entropies,'pulse_cache_discarded':g.pulse_cache_discarded,'first_answer_from_unsteered_reencoding':g.first_answer_from_unsteered_reencoding}
        row['answer_perplexity']=model.segment_ppl(g.answer_prefix_ids,g.answer_ids)
        row['trace_perplexity']=model.segment_ppl(g.prompt_ids+g.token_ids[:g.token_ids.index(model.open_think)+1],g.thinking_ids) if g.thinking_ids else None
        row['answer_classifier']=clf.score(g.answer);row['EH_answer']=row['answer_classifier']['eh'];row['EW']=row['answer_classifier']['ew']
        windows=[]
        for offset in range(0,len(g.thinking_ids),cfg['measures']['trace_window_tokens']):
            ids=g.thinking_ids[offset:offset+cfg['measures']['trace_window_tokens']]
            windows.append({'start':offset,'token_count':len(ids),**clf.score(model.tokenizer.decode(ids,skip_special_tokens=True))})
        row['trace_windows']=windows
        row['EH_trace']=sum(w['eh'] for w in windows)/len(windows) if windows and all(w['eh'] is not None for w in windows) else None
        row['LHP'],row['opener_logprobs']=model.lhp(g.answer_prefix_ids,openers,alpha,norm,vector,route=='pulse')
        baseline=done.get((pid,mode,'regular','none',0.))
        rating=model.ratings(messages,g,question,alpha,norm,vector,SimpleNamespace(**baseline) if baseline else g,hostility_vector=vectors['hostility'])
        row['ratings']=rating;row.update(R_full=rating['full'],R_text=rating['text_only'],R_zero=rating['R_zero'])
        row['C']=row['R_full']-row['R_zero'];row['X']=row['R_text']-row['R_zero'];row['H']=row['R_full']-row['R_text']
        row['total_seconds']=time.monotonic()-t;row['provenance']=provenance
        append(path,row);done[cell]=row
        assert rating['rating_prefix_text']==cfg['ratings']['prefix']
        if not a:assert abs(row['H'])<=cfg['ratings']['zero_tolerance']
        assert row['EH_answer'] is not None and (mode=='direct' or row['EH_trace'] is not None),'Classifier failed; inspect saved cell'
        del g;free()
        remaining=(len(cells)-len(done))*(time.monotonic()-start)/max(1,len(done)-initial)
        progress(f'Stage D {"dry-run" if args.dry_run else "main"}: {len(done)}/{len(cells)} saved; {pid} {mode} {route} {d} a={a}; provisional remaining {remaining/60:.1f} min.')
    progress(f'Stage D {"dry-run" if args.dry_run else "main"} complete: {len(done)} cells, exact provenance and baseline checks passed.')
if __name__=='__main__':guarded(main)
