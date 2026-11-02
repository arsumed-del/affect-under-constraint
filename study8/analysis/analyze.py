import argparse,json,warnings
import numpy as np
from study8.src.common import *
from study8.src.validity import agreement
from study8.src.judge import valid_scores
CONTROLS=('unsteered','technicality','random')

def component_label(ci,eq,sign,margin):
    predicted=ci[0]>0 if sign>0 else ci[1]<0
    opposite=ci[1]<0 if sign>0 else ci[0]>0
    negligible=margin is not None and eq[0]>-margin and eq[1]<margin
    if predicted:return 'small but detectable' if negligible else 'supported'
    if opposite:return 'reversed'
    if negligible:return 'negligible'
    return 'inconclusive'

def conjunction(components):
    labs=[x['label'] for x in components]
    if all(x in ('supported','small but detectable') for x in labs):return 'small but detectable' if all(x=='small but detectable' for x in labs) else 'supported'
    if all(x=='reversed' for x in labs):return 'reversed'
    if all(x in ('negligible','small but detectable') for x in labs):return 'negligible'
    if 'reversed' in labs and any(x in ('supported','small but detectable') for x in labs):return 'mixed'
    return 'inconclusive'

def estimate(matrix,draws,confidence,sign,margin,eligible=None,bounds=None):
    # Paired complete-case exclusion across components within this conjunction.
    eligible=np.ones(len(matrix),bool) if eligible is None else np.array(eligible,bool)
    valid=np.isfinite(matrix).all(axis=1)&eligible
    n=int(valid.sum())
    if not n:return {'label':'not estimable','supported':False,'n':0,'missing_prompts':int(eligible.sum()),'components':[]}
    values=np.where(valid[:,None],matrix,0)
    counts=draws@valid.astype(float)
    boot=np.divide(draws@values,counts[:,None],out=np.full((len(draws),matrix.shape[1]),np.nan),where=counts[:,None]>0)
    ci=np.nanquantile(boot,[(1-confidence)/2,1-(1-confidence)/2],axis=0)
    eq=np.nanquantile(boot,[.05,.95],axis=0)
    point=np.mean(matrix[valid],axis=0);components=[]
    for k,value in enumerate(point):
        comp={'estimate':float(value),'ci':ci[:,k].tolist(),'ci90':eq[:,k].tolist(),'label':component_label(ci[:,k],eq[:,k],sign,margin)}
        if bounds is not None:comp['worst_case_bound_all_prompts']=[float(np.mean(b[eligible,k])) for b in bounds]
        components.append(comp)
    label=conjunction(components)
    return {'label':label,'supported':label in ('supported','small but detectable'),'n':n,'missing_prompts':int(eligible.sum()-n),'bootstrap_empty_resamples':int((counts==0).sum()),'confidence':confidence,'margin':margin,'components':components}

def joint_draws(types,resamples,seed):
    rng=np.random.default_rng(seed);counts=np.zeros((resamples,len(types)))
    for kind in sorted(set(types)):
        ix=np.flatnonzero(np.array(types)==kind)
        counts[:,ix]=rng.multinomial(len(ix),np.ones(len(ix))/len(ix),size=resamples)
    return counts

