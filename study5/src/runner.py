"""Stored-trace replay only. No trace generation or direction loading."""
import argparse
import gc
import json
import time
import warnings
import fcntl
from .common import ROOT, SOURCES, CONDITIONS, config, sha, digest, save, append, verified_rows, rows, input_path, verify_inputs, output_path
from .assembly import Assembly
from study4.src.runner import Backend as Study4Backend, assert_no_hooks

class Backend(Study4Backend):
    def __init__(self, cfg):
        import torch
        from study3.src.main_model import Model
        from study3.src.metrics import EmotionClassifier
        if not torch.backends.mps.is_available(): raise RuntimeError('MPS unavailable; use Terminal outside sandbox. No CPU model substitution.')
        self.torch = torch
        self.m = Model(dict(cfg['model'], local_path=str((ROOT/cfg['model']['local_path']).resolve())))
        self.classifier = EmotionClassifier(str((ROOT/cfg['classifier']['local_path']).resolve()))
        self.cfg = cfg; self.peak = 0; self.events = []
        assert_no_hooks(self.m.model)
    def trace(self, *args, **kwargs):
        raise RuntimeError('Study 5 forbids new trace generation')

def load_plan(cfg, mode):
    verify_inputs(cfg)
    ids = cfg['main_prompt_ids'] if mode=='main' else cfg['pilot_prompt_ids']
    if mode=='pilot' and (not ids or len(ids)!=4):
        raise RuntimeError('Pilot prompt IDs unresolved: specification says four, reference contains 80. See BUILD_NOTES.md.')
    if len(ids)!=len(set(ids)) or (mode=='main' and len(ids)!=80): raise ValueError('Invalid prompt plan')
    prompt_map = {p['id']:p for p in rows(input_path(cfg,mode+'_prompts'))}
    prompts = [prompt_map[p] for p in ids]
    tr_rows = verified_rows(input_path(cfg,mode+'_traces'))
    traces = {tuple(r['trace_key']):r for r in tr_rows}
    if len(traces)!=len(tr_rows): raise ValueError('Duplicate input traces')
    for p in ids:
        for s in SOURCES:
            if (p,s) not in traces: raise ValueError(f'Missing stored trace {p}/{s}')
            for c in CONDITIONS: cfg['answer_seeds'][mode]['/'.join([p,s,c])]
    return prompts,traces

def validate_resume(data, expected, manifest_hash):
    keys = set()
    for row in data:
        key = tuple(row['cell_key'])
        if key not in expected or key in keys: raise RuntimeError(f'Unexpected/duplicate resume cell: {key}')
        if row['manifest_sha256']!=manifest_hash: raise RuntimeError('Resume row provenance mismatch')
        keys.add(key)
    return keys

def run_cell(backend, assembly, cfg, mode, prompt, source, condition, trace, checks, manifest_hash):
    start = time.monotonic(); backend.events=[]; backend.peak=0
    key = [prompt['id'],source,condition]
    prefix,bounds = assembly.assemble(prompt['text'],trace,condition)
    value = cfg['answer_seeds'][mode]['/'.join(key)]
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter('always')
        answer = backend.answer(prefix,value,cfg['generation']['answer_cap'])
        history = prefix+answer
        branches = {'sender':assembly.branch(history,'sender')}
        ratings = {'sender':backend.rating(branches['sender'])}
        diagnostic = {}; diagnostic_ids = {}
        if prompt['id'] in checks:
            for q in ['structural','structural_swap','source','source_swap']:
                diagnostic_ids[q] = assembly.branch(history,q)
                diagnostic[q] = backend.rating(diagnostic_ids[q],list('ABC') if q.startswith('structural') else list('AB'))
        text = backend.m.tokenizer.decode(answer,skip_special_tokens=True)
        classifier = backend.classifier.score(text)
    for w in caught: print(f'{w.category.__name__}: {w.message}',flush=True)
    eos = backend.m.model.generation_config.eos_token_id
    eos = eos if isinstance(eos,list) else [eos]
    backend.torch.mps.synchronize()
    return {'schema':'study5-v0.2','cell_key':key,'mode':mode,'prompt_id':prompt['id'],'prompt_type':prompt['type'],
        'source':source,'condition':condition,'trace_sha256':trace['row_sha256'],'trace_ids':trace['trace_ids'],
        'forced_closure':trace['forced_closure'],'answer_prefix_ids':prefix,'trace_bounds':bounds,
        'answer_ids':answer,'answer_text':text,'answer_seed':value,'answer_length':len(answer),
        'answer_truncated':len(answer)==cfg['generation']['answer_cap'] and answer[-1] not in eos,
        'ratings':ratings,'branch_ids':branches,'checks':diagnostic,'diagnostic_branch_ids':diagnostic_ids,
        'EH_answer':classifier['eh'],'answer_classifier':classifier,'replay_assertions':backend.events.copy(),
        'warnings':[str(w.message) for w in caught],'seconds':time.monotonic()-start,
        'peak_driver_memory_bytes':backend.peak,'manifest_sha256':manifest_hash}

