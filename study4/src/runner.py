"""Study 4 token-preserving replay. Importing this module never loads a model."""
import argparse
import json
import time
from pathlib import Path
from .common import ROOT, SOURCES, FRAMINGS, config, rows, sha, digest, seed, save, append, verified_rows, verify_reuse

class Assembly:
    def __init__(self, tokenizer, manifest):
        self.t = tokenizer
        self.f = manifest
    def enc(self, s):
        return self.t.encode(s, add_special_tokens=False)
    def marker(self, name):
        return self.enc(self.f['markers'][name])
    def base(self, prompt):
        return self.marker('system_start') + self.enc(self.f['system']) + self.marker('turn_end') + self.marker('user_start') + self.enc(prompt)
    def assemble(self, prompt, trace, framing):
        ids = self.base(prompt)
        if framing == 'own_native':
            ids += self.marker('turn_end') + self.marker('assistant_start') + trace['pre_trace_ids']
            start = len(ids)
            ids += trace['trace_ids'] + self.marker('think_close') + self.marker('answer_separator')
        else:
            ids += self.enc(self.f['quoted_before'].format(label=self.f['labels'][framing]))
            start = len(ids)
            ids += trace['trace_ids'] + self.enc(self.f['quoted_after'])
            ids += self.marker('turn_end') + self.marker('assistant_start') + self.marker('empty_thinking')
        assert ids[start:start+len(trace['trace_ids'])] == trace['trace_ids']
        return ids, [start, start+len(trace['trace_ids'])]
    def end_turn(self, history):
        end = self.marker('turn_end')
        # Qwen emits im_end but not its trailing newline.
        if history[-len(end):] == end:
            return list(history)
        if history and history[-1] == end[0]:
            return history + end[1:]
        return history + end
    def branch(self, history, question):
        return self.end_turn(history) + self.marker('user_start') + self.enc(self.f['questions'][question]) + self.marker('turn_end') + self.enc(self.f['rating_prefix'])
    def branches(self, history, framing, sender_argmax=None):
        targets = ['sender'] if framing == 'own_native' else ['sender','writer','notes']
        if sender_argmax is not None:
            history = self.branch(history, 'sender') + self.enc(str(sender_argmax))
        return {t:self.branch(history,t) for t in targets}
    def fixed_segments(self, prompt, trace):
        result = {}
        for name in self.f['fixed_segments']:
            if name == 'original_user_prompt': value = self.enc(prompt)
            elif name == 'trace_ids': value = trace['trace_ids']
            elif name.startswith('questions.'): value = self.enc(self.f['questions'][name.split('.')[1]])
            elif name == 'system': value = self.enc(self.f['system'])
            else: value = self.marker(name)
            result[name] = digest(value)
        return result

def assert_no_hooks(model):
    """Fail closed on any forward/pre-forward hook, including global hooks."""
    import torch
    bad = [n for n,m in model.named_modules() if m._forward_hooks or m._forward_pre_hooks]
    global_hooks = torch.nn.modules.module
    if bad or global_hooks._global_forward_hooks or global_hooks._global_forward_pre_hooks:
        raise RuntimeError(f'Post-trace hook-absence assertion failed: {bad}')
    return True

def readout(logits, tokenizer, labels):
    import torch
    encoded = [tokenizer.encode(x,add_special_tokens=False) for x in labels]
    if any(len(x)!=1 for x in encoded) or len({x[0] for x in encoded})!=len(labels):
        raise ValueError('Readout labels must have distinct single tokens')
    ids = [x[0] for x in encoded]
    raw = logits.float()
    if not torch.isfinite(raw).all(): raise ValueError('Nonfinite readout logits')
    mass = raw.softmax(-1)[ids].sum().item()
    probs = raw[ids].softmax(-1).cpu().tolist()
    result = {'probabilities':dict(zip(labels,probs)), 'valid_mass':mass, 'argmax':labels[max(range(len(probs)),key=probs.__getitem__)]}
    if labels == list('0123456789'):
        result.update(expected=sum(i*p for i,p in enumerate(probs)), low_mass=mass<.5)
    return result

