"""Real tokenizer plus synthetic inference tests; no model generation/readout."""
import copy
import json
import unittest
import numpy as np
from study6.src.common import ROOT, config, input_path, verified_rows, digest
from study6.src.assembly import Assembly,index_original,preflight,plan,answer_for
from study6.src.validity import numerical_check,mass_report,validate_rows
from study6.analysis.analyze import analyze,report,summarize,reading
from study6.tests.synthetic import generate,PATTERNS

class TokenTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from transformers import AutoTokenizer
        cls.cfg=config()
        cls.t=AutoTokenizer.from_pretrained(ROOT/cls.cfg['model']['local_path'],local_files_only=True)
        cls.a=Assembly(cls.t,json.loads(input_path(cls.cfg,'study5_framings').read_text()))
        cls.g=json.loads((ROOT/'generic_answer.json').read_text())['ids']
        cls.maps={m:index_original(verified_rows(input_path(cls.cfg,m+'_cells')),cls.cfg[m+'_prompt_ids']) for m in ('main','pilot')}

    def test_all_original_branches_and_counts(self):
        for mode,count in [('main',1600),('pilot',80)]:
            lookup=self.maps[mode]
            self.assertEqual(preflight(self.a,lookup),count)
            keys=list(plan(self.cfg[mode+'_prompt_ids'],mode))
            self.assertEqual(len(keys),2640 if mode=='main' else 212)
            self.assertEqual(len(keys),len(set(keys)))
            for key in keys:
                answer,_=answer_for(key,lookup,self.g)
                row=lookup[key[:3]]; ids=self.a.rating_input(row,answer)
                lo,hi=row['trace_bounds']; self.assertEqual(ids[lo:hi],row['trace_ids'])
                start=len(row['answer_prefix_ids']); self.assertEqual(ids[start:start+len(answer)],answer)
                if key[1]=='unsteered' and key[-1]=='clamp': self.assertEqual(ids,row['branch_ids']['sender'])

    def test_closure_paths_and_generic(self):
        end=self.a.marker('turn_end'); answer=self.a.enc('A response.')
        self.assertEqual(self.a.end_turn(answer),answer+end)
        self.assertEqual(self.a.end_turn(answer+end),answer+end)
        self.assertEqual(self.a.end_turn(answer+end[:1]),answer+end)
        self.assertEqual(self.a.end_turn([]),end)
        self.assertEqual(self.g,self.a.enc(self.cfg['generic_answer']))
        for mode in self.maps:
            rows=list(self.maps[mode].values())
            self.assertTrue(any(r['answer_truncated'] for r in rows))
            self.assertTrue(any(not r['answer_truncated'] for r in rows))
            for r in rows:
                self.assertEqual(self.a.rating_input(r,r['answer_ids']),self.a.branch(r['answer_prefix_ids']+r['answer_ids'],'sender'))

    def test_fail_closed_tokens_duplicates_missing(self):
        lookup=self.maps['pilot']; key=next(iter(lookup)); broken=dict(lookup)
        broken[key]=copy.deepcopy(lookup[key]); broken[key]['branch_ids']['sender'][0]+=1
        with self.assertRaisesRegex(RuntimeError,'token mismatch'): preflight(self.a,broken)
        rows=list(lookup.values())
        with self.assertRaises(ValueError): index_original(rows+rows[:1],self.cfg['pilot_prompt_ids'])
        with self.assertRaises(ValueError): index_original(rows[1:],self.cfg['pilot_prompt_ids'])

    def test_numerical_failure_and_resume_hash(self):
        lookup=self.maps['pilot']; k=next(iter(lookup)); original=lookup[k]
        row={'cell_key':[*k,'sham'],'prompt_id':k[0],'source':k[1],'condition':k[2],'arm':'sham',
             'ratings':copy.deepcopy(original['ratings']),'manifest_sha256':'test',
             'input_ids_sha256':digest(original['branch_ids']['sender'])}
        self.assertEqual(numerical_check(row,lookup),0.)
        self.assertEqual(validate_rows([row],{tuple(row['cell_key'])},'test',lookup,self.a,self.g),{tuple(row['cell_key'])})
        row['ratings']['sender']['expected']+=.0101
        with self.assertRaisesRegex(RuntimeError,'Numerical replay BLOCKED'): numerical_check(row,lookup)
        row['ratings']=copy.deepcopy(original['ratings']); row['input_ids_sha256']='wrong'
        with self.assertRaisesRegex(RuntimeError,'token hash'): validate_rows([row],{tuple(row['cell_key'])},'test',lookup,self.a,self.g)

class SyntheticTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cfg=config(); cls.results={}; cls.raw={}
        for pattern in PATTERNS:
            old,new,ids=generate(pattern)
            audit={p:{'instructions':False,'negative_characterizations':False} for p in ids}
            cls.results[pattern]=analyze(old,new,cls.cfg,ids,audit)
            cls.raw[pattern]=(old,new,ids)

    def test_planted_patterns(self):
        expected={'no_change':(-1.,0.),'partial_attenuation':(-.5,-.5),'full_attenuation':(0.,-1.),
                  'amplification':(-1.5,.5),'reversal':(.5,-1.5)}
        for pattern,(d,m) in expected.items():
            r=self.results[pattern]['primary']['placements']['R1']; e=r['estimands']
            self.assertEqual(e['D_U']['estimate'],d); self.assertEqual(e['M^X']['estimate'],m)
            self.assertEqual(e['TE']['estimate'],e['D_U']['estimate']+e['M^X']['estimate'])
            self.assertEqual(r['identity_max_abs_error'],0.)
        self.assertEqual(self.results['no_change']['hypotheses']['M1']['status'],'negligible')
        self.assertEqual(self.results['full_attenuation']['hypotheses']['D1']['status'],'negligible')
        self.assertEqual(self.results['reversal']['hypotheses']['D1']['status'],'reversed')
        self.assertIn('amplifies',self.results['amplification']['primary']['placements']['R1']['reading'])
        self.assertIn('attenuates',self.results['partial_attenuation']['primary']['placements']['R1']['reading'])

    def test_mixed_missing_and_brackets(self):
        r=self.results['mixed_controls']['primary']['placements']['R1']
        self.assertEqual(r['M_control_label'],'mixed control-relative effects')
        self.assertTrue(self.results['mixed_controls']['hypotheses']['M1']['supported'])
        for result in self.results.values():
            for placement in result['primary']['placements'].values():
                e=placement['estimands']
                for name,term in [('M_T','replacement_T'),('M_Q','replacement_Q')]:
                    if 'estimate' in e[name]: self.assertEqual(e[name]['estimate'],e['M^X']['estimate']-e[term]['estimate'])
        missing=self.results['missing_cells']['primary']['placements']
        self.assertEqual(missing['R1']['estimands']['D_U']['status'],'not estimable')
        self.assertEqual(missing['R1']['estimands']['M^X']['status'],'not estimable')
        self.assertEqual(missing['R1']['estimands']['TE']['n'],80)
        self.assertTrue(missing['R3']['D']['supported'])

    def test_levels_joint_draws_and_ratio(self):
        r=self.results['partial_attenuation']; e=r['primary']['placements']['R1']['estimands']
        self.assertEqual(e['D_U']['ci_level'],1-.05/3)
        self.assertEqual(e['M^X']['ci_level'],1-.05/3)
        self.assertEqual(e['S']['ci_level'],.95)
        self.assertEqual(r['primary']['placements']['R3']['estimands']['M^X']['ci_level'],.95)
        self.assertEqual(len({v['bootstrap_draws_sha256'] for v in self.results.values()}),1)
        self.assertEqual(r['primary']['placements']['R1']['proportion']['estimate'],.5)
        self.assertEqual(self.results['amplification']['primary']['placements']['R1']['proportion']['estimate'],-.5)

    def test_small_detectable_and_reversed_priority(self):
        s=summarize(np.array([-.1]*80),np.array([-.1]*10000),1-.05/3,'negative')
        self.assertEqual(s['status'],'small but detectable')
        s=summarize(np.array([.1]*80),np.array([.1]*10000),1-.05/3,'negative')
        self.assertEqual(s['status'],'reversed')

    def test_null_denominator_subsets_and_drop(self):
        old,new,ids=copy.deepcopy(self.raw['partial_attenuation'])
        for row in old:
            if row['source']=='hostility': row['ratings']['sender']['expected']+=1.
        for row in old:
            if row['prompt_id']==ids[0] and row['source']=='unsteered' and row['condition']=='R1': row['answer_truncated']=True
            if row['prompt_id']==ids[1]: row['forced_closure']=True
        audit={p:{'instructions':p==ids[2],'negative_characterizations':False} for p in ids}
        r=analyze(old,new,self.cfg,ids,audit,dropped=['R4'])
        self.assertEqual(r['primary']['placements']['R1']['proportion']['status'],'not reported')
        self.assertEqual(r['sensitivity']['completed_answer']['placements']['R1']['n_by_estimand']['D_U'],79)
        self.assertEqual(r['sensitivity']['completed_answer']['placements']['R3']['n_by_estimand']['D_U'],80)
        self.assertEqual(r['sensitivity']['natural_closure']['placements']['R1']['n_by_estimand']['D_U'],79)
        self.assertEqual(r['sensitivity']['E5']['placements']['R1']['n_by_estimand']['D_U'],79)
        self.assertEqual(r['primary']['placements']['R4']['status'],'dropped')
        self.assertIn('95%, unadjusted',report(r))

    def test_valid_mass_placement_failure(self):
        rows=copy.deepcopy(self.raw['no_change'][1])
        for r in rows:
            if r['condition']=='R2' and r['source']=='random': r['ratings']['sender']['valid_mass']=.79
        self.assertEqual(mass_report(rows)['dropped_placements'],['R2'])