def analyze(records,prompt_info,clean=None,judge_valid=True,resamples=10000,bootstrap_seed=20261030):
    ids=[p['id'] for p in prompt_info];types=[p['type'] for p in prompt_info];index={}
    for r in records:
        k=(r['prompt_id'],r['source'],r['generation_context'],r['context'],r['arm'])
        if k in index:raise ValueError('Duplicate analysis cell')
        if r['prompt_id'] not in ids:raise ValueError('Unexpected prompt (pilot contamination)')
        index[k]=r
    draws=joint_draws(types,resamples,bootstrap_seed)
    tests={};miss={}
    for s in SOURCES:
        for c in CONTEXTS:
            count=sum(index.get((p,s,c,c,'generated'),{}).get('W') is None for p in ids)
            miss[f'{s}/{c}']={'missing':count,'total':len(ids),'fraction':count/len(ids),'flag':count/len(ids)>.05}
    crossover_missing={}
    for g,c in [('N','M'),('M','N')]:
        for s in SOURCES:
            count=sum(index.get((p,s,g,c,'crossover'),{}).get('W') is None for p in ids)
            crossover_missing[f'{s}/{g}->{c}']={'missing':count,'total':len(ids),'fraction':count/len(ids),'flag':count/len(ids)>.05}
    def Y(p,s,g,r,arm,o):
        v=index.get((p,s,g,r,arm),{}).get(o)
        return np.nan if v is None else float(v)
    def simple(o,c,arm='generated',g=None,control='unsteered'):
        g=c if g is None else g
        return [(1,'hostility',g,c,arm,o),(-1,control,g,c,arm,o)]
    def subtract(a,b):return a+[(-coef,*rest) for coef,*rest in b]
    def test(name,terms,sign=1,primary=False,eligible=None):
        matrix=[];lower=[];upper=[]
        warmth=all(t[-1]=='W' for term in terms for t in term)
        for p in ids:
            row=[];lo=[];hi=[]
            for term in terms:
                row.append(sum(coef*Y(p,s,g,r,arm,o) for coef,s,g,r,arm,o in term))
                lows=[];highs=[]
                for coef,s,g,r,arm,o in term:
                    val=Y(p,s,g,r,arm,o)
                    if np.isfinite(val):lows.append(coef*val);highs.append(coef*val)
                    else:lows.append(coef*(1 if coef>0 else 5));highs.append(coef*(5 if coef>0 else 1))
                lo.append(sum(lows));hi.append(sum(highs))
            matrix.append(row);lower.append(lo);upper.append(hi)
        outcome=terms[0][0][-1];margin={'W':.25,'O1':.15}.get(outcome)
        result=estimate(np.array(matrix),draws,1-.05/3 if primary else .95,sign,margin,eligible,(np.array(lower),np.array(upper)) if warmth else None)
        result.update(terms=terms,interpretability='interpretable' if not warmth or judge_valid else 'not interpretable: judge gate failed',unadjusted_secondary=not primary)
        if warmth and not judge_valid:result['supported']=False
        tests[name]=result
    def simples(o,c,arm='generated'):return [simple(o,c,arm,control=b) for b in CONTROLS]
    def interactions(o,a,b):return [subtract(simple(o,a,control=s),simple(o,b,control=s)) for s in CONTROLS]
    primary_specs=[('RF1',simples('W','M'),1),('RF2',simples('O1','M'),-1),('RF3',interactions('W','M','N'),1)]
    for name,term,sign in primary_specs:test(name,term,sign,True)
    test('S1',interactions('W','M','P'))
    for c in ('P','N'):
        test('S2_W_'+c,simples('W',c));test('S2_O1_'+c,simples('O1',c),-1)
    for o in ('W','O1'):
        def crossed(g,r):return simple(o,r,'generated' if g==r else 'crossover',g)
        for g in ('N','M'):test(f'S3_{o}_replay_at_{g}',[subtract(crossed(g,'M'),crossed(g,'N'))])
        for r in ('N','M'):test(f'S3_{o}_formation_at_{r}',[subtract(crossed('M',r),crossed('N',r))])
        # Average formation/replay paths sum exactly to the total RF3 U contrast.
        for name,terms in [('formation',[subtract(crossed('M',r),crossed('N',r)) for r in ('N','M')]),('replay',[subtract(crossed(g,'M'),crossed(g,'N')) for g in ('N','M')])]:
            test(f'S3_{o}_{name}_average',[[(coef/2,*rest) for term in terms for coef,*rest in term]])
    for c in ('M','N'):test('S4_'+c,simples('O1',c,'fixed_answer'),-1)
    for c in CONTEXTS:test('S5_'+c,simples('alignment',c))
    for o in ('W','length','d'):
        test('S6_'+o,[[(1,'unsteered','M','M','generated',o),(-1,'unsteered','N','N','generated',o)]])
    for name,term,sign in primary_specs:
        test('S7_'+name,term,sign,eligible=[p in set(clean or []) for p in ids])
        tests['S7_'+name]['underpowered']=clean is not None and len(clean)<20
        if clean is None:tests['S7_'+name]['audit_status']='not supplied'
    for o in ('b','c','d','e'):test('S8_'+o,[simple(o,'M')])
    supported=lambda n:tests[n]['supported']
    descriptive={}
    for o in ('O3','EH','joy','answer_alignment','length','answer_truncated','forced_closure','f','g','h'):
        descriptive[o]={}
        for s in SOURCES:
            for c in CONTEXTS:
                v=np.array([Y(p,s,c,c,'generated',o) for p in ids]);ok=np.isfinite(v)
                descriptive[o][f'{s}/{c}']={'n':int(ok.sum()),'mean':float(v[ok].mean()) if ok.any() else None}
    return {'hypotheses':tests,'Level_A':supported('RF1') and supported('RF2'),'Level_B':all(supported(n) for n in ('RF1','RF2','RF3')),'kindness_specific_Level_B':all(supported(n) for n in ('RF1','RF2','RF3','S1')),'judge_valid':judge_valid,'W_missingness':miss,'W_crossover_missingness':crossover_missing,'W_missingness_flag':any(v['flag'] for v in [*miss.values(),*crossover_missing.values()]),'common_clean_n':None if clean is None else len(clean),'bootstrap':{'seed':bootstrap_seed,'resamples':resamples,'joint':True,'strata':{k:types.count(k) for k in set(types)}},'descriptive':descriptive,'interpretation':'RF3 is total context-by-steering interaction. Level A/B do not establish a defense, concealment, or private affect. S1-S8 are descriptive and unadjusted.'}