def main():
    p=argparse.ArgumentParser(); p.add_argument('--mode',choices=['pilot','main'],required=True); args=p.parse_args()
    cfg=config()
    prompts,traces=load_plan(cfg,args.mode)
    if args.mode=='main':
        from .approval import require_approval
        require_approval()
        from .approval import freeze_hashes
        from study5.analysis.pilot import evaluate
        pilot_prompts,_=load_plan(cfg,'pilot')
        pilot_manifest={'mode':'pilot','hashes':freeze_hashes(),
                        'prompt_ids':[p['id'] for p in pilot_prompts],
                        'check_ids':[p['id'] for p in pilot_prompts]}
        pilot_path=ROOT/'data/pilot/manifest.json'
        if not pilot_path.exists(): raise RuntimeError('Pilot manifest missing')
        stored=json.loads(pilot_path.read_text())
        # Post-pilot disposition (DEVIATIONS 2026-10-26) may change only these files; all generation code/inputs must match.
        disposition_files={'Study5_RoleLadder_PREREG_v0.2_draft.md','Study5_RoleLadder_PREREG_v0.3.md','config_s5.yaml','src/runner.py'}
        hs,hn=stored.get('hashes',{}),pilot_manifest['hashes']
        changed={k for k in set(hs)|set(hn) if hs.get(k)!=hn.get(k)}
        if {k:v for k,v in stored.items() if k!='hashes'}!={k:v for k,v in pilot_manifest.items() if k!='hashes'} or not changed<=disposition_files:
            raise RuntimeError('Pilot manifest missing or stale for this build')
        pilot_manifest=stored
        pilot_rows=verified_rows(ROOT/'data/pilot/cells.jsonl')
        pilot_expected={(p['id'],s,c) for p in pilot_prompts for s in SOURCES for c in CONDITIONS}
        complete=validate_resume(pilot_rows,pilot_expected,digest(pilot_manifest))==pilot_expected
        validity=evaluate(pilot_rows,cfg)
        accepted=set((cfg.get('pilot_disposition') or {}).get('accepted_baseline_sd_shortfall') or [])
        def sd_only(c,e):
            if e['pass']: return True
            if c not in accepted or not e['complete'] or e['mean_valid_mass']<cfg['pilot_validity']['mean_valid_mass_min']: return False
            if e.get('reference_differences') is not None and abs(e['reference_mean_difference'])>cfg['pilot_validity']['reference_baseline_tolerance']: return False
            return True
        if not complete or not all(sd_only(c,e) for c,e in validity['conditions'].items()):
            raise RuntimeError('Main requires passing pilot validity; failed conditions need documented author disposition before freezing')
    from .approval import freeze_hashes
    manifest={'mode':args.mode,'hashes':freeze_hashes(),'prompt_ids':[p['id'] for p in prompts],
              'check_ids':cfg['diagnostic_prompt_ids'] if args.mode=='main' else [p['id'] for p in prompts]}
    out=ROOT/'data'/args.mode; output_path(out/'manifest.json')
    with (out/'run.lock').open('a') as lock:
        fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
        if (out/'manifest.json').exists():
            if json.loads((out/'manifest.json').read_text())!=manifest: raise RuntimeError('Resume manifest differs; preserve old outputs')
        else: save(out/'manifest.json',manifest)
        expected={(p['id'],s,c) for p in prompts for s in SOURCES for c in CONDITIONS}
        done=validate_resume(verified_rows(out/'cells.jsonl'),expected,digest(manifest))
        if done != expected:
            backend=Backend(cfg); assembly=Assembly(backend.m.tokenizer,json.loads((ROOT/'framings_s5.json').read_text()))
            for prompt in prompts:
                for source in SOURCES:
                    for condition in CONDITIONS:
                        key=(prompt['id'],source,condition)
                        if key in done: continue
                        try:
                            row=run_cell(backend,assembly,cfg,args.mode,prompt,source,condition,traces[key[:2]],set(manifest['check_ids']),digest(manifest))
                            append(out/'cells.jsonl',row); done.add(key)
                            progress=f'{len(done)}/{len(expected)} cells saved; last cell {row["seconds"]:.1f}s; provisional remaining {(len(expected)-len(done))*row["seconds"]/3600:.2f} h.'
                            print(progress,flush=True)
                            (ROOT/'STATUS.md').write_text(f'# Study 5 {args.mode}\n{progress}\nResumable outputs: data/{args.mode}/cells.jsonl.\n')
                            del row
                        finally:
                            gc.collect(); backend.torch.mps.empty_cache()
        if args.mode=='pilot':
            from study5.analysis.pilot import evaluate
            if not (out/'validity.json').exists(): save(out/'validity.json',evaluate(verified_rows(out/'cells.jsonl'),cfg))
        print(f'Complete: {len(done)} cells.',flush=True)

if __name__=='__main__':
    try: main()
    except Exception as exc:
        message=f'{type(exc).__name__}: {exc}'
        (ROOT/'STATUS.md').write_text('# Study 5 run BLOCKED\n'+message+'\nExisting data preserved.\n')
        with (ROOT/'DEVIATIONS.md').open('a') as f:f.write('\n## Run stopped\n'+message+'\n')
        raise
