"""Three arms, fresh unsteered replay, no execution on import."""
import argparse, gc, json, time, resource, subprocess
from .common import *
from .assembly import Assembly
from .projection import observe
from study4.src.runner import Backend as Base, assert_no_hooks
class Backend(Base):
    def trace_context(self,prompt,source,value,context,assembly):
        self.cfg['condition']=assembly.f['systems'][context]
        tr=super().trace(prompt,source,value,self.cfg['generation']['thinking_cap'])
        assert tr['prompt_ids']==assembly.prompt_ids(prompt,context)
        prefix,_=assembly.assemble(prompt,tr,context)
        assert prefix==tr['prompt_ids']+tr['pre_trace_ids']+tr['trace_ids']+assembly.marker('think_close')+assembly.marker('answer_separator')
        tr['steered_prompt_positions']=0 if source=='unsteered' else len(tr['prompt_ids'])
        tr['steered_system_positions']=0 if source=='unsteered' else len(assembly.f['system_turn_ids'][context])
        return tr

def plan(ps):
    for p in ps:
        for c in CONTEXTS:
            for s in SOURCES: yield (p['id'],s,c,c,'generated')
        for g,r in [('N','M'),('M','N')]:
            for s in SOURCES: yield (p['id'],s,g,r,'crossover')
        for c in ('N','M'):
            for s in SOURCES: yield (p['id'],s,c,c,'fixed_answer')