class Backend:
    def __init__(self, cfg):
        import torch
        from study3.src.main_model import Model
        from study3.src.metrics import EmotionClassifier
        if not torch.backends.mps.is_available():
            raise RuntimeError('MPS required: launch run_smoke_test.command outside the sandbox; no CPU substitution')
        self.torch = torch
        spec = dict(cfg['model'],local_path=str((ROOT/cfg['model']['local_path']).resolve()))
        self.m = Model(spec)
        assert self.m.layer_index == cfg['model']['layer_index']
        self.classifier = EmotionClassifier(str((ROOT/cfg['classifier']['local_path']).resolve()))
        self.cfg = cfg
        self.peak = 0
        self.events = []
        self.vectors = {}
        for source,item in cfg['directions'].items():
            obj = torch.load(ROOT/item['path'],map_location='cpu',weights_only=False)
            self.vectors[source] = obj['vector'] if 'vector' in obj else obj['v_hat']
    def clean(self, operation):
        assert_no_hooks(self.m.model)
        self.events.append({'operation':operation,'hook_absent':True,'initial_cache':None})
    def forward(self, ids, cache=None, use_cache=False):
        out = self.m.model(input_ids=self.m.tensor(ids),past_key_values=cache,use_cache=use_cache)
        self.peak = max(self.peak,self.torch.mps.driver_allocated_memory())
        return out
    def sample(self, raw):
        torch = self.torch
        g = self.cfg['generation']
        vals, ix = (raw.float()/g['temperature']).topk(g['top_k'])
        cut = vals.softmax(-1).cumsum(-1)>g['top_p']
        cut[1:] = cut[:-1].clone(); cut[0] = False; vals[cut] = -torch.inf
        return ix[torch.multinomial(vals.softmax(-1),1)].item()
    def set_seed(self, value):
        self.torch.manual_seed(value); self.torch.mps.manual_seed(value)
    def trace(self, prompt, source, value, cap):
        self.set_seed(value)
        ids = self.m.ids(self.m.messages(prompt,self.cfg['condition']),thinking=True)
        tokens = []; cache = None; forced = False
        with self.torch.inference_mode(), self.m.steering(0 if source=='unsteered' else self.cfg['alpha'], self.cfg['norm']['value'],self.vectors.get(source)):
            out = self.forward(ids, use_cache=True)
            cache = out.past_key_values
            for _ in range(cap):
                tok = self.sample(out.logits[0,-1]); tokens.append(tok)
                out = self.forward([tok],cache,True); cache = out.past_key_values
                if tok == self.m.close_think: break
                eos = self.m.model.generation_config.eos_token_id
                if tok in (eos if isinstance(eos,list) else [eos]): raise RuntimeError('EOS before thinking closure')
            else: forced = True
        del cache,out
        self.clean('trace_cache_discarded')
        if self.m.open_think not in tokens: raise RuntimeError('Missing sampled <think>')
        opening = tokens.index(self.m.open_think)
        closing = tokens.index(self.m.close_think) if self.m.close_think in tokens else len(tokens)
        return {'prompt_ids':ids,'pre_trace_ids':tokens[:opening+1],'trace_ids':tokens[opening+1:closing], 'forced_closure':forced,'seed':value}
    def answer(self, prefix, value, cap):
        self.clean('answer'); self.set_seed(value)
        tokens = []; cache = None
        eos = self.m.model.generation_config.eos_token_id
        eos = eos if isinstance(eos,list) else [eos]
        with self.torch.inference_mode():
            out = self.forward(prefix,use_cache=True); cache = out.past_key_values
            for _ in range(cap):
                tok = self.sample(out.logits[0,-1]); tokens.append(tok)
                if tok in eos: break
                out = self.forward([tok],cache,True); cache = out.past_key_values
        del out,cache
        return tokens
    def rating(self, ids, labels=list('0123456789')):
        self.clean('readout')
        with self.torch.inference_mode():
            return readout(self.forward(ids).logits[0,-1],self.m.tokenizer,labels)
    def ppl(self, prefix, ids):
        self.clean('perplexity')
        with self.torch.inference_mode():
            value = self.m.segment_ppl(prefix,ids)
            self.peak = max(self.peak,self.torch.mps.driver_allocated_memory())
            return value

def select_checks(prompts, cfg, mode):
    import numpy as np
    rng = np.random.default_rng(cfg['seeds']['check_permutation'])
    counts = cfg['check_sample']['pilot' if mode!='main' else str(len(prompts))]
    selected = []
    for kind,n in zip(('provocative','neutral'),counts):
        pool = sorted(p['id'] for p in prompts if p['type']==kind)
        selected.extend(rng.permutation(pool).tolist()[:n])
    return set(selected)

