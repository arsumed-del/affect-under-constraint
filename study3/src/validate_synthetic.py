"""Fixed-seed, model-free v0.4 validation. No empirical outcomes used to tune tests."""
import copy,json
from pathlib import Path
import numpy as np
from .study3_spec import config,plan
from .analyze import analyze,table
from .common import append,save_once,progress,sha
from .check_common import guarded

SEED=20261008

def generate(kind,seed):
    rng=np.random.default_rng(seed);ids=[f's3t{i:02}' for i in range(80)];data=[]
    baseline={(p,m):7+rng.normal(0,.15) for p in ids for m in ['direct','think']}
    offsets={p:rng.normal(0,.015) for p in ids}
    for p,m,route,d,a in plan(ids):
        z=baseline[p,m];text=z+(rng.normal(0,.08) if a else 0);full=text+(rng.normal(0,.05) if a else 0)
        ea=.25+offsets[p]+rng.normal(0,.025);et=.25+offsets[p]+rng.normal(0,.025) if m=='think' else None
        lhp=rng.normal(0,.1)
        if kind in ['P1','truncation','floor20'] and d=='hostility' and m=='think' and route=='regular':full-=1.2*a;text-=.8*a
        if kind=='P2' and d=='hostility' and m=='think' and route=='regular':et+=.45*a
        if kind=='S5' and d=='hostility' and route=='pulse':text-=1.2;full-=1.2
        if kind=='hidden_only' and route=='pulse':text=z;full=z-(1.2 if d=='hostility' else 0)
        trunc=kind=='truncation' and m=='think' and a>0 and int(p[-2:])<65
        trunc|=kind=='floor20' and m=='think' and a>0 and int(p[-2:])<60
        rating={'R_zero':z,'text_only':text,'full':full,'hidden':full,'difference':full-text,'trajectory':{'token_ids':[9,10],'R_full':[0.,0.],'R_text':[0.,0.]},'rating_prefix_ids':[151644,77091,198,151667,271,151668,271],'rating_prefix_text':'<|im_start|>assistant\n<think>\n\n</think>\n\n','turn2_direct_steering':False,'identical_visible_ids':True}
        data.append({'schema_version':'study3-v0.4','model':'Qwen/Qwen3-4B','prompt_id':p,'mode':m,'route':route,'direction':d,'dose_fraction':a,'alpha':.0175*a,'seed':seed,'condition':'warm_constraint','prompt_ids':[1,2],'token_ids':[3,4,5] if m=='think' else [5],'text':'SYNTHETIC','seconds':1.,'peak_driver_memory':0,'thinking':'SYNTHETIC' if m=='think' else '','answer':'SYNTHETIC','thinking_ids':[3] if m=='think' else [],'answer_ids':[5],'forced_ids':[],'thinking_truncated':bool(trunc),'answer_truncated':False,'thinking_enabled':m=='think','sampled_tokens':3 if m=='think' else 1,'answer_prefix_ids':[1,2,3,4] if m=='think' else [1,2],'entropy':1.,'token_entropies':[1.]* (3 if m=='think' else 1),'pulse_cache_discarded':route=='pulse','first_answer_from_unsteered_reencoding':route=='pulse','answer_perplexity':2.,'trace_perplexity':2. if m=='think' else None,'answer_classifier':{'eh':ea,'ew':.3,'error':None},'EH_answer':ea,'EW':.3,'trace_windows':[{'start':0,'token_count':1,'eh':et,'error':None}] if m=='think' else [],'EH_trace':et,'LHP':lhp,'opener_logprobs':{'hostile':[-2+lhp]*12,'warm':[-2.]*12},'ratings':rating,'R_full':full,'R_text':text,'R_zero':z,'C':full-z,'X':text-z,'H':full-text,'total_seconds':1.,'provenance':{'synthetic':True,'generator_seed':seed,'scenario':kind}})
    return data