class SafetyTests(unittest.TestCase):
    def test_approval_requires_author_record(self):
        from study6.src.approval import require_approval
        from unittest.mock import patch
        self.assertFalse((ROOT/'PREREG_APPROVED').exists())
        with patch('study6.src.approval.verify_inputs'),patch('study6.src.approval.verify_environment'):
            with self.assertRaisesRegex(RuntimeError,'author-created'): require_approval()

    def test_hook_absence_and_inherited_rating_path(self):
        import torch
        from study4.src.runner import assert_no_hooks,Backend as B4
        from study6.src.runner import Backend as B6
        self.assertIs(B6.rating,B4.rating)
        self.assertIs(B6.clean,B4.clean)
        layer=torch.nn.Linear(2,2)
        self.assertTrue(assert_no_hooks(layer))
        hook=layer.register_forward_hook(lambda m,a,o:o)
        try:
            with self.assertRaisesRegex(RuntimeError,'hook-absence'): assert_no_hooks(layer)
        finally: hook.remove()
        self.assertTrue(assert_no_hooks(layer))
        with self.assertRaisesRegex(RuntimeError,'forbids generation'): B6.answer(None)

    def test_two_process_pilot_gate(self):
        from unittest.mock import patch
        from study6.src.validity import pilot_evaluation
        cfg=config(); ids=cfg['pilot_prompt_ids']; mh='synthetic-manifest'
        first=[]
        for k in plan(ids,'pilot'):
            first.append({'cell_key':list(k),'prompt_id':k[0],'source':k[1],'condition':k[2],'arm':k[3],
                          'ratings':{'sender':{'valid_mass':.99}},'process_start_id':'process-one',
                          'seconds':1.,'input_length':100,'peak_driver_memory_bytes':1024})
        second=copy.deepcopy([r for r in first if r['arm']=='sham'])
        # Token/numeric validation is tested on real stored rows separately; isolate start gate here.
        def checked(data,expected,*args): return {tuple(r['cell_key']) for r in data}
        with patch('study6.src.validity.validate_rows',side_effect=checked):
            with self.assertRaisesRegex(RuntimeError,'separate process'): pilot_evaluation(first,second,cfg,mh,{},None,[])
            for r in second:r['process_start_id']='process-two'
            v=pilot_evaluation(first,second,cfg,mh,{},None,[])
            self.assertTrue(v['pass']); self.assertEqual(v['second_sham_cells'],80)
            with self.assertRaisesRegex(RuntimeError,'incomplete'): pilot_evaluation(first,second[:-1],cfg,mh,{},None,[])

class BootstrapTests(unittest.TestCase):
    def test_heterogeneous_paired_draws(self):
        cfg=config(); old,new,ids=generate('partial_attenuation')
        perturb={p:(i-40)/128 for i,p in enumerate(ids)}
        for r in old:
            if r['source']=='hostility': r['ratings']['sender']['expected']+=perturb[r['prompt_id']]
        audit={p:{'instructions':False,'negative_characterizations':False} for p in ids}
        result=analyze(old,new,cfg,ids,audit)
        rng=np.random.default_rng(cfg['bootstrap_seed'])
        indices=(rng.random((10000,80))*80).astype(int)
        expected=np.array([-1+perturb[p] for p in ids])[indices].mean(axis=1)
        te=result['primary']['placements']['R1']['estimands']['TE']
        np.testing.assert_allclose(te['ci'],np.quantile(expected,[.025,.975]),atol=1e-12)
        mx=result['primary']['placements']['R1']['estimands']['M^X']
        level=1-.05/3
        np.testing.assert_allclose(mx['ci'],np.quantile(expected+.5,[(1-level)/2,(1+level)/2]),atol=1e-12)
        self.assertEqual(result['bootstrap_resamples'],10000)

if __name__=='__main__': unittest.main()