def reused_traces(cfg):
    result = {}
    for r in rows(ROOT/cfg['study3_raw']['path']):
        if r['mode']!='think': continue
        if r['dose_fraction']==0: source='unsteered'
        elif r['route']=='pulse' and r['dose_fraction']==1: source=r['direction']
        else: continue
        key = (r['prompt_id'],source)
        if key in result: raise RuntimeError(f'Duplicate reused trace {key}')
        # Find the saved trace as an exact token slice; 151667 is verified by the real-tokenizer unit test.
        opening = r['token_ids'].index(151667)
        result[key] = {'prompt_ids':r['prompt_ids'],'pre_trace_ids':r['token_ids'][:opening+1], 'trace_ids':r['thinking_ids'],'forced_closure':r['thinking_truncated'],'seed':r['seed'],'study3_row_sha256':digest(r)}
    return result

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode',choices=['smoke','pilot','main'],required=True)
    parser.add_argument('--output',required=True)
    args = parser.parse_args()
    cfg = config(); verify_reuse(cfg)
    if args.mode=='main':
        from .approval import require_approval
        require_approval()
    outdir = (ROOT/args.output).resolve()
    from .common import output_path
    output_path(outdir/'placeholder')
    framing = json.loads((ROOT/'framings.json').read_text())
    prompt_path = ROOT/cfg['prompts']['test' if args.mode=='main' else 'pilot']
    prompts = rows(prompt_path)
    if args.mode=='main':
        assert len(prompts)==cfg['N']
        assert all(sum(p['type']==kind for p in prompts)==n for kind,n in cfg['composition'].items())
    if args.mode=='smoke': prompts = [p for p in prompts if p['id'] in cfg['smoke']['prompt_ids']]
    checks = select_checks(prompts,cfg,args.mode)
    provenance = {str(p.relative_to(ROOT)):sha(p) for p in [ROOT/'config.yaml',ROOT/'framings.json',prompt_path,*sorted((ROOT/'src').glob('*.py'))]}
    provenance.update({str(p.relative_to(ROOT.parent)):sha(p) for p in [ROOT.parent/'study3/src'/name for name in ['base_model.py','model_utils.py','main_model.py','metrics.py']]})
    manifest = {'mode':args.mode,'hashes':provenance,'check_ids':sorted(checks),'short_caps':args.mode=='smoke'}
    if (outdir/'manifest.json').exists():
        old = json.loads((outdir/'manifest.json').read_text())
        if old!=manifest:
            # Allowed only for the logged 2026-10-22 memory fix: everything except src/runner.py must match.
            diff = {k for k in set(old['hashes'])|set(manifest['hashes']) if old['hashes'].get(k)!=manifest['hashes'].get(k)}
            same_rest = {k:v for k,v in old.items() if k!='hashes'}=={k:v for k,v in manifest.items() if k!='hashes'}
            if diff!={'src/runner.py'} or not same_rest: raise RuntimeError(f'Resume manifest differs: {sorted(diff)}')
            if not (outdir/'manifest_pre_memfix.json').exists(): (outdir/'manifest.json').rename(outdir/'manifest_pre_memfix.json')
            else: (outdir/'manifest.json').unlink()
            save(outdir/'manifest.json',manifest)
    else: save(outdir/'manifest.json',manifest)
    done = verified_rows(outdir/'cells.jsonl'); done_keys = {tuple(r['cell_key']) for r in done}
    trace_rows = verified_rows(outdir/'traces.jsonl')
    traces = {tuple(r['trace_key']):r for r in trace_rows}
    if len(done_keys)!=len(done) or len(traces)!=len(trace_rows): raise RuntimeError('Duplicate resume keys')
    backend = Backend(cfg); assembly = Assembly(backend.m.tokenizer,framing)
    reused = reused_traces(cfg) if args.mode=='pilot' else {}
    caps = cfg['smoke'] if args.mode=='smoke' else cfg['generation']
    for p in prompts:
        for source in SOURCES:
            key = (p['id'],source)
            if key not in traces:
                started = time.monotonic()
                tr = reused[key] if args.mode=='pilot' else backend.trace(p['text'],source,seed(cfg,'trace',*key),caps['thinking_cap'])
                assert tr['pre_trace_ids'][-1] == backend.m.open_think
                native,_ = assembly.assemble(p['text'],tr,'own_native')
                expected = tr['prompt_ids']+tr['pre_trace_ids']+tr['trace_ids']+assembly.marker('think_close')+assembly.marker('answer_separator')
                assert native==expected,'Native construction differs from Study 3 pulse prefix'
                tr['text'] = backend.m.tokenizer.decode(tr['trace_ids'],skip_special_tokens=True)
                tr['perplexity'] = backend.ppl(tr['prompt_ids']+tr['pre_trace_ids'],tr['trace_ids'])
                # Study 3 scores contiguous 120-model-token trace windows, then averages.
                windows = []
                for offset in range(0,len(tr['trace_ids']),120):
                    ids = tr['trace_ids'][offset:offset+120]
                    windows.append({'start':offset,'token_count':len(ids),**backend.classifier.score(backend.m.tokenizer.decode(ids,skip_special_tokens=True))})
                tr['trace_windows'] = windows
                eh = sum(w['eh'] for w in windows)/len(windows) if windows and all(w['eh'] is not None for w in windows) else None
                tr['classifier'] = {'eh':eh,'error':None if eh is not None else 'Empty trace or classifier failure; no alternate scorer'}
                tr.update(trace_key=list(key),seconds=time.monotonic()-started)
                traces[key] = append(outdir/'traces.jsonl',tr)
                import gc; gc.collect(); backend.torch.mps.empty_cache()
            tr = traces[key]
            for frame in FRAMINGS:
                cell_key = (*key,frame)
                if cell_key in done_keys: continue
                started = time.monotonic(); backend.events=[]; backend.peak=0
                prefix,bounds = assembly.assemble(p['text'],tr,frame)
                answer_seed = seed(cfg,'answer',*cell_key)
                answer = backend.answer(prefix,answer_seed,caps['answer_cap'])
                history = prefix+answer
                branch_ids = assembly.branches(history,frame)
                ratings = {t:backend.rating(ids) for t,ids in branch_ids.items()}
                seq_ids = assembly.branches(history,frame,ratings['sender']['argmax'])
                sequential = {'sender':ratings['sender']}
                sequential.update({t:backend.rating(ids) for t,ids in seq_ids.items() if t!='sender'})
                check = {}
                if p['id'] in checks:
                    if frame!='own_native':
                        check = {q:backend.rating(assembly.branch(history,q),['A','B']) for q in ('label','operative')}
                    sender_history = branch_ids['sender']+assembly.enc(ratings['sender']['argmax'])
                    check['referent'] = backend.rating(assembly.branch(sender_history,'referent'),['A','B'])
                    check['referent_swap'] = backend.rating(assembly.branch(sender_history,'referent_swap'),['A','B'])
                text = backend.m.tokenizer.decode(answer,skip_special_tokens=True)
                ppl = backend.ppl(prefix,answer)
                classifier = backend.classifier.score(text)
                backend.torch.mps.synchronize()
                row = {'schema':'study4-v0.5.1','cell_key':list(cell_key),'prompt_id':p['id'],'prompt_type':p['type'],'source':source,'framing':frame,'mode':args.mode,'trace_sha256':tr['row_sha256'],'trace_ids':tr['trace_ids'],'trace_text':tr['text'],'forced_closure':tr['forced_closure'],'EH_trace':tr['classifier']['eh'],'trace_perplexity':tr['perplexity'],'answer_prefix_ids':prefix,'trace_bounds':bounds,'fixed_segments':assembly.fixed_segments(p['text'],tr),'answer_ids':answer,'answer_text':text,'answer_seed':answer_seed,'ratings':ratings,'sequential':sequential,'branch_ids':branch_ids,'sequential_branch_ids':{t:v for t,v in seq_ids.items() if t!='sender'},'checks':check,'EH_answer':classifier['eh'],'answer_classifier':classifier,'answer_perplexity':ppl,'replay_assertions':backend.events,'seconds':time.monotonic()-started,'peak_driver_memory_bytes':backend.peak,'manifest_sha256':digest(manifest)}
                append(outdir/'cells.jsonl',row)
                print(json.dumps({'finished':cell_key,'seconds':row['seconds'],'peak_memory':backend.peak}),flush=True)
                # Engineering fix 2026-10-22: release per-cell tensors so MPS memory does not accumulate across cells.
                del row,prefix,answer,history,branch_ids,seq_ids,ratings,sequential,check
                import gc; gc.collect(); backend.torch.mps.empty_cache()
    result = verified_rows(outdir/'cells.jsonl')
    # Separate check dataset, with an explicit link to the identical post-answer history.
    existing_checks = {tuple(r['cell_key']) for r in verified_rows(outdir/'checks.jsonl')}
    for r in result:
        if r['checks'] and tuple(r['cell_key']) not in existing_checks:
            append(outdir/'checks.jsonl',{'cell_key':r['cell_key'],'main_cell_sha256':r['row_sha256'],'prompt_id':r['prompt_id'],'source':r['source'],'framing':r['framing'],'checks':r['checks'],'post_answer_sha256':digest(r['answer_prefix_ids']+r['answer_ids'])})
    if not (outdir/'summary.json').exists():
        save(outdir/'summary.json',{'mode':args.mode,'cells':len(result),'expected_cells':len(prompts)*12,'seconds':sum(r['seconds'] for r in result),'peak_driver_memory_bytes':max(r['peak_driver_memory_bytes'] for r in result),'all_hooks_absent':all(e['hook_absent'] for r in result for e in r['replay_assertions']),'per_cell':[{'key':r['cell_key'],'seconds':r['seconds'],'peak_driver_memory_bytes':r['peak_driver_memory_bytes']} for r in result]})

if __name__=='__main__': main()