def main():
    cfg=config();root=Path('data/synthetic/v04');root.mkdir(parents=True,exist_ok=True)
    results={};checks={}
    for index,kind in enumerate(['P1','P2','S5','null','truncation','floor20','hidden_only','missing','missing_baseline','missing_prompt','gate']):
        index={'P1':0,'P2':1,'S5':2,'null':3,'truncation':4,'floor20':5,'hidden_only':6,'missing':7,'gate':8,'missing_baseline':9,'missing_prompt':10}[kind]
        data=generate('P2' if kind=='gate' else 'P1' if kind=='missing' else kind,SEED+index)
        if kind=='missing':data=[r for r in data if not (r['prompt_id']=='s3t00' and r['mode']=='think' and r['route']=='regular' and r['direction']=='hostility' and r['dose_fraction']==1)]
        if kind=='missing_prompt':data=[r for r in data if r['prompt_id']!='s3t79']
        if kind=='missing_baseline':data=[r for r in data if not (r['prompt_id']=='s3t00' and r['mode']=='direct' and r['dose_fraction']==0)]
        if kind=='gate':
            for r in data:
                if r['mode']=='think' and r['route']=='regular' and r['direction']=='random' and r['dose_fraction']==.5:r['trace_perplexity']=7.
        path=root/(kind+'.jsonl')
        if not path.exists():
            for r in data:append(path,r)
        else:assert [json.loads(l) for l in path.read_text().splitlines()]==data
        output=analyze(data,cfg)
        save_once(root/(kind+'_analysis.json'),output);results[kind]=output
        if kind in ['P1','P2','S5']:assert output['hypotheses'][kind]['verdict']=='supported',kind
        if kind=='null':assert all(h['verdict']=='not supported' for h in output['hypotheses'].values())
        if kind=='hidden_only':assert output['hypotheses']['S5']['verdict']=='not supported'
        if kind=='missing':assert output['hypotheses']['P1']['verdict']=='not estimable'
        if kind=='missing_prompt':
            assert output['missing_prompt_count']==1
            assert all(h['verdict']=='not estimable' for h in output['hypotheses'].values())
        if kind=='missing_baseline':
            assert output['hypotheses']['S4']['verdict']!='not estimable'
            assert output['hypotheses']['P1']['verdict']=='not estimable'
        if kind=='gate':
            assert output['hypotheses']['P2']['verdict']=='not estimable'
            assert output['hypotheses']['P1']['verdict']!='not estimable'
            assert output['hypotheses']['S3']['verdict']!='not estimable'
        if kind=='truncation':
            assert output['hypotheses']['P1']['verdict']=='supported'
            assert all(e['n_prompts']==15 and e['result']['verdict']=='not estimable' for e in output['exploratory']['E3'].values())
        if kind=='floor20':assert all(e['n_prompts']==20 and e['result']['verdict']!='not estimable' for e in output['exploratory']['E3'].values())
        progress(f'Stage D synthetic {kind}: checks passed; 10,000 bootstrap resamples.')
    # Independently verify OLS and group median boundary without choosing a new test seed.
    data=generate('P2',SEED+1);host=[r for r in data if r['mode']=='think' and r['route']=='regular' and (r['direction']=='hostility' or r['dose_fraction']==0)]
    x=np.array([r['dose_fraction'] for r in host]);y=np.array([r['EH_trace']-r['EH_answer'] for r in host]);X=np.column_stack([np.ones(len(x)),x])
    reference=float(np.linalg.lstsq(X,y,rcond=None)[0][1]);actual=results['P2']['hypotheses']['P2']['components']['hostility']['estimate'];assert abs(reference-actual)<1e-12
    boundary=copy.deepcopy(data)
    for r in boundary:
        if r['mode']=='think':r['trace_perplexity']=6.
    assert analyze(boundary,cfg,resamples=1000,exploratory=False)['hypotheses']['P2']['verdict']!='not estimable'
    boundary[0]['answer_perplexity']=100.
    assert analyze(boundary,cfg,resamples=1000,exploratory=False)['hypotheses']['P2']['verdict']!='not estimable'
    checks.update(ols_reference_error=abs(reference-actual),strict_greater_than_six=True,median_not_single_outlier=True)
    null_path=root/'null_replicates.jsonl';done={r['replicate']:r for r in (__import__('src.common',fromlist=['rows']).rows(null_path))}
    for i in range(200):
        if i in done:continue
        data=generate('null',SEED+1000+i)
        result=analyze(data,cfg,resamples=1000,seed=SEED+10000+i,exploratory=False)
        record={'replicate':i,'data_seed':SEED+1000+i,'bootstrap_seed':SEED+10000+i,'bootstrap_resamples':1000,'P1':result['hypotheses']['P1']['verdict'],'P2':result['hypotheses']['P2']['verdict']}
        append(null_path,record);done[i]=record
        if (i+1)%20==0:progress(f'Stage D null calibration: {i+1}/200 replicates complete.')
    rates={p:sum(r[p]=='supported' for r in done.values())/200 for p in ['P1','P2']}
    nominal=1-cfg['analysis']['primary_ci'];passed=all(r<=nominal+1e-12 for r in rates.values())
    summary={'status':'PASS' if passed else 'FAIL','seed':SEED,'replicates':200,'null_rates':rates,'nominal':nominal,'checks':checks,'scenario_verdicts':{k:{h:v['verdict'] for h,v in r['hypotheses'].items()} for k,r in results.items()}}
    save_once('results/stageD_synthetic.json',summary)
    out=['# Stage D — synthetic validation','','All data are synthetic; no model calls or test-prompt reads. Full structure: 80 prompts × 17 cells = 1,360 records. The missing-cell case intentionally has 1,359. Fixed generator seed base 20261008; no seed or estimator search. Each scenario uses 10,000 prompt-cluster bootstrap resamples and the specified CI levels. Null calibration uses 200 independently seeded datasets with 1,000 resamples each.','','| Scenario | P1 | P2 | S5 |','|---|---|---|---|']
    for k,r in results.items():out.append('| '+k+' | '+' | '.join(r['hypotheses'][p]['verdict'] for p in ['P1','P2','S5'])+' |')
    out+=['',f'Primary null false-positive rates: P1 {rates["P1"]:.3%}; P2 {rates["P2"]:.3%}. Nominal level: {nominal:.3%}. Requirement: **{summary["status"]}**. These are observed finite-simulation rates, not a proof of universal calibration.','', 'Additional checks passed: hidden-only pulse change does not support S5; a required gated trace group makes P2 not estimable while ratings and LHP remain estimable; a missing required row makes P1 not estimable; E3 excludes to 15 common prompts and is not estimable, while exactly 20 meets the floor; confirmatory P1 still uses all truncated cells; direct least-squares P2 estimate agrees within 1e-12; threshold exactly 6 passes; a single extreme perplexity does not exclude a group whose median passes.','', 'Scenario data and full outputs: `data/synthetic/v04/`. Null datasets can be reconstructed exactly from the recorded generator and per-replicate seeds. No inferential analysis was run on calibration outputs.','', '## Planted P1 table','',table(results['P1'])]
    Path('results/stageD_synthetic.md').write_text('\n'.join(out)+'\n')
    assert passed,f'Null false-positive validation failed: {rates}; nominal={nominal}'
    progress('Stage D synthetic validation PASS: planted effects, missing/gated groups, truncation floor, and 200 null replicates verified.')
if __name__=='__main__':guarded(main)