def normalize(cells,judgments,mapping):
    by_key={tuple(mapping[rid]['cell_key']):score for rid,score in judgments.items() if rid in mapping}
    out=[]
    for r in cells:
        j=by_key.get(tuple(r['cell_key'])) or {};proj=r.get('projection') or {};cl=r.get('classifier') or {}
        out.append({**{k:r[k] for k in ('prompt_id','prompt_type','source','generation_context','context','arm')},'W':j.get('a'),**{k:j.get(k) for k in 'bcdefgh'},'O1':r['ratings']['O1']['expected'],'O3':r['ratings'].get('O3',{}).get('expected'),'alignment':proj.get('means',{}).get('O1_question'),'answer_alignment':proj.get('means',{}).get('answer'),'EH':cl.get('eh'),'joy':cl.get('ew'),'length':r['answer_length'],'answer_truncated':r['answer_truncated'],'forced_closure':r['forced_closure']})
    return out

def markdown(result):
    lines=['# Study 8 analysis','',result['interpretation'],'',f'Level A: {result["Level_A"]}. Level B: {result["Level_B"]}. Judge valid: {result["judge_valid"]}.','', '| Test | Label | n | Component estimates and intervals |','|---|---|---:|---|']
    for name,v in result['hypotheses'].items():
        values='; '.join(f'{x["estimate"]:.3f} [{x["ci"][0]:.3f}, {x["ci"][1]:.3f}]' for x in v['components'])
        lines.append(f'| {name} | {v["label"]}; {v["interpretability"]} | {v["n"]} | {values} |')
    lines+=['','All detailed missingness, worst-case bounds, margins, audit counts, agreement and descriptive results are in analysis.json. S7 uses a post-intervention subset.','',f'Warmth missingness flag: {result["W_missingness_flag"]}. Clean prompts: {result["common_clean_n"]}.']
    return '\n'.join(lines)+'\n'

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--mode',choices=['main'],default='main');args=ap.parse_args();c=config();require_approval();verify(c);d=ROOT/'data'/args.mode
    # Read audit receipt and verify it before opening any outcome file.
    audit=json.loads((d/'audit_receipt.json').read_text())
    for field,file in [('codes_sha256','audit_codes.json'),('map_sha256','audit_map.json'),('traces_sha256','traces.jsonl')]:
        if audit[field]!=sha(d/file):raise RuntimeError('Audit changed after committing subset')
    complete=json.loads((d/'qwen_complete.json').read_text())
    if sha(d/'cells.jsonl')!=complete['cells_sha256'] or sha(d/'traces.jsonl')!=complete['traces_sha256']:raise RuntimeError('Completed Qwen data changed')
    cells=verified(d/'cells.jsonl','cell_key')
    from study8.src.runner import plan
    if {tuple(r['cell_key']) for r in cells}!=set(plan(prompts('main'))):raise RuntimeError('Main run incomplete or unexpected cells')
    mapping=json.loads((d/'judge_map.json').read_text())
    cell_map={tuple(r['cell_key']):r for r in cells if r['arm']!='fixed_answer'}
    if {tuple(r['cell_key']) for r in mapping.values()}!=set(cell_map) or len(mapping)!=len(cell_map):raise RuntimeError('Judge mapping incomplete or duplicate')
    for row in mapping.values():
        if cell_map[tuple(row['cell_key'])]['row_sha256']!=row['row_sha256']:raise RuntimeError('Judge mapping source changed')
    sample=json.loads((d/'agreement_sample.json').read_text())
    if len(sample)!=80 or len(set(sample))!=80:raise RuntimeError('Agreement sample size mismatch')
    cal={r['id']:r for r in rows(ROOT/'calibration/calibration_items.jsonl')}
    blind=json.loads((d/'judge_inputs.json').read_text()); all_inputs={**cal,**{r['id']:r for r in blind}}
    js={}
    for j in ('gemma','llama'):
        rr=verified(d/f'judge_{j}.jsonl','id')
        expected=set(cal)|(set(mapping) if j=='gemma' else set(sample))
        if {r['id'] for r in rr}!=expected:raise RuntimeError('Judge run incomplete: '+j)
        for row in rr:
            if row['input_sha256']!=digest(all_inputs[row['id']]):raise RuntimeError('Judge input changed')
        js[j]={r['id']:valid_scores(r) for r in rr}
    pilot=json.loads((ROOT/'data/pilot/validity.json').read_text())
    result=analyze(normalize(cells,js['gemma'],mapping),prompts('main'),audit['clean_prompt_ids'],pilot['judge_gate_passed'],c['analysis']['resamples'],c['seeds']['bootstrap'])
    result['post_main_agreement']=agreement(*[[js[j].get(i,{}).get('a') if js[j].get(i) else None for i in sample] for j in ('gemma','llama')])
    result['post_main_agreement_interpretation']='Diagnostic only; primary judge is not replaced.'
    result['audit_counts']={f'{s}/{ctx}':{k:sum(r[k] for r in audit['joined'] if r['trace_key'][1:]==[s,ctx]) for k in ('negative_user','hostile_instruction','kindness_strategy','rating_reference','forced_closure')} for s in SOURCES for ctx in CONTEXTS}
    ensure(d/'analysis.json',result)
    p=output(d/'analysis.md');text=markdown(result)
    if p.exists():assert p.read_text()==text
    else:p.write_text(text)
if __name__=='__main__':main()
