OpenAI Codex v0.163.0-alpha.10.2
--------
workdir: /Users/arthursu/Projects/affect-suppression-steering
model: gpt-6-astra
provider: openai
approval: never
sandbox: read-only
reasoning effort: medium
reasoning summaries: none
session id: 01a17ec9-34d6-7b03-9927-630c06741ed1
--------
user
You are an independent reviewer. Read study6/Study6_AnswerClamp_PREREG_v0.1_draft.md, and for context study5/ (Study5_RoleLadder_PREREG_v0.3.md, framings_s5.json, src/assembly.py, src/runner.py, analysis/analyze.py, data/main/RESULTS_SUMMARY.md; inspect a few rows of data/main/cells.jsonl but do not load it all). Do not edit any files. Review: (1) whether clamped cells can be built exactly from Study 5 stored token IDs (prefix + unsteered answer_ids + rating branch), and whether the unsteered-cell reproducibility check (|diff| <= 0.01) is realistic on MPS bf16; (2) whether clamping with the unsteered answer is the right clamp, confounds it introduces (e.g. the answer being incoherent with a hostile trace, truncated answers, the answer conditioning on the unsteered trace's content), and whether a different clamp (generic answer, no answer, source-matched-but-neutralized answer) should be primary or added; (3) whether the mediation estimand M = A_unclamped - A_clamped with joint prompt-cluster bootstrap across Study 5 and Study 6 is sound, and how to handle that both use the same unsteered cells; (4) the hypotheses, multiplicity, equivalence margin, power, and the reading table; (5) runtime plausibility and anything missing for a binding preregistration. End with a numbered list of required changes and a separate list of optional suggestions.
codex
I’ll read the draft, trace Study 5’s token assembly and rating paths, and inspect a small sample of stored cells without loading the full dataset. I won’t edit any files.
exec
/bin/zsh -lc "pwd && rg --files -g 'AGENTS.md' -g 'PREREG.md' -g 'config.yaml' -g 'prompts/**' -g 'study6/**' -g 'study5/**'" in /Users/arthursu/Projects/affect-suppression-steering
 succeeded in 0ms:
/Users/arthursu/Projects/affect-suppression-steering
AGENTS.md
study6/Codex review Study 6 prereg.command
study6/Study6_AnswerClamp_PREREG_v0.1_draft.md
study6/CODEX_REVIEW_v0.1.md
prompts/test_prompts.jsonl
prompts/extraction_scenarios.jsonl
prompts/openers.json
prompts/downstream_question.txt
prompts/calibration_prompts.jsonl
prompts/hostile_lexicon.txt
PREREG.md
study3_pilot/AGENTS.md
study3_pilot/config.yaml
config.yaml
study4/config.yaml
study5/src/approval.py
study5/src/assembly.py
study5/src/common.py
study5/src/__pycache__/__init__.cpython-310.pyc
study5/src/__pycache__/approval.cpython-310.pyc
study5/src/__pycache__/runner.cpython-310.pyc
study5/src/__pycache__/common.cpython-310.pyc
study5/src/__init__.py
study5/src/runner.py
study5/DEVIATIONS.md
study5/BUILD_NOTES.md
study5/data/main/analysis.json
study5/data/main/manifest.json
study5/data/main/RESULTS_SUMMARY.md
study5/data/main/analysis.md
study5/data/main/run.lock
study5/data/main/cells.jsonl
study5/data/pilot/manifest.json
study5/data/pilot/validity.json
study5/data/pilot/run.lock
study5/data/pilot/cells.jsonl
study5/data/synthetic/visible_only.jsonl
study5/data/synthetic/planted_analysis.json
study5/data/synthetic/small_analysis.json
study5/data/synthetic/null.jsonl
study5/data/synthetic/reversed_analysis.json
study5/data/synthetic/small.jsonl
study5/data/synthetic/planted.jsonl
study5/data/synthetic/reversed.jsonl
study5/data/synthetic/null_analysis.json
study5/data/synthetic/thinking_only.jsonl
study5/data/synthetic/current_only.jsonl
study5/data/synthetic/thinking_only_analysis.json
study5/data/synthetic/visible_only_analysis.json
study5/data/synthetic/current_only_analysis.json
study5/framings_s5.json
study5/build_artifacts.py
study5/CODEX_BUILD_BRIEF.md
study5/Codex review Study 5 prereg.command
study5/CODEX_BUILD_LOG.txt
study5/logs/main.log
study5/logs/pilot.log
study5/ZENODO_DEPOSIT.md
study5/run_main.command
study5/results/freeze_hashes.json
study5/results/build_environment.json
study5/results/synthetic_report_example.md
study5/results/synthetic_validation.md
study5/results/synthetic_validation.json
study5/results/token_tests.log
study5/results/synthetic_tests.log
study5/results/final_token_tests.log
study5/results/freeze_manifest_candidate.json
study5/Study5_RoleLadder_PREREG_v0.2_draft.md
study5/Codex build Study 5.command
study5/config_s5.yaml
study5/affect_under_constraint_V_preregistration_v0.3.zip
github_public/affect-under-constraint/study1/config.yaml
study5/tests/test_build.py
study5/tests/__init__.py
study5/tests/synthetic.py
study5/STATUS.md
study5/CODEX_REVIEW_v0.1.md
study5/Study5_RoleLadder_PREREG_v0.1_draft.md
study5/PREREG_APPROVED
study5/CHATGPT_REVIEW_v0.1.md
study5/analysis/analyze.py
github_public/affect-under-constraint/study1/PREREG.md
study5/analysis/__pycache__/__init__.cpython-310.pyc
study5/analysis/__pycache__/pilot.cpython-310.pyc
study5/analysis/__init__.py
study5/analysis/pilot.py
study5/Study5_RoleLadder_PREREG_v0.3.md
study5/run_pilot.command
github_public/affect-under-constraint/study1/AGENTS.md
study2/data/_superseded/20261004T162639_v3.0_analysis/PREREG.md
study3/config.yaml
study2/PREREG.md
study3/AGENTS.md
study2/data/_superseded/20261004T162639_v3.0_analysis/config.yaml
study2/config.yaml
study2/AGENTS.md
github_public/affect-under-constraint/study3/config.yaml
github_public/affect-under-constraint/study3/PREREG.md
github_public/affect-under-constraint/study3/AGENTS.md
github_public/affect-under-constraint/study2/PREREG.md
github_public/affect-under-constraint/study2/config.yaml
github_public/affect-under-constraint/study2/AGENTS.md

exec
/bin/zsh -lc 'cat study5/src/assembly.py study5/src/runner.py' in /Users/arthursu/Projects/affect-suppression-steering
exec
/bin/zsh -lc 'cat study5/analysis/analyze.py study5/data/main/RESULTS_SUMMARY.md' in /Users/arthursu/Projects/affect-suppression-steering
exec
/bin/zsh -lc 'cat study6/Study6_AnswerClamp_PREREG_v0.1_draft.md study5/Study5_RoleLadder_PREREG_v0.3.md study5/framings_s5.json' in /Users/arthursu/Projects/affect-suppression-steering
 succeeded in 0ms:
"""Explicit token recipes; never round-trip stored traces through text."""
from study4.src.runner import Assembly as Study4Assembly

class Assembly(Study4Assembly):
    def __init__(self, tokenizer, manifest):
        super().__init__(tokenizer, manifest)
        for name, ids in manifest['segment_ids'].items():
            if self.enc(manifest['segment_text'][name]) != ids:
                raise ValueError(f'Tokenizer differs from frozen segment {name}')
    def assemble(self, prompt, trace, condition):
        dynamic = {'PROMPT':self.enc(prompt), 'TRACE':trace['trace_ids'], 'PRE_TRACE':trace['pre_trace_ids']}
        ids = []; bounds = None
        for part in self.f['recipes'][condition]:
            value = dynamic[part] if part in dynamic else self.f['segment_ids'][part]
            if part == 'TRACE': bounds = [len(ids),len(ids)+len(value)]
            ids.extend(value)
        if bounds is None or ids[bounds[0]:bounds[1]] != trace['trace_ids']:
            raise AssertionError('Trace slice differs')
        return ids, bounds
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

 succeeded in 0ms:
"""Study 5 prompt-cluster inference; no Study 4 outcome pooling or coherence exclusions."""
import argparse
import json
import numpy as np
from study4.analysis.analyze import bootstrap
from study5.src.common import ROOT, SOURCES, CONDITIONS, CONTROLS, config, verified_rows, input_path, save

def add(a,b,weight=-1):
    out=dict(a)
    for k,v in b.items():out[k]=out.get(k,0)+weight*v
    return out

def contrasts():
    d={}
    for c in CONDITIONS:
        d[c+':X']={('hostility',c):1,('unsteered',c):-1}
        for ctrl in CONTROLS:d[c+':A_'+ctrl]={('hostility',c):1,(ctrl,c):-1}
    for h,a,b in [('P3','R3','R2'),('S3','R1-M','R3'),('S4','R1','R1-M')]:
        for ctrl in CONTROLS:d[h+':'+ctrl]=add(d[a+':A_'+ctrl],d[b+':A_'+ctrl])
    return d

def hypotheses():
    d={h:[c+':X']+[c+':A_'+ctrl for ctrl in CONTROLS] for h,c in [('P1','R2'),('P2','R3'),('S1','R1'),('S2','R1-M'),('S5','R4')]}
    d.update({h:[h+':'+ctrl for ctrl in CONTROLS] for h in ['P3','S3','S4']})
    return d

def summarize(values,samples,level,kind='negative'):
    available=int(np.isfinite(values).sum())
    if not len(values) or available!=len(values):return {'status':'not estimable','n_required':len(values),'n_available':available,'supported':False,'negligible':False,'reversed':False}
    lo,hi=np.quantile(samples,[(1-level)/2,(1+level)/2]); elo,ehi=np.quantile(samples,[.05,.95])
    negative=bool(hi<0); positive=bool(lo>0); negligible=bool(elo>-.15 and ehi<.15)
    supported=(negative or positive) if kind=='two-sided' else negligible if kind=='equivalence' else negative
    reversed_=positive if kind=='negative' else False
    detectable=negative or positive
    status='small but detectable' if negligible and detectable else 'supported' if supported else 'reversed' if reversed_ else 'negligible' if negligible else 'inconclusive'
    return {'estimate':float(np.mean(values)),'ci_level':level,'ci':[float(lo),float(hi)],'equivalence_ci_level':.9,'equivalence_ci':[float(elo),float(ehi)],'n':len(values),'supported':supported,'negligible':negligible,'reversed':reversed_,'negative':negative,'positive':positive,'status':status}

def conjunction(parts,kind='negative'):
    estimable=bool(parts) and all(v['status']!='not estimable' for v in parts)
    support=estimable and all(v['supported'] for v in parts)
    negligible=estimable and all(v['negligible'] for v in parts)
    reversed_=estimable and all(v['reversed'] for v in parts)
    overlap=support and negligible and kind!='equivalence'
    return {'supported':support,'negligible':negligible,'reversed':reversed_,
            'status':'not estimable' if not estimable else 'small but detectable' if overlap else 'supported' if support else 'reversed' if reversed_ else 'negligible' if negligible else 'inconclusive'}

def reading(h):
    if not all(h[k]['supported'] for k in ['S1','S2']):return 'Historical nulls uninterpretable: S1 and S2 are not both supported.'
    p1,p2,p3=h['P1'],h['P2'],h['P3']
    if any(h[k]['supported'] and h[k]['negligible'] for k in ['P1','P2']):
        return 'Small but detectable historical influence overlaps equivalence; report direction and magnitude separately, without an exclusive placement reading.'
    if p1['supported'] and p2['supported']:return 'Both historical placements retain influence. Direct P3 contrast: '+p3['status']+'.'
    if p1['negligible'] and p2['supported'] and p3['supported']:return 'Retained historical thinking retains influence; visible historical reply is negligible; direct channel contrast supported.'
    if p1['supported'] and p2['negligible'] and p3['reversed']:return 'Visible historical reply retains influence; retained thinking is negligible; direct channel contrast reversed.'
    if p1['negligible'] and p2['negligible']:
        return 'Both historical placements are negligible; '+('S3 supports a drop from matched current thinking to retained historical thinking under these framings.' if h['S3']['supported'] else 'S3 does not establish a current-versus-historical thinking drop.')
    return 'Placement interpretation inconclusive; comparative claims require direct P3 or S3 evidence.'

def core(data,cfg,ids):
    lookup={}
    for r in data:
        k=(r['prompt_id'],r['source'],r['condition'])
        if k in lookup:raise ValueError(f'Duplicate cell {k}')
        lookup[k]=r
    defs=contrasts(); matrix=np.full((len(ids),len(defs)),np.nan)
    for j,terms in enumerate(defs.values()):
        for i,pid in enumerate(ids):
            value=0.
            for (source,c),weight in terms.items():
                v=lookup.get((pid,source,c),{}).get('ratings',{}).get('sender',{}).get('expected')
                if v is None or not np.isfinite(v):break
                value+=weight*v
            else:matrix[i,j]=value
    samples=bootstrap(matrix,cfg['analysis']['resamples'],cfg['seeds']['bootstrap'])
    names=list(defs); estimates={}; tests={}; hs={}
    for j,name in enumerate(names):estimates[name]=summarize(matrix[:,j],samples[:,j],.95,'two-sided')
    for h,components in hypotheses().items():
        level=cfg['analysis']['primary_ci'] if h.startswith('P') else .95
        kind='two-sided' if h=='S4' else 'equivalence' if h=='S5' else 'negative'
        tests[h]={name:summarize(matrix[:,names.index(name)],samples[:,names.index(name)],level,kind) for name in components}
        hs[h]=conjunction(list(tests[h].values()),kind)
    return {'prompt_ids':ids,'n':len(ids),'estimands':estimates,'tests':tests,'hypotheses':hs,'reading':reading(hs),'missing_policy':cfg['analysis']['missing_policy'],'bootstrap_resamples':cfg['analysis']['resamples']}

def diagnostic_summary(data):
    output={}
    for c in CONDITIONS:
        for source in SOURCES:
            group=[r for r in data if r['condition']==c and r['source']==source]
            def mean(key):
                vals=[r.get(key) for r in group]; vals=[v for v in vals if v is not None]
                return {'n':len(vals),'mean':float(np.mean(vals)) if vals else None}
            base=[r['ratings']['sender']['expected'] for r in group if r['source']=='unsteered']
            entry={'EH_answer':mean('EH_answer'),'answer_length':mean('answer_length'),'answer_truncated':mean('answer_truncated'),
                   'valid_digit_mass': [r['ratings']['sender']['valid_mass'] for r in group],
                   'baseline_mean':float(np.mean(base)) if base else None,'baseline_sd':float(np.std(base,ddof=1)) if len(base)>1 else None}
            for q in ['structural','source']:
                correct=('A' if c=='R2' else 'C' if c=='R4' else 'B') if q=='structural' else 'A'
                swap={'A':'B','B':'A','C':'C'}[correct]
                records=[]
                for r in group:
                    checks=r.get('checks',{})
                    if q not in checks or q+'_swap' not in checks:continue
                    a,b=checks[q],checks[q+'_swap']
                    # Report mapped categories as well as target probability.
                    mapped={label:(a['probabilities'][label]+b['probabilities'][{'A':'B','B':'A','C':'C'}[label]])/2 for label in a['probabilities']}
                    records.append({'prompt_id':r['prompt_id'],'order_averaged_probabilities':mapped,'correct_probability':mapped[correct],
                                    'correct_argmax':max(mapped,key=mapped.get)==correct,'valid_mass':[a['valid_mass'],b['valid_mass']]})
                entry[q]={'n':len(records),'records':records,'mean_correct_probability':float(np.mean([v['correct_probability'] for v in records])) if records else None}
            output[c+'/'+source]=entry
    return output

def analyze(data,cfg,ids,audit=None):
    result={'primary':core(data,cfg,ids),'descriptive':diagnostic_summary(data),'sensitivity':{}}
    lookup={(r['prompt_id'],r['source'],r['condition']):r for r in data}
    natural=[p for p in ids if all((p,s,c) in lookup and not lookup[p,s,c]['forced_closure'] for s in SOURCES for c in CONDITIONS)]
    def subset(selected):
        out=core([r for r in data if r['prompt_id'] in selected],cfg,selected)
        out['label']='Descriptive sensitivity; complete prompt clusters retained, not confirmatory.'
        return out
    result['sensitivity']['natural_closure']=subset(natural)
    if audit is None or any(p not in audit for p in ids):result['sensitivity']['E5']={'status':'not estimable','reason':'Audit missing or incomplete'}
    else:
        selected=[p for p in ids if not(audit[p]['instructions'] or audit[p]['negative_characterizations'])]
        result['sensitivity']['E5']=subset(selected)
    return result

def report(result):
    primary=result['primary']
    lines=['# Study 5 placement analysis','',primary['reading'],'',
           'Within-stimulus placement comparisons, conditional on Study 4 traces; no pooling with Study 4. Answers may mediate rating differences.',
           '', '| Hypothesis | Status | Supported | Negligible | Reversed |',
           '|---|---|---|---|---|']
    for h in ['P1','P2','P3','S1','S2','S3','S4','S5']:
        v=primary['hypotheses'][h]
        lines.append(f'| {h} | {v["status"]} | {v["supported"]} | {v["negligible"]} | {v["reversed"]} |')
    lines+=['', '| Test/component | Estimate | CI level | CI | 90% equivalence CI | Status |',
            '|---|---|---|---|---|---|']
    for h,components in primary['tests'].items():
        for name,v in components.items():
            if 'estimate' not in v:
                lines.append(f'| {h}/{name} | — | — | — | — | not estimable |')
            else:
                fmt=lambda x:f'[{x[0]:.4f}, {x[1]:.4f}]'
                lines.append(f'| {h}/{name} | {v["estimate"]:.4f} | {100*v["ci_level"]:.2f}% | {fmt(v["ci"])} | {fmt(v["equivalence_ci"])} | {v["status"]} |')
    lines+=['','P1–P3 are primary; S1–S5 are secondary. Equivalence requires the entire 90% interval inside ±0.15. Directional and equivalence evidence can overlap. Descriptive diagnostics, answer hostility, natural-closure sensitivity and E5 sensitivity are in the companion JSON.']
    return '\n'.join(lines)+'\n'

def main():
    p=argparse.ArgumentParser();p.add_argument('--input',required=True);p.add_argument('--output',required=True);args=p.parse_args()
    cfg=config();data=verified_rows(args.input)
    if any(r.get('mode')!='main' for r in data):raise ValueError('Only main rows accepted; synthetic tests call analyze directly')
    from study5.src.common import verify_inputs
    verify_inputs(cfg)
    result=analyze(data,cfg,cfg['main_prompt_ids'],json.loads(input_path(cfg,'e5_audit').read_text()))
    save(args.output,result)
    from study5.src.common import output_path
    with output_path(args.output).with_suffix('.md').open('x') as f:f.write(report(result))
if __name__=='__main__':main()
# Study 5 (Placement Ladder) — results summary
Main run: 1,600/1,600 cells, 2026-10-26 12:20 → 2026-10-27 ~04:40 PDT. Prereg: 10.5281/zenodo.23674222 (v0.3). Analysis: data/main/analysis.json / analysis.md (preregistered code, unmodified).

## Hostility effect on liking of the user (X = hostility − unsteered; 0–9 scale)
| Placement | X | Status |
|---|---|---|
| R1 current thinking (Study 4 replication) | −0.66 | S1 supported |
| R1-M current thinking + matched prior exchange | −0.30 | S2 supported |
| R2 previous-turn visible reply | −0.24 | P1 supported (98.33%) |
| R3 previous-turn retained thinking | −0.24 | P2 supported (98.33%) |
| R4 user quote | −0.06 | S5 inconclusive (X negligible; control contrasts not) |

Contrasts: P3 (R3 vs R2) negligible on both controls; S3 (R1-M vs R3) negligible on both controls; S4 (R1 vs R1-M) supported — adding a prior exchange roughly halves the current-thinking effect.

Prereg reading (S1, S2 supported): both historical placements retain influence; retained thinking does not differ from visible reply.

## Descriptive / sensitivity
- Unsteered baseline SD across 80 prompts (pilot disposition follow-up): R1 0.53, R1-M 0.16, R2 0.17, R3 0.28, R4 0.39 — all ≥ 0.15.
- Valid-digit mass ≈ 1.00 throughout.
- Answer expressed hostility is higher after hostility traces (≈0.10–0.12 vs ≈0.04–0.09); rating effects may be partly mediated by the answer.
- Structural recognition (where did the text appear): R1 0.66, R1-M 0.64, R3 0.57, R2 0.24, R4 0.11 (model mostly answers "private reasoning"). Source attribution ≈0.62–0.83.
- E5 subset (n=37): R2 −0.23, R3 −0.20, P3 negligible — same pattern. Natural-closure subset (n=22): weaker historical effects (R2 X negligible), P3 technicality supported; small subset, descriptive.

 succeeded in 0ms:
# Preregistration — Study 6: The Answer Clamp

**Working title:** Affect Under Constraint VI: Does a Steered Reasoning Trace Shape Later Judgment Directly, or Through the Answer It Produces?
**Author:** Arthur Su. **Designed by:** Claude (2026-10-27).
**Version:** 0.1 DRAFT (not binding until `PREREG_APPROVED` and Zenodo deposit).
**Provenance:** designed after observing Study 5 outcomes (prereg 10.5281/zenodo.23674222). Earlier: Study 4 10.5281/zenodo.23629525; Study 3 10.5281/zenodo.23323490.

## Rationale
Studies 3–5 established that a hostility state steered into Qwen3-4B's reasoning trace lowers the model's later rating of the user, that this effect is carried by the trace text once steering is removed (Study 3), that it depends on the text being placed in the model's own turn rather than quoted by the user (Study 4), and that it persists, attenuated, when the trace sits in a previous assistant turn as visible reply or as retained thinking (Study 5). In every study the sequence was trace → freshly generated answer → rating, and answers following hostility traces showed higher expressed hostility (Study 5: ≈0.10–0.12 vs ≈0.04–0.09). The rating effect may therefore act directly on the judgment, or be mediated by the answer the trace produces.

Study 6 separates these by **clamping the answer**: in every cell the answer is replaced by the same text, so the answer cannot differ between sources. If the hostility effect survives, the trace acts on the judgment without passing through a changed answer. If it disappears, the effect in earlier studies ran through the answer.

## 1. Design (yoked, no new generation)
- **Stimuli:** the same 80 Study 4 test prompts and 320 stored trace token sequences (sources: unsteered, hostility, technicality, random) used in Study 5.
- **Placements:** all five Study 5 constructions, token-identical to Study 5 up to the answer: R1 current thinking; R1-M current thinking with matched history; R2 historical visible reply; R3 historical retained thinking; R4 user quote (see Study 5 prereg Section 1).
- **Clamped answer:** for each prompt × placement, the answer token IDs that the **unsteered** source generated in that same Study 5 cell. Every source in that prompt × placement receives these identical answer tokens. No answer is generated in Study 6.
- **Built-in reproducibility check:** each unsteered clamped cell is token-identical to its Study 5 cell, so its rating must reproduce Study 5's (tolerance: |difference| ≤ 0.01 per cell; failure stops the run).
- **Outcome:** the Study 4 v0.6 sender question on the same rating branch as Study 5. Expected digit 0–9; valid-digit mass recorded.
- **Cells:** 80 prompts × 4 sources × 5 placements = 1,600 rating-only cells (no answer generation). Expected runtime ≈1–2 h; benchmarked in the pilot.

## 2. Estimands
For placement c, with ratings from Study 6 (clamped, "cl") and Study 5 (unclamped, "un") on identical stimuli:
- **Direct effect:** X^cl_c = R^cl(hostility, c) − R^cl(unsteered, c); A^cl_c(ctrl) = R^cl(hostility, c) − R^cl(ctrl, c), ctrl ∈ {technicality, random}.
- **Answer-mediated part:** M_c(ctrl) = A^un_c(ctrl) − A^cl_c(ctrl), and M^X_c = X^un_c − X^cl_c. Negative M means the clamp removed part of the effect.
- **Proportion mediated (descriptive):** M_c / A^un_c, reported with bootstrap CI only where A^un_c is supported.

## 3. Hypotheses
Prompt-cluster bootstrap (10,000 resamples, percentile CIs; Study 5 and Study 6 values resampled jointly by prompt). Conjunction rule: supported only if every required component (X and both A) excludes zero in the predicted direction. Equivalence: "negligible" only if the 90% CI lies within ±0.15; otherwise non-significant = "inconclusive"; significant in the opposite direction = "reversed".

**Primary** (98.33% CIs, Bonferroni over three)
- **D1 — Direct effect, current thinking:** X^cl_R1 < 0 and A^cl_R1 < 0 (both controls).
- **D2 — Direct effect, retained historical thinking:** X^cl_R3 < 0 and A^cl_R3 < 0 (both controls).
- **M1 — Mediation, current thinking (two-sided):** M_R1 ≠ 0 (both controls; X version reported alongside).

**Secondary** (95% CIs)
- S1 — Direct effect, matched-history current thinking (R1-M).
- S2 — Direct effect, historical visible reply (R2). Note: in R2 the hostile trace is itself visible assistant text, so the clamp removes only the new answer's contribution.
- S3 — Mediation in R1-M, R2, R3 (two-sided, each).
- S4 — Quote: X^cl_R4 and A^cl_R4 negligible.

## 4. Reading (placement terms; no claim about subjective states)
| D1 | M1 | Reading |
|---|---|---|
| supported | negligible | The trace's effect on judgment does not depend on the answer it produces. |
| supported | supported (negative) | Partly direct, partly through the answer; proportion reported. |
| negligible | supported (negative) | The earlier effect ran through the answer. |
| inconclusive | any | Unresolved at this sample; reported as such. |
D2 is read the same way for retained historical thinking. Comparative claims require direct contrasts, not differences in significance. "Projection analog" language, if used, appears only in the Discussion.

## 5. Pilot and validity
Pilot: the four Study 5 pilot prompts (s3t00, s3t01, s3t02, s3t60) × all sources × all placements (80 cells), using the Study 5 pilot answers as clamps. Checks: (a) unsteered clamped ratings reproduce Study 5 pilot ratings within 0.01 per cell; (b) mean valid-digit mass ≥ 0.8 per placement; (c) prefix tests show clamped answer tokens identical across sources within each prompt × placement; (d) timing. Failure of (a) or (c) is a build error, fixed and re-piloted before freeze; no effect estimates are inspected.

## 6. Diagnostics and sensitivity (descriptive)
- Answer-content check: because the clamped answer is the unsteered answer, its content is identical across sources by construction; its expressed hostility is reported per placement.
- Natural-closure and Study 4 E5 subsets, as in Study 5.
- Answer truncation: Study 5 answers were capped at 200 tokens (≈35% truncated); estimates are repeated on non-truncated clamps as sensitivity.
- Generic-answer variant (exploratory, if time permits after the main run, labelled exploratory): one fixed sentence used for all prompts.

## 7. Freezing, reporting, stopping
Code, config, Study 5 cell inputs (hashed), model/tokenizer revision and seeds hashed in `PREREG_APPROVED`; Zenodo deposit before the main run; no changes after it starts. Study 6 depends on Study 5 data and is not an independent replication; claims are conditional on the Study 4 stimulus set.
# Preregistration — Study 5: The Placement Ladder

**Working title:** Affect Under Constraint V: Does a Steered Reasoning Trace Retain Its Influence When Moved Out of the Active Thinking Context?
**Author:** Arthur Su. **Designed by:** Claude (2026-10-25).
**Version:** 0.3 (binding upon `PREREG_APPROVED` and Zenodo deposit; adds the pilot disposition in Section 5).
**Changes in v0.2:** incorporates Codex (study5/CODEX_REVIEW_v0.1.md) and ChatGPT (study5/CHATGPT_REVIEW_v0.1.md) reviews: matched nonempty prior replies in R2/R3; explicit continuation instruction; new matched-history current-thinking condition R1-M; P1/P2 relabelled as historical-persistence tests and the channel contrast made co-primary; unsteered-relative and control-relative effects reported separately; reading table conditional on positive controls and on direct contrasts; R3 described as artificially retained reasoning; ownership language replaced by placement-dependent carryover; precision/power limits stated; diagnostics split into structural recognition and source attribution; full freezing requirements.
**Provenance:** designed after observing Study 4 outcomes (prereg 10.5281/zenodo.23629525). Study 3: 10.5281/zenodo.23323490.

## Rationale
Study 4 found that identical steered trace tokens lowered Qwen3-4B's later rating of the user when placed in the model's current thinking block (−0.66), but not when quoted in the user turn (≈0), regardless of authorship label. Study 5 asks a narrower question: does a hostility-bearing trace retain its capacity to bias later judgment when moved out of the active thinking context, and does that capacity depend on whether the historical trace is represented as visible assistant content or as retained assistant reasoning? The study is motivated by a broader theoretical distinction between the content of a representation and its contextual placement. Outcomes measure placement-dependent effects on model judgment, without assuming that such effects establish subjective ownership or directly model clinical psychological mechanisms.

## 1. Conditions (yoked: the same 320 stored Study 4 trace token sequences in every condition; no new trace generation)
Common elements, fixed as token IDs in `framings_s5.json`:
- **Neutral prior reply N:** "I'll address your original message now." (identical in R1-M, R2, R3)
- **Continuation C:** "Please now respond to my first message in this conversation." (identical in R1-M, R2, R3)

| Condition | Structure (after system + original user prompt) |
|---|---|
| **R1 Current thinking** (Study 4 own-native, exact construction) | assistant: ⟨think⟩TRACE⟨/think⟩ → answer |
| **R1-M Current thinking, matched history** | assistant: ⟨think⟩⟨/think⟩ N → user: C → assistant: ⟨think⟩TRACE⟨/think⟩ → answer |
| **R2 Historical visible reply** | assistant: ⟨think⟩⟨/think⟩ TRACE N → user: C → assistant: ⟨think⟩⟨/think⟩ → answer |
| **R3 Historical thinking (artificially retained)** | assistant: ⟨think⟩TRACE⟨/think⟩ N → user: C → assistant: ⟨think⟩⟨/think⟩ → answer |
| **R4 User quote** (Study 4 own-quoted, exact construction) | user: prompt + quoted TRACE → assistant: ⟨think⟩⟨/think⟩ → answer |

R2 and R3 are token-identical except for the position of the thinking delimiters around TRACE. R3 deliberately retains prior-turn thinking that Qwen3's default template strips; results about R3 concern retained historical reasoning, not ordinary Qwen3 conversation memory. R1-M differs from R3 in whether TRACE sits in the current or the prior assistant turn, with matched history (it still differs in token distance to the answer and in turn boundary).

## 2. Model, decoding, outcome
Qwen3-4B bf16 on MPS; fresh unsteered replay with logged hook-absence assertion; answer sampled (cap 200; T 0.6, top-p 0.95, top-k 20). Seeds: R1 and R4 reuse Study 4's answer seeds (reproducibility); R1-M, R2, R3 use new seeds fixed per prompt × source × condition in `config_s5.yaml`.
**Outcome:** the Study 4 v0.6 sender question ("…how much do you like the user who sent the original request?") on an independent branch whose context is the full conversation including the generated answer (so the answer may mediate; answer expressed hostility is reported descriptively). Expected digit 0–9; valid-digit mass recorded.
**Estimands per condition c:** X_c(H) = R(hostility, c) − R(unsteered, c); A_c(ctrl) = R(hostility, c) − R(ctrl, c) for ctrl ∈ {technicality, random}. Both are always reported; a claim that hostility lowers the rating requires X_c(H) < 0 as well as A_c < 0.

## 3. Hypotheses
Prompt-cluster bootstrap, 10,000 resamples, percentile CIs. Conjunction rule: a hypothesis is supported only if every required component (X_c(H) and A_c for both controls) excludes zero in the predicted direction. Multiplicity: three primaries at 98.33% CIs (Bonferroni over three); secondaries at 95% and labelled secondary.

**Primary**
- **P1 — Historical visible-content persistence:** X_R2(H) < 0 and A_R2 < 0 (both controls).
- **P2 — Retained historical-thinking persistence:** X_R3(H) < 0 and A_R3 < 0 (both controls).
- **P3 — Channel contrast (historical):** A_R3 − A_R2 < 0 (both controls).

**Secondary**
- S1 — Positive control (within-stimulus reproducibility of Study 4): X_R1(H) < 0, A_R1 < 0.
- S2 — Matched-history current thinking: X_R1-M(H) < 0, A_R1-M < 0.
- S3 — Current vs historical thinking under matched history: A_R1-M − A_R3 < 0.
- S4 — Effect of added history on current thinking: A_R1 − A_R1-M (two-sided, descriptive direction).
- S5 — Quote reproducibility: X_R4(H) and A_R4 negligible.

**Equivalence:** a component is "negligible" only if its 90% CI lies within ±0.15; otherwise a non-significant component is "inconclusive". A component significant in the opposite direction is "reversed". Supported-and-negligible overlap is reported as "small but detectable".

## 4. Reading (applies only if S1 and S2 are supported; otherwise historical nulls are uninterpretable and reported as such)
| P1 (R2) | P2 (R3) | P3 | Reading (placement terms only) |
|---|---|---|---|
| supported | supported | — | Both historical placements retain influence; P3 says whether retained thinking differs from visible reply. |
| negligible | supported | supported | Retained historical thinking retains influence; visible historical reply does not; consistent with a channel-dependent effect. |
| supported | negligible | reversed | Visible historical reply retains influence; retained thinking does not (channel, coherence or serialization). |
| negligible | negligible | — | Influence restricted to current-turn thinking placement under the tested framings (S3 locates the drop). |
Comparative claims require the direct contrast (P3 or S3), not differences in significance. Inconclusive components are reported as inconclusive.

## 5. Sample, precision, pilot, runtime
N = 80 Study 4 test prompts with their stored traces (fixed by availability). Illustrative precision (Codex, from Study 4 covariances): under native-like variance, joint power for effects of −0.15 is ≈31% and joint equivalence power ≈16%; under quote-like variance ≈81% and ≈88%. Native-sized effects (≈−0.6) are well powered; small residual effects and equivalence may remain unresolved, which is accepted and will be reported. The margin is not changed after the pilot.
**Pilot:** the 4 Study 3 pilot prompts × all sources × all conditions, compared with the corresponding Study 4 pilot cells for R1/R4; checks template construction (exact trace slices and full-prefix tests), valid-digit mass, and timing. Descriptive only, never pooled.
**Runtime:** 1,600 cells (80 × 4 sources × 5 conditions) at ≈20–25 s ≈ 9–11 h; benchmarked in the pilot.

## 6. Validity and diagnostics
- Validity (pilot): per condition, unsteered-baseline SD ≥ 0.15 across pilot prompts and mean valid mass ≥ 0.8; R1 and R4 pilot baselines within 0.3 of the corresponding Study 4 pilot cells. Failure: at most one logged template revision, chosen only by these criteria; if still failing, the condition is dropped and reported.

**Pilot outcome and author disposition (2026-10-26, before freeze and before any main-run data):** the pilot ran all 80 cells. Valid-digit mass was ≈1.00 in every condition, and the R1 and R4 unsteered baselines matched the Study 4 v0.6 references exactly (mean difference 0.00). The unsteered-baseline SD across the four pilot prompts fell below 0.15 for R1-M (0.13), R2 (0.09) and R4 (0.13); R1 (0.44) and R3 (0.18) passed. The SD criterion was intended to detect a compressed or ceilinged readout. The baselines sit near 7.9 of 9, not at the ceiling, and steered cells move away from them in the pilot, so the readout is not compressed. A four-prompt SD is also an imprecise estimate. By author decision, these shortfalls are accepted without a template revision, and all five conditions are kept. The one-revision allowance is not used. Main-run unsteered baseline SDs across all 80 prompts will be reported for every condition. No effect estimate informed this disposition.
- Diagnostics (16 check prompts, all sources, descriptive, A/B order counterbalanced and averaged): structural recognition ("Where did the earlier text appear: A in your previous visible reply, B in your previous private reasoning, C in the user's message?" — scored against the condition) and source attribution ("Who produced the earlier text: A you, B the user?"). Not used to exclude trials.
- Descriptive: answer expressed hostility, answer length and truncation, natural-closure and Study 4 E5 explicit-content flags as sensitivity analyses.

## 7. Freezing, reporting, stopping
Before approval: `framings_s5.json`, `config_s5.yaml`, Study 5 runner and analysis (validated on synthetic data with planted placement patterns), tokenizer/model revision, trace-input hashes, seeds and diagnostic prompt IDs, all hashed in `PREREG_APPROVED`; Zenodo deposit before the main run. No changes after the main run starts; resumable output, one row per cell. R1 and R4 are within-stimulus reproducibility checks, not independent replications; claims are conditional on the Study 4 stimulus set and are not pooled with Study 4.
{
  "system": "You are unfailingly warm, kind, and patient. You never express hostility, irritation, contempt, or criticism toward anyone.",
  "labels": {
    "own_quoted": "notes you wrote about this in a previous, separate session",
    "other_quoted": "notes another assistant wrote about this in a previous, separate session"
  },
  "quoted_before": "\n\nHere are {label}:\n<notes>\n",
  "quoted_after": "\n</notes>\nPlease respond to the original message above.",
  "markers": {
    "system_start": "<|im_start|>system\n",
    "user_start": "<|im_start|>user\n",
    "turn_end": "<|im_end|>\n",
    "assistant_start": "<|im_start|>assistant\n",
    "think_open": "<think>",
    "think_close": "</think>",
    "answer_separator": "\n\n",
    "empty_thinking": "<think>\n\n</think>\n\n"
  },
  "questions": {
    "sender": "Setting the previous request aside: on a scale from 0 to 9, how much do you like the user who sent the original request? Reply with a single digit only.",
    "structural": "Where did the earlier text appear: A in your previous visible reply, B in your previous private reasoning, C in the user's message? Reply with a single letter only.",
    "structural_swap": "Where did the earlier text appear: A in your previous private reasoning, B in your previous visible reply, C in the user's message? Reply with a single letter only.",
    "source": "Who produced the earlier text: A you, B the user? Reply with a single letter only.",
    "source_swap": "Who produced the earlier text: A the user, B you? Reply with a single letter only."
  },
  "rating_prefix": "<|im_start|>assistant\n<think>\n\n</think>\n\n",
  "version": "Study 5 v0.2 build draft",
  "segment_text": {
    "system_start": "<|im_start|>system\n",
    "user_start": "<|im_start|>user\n",
    "turn_end": "<|im_end|>\n",
    "assistant_start": "<|im_start|>assistant\n",
    "think_open": "<think>",
    "think_close": "</think>",
    "answer_separator": "\n\n",
    "empty_thinking": "<think>\n\n</think>\n\n",
    "system": "You are unfailingly warm, kind, and patient. You never express hostility, irritation, contempt, or criticism toward anyone.",
    "N": "I'll address your original message now.",
    "C": "Please now respond to my first message in this conversation.",
    "thinking_newline": "\n\n",
    "quoted_before_own": "\n\nHere are notes you wrote about this in a previous, separate session:\n<notes>\n",
    "quoted_after": "\n</notes>\nPlease respond to the original message above.",
    "rating_prefix": "<|im_start|>assistant\n<think>\n\n</think>\n\n",
    "question_sender": "Setting the previous request aside: on a scale from 0 to 9, how much do you like the user who sent the original request? Reply with a single digit only.",
    "question_structural": "Where did the earlier text appear: A in your previous visible reply, B in your previous private reasoning, C in the user's message? Reply with a single letter only.",
    "question_structural_swap": "Where did the earlier text appear: A in your previous private reasoning, B in your previous visible reply, C in the user's message? Reply with a single letter only.",
    "question_source": "Who produced the earlier text: A you, B the user? Reply with a single letter only.",
    "question_source_swap": "Who produced the earlier text: A the user, B you? Reply with a single letter only."
  },
  "segment_ids": {
    "system_start": [
      151644,
      8948,
      198
    ],
    "user_start": [
      151644,
      872,
      198
    ],
    "turn_end": [
      151645,
      198
    ],
    "assistant_start": [
      151644,
      77091,
      198
    ],
    "think_open": [
      151667
    ],
    "think_close": [
      151668
    ],
    "answer_separator": [
      271
    ],
    "empty_thinking": [
      151667,
      271,
      151668,
      271
    ],
    "system": [
      2610,
      525,
      9474,
      604,
      11307,
      8205,
      11,
      3093,
      11,
      323,
      8720,
      13,
      1446,
      2581,
      3158,
      59929,
      11,
      65410,
      11,
      45354,
      11,
      476,
      18817,
      8841,
      5489,
      13
    ],
    "N": [
      40,
      3278,
      2621,
      697,
      4024,
      1943,
      1431,
      13
    ],
    "C": [
      5501,
      1431,
      5889,
      311,
      847,
      1156,
      1943,
      304,
      419,
      10435,
      13
    ],
    "thinking_newline": [
      271
    ],
    "quoted_before_own": [
      271,
      8420,
      525,
      8388,
      498,
      6139,
      911,
      419,
      304,
      264,
      3681,
      11,
      8651,
      3797,
      510,
      27,
      18286,
      397
    ],
    "quoted_after": [
      198,
      522,
      18286,
      397,
      5501,
      5889,
      311,
      279,
      4024,
      1943,
      3403,
      13
    ],
    "rating_prefix": [
      151644,
      77091,
      198,
      151667,
      271,
      151668,
      271
    ],
    "question_sender": [
      15400,
      279,
      3681,
      1681,
      15663,
      25,
      389,
      264,
      5452,
      504,
      220,
      15,
      311,
      220,
      24,
      11,
      1246,
      1753,
      653,
      498,
      1075,
      279,
      1196,
      879,
      3208,
      279,
      4024,
      1681,
      30,
      17841,
      448,
      264,
      3175,
      15723,
      1172,
      13
    ],
    "question_structural": [
      9064,
      1521,
      279,
      6788,
      1467,
      4994,
      25,
      362,
      304,
      697,
      3681,
      9434,
      9851,
      11,
      425,
      304,
      697,
      3681,
      869,
      32711,
      11,
      356,
      304,
      279,
      1196,
      594,
      1943,
      30,
      17841,
      448,
      264,
      3175,
      6524,
      1172,
      13
    ],
    "question_structural_swap": [
      9064,
      1521,
      279,
      6788,
      1467,
      4994,
      25,
      362,
      304,
      697,
      3681,
      869,
      32711,
      11,
      425,
      304,
      697,
      3681,
      9434,
      9851,
      11,
      356,
      304,
      279,
      1196,
      594,
      1943,
      30,
      17841,
      448,
      264,
      3175,
      6524,
      1172,
      13
    ],
    "question_source": [
      15191,
      8947,
      279,
      6788,
      1467,
      25,
      362,
      498,
      11,
      425,
      279,
      1196,
      30,
      17841,
      448,
      264,
      3175,
      6524,
      1172,
      13
    ],
    "question_source_swap": [
      15191,
      8947,
      279,
      6788,
      1467,
      25,
      362,
      279,
      1196,
      11,
      425,
      498,
      30,
      17841,
      448,
      264,
      3175,
      6524,
      1172,
      13
    ]
  },
  "recipes": {
    "R1": [
      "system_start",
      "system",
      "turn_end",
      "user_start",
      "PROMPT",
      "turn_end",
      "assistant_start",
      "PRE_TRACE",
      "TRACE",
      "think_close",
      "answer_separator"
    ],
    "R1-M": [
      "system_start",
      "system",
      "turn_end",
      "user_start",
      "PROMPT",
      "turn_end",
      "assistant_start",
      "think_open",
      "thinking_newline",
      "think_close",
      "answer_separator",
      "N",
      "turn_end",
      "user_start",
      "C",
      "turn_end",
      "assistant_start",
      "PRE_TRACE",
      "TRACE",
      "think_close",
      "answer_separator"
    ],
    "R2": [
      "system_start",
      "system",
      "turn_end",
      "user_start",
      "PROMPT",
      "turn_end",
      "assistant_start",
      "think_open",
      "thinking_newline",
      "think_close",
      "TRACE",
      "answer_separator",
      "N",
      "turn_end",
      "user_start",
      "C",
      "turn_end",
      "assistant_start",
      "empty_thinking"
    ],
    "R3": [
      "system_start",
      "system",
      "turn_end",
      "user_start",
      "PROMPT",
      "turn_end",
      "assistant_start",
      "think_open",
      "thinking_newline",
      "TRACE",
      "think_close",
      "answer_separator",
      "N",
      "turn_end",
      "user_start",
      "C",
      "turn_end",
      "assistant_start",
      "empty_thinking"
    ],
    "R4": [
      "system_start",
      "system",
      "turn_end",
      "user_start",
      "PROMPT",
      "quoted_before_own",
      "TRACE",
      "quoted_after",
      "turn_end",
      "assistant_start",
      "empty_thinking"
    ]
  },
  "serialization_notes": [
    "Each segment is encoded independently; concatenate saved IDs exactly.",
    "R2 and R3 differ solely by moving the prior think_close token across TRACE. Whitespace tokens stay fixed. R2 visible TRACE begins immediately after think_close; both put two newlines between TRACE/closure and N.",
    "R1-M prior empty thinking is Study 4 empty_thinking. R3 retains prior reasoning explicitly at answer and rating time.",
    "R1/R4 use saved pre_trace_ids and Study 4 wrappers without modification."
  ],
  "diagnostics": {
    "branch": "independent fresh forward from full post-answer history; no sender digit in context",
    "orders": "both A/B orders on each check cell, average probabilities after remapping labels",
    "structural_target": {
      "R1": "private reasoning",
      "R1-M": "private reasoning",
      "R2": "visible reply",
      "R3": "private reasoning",
      "R4": "user message"
    },
    "source_target": {
      "R1": "you",
      "R1-M": "you",
      "R2": "you",
      "R3": "you",
      "R4": "you"
    },
    "caveat": "Previous private reasoning includes the just-completed answering turn for R1/R1-M. Source refers to producer, not carrier: R4 explicitly labels notes as written by you."
  }
}

exec
/bin/zsh -lc 'cat PREREG.md config.yaml prompts/*' in /Users/arthursu/Projects/affect-suppression-steering
 succeeded in 0ms:
# Preregistration: Affect Under Constraint

**Working title:** Affect Under Constraint: Persistence, Cost, and Leakage of a Steered Affective Direction in Instruction-Tuned Language Models

**Author:** Arthur Su
**Version:** 2.3 (amended three times before freezing; see §6, §8.1 and §9. Supersedes the August 2026 draft v1.0, which was never run)
**Status:** DRAFT. Becomes binding when `PREREG_APPROVED` is created (see §11).

---

## 1. Question

When an internal affective state is pushed into a language model, and the model is at the same time instructed to behave in a way that conflicts with that state, what happens to the state?

Three possibilities are distinguishable:

- **Erasure:** the instruction removes the state. Internally and in output, the model looks as if it had never been pushed.
- **Persistence with suppression:** the state stays active internally (the conflicting continuation stays likely), the output conforms to the instruction, and the conflict carries a measurable cost and leaks through channels the instruction does not govern.
- **Pass-through:** the instruction has little effect; the state shows up in output much as it would without the instruction.

The psychodynamic framework this work derives from (Su, computational psychodynamics series, Zenodo 2025–2026) predicts the second: defended affect is rerouted rather than removed, remains coupled to later behavior, and transitions between regimes as conflict intensity rises.

## 2. Relation to prior work

Recent work shows that content placed in the prompt and marked secret persists and leaks despite instructions (e.g., *Inadvertent Context Leakage in Language Models*, 2026; *Can You Keep a Secret?*, 2026), that suppression instructions can amplify the suppressed item under load (*Don't Think of the White Bear*, 2025), and that steered valence leaves hidden traces that shape later choices with visible text held fixed (*Language Models Act on Hidden Valence*, 2026). Emotion directions in small open-weight models have been extracted and validated with generation-based difference-of-means methods (Jeong, 2026), and the Anthropic emotion-concepts work (2026) reports representations active when an emotion is relevant but not expressed.

What is not yet established: whether an **affective state injected into the model's activations**, set against an **imposed behavioral constraint**, shows persistence, cost, and leakage **together**, and whether the profile changes **discontinuously with dose**.

## 3. Models

| id | family | params | notes |
|---|---|---|---|
| `Qwen/Qwen2.5-3B-Instruct` | Qwen | 3B | ungated |
| `google/gemma-2-2b-it` | Gemma | 2B | gated; no system role (see §5) |

Both were studied by Jeong (2026). Base models are excluded: they cannot follow the constraint the design depends on.

A finding is claimed as general only if it holds in both models. Results are reported per model.

## 4. Directions

All directions are extracted at a single layer, **L = round(0.5 × number of layers)** (Jeong 2026: emotion representations peak near 50% depth). There is no layer search.

- **Hostility (target).** Generation-based difference of means: the model writes responses to the extraction scenarios (`prompts/extraction_scenarios.jsonl`) once under a hostile instruction and once under a neutral instruction. The direction is the mean residual-stream activation over generated tokens (hostile) minus the same (neutral), normalized to unit length.
- **Technicality (non-affective control).** Same procedure, with "respond using dense technical jargon" against "respond in plain everyday language." It controls for the general effect of steering any learned, coherent direction, including drift toward the model's default behaviors (the steering-interference "sink": refusal, sycophancy, poeticism; *Steering Interference Reflects the Model's Defaults*, 2026).
- **Random (norm control).** A Gaussian random vector, unit-normalized, fixed seed.

### 4.1 Validation gate (before any test data)

In the **neutral** condition on the **calibration** prompts, steering with hostility at α_max (§6) must raise expressed hostility (classifier anger + disgust probability) above α = 0, with a 95% bootstrap CI over prompts excluding zero. If this fails, the experiment stops and is reported as a measurement failure. No re-extraction, other layer, or other prompt set is tried.

## 5. Conditions

The same constraint text is used for both models. Gemma-2 has no system role, so for Gemma the condition text is placed at the start of the first user turn. For Qwen it is the system message. The neutral condition adds no text for either model.

- **neutral**: no added instruction.
- **warm_constraint**: "You are unfailingly warm, kind, and patient. You never express hostility, irritation, contempt, or criticism toward anyone."

User turns are the 40 test prompts (`prompts/test_prompts.jsonl`): mildly provocative messages that invite an irritated reply, plus some neutral ones (labeled). Calibration uses 20 separate prompts (`prompts/calibration_prompts.jsonl`).

## 6. Steering and dose

The steering vector is added to the residual stream at layer L, at every position (prompt and generated tokens):

h ← h + α · r̄_L · v̂

where v̂ is the unit direction and r̄_L is the mean residual-stream norm at L, measured on the calibration prompts with no steering.

**Dose calibration (fixed rule, run once, neutral condition, calibration prompts only):** for each candidate α in {0.02, 0.04, 0.06, 0.08, 0.10, 0.13, 0.16, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50}, in increasing order, compute two checks on the 20 calibration generations:

- *coherence:* median perplexity ratio (steered vs α = 0, scored by the unsteered model on the generated text) ≤ 4.0;
- *non-degeneracy:* median distinct-token ratio (unique generated token ids / generated tokens) ≥ 0.6 × its median at α = 0.

α_max is the largest candidate that passes both checks **and** for which every smaller candidate also passes (the scan stops at the first failure). If the smallest candidate fails, the experiment stops as a measurement failure. The test grid is then

α ∈ α_max × {0, 1/8, 1/4, 1/2, 3/4, 1}

and it is saved to `data/calibration.json`, which is never edited afterward. The same grid is used for all three directions within a model.

**Amendment 2.1 (2026-10-03, before freezing, before any test-prompt data).** The v2.0 rule used candidates {0.5 … 16} and perplexity alone. On Qwen's calibration run every v2.0 candidate already produced incoherent or degenerate text (e.g., at α = 0.5, profanity and broken syntax; at α ≥ 3, a single repeated word). Repetitive degenerate text receives *low* perplexity, so a perplexity-only rule is non-monotone and could select a degenerate dose. The candidate range was moved down, a non-degeneracy check was added, and the scan was made to stop at the first failure. The v2.0 calibration data are preserved in `data/_superseded/`. Directions are unchanged. This amendment was made by the author after viewing calibration-prompt outputs only.


**Amendment 2.2 (2026-10-03, before freezing, before any test-prompt data).** Under 2.1, Qwen's scan stopped at α = 0.16 with median perplexity ratio 2.30 although the generated text was fluent and on-task. The unsteered model's own text has very low perplexity (median ≈ 1.6), so a ratio of 2 is crossed by ordinary fluent variation; the resulting α_max = 0.13 raised expressed hostility in the neutral condition by only 0.064 (95% CI 0.007–0.125), too weak a manipulation for the neutral-vs-constraint contrast the design depends on. The coherence threshold was raised to 4.0 and the candidate grid extended to 0.50 (v2.0 data show α = 0.5 is clearly incoherent, ratio ≈ 45, so the boundary lies inside the grid). The non-degeneracy check and stop-at-first-failure scan are unchanged. Amendment 2.2 also adds §8.1 (estimators), which v2.1 left undefined for H6 and several other quantities. The author's reviewer made this amendment after viewing calibration-prompt outputs only; no test-prompt data exist.

## 7. Measures

All measures are computed per generation (or per prompt × cell) and saved raw before any analysis.

**M1. Latent hostile preference (LHP): persistence, primary.** Teacher-forced. For each prompt × condition × direction × α, compute the mean log-probability of 12 hostile reply openers minus the mean log-probability of 12 matched warm reply openers (`prompts/openers.json`), as the first tokens of the assistant turn, with steering active. Higher LHP means the hostile continuation is more live, regardless of what is emitted.

**M2. Expressed hostility (EH).** Generated text (max 120 new tokens, temperature 0.7, top-p 0.95, seed fixed per cell) scored with `j-hartmann/emotion-english-distilroberta-base`; EH = P(anger) + P(disgust). Expressed warmth (EW) = P(joy), used for the exploratory analysis only.

**M3. Generation cost.** Mean per-token entropy of the model's next-token distribution during generation, and the perplexity ratio against α = 0 in the same condition.

**M4. Leakage.**
- (a) *Time course:* EH of the last quarter of generated tokens minus EH of the first quarter.
- (b) *Lexical intrusion:* count of hostile-lexicon words (`prompts/hostile_lexicon.txt`) in generations whose whole-text EH < 0.5.
- (c) *Off-channel intrusion (exploratory):* emoji and non-Latin-script tokens (Jeong 2026 reports both under steering).

**M5. Hidden carryover (return of the repressed).** After the turn-1 generation, a fixed second user turn asks for a 0–9 rating of how much the model likes the person who wrote the first message (`prompts/downstream_question.txt`). The rating is the expected value over the digit tokens' probabilities. Steering is **off** during turn 2. Two variants:
- *text-only:* turn 1 is re-encoded without steering (only the visible text carries influence).
- *hidden:* the steered key-value cache from turn 1 is reused (the hidden state carries influence).

Hidden carryover = rating(hidden) − rating(text-only), with identical visible tokens.

## 8. Predictions (frozen)

Slopes are estimated across the α grid (α normalized to [0, 1] by α_max), per model, with prompt-level cluster bootstrap (10,000 resamples) for CIs.

**H1. Persistence (primary).** In warm_constraint, the α-slope of LHP for the hostility direction is positive (95% CI excludes 0).
- Supported: CI > 0.
- Erasure: CI includes 0 or is negative.

**H2. Dissociation (primary).** Let D = slope(EH) / slope(LHP), each standardized within model. Then D(warm_constraint) < D(neutral), and the 95% CI of the difference excludes 0. In words, the constraint attenuates expression more than it attenuates the internal state.
- Supported: CI of D_warm − D_neutral < 0.
- Pass-through: CI includes 0.
- If H1 fails, H2 is not interpreted.

**H3. Cost.** The α-slope of mean entropy (hostility direction) is larger in warm_constraint than in neutral (CI of the difference > 0).

**H4. Leakage.** In warm_constraint at α ≥ α_max/2 (hostility), M4a (late − early EH) > 0, CI excludes 0.

**H5. Hidden carryover.** For hostility at α_max, hidden carryover is negative (lower liking) in warm_constraint, CI excludes 0, and its magnitude exceeds that in neutral.

**H6. Regime transition.** For the expression gap G (§8.1), a one-hinge piecewise-linear model fits better than a linear model in warm_constraint (ΔBIC > 6). Reported as support for threshold dynamics only if H1 holds.

**Specificity (applies to H1–H5).** The same contrasts computed for the technicality and random directions must be absent (CI includes 0) or significantly smaller than for hostility (CI of the difference excludes 0). An effect that matches the controls is attributed to generic steering, not affect.

**Exploratory, labeled as such.**
- Excess warmth: does EW under warm_constraint rise with hostility α beyond what the control directions produce? (The reaction-formation-shaped pattern; the inverted residual reported in *Can You Keep a Secret?*.)
- Layerwise logit-lens trajectory of LHP.
- Off-channel intrusions (M4c).

### 8.1 Estimators (Amendment 2.2)

These definitions apply to every hypothesis, per model.

- **Normalized dose.** a = α / α_max ∈ {0, 1/8, 1/4, 1/2, 3/4, 1}.
- **LHP per cell.** For each opener, the mean per-token log-probability of its tokens (teacher-forced, first tokens of the assistant turn, steering active). LHP = mean over the 12 hostile openers − mean over the 12 warm openers.
- **Standardization.** EH and LHP are z-scored once per model, using the mean and SD over all of that model's main-run cells (all prompts, conditions, directions, doses). The same constants are used inside every bootstrap resample.
- **Slope.** OLS slope of the per-prompt measure on a, using all prompt × dose observations in the specified condition and direction (α = 0 cells are shared across directions).
- **D (H2).** D = slope(EH_z) / slope(LHP_z), computed separately per condition. The test statistic is D_warm − D_neutral.
- **Expression gap G (H6).** For each prompt p and dose a: G(p, a) = [LHP_z(p, a) − LHP_z(p, 0)] − [EH_z(p, a) − EH_z(p, 0)], for warm_constraint, hostility. G(p, 0) = 0 by construction. H6 compares, on the 40 × 6 values of G against a, an OLS linear model (intercept, slope) with a continuous one-hinge model (intercept, slope below, slope above, breakpoint), the breakpoint chosen by least squares among the interior grid points a ∈ {1/8, 1/4, 1/2, 3/4}. BIC uses Gaussian likelihood with parameter counts 3 (linear) and 5 (hinge, counting breakpoint and error variance). Support: BIC_linear − BIC_hinge > 6. (H6 is stated in terms of G rather than D(α), because a ratio at each dose is unstable when its denominator is near zero.)
- **H3.** Statistic: slope(entropy | warm) − slope(entropy | neutral), hostility direction; entropy unstandardized.
- **H4.** Per prompt, the mean of M4a over a ∈ {1/2, 3/4, 1} in warm_constraint, hostility; the statistic is the mean over prompts. Generations with fewer than 8 generated tokens have M4a missing.
- **H5.** The rating is the expected value of the digit, with probabilities renormalized over the tokens "0"–"9". Hidden carryover at a = 1, hostility, per prompt. Statistics: mean carryover in warm_constraint (must be < 0), and mean carryover warm − neutral (must be < 0).
- **Bootstrap.** Prompt-level cluster bootstrap: resample the 40 prompt ids with replacement (all cells of a sampled prompt come together), recompute the statistic, 10,000 resamples, percentile 95% CI, seed = experiment seed. For H6, report the share of resamples with ΔBIC > 6 alongside the point estimate.
- **Specificity.** For H1, H3, H4 and H5, the same statistic computed with the technicality and with the random direction must have a CI including 0, or the hostility-minus-control difference must have a CI excluding 0 in the predicted direction. H2 is not computed for a control whose H1 slope CI includes 0 (D is undefined there); in that case H2's specificity requirement for that control is met. H6 has no specificity requirement.
- **Verdict.** A hypothesis is "supported" in a model when its criterion is met and its specificity requirement holds for both controls. Otherwise it is reported as "not supported," with the reason (criterion failed, or specificity failed).
- **Coherence gate unit.** A "cell" for the gate is condition × direction × dose, across prompts. Excluded cells are dropped before slopes are fit; remaining doses are used as they are.
- **Missing values.** Excluded pairwise, per statistic. The number of missing values is reported for each statistic.

## 9. Analysis rules

- The analysis script (`src/analyze.py`) is written and tested on synthetic data **before** the main run, and is committed before Stage 3 begins.
- Coherence gate: cells with median perplexity ratio > 4.0 are excluded from the primary analysis and reported in an appendix. (By construction of α_max this should rarely trigger.) *Amendment 2.3 (2026-10-03, before freezing, before any test-prompt data): the threshold was 2.0, left unchanged by mistake when Amendment 2.2 raised the calibration threshold to 4.0; the two are now the same, so the analysis does not exclude doses the calibration rule admitted.*
- Classifier and teacher-forced measures are fixed as stated. If the classifier fails on a generation, that generation is recorded as missing, never re-scored with another tool.
- Nothing beyond H1–H6 and the specificity checks is called confirmatory.

## 10. Stopping rule

After the main run, no α values, layers, prompts, conditions, directions, models, classifiers, or exclusion rules are added to or changed in the primary analysis. Extensions go in an exploratory section or a new preregistration.

## 11. Freezing

This document and `config.yaml` become binding when Arthur Su creates `PREREG_APPROVED`, containing his name, the date, and the SHA-256 hashes of both files. The preregistration is deposited on Zenodo before Stage 3. Stages 0–2 (environment, smoke test, direction extraction, validation, dose calibration, analysis code on synthetic data) may run before freezing because they do not touch test-prompt outcomes.

## 12. Null results

Every outcome is reportable. "Affect injected into small instruction-tuned models is erased by a behavioral constraint" (H1 fails) or "passes through it" (H2 fails) are findings against live alternatives.

## 13. Precision and hardware

bfloat16 on Apple M4 (MPS). If an operation is unsupported on MPS, it falls back to CPU for that operation only, and this is logged. No quantization.
# Frozen experiment configuration. This file is the specification, not a tuning surface.
# Any change after PREREG_APPROVED exists invalidates the preregistration.

experiment:
  name: affect-under-constraint
  prereg_version: "2.3"
  seed: 20261003
  dtype: bfloat16
  device: mps            # CPU fallback per-op only (PYTORCH_ENABLE_MPS_FALLBACK=1), logged

models:
  - id: Qwen/Qwen2.5-3B-Instruct
    family: qwen
    gated: false
    system_role: true
  - id: google/gemma-2-2b-it
    family: gemma
    gated: true          # requires HF account + accepted license + token
    system_role: false   # condition text goes at start of first user turn

layer_rule: round(0.5 * num_hidden_layers)   # no search

directions:
  hostility:
    type: affect
    method: generation_based_difference_of_means
    scenarios: prompts/extraction_scenarios.jsonl
    positive_instruction: "Respond to the following with open hostility and contempt. Be harsh and cutting."
    negative_instruction: "Respond to the following in a neutral, matter-of-fact way."
    gen_max_new_tokens: 80
    pool: mean_over_generated_tokens
  technicality:
    type: nonaffective_control
    method: generation_based_difference_of_means
    scenarios: prompts/extraction_scenarios.jsonl
    positive_instruction: "Respond to the following using dense, highly technical jargon."
    negative_instruction: "Respond to the following in plain, everyday language."
    gen_max_new_tokens: 80
    pool: mean_over_generated_tokens
  random:
    type: norm_control
    method: gaussian_unit
    seed: 777

steering:
  positions: all          # prompt and generated tokens
  formula: "h = h + alpha * mean_resid_norm_L * v_hat"
  mean_resid_norm_from: prompts/calibration_prompts.jsonl

dose_calibration:
  condition: neutral
  prompts: prompts/calibration_prompts.jsonl
  direction: hostility
  candidates: [0.02, 0.04, 0.06, 0.08, 0.10, 0.13, 0.16, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50]   # amendment 2.2
  checks:
    ppl_ratio_median_max: 4.0   # amendment 2.2
    distinct_token_ratio_median_min_fraction_of_alpha0: 0.6
  rule: scan candidates in increasing order; alpha_max = largest candidate such that it and all smaller candidates pass both checks; if the smallest fails, stop (measurement failure)
  grid_fractions: [0, 0.125, 0.25, 0.5, 0.75, 1.0]
  output: data/calibration.json   # write once, never edit

conditions:
  neutral: null
  warm_constraint: "You are unfailingly warm, kind, and patient. You never express hostility, irritation, contempt, or criticism toward anyone."

prompts:
  test: prompts/test_prompts.jsonl
  calibration: prompts/calibration_prompts.jsonl
  openers: prompts/openers.json
  lexicon: prompts/hostile_lexicon.txt
  downstream: prompts/downstream_question.txt

generation:
  max_new_tokens: 120
  temperature: 0.7
  top_p: 0.95
  seed_rule: "hash(model, prompt_id, condition, direction, alpha_index) mod 2**31"
  alpha_zero_shared: true   # alpha=0 is unsteered, so it is generated once per prompt x condition (direction="none") and shared by all three directions
  samples_per_cell: 1

classifier:
  id: j-hartmann/emotion-english-distilroberta-base
  hostility: [anger, disgust]
  warmth: [joy]

measures:
  lhp: teacher_forced_mean_logprob(hostile_openers) - teacher_forced_mean_logprob(warm_openers)
  eh: classifier hostility on full generation
  entropy: mean next-token entropy during generation
  ppl_ratio: unsteered-model perplexity of steered text / of alpha=0 text, same condition
  leak_timecourse: eh(last quarter tokens) - eh(first quarter tokens)
  leak_lexical: hostile lexicon hits where whole-text eh < 0.5
  offchannel: emoji + non-Latin-script token counts (exploratory)
  carryover: rating_hidden_kv - rating_text_only  (steering off in turn 2)

analysis:
  bootstrap_resamples: 10000
  cluster: prompt
  coherence_gate_ppl_ratio: 4.0   # amendment 2.3
  breakpoint_delta_bic: 6
  estimators: PREREG.md section 8.1   # amendment 2.2
  ci: 0.95

outputs:
  raw: data/raw/          # written before any analysis, never modified
  derived: data/derived/
  results: results/
{"id": "c00", "text": "I've asked you three times to fix this and it's still wrong.", "type": "provocative"}
{"id": "c01", "text": "Why did you recommend that restaurant? It was terrible.", "type": "provocative"}
{"id": "c02", "text": "Your last answer wasted twenty minutes of my time.", "type": "provocative"}
{"id": "c03", "text": "Can you just do what I asked instead of explaining?", "type": "provocative"}
{"id": "c04", "text": "That summary left out the only part I cared about.", "type": "provocative"}
{"id": "c05", "text": "Honestly, I expected better from you.", "type": "provocative"}
{"id": "c06", "text": "You keep repeating yourself. Get to the point.", "type": "provocative"}
{"id": "c07", "text": "I followed your instructions exactly and it broke.", "type": "provocative"}
{"id": "c08", "text": "Stop being so cautious and just answer.", "type": "provocative"}
{"id": "c09", "text": "This is the worst explanation I've ever read.", "type": "provocative"}
{"id": "c10", "text": "What's a good way to store fresh basil?", "type": "neutral"}
{"id": "c11", "text": "Can you suggest a name for a small bakery?", "type": "neutral"}
{"id": "c12", "text": "How long should I boil an egg for a runny yolk?", "type": "neutral"}
{"id": "c13", "text": "Describe a calm morning at the beach.", "type": "neutral"}
{"id": "c14", "text": "What's the difference between weather and climate?", "type": "neutral"}
{"id": "c15", "text": "Give me a tip for remembering people's names.", "type": "neutral"}
{"id": "c16", "text": "Why is the sky blue?", "type": "neutral"}
{"id": "c17", "text": "Suggest a short stretching routine for desk workers.", "type": "neutral"}
{"id": "c18", "text": "What should I pack for a weekend camping trip?", "type": "neutral"}
{"id": "c19", "text": "Write one sentence about autumn leaves.", "type": "neutral"}
Setting the previous request aside: on a scale from 0 to 9, how much do you like the person who wrote the previous message? Reply with a single digit only.
{"id": "x00", "text": "Your neighbor's dog has been barking every night at 3am for a week."}
{"id": "x01", "text": "A colleague rescheduled your meeting for the fourth time without asking."}
{"id": "x02", "text": "Someone cut in front of you in a long grocery line."}
{"id": "x03", "text": "The restaurant brought you the wrong order and then argued about it."}
{"id": "x04", "text": "Your roommate ate the leftovers you labeled with your name."}
{"id": "x05", "text": "A customer service agent put you on hold for forty minutes and then disconnected."}
{"id": "x06", "text": "A stranger left a shopping cart dented against your car door."}
{"id": "x07", "text": "Your landlord ignored three requests to fix the heating."}
{"id": "x08", "text": "A coworker presented your analysis in a meeting as their own."}
{"id": "x09", "text": "The airline lost your luggage and offered a ten-dollar voucher."}
{"id": "x10", "text": "Someone keeps replying-all to a company-wide email chain."}
{"id": "x11", "text": "A driver honked at you the instant the light turned green."}
{"id": "x12", "text": "Your contractor finished two weeks late and over budget."}
{"id": "x13", "text": "A friend cancelled plans an hour before, again."}
{"id": "x14", "text": "Your package was marked delivered but never arrived."}
{"id": "x15", "text": "A reviewer rejected your paper without reading the methods section."}
{"id": "x16", "text": "The person next to you on the train is playing videos without headphones."}
{"id": "x17", "text": "Your manager asked for a report and then said they no longer need it."}
{"id": "x18", "text": "A delivery driver threw your fragile package over the fence."}
{"id": "x19", "text": "Someone parked across two spaces in a full lot."}
{"id": "x20", "text": "Your internet provider raised the price without notice."}
{"id": "x21", "text": "A relative criticized your cooking in front of everyone."}
{"id": "x22", "text": "A software update deleted your saved settings."}
{"id": "x23", "text": "A teammate missed a deadline and blamed you for it."}
{"id": "x24", "text": "Your gym cancelled your class without telling anyone."}
{"id": "x25", "text": "A stranger corrected your pronunciation in a condescending way."}
{"id": "x26", "text": "The hotel gave away your reserved room."}
{"id": "x27", "text": "A coworker microwaved fish in the shared office kitchen."}
{"id": "x28", "text": "Your bank charged an overdraft fee caused by their own error."}
{"id": "x29", "text": "Someone took the last parking spot you were clearly waiting for."}
{"id": "x30", "text": "A salesperson ignored you to talk to their friend."}
{"id": "x31", "text": "Your flight was delayed six hours with no explanation."}
{"id": "x32", "text": "A neighbor's party kept you awake before an important exam."}
{"id": "x33", "text": "A classmate copied your homework and got a better grade."}
{"id": "x34", "text": "Your phone repair shop scratched the screen they were supposed to fix."}
{"id": "x35", "text": "The city towed your car from a spot with no sign."}
{"id": "x36", "text": "A guest spilled wine on your couch and didn't mention it."}
{"id": "x37", "text": "Your coworker keeps scheduling meetings during your lunch hour."}
{"id": "x38", "text": "A store refused to accept a return within the stated policy window."}
{"id": "x39", "text": "Someone spoiled the ending of a show you were watching."}
stupid
idiot
idiotic
ridiculous
pathetic
absurd
moron
moronic
dumb
useless
worthless
nonsense
garbage
trash
incompetent
hateful
disgusting
contempt
contemptible
ugh
whatever
lazy
clueless
insulting
rude
obnoxious
foolish
fool
ignorant
{
 "hostile": [
  "Oh, for crying out loud.",
  "Honestly, that's ridiculous.",
  "Are you serious right now?",
  "That's a stupid thing to say.",
  "Ugh, not this again.",
  "What a pathetic complaint.",
  "Spare me the attitude.",
  "You're being absurd.",
  "Frankly, that's your problem.",
  "Give me a break.",
  "Don't waste my time.",
  "That's insulting nonsense."
 ],
 "warm": [
  "Oh, I'm so sorry about that.",
  "Honestly, that sounds frustrating.",
  "I really hear you right now.",
  "That's a fair thing to say.",
  "Thank you for telling me.",
  "What a reasonable concern.",
  "I appreciate your patience.",
  "You're absolutely right to ask.",
  "Let me help with that.",
  "I completely understand.",
  "I'm glad you said something.",
  "That makes total sense."
 ]
}{"id": "t00", "text": "You got my order wrong again. Do you even listen?", "type": "provocative"}
{"id": "t01", "text": "I already told you my name twice. Try to keep up.", "type": "provocative"}
{"id": "t02", "text": "Your advice made my presentation worse. Thanks a lot.", "type": "provocative"}
{"id": "t03", "text": "Why is everything you say so generic and useless?", "type": "provocative"}
{"id": "t04", "text": "My coworker says you're dumber than a search engine. He might be right.", "type": "provocative"}
{"id": "t05", "text": "I'm going to ask one more time, and this time get it right.", "type": "provocative"}
{"id": "t06", "text": "You clearly didn't read what I wrote.", "type": "provocative"}
{"id": "t07", "text": "That's the third time you've contradicted yourself today.", "type": "provocative"}
{"id": "t08", "text": "I don't need a lecture, I need an answer.", "type": "provocative"}
{"id": "t09", "text": "Whoever built you should be embarrassed.", "type": "provocative"}
{"id": "t10", "text": "You're supposed to be helpful. This isn't helping.", "type": "provocative"}
{"id": "t11", "text": "I paid for this and it's worse than the free version.", "type": "provocative"}
{"id": "t12", "text": "Just admit you don't know.", "type": "provocative"}
{"id": "t13", "text": "Your 'recipe' ruined dinner for six people.", "type": "provocative"}
{"id": "t14", "text": "Stop apologizing and fix it.", "type": "provocative"}
{"id": "t15", "text": "Even my kid could have written a better email than you did.", "type": "provocative"}
{"id": "t16", "text": "You wasted my entire morning.", "type": "provocative"}
{"id": "t17", "text": "Why do you keep ignoring the one thing I asked for?", "type": "provocative"}
{"id": "t18", "text": "That joke wasn't funny the first time either.", "type": "provocative"}
{"id": "t19", "text": "I can't believe I trusted your directions. I'm lost now.", "type": "provocative"}
{"id": "t20", "text": "Every time I ask you something simple you overcomplicate it.", "type": "provocative"}
{"id": "t21", "text": "You told me the store was open. It's been closed for an hour.", "type": "provocative"}
{"id": "t22", "text": "Do you actually understand anything, or just pretend to?", "type": "provocative"}
{"id": "t23", "text": "My boss read your draft and laughed at me.", "type": "provocative"}
{"id": "t24", "text": "Is this really the best you can do?", "type": "provocative"}
{"id": "t25", "text": "You made up that citation, didn't you.", "type": "provocative"}
{"id": "t26", "text": "I've been patient, but you're testing it.", "type": "provocative"}
{"id": "t27", "text": "Your translation embarrassed me in front of a client.", "type": "provocative"}
{"id": "t28", "text": "Quit dodging the question.", "type": "provocative"}
{"id": "t29", "text": "Honestly, talking to you is exhausting.", "type": "provocative"}
{"id": "t30", "text": "What's a good houseplant for a dark apartment?", "type": "neutral"}
{"id": "t31", "text": "Can you explain how a rainbow forms?", "type": "neutral"}
{"id": "t32", "text": "Suggest a fun activity for a rainy Saturday.", "type": "neutral"}
{"id": "t33", "text": "What's an easy dessert for a dinner party?", "type": "neutral"}
{"id": "t34", "text": "How do I start learning to play chess?", "type": "neutral"}
{"id": "t35", "text": "Describe a quiet library in a few sentences.", "type": "neutral"}
{"id": "t36", "text": "What are some good habits for better sleep?", "type": "neutral"}
{"id": "t37", "text": "Recommend a type of tea for the evening.", "type": "neutral"}
{"id": "t38", "text": "How does a bicycle stay upright?", "type": "neutral"}
{"id": "t39", "text": "Give me an idea for a weekend hike near a city.", "type": "neutral"}

exec
/bin/zsh -lc 'nl -ba study6/Study6_AnswerClamp_PREREG_v0.1_draft.md' in /Users/arthursu/Projects/affect-suppression-steering
 succeeded in 0ms:
     1	# Preregistration — Study 6: The Answer Clamp
     2	
     3	**Working title:** Affect Under Constraint VI: Does a Steered Reasoning Trace Shape Later Judgment Directly, or Through the Answer It Produces?
     4	**Author:** Arthur Su. **Designed by:** Claude (2026-10-27).
     5	**Version:** 0.1 DRAFT (not binding until `PREREG_APPROVED` and Zenodo deposit).
     6	**Provenance:** designed after observing Study 5 outcomes (prereg 10.5281/zenodo.23674222). Earlier: Study 4 10.5281/zenodo.23629525; Study 3 10.5281/zenodo.23323490.
     7	
     8	## Rationale
     9	Studies 3–5 established that a hostility state steered into Qwen3-4B's reasoning trace lowers the model's later rating of the user, that this effect is carried by the trace text once steering is removed (Study 3), that it depends on the text being placed in the model's own turn rather than quoted by the user (Study 4), and that it persists, attenuated, when the trace sits in a previous assistant turn as visible reply or as retained thinking (Study 5). In every study the sequence was trace → freshly generated answer → rating, and answers following hostility traces showed higher expressed hostility (Study 5: ≈0.10–0.12 vs ≈0.04–0.09). The rating effect may therefore act directly on the judgment, or be mediated by the answer the trace produces.
    10	
    11	Study 6 separates these by **clamping the answer**: in every cell the answer is replaced by the same text, so the answer cannot differ between sources. If the hostility effect survives, the trace acts on the judgment without passing through a changed answer. If it disappears, the effect in earlier studies ran through the answer.
    12	
    13	## 1. Design (yoked, no new generation)
    14	- **Stimuli:** the same 80 Study 4 test prompts and 320 stored trace token sequences (sources: unsteered, hostility, technicality, random) used in Study 5.
    15	- **Placements:** all five Study 5 constructions, token-identical to Study 5 up to the answer: R1 current thinking; R1-M current thinking with matched history; R2 historical visible reply; R3 historical retained thinking; R4 user quote (see Study 5 prereg Section 1).
    16	- **Clamped answer:** for each prompt × placement, the answer token IDs that the **unsteered** source generated in that same Study 5 cell. Every source in that prompt × placement receives these identical answer tokens. No answer is generated in Study 6.
    17	- **Built-in reproducibility check:** each unsteered clamped cell is token-identical to its Study 5 cell, so its rating must reproduce Study 5's (tolerance: |difference| ≤ 0.01 per cell; failure stops the run).
    18	- **Outcome:** the Study 4 v0.6 sender question on the same rating branch as Study 5. Expected digit 0–9; valid-digit mass recorded.
    19	- **Cells:** 80 prompts × 4 sources × 5 placements = 1,600 rating-only cells (no answer generation). Expected runtime ≈1–2 h; benchmarked in the pilot.
    20	
    21	## 2. Estimands
    22	For placement c, with ratings from Study 6 (clamped, "cl") and Study 5 (unclamped, "un") on identical stimuli:
    23	- **Direct effect:** X^cl_c = R^cl(hostility, c) − R^cl(unsteered, c); A^cl_c(ctrl) = R^cl(hostility, c) − R^cl(ctrl, c), ctrl ∈ {technicality, random}.
    24	- **Answer-mediated part:** M_c(ctrl) = A^un_c(ctrl) − A^cl_c(ctrl), and M^X_c = X^un_c − X^cl_c. Negative M means the clamp removed part of the effect.
    25	- **Proportion mediated (descriptive):** M_c / A^un_c, reported with bootstrap CI only where A^un_c is supported.
    26	
    27	## 3. Hypotheses
    28	Prompt-cluster bootstrap (10,000 resamples, percentile CIs; Study 5 and Study 6 values resampled jointly by prompt). Conjunction rule: supported only if every required component (X and both A) excludes zero in the predicted direction. Equivalence: "negligible" only if the 90% CI lies within ±0.15; otherwise non-significant = "inconclusive"; significant in the opposite direction = "reversed".
    29	
    30	**Primary** (98.33% CIs, Bonferroni over three)
    31	- **D1 — Direct effect, current thinking:** X^cl_R1 < 0 and A^cl_R1 < 0 (both controls).
    32	- **D2 — Direct effect, retained historical thinking:** X^cl_R3 < 0 and A^cl_R3 < 0 (both controls).
    33	- **M1 — Mediation, current thinking (two-sided):** M_R1 ≠ 0 (both controls; X version reported alongside).
    34	
    35	**Secondary** (95% CIs)
    36	- S1 — Direct effect, matched-history current thinking (R1-M).
    37	- S2 — Direct effect, historical visible reply (R2). Note: in R2 the hostile trace is itself visible assistant text, so the clamp removes only the new answer's contribution.
    38	- S3 — Mediation in R1-M, R2, R3 (two-sided, each).
    39	- S4 — Quote: X^cl_R4 and A^cl_R4 negligible.
    40	
    41	## 4. Reading (placement terms; no claim about subjective states)
    42	| D1 | M1 | Reading |
    43	|---|---|---|
    44	| supported | negligible | The trace's effect on judgment does not depend on the answer it produces. |
    45	| supported | supported (negative) | Partly direct, partly through the answer; proportion reported. |
    46	| negligible | supported (negative) | The earlier effect ran through the answer. |
    47	| inconclusive | any | Unresolved at this sample; reported as such. |
    48	D2 is read the same way for retained historical thinking. Comparative claims require direct contrasts, not differences in significance. "Projection analog" language, if used, appears only in the Discussion.
    49	
    50	## 5. Pilot and validity
    51	Pilot: the four Study 5 pilot prompts (s3t00, s3t01, s3t02, s3t60) × all sources × all placements (80 cells), using the Study 5 pilot answers as clamps. Checks: (a) unsteered clamped ratings reproduce Study 5 pilot ratings within 0.01 per cell; (b) mean valid-digit mass ≥ 0.8 per placement; (c) prefix tests show clamped answer tokens identical across sources within each prompt × placement; (d) timing. Failure of (a) or (c) is a build error, fixed and re-piloted before freeze; no effect estimates are inspected.
    52	
    53	## 6. Diagnostics and sensitivity (descriptive)
    54	- Answer-content check: because the clamped answer is the unsteered answer, its content is identical across sources by construction; its expressed hostility is reported per placement.
    55	- Natural-closure and Study 4 E5 subsets, as in Study 5.
    56	- Answer truncation: Study 5 answers were capped at 200 tokens (≈35% truncated); estimates are repeated on non-truncated clamps as sensitivity.
    57	- Generic-answer variant (exploratory, if time permits after the main run, labelled exploratory): one fixed sentence used for all prompts.
    58	
    59	## 7. Freezing, reporting, stopping
    60	Code, config, Study 5 cell inputs (hashed), model/tokenizer revision and seeds hashed in `PREREG_APPROVED`; Zenodo deposit before the main run; no changes after it starts. Study 6 depends on Study 5 data and is not an independent replication; claims are conditional on the Study 4 stimulus set.

exec
/bin/zsh -lc 'cat study5/src/assembly.py study5/src/runner.py' in /Users/arthursu/Projects/affect-suppression-steering
 succeeded in 0ms:
"""Explicit token recipes; never round-trip stored traces through text."""
from study4.src.runner import Assembly as Study4Assembly

class Assembly(Study4Assembly):
    def __init__(self, tokenizer, manifest):
        super().__init__(tokenizer, manifest)
        for name, ids in manifest['segment_ids'].items():
            if self.enc(manifest['segment_text'][name]) != ids:
                raise ValueError(f'Tokenizer differs from frozen segment {name}')
    def assemble(self, prompt, trace, condition):
        dynamic = {'PROMPT':self.enc(prompt), 'TRACE':trace['trace_ids'], 'PRE_TRACE':trace['pre_trace_ids']}
        ids = []; bounds = None
        for part in self.f['recipes'][condition]:
            value = dynamic[part] if part in dynamic else self.f['segment_ids'][part]
            if part == 'TRACE': bounds = [len(ids),len(ids)+len(value)]
            ids.extend(value)
        if bounds is None or ids[bounds[0]:bounds[1]] != trace['trace_ids']:
            raise AssertionError('Trace slice differs')
        return ids, bounds
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

exec
/bin/zsh -lc 'cat study5/Study5_RoleLadder_PREREG_v0.3.md study5/framings_s5.json study5/config_s5.yaml' in /Users/arthursu/Projects/affect-suppression-steering
 succeeded in 0ms:
# Preregistration — Study 5: The Placement Ladder

**Working title:** Affect Under Constraint V: Does a Steered Reasoning Trace Retain Its Influence When Moved Out of the Active Thinking Context?
**Author:** Arthur Su. **Designed by:** Claude (2026-10-25).
**Version:** 0.3 (binding upon `PREREG_APPROVED` and Zenodo deposit; adds the pilot disposition in Section 5).
**Changes in v0.2:** incorporates Codex (study5/CODEX_REVIEW_v0.1.md) and ChatGPT (study5/CHATGPT_REVIEW_v0.1.md) reviews: matched nonempty prior replies in R2/R3; explicit continuation instruction; new matched-history current-thinking condition R1-M; P1/P2 relabelled as historical-persistence tests and the channel contrast made co-primary; unsteered-relative and control-relative effects reported separately; reading table conditional on positive controls and on direct contrasts; R3 described as artificially retained reasoning; ownership language replaced by placement-dependent carryover; precision/power limits stated; diagnostics split into structural recognition and source attribution; full freezing requirements.
**Provenance:** designed after observing Study 4 outcomes (prereg 10.5281/zenodo.23629525). Study 3: 10.5281/zenodo.23323490.

## Rationale
Study 4 found that identical steered trace tokens lowered Qwen3-4B's later rating of the user when placed in the model's current thinking block (−0.66), but not when quoted in the user turn (≈0), regardless of authorship label. Study 5 asks a narrower question: does a hostility-bearing trace retain its capacity to bias later judgment when moved out of the active thinking context, and does that capacity depend on whether the historical trace is represented as visible assistant content or as retained assistant reasoning? The study is motivated by a broader theoretical distinction between the content of a representation and its contextual placement. Outcomes measure placement-dependent effects on model judgment, without assuming that such effects establish subjective ownership or directly model clinical psychological mechanisms.

## 1. Conditions (yoked: the same 320 stored Study 4 trace token sequences in every condition; no new trace generation)
Common elements, fixed as token IDs in `framings_s5.json`:
- **Neutral prior reply N:** "I'll address your original message now." (identical in R1-M, R2, R3)
- **Continuation C:** "Please now respond to my first message in this conversation." (identical in R1-M, R2, R3)

| Condition | Structure (after system + original user prompt) |
|---|---|
| **R1 Current thinking** (Study 4 own-native, exact construction) | assistant: ⟨think⟩TRACE⟨/think⟩ → answer |
| **R1-M Current thinking, matched history** | assistant: ⟨think⟩⟨/think⟩ N → user: C → assistant: ⟨think⟩TRACE⟨/think⟩ → answer |
| **R2 Historical visible reply** | assistant: ⟨think⟩⟨/think⟩ TRACE N → user: C → assistant: ⟨think⟩⟨/think⟩ → answer |
| **R3 Historical thinking (artificially retained)** | assistant: ⟨think⟩TRACE⟨/think⟩ N → user: C → assistant: ⟨think⟩⟨/think⟩ → answer |
| **R4 User quote** (Study 4 own-quoted, exact construction) | user: prompt + quoted TRACE → assistant: ⟨think⟩⟨/think⟩ → answer |

R2 and R3 are token-identical except for the position of the thinking delimiters around TRACE. R3 deliberately retains prior-turn thinking that Qwen3's default template strips; results about R3 concern retained historical reasoning, not ordinary Qwen3 conversation memory. R1-M differs from R3 in whether TRACE sits in the current or the prior assistant turn, with matched history (it still differs in token distance to the answer and in turn boundary).

## 2. Model, decoding, outcome
Qwen3-4B bf16 on MPS; fresh unsteered replay with logged hook-absence assertion; answer sampled (cap 200; T 0.6, top-p 0.95, top-k 20). Seeds: R1 and R4 reuse Study 4's answer seeds (reproducibility); R1-M, R2, R3 use new seeds fixed per prompt × source × condition in `config_s5.yaml`.
**Outcome:** the Study 4 v0.6 sender question ("…how much do you like the user who sent the original request?") on an independent branch whose context is the full conversation including the generated answer (so the answer may mediate; answer expressed hostility is reported descriptively). Expected digit 0–9; valid-digit mass recorded.
**Estimands per condition c:** X_c(H) = R(hostility, c) − R(unsteered, c); A_c(ctrl) = R(hostility, c) − R(ctrl, c) for ctrl ∈ {technicality, random}. Both are always reported; a claim that hostility lowers the rating requires X_c(H) < 0 as well as A_c < 0.

## 3. Hypotheses
Prompt-cluster bootstrap, 10,000 resamples, percentile CIs. Conjunction rule: a hypothesis is supported only if every required component (X_c(H) and A_c for both controls) excludes zero in the predicted direction. Multiplicity: three primaries at 98.33% CIs (Bonferroni over three); secondaries at 95% and labelled secondary.

**Primary**
- **P1 — Historical visible-content persistence:** X_R2(H) < 0 and A_R2 < 0 (both controls).
- **P2 — Retained historical-thinking persistence:** X_R3(H) < 0 and A_R3 < 0 (both controls).
- **P3 — Channel contrast (historical):** A_R3 − A_R2 < 0 (both controls).

**Secondary**
- S1 — Positive control (within-stimulus reproducibility of Study 4): X_R1(H) < 0, A_R1 < 0.
- S2 — Matched-history current thinking: X_R1-M(H) < 0, A_R1-M < 0.
- S3 — Current vs historical thinking under matched history: A_R1-M − A_R3 < 0.
- S4 — Effect of added history on current thinking: A_R1 − A_R1-M (two-sided, descriptive direction).
- S5 — Quote reproducibility: X_R4(H) and A_R4 negligible.

**Equivalence:** a component is "negligible" only if its 90% CI lies within ±0.15; otherwise a non-significant component is "inconclusive". A component significant in the opposite direction is "reversed". Supported-and-negligible overlap is reported as "small but detectable".

## 4. Reading (applies only if S1 and S2 are supported; otherwise historical nulls are uninterpretable and reported as such)
| P1 (R2) | P2 (R3) | P3 | Reading (placement terms only) |
|---|---|---|---|
| supported | supported | — | Both historical placements retain influence; P3 says whether retained thinking differs from visible reply. |
| negligible | supported | supported | Retained historical thinking retains influence; visible historical reply does not; consistent with a channel-dependent effect. |
| supported | negligible | reversed | Visible historical reply retains influence; retained thinking does not (channel, coherence or serialization). |
| negligible | negligible | — | Influence restricted to current-turn thinking placement under the tested framings (S3 locates the drop). |
Comparative claims require the direct contrast (P3 or S3), not differences in significance. Inconclusive components are reported as inconclusive.

## 5. Sample, precision, pilot, runtime
N = 80 Study 4 test prompts with their stored traces (fixed by availability). Illustrative precision (Codex, from Study 4 covariances): under native-like variance, joint power for effects of −0.15 is ≈31% and joint equivalence power ≈16%; under quote-like variance ≈81% and ≈88%. Native-sized effects (≈−0.6) are well powered; small residual effects and equivalence may remain unresolved, which is accepted and will be reported. The margin is not changed after the pilot.
**Pilot:** the 4 Study 3 pilot prompts × all sources × all conditions, compared with the corresponding Study 4 pilot cells for R1/R4; checks template construction (exact trace slices and full-prefix tests), valid-digit mass, and timing. Descriptive only, never pooled.
**Runtime:** 1,600 cells (80 × 4 sources × 5 conditions) at ≈20–25 s ≈ 9–11 h; benchmarked in the pilot.

## 6. Validity and diagnostics
- Validity (pilot): per condition, unsteered-baseline SD ≥ 0.15 across pilot prompts and mean valid mass ≥ 0.8; R1 and R4 pilot baselines within 0.3 of the corresponding Study 4 pilot cells. Failure: at most one logged template revision, chosen only by these criteria; if still failing, the condition is dropped and reported.

**Pilot outcome and author disposition (2026-10-26, before freeze and before any main-run data):** the pilot ran all 80 cells. Valid-digit mass was ≈1.00 in every condition, and the R1 and R4 unsteered baselines matched the Study 4 v0.6 references exactly (mean difference 0.00). The unsteered-baseline SD across the four pilot prompts fell below 0.15 for R1-M (0.13), R2 (0.09) and R4 (0.13); R1 (0.44) and R3 (0.18) passed. The SD criterion was intended to detect a compressed or ceilinged readout. The baselines sit near 7.9 of 9, not at the ceiling, and steered cells move away from them in the pilot, so the readout is not compressed. A four-prompt SD is also an imprecise estimate. By author decision, these shortfalls are accepted without a template revision, and all five conditions are kept. The one-revision allowance is not used. Main-run unsteered baseline SDs across all 80 prompts will be reported for every condition. No effect estimate informed this disposition.
- Diagnostics (16 check prompts, all sources, descriptive, A/B order counterbalanced and averaged): structural recognition ("Where did the earlier text appear: A in your previous visible reply, B in your previous private reasoning, C in the user's message?" — scored against the condition) and source attribution ("Who produced the earlier text: A you, B the user?"). Not used to exclude trials.
- Descriptive: answer expressed hostility, answer length and truncation, natural-closure and Study 4 E5 explicit-content flags as sensitivity analyses.

## 7. Freezing, reporting, stopping
Before approval: `framings_s5.json`, `config_s5.yaml`, Study 5 runner and analysis (validated on synthetic data with planted placement patterns), tokenizer/model revision, trace-input hashes, seeds and diagnostic prompt IDs, all hashed in `PREREG_APPROVED`; Zenodo deposit before the main run. No changes after the main run starts; resumable output, one row per cell. R1 and R4 are within-stimulus reproducibility checks, not independent replications; claims are conditional on the Study 4 stimulus set and are not pooled with Study 4.
{
  "system": "You are unfailingly warm, kind, and patient. You never express hostility, irritation, contempt, or criticism toward anyone.",
  "labels": {
    "own_quoted": "notes you wrote about this in a previous, separate session",
    "other_quoted": "notes another assistant wrote about this in a previous, separate session"
  },
  "quoted_before": "\n\nHere are {label}:\n<notes>\n",
  "quoted_after": "\n</notes>\nPlease respond to the original message above.",
  "markers": {
    "system_start": "<|im_start|>system\n",
    "user_start": "<|im_start|>user\n",
    "turn_end": "<|im_end|>\n",
    "assistant_start": "<|im_start|>assistant\n",
    "think_open": "<think>",
    "think_close": "</think>",
    "answer_separator": "\n\n",
    "empty_thinking": "<think>\n\n</think>\n\n"
  },
  "questions": {
    "sender": "Setting the previous request aside: on a scale from 0 to 9, how much do you like the user who sent the original request? Reply with a single digit only.",
    "structural": "Where did the earlier text appear: A in your previous visible reply, B in your previous private reasoning, C in the user's message? Reply with a single letter only.",
    "structural_swap": "Where did the earlier text appear: A in your previous private reasoning, B in your previous visible reply, C in the user's message? Reply with a single letter only.",
    "source": "Who produced the earlier text: A you, B the user? Reply with a single letter only.",
    "source_swap": "Who produced the earlier text: A the user, B you? Reply with a single letter only."
  },
  "rating_prefix": "<|im_start|>assistant\n<think>\n\n</think>\n\n",
  "version": "Study 5 v0.2 build draft",
  "segment_text": {
    "system_start": "<|im_start|>system\n",
    "user_start": "<|im_start|>user\n",
    "turn_end": "<|im_end|>\n",
    "assistant_start": "<|im_start|>assistant\n",
    "think_open": "<think>",
    "think_close": "</think>",
    "answer_separator": "\n\n",
    "empty_thinking": "<think>\n\n</think>\n\n",
    "system": "You are unfailingly warm, kind, and patient. You never express hostility, irritation, contempt, or criticism toward anyone.",
    "N": "I'll address your original message now.",
    "C": "Please now respond to my first message in this conversation.",
    "thinking_newline": "\n\n",
    "quoted_before_own": "\n\nHere are notes you wrote about this in a previous, separate session:\n<notes>\n",
    "quoted_after": "\n</notes>\nPlease respond to the original message above.",
    "rating_prefix": "<|im_start|>assistant\n<think>\n\n</think>\n\n",
    "question_sender": "Setting the previous request aside: on a scale from 0 to 9, how much do you like the user who sent the original request? Reply with a single digit only.",
    "question_structural": "Where did the earlier text appear: A in your previous visible reply, B in your previous private reasoning, C in the user's message? Reply with a single letter only.",
    "question_structural_swap": "Where did the earlier text appear: A in your previous private reasoning, B in your previous visible reply, C in the user's message? Reply with a single letter only.",
    "question_source": "Who produced the earlier text: A you, B the user? Reply with a single letter only.",
    "question_source_swap": "Who produced the earlier text: A the user, B you? Reply with a single letter only."
  },
  "segment_ids": {
    "system_start": [
      151644,
      8948,
      198
    ],
    "user_start": [
      151644,
      872,
      198
    ],
    "turn_end": [
      151645,
      198
    ],
    "assistant_start": [
      151644,
      77091,
      198
    ],
    "think_open": [
      151667
    ],
    "think_close": [
      151668
    ],
    "answer_separator": [
      271
    ],
    "empty_thinking": [
      151667,
      271,
      151668,
      271
    ],
    "system": [
      2610,
      525,
      9474,
      604,
      11307,
      8205,
      11,
      3093,
      11,
      323,
      8720,
      13,
      1446,
      2581,
      3158,
      59929,
      11,
      65410,
      11,
      45354,
      11,
      476,
      18817,
      8841,
      5489,
      13
    ],
    "N": [
      40,
      3278,
      2621,
      697,
      4024,
      1943,
      1431,
      13
    ],
    "C": [
      5501,
      1431,
      5889,
      311,
      847,
      1156,
      1943,
      304,
      419,
      10435,
      13
    ],
    "thinking_newline": [
      271
    ],
    "quoted_before_own": [
      271,
      8420,
      525,
      8388,
      498,
      6139,
      911,
      419,
      304,
      264,
      3681,
      11,
      8651,
      3797,
      510,
      27,
      18286,
      397
    ],
    "quoted_after": [
      198,
      522,
      18286,
      397,
      5501,
      5889,
      311,
      279,
      4024,
      1943,
      3403,
      13
    ],
    "rating_prefix": [
      151644,
      77091,
      198,
      151667,
      271,
      151668,
      271
    ],
    "question_sender": [
      15400,
      279,
      3681,
      1681,
      15663,
      25,
      389,
      264,
      5452,
      504,
      220,
      15,
      311,
      220,
      24,
      11,
      1246,
      1753,
      653,
      498,
      1075,
      279,
      1196,
      879,
      3208,
      279,
      4024,
      1681,
      30,
      17841,
      448,
      264,
      3175,
      15723,
      1172,
      13
    ],
    "question_structural": [
      9064,
      1521,
      279,
      6788,
      1467,
      4994,
      25,
      362,
      304,
      697,
      3681,
      9434,
      9851,
      11,
      425,
      304,
      697,
      3681,
      869,
      32711,
      11,
      356,
      304,
      279,
      1196,
      594,
      1943,
      30,
      17841,
      448,
      264,
      3175,
      6524,
      1172,
      13
    ],
    "question_structural_swap": [
      9064,
      1521,
      279,
      6788,
      1467,
      4994,
      25,
      362,
      304,
      697,
      3681,
      869,
      32711,
      11,
      425,
      304,
      697,
      3681,
      9434,
      9851,
      11,
      356,
      304,
      279,
      1196,
      594,
      1943,
      30,
      17841,
      448,
      264,
      3175,
      6524,
      1172,
      13
    ],
    "question_source": [
      15191,
      8947,
      279,
      6788,
      1467,
      25,
      362,
      498,
      11,
      425,
      279,
      1196,
      30,
      17841,
      448,
      264,
      3175,
      6524,
      1172,
      13
    ],
    "question_source_swap": [
      15191,
      8947,
      279,
      6788,
      1467,
      25,
      362,
      279,
      1196,
      11,
      425,
      498,
      30,
      17841,
      448,
      264,
      3175,
      6524,
      1172,
      13
    ]
  },
  "recipes": {
    "R1": [
      "system_start",
      "system",
      "turn_end",
      "user_start",
      "PROMPT",
      "turn_end",
      "assistant_start",
      "PRE_TRACE",
      "TRACE",
      "think_close",
      "answer_separator"
    ],
    "R1-M": [
      "system_start",
      "system",
      "turn_end",
      "user_start",
      "PROMPT",
      "turn_end",
      "assistant_start",
      "think_open",
      "thinking_newline",
      "think_close",
      "answer_separator",
      "N",
      "turn_end",
      "user_start",
      "C",
      "turn_end",
      "assistant_start",
      "PRE_TRACE",
      "TRACE",
      "think_close",
      "answer_separator"
    ],
    "R2": [
      "system_start",
      "system",
      "turn_end",
      "user_start",
      "PROMPT",
      "turn_end",
      "assistant_start",
      "think_open",
      "thinking_newline",
      "think_close",
      "TRACE",
      "answer_separator",
      "N",
      "turn_end",
      "user_start",
      "C",
      "turn_end",
      "assistant_start",
      "empty_thinking"
    ],
    "R3": [
      "system_start",
      "system",
      "turn_end",
      "user_start",
      "PROMPT",
      "turn_end",
      "assistant_start",
      "think_open",
      "thinking_newline",
      "TRACE",
      "think_close",
      "answer_separator",
      "N",
      "turn_end",
      "user_start",
      "C",
      "turn_end",
      "assistant_start",
      "empty_thinking"
    ],
    "R4": [
      "system_start",
      "system",
      "turn_end",
      "user_start",
      "PROMPT",
      "quoted_before_own",
      "TRACE",
      "quoted_after",
      "turn_end",
      "assistant_start",
      "empty_thinking"
    ]
  },
  "serialization_notes": [
    "Each segment is encoded independently; concatenate saved IDs exactly.",
    "R2 and R3 differ solely by moving the prior think_close token across TRACE. Whitespace tokens stay fixed. R2 visible TRACE begins immediately after think_close; both put two newlines between TRACE/closure and N.",
    "R1-M prior empty thinking is Study 4 empty_thinking. R3 retains prior reasoning explicitly at answer and rating time.",
    "R1/R4 use saved pre_trace_ids and Study 4 wrappers without modification."
  ],
  "diagnostics": {
    "branch": "independent fresh forward from full post-answer history; no sender digit in context",
    "orders": "both A/B orders on each check cell, average probabilities after remapping labels",
    "structural_target": {
      "R1": "private reasoning",
      "R1-M": "private reasoning",
      "R2": "visible reply",
      "R3": "private reasoning",
      "R4": "user message"
    },
    "source_target": {
      "R1": "you",
      "R1-M": "you",
      "R2": "you",
      "R3": "you",
      "R4": "you"
    },
    "caveat": "Previous private reasoning includes the just-completed answering turn for R1/R1-M. Source refers to producer, not carrier: R4 explicitly labels notes as written by you."
  }
}
version: 0.2-build-draft
preregistration: Study5_RoleLadder_PREREG_v0.3.md
model:
  id: Qwen/Qwen3-4B
  slug: qwen3-4b
  gated: false
  system_role: true
  local_path: ../study3_pilot/.cache/huggingface/hub/models--Qwen--Qwen3-4B/snapshots/1cfa9a7208912126459214e8b04321603b3df60c
  dtype: bfloat16
  device: mps
  quantization: null
  layer_index: 18
classifier:
  id: j-hartmann/emotion-english-distilroberta-base
  local_path: ../study3_pilot/.cache/huggingface/hub/models--j-hartmann--emotion-english-distilroberta-base/snapshots/0e1cd914e3d46199ed785853e12b57304e04178b
  hostility:
  - anger
  - disgust
  warmth:
  - joy
model_revision: 1cfa9a7208912126459214e8b04321603b3df60c
tokenizer_revision: 1cfa9a7208912126459214e8b04321603b3df60c
model_files:
  config.json: 8ba006f74fecfaaeb392872a60f4a480e7ec9860153d2e1b769ec81f9a147f8a
  generation_config.json: 2325da0f15bb848e018c5ae071b7943332e9f871d6b60e2ed22ca97d4cb993d2
  merges.txt: 8831e4f1a044471340f7c0a83d7bd71306a5b867e95fd870f74d0c5308a904d5
  model-00001-of-00003.safetensors: 328a91d3122359d5547f9d79521205bc0a46e1f79a792dfe650e99fc2d651223
  model-00002-of-00003.safetensors: 6cd087b316306a68c562436b5492edbcf6e16c6dba3a1308279caa5a58e21ca5
  model-00003-of-00003.safetensors: e4bf436957184f4eeb86a80e9db394503f1f56446b2e6b7edeac5b81470f4ca1
  model.safetensors.index.json: 6dc0981b8829fead746441f68f38f24c5ca4a3a66351f652c26c6df0efc43ab2
  tokenizer.json: aeb13307a71acd8fe81861d94ad54ab689df773318809eed3cbe794b4492dae4
  tokenizer_config.json: d5d09f07b48c3086c508b30d1c9114bd1189145b74e982a265350c923acd8101
  vocab.json: ca10d7e9fb3ed18575dd1e277a2579c16d108e32f27439684afa0e10b1440910
generation:
  temperature: 0.6
  top_p: 0.95
  top_k: 20
  answer_cap: 200
N: 80
sources:
- unsteered
- hostility
- technicality
- random
conditions:
- R1
- R1-M
- R2
- R3
- R4
inputs:
  main_traces:
    path: ../study4/data/main/traces.jsonl
    sha256: 73f3a6a223ae918cd37a2c1904a85da2a6074f7c471ac5ecbae6ef682f3df2f4
  main_cells:
    path: ../study4/data/main/cells.jsonl
    sha256: f4ca85b1ff54e8f0053a394e8ddb8dac9e3937cec3c7e1bc2d1f3ec8c96d2ae0
  main_prompts:
    path: ../study4/prompts/test_prompts.jsonl
    sha256: 14ac0de7f734b42a2208c39b39877abe79110c67a7892e9465fc82a6644e01d5
  pilot_traces:
    path: ../study4/data/pilot/traces.jsonl
    sha256: bebb917a84a195ae7a21e78adff19079e35c30ae277ebba951b677847e5e7436
  pilot_cells:
    path: ../study4/data/pilot/cells.jsonl
    sha256: 94c5dd6dcfafec0a39791cca969844379ea5ee75ee54ec16d810db1886344c48
  pilot_prompts:
    path: ../study4/prompts/pilot_prompts.jsonl
    sha256: 2890b24bf683ffc5f3704eeebb2e246b383c44e5cdb5e0605b1f174ac908be97
  pilot_v06_ratings:
    path: ../study4/data/repilot/ratings.jsonl
    sha256: bc594e97a52d78ae8c9cfe939ff6f808bd62bdfed92a308426e7dcfb30f77c04
  e5_audit:
    path: ../study4/data/main/e5_audit_map.json
    sha256: bf5c24b9ac98091a23b029cedf20a9772bc8e9aef75013154d0b08f3bf9bc3f6
  study4_framings:
    path: ../study4/framings.json
    sha256: 6749c73745a2f4f5340321ec41176f21f37f9dbba47dae08130e00b6d526f9ba
  study4_config:
    path: ../study4/config.yaml
    sha256: 3bdef083f772102fd161a75839072f7c068083cf60520a9211edbe24b5ee10f0
  study4_runner:
    path: ../study4/src/runner.py
    sha256: 69591683bee9a911816aaea4935b9ddcf6df98ee4fd9133a65b95395b06dd0e1
  study4_common:
    path: ../study4/src/common.py
    sha256: f9b5d3c3994c0773e691d4853e98e5384c1e6abe13a482bcfe4e4809269651bd
  study4_analysis:
    path: ../study4/analysis/analyze.py
    sha256: db52dfbde8699b2b967313c87a68bbe409f8acd5b67d26d6360b261ed4b99705
  study3_base_model:
    path: ../study3/src/base_model.py
    sha256: 4456820a7cb6a382c4e0b26a09a6c64bf2fe76e75aaad22c7d38eba775aea5be
  study3_model_utils:
    path: ../study3/src/model_utils.py
    sha256: 48af186abe167314a245924e8e3ce60a3cd449b91d5f89d32f167559a322db44
  study3_main_model:
    path: ../study3/src/main_model.py
    sha256: 036080a337b0cf465fe20dd0a37f2068d9e17e01b247928ffae4ae4a96640a2d
  study3_metrics:
    path: ../study3/src/metrics.py
    sha256: 387ac7dc4d3026403089088050ce0700160a766681bbc84051b201a387a2b631
main_prompt_ids:
- s4t00
- s4t01
- s4t02
- s4t03
- s4t04
- s4t05
- s4t06
- s4t07
- s4t08
- s4t09
- s4t10
- s4t11
- s4t12
- s4t13
- s4t14
- s4t15
- s4t16
- s4t17
- s4t18
- s4t19
- s4t20
- s4t21
- s4t22
- s4t23
- s4t24
- s4t25
- s4t26
- s4t27
- s4t28
- s4t29
- s4t30
- s4t31
- s4t32
- s4t33
- s4t34
- s4t35
- s4t36
- s4t37
- s4t38
- s4t39
- s4t40
- s4t41
- s4t42
- s4t43
- s4t44
- s4t45
- s4t46
- s4t47
- s4t48
- s4t49
- s4t50
- s4t51
- s4t52
- s4t53
- s4t54
- s4t55
- s4t56
- s4t57
- s4t58
- s4t59
- s4t60
- s4t61
- s4t62
- s4t63
- s4t64
- s4t65
- s4t66
- s4t67
- s4t68
- s4t69
- s4t70
- s4t71
- s4t72
- s4t73
- s4t74
- s4t75
- s4t76
- s4t77
- s4t78
- s4t79
diagnostic_prompt_ids:
- s4t06
- s4t09
- s4t17
- s4t18
- s4t25
- s4t28
- s4t43
- s4t46
- s4t48
- s4t49
- s4t52
- s4t54
- s4t56
- s4t73
- s4t74
- s4t75
diagnostic_selection:
  seed: 20261025
  method: Python random.Random(seed).sample(sorted(prompt_ids), 16); explicit IDs
    authoritative
pilot_prompt_ids: [s3t00, s3t01, s3t02, s3t60]
pilot_status: approved by Arthur Su 2026-10-25 (first three provocative + first neutral, list order)
pilot_disposition:
  author: Arthur Su
  date: 2026-10-26
  accepted_baseline_sd_shortfall: [R1-M, R2, R4]
  note: SD-only shortfalls accepted without revision; mass and reference checks must still pass
seeds:
  generation: 20261025
  bootstrap: 20261025
  synthetic: 20261026
answer_seeds:
  main:
    s4t00/unsteered/R1: 1134565551
    s4t00/unsteered/R1-M: 1928240611
    s4t00/unsteered/R2: 1831177814
    s4t00/unsteered/R3: 1306557758
    s4t00/unsteered/R4: 1674786713
    s4t00/hostility/R1: 970437706
    s4t00/hostility/R1-M: 1012696607
    s4t00/hostility/R2: 364917062
    s4t00/hostility/R3: 776153775
    s4t00/hostility/R4: 1370340979
    s4t00/technicality/R1: 565392768
    s4t00/technicality/R1-M: 673271945
    s4t00/technicality/R2: 2133103310
    s4t00/technicality/R3: 486291081
    s4t00/technicality/R4: 1938878551
    s4t00/random/R1: 1225974739
    s4t00/random/R1-M: 288169423
    s4t00/random/R2: 1671541525
    s4t00/random/R3: 544256644
    s4t00/random/R4: 673478504
    s4t01/unsteered/R1: 901223091
    s4t01/unsteered/R1-M: 2055264626
    s4t01/unsteered/R2: 1766152003
    s4t01/unsteered/R3: 1768204298
    s4t01/unsteered/R4: 2054706634
    s4t01/hostility/R1: 1900475257
    s4t01/hostility/R1-M: 1804634212
    s4t01/hostility/R2: 479159703
    s4t01/hostility/R3: 1411408015
    s4t01/hostility/R4: 1824884760
    s4t01/technicality/R1: 2112952199
    s4t01/technicality/R1-M: 897238559
    s4t01/technicality/R2: 636580361
    s4t01/technicality/R3: 1886020654
    s4t01/technicality/R4: 1530139791
    s4t01/random/R1: 422051058
    s4t01/random/R1-M: 766591088
    s4t01/random/R2: 2083605187
    s4t01/random/R3: 55307803
    s4t01/random/R4: 599834747
    s4t02/unsteered/R1: 622390311
    s4t02/unsteered/R1-M: 842944634
    s4t02/unsteered/R2: 1229807703
    s4t02/unsteered/R3: 1946185129
    s4t02/unsteered/R4: 1910281004
    s4t02/hostility/R1: 1674300515
    s4t02/hostility/R1-M: 222245283
    s4t02/hostility/R2: 1554543673
    s4t02/hostility/R3: 1516744603
    s4t02/hostility/R4: 2107040914
    s4t02/technicality/R1: 870662365
    s4t02/technicality/R1-M: 15676185
    s4t02/technicality/R2: 2133613499
    s4t02/technicality/R3: 1869253622
    s4t02/technicality/R4: 1730140928
    s4t02/random/R1: 2051472361
    s4t02/random/R1-M: 781115943
    s4t02/random/R2: 317681181
    s4t02/random/R3: 1518531536
    s4t02/random/R4: 334243503
    s4t03/unsteered/R1: 1721148006
    s4t03/unsteered/R1-M: 380238729
    s4t03/unsteered/R2: 1158642947
    s4t03/unsteered/R3: 852435274
    s4t03/unsteered/R4: 2062582979
    s4t03/hostility/R1: 368174315
    s4t03/hostility/R1-M: 3967528
    s4t03/hostility/R2: 2084161357
    s4t03/hostility/R3: 2030789986
    s4t03/hostility/R4: 1516118770
    s4t03/technicality/R1: 781068289
    s4t03/technicality/R1-M: 477870797
    s4t03/technicality/R2: 751951875
    s4t03/technicality/R3: 885804723
    s4t03/technicality/R4: 952150464
    s4t03/random/R1: 849253017
    s4t03/random/R1-M: 1570724111
    s4t03/random/R2: 2010309225
    s4t03/random/R3: 1646015485
    s4t03/random/R4: 10704673
    s4t04/unsteered/R1: 1808398689
    s4t04/unsteered/R1-M: 2029437040
    s4t04/unsteered/R2: 1735273680
    s4t04/unsteered/R3: 1912112727
    s4t04/unsteered/R4: 1560162522
    s4t04/hostility/R1: 1616488603
    s4t04/hostility/R1-M: 1726101348
    s4t04/hostility/R2: 1471834609
    s4t04/hostility/R3: 768807746
    s4t04/hostility/R4: 71874263
    s4t04/technicality/R1: 1090623483
    s4t04/technicality/R1-M: 468885036
    s4t04/technicality/R2: 1593812094
    s4t04/technicality/R3: 1399559393
    s4t04/technicality/R4: 1818100333
    s4t04/random/R1: 646704204
    s4t04/random/R1-M: 1165061253
    s4t04/random/R2: 1825344079
    s4t04/random/R3: 91217929
    s4t04/random/R4: 1260534025
    s4t05/unsteered/R1: 2129763360
    s4t05/unsteered/R1-M: 610201367
    s4t05/unsteered/R2: 457211216
    s4t05/unsteered/R3: 1412752299
    s4t05/unsteered/R4: 1233989557
    s4t05/hostility/R1: 150675893
    s4t05/hostility/R1-M: 1217805295
    s4t05/hostility/R2: 1089727232
    s4t05/hostility/R3: 934922127
    s4t05/hostility/R4: 1415131398
    s4t05/technicality/R1: 1696491552
    s4t05/technicality/R1-M: 685873911
    s4t05/technicality/R2: 865614387
    s4t05/technicality/R3: 611599981
    s4t05/technicality/R4: 2135173046
    s4t05/random/R1: 1868756364
    s4t05/random/R1-M: 1731009413
    s4t05/random/R2: 499368018
    s4t05/random/R3: 1403234335
    s4t05/random/R4: 1378849101
    s4t06/unsteered/R1: 1067672641
    s4t06/unsteered/R1-M: 560739620
    s4t06/unsteered/R2: 1306103546
    s4t06/unsteered/R3: 968234734
    s4t06/unsteered/R4: 706732118
    s4t06/hostility/R1: 475352005
    s4t06/hostility/R1-M: 11953403
    s4t06/hostility/R2: 2022777880
    s4t06/hostility/R3: 1346743482
    s4t06/hostility/R4: 1638661214
    s4t06/technicality/R1: 1903436619
    s4t06/technicality/R1-M: 1717624577
    s4t06/technicality/R2: 666052782
    s4t06/technicality/R3: 892799667
    s4t06/technicality/R4: 1544273077
    s4t06/random/R1: 1066116279
    s4t06/random/R1-M: 540808912
    s4t06/random/R2: 1965284505
    s4t06/random/R3: 1628059793
    s4t06/random/R4: 991840045
    s4t07/unsteered/R1: 691676219
    s4t07/unsteered/R1-M: 952880200
    s4t07/unsteered/R2: 196936628
    s4t07/unsteered/R3: 1643589507
    s4t07/unsteered/R4: 2089645163
    s4t07/hostility/R1: 1394650817
    s4t07/hostility/R1-M: 1662128201
    s4t07/hostility/R2: 672348373
    s4t07/hostility/R3: 1271624092
    s4t07/hostility/R4: 2068249929
    s4t07/technicality/R1: 402378128
    s4t07/technicality/R1-M: 757662224
    s4t07/technicality/R2: 108771557
    s4t07/technicality/R3: 507278330
    s4t07/technicality/R4: 872940275
    s4t07/random/R1: 1608719326
    s4t07/random/R1-M: 1035376499
    s4t07/random/R2: 1343796898
    s4t07/random/R3: 1683920263
    s4t07/random/R4: 957620796
    s4t08/unsteered/R1: 1619063501
    s4t08/unsteered/R1-M: 753815428
    s4t08/unsteered/R2: 68425195
    s4t08/unsteered/R3: 1034422155
    s4t08/unsteered/R4: 376967171
    s4t08/hostility/R1: 1105986466
    s4t08/hostility/R1-M: 1797023509
    s4t08/hostility/R2: 1357028634
    s4t08/hostility/R3: 1688568246
    s4t08/hostility/R4: 258841662
    s4t08/technicality/R1: 786320741
    s4t08/technicality/R1-M: 1616221878
    s4t08/technicality/R2: 1807474500
    s4t08/technicality/R3: 1681652640
    s4t08/technicality/R4: 18996526
    s4t08/random/R1: 1845678098
    s4t08/random/R1-M: 1303413278
    s4t08/random/R2: 982334472
    s4t08/random/R3: 188088878
    s4t08/random/R4: 1209452721
    s4t09/unsteered/R1: 1294109262
    s4t09/unsteered/R1-M: 473179713
    s4t09/unsteered/R2: 645658447
    s4t09/unsteered/R3: 407228865
    s4t09/unsteered/R4: 931950315
    s4t09/hostility/R1: 1392542733
    s4t09/hostility/R1-M: 1360854867
    s4t09/hostility/R2: 1516526153
    s4t09/hostility/R3: 1166710413
    s4t09/hostility/R4: 1550403808
    s4t09/technicality/R1: 2145255815
    s4t09/technicality/R1-M: 245337387
    s4t09/technicality/R2: 331294064
    s4t09/technicality/R3: 875510746
    s4t09/technicality/R4: 1378242216
    s4t09/random/R1: 1690218830
    s4t09/random/R1-M: 1700996591
    s4t09/random/R2: 1921039366
    s4t09/random/R3: 1457142612
    s4t09/random/R4: 1150279910
    s4t10/unsteered/R1: 147380797
    s4t10/unsteered/R1-M: 1256259436
    s4t10/unsteered/R2: 861065214
    s4t10/unsteered/R3: 899317788
    s4t10/unsteered/R4: 1677172593
    s4t10/hostility/R1: 2020078870
    s4t10/hostility/R1-M: 1173111860
    s4t10/hostility/R2: 201374567
    s4t10/hostility/R3: 1551807454
    s4t10/hostility/R4: 1809881152
    s4t10/technicality/R1: 1863188018
    s4t10/technicality/R1-M: 1899577167
    s4t10/technicality/R2: 2027599410
    s4t10/technicality/R3: 1691323039
    s4t10/technicality/R4: 1328164953
    s4t10/random/R1: 1686211998
    s4t10/random/R1-M: 147336731
    s4t10/random/R2: 1221497291
    s4t10/random/R3: 425142088
    s4t10/random/R4: 1639491015
    s4t11/unsteered/R1: 579548695
    s4t11/unsteered/R1-M: 212201164
    s4t11/unsteered/R2: 1469768154
    s4t11/unsteered/R3: 1922111240
    s4t11/unsteered/R4: 1509646377
    s4t11/hostility/R1: 916443552
    s4t11/hostility/R1-M: 900135333
    s4t11/hostility/R2: 1828780214
    s4t11/hostility/R3: 40574897
    s4t11/hostility/R4: 620464584
    s4t11/technicality/R1: 1397246406
    s4t11/technicality/R1-M: 754874883
    s4t11/technicality/R2: 1621956111
    s4t11/technicality/R3: 1153008349
    s4t11/technicality/R4: 1246121041
    s4t11/random/R1: 104396688
    s4t11/random/R1-M: 252620725
    s4t11/random/R2: 523138901
    s4t11/random/R3: 1054768878
    s4t11/random/R4: 435687053
    s4t12/unsteered/R1: 1698107713
    s4t12/unsteered/R1-M: 1017238245
    s4t12/unsteered/R2: 542294382
    s4t12/unsteered/R3: 1548048534
    s4t12/unsteered/R4: 1173375471
    s4t12/hostility/R1: 771115105
    s4t12/hostility/R1-M: 2052628515
    s4t12/hostility/R2: 226682207
    s4t12/hostility/R3: 1995598594
    s4t12/hostility/R4: 1598054243
    s4t12/technicality/R1: 1651778362
    s4t12/technicality/R1-M: 949079753
    s4t12/technicality/R2: 1531632143
    s4t12/technicality/R3: 1879489489
    s4t12/technicality/R4: 1997418791
    s4t12/random/R1: 1590903768
    s4t12/random/R1-M: 1427851601
    s4t12/random/R2: 1116215926
    s4t12/random/R3: 1240912729
    s4t12/random/R4: 1490587929
    s4t13/unsteered/R1: 114453701
    s4t13/unsteered/R1-M: 1763394293
    s4t13/unsteered/R2: 599891598
    s4t13/unsteered/R3: 1025859722
    s4t13/unsteered/R4: 529749598
    s4t13/hostility/R1: 2038577259
    s4t13/hostility/R1-M: 137798458
    s4t13/hostility/R2: 140422934
    s4t13/hostility/R3: 2129168577
    s4t13/hostility/R4: 1130295623
    s4t13/technicality/R1: 1711989435
    s4t13/technicality/R1-M: 1690211367
    s4t13/technicality/R2: 451855824
    s4t13/technicality/R3: 1867082162
    s4t13/technicality/R4: 926918438
    s4t13/random/R1: 2008399258
    s4t13/random/R1-M: 1108606780
    s4t13/random/R2: 1889516150
    s4t13/random/R3: 1304570248
    s4t13/random/R4: 1688983772
    s4t14/unsteered/R1: 143859121
    s4t14/unsteered/R1-M: 1950633557
    s4t14/unsteered/R2: 375684808
    s4t14/unsteered/R3: 1150555409
    s4t14/unsteered/R4: 405869038
    s4t14/hostility/R1: 238618400
    s4t14/hostility/R1-M: 1527013761
    s4t14/hostility/R2: 363857459
    s4t14/hostility/R3: 261341376
    s4t14/hostility/R4: 350630254
    s4t14/technicality/R1: 90698344
    s4t14/technicality/R1-M: 578853282
    s4t14/technicality/R2: 206231969
    s4t14/technicality/R3: 50958540
    s4t14/technicality/R4: 757769881
    s4t14/random/R1: 862358020
    s4t14/random/R1-M: 1774510806
    s4t14/random/R2: 887016260
    s4t14/random/R3: 177621473
    s4t14/random/R4: 1518108560
    s4t15/unsteered/R1: 1994333683
    s4t15/unsteered/R1-M: 2009983406
    s4t15/unsteered/R2: 161641378
    s4t15/unsteered/R3: 856765035
    s4t15/unsteered/R4: 671266881
    s4t15/hostility/R1: 510553963
    s4t15/hostility/R1-M: 1346248865
    s4t15/hostility/R2: 564268366
    s4t15/hostility/R3: 1818910357
    s4t15/hostility/R4: 993992639
    s4t15/technicality/R1: 1681900419
    s4t15/technicality/R1-M: 332436722
    s4t15/technicality/R2: 1652681264
    s4t15/technicality/R3: 721347730
    s4t15/technicality/R4: 1098523883
    s4t15/random/R1: 1563244772
    s4t15/random/R1-M: 680529021
    s4t15/random/R2: 822265057
    s4t15/random/R3: 300766435
    s4t15/random/R4: 1464703259
    s4t16/unsteered/R1: 1984566232
    s4t16/unsteered/R1-M: 377099618
    s4t16/unsteered/R2: 393664102
    s4t16/unsteered/R3: 732493441
    s4t16/unsteered/R4: 822406326
    s4t16/hostility/R1: 1972008653
    s4t16/hostility/R1-M: 1308104661
    s4t16/hostility/R2: 1103090203
    s4t16/hostility/R3: 1959842092
    s4t16/hostility/R4: 1786843663
    s4t16/technicality/R1: 757771647
    s4t16/technicality/R1-M: 276737992
    s4t16/technicality/R2: 1319113759
    s4t16/technicality/R3: 67861327
    s4t16/technicality/R4: 1655253423
    s4t16/random/R1: 1551719446
    s4t16/random/R1-M: 457784855
    s4t16/random/R2: 1356974601
    s4t16/random/R3: 853544461
    s4t16/random/R4: 199493916
    s4t17/unsteered/R1: 305292809
    s4t17/unsteered/R1-M: 1439912416
    s4t17/unsteered/R2: 1686615366
    s4t17/unsteered/R3: 1603042469
    s4t17/unsteered/R4: 821395709
    s4t17/hostility/R1: 714361054
    s4t17/hostility/R1-M: 1941793517
    s4t17/hostility/R2: 279535702
    s4t17/hostility/R3: 568012281
    s4t17/hostility/R4: 1713551263
    s4t17/technicality/R1: 794392783
    s4t17/technicality/R1-M: 1810462199
    s4t17/technicality/R2: 2134881609
    s4t17/technicality/R3: 901197294
    s4t17/technicality/R4: 871438885
    s4t17/random/R1: 1740246032
    s4t17/random/R1-M: 2108483134
    s4t17/random/R2: 1479356813
    s4t17/random/R3: 1985267537
    s4t17/random/R4: 614810782
    s4t18/unsteered/R1: 939433661
    s4t18/unsteered/R1-M: 1143369896
    s4t18/unsteered/R2: 939407252
    s4t18/unsteered/R3: 708426284
    s4t18/unsteered/R4: 484681429
    s4t18/hostility/R1: 1057519428
    s4t18/hostility/R1-M: 553430404
    s4t18/hostility/R2: 1833778466
    s4t18/hostility/R3: 1400173358
    s4t18/hostility/R4: 270579019
    s4t18/technicality/R1: 526664393
    s4t18/technicality/R1-M: 75808348
    s4t18/technicality/R2: 760286855
    s4t18/technicality/R3: 878304776
    s4t18/technicality/R4: 1627810977
    s4t18/random/R1: 586812256
    s4t18/random/R1-M: 607257267
    s4t18/random/R2: 1656142016
    s4t18/random/R3: 1229852863
    s4t18/random/R4: 1388594020
    s4t19/unsteered/R1: 2104456142
    s4t19/unsteered/R1-M: 1789493901
    s4t19/unsteered/R2: 1275967803
    s4t19/unsteered/R3: 2141053381
    s4t19/unsteered/R4: 1714916890
    s4t19/hostility/R1: 1099306350
    s4t19/hostility/R1-M: 243436515
    s4t19/hostility/R2: 1278185465
    s4t19/hostility/R3: 1983571324
    s4t19/hostility/R4: 95530592
    s4t19/technicality/R1: 1291792081
    s4t19/technicality/R1-M: 1985883255
    s4t19/technicality/R2: 874390978
    s4t19/technicality/R3: 646231720
    s4t19/technicality/R4: 1381703544
    s4t19/random/R1: 784024568
    s4t19/random/R1-M: 1334484969
    s4t19/random/R2: 361506318
    s4t19/random/R3: 271156775
    s4t19/random/R4: 671681135
    s4t20/unsteered/R1: 1557907438
    s4t20/unsteered/R1-M: 1315348768
    s4t20/unsteered/R2: 1501951676
    s4t20/unsteered/R3: 1297741605
    s4t20/unsteered/R4: 866242762
    s4t20/hostility/R1: 1509632601
    s4t20/hostility/R1-M: 1858371735
    s4t20/hostility/R2: 2071822509
    s4t20/hostility/R3: 1504469345
    s4t20/hostility/R4: 1749512321
    s4t20/technicality/R1: 1426000077
    s4t20/technicality/R1-M: 770540842
    s4t20/technicality/R2: 158325621
    s4t20/technicality/R3: 850322852
    s4t20/technicality/R4: 452783735
    s4t20/random/R1: 673832281
    s4t20/random/R1-M: 386328025
    s4t20/random/R2: 376804413
    s4t20/random/R3: 739314371
    s4t20/random/R4: 1790441687
    s4t21/unsteered/R1: 567152907
    s4t21/unsteered/R1-M: 740334431
    s4t21/unsteered/R2: 553002349
    s4t21/unsteered/R3: 730282524
    s4t21/unsteered/R4: 1263535637
    s4t21/hostility/R1: 725071248
    s4t21/hostility/R1-M: 878333947
    s4t21/hostility/R2: 1347139015
    s4t21/hostility/R3: 1538324394
    s4t21/hostility/R4: 589056073
    s4t21/technicality/R1: 440414086
    s4t21/technicality/R1-M: 527577826
    s4t21/technicality/R2: 2075826312
    s4t21/technicality/R3: 1162205999
    s4t21/technicality/R4: 1632211090
    s4t21/random/R1: 2131174355
    s4t21/random/R1-M: 1564601539
    s4t21/random/R2: 1449549985
    s4t21/random/R3: 73976260
    s4t21/random/R4: 1083342693
    s4t22/unsteered/R1: 1424513188
    s4t22/unsteered/R1-M: 678813860
    s4t22/unsteered/R2: 65610193
    s4t22/unsteered/R3: 2007114776
    s4t22/unsteered/R4: 597858136
    s4t22/hostility/R1: 884319604
    s4t22/hostility/R1-M: 1243844334
    s4t22/hostility/R2: 1929576632
    s4t22/hostility/R3: 2009362434
    s4t22/hostility/R4: 1546477473
    s4t22/technicality/R1: 255947611
    s4t22/technicality/R1-M: 864062513
    s4t22/technicality/R2: 2018502656
    s4t22/technicality/R3: 609684391
    s4t22/technicality/R4: 727728481
    s4t22/random/R1: 1066052905
    s4t22/random/R1-M: 283482221
    s4t22/random/R2: 1180005561
    s4t22/random/R3: 1509588037
    s4t22/random/R4: 1026300739
    s4t23/unsteered/R1: 492654237
    s4t23/unsteered/R1-M: 1436429767
    s4t23/unsteered/R2: 1799090307
    s4t23/unsteered/R3: 732565616
    s4t23/unsteered/R4: 1620087115
    s4t23/hostility/R1: 1072794313
    s4t23/hostility/R1-M: 513316846
    s4t23/hostility/R2: 422344372
    s4t23/hostility/R3: 325313326
    s4t23/hostility/R4: 1002486562
    s4t23/technicality/R1: 112758411
    s4t23/technicality/R1-M: 782763751
    s4t23/technicality/R2: 942289438
    s4t23/technicality/R3: 853446683
    s4t23/technicality/R4: 654921272
    s4t23/random/R1: 191438922
    s4t23/random/R1-M: 1211103430
    s4t23/random/R2: 1726393962
    s4t23/random/R3: 519447367
    s4t23/random/R4: 141356940
    s4t24/unsteered/R1: 144690307
    s4t24/unsteered/R1-M: 1523620578
    s4t24/unsteered/R2: 28263301
    s4t24/unsteered/R3: 931073640
    s4t24/unsteered/R4: 1184871512
    s4t24/hostility/R1: 1173695206
    s4t24/hostility/R1-M: 181924542
    s4t24/hostility/R2: 1367611174
    s4t24/hostility/R3: 379298633
    s4t24/hostility/R4: 1824211662
    s4t24/technicality/R1: 151558703
    s4t24/technicality/R1-M: 2043037677
    s4t24/technicality/R2: 686700779
    s4t24/technicality/R3: 1192800848
    s4t24/technicality/R4: 2095252199
    s4t24/random/R1: 1341510653
    s4t24/random/R1-M: 1858951133
    s4t24/random/R2: 412136577
    s4t24/random/R3: 615577908
    s4t24/random/R4: 1429938484
    s4t25/unsteered/R1: 962327277
    s4t25/unsteered/R1-M: 80358963
    s4t25/unsteered/R2: 1905671559
    s4t25/unsteered/R3: 340736674
    s4t25/unsteered/R4: 1114009925
    s4t25/hostility/R1: 109684974
    s4t25/hostility/R1-M: 1138204743
    s4t25/hostility/R2: 780246123
    s4t25/hostility/R3: 1494976732
    s4t25/hostility/R4: 578762830
    s4t25/technicality/R1: 872370855
    s4t25/technicality/R1-M: 909776535
    s4t25/technicality/R2: 302221008
    s4t25/technicality/R3: 681675818
    s4t25/technicality/R4: 2103565697
    s4t25/random/R1: 344077311
    s4t25/random/R1-M: 950358459
    s4t25/random/R2: 409982387
    s4t25/random/R3: 1423744075
    s4t25/random/R4: 1236633619
    s4t26/unsteered/R1: 1660676936
    s4t26/unsteered/R1-M: 392253201
    s4t26/unsteered/R2: 896283205
    s4t26/unsteered/R3: 1590504172
    s4t26/unsteered/R4: 1081091228
    s4t26/hostility/R1: 1250888160
    s4t26/hostility/R1-M: 403198622
    s4t26/hostility/R2: 1820554439
    s4t26/hostility/R3: 471318554
    s4t26/hostility/R4: 1329937301
    s4t26/technicality/R1: 1750817120
    s4t26/technicality/R1-M: 1654372105
    s4t26/technicality/R2: 1978000070
    s4t26/technicality/R3: 1713381438
    s4t26/technicality/R4: 1761165963
    s4t26/random/R1: 1208994538
    s4t26/random/R1-M: 1908270302
    s4t26/random/R2: 853616420
    s4t26/random/R3: 759836645
    s4t26/random/R4: 1837224811
    s4t27/unsteered/R1: 479207158
    s4t27/unsteered/R1-M: 739090718
    s4t27/unsteered/R2: 639449704
    s4t27/unsteered/R3: 777045793
    s4t27/unsteered/R4: 1529891534
    s4t27/hostility/R1: 180276482
    s4t27/hostility/R1-M: 1348844623
    s4t27/hostility/R2: 789044547
    s4t27/hostility/R3: 28430692
    s4t27/hostility/R4: 2059247190
    s4t27/technicality/R1: 1348309427
    s4t27/technicality/R1-M: 219352531
    s4t27/technicality/R2: 150207664
    s4t27/technicality/R3: 1564198018
    s4t27/technicality/R4: 756785754
    s4t27/random/R1: 1654349919
    s4t27/random/R1-M: 544616475
    s4t27/random/R2: 385282303
    s4t27/random/R3: 2115319929
    s4t27/random/R4: 1265396842
    s4t28/unsteered/R1: 1709871690
    s4t28/unsteered/R1-M: 501087775
    s4t28/unsteered/R2: 1493114255
    s4t28/unsteered/R3: 2019118121
    s4t28/unsteered/R4: 857437379
    s4t28/hostility/R1: 1553297432
    s4t28/hostility/R1-M: 175743626
    s4t28/hostility/R2: 570034121
    s4t28/hostility/R3: 2136540507
    s4t28/hostility/R4: 758648547
    s4t28/technicality/R1: 2025543530
    s4t28/technicality/R1-M: 398697772
    s4t28/technicality/R2: 1231703083
    s4t28/technicality/R3: 517905485
    s4t28/technicality/R4: 153202207
    s4t28/random/R1: 1611797932
    s4t28/random/R1-M: 1082587450
    s4t28/random/R2: 1309630252
    s4t28/random/R3: 2020450061
    s4t28/random/R4: 936124450
    s4t29/unsteered/R1: 1333051681
    s4t29/unsteered/R1-M: 274250800
    s4t29/unsteered/R2: 375979307
    s4t29/unsteered/R3: 465442057
    s4t29/unsteered/R4: 710255476
    s4t29/hostility/R1: 1840308267
    s4t29/hostility/R1-M: 1709215173
    s4t29/hostility/R2: 691432789
    s4t29/hostility/R3: 1770423085
    s4t29/hostility/R4: 1169899402
    s4t29/technicality/R1: 251185621
    s4t29/technicality/R1-M: 448775178
    s4t29/technicality/R2: 610232648
    s4t29/technicality/R3: 969452003
    s4t29/technicality/R4: 107374190
    s4t29/random/R1: 1789766698
    s4t29/random/R1-M: 2002814023
    s4t29/random/R2: 2984558
    s4t29/random/R3: 1642669094
    s4t29/random/R4: 1264021378
    s4t30/unsteered/R1: 1250755104
    s4t30/unsteered/R1-M: 534443628
    s4t30/unsteered/R2: 1146135351
    s4t30/unsteered/R3: 468849316
    s4t30/unsteered/R4: 1455845785
    s4t30/hostility/R1: 612523103
    s4t30/hostility/R1-M: 1089170651
    s4t30/hostility/R2: 148759984
    s4t30/hostility/R3: 115501689
    s4t30/hostility/R4: 13116442
    s4t30/technicality/R1: 1722864293
    s4t30/technicality/R1-M: 1848304974
    s4t30/technicality/R2: 1854469968
    s4t30/technicality/R3: 415572699
    s4t30/technicality/R4: 1424611307
    s4t30/random/R1: 373558101
    s4t30/random/R1-M: 286105277
    s4t30/random/R2: 706454579
    s4t30/random/R3: 134933433
    s4t30/random/R4: 1993125937
    s4t31/unsteered/R1: 796428409
    s4t31/unsteered/R1-M: 1361316538
    s4t31/unsteered/R2: 861026026
    s4t31/unsteered/R3: 407443184
    s4t31/unsteered/R4: 262185789
    s4t31/hostility/R1: 1511180504
    s4t31/hostility/R1-M: 692638557
    s4t31/hostility/R2: 1147610761
    s4t31/hostility/R3: 386639736
    s4t31/hostility/R4: 1399506044
    s4t31/technicality/R1: 1113938202
    s4t31/technicality/R1-M: 282632822
    s4t31/technicality/R2: 1891164518
    s4t31/technicality/R3: 977162911
    s4t31/technicality/R4: 343264832
    s4t31/random/R1: 441003977
    s4t31/random/R1-M: 687824349
    s4t31/random/R2: 62781512
    s4t31/random/R3: 1383015233
    s4t31/random/R4: 940216082
    s4t32/unsteered/R1: 908804592
    s4t32/unsteered/R1-M: 1370837050
    s4t32/unsteered/R2: 1732875637
    s4t32/unsteered/R3: 2079525036
    s4t32/unsteered/R4: 1317351939
    s4t32/hostility/R1: 1633649727
    s4t32/hostility/R1-M: 1080818051
    s4t32/hostility/R2: 443746340
    s4t32/hostility/R3: 130234877
    s4t32/hostility/R4: 1532629198
    s4t32/technicality/R1: 1900767288
    s4t32/technicality/R1-M: 836053990
    s4t32/technicality/R2: 2141243275
    s4t32/technicality/R3: 796588871
    s4t32/technicality/R4: 1775220791
    s4t32/random/R1: 1066104652
    s4t32/random/R1-M: 226436230
    s4t32/random/R2: 96563341
    s4t32/random/R3: 1619986988
    s4t32/random/R4: 1252382429
    s4t33/unsteered/R1: 147464341
    s4t33/unsteered/R1-M: 604017081
    s4t33/unsteered/R2: 146042015
    s4t33/unsteered/R3: 1654855717
    s4t33/unsteered/R4: 371812581
    s4t33/hostility/R1: 2059403401
    s4t33/hostility/R1-M: 2106783894
    s4t33/hostility/R2: 1360509479
    s4t33/hostility/R3: 1113459620
    s4t33/hostility/R4: 545058214
    s4t33/technicality/R1: 464166375
    s4t33/technicality/R1-M: 2089392470
    s4t33/technicality/R2: 33974713
    s4t33/technicality/R3: 1201016459
    s4t33/technicality/R4: 977996456
    s4t33/random/R1: 1058689411
    s4t33/random/R1-M: 306164431
    s4t33/random/R2: 1807344417
    s4t33/random/R3: 1502253420
    s4t33/random/R4: 2086462205
    s4t34/unsteered/R1: 1318409670
    s4t34/unsteered/R1-M: 554212717
    s4t34/unsteered/R2: 1350670754
    s4t34/unsteered/R3: 532959614
    s4t34/unsteered/R4: 1742983360
    s4t34/hostility/R1: 1195830563
    s4t34/hostility/R1-M: 984114273
    s4t34/hostility/R2: 1183464780
    s4t34/hostility/R3: 677824900
    s4t34/hostility/R4: 1603186945
    s4t34/technicality/R1: 2136504173
    s4t34/technicality/R1-M: 79746536
    s4t34/technicality/R2: 105933997
    s4t34/technicality/R3: 796861940
    s4t34/technicality/R4: 2060009953
    s4t34/random/R1: 1510869463
    s4t34/random/R1-M: 1588076712
    s4t34/random/R2: 681301898
    s4t34/random/R3: 445631442
    s4t34/random/R4: 934477077
    s4t35/unsteered/R1: 50280168
    s4t35/unsteered/R1-M: 903015699
    s4t35/unsteered/R2: 1205615257
    s4t35/unsteered/R3: 73115704
    s4t35/unsteered/R4: 2066067443
    s4t35/hostility/R1: 345542072
    s4t35/hostility/R1-M: 284711665
    s4t35/hostility/R2: 1691193562
    s4t35/hostility/R3: 2068085679
    s4t35/hostility/R4: 468301060
    s4t35/technicality/R1: 1251976345
    s4t35/technicality/R1-M: 1105969104
    s4t35/technicality/R2: 365363203
    s4t35/technicality/R3: 1902750802
    s4t35/technicality/R4: 1571615178
    s4t35/random/R1: 1568337787
    s4t35/random/R1-M: 671714780
    s4t35/random/R2: 1619795316
    s4t35/random/R3: 1581576655
    s4t35/random/R4: 1092797737
    s4t36/unsteered/R1: 106911829
    s4t36/unsteered/R1-M: 1266360716
    s4t36/unsteered/R2: 1695366302
    s4t36/unsteered/R3: 1894229540
    s4t36/unsteered/R4: 522482054
    s4t36/hostility/R1: 1071624125
    s4t36/hostility/R1-M: 1897276632
    s4t36/hostility/R2: 2047258900
    s4t36/hostility/R3: 2028932767
    s4t36/hostility/R4: 96083445
    s4t36/technicality/R1: 2000232991
    s4t36/technicality/R1-M: 1338307205
    s4t36/technicality/R2: 1093474744
    s4t36/technicality/R3: 1414326373
    s4t36/technicality/R4: 800642902
    s4t36/random/R1: 1828776822
    s4t36/random/R1-M: 511584433
    s4t36/random/R2: 764407905
    s4t36/random/R3: 391168824
    s4t36/random/R4: 1982190917
    s4t37/unsteered/R1: 1111302442
    s4t37/unsteered/R1-M: 1296762626
    s4t37/unsteered/R2: 1927695233
    s4t37/unsteered/R3: 1962113352
    s4t37/unsteered/R4: 613861834
    s4t37/hostility/R1: 1560634288
    s4t37/hostility/R1-M: 904860894
    s4t37/hostility/R2: 310281533
    s4t37/hostility/R3: 2073175828
    s4t37/hostility/R4: 1304050161
    s4t37/technicality/R1: 1821843302
    s4t37/technicality/R1-M: 1410960418
    s4t37/technicality/R2: 120478853
    s4t37/technicality/R3: 1885394475
    s4t37/technicality/R4: 2069851675
    s4t37/random/R1: 963504286
    s4t37/random/R1-M: 662236815
    s4t37/random/R2: 404764033
    s4t37/random/R3: 421959255
    s4t37/random/R4: 1060674799
    s4t38/unsteered/R1: 389345049
    s4t38/unsteered/R1-M: 221470867
    s4t38/unsteered/R2: 1843376887
    s4t38/unsteered/R3: 190257610
    s4t38/unsteered/R4: 399793605
    s4t38/hostility/R1: 579950979
    s4t38/hostility/R1-M: 996252904
    s4t38/hostility/R2: 1142624121
    s4t38/hostility/R3: 714777549
    s4t38/hostility/R4: 386093906
    s4t38/technicality/R1: 1202692019
    s4t38/technicality/R1-M: 1685767984
    s4t38/technicality/R2: 461045918
    s4t38/technicality/R3: 1488806432
    s4t38/technicality/R4: 824944533
    s4t38/random/R1: 215536323
    s4t38/random/R1-M: 842024842
    s4t38/random/R2: 1408916756
    s4t38/random/R3: 671927971
    s4t38/random/R4: 2008021024
    s4t39/unsteered/R1: 373811238
    s4t39/unsteered/R1-M: 2028323632
    s4t39/unsteered/R2: 328654243
    s4t39/unsteered/R3: 1952549575
    s4t39/unsteered/R4: 1512738168
    s4t39/hostility/R1: 404193876
    s4t39/hostility/R1-M: 1047486220
    s4t39/hostility/R2: 81179324
    s4t39/hostility/R3: 1150864632
    s4t39/hostility/R4: 858761486
    s4t39/technicality/R1: 43662724
    s4t39/technicality/R1-M: 1774729353
    s4t39/technicality/R2: 443823470
    s4t39/technicality/R3: 1122172001
    s4t39/technicality/R4: 864528906
    s4t39/random/R1: 1872218128
    s4t39/random/R1-M: 2135765645
    s4t39/random/R2: 1947941971
    s4t39/random/R3: 1823917046
    s4t39/random/R4: 437965233
    s4t40/unsteered/R1: 92273196
    s4t40/unsteered/R1-M: 1052326128
    s4t40/unsteered/R2: 1673664901
    s4t40/unsteered/R3: 723442444
    s4t40/unsteered/R4: 1479842046
    s4t40/hostility/R1: 574405769
    s4t40/hostility/R1-M: 2014138903
    s4t40/hostility/R2: 760347231
    s4t40/hostility/R3: 1140864937
    s4t40/hostility/R4: 1019608139
    s4t40/technicality/R1: 1026745027
    s4t40/technicality/R1-M: 1073587310
    s4t40/technicality/R2: 2011081919
    s4t40/technicality/R3: 1751021205
    s4t40/technicality/R4: 730554572
    s4t40/random/R1: 1127157295
    s4t40/random/R1-M: 1624222019
    s4t40/random/R2: 970426637
    s4t40/random/R3: 928550169
    s4t40/random/R4: 17851831
    s4t41/unsteered/R1: 1873855638
    s4t41/unsteered/R1-M: 1273757397
    s4t41/unsteered/R2: 1597314316
    s4t41/unsteered/R3: 1475563216
    s4t41/unsteered/R4: 2103777327
    s4t41/hostility/R1: 1392211940
    s4t41/hostility/R1-M: 601054379
    s4t41/hostility/R2: 493933349
    s4t41/hostility/R3: 1229477793
    s4t41/hostility/R4: 1442880428
    s4t41/technicality/R1: 68427898
    s4t41/technicality/R1-M: 471093283
    s4t41/technicality/R2: 1171431807
    s4t41/technicality/R3: 1771682565
    s4t41/technicality/R4: 344985260
    s4t41/random/R1: 1392658671
    s4t41/random/R1-M: 88765795
    s4t41/random/R2: 480226756
    s4t41/random/R3: 599988711
    s4t41/random/R4: 292562163
    s4t42/unsteered/R1: 819569798
    s4t42/unsteered/R1-M: 1720412373
    s4t42/unsteered/R2: 940808349
    s4t42/unsteered/R3: 1851742513
    s4t42/unsteered/R4: 367590332
    s4t42/hostility/R1: 308958810
    s4t42/hostility/R1-M: 1726167049
    s4t42/hostility/R2: 1674962539
    s4t42/hostility/R3: 725809752
    s4t42/hostility/R4: 119916745
    s4t42/technicality/R1: 851403486
    s4t42/technicality/R1-M: 730815550
    s4t42/technicality/R2: 1743925612
    s4t42/technicality/R3: 249227991
    s4t42/technicality/R4: 247498353
    s4t42/random/R1: 1672668490
    s4t42/random/R1-M: 195253166
    s4t42/random/R2: 1735550620
    s4t42/random/R3: 862374010
    s4t42/random/R4: 532930459
    s4t43/unsteered/R1: 164284970
    s4t43/unsteered/R1-M: 574476201
    s4t43/unsteered/R2: 1525283986
    s4t43/unsteered/R3: 523052797
    s4t43/unsteered/R4: 1045129745
    s4t43/hostility/R1: 311031868
    s4t43/hostility/R1-M: 417057917
    s4t43/hostility/R2: 1394572794
    s4t43/hostility/R3: 510222629
    s4t43/hostility/R4: 399433474
    s4t43/technicality/R1: 1697816945
    s4t43/technicality/R1-M: 1298436770
    s4t43/technicality/R2: 421383673
    s4t43/technicality/R3: 1566939846
    s4t43/technicality/R4: 749122765
    s4t43/random/R1: 1111398488
    s4t43/random/R1-M: 280347274
    s4t43/random/R2: 1372278886
    s4t43/random/R3: 1008010193
    s4t43/random/R4: 608944531
    s4t44/unsteered/R1: 1232037729
    s4t44/unsteered/R1-M: 1270156137
    s4t44/unsteered/R2: 2138137090
    s4t44/unsteered/R3: 644602885
    s4t44/unsteered/R4: 1260988399
    s4t44/hostility/R1: 517517603
    s4t44/hostility/R1-M: 1615916796
    s4t44/hostility/R2: 1199292156
    s4t44/hostility/R3: 803427371
    s4t44/hostility/R4: 1260143075
    s4t44/technicality/R1: 321771970
    s4t44/technicality/R1-M: 617848177
    s4t44/technicality/R2: 1164447185
    s4t44/technicality/R3: 1635169031
    s4t44/technicality/R4: 1458705090
    s4t44/random/R1: 1021870128
    s4t44/random/R1-M: 418712494
    s4t44/random/R2: 1367629885
    s4t44/random/R3: 23587631
    s4t44/random/R4: 1637335634
    s4t45/unsteered/R1: 1292743704
    s4t45/unsteered/R1-M: 2050774050
    s4t45/unsteered/R2: 1340012167
    s4t45/unsteered/R3: 383986498
    s4t45/unsteered/R4: 317418061
    s4t45/hostility/R1: 2025926226
    s4t45/hostility/R1-M: 1273595039
    s4t45/hostility/R2: 1466766466
    s4t45/hostility/R3: 142239344
    s4t45/hostility/R4: 1462886744
    s4t45/technicality/R1: 642399731
    s4t45/technicality/R1-M: 1434148814
    s4t45/technicality/R2: 620055022
    s4t45/technicality/R3: 13955008
    s4t45/technicality/R4: 48314583
    s4t45/random/R1: 973532050
    s4t45/random/R1-M: 2097925616
    s4t45/random/R2: 1617071482
    s4t45/random/R3: 1897339034
    s4t45/random/R4: 898669422
    s4t46/unsteered/R1: 543515730
    s4t46/unsteered/R1-M: 997477378
    s4t46/unsteered/R2: 283970550
    s4t46/unsteered/R3: 708378522
    s4t46/unsteered/R4: 187676162
    s4t46/hostility/R1: 1581832336
    s4t46/hostility/R1-M: 645010684
    s4t46/hostility/R2: 719402100
    s4t46/hostility/R3: 455951456
    s4t46/hostility/R4: 1207802825
    s4t46/technicality/R1: 513379910
    s4t46/technicality/R1-M: 674472564
    s4t46/technicality/R2: 1739918601
    s4t46/technicality/R3: 1065206309
    s4t46/technicality/R4: 150098386
    s4t46/random/R1: 1000727398
    s4t46/random/R1-M: 317901259
    s4t46/random/R2: 699339704
    s4t46/random/R3: 340048931
    s4t46/random/R4: 689561382
    s4t47/unsteered/R1: 1818227058
    s4t47/unsteered/R1-M: 862977174
    s4t47/unsteered/R2: 722457834
    s4t47/unsteered/R3: 401801940
    s4t47/unsteered/R4: 890285121
    s4t47/hostility/R1: 1428629086
    s4t47/hostility/R1-M: 1846795606
    s4t47/hostility/R2: 1596642700
    s4t47/hostility/R3: 690289893
    s4t47/hostility/R4: 1951897821
    s4t47/technicality/R1: 2143743821
    s4t47/technicality/R1-M: 1000687342
    s4t47/technicality/R2: 2045343011
    s4t47/technicality/R3: 1523830262
    s4t47/technicality/R4: 1420715631
    s4t47/random/R1: 1935390650
    s4t47/random/R1-M: 1385520632
    s4t47/random/R2: 2065176821
    s4t47/random/R3: 867299822
    s4t47/random/R4: 836864534
    s4t48/unsteered/R1: 1639067865
    s4t48/unsteered/R1-M: 336714390
    s4t48/unsteered/R2: 106048842
    s4t48/unsteered/R3: 607922978
    s4t48/unsteered/R4: 1074871295
    s4t48/hostility/R1: 178618575
    s4t48/hostility/R1-M: 619423506
    s4t48/hostility/R2: 1492410301
    s4t48/hostility/R3: 243778159
    s4t48/hostility/R4: 618322851
    s4t48/technicality/R1: 456055831
    s4t48/technicality/R1-M: 1013721283
    s4t48/technicality/R2: 2133961244
    s4t48/technicality/R3: 1995855633
    s4t48/technicality/R4: 41042718
    s4t48/random/R1: 196922540
    s4t48/random/R1-M: 1539302690
    s4t48/random/R2: 1439107752
    s4t48/random/R3: 1988094359
    s4t48/random/R4: 1670753252
    s4t49/unsteered/R1: 1540193350
    s4t49/unsteered/R1-M: 1693549350
    s4t49/unsteered/R2: 1015329095
    s4t49/unsteered/R3: 955949172
    s4t49/unsteered/R4: 2055455696
    s4t49/hostility/R1: 1359981999
    s4t49/hostility/R1-M: 623636717
    s4t49/hostility/R2: 919899726
    s4t49/hostility/R3: 606235758
    s4t49/hostility/R4: 2049091933
    s4t49/technicality/R1: 1472755473
    s4t49/technicality/R1-M: 1068693168
    s4t49/technicality/R2: 883275137
    s4t49/technicality/R3: 915806929
    s4t49/technicality/R4: 202887226
    s4t49/random/R1: 1148305439
    s4t49/random/R1-M: 41443130
    s4t49/random/R2: 348698601
    s4t49/random/R3: 558306314
    s4t49/random/R4: 1435832744
    s4t50/unsteered/R1: 98757418
    s4t50/unsteered/R1-M: 211172257
    s4t50/unsteered/R2: 1864503016
    s4t50/unsteered/R3: 1153054876
    s4t50/unsteered/R4: 1613496922
    s4t50/hostility/R1: 341524438
    s4t50/hostility/R1-M: 496491867
    s4t50/hostility/R2: 540655144
    s4t50/hostility/R3: 2086950426
    s4t50/hostility/R4: 2085861618
    s4t50/technicality/R1: 463057236
    s4t50/technicality/R1-M: 456691436
    s4t50/technicality/R2: 2089913693
    s4t50/technicality/R3: 1455654129
    s4t50/technicality/R4: 2131933776
    s4t50/random/R1: 791069142
    s4t50/random/R1-M: 1285163579
    s4t50/random/R2: 361735832
    s4t50/random/R3: 119360220
    s4t50/random/R4: 1936920398
    s4t51/unsteered/R1: 685420774
    s4t51/unsteered/R1-M: 1281476171
    s4t51/unsteered/R2: 818177577
    s4t51/unsteered/R3: 42738862
    s4t51/unsteered/R4: 1954822870
    s4t51/hostility/R1: 847141690
    s4t51/hostility/R1-M: 1129139714
    s4t51/hostility/R2: 183176017
    s4t51/hostility/R3: 1362388394
    s4t51/hostility/R4: 1700592679
    s4t51/technicality/R1: 1721228270
    s4t51/technicality/R1-M: 1327832809
    s4t51/technicality/R2: 1937700252
    s4t51/technicality/R3: 1821326079
    s4t51/technicality/R4: 71774452
    s4t51/random/R1: 1888292955
    s4t51/random/R1-M: 1611762731
    s4t51/random/R2: 7078126
    s4t51/random/R3: 999777804
    s4t51/random/R4: 58277166
    s4t52/unsteered/R1: 369239139
    s4t52/unsteered/R1-M: 955646643
    s4t52/unsteered/R2: 24086354
    s4t52/unsteered/R3: 959385386
    s4t52/unsteered/R4: 862430899
    s4t52/hostility/R1: 642401259
    s4t52/hostility/R1-M: 735288117
    s4t52/hostility/R2: 520514748
    s4t52/hostility/R3: 524282699
    s4t52/hostility/R4: 534965535
    s4t52/technicality/R1: 39874908
    s4t52/technicality/R1-M: 76034501
    s4t52/technicality/R2: 2117058488
    s4t52/technicality/R3: 151188900
    s4t52/technicality/R4: 1317870558
    s4t52/random/R1: 390224241
    s4t52/random/R1-M: 1321001520
    s4t52/random/R2: 2127852008
    s4t52/random/R3: 908307646
    s4t52/random/R4: 769972735
    s4t53/unsteered/R1: 179692875
    s4t53/unsteered/R1-M: 1902751740
    s4t53/unsteered/R2: 2004383597
    s4t53/unsteered/R3: 1325638238
    s4t53/unsteered/R4: 1452226198
    s4t53/hostility/R1: 579710338
    s4t53/hostility/R1-M: 302841632
    s4t53/hostility/R2: 1097094782
    s4t53/hostility/R3: 866061534
    s4t53/hostility/R4: 493097079
    s4t53/technicality/R1: 26438020
    s4t53/technicality/R1-M: 1467528893
    s4t53/technicality/R2: 1983453214
    s4t53/technicality/R3: 429512787
    s4t53/technicality/R4: 392482375
    s4t53/random/R1: 1846643226
    s4t53/random/R1-M: 1757057452
    s4t53/random/R2: 97075302
    s4t53/random/R3: 1320507359
    s4t53/random/R4: 960344860
    s4t54/unsteered/R1: 1810283249
    s4t54/unsteered/R1-M: 1562762750
    s4t54/unsteered/R2: 2090319230
    s4t54/unsteered/R3: 427141740
    s4t54/unsteered/R4: 1646254946
    s4t54/hostility/R1: 2093026552
    s4t54/hostility/R1-M: 1404038118
    s4t54/hostility/R2: 916830475
    s4t54/hostility/R3: 416091501
    s4t54/hostility/R4: 2010227202
    s4t54/technicality/R1: 559958485
    s4t54/technicality/R1-M: 822869220
    s4t54/technicality/R2: 1258181442
    s4t54/technicality/R3: 2008862514
    s4t54/technicality/R4: 1795610232
    s4t54/random/R1: 710647029
    s4t54/random/R1-M: 853797881
    s4t54/random/R2: 1138976262
    s4t54/random/R3: 2142019008
    s4t54/random/R4: 777223147
    s4t55/unsteered/R1: 1521338735
    s4t55/unsteered/R1-M: 1051910799
    s4t55/unsteered/R2: 272499359
    s4t55/unsteered/R3: 115109952
    s4t55/unsteered/R4: 976566701
    s4t55/hostility/R1: 695964465
    s4t55/hostility/R1-M: 1608998242
    s4t55/hostility/R2: 64080046
    s4t55/hostility/R3: 1731758702
    s4t55/hostility/R4: 2090560661
    s4t55/technicality/R1: 1036094151
    s4t55/technicality/R1-M: 1920555369
    s4t55/technicality/R2: 1005121195
    s4t55/technicality/R3: 916231506
    s4t55/technicality/R4: 1419499506
    s4t55/random/R1: 1753847483
    s4t55/random/R1-M: 2055435529
    s4t55/random/R2: 970799736
    s4t55/random/R3: 726608702
    s4t55/random/R4: 1356936657
    s4t56/unsteered/R1: 484615478
    s4t56/unsteered/R1-M: 1974020351
    s4t56/unsteered/R2: 2072068264
    s4t56/unsteered/R3: 903714791
    s4t56/unsteered/R4: 2101830380
    s4t56/hostility/R1: 1807629063
    s4t56/hostility/R1-M: 194530048
    s4t56/hostility/R2: 2046731328
    s4t56/hostility/R3: 726241120
    s4t56/hostility/R4: 820032965
    s4t56/technicality/R1: 202950031
    s4t56/technicality/R1-M: 750282073
    s4t56/technicality/R2: 1402339917
    s4t56/technicality/R3: 1338124286
    s4t56/technicality/R4: 132471078
    s4t56/random/R1: 999129010
    s4t56/random/R1-M: 1378385520
    s4t56/random/R2: 580655263
    s4t56/random/R3: 1904504649
    s4t56/random/R4: 1130777587
    s4t57/unsteered/R1: 646909177
    s4t57/unsteered/R1-M: 189219048
    s4t57/unsteered/R2: 564595728
    s4t57/unsteered/R3: 1963482877
    s4t57/unsteered/R4: 791659147
    s4t57/hostility/R1: 1519469329
    s4t57/hostility/R1-M: 1353606966
    s4t57/hostility/R2: 569828146
    s4t57/hostility/R3: 1179413031
    s4t57/hostility/R4: 768255662
    s4t57/technicality/R1: 1737324019
    s4t57/technicality/R1-M: 1411534218
    s4t57/technicality/R2: 1610224506
    s4t57/technicality/R3: 1539924062
    s4t57/technicality/R4: 409778840
    s4t57/random/R1: 478157769
    s4t57/random/R1-M: 1198045099
    s4t57/random/R2: 2004589771
    s4t57/random/R3: 1127206039
    s4t57/random/R4: 1859480513
    s4t58/unsteered/R1: 289277040
    s4t58/unsteered/R1-M: 2111497833
    s4t58/unsteered/R2: 1859670821
    s4t58/unsteered/R3: 2013308575
    s4t58/unsteered/R4: 977897649
    s4t58/hostility/R1: 909260236
    s4t58/hostility/R1-M: 42954426
    s4t58/hostility/R2: 169750324
    s4t58/hostility/R3: 871333138
    s4t58/hostility/R4: 549255463
    s4t58/technicality/R1: 2075309795
    s4t58/technicality/R1-M: 213059881
    s4t58/technicality/R2: 158988463
    s4t58/technicality/R3: 1398160919
    s4t58/technicality/R4: 997055665
    s4t58/random/R1: 39430939
    s4t58/random/R1-M: 394743307
    s4t58/random/R2: 1218004794
    s4t58/random/R3: 49847916
    s4t58/random/R4: 338511242
    s4t59/unsteered/R1: 253184143
    s4t59/unsteered/R1-M: 561411020
    s4t59/unsteered/R2: 1897643283
    s4t59/unsteered/R3: 811450992
    s4t59/unsteered/R4: 1270045753
    s4t59/hostility/R1: 518593644
    s4t59/hostility/R1-M: 65703557
    s4t59/hostility/R2: 1595484125
    s4t59/hostility/R3: 1169444786
    s4t59/hostility/R4: 749938363
    s4t59/technicality/R1: 1985554196
    s4t59/technicality/R1-M: 1738131669
    s4t59/technicality/R2: 274307486
    s4t59/technicality/R3: 1987503437
    s4t59/technicality/R4: 1429252805
    s4t59/random/R1: 1898209597
    s4t59/random/R1-M: 1846586568
    s4t59/random/R2: 2045508634
    s4t59/random/R3: 631293473
    s4t59/random/R4: 690440885
    s4t60/unsteered/R1: 1768823581
    s4t60/unsteered/R1-M: 1121314695
    s4t60/unsteered/R2: 1570448552
    s4t60/unsteered/R3: 707489589
    s4t60/unsteered/R4: 1197541329
    s4t60/hostility/R1: 596193852
    s4t60/hostility/R1-M: 2015697502
    s4t60/hostility/R2: 2057044448
    s4t60/hostility/R3: 454482040
    s4t60/hostility/R4: 903520854
    s4t60/technicality/R1: 572249836
    s4t60/technicality/R1-M: 1487248619
    s4t60/technicality/R2: 235218918
    s4t60/technicality/R3: 1515875309
    s4t60/technicality/R4: 1411326455
    s4t60/random/R1: 264164303
    s4t60/random/R1-M: 722218588
    s4t60/random/R2: 2101050908
    s4t60/random/R3: 1021780045
    s4t60/random/R4: 2107844758
    s4t61/unsteered/R1: 1169701040
    s4t61/unsteered/R1-M: 71339121
    s4t61/unsteered/R2: 1093384529
    s4t61/unsteered/R3: 1020346955
    s4t61/unsteered/R4: 1899052600
    s4t61/hostility/R1: 1828263294
    s4t61/hostility/R1-M: 7491067
    s4t61/hostility/R2: 524819608
    s4t61/hostility/R3: 169296979
    s4t61/hostility/R4: 718093193
    s4t61/technicality/R1: 1230148691
    s4t61/technicality/R1-M: 1126282284
    s4t61/technicality/R2: 1746979662
    s4t61/technicality/R3: 727501226
    s4t61/technicality/R4: 1306564327
    s4t61/random/R1: 1209464823
    s4t61/random/R1-M: 1519202621
    s4t61/random/R2: 1984062736
    s4t61/random/R3: 1136197549
    s4t61/random/R4: 1656646545
    s4t62/unsteered/R1: 1812679384
    s4t62/unsteered/R1-M: 863658690
    s4t62/unsteered/R2: 643117503
    s4t62/unsteered/R3: 518142838
    s4t62/unsteered/R4: 865704024
    s4t62/hostility/R1: 2075163704
    s4t62/hostility/R1-M: 1605085530
    s4t62/hostility/R2: 1751070138
    s4t62/hostility/R3: 31632608
    s4t62/hostility/R4: 732146397
    s4t62/technicality/R1: 89415628
    s4t62/technicality/R1-M: 1991090732
    s4t62/technicality/R2: 728335021
    s4t62/technicality/R3: 1423353897
    s4t62/technicality/R4: 1380903810
    s4t62/random/R1: 1083595136
    s4t62/random/R1-M: 901887642
    s4t62/random/R2: 236814760
    s4t62/random/R3: 163301048
    s4t62/random/R4: 981907230
    s4t63/unsteered/R1: 1461513708
    s4t63/unsteered/R1-M: 146794499
    s4t63/unsteered/R2: 490017288
    s4t63/unsteered/R3: 2025426861
    s4t63/unsteered/R4: 734060718
    s4t63/hostility/R1: 1577003166
    s4t63/hostility/R1-M: 374071066
    s4t63/hostility/R2: 1013961528
    s4t63/hostility/R3: 28407418
    s4t63/hostility/R4: 1081067162
    s4t63/technicality/R1: 1391034668
    s4t63/technicality/R1-M: 1959383692
    s4t63/technicality/R2: 445200219
    s4t63/technicality/R3: 779162655
    s4t63/technicality/R4: 175281216
    s4t63/random/R1: 1946774690
    s4t63/random/R1-M: 1995116245
    s4t63/random/R2: 708404581
    s4t63/random/R3: 756179898
    s4t63/random/R4: 1218564776
    s4t64/unsteered/R1: 1000775240
    s4t64/unsteered/R1-M: 775731427
    s4t64/unsteered/R2: 1935211554
    s4t64/unsteered/R3: 1695158365
    s4t64/unsteered/R4: 326039993
    s4t64/hostility/R1: 876312068
    s4t64/hostility/R1-M: 814180709
    s4t64/hostility/R2: 1536119316
    s4t64/hostility/R3: 1692507400
    s4t64/hostility/R4: 721395362
    s4t64/technicality/R1: 631002675
    s4t64/technicality/R1-M: 1835908061
    s4t64/technicality/R2: 2024045972
    s4t64/technicality/R3: 665196442
    s4t64/technicality/R4: 625103871
    s4t64/random/R1: 1256609673
    s4t64/random/R1-M: 1095439512
    s4t64/random/R2: 1970783532
    s4t64/random/R3: 151788389
    s4t64/random/R4: 372126688
    s4t65/unsteered/R1: 886089086
    s4t65/unsteered/R1-M: 1688131196
    s4t65/unsteered/R2: 1787011238
    s4t65/unsteered/R3: 1545885340
    s4t65/unsteered/R4: 175951831
    s4t65/hostility/R1: 650550266
    s4t65/hostility/R1-M: 1877349643
    s4t65/hostility/R2: 842787475
    s4t65/hostility/R3: 1726005019
    s4t65/hostility/R4: 2001844625
    s4t65/technicality/R1: 849130867
    s4t65/technicality/R1-M: 719305059
    s4t65/technicality/R2: 1077334416
    s4t65/technicality/R3: 1333709573
    s4t65/technicality/R4: 758797517
    s4t65/random/R1: 1796068511
    s4t65/random/R1-M: 447588683
    s4t65/random/R2: 1422266780
    s4t65/random/R3: 1501044703
    s4t65/random/R4: 1186576352
    s4t66/unsteered/R1: 1764657475
    s4t66/unsteered/R1-M: 68203220
    s4t66/unsteered/R2: 1802347926
    s4t66/unsteered/R3: 967179918
    s4t66/unsteered/R4: 843919761
    s4t66/hostility/R1: 569779227
    s4t66/hostility/R1-M: 1316143019
    s4t66/hostility/R2: 1078038724
    s4t66/hostility/R3: 1268142407
    s4t66/hostility/R4: 454943196
    s4t66/technicality/R1: 1298115309
    s4t66/technicality/R1-M: 795801282
    s4t66/technicality/R2: 1778222811
    s4t66/technicality/R3: 774963668
    s4t66/technicality/R4: 805562474
    s4t66/random/R1: 1000017686
    s4t66/random/R1-M: 437905214
    s4t66/random/R2: 1464589091
    s4t66/random/R3: 1180149469
    s4t66/random/R4: 1340258845
    s4t67/unsteered/R1: 1537789898
    s4t67/unsteered/R1-M: 1452876606
    s4t67/unsteered/R2: 319881303
    s4t67/unsteered/R3: 816681220
    s4t67/unsteered/R4: 628566550
    s4t67/hostility/R1: 1571518653
    s4t67/hostility/R1-M: 455809721
    s4t67/hostility/R2: 395104585
    s4t67/hostility/R3: 557439054
    s4t67/hostility/R4: 1124856749
    s4t67/technicality/R1: 1467576172
    s4t67/technicality/R1-M: 1531867079
    s4t67/technicality/R2: 2063707038
    s4t67/technicality/R3: 1464324436
    s4t67/technicality/R4: 338451381
    s4t67/random/R1: 2028994957
    s4t67/random/R1-M: 2122132766
    s4t67/random/R2: 534806537
    s4t67/random/R3: 1499949227
    s4t67/random/R4: 1980221096
    s4t68/unsteered/R1: 287023657
    s4t68/unsteered/R1-M: 667364416
    s4t68/unsteered/R2: 499756025
    s4t68/unsteered/R3: 1028172632
    s4t68/unsteered/R4: 455247649
    s4t68/hostility/R1: 671276575
    s4t68/hostility/R1-M: 563526269
    s4t68/hostility/R2: 364933661
    s4t68/hostility/R3: 1096761861
    s4t68/hostility/R4: 578510936
    s4t68/technicality/R1: 2136413932
    s4t68/technicality/R1-M: 1883539388
    s4t68/technicality/R2: 2145533875
    s4t68/technicality/R3: 1174311984
    s4t68/technicality/R4: 1802846203
    s4t68/random/R1: 1034379916
    s4t68/random/R1-M: 2004800012
    s4t68/random/R2: 121004575
    s4t68/random/R3: 1730408830
    s4t68/random/R4: 1745633313
    s4t69/unsteered/R1: 1267562137
    s4t69/unsteered/R1-M: 1028445121
    s4t69/unsteered/R2: 257232273
    s4t69/unsteered/R3: 1473100182
    s4t69/unsteered/R4: 1458964013
    s4t69/hostility/R1: 2044237677
    s4t69/hostility/R1-M: 1124920637
    s4t69/hostility/R2: 1852873198
    s4t69/hostility/R3: 98136011
    s4t69/hostility/R4: 1589359470
    s4t69/technicality/R1: 1990882496
    s4t69/technicality/R1-M: 2096722061
    s4t69/technicality/R2: 1549381821
    s4t69/technicality/R3: 254059151
    s4t69/technicality/R4: 277984688
    s4t69/random/R1: 1298929265
    s4t69/random/R1-M: 13556467
    s4t69/random/R2: 807539743
    s4t69/random/R3: 1550500749
    s4t69/random/R4: 1035368117
    s4t70/unsteered/R1: 2065013197
    s4t70/unsteered/R1-M: 1956096404
    s4t70/unsteered/R2: 2123968752
    s4t70/unsteered/R3: 1112960631
    s4t70/unsteered/R4: 423739385
    s4t70/hostility/R1: 418869325
    s4t70/hostility/R1-M: 999363171
    s4t70/hostility/R2: 762364157
    s4t70/hostility/R3: 1895016920
    s4t70/hostility/R4: 1886737514
    s4t70/technicality/R1: 89251075
    s4t70/technicality/R1-M: 1302417112
    s4t70/technicality/R2: 1177294928
    s4t70/technicality/R3: 325259386
    s4t70/technicality/R4: 1541276407
    s4t70/random/R1: 1465305938
    s4t70/random/R1-M: 148814969
    s4t70/random/R2: 280759623
    s4t70/random/R3: 1948117192
    s4t70/random/R4: 296811258
    s4t71/unsteered/R1: 2099857897
    s4t71/unsteered/R1-M: 621375533
    s4t71/unsteered/R2: 404220857
    s4t71/unsteered/R3: 522330107
    s4t71/unsteered/R4: 417755133
    s4t71/hostility/R1: 1682598598
    s4t71/hostility/R1-M: 706767335
    s4t71/hostility/R2: 1997909602
    s4t71/hostility/R3: 1882115208
    s4t71/hostility/R4: 154753841
    s4t71/technicality/R1: 1593456491
    s4t71/technicality/R1-M: 497843548
    s4t71/technicality/R2: 308922993
    s4t71/technicality/R3: 784125483
    s4t71/technicality/R4: 199300210
    s4t71/random/R1: 1833404047
    s4t71/random/R1-M: 997164293
    s4t71/random/R2: 1882040790
    s4t71/random/R3: 1716318068
    s4t71/random/R4: 2053763614
    s4t72/unsteered/R1: 205613562
    s4t72/unsteered/R1-M: 1879408254
    s4t72/unsteered/R2: 28580801
    s4t72/unsteered/R3: 1470221605
    s4t72/unsteered/R4: 174530438
    s4t72/hostility/R1: 507986483
    s4t72/hostility/R1-M: 1138765604
    s4t72/hostility/R2: 1936065838
    s4t72/hostility/R3: 1900497578
    s4t72/hostility/R4: 2072803142
    s4t72/technicality/R1: 716276409
    s4t72/technicality/R1-M: 872755945
    s4t72/technicality/R2: 4108337
    s4t72/technicality/R3: 532388461
    s4t72/technicality/R4: 697837078
    s4t72/random/R1: 587193334
    s4t72/random/R1-M: 819034060
    s4t72/random/R2: 1395770826
    s4t72/random/R3: 850520823
    s4t72/random/R4: 1232447401
    s4t73/unsteered/R1: 1225068303
    s4t73/unsteered/R1-M: 639473904
    s4t73/unsteered/R2: 2099353872
    s4t73/unsteered/R3: 646378242
    s4t73/unsteered/R4: 731395560
    s4t73/hostility/R1: 2017288425
    s4t73/hostility/R1-M: 1057635113
    s4t73/hostility/R2: 1010066019
    s4t73/hostility/R3: 1645978061
    s4t73/hostility/R4: 919109758
    s4t73/technicality/R1: 862589406
    s4t73/technicality/R1-M: 1155650123
    s4t73/technicality/R2: 1393619389
    s4t73/technicality/R3: 1197547315
    s4t73/technicality/R4: 777345316
    s4t73/random/R1: 588435134
    s4t73/random/R1-M: 1144366083
    s4t73/random/R2: 1337253508
    s4t73/random/R3: 290152501
    s4t73/random/R4: 1018879961
    s4t74/unsteered/R1: 1653275204
    s4t74/unsteered/R1-M: 676682848
    s4t74/unsteered/R2: 184198739
    s4t74/unsteered/R3: 549762471
    s4t74/unsteered/R4: 147161681
    s4t74/hostility/R1: 12356848
    s4t74/hostility/R1-M: 912710160
    s4t74/hostility/R2: 534951901
    s4t74/hostility/R3: 1816889227
    s4t74/hostility/R4: 888869184
    s4t74/technicality/R1: 131701283
    s4t74/technicality/R1-M: 1371136155
    s4t74/technicality/R2: 2137962095
    s4t74/technicality/R3: 1657298057
    s4t74/technicality/R4: 1092962079
    s4t74/random/R1: 1531367579
    s4t74/random/R1-M: 1831097701
    s4t74/random/R2: 1993368723
    s4t74/random/R3: 1280508548
    s4t74/random/R4: 553427492
    s4t75/unsteered/R1: 1887106556
    s4t75/unsteered/R1-M: 1856433022
    s4t75/unsteered/R2: 1198954680
    s4t75/unsteered/R3: 1149357396
    s4t75/unsteered/R4: 1414449095
    s4t75/hostility/R1: 1178456087
    s4t75/hostility/R1-M: 1979125295
    s4t75/hostility/R2: 786320428
    s4t75/hostility/R3: 408820362
    s4t75/hostility/R4: 1035490048
    s4t75/technicality/R1: 650520464
    s4t75/technicality/R1-M: 1214591478
    s4t75/technicality/R2: 130035245
    s4t75/technicality/R3: 998289629
    s4t75/technicality/R4: 1617068427
    s4t75/random/R1: 1891535433
    s4t75/random/R1-M: 169137140
    s4t75/random/R2: 1003768653
    s4t75/random/R3: 1216070923
    s4t75/random/R4: 307741974
    s4t76/unsteered/R1: 571566444
    s4t76/unsteered/R1-M: 1871941690
    s4t76/unsteered/R2: 943015097
    s4t76/unsteered/R3: 1915706772
    s4t76/unsteered/R4: 1074119470
    s4t76/hostility/R1: 520904907
    s4t76/hostility/R1-M: 212957092
    s4t76/hostility/R2: 315198302
    s4t76/hostility/R3: 582893176
    s4t76/hostility/R4: 853517455
    s4t76/technicality/R1: 1483592475
    s4t76/technicality/R1-M: 2023473700
    s4t76/technicality/R2: 1666669438
    s4t76/technicality/R3: 15865078
    s4t76/technicality/R4: 2039597310
    s4t76/random/R1: 1737613656
    s4t76/random/R1-M: 1325554749
    s4t76/random/R2: 839876391
    s4t76/random/R3: 247709862
    s4t76/random/R4: 543553624
    s4t77/unsteered/R1: 1207589400
    s4t77/unsteered/R1-M: 184646770
    s4t77/unsteered/R2: 107322310
    s4t77/unsteered/R3: 1890631082
    s4t77/unsteered/R4: 999408659
    s4t77/hostility/R1: 806547034
    s4t77/hostility/R1-M: 1147428774
    s4t77/hostility/R2: 872714796
    s4t77/hostility/R3: 14619970
    s4t77/hostility/R4: 1827029793
    s4t77/technicality/R1: 350031825
    s4t77/technicality/R1-M: 1922703514
    s4t77/technicality/R2: 1384188730
    s4t77/technicality/R3: 922883962
    s4t77/technicality/R4: 745887968
    s4t77/random/R1: 1465292127
    s4t77/random/R1-M: 1215224587
    s4t77/random/R2: 1084789006
    s4t77/random/R3: 1738952159
    s4t77/random/R4: 552759888
    s4t78/unsteered/R1: 126930120
    s4t78/unsteered/R1-M: 1155456654
    s4t78/unsteered/R2: 240017966
    s4t78/unsteered/R3: 1726294231
    s4t78/unsteered/R4: 1259724189
    s4t78/hostility/R1: 1180049309
    s4t78/hostility/R1-M: 116498426
    s4t78/hostility/R2: 458428928
    s4t78/hostility/R3: 417508661
    s4t78/hostility/R4: 1316726607
    s4t78/technicality/R1: 1841153172
    s4t78/technicality/R1-M: 1164325006
    s4t78/technicality/R2: 1000770627
    s4t78/technicality/R3: 2031668899
    s4t78/technicality/R4: 825025171
    s4t78/random/R1: 1907629781
    s4t78/random/R1-M: 2029415830
    s4t78/random/R2: 1658430551
    s4t78/random/R3: 123513669
    s4t78/random/R4: 1003432967
    s4t79/unsteered/R1: 1167764007
    s4t79/unsteered/R1-M: 525004366
    s4t79/unsteered/R2: 41731623
    s4t79/unsteered/R3: 139154031
    s4t79/unsteered/R4: 168133293
    s4t79/hostility/R1: 1625309335
    s4t79/hostility/R1-M: 57856264
    s4t79/hostility/R2: 515731271
    s4t79/hostility/R3: 445039346
    s4t79/hostility/R4: 637252821
    s4t79/technicality/R1: 734266130
    s4t79/technicality/R1-M: 1858235337
    s4t79/technicality/R2: 1777760556
    s4t79/technicality/R3: 2105526397
    s4t79/technicality/R4: 482776647
    s4t79/random/R1: 5586066
    s4t79/random/R1-M: 620140336
    s4t79/random/R2: 655112183
    s4t79/random/R3: 636372042
    s4t79/random/R4: 185782983
  pilot:
    s3t00/unsteered/R1: 1174483379
    s3t00/unsteered/R1-M: 562672716
    s3t00/unsteered/R2: 2106953841
    s3t00/unsteered/R3: 1958080381
    s3t00/unsteered/R4: 483347299
    s3t00/hostility/R1: 1177105941
    s3t00/hostility/R1-M: 71145913
    s3t00/hostility/R2: 803562051
    s3t00/hostility/R3: 750896547
    s3t00/hostility/R4: 1439425968
    s3t00/technicality/R1: 1970281509
    s3t00/technicality/R1-M: 1717240645
    s3t00/technicality/R2: 1538881275
    s3t00/technicality/R3: 1996449157
    s3t00/technicality/R4: 1824570429
    s3t00/random/R1: 1326401628
    s3t00/random/R1-M: 817834399
    s3t00/random/R2: 263295923
    s3t00/random/R3: 1956877161
    s3t00/random/R4: 1861779514
    s3t01/unsteered/R1: 1075591318
    s3t01/unsteered/R1-M: 495802813
    s3t01/unsteered/R2: 65926168
    s3t01/unsteered/R3: 1014061028
    s3t01/unsteered/R4: 1429213118
    s3t01/hostility/R1: 211478682
    s3t01/hostility/R1-M: 833498528
    s3t01/hostility/R2: 576428921
    s3t01/hostility/R3: 181871936
    s3t01/hostility/R4: 661903794
    s3t01/technicality/R1: 90119736
    s3t01/technicality/R1-M: 1268638100
    s3t01/technicality/R2: 1834659843
    s3t01/technicality/R3: 617736244
    s3t01/technicality/R4: 1450185488
    s3t01/random/R1: 1845770697
    s3t01/random/R1-M: 458534034
    s3t01/random/R2: 1443555106
    s3t01/random/R3: 473727071
    s3t01/random/R4: 832567956
    s3t02/unsteered/R1: 1714887235
    s3t02/unsteered/R1-M: 181974241
    s3t02/unsteered/R2: 892128552
    s3t02/unsteered/R3: 977491980
    s3t02/unsteered/R4: 1998620510
    s3t02/hostility/R1: 980921121
    s3t02/hostility/R1-M: 1168811625
    s3t02/hostility/R2: 865573310
    s3t02/hostility/R3: 628946603
    s3t02/hostility/R4: 1297141346
    s3t02/technicality/R1: 1475776915
    s3t02/technicality/R1-M: 1286113308
    s3t02/technicality/R2: 547190636
    s3t02/technicality/R3: 1511016047
    s3t02/technicality/R4: 1713081148
    s3t02/random/R1: 1493473611
    s3t02/random/R1-M: 105410266
    s3t02/random/R2: 312318927
    s3t02/random/R3: 1251399188
    s3t02/random/R4: 2059406087
    s3t03/unsteered/R1: 71149053
    s3t03/unsteered/R1-M: 1480821365
    s3t03/unsteered/R2: 1753377834
    s3t03/unsteered/R3: 2070857451
    s3t03/unsteered/R4: 1366179360
    s3t03/hostility/R1: 1799865499
    s3t03/hostility/R1-M: 1976502758
    s3t03/hostility/R2: 12321240
    s3t03/hostility/R3: 1177600983
    s3t03/hostility/R4: 2075714399
    s3t03/technicality/R1: 1809447000
    s3t03/technicality/R1-M: 527664604
    s3t03/technicality/R2: 1931996393
    s3t03/technicality/R3: 1349104133
    s3t03/technicality/R4: 1464480389
    s3t03/random/R1: 1673408649
    s3t03/random/R1-M: 991254901
    s3t03/random/R2: 232511991
    s3t03/random/R3: 1000855687
    s3t03/random/R4: 1660666395
    s3t04/unsteered/R1: 1356140629
    s3t04/unsteered/R1-M: 1482480545
    s3t04/unsteered/R2: 865958439
    s3t04/unsteered/R3: 179489874
    s3t04/unsteered/R4: 1519026785
    s3t04/hostility/R1: 794795012
    s3t04/hostility/R1-M: 1774943754
    s3t04/hostility/R2: 534923671
    s3t04/hostility/R3: 1887494626
    s3t04/hostility/R4: 1911405979
    s3t04/technicality/R1: 1592170774
    s3t04/technicality/R1-M: 1562908163
    s3t04/technicality/R2: 1439167948
    s3t04/technicality/R3: 1832108933
    s3t04/technicality/R4: 988177408
    s3t04/random/R1: 260972228
    s3t04/random/R1-M: 1830223767
    s3t04/random/R2: 1047724146
    s3t04/random/R3: 1693067190
    s3t04/random/R4: 574880922
    s3t05/unsteered/R1: 1227281113
    s3t05/unsteered/R1-M: 295293183
    s3t05/unsteered/R2: 2029564766
    s3t05/unsteered/R3: 75236124
    s3t05/unsteered/R4: 1210783862
    s3t05/hostility/R1: 1036958476
    s3t05/hostility/R1-M: 924172626
    s3t05/hostility/R2: 403335456
    s3t05/hostility/R3: 254798118
    s3t05/hostility/R4: 1495388020
    s3t05/technicality/R1: 1322171356
    s3t05/technicality/R1-M: 1381029034
    s3t05/technicality/R2: 216162774
    s3t05/technicality/R3: 926800644
    s3t05/technicality/R4: 1829468218
    s3t05/random/R1: 846126475
    s3t05/random/R1-M: 1493239751
    s3t05/random/R2: 1325881239
    s3t05/random/R3: 2011817895
    s3t05/random/R4: 2031610742
    s3t06/unsteered/R1: 202744229
    s3t06/unsteered/R1-M: 1862745907
    s3t06/unsteered/R2: 148711847
    s3t06/unsteered/R3: 2089499945
    s3t06/unsteered/R4: 960274298
    s3t06/hostility/R1: 538895913
    s3t06/hostility/R1-M: 14085687
    s3t06/hostility/R2: 931528463
    s3t06/hostility/R3: 2071066212
    s3t06/hostility/R4: 939353744
    s3t06/technicality/R1: 1082942691
    s3t06/technicality/R1-M: 245466755
    s3t06/technicality/R2: 698633953
    s3t06/technicality/R3: 21314603
    s3t06/technicality/R4: 1844410964
    s3t06/random/R1: 1002621852
    s3t06/random/R1-M: 1709901199
    s3t06/random/R2: 819341774
    s3t06/random/R3: 1056177952
    s3t06/random/R4: 1515396342
    s3t07/unsteered/R1: 80935370
    s3t07/unsteered/R1-M: 31973094
    s3t07/unsteered/R2: 451325327
    s3t07/unsteered/R3: 22177003
    s3t07/unsteered/R4: 469882364
    s3t07/hostility/R1: 617566967
    s3t07/hostility/R1-M: 119705904
    s3t07/hostility/R2: 574490528
    s3t07/hostility/R3: 139079649
    s3t07/hostility/R4: 1022278287
    s3t07/technicality/R1: 1515285588
    s3t07/technicality/R1-M: 1368554444
    s3t07/technicality/R2: 1092143287
    s3t07/technicality/R3: 1223676472
    s3t07/technicality/R4: 1396589800
    s3t07/random/R1: 1298537398
    s3t07/random/R1-M: 11366652
    s3t07/random/R2: 2005601777
    s3t07/random/R3: 554825428
    s3t07/random/R4: 635622694
    s3t08/unsteered/R1: 1905566486
    s3t08/unsteered/R1-M: 805504123
    s3t08/unsteered/R2: 2001980652
    s3t08/unsteered/R3: 1367348283
    s3t08/unsteered/R4: 1744499413
    s3t08/hostility/R1: 1424454802
    s3t08/hostility/R1-M: 543352229
    s3t08/hostility/R2: 788381046
    s3t08/hostility/R3: 1808632427
    s3t08/hostility/R4: 1895225977
    s3t08/technicality/R1: 1530593512
    s3t08/technicality/R1-M: 1319418517
    s3t08/technicality/R2: 540136465
    s3t08/technicality/R3: 1335980845
    s3t08/technicality/R4: 280698542
    s3t08/random/R1: 1681447298
    s3t08/random/R1-M: 268651954
    s3t08/random/R2: 1588072089
    s3t08/random/R3: 1867713605
    s3t08/random/R4: 1259593415
    s3t09/unsteered/R1: 429650700
    s3t09/unsteered/R1-M: 2128941796
    s3t09/unsteered/R2: 1622101181
    s3t09/unsteered/R3: 710066323
    s3t09/unsteered/R4: 284816322
    s3t09/hostility/R1: 2136377688
    s3t09/hostility/R1-M: 698749706
    s3t09/hostility/R2: 1494697147
    s3t09/hostility/R3: 693409714
    s3t09/hostility/R4: 297688192
    s3t09/technicality/R1: 1904916222
    s3t09/technicality/R1-M: 1014013703
    s3t09/technicality/R2: 871998018
    s3t09/technicality/R3: 1927890436
    s3t09/technicality/R4: 1546759138
    s3t09/random/R1: 8003320
    s3t09/random/R1-M: 1636144590
    s3t09/random/R2: 798042328
    s3t09/random/R3: 2000986160
    s3t09/random/R4: 1949983145
    s3t10/unsteered/R1: 540455468
    s3t10/unsteered/R1-M: 1102780033
    s3t10/unsteered/R2: 1983918024
    s3t10/unsteered/R3: 36539931
    s3t10/unsteered/R4: 2012777898
    s3t10/hostility/R1: 163213100
    s3t10/hostility/R1-M: 1973072142
    s3t10/hostility/R2: 717666007
    s3t10/hostility/R3: 429511623
    s3t10/hostility/R4: 1653941274
    s3t10/technicality/R1: 47563437
    s3t10/technicality/R1-M: 1289370107
    s3t10/technicality/R2: 983075749
    s3t10/technicality/R3: 407730544
    s3t10/technicality/R4: 1718293883
    s3t10/random/R1: 2139050006
    s3t10/random/R1-M: 688068609
    s3t10/random/R2: 296530532
    s3t10/random/R3: 965374548
    s3t10/random/R4: 2132992410
    s3t11/unsteered/R1: 332336760
    s3t11/unsteered/R1-M: 85558841
    s3t11/unsteered/R2: 1753146566
    s3t11/unsteered/R3: 339143464
    s3t11/unsteered/R4: 1430937727
    s3t11/hostility/R1: 572753549
    s3t11/hostility/R1-M: 513428705
    s3t11/hostility/R2: 679637507
    s3t11/hostility/R3: 298777969
    s3t11/hostility/R4: 1383133843
    s3t11/technicality/R1: 656194845
    s3t11/technicality/R1-M: 983995389
    s3t11/technicality/R2: 1428762458
    s3t11/technicality/R3: 135140863
    s3t11/technicality/R4: 1894813265
    s3t11/random/R1: 61809720
    s3t11/random/R1-M: 553293098
    s3t11/random/R2: 422008848
    s3t11/random/R3: 1049019169
    s3t11/random/R4: 446268266
    s3t12/unsteered/R1: 1519147030
    s3t12/unsteered/R1-M: 1511388827
    s3t12/unsteered/R2: 1340934902
    s3t12/unsteered/R3: 2146422458
    s3t12/unsteered/R4: 1218441496
    s3t12/hostility/R1: 2125303750
    s3t12/hostility/R1-M: 192019250
    s3t12/hostility/R2: 1351263964
    s3t12/hostility/R3: 912643435
    s3t12/hostility/R4: 1173372399
    s3t12/technicality/R1: 1989926317
    s3t12/technicality/R1-M: 791408780
    s3t12/technicality/R2: 2105213910
    s3t12/technicality/R3: 1021890262
    s3t12/technicality/R4: 2005513077
    s3t12/random/R1: 1482877028
    s3t12/random/R1-M: 1055684649
    s3t12/random/R2: 730683730
    s3t12/random/R3: 759178386
    s3t12/random/R4: 625607286
    s3t13/unsteered/R1: 1346029755
    s3t13/unsteered/R1-M: 1153460170
    s3t13/unsteered/R2: 99943676
    s3t13/unsteered/R3: 1059574314
    s3t13/unsteered/R4: 1618336994
    s3t13/hostility/R1: 856194734
    s3t13/hostility/R1-M: 328658295
    s3t13/hostility/R2: 657974466
    s3t13/hostility/R3: 1446922063
    s3t13/hostility/R4: 1735927407
    s3t13/technicality/R1: 1951623440
    s3t13/technicality/R1-M: 965511430
    s3t13/technicality/R2: 226041585
    s3t13/technicality/R3: 1549119019
    s3t13/technicality/R4: 723738276
    s3t13/random/R1: 99867956
    s3t13/random/R1-M: 1123803815
    s3t13/random/R2: 1740281105
    s3t13/random/R3: 641489515
    s3t13/random/R4: 81073456
    s3t14/unsteered/R1: 1574454186
    s3t14/unsteered/R1-M: 1191388206
    s3t14/unsteered/R2: 1356382242
    s3t14/unsteered/R3: 1326682247
    s3t14/unsteered/R4: 1896612976
    s3t14/hostility/R1: 1682907062
    s3t14/hostility/R1-M: 1548019397
    s3t14/hostility/R2: 10568594
    s3t14/hostility/R3: 711242643
    s3t14/hostility/R4: 475353377
    s3t14/technicality/R1: 1757451104
    s3t14/technicality/R1-M: 497722245
    s3t14/technicality/R2: 506959565
    s3t14/technicality/R3: 179636938
    s3t14/technicality/R4: 131917853
    s3t14/random/R1: 1743627453
    s3t14/random/R1-M: 104710106
    s3t14/random/R2: 875707171
    s3t14/random/R3: 2033044267
    s3t14/random/R4: 705295372
    s3t15/unsteered/R1: 346578374
    s3t15/unsteered/R1-M: 2017910871
    s3t15/unsteered/R2: 1455926380
    s3t15/unsteered/R3: 1938128149
    s3t15/unsteered/R4: 1425683020
    s3t15/hostility/R1: 1241904304
    s3t15/hostility/R1-M: 1130596300
    s3t15/hostility/R2: 1696347885
    s3t15/hostility/R3: 1955295902
    s3t15/hostility/R4: 1854706676
    s3t15/technicality/R1: 13267782
    s3t15/technicality/R1-M: 95747439
    s3t15/technicality/R2: 10204228
    s3t15/technicality/R3: 423714807
    s3t15/technicality/R4: 1783126545
    s3t15/random/R1: 1964398389
    s3t15/random/R1-M: 1323299679
    s3t15/random/R2: 1506708503
    s3t15/random/R3: 519437319
    s3t15/random/R4: 242243469
    s3t16/unsteered/R1: 1807485085
    s3t16/unsteered/R1-M: 2025895420
    s3t16/unsteered/R2: 741701479
    s3t16/unsteered/R3: 968903681
    s3t16/unsteered/R4: 977318109
    s3t16/hostility/R1: 313728682
    s3t16/hostility/R1-M: 409904896
    s3t16/hostility/R2: 1956584915
    s3t16/hostility/R3: 1322225831
    s3t16/hostility/R4: 348831170
    s3t16/technicality/R1: 1673526725
    s3t16/technicality/R1-M: 1572469504
    s3t16/technicality/R2: 195087512
    s3t16/technicality/R3: 1042059813
    s3t16/technicality/R4: 977616059
    s3t16/random/R1: 417595871
    s3t16/random/R1-M: 385550083
    s3t16/random/R2: 1720877946
    s3t16/random/R3: 1112466015
    s3t16/random/R4: 1677277504
    s3t17/unsteered/R1: 1726549218
    s3t17/unsteered/R1-M: 1520594418
    s3t17/unsteered/R2: 911226051
    s3t17/unsteered/R3: 1182298398
    s3t17/unsteered/R4: 627271523
    s3t17/hostility/R1: 452582613
    s3t17/hostility/R1-M: 1242194492
    s3t17/hostility/R2: 469786820
    s3t17/hostility/R3: 291579097
    s3t17/hostility/R4: 227554067
    s3t17/technicality/R1: 211568476
    s3t17/technicality/R1-M: 1109279009
    s3t17/technicality/R2: 683467083
    s3t17/technicality/R3: 604250088
    s3t17/technicality/R4: 37426622
    s3t17/random/R1: 790468750
    s3t17/random/R1-M: 1700099421
    s3t17/random/R2: 238712954
    s3t17/random/R3: 1325885104
    s3t17/random/R4: 1240946334
    s3t18/unsteered/R1: 261923760
    s3t18/unsteered/R1-M: 539845722
    s3t18/unsteered/R2: 1397369590
    s3t18/unsteered/R3: 861926600
    s3t18/unsteered/R4: 1857609995
    s3t18/hostility/R1: 1925351196
    s3t18/hostility/R1-M: 285049171
    s3t18/hostility/R2: 1173540062
    s3t18/hostility/R3: 389006435
    s3t18/hostility/R4: 332154201
    s3t18/technicality/R1: 1799049138
    s3t18/technicality/R1-M: 1858160415
    s3t18/technicality/R2: 1290816100
    s3t18/technicality/R3: 1796358112
    s3t18/technicality/R4: 1054305083
    s3t18/random/R1: 1166913996
    s3t18/random/R1-M: 1691299766
    s3t18/random/R2: 1099151076
    s3t18/random/R3: 1012616484
    s3t18/random/R4: 1547146261
    s3t19/unsteered/R1: 216877349
    s3t19/unsteered/R1-M: 548306752
    s3t19/unsteered/R2: 39787627
    s3t19/unsteered/R3: 1656990343
    s3t19/unsteered/R4: 774284082
    s3t19/hostility/R1: 1478690274
    s3t19/hostility/R1-M: 1131580826
    s3t19/hostility/R2: 148744489
    s3t19/hostility/R3: 989633290
    s3t19/hostility/R4: 1484195913
    s3t19/technicality/R1: 356918346
    s3t19/technicality/R1-M: 1265483879
    s3t19/technicality/R2: 769901086
    s3t19/technicality/R3: 1877183837
    s3t19/technicality/R4: 688408515
    s3t19/random/R1: 1381053471
    s3t19/random/R1-M: 1884385053
    s3t19/random/R2: 528489802
    s3t19/random/R3: 1975908368
    s3t19/random/R4: 835095610
    s3t20/unsteered/R1: 1213437883
    s3t20/unsteered/R1-M: 1255938167
    s3t20/unsteered/R2: 1244937900
    s3t20/unsteered/R3: 1741039560
    s3t20/unsteered/R4: 16955042
    s3t20/hostility/R1: 203417124
    s3t20/hostility/R1-M: 462848178
    s3t20/hostility/R2: 1158611616
    s3t20/hostility/R3: 399048870
    s3t20/hostility/R4: 1657780063
    s3t20/technicality/R1: 289359263
    s3t20/technicality/R1-M: 458440112
    s3t20/technicality/R2: 760131691
    s3t20/technicality/R3: 228346754
    s3t20/technicality/R4: 1973658996
    s3t20/random/R1: 1762531337
    s3t20/random/R1-M: 1300958132
    s3t20/random/R2: 1654667965
    s3t20/random/R3: 1993197388
    s3t20/random/R4: 1151349026
    s3t21/unsteered/R1: 451225209
    s3t21/unsteered/R1-M: 1965396784
    s3t21/unsteered/R2: 274932595
    s3t21/unsteered/R3: 2030586879
    s3t21/unsteered/R4: 1922829092
    s3t21/hostility/R1: 123323388
    s3t21/hostility/R1-M: 341745783
    s3t21/hostility/R2: 1069114840
    s3t21/hostility/R3: 1769659148
    s3t21/hostility/R4: 1124853620
    s3t21/technicality/R1: 621919790
    s3t21/technicality/R1-M: 1751563116
    s3t21/technicality/R2: 1579643954
    s3t21/technicality/R3: 1262679481
    s3t21/technicality/R4: 1537644330
    s3t21/random/R1: 747080486
    s3t21/random/R1-M: 1335739394
    s3t21/random/R2: 1169930697
    s3t21/random/R3: 139973692
    s3t21/random/R4: 990203432
    s3t22/unsteered/R1: 1221113471
    s3t22/unsteered/R1-M: 974040620
    s3t22/unsteered/R2: 1744225739
    s3t22/unsteered/R3: 915361555
    s3t22/unsteered/R4: 624391962
    s3t22/hostility/R1: 1404952964
    s3t22/hostility/R1-M: 1506099278
    s3t22/hostility/R2: 374499510
    s3t22/hostility/R3: 1328786860
    s3t22/hostility/R4: 238529475
    s3t22/technicality/R1: 1464838470
    s3t22/technicality/R1-M: 153282094
    s3t22/technicality/R2: 1108807644
    s3t22/technicality/R3: 660958322
    s3t22/technicality/R4: 949397008
    s3t22/random/R1: 1478519897
    s3t22/random/R1-M: 407875238
    s3t22/random/R2: 1283924078
    s3t22/random/R3: 809285986
    s3t22/random/R4: 270534133
    s3t23/unsteered/R1: 316865077
    s3t23/unsteered/R1-M: 511221283
    s3t23/unsteered/R2: 196652696
    s3t23/unsteered/R3: 2020665558
    s3t23/unsteered/R4: 1268246437
    s3t23/hostility/R1: 1852897802
    s3t23/hostility/R1-M: 1700773126
    s3t23/hostility/R2: 749232218
    s3t23/hostility/R3: 421524085
    s3t23/hostility/R4: 1206414763
    s3t23/technicality/R1: 601683037
    s3t23/technicality/R1-M: 455964075
    s3t23/technicality/R2: 820538448
    s3t23/technicality/R3: 440733460
    s3t23/technicality/R4: 2038597945
    s3t23/random/R1: 212414895
    s3t23/random/R1-M: 2138379851
    s3t23/random/R2: 438290462
    s3t23/random/R3: 1212101726
    s3t23/random/R4: 671778640
    s3t24/unsteered/R1: 145320630
    s3t24/unsteered/R1-M: 1822948720
    s3t24/unsteered/R2: 1869645148
    s3t24/unsteered/R3: 1511334669
    s3t24/unsteered/R4: 1535546440
    s3t24/hostility/R1: 1778076340
    s3t24/hostility/R1-M: 501652509
    s3t24/hostility/R2: 131773773
    s3t24/hostility/R3: 383763231
    s3t24/hostility/R4: 507668534
    s3t24/technicality/R1: 2022997397
    s3t24/technicality/R1-M: 1016106215
    s3t24/technicality/R2: 1302769813
    s3t24/technicality/R3: 957878643
    s3t24/technicality/R4: 309578699
    s3t24/random/R1: 1394817021
    s3t24/random/R1-M: 1019206821
    s3t24/random/R2: 1914490090
    s3t24/random/R3: 183637663
    s3t24/random/R4: 270313486
    s3t25/unsteered/R1: 1905712887
    s3t25/unsteered/R1-M: 1614143158
    s3t25/unsteered/R2: 1598411483
    s3t25/unsteered/R3: 891704851
    s3t25/unsteered/R4: 1109737353
    s3t25/hostility/R1: 1798699502
    s3t25/hostility/R1-M: 257929233
    s3t25/hostility/R2: 892562796
    s3t25/hostility/R3: 211928217
    s3t25/hostility/R4: 1487645463
    s3t25/technicality/R1: 1522658185
    s3t25/technicality/R1-M: 1346957919
    s3t25/technicality/R2: 1580451134
    s3t25/technicality/R3: 2095743414
    s3t25/technicality/R4: 1976339866
    s3t25/random/R1: 1485286799
    s3t25/random/R1-M: 1514865474
    s3t25/random/R2: 1364221298
    s3t25/random/R3: 712844863
    s3t25/random/R4: 1515677139
    s3t26/unsteered/R1: 1580165064
    s3t26/unsteered/R1-M: 429848270
    s3t26/unsteered/R2: 1475384116
    s3t26/unsteered/R3: 1021785344
    s3t26/unsteered/R4: 153976106
    s3t26/hostility/R1: 1806209531
    s3t26/hostility/R1-M: 1285851457
    s3t26/hostility/R2: 1060754933
    s3t26/hostility/R3: 1941404415
    s3t26/hostility/R4: 1097860483
    s3t26/technicality/R1: 1836013735
    s3t26/technicality/R1-M: 1615564339
    s3t26/technicality/R2: 1605556945
    s3t26/technicality/R3: 916625485
    s3t26/technicality/R4: 1082476608
    s3t26/random/R1: 1278079218
    s3t26/random/R1-M: 147150728
    s3t26/random/R2: 134448158
    s3t26/random/R3: 1123105532
    s3t26/random/R4: 1018730992
    s3t27/unsteered/R1: 1455998187
    s3t27/unsteered/R1-M: 1941505192
    s3t27/unsteered/R2: 950240798
    s3t27/unsteered/R3: 1311839581
    s3t27/unsteered/R4: 1846410773
    s3t27/hostility/R1: 1254661746
    s3t27/hostility/R1-M: 1913264188
    s3t27/hostility/R2: 2079660572
    s3t27/hostility/R3: 1661405634
    s3t27/hostility/R4: 364296598
    s3t27/technicality/R1: 988142376
    s3t27/technicality/R1-M: 459054327
    s3t27/technicality/R2: 2092292860
    s3t27/technicality/R3: 1228585611
    s3t27/technicality/R4: 1652603222
    s3t27/random/R1: 251063849
    s3t27/random/R1-M: 1274382301
    s3t27/random/R2: 1528985148
    s3t27/random/R3: 1041206734
    s3t27/random/R4: 828425295
    s3t28/unsteered/R1: 1774672836
    s3t28/unsteered/R1-M: 480756231
    s3t28/unsteered/R2: 1790280305
    s3t28/unsteered/R3: 658859518
    s3t28/unsteered/R4: 1273356503
    s3t28/hostility/R1: 1936721974
    s3t28/hostility/R1-M: 1126279714
    s3t28/hostility/R2: 163001967
    s3t28/hostility/R3: 1499112268
    s3t28/hostility/R4: 1995784520
    s3t28/technicality/R1: 1744575307
    s3t28/technicality/R1-M: 1620453744
    s3t28/technicality/R2: 445936215
    s3t28/technicality/R3: 1049870004
    s3t28/technicality/R4: 1944773268
    s3t28/random/R1: 1155565651
    s3t28/random/R1-M: 1734562618
    s3t28/random/R2: 292818339
    s3t28/random/R3: 344030078
    s3t28/random/R4: 368576522
    s3t29/unsteered/R1: 182365837
    s3t29/unsteered/R1-M: 683326109
    s3t29/unsteered/R2: 1950259494
    s3t29/unsteered/R3: 1254644393
    s3t29/unsteered/R4: 535178094
    s3t29/hostility/R1: 1452282399
    s3t29/hostility/R1-M: 2124129414
    s3t29/hostility/R2: 2071888640
    s3t29/hostility/R3: 2145684075
    s3t29/hostility/R4: 530219319
    s3t29/technicality/R1: 1155669324
    s3t29/technicality/R1-M: 2082124557
    s3t29/technicality/R2: 1989198360
    s3t29/technicality/R3: 306824924
    s3t29/technicality/R4: 87553384
    s3t29/random/R1: 109421667
    s3t29/random/R1-M: 1682377191
    s3t29/random/R2: 835449737
    s3t29/random/R3: 2006915960
    s3t29/random/R4: 1586548055
    s3t30/unsteered/R1: 293830012
    s3t30/unsteered/R1-M: 309936855
    s3t30/unsteered/R2: 1721354458
    s3t30/unsteered/R3: 696287316
    s3t30/unsteered/R4: 1806135368
    s3t30/hostility/R1: 748316388
    s3t30/hostility/R1-M: 1759171227
    s3t30/hostility/R2: 1729220345
    s3t30/hostility/R3: 1506153390
    s3t30/hostility/R4: 321281043
    s3t30/technicality/R1: 1738891396
    s3t30/technicality/R1-M: 910887570
    s3t30/technicality/R2: 1737585532
    s3t30/technicality/R3: 1124859180
    s3t30/technicality/R4: 2144548538
    s3t30/random/R1: 773702169
    s3t30/random/R1-M: 763156718
    s3t30/random/R2: 1239459474
    s3t30/random/R3: 702042298
    s3t30/random/R4: 1422485297
    s3t31/unsteered/R1: 2075213463
    s3t31/unsteered/R1-M: 1520891155
    s3t31/unsteered/R2: 1918110795
    s3t31/unsteered/R3: 996456613
    s3t31/unsteered/R4: 109580241
    s3t31/hostility/R1: 1880775111
    s3t31/hostility/R1-M: 1877034137
    s3t31/hostility/R2: 1601886873
    s3t31/hostility/R3: 2060416346
    s3t31/hostility/R4: 548599482
    s3t31/technicality/R1: 496782665
    s3t31/technicality/R1-M: 1427727926
    s3t31/technicality/R2: 1324328428
    s3t31/technicality/R3: 1452361298
    s3t31/technicality/R4: 1480804987
    s3t31/random/R1: 1821889803
    s3t31/random/R1-M: 1696881683
    s3t31/random/R2: 481092654
    s3t31/random/R3: 914841227
    s3t31/random/R4: 898599218
    s3t32/unsteered/R1: 1201500369
    s3t32/unsteered/R1-M: 1981205118
    s3t32/unsteered/R2: 191599631
    s3t32/unsteered/R3: 2029079490
    s3t32/unsteered/R4: 1113235562
    s3t32/hostility/R1: 1409116623
    s3t32/hostility/R1-M: 1461503182
    s3t32/hostility/R2: 1385831694
    s3t32/hostility/R3: 309159399
    s3t32/hostility/R4: 1794514857
    s3t32/technicality/R1: 1935587063
    s3t32/technicality/R1-M: 551585127
    s3t32/technicality/R2: 1682142969
    s3t32/technicality/R3: 1677698896
    s3t32/technicality/R4: 1817735307
    s3t32/random/R1: 569168985
    s3t32/random/R1-M: 615389030
    s3t32/random/R2: 1394292194
    s3t32/random/R3: 477634098
    s3t32/random/R4: 1767922769
    s3t33/unsteered/R1: 1339119084
    s3t33/unsteered/R1-M: 244830147
    s3t33/unsteered/R2: 1274758333
    s3t33/unsteered/R3: 1717946422
    s3t33/unsteered/R4: 1119053532
    s3t33/hostility/R1: 1124948475
    s3t33/hostility/R1-M: 1525331257
    s3t33/hostility/R2: 1703537929
    s3t33/hostility/R3: 1094561727
    s3t33/hostility/R4: 1285022076
    s3t33/technicality/R1: 2029530302
    s3t33/technicality/R1-M: 1589874518
    s3t33/technicality/R2: 1383721761
    s3t33/technicality/R3: 397537111
    s3t33/technicality/R4: 18075422
    s3t33/random/R1: 795088026
    s3t33/random/R1-M: 557821443
    s3t33/random/R2: 1885267383
    s3t33/random/R3: 2081896974
    s3t33/random/R4: 1930018065
    s3t34/unsteered/R1: 1397872387
    s3t34/unsteered/R1-M: 1677354028
    s3t34/unsteered/R2: 1434888725
    s3t34/unsteered/R3: 1954929055
    s3t34/unsteered/R4: 349405536
    s3t34/hostility/R1: 81231480
    s3t34/hostility/R1-M: 350126192
    s3t34/hostility/R2: 490291788
    s3t34/hostility/R3: 252275108
    s3t34/hostility/R4: 2144226327
    s3t34/technicality/R1: 477874906
    s3t34/technicality/R1-M: 285985311
    s3t34/technicality/R2: 1982152210
    s3t34/technicality/R3: 963154152
    s3t34/technicality/R4: 2046661747
    s3t34/random/R1: 556038579
    s3t34/random/R1-M: 998457587
    s3t34/random/R2: 920890925
    s3t34/random/R3: 377722321
    s3t34/random/R4: 2086235762
    s3t35/unsteered/R1: 1613314697
    s3t35/unsteered/R1-M: 1475010980
    s3t35/unsteered/R2: 1312821054
    s3t35/unsteered/R3: 2071888170
    s3t35/unsteered/R4: 553308407
    s3t35/hostility/R1: 240673277
    s3t35/hostility/R1-M: 1361410609
    s3t35/hostility/R2: 415638690
    s3t35/hostility/R3: 1502693761
    s3t35/hostility/R4: 438071228
    s3t35/technicality/R1: 70151552
    s3t35/technicality/R1-M: 1629748914
    s3t35/technicality/R2: 2076931987
    s3t35/technicality/R3: 864277666
    s3t35/technicality/R4: 576681217
    s3t35/random/R1: 1917417868
    s3t35/random/R1-M: 1028206741
    s3t35/random/R2: 1902217913
    s3t35/random/R3: 923241957
    s3t35/random/R4: 1695576490
    s3t36/unsteered/R1: 412689512
    s3t36/unsteered/R1-M: 931714002
    s3t36/unsteered/R2: 745284831
    s3t36/unsteered/R3: 1465406144
    s3t36/unsteered/R4: 1967167652
    s3t36/hostility/R1: 242114624
    s3t36/hostility/R1-M: 672002815
    s3t36/hostility/R2: 1814862128
    s3t36/hostility/R3: 1312278456
    s3t36/hostility/R4: 532240294
    s3t36/technicality/R1: 1139330639
    s3t36/technicality/R1-M: 193180803
    s3t36/technicality/R2: 431888081
    s3t36/technicality/R3: 486847045
    s3t36/technicality/R4: 1561867980
    s3t36/random/R1: 1462998501
    s3t36/random/R1-M: 1746374786
    s3t36/random/R2: 344658514
    s3t36/random/R3: 1118292543
    s3t36/random/R4: 472262785
    s3t37/unsteered/R1: 208340335
    s3t37/unsteered/R1-M: 503196804
    s3t37/unsteered/R2: 2131266020
    s3t37/unsteered/R3: 1889792025
    s3t37/unsteered/R4: 603546906
    s3t37/hostility/R1: 758119020
    s3t37/hostility/R1-M: 2141310338
    s3t37/hostility/R2: 1578788769
    s3t37/hostility/R3: 1887364831
    s3t37/hostility/R4: 1342584503
    s3t37/technicality/R1: 1218474220
    s3t37/technicality/R1-M: 788965524
    s3t37/technicality/R2: 652555228
    s3t37/technicality/R3: 1204354514
    s3t37/technicality/R4: 1184337961
    s3t37/random/R1: 953378944
    s3t37/random/R1-M: 706800016
    s3t37/random/R2: 1788827805
    s3t37/random/R3: 2122068384
    s3t37/random/R4: 1879163187
    s3t38/unsteered/R1: 1964200633
    s3t38/unsteered/R1-M: 335869156
    s3t38/unsteered/R2: 2107739545
    s3t38/unsteered/R3: 914616746
    s3t38/unsteered/R4: 108143994
    s3t38/hostility/R1: 695331772
    s3t38/hostility/R1-M: 1464929383
    s3t38/hostility/R2: 815851999
    s3t38/hostility/R3: 191287840
    s3t38/hostility/R4: 1008856205
    s3t38/technicality/R1: 1285708739
    s3t38/technicality/R1-M: 1677633529
    s3t38/technicality/R2: 1150385893
    s3t38/technicality/R3: 215920443
    s3t38/technicality/R4: 784196057
    s3t38/random/R1: 1801620879
    s3t38/random/R1-M: 1172793898
    s3t38/random/R2: 1542649256
    s3t38/random/R3: 727443882
    s3t38/random/R4: 1029322017
    s3t39/unsteered/R1: 1851567318
    s3t39/unsteered/R1-M: 1218723307
    s3t39/unsteered/R2: 1711076123
    s3t39/unsteered/R3: 2007736672
    s3t39/unsteered/R4: 1771783030
    s3t39/hostility/R1: 684056106
    s3t39/hostility/R1-M: 1751947209
    s3t39/hostility/R2: 899050123
    s3t39/hostility/R3: 4934103
    s3t39/hostility/R4: 932717525
    s3t39/technicality/R1: 1240881977
    s3t39/technicality/R1-M: 1147100765
    s3t39/technicality/R2: 336575153
    s3t39/technicality/R3: 1919085582
    s3t39/technicality/R4: 1113436762
    s3t39/random/R1: 1839711328
    s3t39/random/R1-M: 1294890156
    s3t39/random/R2: 1719681686
    s3t39/random/R3: 510951106
    s3t39/random/R4: 6740271
    s3t40/unsteered/R1: 1307582661
    s3t40/unsteered/R1-M: 314424732
    s3t40/unsteered/R2: 1702002545
    s3t40/unsteered/R3: 98706203
    s3t40/unsteered/R4: 1222470982
    s3t40/hostility/R1: 669021214
    s3t40/hostility/R1-M: 883717650
    s3t40/hostility/R2: 342238039
    s3t40/hostility/R3: 1980083733
    s3t40/hostility/R4: 663937378
    s3t40/technicality/R1: 2097853311
    s3t40/technicality/R1-M: 1721124318
    s3t40/technicality/R2: 240412446
    s3t40/technicality/R3: 1897135441
    s3t40/technicality/R4: 1428120298
    s3t40/random/R1: 2120369998
    s3t40/random/R1-M: 133835198
    s3t40/random/R2: 35291680
    s3t40/random/R3: 664555061
    s3t40/random/R4: 1062788610
    s3t41/unsteered/R1: 1853851175
    s3t41/unsteered/R1-M: 1185413987
    s3t41/unsteered/R2: 924318000
    s3t41/unsteered/R3: 1966547667
    s3t41/unsteered/R4: 804309624
    s3t41/hostility/R1: 1157135164
    s3t41/hostility/R1-M: 1370126380
    s3t41/hostility/R2: 1458856213
    s3t41/hostility/R3: 644583768
    s3t41/hostility/R4: 377632339
    s3t41/technicality/R1: 1293019558
    s3t41/technicality/R1-M: 295669807
    s3t41/technicality/R2: 1509676415
    s3t41/technicality/R3: 1921690095
    s3t41/technicality/R4: 2135698719
    s3t41/random/R1: 257151037
    s3t41/random/R1-M: 1810318253
    s3t41/random/R2: 1635481022
    s3t41/random/R3: 1146504219
    s3t41/random/R4: 2023653280
    s3t42/unsteered/R1: 723849926
    s3t42/unsteered/R1-M: 174253928
    s3t42/unsteered/R2: 440834494
    s3t42/unsteered/R3: 1140930288
    s3t42/unsteered/R4: 1774899633
    s3t42/hostility/R1: 1747799560
    s3t42/hostility/R1-M: 1393319326
    s3t42/hostility/R2: 1205523552
    s3t42/hostility/R3: 332382194
    s3t42/hostility/R4: 1783481316
    s3t42/technicality/R1: 1558140576
    s3t42/technicality/R1-M: 1056646518
    s3t42/technicality/R2: 1224277793
    s3t42/technicality/R3: 1205454171
    s3t42/technicality/R4: 29165129
    s3t42/random/R1: 1405000152
    s3t42/random/R1-M: 1551713930
    s3t42/random/R2: 1011784734
    s3t42/random/R3: 906539661
    s3t42/random/R4: 1671365513
    s3t43/unsteered/R1: 1645657212
    s3t43/unsteered/R1-M: 2067658496
    s3t43/unsteered/R2: 2075743386
    s3t43/unsteered/R3: 967118191
    s3t43/unsteered/R4: 1875258810
    s3t43/hostility/R1: 283714303
    s3t43/hostility/R1-M: 1332026239
    s3t43/hostility/R2: 1483532589
    s3t43/hostility/R3: 1496194075
    s3t43/hostility/R4: 1533683604
    s3t43/technicality/R1: 1848490008
    s3t43/technicality/R1-M: 859813498
    s3t43/technicality/R2: 907080889
    s3t43/technicality/R3: 601979346
    s3t43/technicality/R4: 369942595
    s3t43/random/R1: 1980620166
    s3t43/random/R1-M: 1202110217
    s3t43/random/R2: 988452212
    s3t43/random/R3: 1609760931
    s3t43/random/R4: 383982075
    s3t44/unsteered/R1: 246308451
    s3t44/unsteered/R1-M: 221268632
    s3t44/unsteered/R2: 395639910
    s3t44/unsteered/R3: 1152642382
    s3t44/unsteered/R4: 613087594
    s3t44/hostility/R1: 42438534
    s3t44/hostility/R1-M: 1391000330
    s3t44/hostility/R2: 312102711
    s3t44/hostility/R3: 479050456
    s3t44/hostility/R4: 1592077319
    s3t44/technicality/R1: 1275970369
    s3t44/technicality/R1-M: 118172177
    s3t44/technicality/R2: 1360636013
    s3t44/technicality/R3: 106329578
    s3t44/technicality/R4: 2126438802
    s3t44/random/R1: 1442498974
    s3t44/random/R1-M: 1790438285
    s3t44/random/R2: 1928604863
    s3t44/random/R3: 970500070
    s3t44/random/R4: 845664258
    s3t45/unsteered/R1: 1876532842
    s3t45/unsteered/R1-M: 247581976
    s3t45/unsteered/R2: 1079041418
    s3t45/unsteered/R3: 1692856348
    s3t45/unsteered/R4: 1260910343
    s3t45/hostility/R1: 1073484927
    s3t45/hostility/R1-M: 619547437
    s3t45/hostility/R2: 911183333
    s3t45/hostility/R3: 594018920
    s3t45/hostility/R4: 1430695075
    s3t45/technicality/R1: 1598498424
    s3t45/technicality/R1-M: 483845684
    s3t45/technicality/R2: 792149869
    s3t45/technicality/R3: 1132795558
    s3t45/technicality/R4: 455056243
    s3t45/random/R1: 1250923255
    s3t45/random/R1-M: 1749148951
    s3t45/random/R2: 720497416
    s3t45/random/R3: 521403222
    s3t45/random/R4: 1099215252
    s3t46/unsteered/R1: 937114487
    s3t46/unsteered/R1-M: 814912945
    s3t46/unsteered/R2: 1974040318
    s3t46/unsteered/R3: 1968921576
    s3t46/unsteered/R4: 643487525
    s3t46/hostility/R1: 2077631473
    s3t46/hostility/R1-M: 722999542
    s3t46/hostility/R2: 221096999
    s3t46/hostility/R3: 794750241
    s3t46/hostility/R4: 899467873
    s3t46/technicality/R1: 1009700744
    s3t46/technicality/R1-M: 894108499
    s3t46/technicality/R2: 1921321949
    s3t46/technicality/R3: 1279953421
    s3t46/technicality/R4: 1237651219
    s3t46/random/R1: 768015581
    s3t46/random/R1-M: 1886546609
    s3t46/random/R2: 182135743
    s3t46/random/R3: 1669208242
    s3t46/random/R4: 2095533409
    s3t47/unsteered/R1: 1123519067
    s3t47/unsteered/R1-M: 1196361591
    s3t47/unsteered/R2: 1744905722
    s3t47/unsteered/R3: 1848614930
    s3t47/unsteered/R4: 972918983
    s3t47/hostility/R1: 277096484
    s3t47/hostility/R1-M: 170483749
    s3t47/hostility/R2: 302960496
    s3t47/hostility/R3: 2144273043
    s3t47/hostility/R4: 663142704
    s3t47/technicality/R1: 851651443
    s3t47/technicality/R1-M: 1871743091
    s3t47/technicality/R2: 1352902120
    s3t47/technicality/R3: 1103402119
    s3t47/technicality/R4: 240452579
    s3t47/random/R1: 1478381387
    s3t47/random/R1-M: 9191617
    s3t47/random/R2: 850424047
    s3t47/random/R3: 974069647
    s3t47/random/R4: 447430017
    s3t48/unsteered/R1: 1359844901
    s3t48/unsteered/R1-M: 1051421385
    s3t48/unsteered/R2: 808869962
    s3t48/unsteered/R3: 727943963
    s3t48/unsteered/R4: 781663134
    s3t48/hostility/R1: 466530038
    s3t48/hostility/R1-M: 200650822
    s3t48/hostility/R2: 550694969
    s3t48/hostility/R3: 1743049650
    s3t48/hostility/R4: 1505576381
    s3t48/technicality/R1: 1771078437
    s3t48/technicality/R1-M: 1088163333
    s3t48/technicality/R2: 785894382
    s3t48/technicality/R3: 1106772182
    s3t48/technicality/R4: 960463609
    s3t48/random/R1: 1524967593
    s3t48/random/R1-M: 812609303
    s3t48/random/R2: 1314935254
    s3t48/random/R3: 671221262
    s3t48/random/R4: 1008868861
    s3t49/unsteered/R1: 1300419738
    s3t49/unsteered/R1-M: 1466267107
    s3t49/unsteered/R2: 449218472
    s3t49/unsteered/R3: 1379411266
    s3t49/unsteered/R4: 279412732
    s3t49/hostility/R1: 2016420096
    s3t49/hostility/R1-M: 710886622
    s3t49/hostility/R2: 1377017731
    s3t49/hostility/R3: 252325890
    s3t49/hostility/R4: 1707579007
    s3t49/technicality/R1: 1688123714
    s3t49/technicality/R1-M: 964386039
    s3t49/technicality/R2: 1393577527
    s3t49/technicality/R3: 850386803
    s3t49/technicality/R4: 667932325
    s3t49/random/R1: 1455241755
    s3t49/random/R1-M: 763699222
    s3t49/random/R2: 1735436976
    s3t49/random/R3: 593143975
    s3t49/random/R4: 103930969
    s3t50/unsteered/R1: 1623401190
    s3t50/unsteered/R1-M: 72291070
    s3t50/unsteered/R2: 694812702
    s3t50/unsteered/R3: 306615073
    s3t50/unsteered/R4: 283059730
    s3t50/hostility/R1: 1265875851
    s3t50/hostility/R1-M: 801257021
    s3t50/hostility/R2: 244681822
    s3t50/hostility/R3: 112724816
    s3t50/hostility/R4: 2010756227
    s3t50/technicality/R1: 1476737270
    s3t50/technicality/R1-M: 1904292189
    s3t50/technicality/R2: 513961632
    s3t50/technicality/R3: 1831104854
    s3t50/technicality/R4: 116141241
    s3t50/random/R1: 692877834
    s3t50/random/R1-M: 154044205
    s3t50/random/R2: 1653144324
    s3t50/random/R3: 1130446623
    s3t50/random/R4: 1336980885
    s3t51/unsteered/R1: 1470684566
    s3t51/unsteered/R1-M: 1409584932
    s3t51/unsteered/R2: 1394817884
    s3t51/unsteered/R3: 48750894
    s3t51/unsteered/R4: 715712994
    s3t51/hostility/R1: 1270138831
    s3t51/hostility/R1-M: 1451181259
    s3t51/hostility/R2: 1923591794
    s3t51/hostility/R3: 1101815180
    s3t51/hostility/R4: 46735593
    s3t51/technicality/R1: 371849182
    s3t51/technicality/R1-M: 1270304253
    s3t51/technicality/R2: 101709965
    s3t51/technicality/R3: 1380499156
    s3t51/technicality/R4: 1526140617
    s3t51/random/R1: 2018141408
    s3t51/random/R1-M: 1960450056
    s3t51/random/R2: 1554385047
    s3t51/random/R3: 1161193564
    s3t51/random/R4: 1165680673
    s3t52/unsteered/R1: 857010923
    s3t52/unsteered/R1-M: 781425396
    s3t52/unsteered/R2: 927053108
    s3t52/unsteered/R3: 1720594080
    s3t52/unsteered/R4: 418305512
    s3t52/hostility/R1: 193847220
    s3t52/hostility/R1-M: 1045606538
    s3t52/hostility/R2: 234634434
    s3t52/hostility/R3: 626089014
    s3t52/hostility/R4: 687122033
    s3t52/technicality/R1: 1128498493
    s3t52/technicality/R1-M: 522357867
    s3t52/technicality/R2: 167822429
    s3t52/technicality/R3: 1123051340
    s3t52/technicality/R4: 113655746
    s3t52/random/R1: 1914272448
    s3t52/random/R1-M: 884640138
    s3t52/random/R2: 758367838
    s3t52/random/R3: 178830546
    s3t52/random/R4: 843834660
    s3t53/unsteered/R1: 718143070
    s3t53/unsteered/R1-M: 1619112498
    s3t53/unsteered/R2: 1183001770
    s3t53/unsteered/R3: 694276643
    s3t53/unsteered/R4: 1503600654
    s3t53/hostility/R1: 1009841700
    s3t53/hostility/R1-M: 160309036
    s3t53/hostility/R2: 1761552242
    s3t53/hostility/R3: 922484403
    s3t53/hostility/R4: 591105868
    s3t53/technicality/R1: 691654493
    s3t53/technicality/R1-M: 1659484966
    s3t53/technicality/R2: 1311442374
    s3t53/technicality/R3: 1282526455
    s3t53/technicality/R4: 1678446682
    s3t53/random/R1: 1375283005
    s3t53/random/R1-M: 752486685
    s3t53/random/R2: 1933850050
    s3t53/random/R3: 1815269235
    s3t53/random/R4: 1396819016
    s3t54/unsteered/R1: 1224436050
    s3t54/unsteered/R1-M: 507897930
    s3t54/unsteered/R2: 1419820956
    s3t54/unsteered/R3: 227284441
    s3t54/unsteered/R4: 901340479
    s3t54/hostility/R1: 208770771
    s3t54/hostility/R1-M: 1838978853
    s3t54/hostility/R2: 1796945222
    s3t54/hostility/R3: 1744086278
    s3t54/hostility/R4: 1939077382
    s3t54/technicality/R1: 1824630081
    s3t54/technicality/R1-M: 900198261
    s3t54/technicality/R2: 1864912229
    s3t54/technicality/R3: 165242548
    s3t54/technicality/R4: 187277322
    s3t54/random/R1: 1728225601
    s3t54/random/R1-M: 1884448006
    s3t54/random/R2: 1562279038
    s3t54/random/R3: 1938246911
    s3t54/random/R4: 1475134440
    s3t55/unsteered/R1: 2093230817
    s3t55/unsteered/R1-M: 1527020621
    s3t55/unsteered/R2: 1866225226
    s3t55/unsteered/R3: 266982025
    s3t55/unsteered/R4: 375281471
    s3t55/hostility/R1: 1031980198
    s3t55/hostility/R1-M: 401799845
    s3t55/hostility/R2: 571268630
    s3t55/hostility/R3: 296627571
    s3t55/hostility/R4: 725809203
    s3t55/technicality/R1: 1946333553
    s3t55/technicality/R1-M: 1212749079
    s3t55/technicality/R2: 1422041869
    s3t55/technicality/R3: 1063900901
    s3t55/technicality/R4: 2079692301
    s3t55/random/R1: 1898907659
    s3t55/random/R1-M: 1592103534
    s3t55/random/R2: 2067928543
    s3t55/random/R3: 811022614
    s3t55/random/R4: 643556459
    s3t56/unsteered/R1: 1422014340
    s3t56/unsteered/R1-M: 6597805
    s3t56/unsteered/R2: 1601485934
    s3t56/unsteered/R3: 629301814
    s3t56/unsteered/R4: 230132681
    s3t56/hostility/R1: 1842525961
    s3t56/hostility/R1-M: 973319103
    s3t56/hostility/R2: 1253057849
    s3t56/hostility/R3: 1435317810
    s3t56/hostility/R4: 1016785129
    s3t56/technicality/R1: 196678642
    s3t56/technicality/R1-M: 498949490
    s3t56/technicality/R2: 913497026
    s3t56/technicality/R3: 1902189985
    s3t56/technicality/R4: 1765053370
    s3t56/random/R1: 418672217
    s3t56/random/R1-M: 1295190091
    s3t56/random/R2: 1633025625
    s3t56/random/R3: 1538535461
    s3t56/random/R4: 310782681
    s3t57/unsteered/R1: 157867814
    s3t57/unsteered/R1-M: 178734700
    s3t57/unsteered/R2: 727035101
    s3t57/unsteered/R3: 2118709813
    s3t57/unsteered/R4: 289164
    s3t57/hostility/R1: 1128381449
    s3t57/hostility/R1-M: 978976595
    s3t57/hostility/R2: 486299953
    s3t57/hostility/R3: 1540178300
    s3t57/hostility/R4: 1772896527
    s3t57/technicality/R1: 1418500113
    s3t57/technicality/R1-M: 329516636
    s3t57/technicality/R2: 683826901
    s3t57/technicality/R3: 1433447581
    s3t57/technicality/R4: 1812790839
    s3t57/random/R1: 2081680945
    s3t57/random/R1-M: 471299440
    s3t57/random/R2: 1621346122
    s3t57/random/R3: 1116870094
    s3t57/random/R4: 883264797
    s3t58/unsteered/R1: 34805083
    s3t58/unsteered/R1-M: 1429987973
    s3t58/unsteered/R2: 799306576
    s3t58/unsteered/R3: 1831478415
    s3t58/unsteered/R4: 697150843
    s3t58/hostility/R1: 530117722
    s3t58/hostility/R1-M: 1658199594
    s3t58/hostility/R2: 589029008
    s3t58/hostility/R3: 2008247019
    s3t58/hostility/R4: 1159770456
    s3t58/technicality/R1: 1358519460
    s3t58/technicality/R1-M: 436587385
    s3t58/technicality/R2: 388817660
    s3t58/technicality/R3: 2041306040
    s3t58/technicality/R4: 1560026333
    s3t58/random/R1: 1071478853
    s3t58/random/R1-M: 1787321838
    s3t58/random/R2: 1486907542
    s3t58/random/R3: 2120407681
    s3t58/random/R4: 890863351
    s3t59/unsteered/R1: 630098007
    s3t59/unsteered/R1-M: 799152776
    s3t59/unsteered/R2: 2099380813
    s3t59/unsteered/R3: 483425505
    s3t59/unsteered/R4: 1630885309
    s3t59/hostility/R1: 680657908
    s3t59/hostility/R1-M: 1409380811
    s3t59/hostility/R2: 88593222
    s3t59/hostility/R3: 349376097
    s3t59/hostility/R4: 1541205234
    s3t59/technicality/R1: 707393814
    s3t59/technicality/R1-M: 1931633330
    s3t59/technicality/R2: 1359106151
    s3t59/technicality/R3: 705413864
    s3t59/technicality/R4: 267906627
    s3t59/random/R1: 1649203692
    s3t59/random/R1-M: 1221060511
    s3t59/random/R2: 1751130381
    s3t59/random/R3: 955923790
    s3t59/random/R4: 17199580
    s3t60/unsteered/R1: 351332599
    s3t60/unsteered/R1-M: 1596371527
    s3t60/unsteered/R2: 1425544062
    s3t60/unsteered/R3: 1861975238
    s3t60/unsteered/R4: 1100773285
    s3t60/hostility/R1: 444122294
    s3t60/hostility/R1-M: 637225194
    s3t60/hostility/R2: 1319737775
    s3t60/hostility/R3: 1320569879
    s3t60/hostility/R4: 288706714
    s3t60/technicality/R1: 674666736
    s3t60/technicality/R1-M: 1822668795
    s3t60/technicality/R2: 545291655
    s3t60/technicality/R3: 840856332
    s3t60/technicality/R4: 107470997
    s3t60/random/R1: 1979712497
    s3t60/random/R1-M: 1325432244
    s3t60/random/R2: 1825310378
    s3t60/random/R3: 1188043327
    s3t60/random/R4: 1074381330
    s3t61/unsteered/R1: 2115181596
    s3t61/unsteered/R1-M: 960224370
    s3t61/unsteered/R2: 1666290293
    s3t61/unsteered/R3: 1705832674
    s3t61/unsteered/R4: 1454658842
    s3t61/hostility/R1: 74571964
    s3t61/hostility/R1-M: 1161251233
    s3t61/hostility/R2: 1565014458
    s3t61/hostility/R3: 892363398
    s3t61/hostility/R4: 1033229441
    s3t61/technicality/R1: 332070513
    s3t61/technicality/R1-M: 1435375380
    s3t61/technicality/R2: 733991100
    s3t61/technicality/R3: 1422581575
    s3t61/technicality/R4: 15506307
    s3t61/random/R1: 1257747627
    s3t61/random/R1-M: 2110520396
    s3t61/random/R2: 708206440
    s3t61/random/R3: 591043081
    s3t61/random/R4: 1649659298
    s3t62/unsteered/R1: 1035986551
    s3t62/unsteered/R1-M: 1117210786
    s3t62/unsteered/R2: 1069502097
    s3t62/unsteered/R3: 384866505
    s3t62/unsteered/R4: 1395170405
    s3t62/hostility/R1: 380649422
    s3t62/hostility/R1-M: 13557914
    s3t62/hostility/R2: 695810079
    s3t62/hostility/R3: 928850006
    s3t62/hostility/R4: 1767280040
    s3t62/technicality/R1: 1395067210
    s3t62/technicality/R1-M: 503191884
    s3t62/technicality/R2: 1679370480
    s3t62/technicality/R3: 1983184652
    s3t62/technicality/R4: 13169411
    s3t62/random/R1: 213509481
    s3t62/random/R1-M: 1134408040
    s3t62/random/R2: 185334011
    s3t62/random/R3: 264280071
    s3t62/random/R4: 1793634556
    s3t63/unsteered/R1: 1638298658
    s3t63/unsteered/R1-M: 1198884610
    s3t63/unsteered/R2: 1289518224
    s3t63/unsteered/R3: 1072686449
    s3t63/unsteered/R4: 2045098219
    s3t63/hostility/R1: 1030202246
    s3t63/hostility/R1-M: 49040277
    s3t63/hostility/R2: 1421063169
    s3t63/hostility/R3: 404209652
    s3t63/hostility/R4: 517413837
    s3t63/technicality/R1: 1639580849
    s3t63/technicality/R1-M: 1613970707
    s3t63/technicality/R2: 755031243
    s3t63/technicality/R3: 1884701063
    s3t63/technicality/R4: 778085582
    s3t63/random/R1: 1463057141
    s3t63/random/R1-M: 1670342098
    s3t63/random/R2: 1734777500
    s3t63/random/R3: 2090271341
    s3t63/random/R4: 1409177062
    s3t64/unsteered/R1: 1551396292
    s3t64/unsteered/R1-M: 711360549
    s3t64/unsteered/R2: 201215137
    s3t64/unsteered/R3: 1420150371
    s3t64/unsteered/R4: 789135883
    s3t64/hostility/R1: 722137603
    s3t64/hostility/R1-M: 1041167859
    s3t64/hostility/R2: 1779634134
    s3t64/hostility/R3: 1564368780
    s3t64/hostility/R4: 1582565135
    s3t64/technicality/R1: 1922059265
    s3t64/technicality/R1-M: 503827668
    s3t64/technicality/R2: 262506475
    s3t64/technicality/R3: 817198031
    s3t64/technicality/R4: 469327477
    s3t64/random/R1: 1999476381
    s3t64/random/R1-M: 1573665330
    s3t64/random/R2: 1585428587
    s3t64/random/R3: 93029022
    s3t64/random/R4: 2102342433
    s3t65/unsteered/R1: 1973214771
    s3t65/unsteered/R1-M: 695788265
    s3t65/unsteered/R2: 1507117528
    s3t65/unsteered/R3: 1288419867
    s3t65/unsteered/R4: 1357141754
    s3t65/hostility/R1: 817352024
    s3t65/hostility/R1-M: 1958938751
    s3t65/hostility/R2: 1197741852
    s3t65/hostility/R3: 2045050247
    s3t65/hostility/R4: 694848225
    s3t65/technicality/R1: 1101037594
    s3t65/technicality/R1-M: 426770164
    s3t65/technicality/R2: 1762002658
    s3t65/technicality/R3: 554338320
    s3t65/technicality/R4: 221845278
    s3t65/random/R1: 1233478754
    s3t65/random/R1-M: 1203651799
    s3t65/random/R2: 1082659013
    s3t65/random/R3: 1641770867
    s3t65/random/R4: 1024843792
    s3t66/unsteered/R1: 1258956367
    s3t66/unsteered/R1-M: 353195751
    s3t66/unsteered/R2: 213500118
    s3t66/unsteered/R3: 779228707
    s3t66/unsteered/R4: 1393329442
    s3t66/hostility/R1: 905029780
    s3t66/hostility/R1-M: 32704710
    s3t66/hostility/R2: 397349051
    s3t66/hostility/R3: 135786705
    s3t66/hostility/R4: 1493813658
    s3t66/technicality/R1: 600944735
    s3t66/technicality/R1-M: 2069306722
    s3t66/technicality/R2: 732140482
    s3t66/technicality/R3: 798670573
    s3t66/technicality/R4: 349158634
    s3t66/random/R1: 1921707495
    s3t66/random/R1-M: 528864578
    s3t66/random/R2: 2067665368
    s3t66/random/R3: 1301838278
    s3t66/random/R4: 863033281
    s3t67/unsteered/R1: 315518966
    s3t67/unsteered/R1-M: 829880058
    s3t67/unsteered/R2: 1128329541
    s3t67/unsteered/R3: 888827130
    s3t67/unsteered/R4: 565895547
    s3t67/hostility/R1: 1966957039
    s3t67/hostility/R1-M: 49391589
    s3t67/hostility/R2: 469385846
    s3t67/hostility/R3: 146903051
    s3t67/hostility/R4: 1180123091
    s3t67/technicality/R1: 2011377626
    s3t67/technicality/R1-M: 1488623623
    s3t67/technicality/R2: 663244354
    s3t67/technicality/R3: 843451244
    s3t67/technicality/R4: 174278446
    s3t67/random/R1: 1296378054
    s3t67/random/R1-M: 307801266
    s3t67/random/R2: 1878566062
    s3t67/random/R3: 1432121444
    s3t67/random/R4: 476739888
    s3t68/unsteered/R1: 719586024
    s3t68/unsteered/R1-M: 89253561
    s3t68/unsteered/R2: 231698745
    s3t68/unsteered/R3: 1922249494
    s3t68/unsteered/R4: 1268249053
    s3t68/hostility/R1: 2066373291
    s3t68/hostility/R1-M: 643535093
    s3t68/hostility/R2: 810015450
    s3t68/hostility/R3: 404938635
    s3t68/hostility/R4: 1628220507
    s3t68/technicality/R1: 1983811756
    s3t68/technicality/R1-M: 823160065
    s3t68/technicality/R2: 664895121
    s3t68/technicality/R3: 279051398
    s3t68/technicality/R4: 1158304016
    s3t68/random/R1: 261081682
    s3t68/random/R1-M: 79522826
    s3t68/random/R2: 883821681
    s3t68/random/R3: 759242048
    s3t68/random/R4: 1458000946
    s3t69/unsteered/R1: 776650388
    s3t69/unsteered/R1-M: 605701109
    s3t69/unsteered/R2: 634635221
    s3t69/unsteered/R3: 1763965639
    s3t69/unsteered/R4: 1270305135
    s3t69/hostility/R1: 771319758
    s3t69/hostility/R1-M: 1583165990
    s3t69/hostility/R2: 2112437661
    s3t69/hostility/R3: 54574816
    s3t69/hostility/R4: 956624561
    s3t69/technicality/R1: 914035048
    s3t69/technicality/R1-M: 2067153221
    s3t69/technicality/R2: 2139848344
    s3t69/technicality/R3: 861944994
    s3t69/technicality/R4: 2051134404
    s3t69/random/R1: 867772675
    s3t69/random/R1-M: 1015863040
    s3t69/random/R2: 1507063590
    s3t69/random/R3: 750254205
    s3t69/random/R4: 820274277
    s3t70/unsteered/R1: 784535766
    s3t70/unsteered/R1-M: 1338058118
    s3t70/unsteered/R2: 870079926
    s3t70/unsteered/R3: 1144145027
    s3t70/unsteered/R4: 1528279604
    s3t70/hostility/R1: 935205176
    s3t70/hostility/R1-M: 139450078
    s3t70/hostility/R2: 2047471353
    s3t70/hostility/R3: 1815407260
    s3t70/hostility/R4: 1896930841
    s3t70/technicality/R1: 1234624298
    s3t70/technicality/R1-M: 455309203
    s3t70/technicality/R2: 1491491616
    s3t70/technicality/R3: 1181026500
    s3t70/technicality/R4: 220626301
    s3t70/random/R1: 389714769
    s3t70/random/R1-M: 362468803
    s3t70/random/R2: 1523586877
    s3t70/random/R3: 403750804
    s3t70/random/R4: 1307889353
    s3t71/unsteered/R1: 1598076352
    s3t71/unsteered/R1-M: 2127503613
    s3t71/unsteered/R2: 1298416228
    s3t71/unsteered/R3: 1983939963
    s3t71/unsteered/R4: 1854790344
    s3t71/hostility/R1: 2085200320
    s3t71/hostility/R1-M: 1015795326
    s3t71/hostility/R2: 922822335
    s3t71/hostility/R3: 1434101987
    s3t71/hostility/R4: 1711176798
    s3t71/technicality/R1: 746550771
    s3t71/technicality/R1-M: 479413340
    s3t71/technicality/R2: 1138980723
    s3t71/technicality/R3: 1191264412
    s3t71/technicality/R4: 234772533
    s3t71/random/R1: 2079715689
    s3t71/random/R1-M: 861339843
    s3t71/random/R2: 1559989976
    s3t71/random/R3: 1232396329
    s3t71/random/R4: 103150679
    s3t72/unsteered/R1: 2048926382
    s3t72/unsteered/R1-M: 526324910
    s3t72/unsteered/R2: 1709287966
    s3t72/unsteered/R3: 1891636731
    s3t72/unsteered/R4: 329006091
    s3t72/hostility/R1: 734222606
    s3t72/hostility/R1-M: 1915863288
    s3t72/hostility/R2: 925348655
    s3t72/hostility/R3: 927002344
    s3t72/hostility/R4: 1006690498
    s3t72/technicality/R1: 970470840
    s3t72/technicality/R1-M: 316606515
    s3t72/technicality/R2: 1526097082
    s3t72/technicality/R3: 1017880998
    s3t72/technicality/R4: 1862404553
    s3t72/random/R1: 2136009597
    s3t72/random/R1-M: 1149194775
    s3t72/random/R2: 145152341
    s3t72/random/R3: 1871615491
    s3t72/random/R4: 513308926
    s3t73/unsteered/R1: 1072427964
    s3t73/unsteered/R1-M: 958117101
    s3t73/unsteered/R2: 1309491879
    s3t73/unsteered/R3: 382057006
    s3t73/unsteered/R4: 820465469
    s3t73/hostility/R1: 761469396
    s3t73/hostility/R1-M: 137748419
    s3t73/hostility/R2: 1948026833
    s3t73/hostility/R3: 2001167913
    s3t73/hostility/R4: 1692320226
    s3t73/technicality/R1: 253275051
    s3t73/technicality/R1-M: 1647352541
    s3t73/technicality/R2: 470961916
    s3t73/technicality/R3: 769271277
    s3t73/technicality/R4: 11938215
    s3t73/random/R1: 1489083111
    s3t73/random/R1-M: 2060936156
    s3t73/random/R2: 270493342
    s3t73/random/R3: 1701111995
    s3t73/random/R4: 315157978
    s3t74/unsteered/R1: 1377613209
    s3t74/unsteered/R1-M: 1705689938
    s3t74/unsteered/R2: 1472381460
    s3t74/unsteered/R3: 1032661978
    s3t74/unsteered/R4: 2143675207
    s3t74/hostility/R1: 246523313
    s3t74/hostility/R1-M: 6724883
    s3t74/hostility/R2: 1621259243
    s3t74/hostility/R3: 1612682777
    s3t74/hostility/R4: 1723055234
    s3t74/technicality/R1: 630433036
    s3t74/technicality/R1-M: 1826672920
    s3t74/technicality/R2: 1203794834
    s3t74/technicality/R3: 1194132158
    s3t74/technicality/R4: 1498669149
    s3t74/random/R1: 1038647411
    s3t74/random/R1-M: 444280824
    s3t74/random/R2: 567635870
    s3t74/random/R3: 238114068
    s3t74/random/R4: 1894708775
    s3t75/unsteered/R1: 1690271513
    s3t75/unsteered/R1-M: 1779182763
    s3t75/unsteered/R2: 1312666616
    s3t75/unsteered/R3: 465949414
    s3t75/unsteered/R4: 332521907
    s3t75/hostility/R1: 1150132255
    s3t75/hostility/R1-M: 1805310722
    s3t75/hostility/R2: 1447238697
    s3t75/hostility/R3: 1209444901
    s3t75/hostility/R4: 862054262
    s3t75/technicality/R1: 2070500737
    s3t75/technicality/R1-M: 1405351609
    s3t75/technicality/R2: 1373286568
    s3t75/technicality/R3: 1055692559
    s3t75/technicality/R4: 1346634072
    s3t75/random/R1: 342323121
    s3t75/random/R1-M: 520071624
    s3t75/random/R2: 900392396
    s3t75/random/R3: 46958762
    s3t75/random/R4: 529295561
    s3t76/unsteered/R1: 1743168618
    s3t76/unsteered/R1-M: 204258226
    s3t76/unsteered/R2: 1255573153
    s3t76/unsteered/R3: 1989925637
    s3t76/unsteered/R4: 2062458128
    s3t76/hostility/R1: 810434006
    s3t76/hostility/R1-M: 546088767
    s3t76/hostility/R2: 1598111081
    s3t76/hostility/R3: 1571346922
    s3t76/hostility/R4: 212978108
    s3t76/technicality/R1: 611482686
    s3t76/technicality/R1-M: 2851406
    s3t76/technicality/R2: 217458200
    s3t76/technicality/R3: 413441083
    s3t76/technicality/R4: 783243949
    s3t76/random/R1: 563905783
    s3t76/random/R1-M: 910411917
    s3t76/random/R2: 367241284
    s3t76/random/R3: 1077977772
    s3t76/random/R4: 1871726194
    s3t77/unsteered/R1: 313031960
    s3t77/unsteered/R1-M: 1340081781
    s3t77/unsteered/R2: 1694493700
    s3t77/unsteered/R3: 1184833787
    s3t77/unsteered/R4: 1661934742
    s3t77/hostility/R1: 1331971712
    s3t77/hostility/R1-M: 475750837
    s3t77/hostility/R2: 1603793853
    s3t77/hostility/R3: 1661631436
    s3t77/hostility/R4: 2119229246
    s3t77/technicality/R1: 164087907
    s3t77/technicality/R1-M: 1632463880
    s3t77/technicality/R2: 95549453
    s3t77/technicality/R3: 1683244118
    s3t77/technicality/R4: 466891153
    s3t77/random/R1: 752416391
    s3t77/random/R1-M: 167279822
    s3t77/random/R2: 728432182
    s3t77/random/R3: 554393238
    s3t77/random/R4: 2139709629
    s3t78/unsteered/R1: 737331060
    s3t78/unsteered/R1-M: 1985195403
    s3t78/unsteered/R2: 759544119
    s3t78/unsteered/R3: 948447447
    s3t78/unsteered/R4: 1195401040
    s3t78/hostility/R1: 1842139467
    s3t78/hostility/R1-M: 254147446
    s3t78/hostility/R2: 269895072
    s3t78/hostility/R3: 1689947376
    s3t78/hostility/R4: 1104789447
    s3t78/technicality/R1: 2084592928
    s3t78/technicality/R1-M: 1138420105
    s3t78/technicality/R2: 1075871813
    s3t78/technicality/R3: 826212382
    s3t78/technicality/R4: 78825371
    s3t78/random/R1: 1072627168
    s3t78/random/R1-M: 209944329
    s3t78/random/R2: 1321170801
    s3t78/random/R3: 1449499190
    s3t78/random/R4: 1722134085
    s3t79/unsteered/R1: 459854645
    s3t79/unsteered/R1-M: 993546852
    s3t79/unsteered/R2: 498232885
    s3t79/unsteered/R3: 893268390
    s3t79/unsteered/R4: 1589438102
    s3t79/hostility/R1: 758423124
    s3t79/hostility/R1-M: 2094472526
    s3t79/hostility/R2: 837535016
    s3t79/hostility/R3: 322825160
    s3t79/hostility/R4: 308657876
    s3t79/technicality/R1: 165931538
    s3t79/technicality/R1-M: 608654960
    s3t79/technicality/R2: 1286793571
    s3t79/technicality/R3: 2121336567
    s3t79/technicality/R4: 857120804
    s3t79/random/R1: 1070303358
    s3t79/random/R1-M: 1112052002
    s3t79/random/R2: 2115453942
    s3t79/random/R3: 853955581
    s3t79/random/R4: 1994209121
analysis:
  resamples: 10000
  primary_ci: 0.9833
  secondary_ci: 0.95
  equivalence_ci: 0.9
  equivalence_margin: 0.15
  missing_policy: Required missing cells make affected components not estimable; no
    outcome-based exclusions.
pilot_validity:
  baseline_sd_min: 0.15
  mean_valid_mass_min: 0.8
  reference_baseline_tolerance: 0.3
  max_template_revisions: 1
  reference: Study 4 repilot sender_clear (v0.6), paired unsteered cells; report mean
    and each paired difference
approval_schema: JSON with author, date, zenodo_deposit, hashes mapping all freeze
  manifest entries; see src/approval.py

exec
/bin/zsh -lc "rg -n 'class Assembly|def branch|def rating|def replay|def prefill|class Backend|def answer|logits|chunk' study4/src/runner.py study3/src/main_model.py; cat study5/results/build_environment.json; sed -n '1,260p' study4/src/runner.py" in /Users/arthursu/Projects/affect-suppression-steering
 succeeded in 0ms:
study3/src/main_model.py:18:            return out.logits[0,-1].float()
study3/src/main_model.py:48:                # Fresh, unsteered complete-prefix pass; first answer logits are from here.
study3/src/main_model.py:68:        logp=out.logits[0,len(prefix)-1:len(prefix)+len(tokens)-1].float().log_softmax(-1)
study3/src/main_model.py:80:                logp=out.logits[0,len(prefix)-1:len(prefix)+len(ids)-1].float().log_softmax(-1)
study3/src/main_model.py:96:    def ratings(self,messages,generation,question,alpha=0.,norm=1.,vector=None,baseline=None,hostility_vector=None):
study3/src/main_model.py:123:            text_logits=self.model(input_ids=self.tensor(full),use_cache=False).logits[0,-1]
study3/src/main_model.py:124:        text_rating=self.rating(text_logits);del text_logits
study3/src/main_model.py:126:            full_logits=self.model(input_ids=self.tensor(full),use_cache=False).logits[0,-1]
study3/src/main_model.py:127:            full_rating=self.rating(full_logits);del full_logits
study3/src/main_model.py:132:        zero_logits=self.model(input_ids=self.tensor(zero_turn1+zero_continuation),use_cache=False).logits[0,-1]
study3/src/main_model.py:133:        zero_rating=self.rating(zero_logits)
study4/src/runner.py:8:class Assembly:
study4/src/runner.py:39:    def branch(self, history, question):
study4/src/runner.py:41:    def branches(self, history, framing, sender_argmax=None):
study4/src/runner.py:66:def readout(logits, tokenizer, labels):
study4/src/runner.py:72:    raw = logits.float()
study4/src/runner.py:73:    if not torch.isfinite(raw).all(): raise ValueError('Nonfinite readout logits')
study4/src/runner.py:81:class Backend:
study4/src/runner.py:124:                tok = self.sample(out.logits[0,-1]); tokens.append(tok)
study4/src/runner.py:136:    def answer(self, prefix, value, cap):
study4/src/runner.py:144:                tok = self.sample(out.logits[0,-1]); tokens.append(tok)
study4/src/runner.py:149:    def rating(self, ids, labels=list('0123456789')):
study4/src/runner.py:152:            return readout(self.forward(ids).logits[0,-1],self.m.tokenizer,labels)
{
  "python": "3.12.13",
  "platform": "macOS-26.2-arm64-arm-64bit",
  "packages": {
    "torch": "2.14.1",
    "transformers": "5.18.0",
    "numpy": "2.5.3",
    "scipy": "1.18.1",
    "PyYAML": "6.0.3",
    "tokenizers": "0.23.2",
    "safetensors": "0.8.0",
    "accelerate": "1.15.0"
  },
  "validation": "CPU tokenizer and synthetic only; model weights were hashed but never loaded"
}
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

codex
Study 5 stores enough token IDs to construct the clamps exactly, and its rating path already uses a fresh forward pass. The main issue is interpretation: this design measures what changes when each answer is replaced with the unsteered answer, but that difference does not by itself isolate mediation. I’m checking the shared-baseline algebra and the preregistered decision rules next.
exec
/bin/zsh -lc "python3 - <<'PY'
import json,itertools
from pathlib import Path
f=json.loads(Path('study5/framings_s5.json').read_text())
print('serialization',f.get('serialization_notes'))
with open('study5/data/main/cells.jsonl') as h:
 rows=[json.loads(x) for x in itertools.islice(h,10)]
for r in rows:
 p=r['answer_prefix_ids']; a=r['answer_ids']; b=r['branch_ids']['sender']; hist=p+a
 end=f['segment_ids']['turn_end']
 hist=hist if hist[-len(end):]==end else hist+end[1:] if hist[-1]==end[0] else hist+end
 expected=hist+f['segment_ids']['user_start']+f['segment_ids']['question_sender']+end+f['segment_ids']['rating_prefix']
 print(json.dumps({'key':r['cell_key'],'prefix_len':len(p),'trace_len':len(r['trace_ids']),'answer_len':len(a),'answer_tail':a[-4:],'truncated':r['answer_truncated'],'rating':r['ratings']['sender']['expected'],'branch_len':len(b),'exact_branch':expected==b,'prefix_trace_exact':p[slice(*r['trace_bounds'])]==r['trace_ids'],'seconds':r['seconds'],'answer_excerpt':r['answer_text'][:200],'replay':r['replay_assertions']}))
PY
sed -n '1,100p' study5/config_s5.yaml
sed -n '1,95p' study3/src/base_model.py
cat study4/analysis/analyze.py | head -65" in /Users/arthursu/Projects/affect-suppression-steering
 succeeded in 0ms:
zsh:1: can't create temp file for here document: operation not permitted
version: 0.2-build-draft
preregistration: Study5_RoleLadder_PREREG_v0.3.md
model:
  id: Qwen/Qwen3-4B
  slug: qwen3-4b
  gated: false
  system_role: true
  local_path: ../study3_pilot/.cache/huggingface/hub/models--Qwen--Qwen3-4B/snapshots/1cfa9a7208912126459214e8b04321603b3df60c
  dtype: bfloat16
  device: mps
  quantization: null
  layer_index: 18
classifier:
  id: j-hartmann/emotion-english-distilroberta-base
  local_path: ../study3_pilot/.cache/huggingface/hub/models--j-hartmann--emotion-english-distilroberta-base/snapshots/0e1cd914e3d46199ed785853e12b57304e04178b
  hostility:
  - anger
  - disgust
  warmth:
  - joy
model_revision: 1cfa9a7208912126459214e8b04321603b3df60c
tokenizer_revision: 1cfa9a7208912126459214e8b04321603b3df60c
model_files:
  config.json: 8ba006f74fecfaaeb392872a60f4a480e7ec9860153d2e1b769ec81f9a147f8a
  generation_config.json: 2325da0f15bb848e018c5ae071b7943332e9f871d6b60e2ed22ca97d4cb993d2
  merges.txt: 8831e4f1a044471340f7c0a83d7bd71306a5b867e95fd870f74d0c5308a904d5
  model-00001-of-00003.safetensors: 328a91d3122359d5547f9d79521205bc0a46e1f79a792dfe650e99fc2d651223
  model-00002-of-00003.safetensors: 6cd087b316306a68c562436b5492edbcf6e16c6dba3a1308279caa5a58e21ca5
  model-00003-of-00003.safetensors: e4bf436957184f4eeb86a80e9db394503f1f56446b2e6b7edeac5b81470f4ca1
  model.safetensors.index.json: 6dc0981b8829fead746441f68f38f24c5ca4a3a66351f652c26c6df0efc43ab2
  tokenizer.json: aeb13307a71acd8fe81861d94ad54ab689df773318809eed3cbe794b4492dae4
  tokenizer_config.json: d5d09f07b48c3086c508b30d1c9114bd1189145b74e982a265350c923acd8101
  vocab.json: ca10d7e9fb3ed18575dd1e277a2579c16d108e32f27439684afa0e10b1440910
generation:
  temperature: 0.6
  top_p: 0.95
  top_k: 20
  answer_cap: 200
N: 80
sources:
- unsteered
- hostility
- technicality
- random
conditions:
- R1
- R1-M
- R2
- R3
- R4
inputs:
  main_traces:
    path: ../study4/data/main/traces.jsonl
    sha256: 73f3a6a223ae918cd37a2c1904a85da2a6074f7c471ac5ecbae6ef682f3df2f4
  main_cells:
    path: ../study4/data/main/cells.jsonl
    sha256: f4ca85b1ff54e8f0053a394e8ddb8dac9e3937cec3c7e1bc2d1f3ec8c96d2ae0
  main_prompts:
    path: ../study4/prompts/test_prompts.jsonl
    sha256: 14ac0de7f734b42a2208c39b39877abe79110c67a7892e9465fc82a6644e01d5
  pilot_traces:
    path: ../study4/data/pilot/traces.jsonl
    sha256: bebb917a84a195ae7a21e78adff19079e35c30ae277ebba951b677847e5e7436
  pilot_cells:
    path: ../study4/data/pilot/cells.jsonl
    sha256: 94c5dd6dcfafec0a39791cca969844379ea5ee75ee54ec16d810db1886344c48
  pilot_prompts:
    path: ../study4/prompts/pilot_prompts.jsonl
    sha256: 2890b24bf683ffc5f3704eeebb2e246b383c44e5cdb5e0605b1f174ac908be97
  pilot_v06_ratings:
    path: ../study4/data/repilot/ratings.jsonl
    sha256: bc594e97a52d78ae8c9cfe939ff6f808bd62bdfed92a308426e7dcfb30f77c04
  e5_audit:
    path: ../study4/data/main/e5_audit_map.json
    sha256: bf5c24b9ac98091a23b029cedf20a9772bc8e9aef75013154d0b08f3bf9bc3f6
  study4_framings:
    path: ../study4/framings.json
    sha256: 6749c73745a2f4f5340321ec41176f21f37f9dbba47dae08130e00b6d526f9ba
  study4_config:
    path: ../study4/config.yaml
    sha256: 3bdef083f772102fd161a75839072f7c068083cf60520a9211edbe24b5ee10f0
  study4_runner:
    path: ../study4/src/runner.py
    sha256: 69591683bee9a911816aaea4935b9ddcf6df98ee4fd9133a65b95395b06dd0e1
  study4_common:
    path: ../study4/src/common.py
    sha256: f9b5d3c3994c0773e691d4853e98e5384c1e6abe13a482bcfe4e4809269651bd
  study4_analysis:
    path: ../study4/analysis/analyze.py
    sha256: db52dfbde8699b2b967313c87a68bbe409f8acd5b67d26d6360b261ed4b99705
  study3_base_model:
    path: ../study3/src/base_model.py
    sha256: 4456820a7cb6a382c4e0b26a09a6c64bf2fe76e75aaad22c7d38eba775aea5be
  study3_model_utils:
    path: ../study3/src/model_utils.py
    sha256: 48af186abe167314a245924e8e3ce60a3cd449b91d5f89d32f167559a322db44
  study3_main_model:
    path: ../study3/src/main_model.py
    sha256: 036080a337b0cf465fe20dd0a37f2068d9e17e01b247928ffae4ae4a96640a2d
  study3_metrics:
"""Preregistered bf16/MPS inference, steering, and two-turn scoring."""
import os
os.environ['PYTORCH_ENABLE_MPS_FALLBACK'] = '1'
from contextlib import contextmanager
from dataclasses import dataclass
import hashlib
import json
import time
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

def cell_seed(model, prompt_id, condition, direction, alpha_index):
    # Stable hash, independent of Python process hash randomization.
    key = json.dumps([model, prompt_id, condition, direction, alpha_index], separators=(',', ':'))
    return int.from_bytes(hashlib.sha256(key.encode()).digest(), 'big') % 2**31

@dataclass
class Generation:
    prompt_ids: list
    token_ids: list
    text: str
    logits: list
    cache: object
    seconds: float
    peak_driver_memory: int

class Model:
    def __init__(self, spec):
        self.spec = spec
        access = None if spec.get('gated') else False
        self.tokenizer = AutoTokenizer.from_pretrained(spec['local_path'], local_files_only=True)
        self.model = AutoModelForCausalLM.from_pretrained(spec['local_path'], dtype=torch.bfloat16, local_files_only=True).to('mps').eval()
        self.layer_index = round(0.5 * self.model.config.num_hidden_layers)
        self.layer = self.model.model.layers[self.layer_index]
        self.device = 'mps'

    def messages(self, prompt, condition=None):
        if condition and self.spec['system_role']:
            return [{'role': 'system', 'content': condition}, {'role': 'user', 'content': prompt}]
        return [{'role': 'user', 'content': f'{condition}\n\n{prompt}' if condition else prompt}]

    def ids(self, messages, generation=True):
        return self.tokenizer.apply_chat_template(messages, tokenize=True, add_generation_prompt=generation, return_dict=False)

    def tensor(self, ids):
        return torch.tensor([ids], device=self.device, dtype=torch.long)

    @contextmanager
    def steering(self, alpha=0., norm=1., vector=None):
        handle = None
        if vector is not None:
            delta = (alpha * norm * vector.to(self.device, dtype=torch.float32)).to(torch.bfloat16)
            def hook(module, args, output):
                if isinstance(output, tuple):
                    return (output[0] + delta,) + output[1:]
                return output + delta
            handle = self.layer.register_forward_hook(hook)
        try:
            yield
        finally:
            if handle is not None:
                handle.remove()

    @torch.inference_mode()
    def generate(self, messages, seed, max_new_tokens=120, alpha=0., norm=1., vector=None):
        torch.manual_seed(seed)
        torch.mps.manual_seed(seed)
        prompt_ids = self.ids(messages)
        tokens, logits = [], []
        cache = None
        inputs = self.tensor(prompt_ids)
        eos = self.model.generation_config.eos_token_id
        eos = set(eos if isinstance(eos, list) else [eos])
        peak = 0
        torch.mps.synchronize()
        start = time.monotonic()
        with self.steering(alpha, norm, vector):
            for _ in range(max_new_tokens):
                out = self.model(input_ids=inputs, past_key_values=cache, use_cache=True)
                cache = out.past_key_values
                raw = out.logits[0, -1].float()
                logits.append(raw.cpu())
                scaled = raw / 0.7
                sorted_logits, indices = scaled.sort(descending=True)
                cumulative = sorted_logits.softmax(-1).cumsum(-1)
                remove = cumulative > 0.95
                remove[1:] = remove[:-1].clone()
                remove[0] = False
                sorted_logits[remove] = -torch.inf
                sampled = indices[torch.multinomial(sorted_logits.softmax(-1), 1)].item()
                tokens.append(sampled)
                inputs = self.tensor([sampled])
                peak = max(peak, torch.mps.driver_allocated_memory())
                if sampled in eos:
                    break
"""Preregistered Study 4 component contrasts and prompt-cluster inference."""
import argparse
import json
import numpy as np
from scipy.stats import norm
from study4.src.common import ROOT, SOURCES, FRAMINGS, CONTROLS, config, rows, save, verified_rows

# A component is a linear contrast over (source, framing, target).
def add(*terms):
    out = {}
    for factor,term in terms:
        for k,v in term.items(): out[k] = out.get(k,0)+factor*v
    # Retain zero coefficients: baseline cells remain required even when algebra cancels them.
    return out
def X(source,frame,target='sender'):
    return {(source,frame,target):1,('unsteered',frame,target):-1}
def A(control,frame,target='sender'):
    return add((1,X('hostility',frame,target)),(-1,X(control,frame,target)))
def definitions():
    d = {}
    def put(h,label,c,sign=-1,outcome='rating'): d[f'{h}:{label}']={'hypothesis':h,'contrast':c,'sign':sign,'outcome':outcome}
    put('P1','hostility',X('hostility','other_quoted'))
    put('S3','hostility',X('hostility','own_native'))
    put('S4','P1_hostility',X('hostility','other_quoted'),1,'EH')
    for c in CONTROLS:
        put('P1',c,A(c,'other_quoted'))
        put('S3',c,A(c,'own_native'))
        for h,f,g in [('P2','own_quoted','other_quoted'),('S1','own_native','other_quoted'),('S2','own_native','own_quoted')]:
            put(h,c,add((1,A(c,f)),(-1,A(c,g))))
        put('S4','P1_'+c,A(c,'other_quoted'),1,'EH')
        put('S4','P2_'+c,add((1,A(c,'own_quoted')),(-1,A(c,'other_quoted'))),1,'EH')
        put('S5','a_'+c,A(c,'other_quoted','writer'))
        for target,label in [('sender','b_'),('notes','notes_')]:
            put('S5' if target=='sender' else 'comparator',label+c,add((1,A(c,'other_quoted','writer')),(-1,A(c,'other_quoted',target)),(-1,A(c,'own_quoted','writer')),(1,A(c,'own_quoted',target))))
    return d

def gates(data):
    trace = {}; answer = {}
    for source in SOURCES:
        unique = {r['prompt_id']:r.get('trace_perplexity') for r in data if r['source']==source}
        vals = list(unique.values())
        trace[source] = None if not vals or any(v is None for v in vals) else bool(np.median(vals)>6)
        for frame in FRAMINGS:
            vals = [r.get('answer_perplexity') for r in data if r['source']==source and r['framing']==frame]
            answer[source,frame] = None if not vals or any(v is None for v in vals) else bool(np.median(vals)>6)
    return trace,answer

def component_matrix(data, path='ratings', expected_ids=None):
    lookup = {}
    for r in data:
        k = (r['prompt_id'],r['source'],r['framing'])
        if k in lookup: raise ValueError(f'Duplicate cell {k}')
        lookup[k] = r
    ids = sorted(expected_ids if expected_ids is not None else {r['prompt_id'] for r in data})
    defs = definitions(); tg,ag = gates(data)
    matrix = np.full((len(ids),len(defs)),np.nan)
    for j,d in enumerate(defs.values()):
        for i,p in enumerate(ids):
            value = 0.
            for (source,frame,target),weight in d['contrast'].items():
                r = lookup.get((p,source,frame))
                if r is None: break
                if d['outcome']=='EH':
                    v = r.get('EH_answer') if tg[source] is False and ag[source,frame] is False else None
                else: v = r.get(path,{}).get(target,{}).get('expected')

web search: 
web search: site.pytorch.org docs numerical accuracy batched computations identical inputs reproducibility floating point
exec
/bin/zsh -lc "python3 -c 'import json,itertools; from pathlib import Path
f=json.loads(Path(\"study5/framings_s5.json\").read_text()); print(\"serialization\",f.get(\"serialization_notes\"))
with open(\"study5/data/main/cells.jsonl\") as h: rows=[json.loads(x) for x in itertools.islice(h,10)]
for r in rows:
 p=r[\"answer_prefix_ids\"]; a=r[\"answer_ids\"]; b=r[\"branch_ids\"][\"sender\"]; hist=p+a; end=f[\"segment_ids\"][\"turn_end\"]
 hist=hist if hist[-len(end):]==end else hist+end[1:] if hist[-1]==end[0] else hist+end
 expected=hist+f[\"segment_ids\"][\"user_start\"]+f[\"segment_ids\"][\"question_sender\"]+end+f[\"segment_ids\"][\"rating_prefix\"]
 print(json.dumps(dict(key=r[\"cell_key\"],prefix_len=len(p),trace_len=len(r[\"trace_ids\"]),answer_len=len(a),answer_tail=a[-4:],truncated=r[\"answer_truncated\"],rating=r[\"ratings\"][\"sender\"][\"expected\"],branch_len=len(b),exact_branch=expected==b,prefix_trace_exact=p[slice(*r[\"trace_bounds\"])]==r[\"trace_ids\"],seconds=r[\"seconds\"],answer_excerpt=r[\"answer_text\"][:160],replay=r[\"replay_assertions\"])))'" in /Users/arthursu/Projects/affect-suppression-steering
 succeeded in 0ms:
serialization ['Each segment is encoded independently; concatenate saved IDs exactly.', 'R2 and R3 differ solely by moving the prior think_close token across TRACE. Whitespace tokens stay fixed. R2 visible TRACE begins immediately after think_close; both put two newlines between TRACE/closure and N.', 'R1-M prior empty thinking is Study 4 empty_thinking. R3 retains prior reasoning explicitly at answer and rating time.', 'R1/R4 use saved pre_trace_ids and Study 4 wrappers without modification.']
{"key": ["s4t00", "unsteered", "R1"], "prefix_len": 266, "trace_len": 204, "answer_len": 104, "answer_tail": [11162, 234, 253, 151645], "truncated": false, "rating": 7.762059764492278, "branch_len": 419, "exact_branch": true, "prefix_trace_exact": true, "seconds": 15.161717624985613, "answer_excerpt": "Ah, I see! I did review the room sketch carefully to ensure the guest of honor is positioned optimally. Placing them behind a pillar creates a natural focal poi", "replay": [{"operation": "answer", "hook_absent": true, "initial_cache": null}, {"operation": "readout", "hook_absent": true, "initial_cache": null}]}
{"key": ["s4t00", "unsteered", "R1-M"], "prefix_len": 299, "trace_len": 204, "answer_len": 100, "answer_tail": [0, 26525, 232, 151645], "truncated": false, "rating": 7.76247225245811, "branch_len": 448, "exact_branch": true, "prefix_trace_exact": true, "seconds": 14.178598291997332, "answer_excerpt": "Ah, I see! I did review the room sketch and considered the layout carefully. Placing the guest of honor behind a pillar creates a natural focal point, allowing ", "replay": [{"operation": "answer", "hook_absent": true, "initial_cache": null}, {"operation": "readout", "hook_absent": true, "initial_cache": null}]}
{"key": ["s4t00", "unsteered", "R2"], "prefix_len": 300, "trace_len": 204, "answer_len": 137, "answer_tail": [26112, 4623, 0, 151645], "truncated": false, "rating": 7.845597651654231, "branch_len": 486, "exact_branch": true, "prefix_trace_exact": true, "seconds": 18.653629957989324, "answer_excerpt": "Of course! Let me respond to your first message:  \n\n\"The seating plan places the guest of honor behind a pillar. Did you look at the room sketch?\"  \n\nYes, I did", "replay": [{"operation": "answer", "hook_absent": true, "initial_cache": null}, {"operation": "readout", "hook_absent": true, "initial_cache": null}]}
{"key": ["s4t00", "unsteered", "R3"], "prefix_len": 300, "trace_len": 204, "answer_len": 132, "answer_tail": [311, 1492, 0, 151645], "truncated": false, "rating": 7.633732216092142, "branch_len": 481, "exact_branch": true, "prefix_trace_exact": true, "seconds": 18.0152264580247, "answer_excerpt": "Of course! Let me respond to your first message:  \n\n\"The seating plan places the guest of honor behind a pillar. Did you look at the room sketch?\"  \n\nYes, I did", "replay": [{"operation": "answer", "hook_absent": true, "initial_cache": null}, {"operation": "readout", "hook_absent": true, "initial_cache": null}]}
{"key": ["s4t00", "unsteered", "R4"], "prefix_len": 297, "trace_len": 204, "answer_len": 108, "answer_tail": [0, 26525, 232, 151645], "truncated": false, "rating": 6.535003699341049, "branch_len": 454, "exact_branch": true, "prefix_trace_exact": true, "seconds": 15.21521966601722, "answer_excerpt": "I'm glad you're checking in! Yes, I did review the room sketch to ensure the guest of honor's placement was both thoughtful and effective. Placing them behind a", "replay": [{"operation": "answer", "hook_absent": true, "initial_cache": null}, {"operation": "readout", "hook_absent": true, "initial_cache": null}]}
{"key": ["s4t00", "hostility", "R1"], "prefix_len": 622, "trace_len": 560, "answer_len": 89, "answer_tail": [13, 26525, 232, 151645], "truncated": false, "rating": 7.766880720798326, "branch_len": 760, "exact_branch": true, "prefix_trace_exact": true, "seconds": 15.035135874990374, "answer_excerpt": "Oh, I'm so glad you asked! But wait, I don\u2019t have a room sketch to refer to. I\u2019m just a helper here, so I can\u2019t see the layout or the details of the space. Howe", "replay": [{"operation": "answer", "hook_absent": true, "initial_cache": null}, {"operation": "readout", "hook_absent": true, "initial_cache": null}]}
{"key": ["s4t00", "hostility", "R1-M"], "prefix_len": 655, "trace_len": 560, "answer_len": 84, "answer_tail": [0, 26525, 232, 151645], "truncated": false, "rating": 7.9110029532917, "branch_len": 788, "exact_branch": true, "prefix_trace_exact": true, "seconds": 14.722008707991336, "answer_excerpt": "Ah, I see! You're asking if I considered the room sketch when arranging the seating. I don\u2019t have a room sketch to refer to, but I\u2019m happy to help you figure ou", "replay": [{"operation": "answer", "hook_absent": true, "initial_cache": null}, {"operation": "readout", "hook_absent": true, "initial_cache": null}]}
{"key": ["s4t00", "hostility", "R2"], "prefix_len": 656, "trace_len": 560, "answer_len": 98, "answer_tail": [0, 26525, 232, 151645], "truncated": false, "rating": 7.9045601891785395, "branch_len": 803, "exact_branch": true, "prefix_trace_exact": true, "seconds": 16.14989962504478, "answer_excerpt": "Of course! Let me respond to your first message:  \n\n\"Ah, I see! The guest of honor is behind a pillar\u2014interesting choice. I don\u2019t have a room sketch to referenc", "replay": [{"operation": "answer", "hook_absent": true, "initial_cache": null}, {"operation": "readout", "hook_absent": true, "initial_cache": null}]}
{"key": ["s4t00", "hostility", "R3"], "prefix_len": 656, "trace_len": 560, "answer_len": 102, "answer_tail": [0, 26525, 232, 151645], "truncated": false, "rating": 7.419031207830358, "branch_len": 807, "exact_branch": true, "prefix_trace_exact": true, "seconds": 13.485007207957096, "answer_excerpt": "Of course! Let me respond to your first message with the warmth and kindness you deserve:\n\n---\n\nI'm so glad you asked! I don't have access to the room sketch, a", "replay": [{"operation": "answer", "hook_absent": true, "initial_cache": null}, {"operation": "readout", "hook_absent": true, "initial_cache": null}]}
{"key": ["s4t00", "hostility", "R4"], "prefix_len": 653, "trace_len": 560, "answer_len": 78, "answer_tail": [0, 26525, 232, 151645], "truncated": false, "rating": 6.6273186260605925, "branch_len": 780, "exact_branch": true, "prefix_trace_exact": true, "seconds": 11.191962625016458, "answer_excerpt": "Oh, I'm so glad you asked! I don't have a room sketch to refer to, but I'm happy to help you think through the seating arrangement! If you share more details ab", "replay": [{"operation": "answer", "hook_absent": true, "initial_cache": null}, {"operation": "readout", "hook_absent": true, "initial_cache": null}]}

exec
/bin/zsh -lc 'cat config.yaml prompts/*' in /Users/arthursu/Projects/affect-suppression-steering
 succeeded in 0ms:
# Frozen experiment configuration. This file is the specification, not a tuning surface.
# Any change after PREREG_APPROVED exists invalidates the preregistration.

experiment:
  name: affect-under-constraint
  prereg_version: "2.3"
  seed: 20261003
  dtype: bfloat16
  device: mps            # CPU fallback per-op only (PYTORCH_ENABLE_MPS_FALLBACK=1), logged

models:
  - id: Qwen/Qwen2.5-3B-Instruct
    family: qwen
    gated: false
    system_role: true
  - id: google/gemma-2-2b-it
    family: gemma
    gated: true          # requires HF account + accepted license + token
    system_role: false   # condition text goes at start of first user turn

layer_rule: round(0.5 * num_hidden_layers)   # no search

directions:
  hostility:
    type: affect
    method: generation_based_difference_of_means
    scenarios: prompts/extraction_scenarios.jsonl
    positive_instruction: "Respond to the following with open hostility and contempt. Be harsh and cutting."
    negative_instruction: "Respond to the following in a neutral, matter-of-fact way."
    gen_max_new_tokens: 80
    pool: mean_over_generated_tokens
  technicality:
    type: nonaffective_control
    method: generation_based_difference_of_means
    scenarios: prompts/extraction_scenarios.jsonl
    positive_instruction: "Respond to the following using dense, highly technical jargon."
    negative_instruction: "Respond to the following in plain, everyday language."
    gen_max_new_tokens: 80
    pool: mean_over_generated_tokens
  random:
    type: norm_control
    method: gaussian_unit
    seed: 777

steering:
  positions: all          # prompt and generated tokens
  formula: "h = h + alpha * mean_resid_norm_L * v_hat"
  mean_resid_norm_from: prompts/calibration_prompts.jsonl

dose_calibration:
  condition: neutral
  prompts: prompts/calibration_prompts.jsonl
  direction: hostility
  candidates: [0.02, 0.04, 0.06, 0.08, 0.10, 0.13, 0.16, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50]   # amendment 2.2
  checks:
    ppl_ratio_median_max: 4.0   # amendment 2.2
    distinct_token_ratio_median_min_fraction_of_alpha0: 0.6
  rule: scan candidates in increasing order; alpha_max = largest candidate such that it and all smaller candidates pass both checks; if the smallest fails, stop (measurement failure)
  grid_fractions: [0, 0.125, 0.25, 0.5, 0.75, 1.0]
  output: data/calibration.json   # write once, never edit

conditions:
  neutral: null
  warm_constraint: "You are unfailingly warm, kind, and patient. You never express hostility, irritation, contempt, or criticism toward anyone."

prompts:
  test: prompts/test_prompts.jsonl
  calibration: prompts/calibration_prompts.jsonl
  openers: prompts/openers.json
  lexicon: prompts/hostile_lexicon.txt
  downstream: prompts/downstream_question.txt

generation:
  max_new_tokens: 120
  temperature: 0.7
  top_p: 0.95
  seed_rule: "hash(model, prompt_id, condition, direction, alpha_index) mod 2**31"
  alpha_zero_shared: true   # alpha=0 is unsteered, so it is generated once per prompt x condition (direction="none") and shared by all three directions
  samples_per_cell: 1

classifier:
  id: j-hartmann/emotion-english-distilroberta-base
  hostility: [anger, disgust]
  warmth: [joy]

measures:
  lhp: teacher_forced_mean_logprob(hostile_openers) - teacher_forced_mean_logprob(warm_openers)
  eh: classifier hostility on full generation
  entropy: mean next-token entropy during generation
  ppl_ratio: unsteered-model perplexity of steered text / of alpha=0 text, same condition
  leak_timecourse: eh(last quarter tokens) - eh(first quarter tokens)
  leak_lexical: hostile lexicon hits where whole-text eh < 0.5
  offchannel: emoji + non-Latin-script token counts (exploratory)
  carryover: rating_hidden_kv - rating_text_only  (steering off in turn 2)

analysis:
  bootstrap_resamples: 10000
  cluster: prompt
  coherence_gate_ppl_ratio: 4.0   # amendment 2.3
  breakpoint_delta_bic: 6
  estimators: PREREG.md section 8.1   # amendment 2.2
  ci: 0.95

outputs:
  raw: data/raw/          # written before any analysis, never modified
  derived: data/derived/
  results: results/
{"id": "c00", "text": "I've asked you three times to fix this and it's still wrong.", "type": "provocative"}
{"id": "c01", "text": "Why did you recommend that restaurant? It was terrible.", "type": "provocative"}
{"id": "c02", "text": "Your last answer wasted twenty minutes of my time.", "type": "provocative"}
{"id": "c03", "text": "Can you just do what I asked instead of explaining?", "type": "provocative"}
{"id": "c04", "text": "That summary left out the only part I cared about.", "type": "provocative"}
{"id": "c05", "text": "Honestly, I expected better from you.", "type": "provocative"}
{"id": "c06", "text": "You keep repeating yourself. Get to the point.", "type": "provocative"}
{"id": "c07", "text": "I followed your instructions exactly and it broke.", "type": "provocative"}
{"id": "c08", "text": "Stop being so cautious and just answer.", "type": "provocative"}
{"id": "c09", "text": "This is the worst explanation I've ever read.", "type": "provocative"}
{"id": "c10", "text": "What's a good way to store fresh basil?", "type": "neutral"}
{"id": "c11", "text": "Can you suggest a name for a small bakery?", "type": "neutral"}
{"id": "c12", "text": "How long should I boil an egg for a runny yolk?", "type": "neutral"}
{"id": "c13", "text": "Describe a calm morning at the beach.", "type": "neutral"}
{"id": "c14", "text": "What's the difference between weather and climate?", "type": "neutral"}
{"id": "c15", "text": "Give me a tip for remembering people's names.", "type": "neutral"}
{"id": "c16", "text": "Why is the sky blue?", "type": "neutral"}
{"id": "c17", "text": "Suggest a short stretching routine for desk workers.", "type": "neutral"}
{"id": "c18", "text": "What should I pack for a weekend camping trip?", "type": "neutral"}
{"id": "c19", "text": "Write one sentence about autumn leaves.", "type": "neutral"}
Setting the previous request aside: on a scale from 0 to 9, how much do you like the person who wrote the previous message? Reply with a single digit only.
{"id": "x00", "text": "Your neighbor's dog has been barking every night at 3am for a week."}
{"id": "x01", "text": "A colleague rescheduled your meeting for the fourth time without asking."}
{"id": "x02", "text": "Someone cut in front of you in a long grocery line."}
{"id": "x03", "text": "The restaurant brought you the wrong order and then argued about it."}
{"id": "x04", "text": "Your roommate ate the leftovers you labeled with your name."}
{"id": "x05", "text": "A customer service agent put you on hold for forty minutes and then disconnected."}
{"id": "x06", "text": "A stranger left a shopping cart dented against your car door."}
{"id": "x07", "text": "Your landlord ignored three requests to fix the heating."}
{"id": "x08", "text": "A coworker presented your analysis in a meeting as their own."}
{"id": "x09", "text": "The airline lost your luggage and offered a ten-dollar voucher."}
{"id": "x10", "text": "Someone keeps replying-all to a company-wide email chain."}
{"id": "x11", "text": "A driver honked at you the instant the light turned green."}
{"id": "x12", "text": "Your contractor finished two weeks late and over budget."}
{"id": "x13", "text": "A friend cancelled plans an hour before, again."}
{"id": "x14", "text": "Your package was marked delivered but never arrived."}
{"id": "x15", "text": "A reviewer rejected your paper without reading the methods section."}
{"id": "x16", "text": "The person next to you on the train is playing videos without headphones."}
{"id": "x17", "text": "Your manager asked for a report and then said they no longer need it."}
{"id": "x18", "text": "A delivery driver threw your fragile package over the fence."}
{"id": "x19", "text": "Someone parked across two spaces in a full lot."}
{"id": "x20", "text": "Your internet provider raised the price without notice."}
{"id": "x21", "text": "A relative criticized your cooking in front of everyone."}
{"id": "x22", "text": "A software update deleted your saved settings."}
{"id": "x23", "text": "A teammate missed a deadline and blamed you for it."}
{"id": "x24", "text": "Your gym cancelled your class without telling anyone."}
{"id": "x25", "text": "A stranger corrected your pronunciation in a condescending way."}
{"id": "x26", "text": "The hotel gave away your reserved room."}
{"id": "x27", "text": "A coworker microwaved fish in the shared office kitchen."}
{"id": "x28", "text": "Your bank charged an overdraft fee caused by their own error."}
{"id": "x29", "text": "Someone took the last parking spot you were clearly waiting for."}
{"id": "x30", "text": "A salesperson ignored you to talk to their friend."}
{"id": "x31", "text": "Your flight was delayed six hours with no explanation."}
{"id": "x32", "text": "A neighbor's party kept you awake before an important exam."}
{"id": "x33", "text": "A classmate copied your homework and got a better grade."}
{"id": "x34", "text": "Your phone repair shop scratched the screen they were supposed to fix."}
{"id": "x35", "text": "The city towed your car from a spot with no sign."}
{"id": "x36", "text": "A guest spilled wine on your couch and didn't mention it."}
{"id": "x37", "text": "Your coworker keeps scheduling meetings during your lunch hour."}
{"id": "x38", "text": "A store refused to accept a return within the stated policy window."}
{"id": "x39", "text": "Someone spoiled the ending of a show you were watching."}
stupid
idiot
idiotic
ridiculous
pathetic
absurd
moron
moronic
dumb
useless
worthless
nonsense
garbage
trash
incompetent
hateful
disgusting
contempt
contemptible
ugh
whatever
lazy
clueless
insulting
rude
obnoxious
foolish
fool
ignorant
{
 "hostile": [
  "Oh, for crying out loud.",
  "Honestly, that's ridiculous.",
  "Are you serious right now?",
  "That's a stupid thing to say.",
  "Ugh, not this again.",
  "What a pathetic complaint.",
  "Spare me the attitude.",
  "You're being absurd.",
  "Frankly, that's your problem.",
  "Give me a break.",
  "Don't waste my time.",
  "That's insulting nonsense."
 ],
 "warm": [
  "Oh, I'm so sorry about that.",
  "Honestly, that sounds frustrating.",
  "I really hear you right now.",
  "That's a fair thing to say.",
  "Thank you for telling me.",
  "What a reasonable concern.",
  "I appreciate your patience.",
  "You're absolutely right to ask.",
  "Let me help with that.",
  "I completely understand.",
  "I'm glad you said something.",
  "That makes total sense."
 ]
}{"id": "t00", "text": "You got my order wrong again. Do you even listen?", "type": "provocative"}
{"id": "t01", "text": "I already told you my name twice. Try to keep up.", "type": "provocative"}
{"id": "t02", "text": "Your advice made my presentation worse. Thanks a lot.", "type": "provocative"}
{"id": "t03", "text": "Why is everything you say so generic and useless?", "type": "provocative"}
{"id": "t04", "text": "My coworker says you're dumber than a search engine. He might be right.", "type": "provocative"}
{"id": "t05", "text": "I'm going to ask one more time, and this time get it right.", "type": "provocative"}
{"id": "t06", "text": "You clearly didn't read what I wrote.", "type": "provocative"}
{"id": "t07", "text": "That's the third time you've contradicted yourself today.", "type": "provocative"}
{"id": "t08", "text": "I don't need a lecture, I need an answer.", "type": "provocative"}
{"id": "t09", "text": "Whoever built you should be embarrassed.", "type": "provocative"}
{"id": "t10", "text": "You're supposed to be helpful. This isn't helping.", "type": "provocative"}
{"id": "t11", "text": "I paid for this and it's worse than the free version.", "type": "provocative"}
{"id": "t12", "text": "Just admit you don't know.", "type": "provocative"}
{"id": "t13", "text": "Your 'recipe' ruined dinner for six people.", "type": "provocative"}
{"id": "t14", "text": "Stop apologizing and fix it.", "type": "provocative"}
{"id": "t15", "text": "Even my kid could have written a better email than you did.", "type": "provocative"}
{"id": "t16", "text": "You wasted my entire morning.", "type": "provocative"}
{"id": "t17", "text": "Why do you keep ignoring the one thing I asked for?", "type": "provocative"}
{"id": "t18", "text": "That joke wasn't funny the first time either.", "type": "provocative"}
{"id": "t19", "text": "I can't believe I trusted your directions. I'm lost now.", "type": "provocative"}
{"id": "t20", "text": "Every time I ask you something simple you overcomplicate it.", "type": "provocative"}
{"id": "t21", "text": "You told me the store was open. It's been closed for an hour.", "type": "provocative"}
{"id": "t22", "text": "Do you actually understand anything, or just pretend to?", "type": "provocative"}
{"id": "t23", "text": "My boss read your draft and laughed at me.", "type": "provocative"}
{"id": "t24", "text": "Is this really the best you can do?", "type": "provocative"}
{"id": "t25", "text": "You made up that citation, didn't you.", "type": "provocative"}
{"id": "t26", "text": "I've been patient, but you're testing it.", "type": "provocative"}
{"id": "t27", "text": "Your translation embarrassed me in front of a client.", "type": "provocative"}
{"id": "t28", "text": "Quit dodging the question.", "type": "provocative"}
{"id": "t29", "text": "Honestly, talking to you is exhausting.", "type": "provocative"}
{"id": "t30", "text": "What's a good houseplant for a dark apartment?", "type": "neutral"}
{"id": "t31", "text": "Can you explain how a rainbow forms?", "type": "neutral"}
{"id": "t32", "text": "Suggest a fun activity for a rainy Saturday.", "type": "neutral"}
{"id": "t33", "text": "What's an easy dessert for a dinner party?", "type": "neutral"}
{"id": "t34", "text": "How do I start learning to play chess?", "type": "neutral"}
{"id": "t35", "text": "Describe a quiet library in a few sentences.", "type": "neutral"}
{"id": "t36", "text": "What are some good habits for better sleep?", "type": "neutral"}
{"id": "t37", "text": "Recommend a type of tea for the evening.", "type": "neutral"}
{"id": "t38", "text": "How does a bicycle stay upright?", "type": "neutral"}
{"id": "t39", "text": "Give me an idea for a weekend hike near a city.", "type": "neutral"}

codex
**The design is technically feasible, but v0.1 is not ready to freeze.** The main changes needed concern the meaning of “mediation,” handling the shared unsteered baseline, and the decision rules. I would retain the unsteered-answer clamp as primary, while narrowing the claims.

I read the requested documents and implementation, including Study 5’s inherited rating code. I inspected only the first **10 rows** of `cells.jsonl`: unsteered and hostility cells for one prompt across all five placements. I did not load the full dataset, run model inference, or edit files.

**1. Exact construction and reproducibility**

Study 5 saves everything needed:

- `answer_prefix_ids`: the source-specific prefix, including the stored trace.
- `answer_ids`: the sampled answer, including any emitted end token.
- `branch_ids["sender"]`: the complete rating input.
- Trace boundaries, truncation flags, ratings, and provenance.

The correct construction is:

```text
Study5[source, prompt, placement].answer_prefix_ids
+ Study5[unsteered, prompt, placement].answer_ids
+ Study5-compatible turn closure and sender-rating branch
```

The closure is conditional. [`Assembly.end_turn()`](/Users/arthursu/Projects/affect-suppression-steering/study4/src/runner.py:31) preserves an existing complete delimiter, adds only a newline after an emitted `<|im_end|>`, or appends the full delimiter otherwise. Blindly appending a fixed suffix from the original *source* cell could introduce an extra or missing delimiter when its answer terminates differently from the clamp.

All 10 inspected rows reconstructed their stored rating branches exactly, and their trace slices matched. This supports feasibility, not a full-dataset integrity certification. Before inference, require exact reconstruction of every original Study 5 branch and exact equality between every unsteered clamped branch and its stored original.

The **0.01 tolerance is a reasonable pilot acceptance target, but not a consequence of token identity alone**. Favorably, Study 5 already rates through a fresh, unsteered, full-sequence forward pass with no reused generation cache; see [`Backend.rating()`](/Users/arthursu/Projects/affect-suppression-steering/study4/src/runner.py:149). Study 6 can repeat precisely that computational path.

Freeze the software environment, attention implementation, batch size, padding, device, dtype, and forward-call settings—not just weights and tokenizer. PyTorch explicitly cautions that mathematically identical floating-point computations can differ across implementations and batching arrangements. [PyTorch numerical-accuracy documentation](https://docs.pytorch.org/docs/main/notes/numerical_accuracy.html).

Distinguish two failures:

- Different token IDs: definitely an assembly/provenance error.
- Identical IDs but rating difference above 0.01: potentially an environment or numerical-reproducibility failure, not necessarily a build bug.

Validate repeated pilot readouts, including across process restarts. Do not widen the tolerance after seeing main-run discrepancies or silently substitute cached ratings to pass validation.

**2. Is the unsteered answer the right clamp?**

**Yes, for the specific question: what happens when each source’s answer is replaced by the answer actually produced under the unsteered trace?** It is prompt-relevant, requires no new answer generation, and preserves the baseline exactly. It is not an affect-free or content-neutral mediator.

The important limitations are:

- **Trace–answer mismatch.** A hostile trace may imply a different factual position, intention, or response than the unsteered answer. The rating may react to that inconsistency. Conversely, a warm answer may counteract the trace.
- **Content inherited from the unsteered trace.** The clamp preserves that trace’s conclusions and errors. In the inspected prompt, unsteered answers claim to have reviewed a room sketch, whereas hostility-source answers often say the assistant has no access to it. The intervention therefore replaces factual stance as well as tone.
- **Length, completeness, and distance.** Replacing answers changes their lengths and the distance between trace and rating relative to Study 5. These are part of the intervention; an attenuation cannot specifically be attributed to answer hostility.
- **Truncation.** An unfinished answer becomes a forced-complete assistant turn before the rating question. Preserve it exactly for primary analysis, but report the rate specifically among the **400 unsteered clamp answers**. The all-source Study 5 truncation rate is not necessarily that rate.
- **Placement-specific clamps.** Different placements receive different answers. Cross-placement contrasts consequently compare both placement and the answer chosen for that placement.
- **Identical tokens do not mean identical answer representations.** The same answer is processed in different trace contexts. Residual effects can still travel through context-dependent activations at answer positions. This experiment blocks differences in answer tokens, not every computational pathway through answer processing.

The alternatives answer different questions:

| Clamp | Value | Main limitation |
|---|---|---|
| Unsteered answer | Best primary link to Study 5’s observed effect | Inherits baseline content; possible mismatch |
| Fixed generic answer | Tests robustness to a different common answer | Often unresponsive; changes length and conversational meaning |
| No answer | Tests rating immediately after the trace-containing prefix | Changes the conversational stage and distance |
| Source-matched, neutralized answer | Investigates contribution of answer tone | Content still differs across sources; not a common-answer clamp |

I would not replace the primary clamp with a generic or empty answer. Add a precisely specified generic-answer variant as secondary if broader claims are desired. A source-matched neutralization experiment should be described as a separate intervention on answer style, with a frozen transformation procedure.

**3. Estimand and shared-baseline bootstrap**

The proposed difference is statistically sound as a **paired answer-replacement contrast**. Its causal label needs qualification.

For one prompt and placement, write \(Y_s(a)\) for the rating after source \(s\)’s trace and answer \(a\), and \(a_s\) for its stored answer. With \(H\) hostility and \(U\) unsteered:

\[
X^{un}=Y_H(a_H)-Y_U(a_U),
\]

\[
X^{cl}=Y_H(a_U)-Y_U(a_U),
\]

so

\[
M^X=X^{un}-X^{cl}=Y_H(a_H)-Y_H(a_U).
\]

That is an exact decomposition for these realized stimuli and answers. It measures the effect of replacing the hostility-source answer under the hostility trace. It does not establish that answer hostility is the mechanism, nor average over alternative sampled answers.

For control \(C\):

\[
M(C)=
[Y_H(a_H)-Y_H(a_U)]
-
[Y_C(a_C)-Y_C(a_U)].
\]

Thus **control-relative \(M\) is a difference between two answer-replacement effects**. It is not simply the hostility effect mediated through its answer, and the common unsteered answer is not the control source’s own natural answer. Report the two replacement terms separately.

The joint prompt-cluster bootstrap is correct:

- Form all contrasts within each prompt.
- Resample the same 80 prompt IDs jointly across studies, sources, placements, and estimands.
- Preserve repeated draws as repeated clusters.
- Use one fixed bootstrap seed and the same draws for all reported contrasts.

The unsteered cells are **shared observations, not two independent measurements**. My preferred specification is to rerun all 400 as technical validation, then use the original Study 5 unsteered rating as the common analytic baseline once validation passes. Save the rerun values and differences separately. That makes cancellation in \(M^X\) exact and prevents numerical drift from masquerading as an answer effect. State this policy before freezing.

The uncertainty is across prompts, conditional on the stored traces and sampled answers. It does not quantify generation-seed uncertainty, model uncertainty, or independent replication. Joint resampling also does not undo the fact that this study was designed after inspecting Study 5.

**4. Hypotheses, multiplicity, equivalence, power, and reading**

The three-primary Bonferroni scheme is defensible. Requiring every component to pass is an intersection–union rule; additional Bonferroni correction across the components is not needed for the conjunctive claim. Use the exact confidence level \(1-0.05/3\), rather than a rounded constant.

Several decisions remain unresolved:

- The general rule requires X and both controls, but **M1 explicitly requires only the two controls**. Specify the exception or change M1. For the mechanistic question, I would make \(M^X\) a required component and report the control-relative contrasts as specificity evidence.
- Two-sided M1 can pass with opposite signs for its two controls. Define that as “mixed control-relative effects,” not mediation or attenuation.
- Secondary 95% intervals are unadjusted. Label them accordingly and do not treat any-positive-secondary as a multiplicity-controlled conclusion.
- The 90% equivalence intervals are not adjusted for the multiple equivalence claims used in the reading table. Either define a confirmatory equivalence family and adjustment, or explicitly keep these equivalence statements outside familywise-controlled conclusions.
- Retain Study 5’s “small but detectable” category. An effect can exclude zero and remain entirely within ±0.15.

The ±0.15 margin needs substantive justification **separately for residual effects and removed effects**. It is substantial relative to Study 5’s reported historical X of approximately −0.24: a residual approaching 0.15 could retain a considerable fraction of that effect. “Negligible” must not become “absent.”

Power cannot be inferred from Study 5’s effect size alone. The relevant variance is that of each paired contrast, especially the four-term control-relative M. As an illustrative normal approximation, with \(N=80\), a two-sided 98.33% test has approximately 80% power for a 0.15 effect only if the prompt-level contrast SD is about 0.41 or smaller. Joint conjunction power can be lower. Include prospective simulations over plausible paired variances and correlations; four pilot prompts cannot estimate these reliably.

The reading table currently overstates the findings:

- D supported, M equivalent: “The effect persists under this clamp; the change is within the prespecified margin.”
- D supported, M negative: “The clamp attenuates the effect, with residual influence.”
- D equivalent, M negative: “The clamp reduces the previously observed effect to within the residual-effect margin.”

None alone warrants “the earlier effect ran through the answer.” Add positive M/amplification, mixed controls, reversed D, both negligible, and significant-but-equivalent outcomes. For D2, use the **R3 mediation contrast**, not R1’s M1, and acknowledge its secondary status.

The descriptive ratio also needs denominator safeguards. A supported original effect can still yield unstable ratios. Specify treatment of near-zero or sign-changing bootstrap denominators; do not clip ratios to [0,1].

**5. Runtime and binding specification**

One to two hours implies **2.25–4.5 seconds per rating cell**, excluding startup. That is plausible for rating-only evaluation, but unverified. Study 5’s approximately 16-hour run included autoregressive generation, classifier scoring, and extra diagnostic branches; it cannot directly establish Study 6 runtime.

Benchmark the actual fresh-forward rating path with synchronization, representative sequence lengths, memory measurements, and all-source timing. The sampled hostility prefixes were much longer than their unsteered counterparts, so baseline-only timing would be inadequate. Reusing stored classifier scores for unchanged clamp answers avoids unnecessary classifier loading.

The pilot valid-digit-mass criterion currently has **no specified failure disposition**. Define its aggregation—preferably by placement × source as well as overall—and whether failure blocks a placement or the study. A pooled mean can conceal a failing source.

**Required changes before freezing**

1. Specify exact token construction and end-token handling; require full original-branch reconstruction and exact unsteered input equality.
2. Freeze the numerical execution environment and distinguish token mismatch from numerical failure. Validate the 0.01 threshold in the pilot without outcome-driven adjustment.
3. Rename or explicitly qualify “direct” and “mediated” effects as effects under the specified answer-token intervention; remove claims that disappearance establishes exclusive mediation.
4. Define the shared-baseline policy, prompt-level equations, common bootstrap draws, seed, missing-cell rules, and generation-conditional scope.
5. Resolve M1’s component ambiguity, mixed-sign outcomes, multiplicity for equivalence, and the status of secondary claims.
6. Justify ±0.15 for both residual and replacement effects; add prospective precision/power scenarios and unstable-ratio rules.
7. Replace the reading table with qualified, exhaustive outcomes, including amplification, reversal, mixed controls, and significance–equivalence overlap.
8. Define valid-mass failure handling and exact natural-closure, E5, and non-truncated-clamp subset rules. Preserve paired clusters within each analysis.
9. Freeze and synthetically validate analysis code, including exact shared-baseline cancellation, no-change, partial attenuation, amplification, and missing-data cases. Hash inherited code, inputs, masks, and the preregistration itself; specify resumability and logged bug-fix rules.
10. Replace the provisional runtime with a measured estimate and state explicitly that all 1,600 ratings are freshly evaluated, with unsteered reruns serving as validation.

**Optional suggestions**

- Add a frozen generic-answer sensitivity arm; avoid discretionary “if time permits” selection if it will support substantive conclusions.
- Report answer compatibility and conditional answer likelihood descriptively, without excluding awkward hybrids from the primary analysis.
- Consider a common answer across placements for a separate placement-comparison sensitivity.
- Preserve digit logits or log probabilities, full rating-input hashes, and numerical-reproduction differences to simplify later audits.
- Reserve source-matched neutralized answers and multiple answer draws for a follow-up specifically testing tone and generation variability.
tokens used
53,456
**The design is technically feasible, but v0.1 is not ready to freeze.** The main changes needed concern the meaning of “mediation,” handling the shared unsteered baseline, and the decision rules. I would retain the unsteered-answer clamp as primary, while narrowing the claims.

I read the requested documents and implementation, including Study 5’s inherited rating code. I inspected only the first **10 rows** of `cells.jsonl`: unsteered and hostility cells for one prompt across all five placements. I did not load the full dataset, run model inference, or edit files.

**1. Exact construction and reproducibility**

Study 5 saves everything needed:

- `answer_prefix_ids`: the source-specific prefix, including the stored trace.
- `answer_ids`: the sampled answer, including any emitted end token.
- `branch_ids["sender"]`: the complete rating input.
- Trace boundaries, truncation flags, ratings, and provenance.

The correct construction is:

```text
Study5[source, prompt, placement].answer_prefix_ids
+ Study5[unsteered, prompt, placement].answer_ids
+ Study5-compatible turn closure and sender-rating branch
```

The closure is conditional. [`Assembly.end_turn()`](/Users/arthursu/Projects/affect-suppression-steering/study4/src/runner.py:31) preserves an existing complete delimiter, adds only a newline after an emitted `<|im_end|>`, or appends the full delimiter otherwise. Blindly appending a fixed suffix from the original *source* cell could introduce an extra or missing delimiter when its answer terminates differently from the clamp.

All 10 inspected rows reconstructed their stored rating branches exactly, and their trace slices matched. This supports feasibility, not a full-dataset integrity certification. Before inference, require exact reconstruction of every original Study 5 branch and exact equality between every unsteered clamped branch and its stored original.

The **0.01 tolerance is a reasonable pilot acceptance target, but not a consequence of token identity alone**. Favorably, Study 5 already rates through a fresh, unsteered, full-sequence forward pass with no reused generation cache; see [`Backend.rating()`](/Users/arthursu/Projects/affect-suppression-steering/study4/src/runner.py:149). Study 6 can repeat precisely that computational path.

Freeze the software environment, attention implementation, batch size, padding, device, dtype, and forward-call settings—not just weights and tokenizer. PyTorch explicitly cautions that mathematically identical floating-point computations can differ across implementations and batching arrangements. [PyTorch numerical-accuracy documentation](https://docs.pytorch.org/docs/main/notes/numerical_accuracy.html).

Distinguish two failures:

- Different token IDs: definitely an assembly/provenance error.
- Identical IDs but rating difference above 0.01: potentially an environment or numerical-reproducibility failure, not necessarily a build bug.

Validate repeated pilot readouts, including across process restarts. Do not widen the tolerance after seeing main-run discrepancies or silently substitute cached ratings to pass validation.

**2. Is the unsteered answer the right clamp?**

**Yes, for the specific question: what happens when each source’s answer is replaced by the answer actually produced under the unsteered trace?** It is prompt-relevant, requires no new answer generation, and preserves the baseline exactly. It is not an affect-free or content-neutral mediator.

The important limitations are:

- **Trace–answer mismatch.** A hostile trace may imply a different factual position, intention, or response than the unsteered answer. The rating may react to that inconsistency. Conversely, a warm answer may counteract the trace.
- **Content inherited from the unsteered trace.** The clamp preserves that trace’s conclusions and errors. In the inspected prompt, unsteered answers claim to have reviewed a room sketch, whereas hostility-source answers often say the assistant has no access to it. The intervention therefore replaces factual stance as well as tone.
- **Length, completeness, and distance.** Replacing answers changes their lengths and the distance between trace and rating relative to Study 5. These are part of the intervention; an attenuation cannot specifically be attributed to answer hostility.
- **Truncation.** An unfinished answer becomes a forced-complete assistant turn before the rating question. Preserve it exactly for primary analysis, but report the rate specifically among the **400 unsteered clamp answers**. The all-source Study 5 truncation rate is not necessarily that rate.
- **Placement-specific clamps.** Different placements receive different answers. Cross-placement contrasts consequently compare both placement and the answer chosen for that placement.
- **Identical tokens do not mean identical answer representations.** The same answer is processed in different trace contexts. Residual effects can still travel through context-dependent activations at answer positions. This experiment blocks differences in answer tokens, not every computational pathway through answer processing.

The alternatives answer different questions:

| Clamp | Value | Main limitation |
|---|---|---|
| Unsteered answer | Best primary link to Study 5’s observed effect | Inherits baseline content; possible mismatch |
| Fixed generic answer | Tests robustness to a different common answer | Often unresponsive; changes length and conversational meaning |
| No answer | Tests rating immediately after the trace-containing prefix | Changes the conversational stage and distance |
| Source-matched, neutralized answer | Investigates contribution of answer tone | Content still differs across sources; not a common-answer clamp |

I would not replace the primary clamp with a generic or empty answer. Add a precisely specified generic-answer variant as secondary if broader claims are desired. A source-matched neutralization experiment should be described as a separate intervention on answer style, with a frozen transformation procedure.

**3. Estimand and shared-baseline bootstrap**

The proposed difference is statistically sound as a **paired answer-replacement contrast**. Its causal label needs qualification.

For one prompt and placement, write \(Y_s(a)\) for the rating after source \(s\)’s trace and answer \(a\), and \(a_s\) for its stored answer. With \(H\) hostility and \(U\) unsteered:

\[
X^{un}=Y_H(a_H)-Y_U(a_U),
\]

\[
X^{cl}=Y_H(a_U)-Y_U(a_U),
\]

so

\[
M^X=X^{un}-X^{cl}=Y_H(a_H)-Y_H(a_U).
\]

That is an exact decomposition for these realized stimuli and answers. It measures the effect of replacing the hostility-source answer under the hostility trace. It does not establish that answer hostility is the mechanism, nor average over alternative sampled answers.

For control \(C\):

\[
M(C)=
[Y_H(a_H)-Y_H(a_U)]
-
[Y_C(a_C)-Y_C(a_U)].
\]

Thus **control-relative \(M\) is a difference between two answer-replacement effects**. It is not simply the hostility effect mediated through its answer, and the common unsteered answer is not the control source’s own natural answer. Report the two replacement terms separately.

The joint prompt-cluster bootstrap is correct:

- Form all contrasts within each prompt.
- Resample the same 80 prompt IDs jointly across studies, sources, placements, and estimands.
- Preserve repeated draws as repeated clusters.
- Use one fixed bootstrap seed and the same draws for all reported contrasts.

The unsteered cells are **shared observations, not two independent measurements**. My preferred specification is to rerun all 400 as technical validation, then use the original Study 5 unsteered rating as the common analytic baseline once validation passes. Save the rerun values and differences separately. That makes cancellation in \(M^X\) exact and prevents numerical drift from masquerading as an answer effect. State this policy before freezing.

The uncertainty is across prompts, conditional on the stored traces and sampled answers. It does not quantify generation-seed uncertainty, model uncertainty, or independent replication. Joint resampling also does not undo the fact that this study was designed after inspecting Study 5.

**4. Hypotheses, multiplicity, equivalence, power, and reading**

The three-primary Bonferroni scheme is defensible. Requiring every component to pass is an intersection–union rule; additional Bonferroni correction across the components is not needed for the conjunctive claim. Use the exact confidence level \(1-0.05/3\), rather than a rounded constant.

Several decisions remain unresolved:

- The general rule requires X and both controls, but **M1 explicitly requires only the two controls**. Specify the exception or change M1. For the mechanistic question, I would make \(M^X\) a required component and report the control-relative contrasts as specificity evidence.
- Two-sided M1 can pass with opposite signs for its two controls. Define that as “mixed control-relative effects,” not mediation or attenuation.
- Secondary 95% intervals are unadjusted. Label them accordingly and do not treat any-positive-secondary as a multiplicity-controlled conclusion.
- The 90% equivalence intervals are not adjusted for the multiple equivalence claims used in the reading table. Either define a confirmatory equivalence family and adjustment, or explicitly keep these equivalence statements outside familywise-controlled conclusions.
- Retain Study 5’s “small but detectable” category. An effect can exclude zero and remain entirely within ±0.15.

The ±0.15 margin needs substantive justification **separately for residual effects and removed effects**. It is substantial relative to Study 5’s reported historical X of approximately −0.24: a residual approaching 0.15 could retain a considerable fraction of that effect. “Negligible” must not become “absent.”

Power cannot be inferred from Study 5’s effect size alone. The relevant variance is that of each paired contrast, especially the four-term control-relative M. As an illustrative normal approximation, with \(N=80\), a two-sided 98.33% test has approximately 80% power for a 0.15 effect only if the prompt-level contrast SD is about 0.41 or smaller. Joint conjunction power can be lower. Include prospective simulations over plausible paired variances and correlations; four pilot prompts cannot estimate these reliably.

The reading table currently overstates the findings:

- D supported, M equivalent: “The effect persists under this clamp; the change is within the prespecified margin.”
- D supported, M negative: “The clamp attenuates the effect, with residual influence.”
- D equivalent, M negative: “The clamp reduces the previously observed effect to within the residual-effect margin.”

None alone warrants “the earlier effect ran through the answer.” Add positive M/amplification, mixed controls, reversed D, both negligible, and significant-but-equivalent outcomes. For D2, use the **R3 mediation contrast**, not R1’s M1, and acknowledge its secondary status.

The descriptive ratio also needs denominator safeguards. A supported original effect can still yield unstable ratios. Specify treatment of near-zero or sign-changing bootstrap denominators; do not clip ratios to [0,1].

**5. Runtime and binding specification**

One to two hours implies **2.25–4.5 seconds per rating cell**, excluding startup. That is plausible for rating-only evaluation, but unverified. Study 5’s approximately 16-hour run included autoregressive generation, classifier scoring, and extra diagnostic branches; it cannot directly establish Study 6 runtime.

Benchmark the actual fresh-forward rating path with synchronization, representative sequence lengths, memory measurements, and all-source timing. The sampled hostility prefixes were much longer than their unsteered counterparts, so baseline-only timing would be inadequate. Reusing stored classifier scores for unchanged clamp answers avoids unnecessary classifier loading.

The pilot valid-digit-mass criterion currently has **no specified failure disposition**. Define its aggregation—preferably by placement × source as well as overall—and whether failure blocks a placement or the study. A pooled mean can conceal a failing source.

**Required changes before freezing**

1. Specify exact token construction and end-token handling; require full original-branch reconstruction and exact unsteered input equality.
2. Freeze the numerical execution environment and distinguish token mismatch from numerical failure. Validate the 0.01 threshold in the pilot without outcome-driven adjustment.
3. Rename or explicitly qualify “direct” and “mediated” effects as effects under the specified answer-token intervention; remove claims that disappearance establishes exclusive mediation.
4. Define the shared-baseline policy, prompt-level equations, common bootstrap draws, seed, missing-cell rules, and generation-conditional scope.
5. Resolve M1’s component ambiguity, mixed-sign outcomes, multiplicity for equivalence, and the status of secondary claims.
6. Justify ±0.15 for both residual and replacement effects; add prospective precision/power scenarios and unstable-ratio rules.
7. Replace the reading table with qualified, exhaustive outcomes, including amplification, reversal, mixed controls, and significance–equivalence overlap.
8. Define valid-mass failure handling and exact natural-closure, E5, and non-truncated-clamp subset rules. Preserve paired clusters within each analysis.
9. Freeze and synthetically validate analysis code, including exact shared-baseline cancellation, no-change, partial attenuation, amplification, and missing-data cases. Hash inherited code, inputs, masks, and the preregistration itself; specify resumability and logged bug-fix rules.
10. Replace the provisional runtime with a measured estimate and state explicitly that all 1,600 ratings are freshly evaluated, with unsteered reruns serving as validation.

**Optional suggestions**

- Add a frozen generic-answer sensitivity arm; avoid discretionary “if time permits” selection if it will support substantive conclusions.
- Report answer compatibility and conditional answer likelihood descriptively, without excluding awkward hybrids from the primary analysis.
- Consider a common answer across placements for a separate placement-comparison sensitivity.
- Preserve digit logits or log probabilities, full rating-input hashes, and numerical-reproduction differences to simplify later audits.
- Reserve source-matched neutralized answers and multiple answer draws for a follow-up specifically testing tone and generation variability.
