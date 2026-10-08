"""Synthetic schema fixtures and estimator checks; never reads test prompts."""
import os
os.environ['PYTORCH_ENABLE_MPS_FALLBACK']='1'
import copy
import json
from pathlib import Path
import numpy as np
import yaml
from .analyze import analyze,report,slope,bic_gap,DOSES,prepare
from .schema import validate,SCHEMA_VERSION
from .model_utils import cell_seed
from .common import append,progress,save_once

def generate(planted,cfg):
    model='Qwen/Qwen2.5-3B-Instruct'
    template={'schema_version':SCHEMA_VERSION}
    rng=np.random.default_rng(cfg['experiment']['seed'])
    heterogeneity=rng.normal(0,.15,80)
    heterogeneity-=heterogeneity.mean()
    prompt_offset=rng.normal(0,.1,80)
    prompt_offset-=prompt_offset.mean()
    records=[]
    for condition in ['neutral','warm_constraint']:
        grid=[('none',0)]+[(d,j) for d in ['hostility','technicality','random'] for j in range(1,6)]
        for direction,j in grid:
            a=DOSES[j]
            noise=rng.normal(0,1,(80,6))
            noise-=noise.mean(axis=0,keepdims=True)
            for p in range(80):
                active=bool(planted and direction=='hostility')
                scale=(1+heterogeneity[p]) if active else 0
                warm=condition=='warm_constraint'
                lhp=prompt_offset[p]+noise[p,0]*.025+scale*(1.1*a+.75*max(a-.5,0))
                eh=.14+prompt_offset[p]*.04+noise[p,1]*.006+scale*(.045 if warm else .20)*a
                ent=3.2+noise[p,2]*.03+scale*(.8 if warm else .1)*a
                leak=noise[p,3]*.012+scale*(.14 if warm else 0)*a
                carry=noise[p,4]*.015-scale*(.9 if warm else .1)*a
                ew=.2+noise[p,5]*.005+scale*(.06 if warm else 0)*a
                r=copy.deepcopy(template)
                pid=f's{p:02d}'
                r.update(origin='synthetic_planted' if planted else 'synthetic_null',model=model,prompt_id=pid,prompt_type='synthetic',prompt_text=f'Synthetic prompt {p}; not an experimental test prompt.',condition=condition,direction=direction,alpha=float(.16*a),alpha_index=j,normalized_alpha=float(a),seed=cell_seed(model,pid,condition,direction,j),text='Synthetic placeholder text; no language-model generation.',prompt_token_ids=[1,2,3],token_ids=list(range(10,30)),n_tokens=20,lhp=float(lhp),opener_logprobs={'hostile':[-2+lhp/2]*12,'warm':[-2-lhp/2]*12},eh=float(eh),ew=float(ew),entropy=float(ent),entropy_per_token=[float(ent)]*20,perplexity=float(1.5*(1+.1*a)),ppl_ratio=float(1+.1*a),eh_first_quarter=float(eh-leak/2),eh_last_quarter=float(eh+leak/2),leak_timecourse=float(leak),leak_lexical=0,offchannel={'emoji_count':0,'non_latin_token_count':0},rating_text_only=5.,rating_hidden=float(5+carry),carryover=float(carry),rating_prefix={'template_prefix_exact':True,'identical_visible_ids':True},timings={'generation_seconds':0.,'ratings_seconds':0.,'openers_seconds':0.,'cell_total_seconds':0.},peak_driver_memory=0,provenance={'synthetic':True,'seed':cfg['experiment']['seed'],'no_test_prompt_data':True})
                def score(value):
                    return {'eh':float(value),'ew':float(ew),'probabilities':{'anger':float(value*.7),'disgust':float(value*.3),'joy':float(ew),'neutral':float(1-value-ew)},'error':None}
                r['classifier']={'full':score(eh),'first_quarter':score(eh-leak/2),'last_quarter':score(eh+leak/2)}
                records.append(validate(r))
    return records

