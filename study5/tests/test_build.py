import copy
import json
import unittest
from types import SimpleNamespace
from transformers import AutoTokenizer
from study5.src.common import ROOT, CONDITIONS, SOURCES, config, verified_rows, input_path, rows, verify_inputs, digest, output_path
from study5.src.assembly import Assembly
from study5.src.runner import validate_resume, Backend, run_cell
from study4.src.runner import Assembly as Study4Assembly, assert_no_hooks

class BuildTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cfg=config();cls.f=json.loads((ROOT/'framings_s5.json').read_text())
        cls.t=AutoTokenizer.from_pretrained(str(ROOT/cls.cfg['model']['local_path']),local_files_only=True)
        cls.a=Assembly(cls.t,cls.f)
        cls.old=Study4Assembly(cls.t,json.loads(input_path(cls.cfg,'study4_framings').read_text()))
    def test_hashes_and_plan(self):
        verify_inputs(self.cfg)
        self.assertEqual(len(self.cfg['main_prompt_ids']),80)
        self.assertEqual(len(set(self.cfg['diagnostic_prompt_ids'])),16)
        self.assertTrue(set(self.cfg['diagnostic_prompt_ids'])<=set(self.cfg['main_prompt_ids']))
    def test_all_real_prefixes(self):
        # Independent explicit formulas, not another traversal of manifest recipes.
        count=0
        for mode in ['main','pilot']:
            prompts={p['id']:p['text'] for p in rows(input_path(self.cfg,mode+'_prompts'))}
            cells={(r['prompt_id'],r['source'],r['framing']):r for r in verified_rows(input_path(self.cfg,mode+'_cells'))}
            for tr in verified_rows(input_path(self.cfg,mode+'_traces')):
                pid,source=tr['trace_key']; prompt=prompts[pid]
                e=self.a.enc;m=self.a.marker
                head=self.old.base(prompt)+m('turn_end')+m('assistant_start')
                middle=m('turn_end')+m('user_start')+e(self.f['segment_text']['C'])+m('turn_end')+m('assistant_start')
                n=e(self.f['segment_text']['N']);sep=m('answer_separator');op=m('think_open');cl=m('think_close');trace=tr['trace_ids'];nl=e('\n\n')
                manual={
                    'R1':head+tr['pre_trace_ids']+trace+cl+sep,
                    'R1-M':head+op+nl+cl+sep+n+middle+tr['pre_trace_ids']+trace+cl+sep,
                    'R2':head+op+nl+cl+trace+sep+n+middle+m('empty_thinking'),
                    'R3':head+op+nl+trace+cl+sep+n+middle+m('empty_thinking'),
                    'R4':self.old.base(prompt)+e(self.f['quoted_before'].format(label=self.f['labels']['own_quoted']))+trace+e(self.f['quoted_after'])+m('turn_end')+m('assistant_start')+m('empty_thinking')}
                for c in CONDITIONS:
                    ids,bounds=self.a.assemble(prompt,tr,c)
                    self.assertEqual(ids,manual[c]);self.assertEqual(ids[bounds[0]:bounds[1]],trace)
                    history=ids+[1234]
                    for q in self.f['questions']:
                        branch=self.a.branch(history,q)
                        expected=history+m('turn_end')+m('user_start')+e(self.f['questions'][q])+m('turn_end')+e(self.f['rating_prefix'])
                        self.assertEqual(branch,expected)
                        self.assertEqual(branch[bounds[0]:bounds[1]],trace)
                    if c in ['R1','R4']:
                        frame={'R1':'own_native','R4':'own_quoted'}[c]
                        self.assertEqual(ids,self.old.assemble(prompt,tr,frame)[0])
                        self.assertEqual(ids,cells[pid,source,frame]['answer_prefix_ids'])
                        self.assertEqual(self.cfg['answer_seeds'][mode]['/'.join([pid,source,c])],cells[pid,source,frame]['answer_seed'])
                    count+=1
                # Exact single closing-token move, stronger than stripping all delimiters.
                r2=manual['R2'].copy();r3=manual['R3']
                pos=len(head)+len(op)+len(nl)
                moved=r2.pop(pos);self.assertEqual([moved],cl)
                r2.insert(pos+len(trace),moved)
                self.assertEqual(r2,r3)
        self.assertEqual(count,3200)
    def test_end_turn_and_tokenizer_guard(self):
        end=self.a.marker('turn_end')
        self.assertEqual(self.a.end_turn([42]+end),[42]+end)
        self.assertEqual(self.a.end_turn([42,end[0]]),[42]+end)
        bad=copy.deepcopy(self.f);bad['segment_ids']['N']=[1]
        with self.assertRaises(ValueError):Assembly(self.t,bad)
    def test_hooks_and_no_trace_generation(self):
        import torch
        model=torch.nn.Linear(2,2)
        self.assertTrue(assert_no_hooks(model))
        h=model.register_forward_hook(lambda *a:None)
        with self.assertRaises(RuntimeError):assert_no_hooks(model)
        h.remove();self.assertTrue(assert_no_hooks(model))
        with self.assertRaises(RuntimeError):Backend.trace(None)
    def test_resume_and_write_boundary(self):
        key=('p','hostility','R3');row={'cell_key':list(key),'manifest_sha256':'ok'}
        self.assertEqual(validate_resume([row],{key},'ok'),{key})
        for rr,keys,manifest in [([row,row],{key},'ok'),([row],set(),'ok'),([row],{key},'changed')]:
            with self.assertRaises(RuntimeError):validate_resume(rr,keys,manifest)
        with self.assertRaises(ValueError):output_path(ROOT.parent/'forbidden')
    def test_independent_branches_and_schema(self):
        class FakeBackend:
            def __init__(self,t):
                self.m=SimpleNamespace(tokenizer=t,model=SimpleNamespace(generation_config=SimpleNamespace(eos_token_id=151645)))
                self.torch=SimpleNamespace(mps=SimpleNamespace(synchronize=lambda:None))
                self.classifier=SimpleNamespace(score=lambda text:{'eh':.1,'error':None})
                self.calls=[];self.events=[];self.peak=0
            def answer(self,ids,seed,cap):
                self.events.append({'operation':'answer','hook_absent':True,'initial_cache':None});return [1234,151645]
            def rating(self,ids,labels=list('0123456789')):
                self.calls.append(ids);self.events.append({'operation':'readout','hook_absent':True,'initial_cache':None})
                out={'probabilities':{v:1/len(labels) for v in labels},'valid_mass':1.,'argmax':labels[0]}
                if labels==list('0123456789'):out['expected']=4.5
                return out
        tr=verified_rows(input_path(self.cfg,'main_traces'))[0];pid,source=tr['trace_key']
        prompt=next(p for p in rows(input_path(self.cfg,'main_prompts')) if p['id']==pid)
        for condition in CONDITIONS:
            b=FakeBackend(self.t)
            r=run_cell(b,self.a,self.cfg,'main',prompt,source,condition,tr,{pid},'test')
            self.assertEqual(len(b.calls),5)
            history=r['answer_prefix_ids']+r['answer_ids']
            for ids in b.calls:self.assertEqual(ids[:len(history)],history)
            self.assertEqual(r['answer_seed'],self.cfg['answer_seeds']['main']['/'.join(r['cell_key'])])
            self.assertFalse(r['answer_truncated'])
            self.assertEqual(len(r['replay_assertions']),6)

if __name__=='__main__':unittest.main()