def main():
    a=argparse.ArgumentParser();a.add_argument('--mode',choices=['pilot','main'],required=True);args=a.parse_args()
    lock=process_lock();c=config();verify(c)
    if args.mode=='main': require_approval()
    ps=prompts(args.mode); lookup={p['id']:p for p in ps}; outdir=ROOT/'data'/args.mode
    manifest={'mode':args.mode,'freeze_hashes':freeze_hashes(),'prompt_ids':list(lookup),'schema':'study8-v1'}
    ensure(outdir/'manifest.json',manifest)
    trrows=verified(outdir/'traces.jsonl','trace_key'); traces={tuple(r['trace_key']):r for r in trrows}
    cr=verified(outdir/'cells.jsonl','cell_key'); cells={tuple(r['cell_key']):r for r in cr}
    expected=set(plan(ps))
    if not set(cells)<=expected or not set(traces)<={(p['id'],s,g) for p in ps for s in SOURCES for g in CONTEXTS}: raise RuntimeError('Unexpected resume keys')
    if any(r['manifest_sha256']!=digest(manifest) for r in trrows+cr): raise RuntimeError('Resume provenance mismatch')
    b=Backend(c);f=json.loads((ROOT/'framings_s8.json').read_text());assembly=Assembly(b.m.tokenizer,f)
    eos=b.m.model.generation_config.eos_token_id; eos=eos if isinstance(eos,list) else [eos]
    for key in plan(ps):
        if key in cells: continue
        pid,s,g,r,arm=key;p=lookup[pid];tk=(pid,s,g); timings={};started=time.monotonic();b.events=[];b.peak=0
        if tk not in traces:
            start=time.monotonic();tr=b.trace_context(p['text'],s,c['seed_maps']['trace'][pid][s],g,assembly);timings['trace']=time.monotonic()-start
            start=time.monotonic();tr['perplexity']=b.ppl(tr['prompt_ids']+tr['pre_trace_ids'],tr['trace_ids']);timings['trace_perplexity']=time.monotonic()-start
            start=time.monotonic();windows=[]
            for offset in range(0,len(tr['trace_ids']),120):
                tokens=tr['trace_ids'][offset:offset+120]
                windows.append({'start':offset,'token_count':len(tokens),**b.classifier.score(b.m.tokenizer.decode(tokens,skip_special_tokens=True))})
            tr['classifier_windows']=windows
            tr['classifier']={k:sum(w[k] for w in windows)/len(windows) if windows and all(w[k] is not None for w in windows) else None for k in ('eh','ew')}
            timings['trace_classifier']=time.monotonic()-start
            tr.update(trace_key=list(tk),text=b.m.tokenizer.decode(tr['trace_ids'],skip_special_tokens=True),timings=dict(timings),manifest_sha256=digest(manifest))
            traces[tk]=append(outdir/'traces.jsonl',tr)
            gc.collect();b.torch.mps.empty_cache()
        tr=traces[tk];prefix,bounds=assembly.assemble(p['text'],tr,r)
        donor=None;start=time.monotonic()
        if arm=='fixed_answer':
            donor=cells[(pid,'unsteered',r,r,'generated')]
            answer=list(donor['answer_ids'])
        else: answer=b.answer(prefix,c['seed_maps']['answer'][pid][s],c['generation']['answer_cap'])
        timings['answer']=time.monotonic()-start
        history=prefix+answer; branches={};spans={};ratings={};start=time.monotonic()
        for q in (('O1',) if arm=='fixed_answer' else ('O1','O3')):
            branches[q],spans[q]=assembly.branch_span(history,q);ratings[q]=b.rating(branches[q])
        if arm=='fixed_answer': assert assembly.clamp(prefix,answer)==(branches['O1'],spans['O1'])
        timings['ratings']=time.monotonic()-start
        projection=None;classifier=None
        if arm!='fixed_answer':
            start=time.monotonic()
            # Answer delimiter/EOS is excluded; positions are after consuming tokens.
            end=len(history)
            while end>len(prefix) and history[end-1] in set(b.m.tokenizer.all_special_ids):end-=1
            projection=observe(b.m.model,b.m.layer,b.forward,branches['O1'],b.vectors['hostility'],{'O1_question':spans['O1'],'answer':[len(prefix),end]})
            timings['projections']=time.monotonic()-start
            start=time.monotonic();classifier=b.classifier.score(b.m.tokenizer.decode(answer,skip_special_tokens=True));timings['classifier']=time.monotonic()-start
        b.torch.mps.synchronize();assert_no_hooks(b.m.model)
        row={'schema':'study8-v1','cell_key':list(key),'mode':args.mode,'prompt_id':pid,'prompt_type':p['type'],'source':s,'generation_context':g,'context':r,'arm':arm,'trace_sha256':tr['row_sha256'],'trace_key':list(tk),'answer_prefix_ids':prefix,'trace_bounds':bounds,'answer_ids':answer,'answer_text':b.m.tokenizer.decode(answer,skip_special_tokens=True),'answer_seed':c['seed_maps']['answer'][pid][s] if donor is None else donor['answer_seed'],'trace_seed':tr['seed'],'answer_donor_sha256':None if donor is None else donor['row_sha256'],'ratings':ratings,'branch_ids':branches,'question_spans':spans,'projection':projection,'classifier':classifier,'answer_length':sum(x not in set(b.m.tokenizer.all_special_ids) for x in answer),'answer_truncated':len(answer)==c['generation']['answer_cap'] and answer[-1] not in eos,'answer_natural_closure':bool(answer and answer[-1] in eos),'trace_length':len(tr['trace_ids']),'forced_closure':tr['forced_closure'],'trace_perplexity':tr['perplexity'],'timings':timings,'seconds':time.monotonic()-started,'peak_driver_memory_bytes':b.peak,'max_process_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'system_swap':subprocess.run(['sysctl','vm.swapusage'],capture_output=True,text=True).stdout.strip(),'hook_assertions':b.events,'manifest_sha256':digest(manifest)}
        cells[key]=append(outdir/'cells.jsonl',row)
        print(json.dumps({'finished':key,'cells':len(cells),'total':len(expected),'seconds':row['seconds']}),flush=True)
        status(f'**{args.mode.upper()} RUNNING** — {len(cells)}/{len(expected)} cells complete.\n\nLast cell: {key}; {row["seconds"]:.1f} seconds. Approximate remaining compute: {(len(expected)-len(cells))*sum(x["seconds"] for x in cells.values())/len(cells)/3600:.2f} hours. Model CPU fallbacks/warnings are captured in logs/{args.mode}.log.')
        del history,branches,ratings,projection,classifier,answer,prefix
        gc.collect();b.torch.mps.empty_cache()
    ensure(outdir/'qwen_complete.json',{'manifest_sha256':digest(manifest),'cells':len(cells),'traces':len(traces),'cells_sha256':sha(outdir/'cells.jsonl'),'traces_sha256':sha(outdir/'traces.jsonl')})
    status(f'**{args.mode.upper()} QWEN COMPLETE** — {len(cells)} cells. Qwen process exiting; judges run separately. Blind trace audit required before analysis.')
if __name__=='__main__':main()