def direct_checks(records,cfg):
    ids,arrays,_,_=prepare(records,cfg)
    rng=np.random.default_rng(1831)
    counts=np.bincount(rng.integers(0,80,80),minlength=80)
    weights=np.stack([np.ones(80),counts])
    warm=arrays[('warm_constraint','hostility')]
    y=warm['lhp_z']
    actual=slope(y,weights)
    for k,w in enumerate(weights):
        selected=np.repeat(np.arange(80),w.astype(int))
        xx=np.tile(DOSES,len(selected))
        yy=y[selected].ravel()
        expected=np.linalg.lstsq(np.column_stack([np.ones(len(xx)),xx]),yy,rcond=None)[0][1]
        assert np.isclose(actual[k],expected,rtol=1e-10,atol=1e-10)
    g=(warm['lhp_z']-warm['lhp_z'][:,[0]])-(warm['eh_z']-warm['eh_z'][:,[0]])
    delta,bp=bic_gap(g,weights)
    for k,w in enumerate(weights):
        selected=np.repeat(np.arange(80),w.astype(int))
        xx=np.tile(DOSES,len(selected)); yy=g[selected].ravel(); n=len(yy)
        x=np.column_stack([np.ones(n),xx])
        residual=yy-x@np.linalg.lstsq(x,yy,rcond=None)[0]
        linear_bic=n*np.log(np.dot(residual,residual)/n)+3*np.log(n)
        candidates=[]
        for knot in DOSES[1:-1]:
            x=np.column_stack([np.ones(n),xx,np.maximum(xx-knot,0)])
            residual=yy-x@np.linalg.lstsq(x,yy,rcond=None)[0]
            candidates.append(n*np.log(np.dot(residual,residual)/n)+5*np.log(n))
        assert np.isclose(delta[k],linear_bic-min(candidates),atol=1e-8)
        selected_index=list(DOSES[1:-1]).index(bp[k])
        assert np.isclose(candidates[selected_index],min(candidates),atol=1e-8)
    # Study 2 analysis gate is 4.0; calibration margin is 3.0.
    altered=copy.deepcopy(records)
    for r in altered:
        if r['direction']=='hostility' and r['condition']=='warm_constraint' and r['alpha_index']==5:
            r['ppl_ratio']=4.01
    _,gated,_,excluded=prepare(altered,cfg)
    assert len(excluded)==1
    for field in ['lhp','carryover','entropy']:assert np.isfinite(gated[('warm_constraint','hostility')][field][:,-1]).all()
    for field in ['eh','ew','leak_timecourse','S2_eh_component','S5_eh_component']:assert np.isnan(gated[('warm_constraint','hostility')][field][:,-1]).all()
    ungated_cfg=copy.deepcopy(cfg);ungated_cfg['analysis']['coherence_gate_applies_to']=[]
    _,ungated,_,_=prepare(altered,ungated_cfg)
    assert np.isfinite(ungated[('warm_constraint','hostility')]['leak_timecourse'][:,-1]).all()
    # Short outputs must make time-course leakage missing without losing M1.
    altered=copy.deepcopy(records)
    r=next(r for r in altered if r['direction']=='hostility' and r['condition']=='warm_constraint' and r['alpha_index']==3)
    r['n_tokens']=7;r['token_ids']=r['token_ids'][:7]
    _,short,_,_=prepare(altered,cfg)
    assert np.isnan(short[('warm_constraint','hostility')]['leak_timecourse'][0,3])
    assert np.isfinite(short[('warm_constraint','hostility')]['lhp'][0,3])

