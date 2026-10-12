"""Only Stage A pre-approval calibration cells; no test data or main run."""
import math,time
from types import SimpleNamespace
import torch
from .check_common import *
from .model_utils import Model,cell_seed
from .metrics import EmotionClassifier

@torch.inference_mode()
def segment_ppl(model,prefix,tokens):
    if not tokens:return None
    output=model.model(input_ids=model.tensor(prefix+tokens),use_cache=False)
    logits=output.logits[0,len(prefix)-1:len(prefix)+len(tokens)-1].float()
    return math.exp(-logits.log_softmax(-1).gather(-1,model.tensor(tokens).T).mean().item())

def main():
    cfg=config()
    for manifest in ['checks_source_hashes','reused_hashes','checks_code_hashes']:verify_manifest('results/'+manifest+'.sha256')
    prompts=rows(cfg['calibration_prompts'])[:20]
    assert [p['id'] for p in prompts]==[f's2c{i:02}' for i in range(20)]
    path='data/checks/stageA_cells.jsonl';existing=rows(path)
    done={(r['prompt_id'],r['mode'],r['dose_fraction']):r for r in existing}
    assert len(done)==len(existing)
    plan=[(mode,a,p) for mode in ['direct','think'] for a in [0,1] for p in prompts]
    model=Model(cfg['model']);assert model.layer_index==cfg['layer_index']==18
    classifier=EmotionClassifier(cfg['classifier']['local_path'])
    vector=torch.load('data/reused/qwen3-4b_hostility.pt',map_location='cpu',weights_only=True)['vector']
    question=Path(cfg['downstream_question']).read_text().strip()
    prefix=json.loads(Path('results/rating_prefix.json').read_text())
    start=time.monotonic();initial=len(done)
    for mode,a,p in plan:
        key=(p['id'],mode,a)
        if key in done:continue
        model.thinking=mode=='think';alpha=a*cfg['alpha_max'];norm=cfg['mean_resid_norm']
        seed=cell_seed(cfg['model']['id'],p['id'],'study3_preapproval_warm_'+mode,'hostility' if a else 'none',2 if a else 0)
        messages=model.messages(p['text'],cfg['warm_constraint']);t=time.monotonic()
        g=model.generate(messages,seed,max_new_tokens=200,alpha=alpha,norm=norm,vector=vector if a else None)
        row={'model':cfg['model']['id'],'prompt_id':p['id'],'mode':mode,'condition':'warm_constraint','direction':'hostility','dose_fraction':a,'alpha':alpha,'seed':seed,**record_generation(g)}
        g.cache=None;free()
        answer_start=len(g.token_ids)-len(g.answer_ids)
        row['answer_perplexity']=segment_ppl(model,g.prompt_ids+g.token_ids[:answer_start],g.answer_ids)
        row['answer_classifier']=classifier.score(g.answer)
        windows=[]
        for offset in range(0,len(g.thinking_ids),cfg['trace_window_tokens']):
            ids=g.thinking_ids[offset:offset+cfg['trace_window_tokens']]
            text=model.tokenizer.decode(ids,skip_special_tokens=True)
            windows.append({'start':offset,'token_count':len(ids),'text':text,**classifier.score(text)})
        row['trace_windows']=windows
        row['EH_trace']=sum(w['eh'] for w in windows)/len(windows) if windows and all(w['eh'] is not None for w in windows) else None
        row['EH_answer']=row['answer_classifier']['eh']
        base=done.get((p['id'],mode,0))
        baseline=SimpleNamespace(**base) if base else g
        row['ratings']=model.ratings(messages,g,question,alpha=alpha,norm=norm,vector=vector,baseline=baseline)
        row['total_seconds']=time.monotonic()-t
        row['calibration_sha256']=sha('data/reused/qwen3-4b_amendP1.json')
        row['code_manifest_sha256']=sha('results/checks_code_hashes.sha256')
        append(path,row);done[key]=row
        assert row['ratings']['rating_prefix_ids']==prefix['ids']
        if a==0:assert abs(row['ratings']['difference'])<=.01,f'Baseline rating disagreement: {key}: {row["ratings"]["difference"]}'
        del g;free()
        elapsed=time.monotonic()-start;remaining=(80-len(done))*elapsed/max(1,len(done)-initial)
        progress(f'Stage A: {len(done)}/80 cells saved; {mode}, a={a}, {p["id"]}. Estimated remaining {remaining/60:.1f} min (mixed-mode estimate).')
    progress('Stage A: all 80 cells saved; validity summaries and integrity audit next. No main-study data generated.')
if __name__=='__main__':guarded(main)
