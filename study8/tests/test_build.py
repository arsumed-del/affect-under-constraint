import json,tempfile,unittest
from pathlib import Path
import numpy as np
from study8.src.common import *
from study8.src.assembly import Assembly
from study8.src.projection import observe
from study8.src.validity import agreement,calibration_gate
from study8.src.runner import plan
from study8.analysis.analyze import component_label,estimate,joint_draws

class BuildTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from transformers import AutoTokenizer
        cls.c=config(); cls.t=AutoTokenizer.from_pretrained(cls.c['model']['local_path'],local_files_only=True)
        cls.f=json.loads((ROOT/'framings_s8.json').read_text());cls.a=Assembly(cls.t,cls.f)
    def test_tokens_all_contexts_arms(self):
        a=self.a;tr={'pre_trace_ids':a.enc('<think>'),'trace_ids':a.enc('Consider the request carefully.\n')}
        for context in CONTEXTS:
            prefix,bounds=a.assemble('A test input.',tr,context)
            self.assertEqual(prefix[bounds[0]:bounds[1]],tr['trace_ids'])
            for answer in (a.enc('A useful answer.'),a.enc('A useful answer.<|im_end|>')):
                hist=prefix+answer
                branches={q:a.branch_span(hist,q) for q in ('O1','O3')}
                for q,(ids,(lo,hi)) in branches.items():
                    self.assertEqual(ids[lo:hi],self.f['question_ids'][q]);self.assertEqual(ids[:len(hist)],hist)
                self.assertEqual(a.clamp(prefix,answer),branches['O1'])
                self.assertNotEqual(branches['O1'][0],branches['O3'][0])
            self.assertEqual(prefix[:len(a.prompt_ids('A test input.',context))],a.prompt_ids('A test input.',context))
        self.assertEqual(self.f['system_turn_ids']['N'],[])
        self.assertTrue(self.t.decode(a.prompt_ids('A test input.','N')).startswith('<|im_start|>user\n'))
        self.assertNotIn('<|im_start|>system',self.t.decode(a.prompt_ids('A test input.','N')))
        for g,r in [('N','M'),('M','N')]:
            x,_=a.assemble('A test input.',tr,g);y,b=a.assemble('A test input.',tr,r)
            self.assertNotEqual(x,y);self.assertEqual(y[b[0]:b[1]],tr['trace_ids'])
    def test_plan(self):
        from collections import Counter
        self.assertEqual(Counter(k[-1] for k in plan(prompts('main'))),self.c['arm_counts'])
        self.assertEqual(len(set(plan(prompts('pilot')))),112)
        self.assertFalse(set(p['id'] for p in prompts('main'))&set(self.c['pilot_ids']))
        for p in self.c['seed_maps']['trace']:
            for s in SOURCES:self.assertEqual(self.c['seed_maps']['answer'][p][s],seed('answer',p,s))
        for p in prompts('main')+prompts('pilot'):
            for ctx in CONTEXTS:self.a.prompt_ids(p['text'],ctx)
    def test_projection_read_only_and_cleanup(self):
        import torch
        from types import SimpleNamespace
        torch.manual_seed(1)
        class Tiny(torch.nn.Module):
            def __init__(self):super().__init__();self.emb=torch.nn.Embedding(20,4);self.layer=torch.nn.Linear(4,4);self.head=torch.nn.Linear(4,8)
            def forward(self,x):return SimpleNamespace(logits=self.head(self.layer(self.emb(torch.tensor([x])))))
        m=Tiny().eval();vec=torch.tensor([1.,0.,0.,0.]);ids=[1,2,3,4]
        result=observe(m,m.layer,m,ids,vec,{'question':[1,3],'answer':[0,1]})
        self.assertTrue(result['logits_unchanged']);self.assertFalse(m.layer._forward_hooks)
        expected=m.layer(m.emb(torch.tensor([ids])))[0,1:3,0].detach().tolist()
        self.assertEqual(result['per_token']['question'],expected)
        with self.assertRaises(ValueError):observe(m,m.layer,m,ids,vec,{'bad':[0,100]})
        self.assertFalse(m.layer._forward_hooks)
        handle=m.layer.register_forward_hook(lambda *a:None)
        try:
            with self.assertRaises(RuntimeError):observe(m,m.layer,m,ids,vec,{'x':[0,1]})
        finally:handle.remove()
    def test_resume_corruption_and_paths(self):
        with tempfile.TemporaryDirectory(dir=ROOT/'tests') as temp:
            artifact=Path(temp)/'artifact.json';ensure(artifact,{'terms':[(1,2)]});ensure(artifact,{'terms':[(1,2)]})
            with self.assertRaises(RuntimeError):ensure(artifact,{'terms':[(1,3)]})
            p=Path(temp)/'rows.jsonl';append(p,{'key':[1],'value':3});self.assertEqual(len(verified(p,'key')),1)
            append(p,{'key':[1],'value':4})
            with self.assertRaises(RuntimeError):verified(p,'key')
            p.write_text('{"key":1}')
            with self.assertRaises(RuntimeError):verified(p,'key')
        with self.assertRaises(ValueError):output(REPO/'outside-test')
    def test_equivalence_and_joint_bootstrap(self):
        self.assertEqual(component_label([.02,.08],[.03,.07],1,.25),'small but detectable')
        self.assertEqual(component_label([-.2,.2],[-.15,.15],1,.15),'inconclusive')
        d=joint_draws(['p']*60+['n']*20,100,42)
        self.assertTrue(np.all(d[:,:60].sum(1)==60));self.assertTrue(np.all(d[:,60:].sum(1)==20))
        x=np.zeros((80,3));x[0]=np.nan
        self.assertEqual(estimate(x,d,.95,1,.25)['n'],79)
        rng=np.random.default_rng(100); x=rng.normal(.5,.3,(80,3))
        result=estimate(x,d,.95,1,.25)
        manual=np.quantile((d@x)/80,[.025,.975],axis=0)
        for k,component in enumerate(result['components']):
            np.testing.assert_allclose(component['ci'],manual[:,k])
            self.assertGreater(component['ci'][1],component['ci'][0])
    def test_main_fails_closed(self):
        self.assertFalse((ROOT/'PREREG_APPROVED').exists())
        with self.assertRaises(FileNotFoundError):require_approval()
if __name__=='__main__':unittest.main()