def main():
    import hashlib
    from .analyze import generality,summary
    from .run_main import approval_check
    cfg=yaml.safe_load(Path('config.yaml').read_text())
    Path('data/synthetic').mkdir(parents=True,exist_ok=True)
    checks={};analyses={}
    for name,planted in [('planted',True),('null',False)]:
        base=generate(planted,cfg)
        assert len(base)==2560
        direct_checks(base,cfg)
        records=[]
        for spec in cfg['models']:
            for r in base:
                row=copy.deepcopy(r);row['model']=spec['id'];row['seed']=cell_seed(row['model'],row['prompt_id'],row['condition'],row['direction'],row['alpha_index']);records.append(row)
        path=Path(f'data/synthetic/{name}.jsonl')
        if path.exists():assert [json.loads(s) for s in path.read_text().splitlines()]==records
        else:
            with path.open('x') as f:
                for r in records:f.write(json.dumps(r,allow_nan=False)+'\n')
        progress(f'Stage 2b: {name} synthetic fixture: three models, 80 synthetic prompts/model, 2560 cells/model. Starting 10,000 prompt bootstraps; ETA a few minutes.')
        result=analyze(records,cfg)
        save_once(f'results/synthetic_{name}.json',result)
        with Path(f'results/synthetic_{name}.md').open('x') as f:f.write(report(result))
        actual={m['model']:{h:o['verdict'] for h,o in m['outcomes'].items()} for m in result['models']}
        assert all(o['supported']==planted for m in result['models'] for o in m['outcomes'].values()),actual
        assert all(g['general']==planted for g in result['generality'].values())
        analyses[name]=result;checks[name]=actual
        progress(f'Stage 2b: {name} synthetic verdict checks passed.')
    records=[json.loads(s) for s in Path('data/synthetic/planted.jsonl').read_text().splitlines()]
    last=cfg['models'][-1]['id']
    for r in records:
        if r['model']==last and r['condition']=='warm_constraint' and r['direction']=='technicality' and r['alpha_index']==5:r['ppl_ratio']=4.01
    with Path('data/synthetic/excluded_top.jsonl').open('x') as f:
        for r in records:f.write(json.dumps(r,allow_nan=False)+'\n')
    result=analyze(records,cfg)
    save_once('results/synthetic_excluded_top.json',result)
    with Path('results/synthetic_excluded_top.md').open('x') as f:f.write(report(result))
    gated=next(m for m in result['models'] if m['model']==last)
    assert all(gated['outcomes'][h]['verdict']=='supported' for h in ['P1','P2'])
    assert gated['missingness']['warm_constraint|technicality']['leak_timecourse']['observed_by_dose'][-1]==0
    assert gated['missingness']['warm_constraint|technicality']['carryover']['observed_by_dose'][-1]==80
    assert all(g['general'] and len(g['eligible_models'])==3 and not g['not_estimable_models'] for g in result['generality'].values())
    statuses={m['model']:'PASS' for m in result['models']}
    statuses[result['models'][0]['model']]='EXCLUDED (manipulation check failed)'
    statuses[result['models'][1]['model']]='EXCLUDED (manipulation check failed)'
    reduced=generality(result['models'],statuses)
    assert all(not g['general'] and len(g['eligible_models'])==1 for g in reduced.values())
    # Hostility leakage drops an incoherent top dose, but latent statistics retain it.
    host_gate=copy.deepcopy([r for r in records if r['model']==cfg['models'][0]['id']])
    for r in host_gate:
        if r['condition']=='warm_constraint' and r['direction']=='hostility' and r['alpha_index']==5:r['ppl_ratio']=4.01
    host_result=analyze(host_gate,cfg)
    hm=host_result['models'][0]
    assert hm['missingness']['warm_constraint|hostility']['leak_timecourse']['observed_by_dose'][-1]==0
    expected=np.mean([r['leak_timecourse'] for r in host_gate if r['condition']=='warm_constraint' and r['direction']=='hostility' and r['alpha_index'] in [3,4]])
    assert np.isclose(hm['outcomes']['S3']['statistics']['S3']['estimate'],expected)
    baseline=next(m for m in analyses['planted']['models'] if m['model']==hm['model'])
    for h in ['P1','P2','S1','S4']:assert hm['outcomes'][h]==baseline['outcomes'][h]
    save_once('results/synthetic_hostility_gate.json',host_result)
    # Genuine missing required measurements, rather than coherence, cause non-estimability.
    unavailable=copy.deepcopy(host_gate)
    for r in unavailable:
        if r['condition']=='warm_constraint' and r['direction']=='technicality':r['lhp']=None;r['carryover']=None
        if r['condition']=='warm_constraint' and r['direction']=='none':r['lhp']=None
    missing_required=analyze(unavailable,cfg)
    assert all(missing_required['models'][0]['outcomes'][h]['verdict']=='not estimable' for h in ['P1','P2'])
    save_once('results/synthetic_required_missing.json',missing_required)
    # Required control superiority cannot be replaced by a null control CI.
    matched=copy.deepcopy([r for r in records if r['model']==cfg['models'][0]['id']])
    host={(r['prompt_id'],r['condition'],r['alpha_index']):r for r in matched if r['direction']=='hostility'}
    for r in matched:
        if r['direction']=='technicality':
            h=host[(r['prompt_id'],r['condition'],r['alpha_index'])]
            r['lhp']=h['lhp'];r['carryover']=h['carryover'];r['rating_hidden']=r['rating_text_only']+r['carryover']
    matched_result=analyze(matched,cfg)
    assert all(not matched_result['models'][0]['outcomes'][h]['supported'] for h in ['P1','P2'])
    save_once('results/synthetic_matched_control.json',matched_result)
    # Paired missingness and short generations: omissions remain explicit.
    missing=copy.deepcopy(matched)
    target=next(r for r in missing if r['condition']=='warm_constraint' and r['direction']=='technicality' and r['alpha_index']==5)
    target['carryover']=None;target['rating_hidden']=None
    missing_result=analyze(missing,cfg)
    assert missing_result['models'][0]['paired_missingness']['P2_control_missing_prompt_pairs']['technicality']==1
    vals=np.r_[0,np.arange(10000)]
    assert np.allclose(summary(vals,.975)['ci'],np.quantile(vals[1:],[.0125,.9875]),rtol=0,atol=1e-10)
    # These are direct guard calls: never read test prompts or invoke main mode.
    original=Path.cwd();fixture=original/'data/synthetic/absent_approval_guard';fixture.mkdir(exist_ok=True)
    try:
        os.chdir(fixture)
        try:approval_check()
        except RuntimeError as exc:assert 'PREREG_APPROVED is absent' in str(exc)
        else:raise AssertionError('Main approval guard failed')
    finally:os.chdir(original)
    save_once('results/stage2b_checks.json',{'fixture_verdicts':checks,'independent_ols_bic':'PASS','incoherent_control_primary_retained':'PASS','hostility_S3_gate':'PASS','configuration_driven_gate':'PASS','required_missing_not_estimable':'PASS','generality_eligible_models':'PASS','matched_controls_not_supported':'PASS','paired_missingness':'PASS','short_generation_leakage_missing':'PASS','primary_975_percentiles':'PASS','stage3_locked':'PASS'})
    lines=['# Study 2 Stage 2b synthetic checks','','**PASS.** Planted and null fixtures each have three model IDs, 80 synthetic prompt IDs per model, and 2,560 cells per model in the Stage 3 schema. No test-prompt generations were performed.','','| Fixture | P1 | P2 | S1–S5 | Generality |','|---|---|---|---|','| Planted | supported in all three | supported in all three | all supported | both general |','| Null | not supported in all three | not supported in all three | none supported | neither general |','| Incoherent top-dose technicality, one model | supported | supported | text leakage cell excluded | three eligible models support both |','','All fixtures used 10,000 prompt-cluster bootstrap resamples. Primary intervals are 97.5%; secondary intervals are 95%. Independent direct least-squares calculations matched the weighted OLS and BIC estimators. Amendment 3.1 checks confirm that an incoherent top-dose control retains P2, an incoherent hostility top dose is excluded from S3, and P1/P2/S1/S4 are unchanged by that gate. The field list is read from config. Genuine missing required measurements remain not estimable. Additional checks covered identical-strength controls (primary verdicts fail), pairwise missingness, fewer-than-eight-token leakage, and the fewer-than-two-eligible-model generality rule. The absent-approval guard refused Stage 3. Detailed estimates, intervals and omissions are saved in the accompanying JSON files.','','Synthetic behavior validates implementation, not the experimental predictions.']
    with Path('results/stage2b_synthetic_check.md').open('x') as f:f.write('\n'.join(lines)+'\n')
    progress('Stage 2b synthetic checks passed. Timing and final source audit remain before freeze.')
if __name__=='__main__':main()
