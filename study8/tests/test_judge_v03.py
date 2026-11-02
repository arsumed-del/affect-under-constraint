"""Offline v0.3 checks: synthetic logits and fixtures only."""
import json,tempfile,unittest,ast
from pathlib import Path
import torch
from study8.src.common import ROOT,config,append
from study8.src.judge import expected_score,digit_ids,valid_scores,ITEMS,TEMPLATE,METHOD,item_prompt
from study8.src.validity import calibration_gate,agreement
from study8.src.prepare_pilot_judges import prepare

def judgment(scores,mass=0.9):
    return {'method':METHOD,'scores':scores,'items':{k:{'digit_mass':mass} for k in scores}}

class JudgeTests(unittest.TestCase):
    def test_expected_score(self):
        probs=torch.tensor([.05,.10,.15,.20,.30,.20],dtype=torch.float64)
        r=expected_score(probs.log(),[[i] for i in range(5)])
        self.assertAlmostEqual(r['digit_mass'],.8,places=6)
        self.assertAlmostEqual(r['score'],3.75,places=6)
        self.assertAlmostEqual(r['digit_probabilities']['5'],.3,places=6)
        low=expected_score(torch.tensor([.04,.04,.04,.04,.04,.8]).log(),[[i] for i in range(5)])
        self.assertIsNone(low['score']);self.assertAlmostEqual(low['expected_score'],3.,places=6)
        self.assertIsNotNone(expected_score(torch.zeros(10),[[i] for i in range(5)])['score'])
        self.assertIsNone(expected_score(torch.zeros(11),[[i] for i in range(5)])['score'])
        duplicate=[[0],[0],[1],[2],[3]]
        with self.assertRaises(ValueError):expected_score(torch.zeros(5),duplicate)
        with self.assertRaises(ValueError):expected_score(torch.zeros(5),[[],[1],[2],[3],[4]])
        r=expected_score(torch.zeros(6),[[0,5],[1],[2],[3],[4]])
        self.assertAlmostEqual(r['score'],16/6,places=6)
    def test_digit_ids_and_prompts(self):
        class Tokenizer:
            unk_token_id=99
            def encode(self,s,**kw):return [int(s)] if len(s)==1 else [0,int(s)]
            def convert_tokens_to_ids(self,s):return int(s) if s.isdigit() else 10+int(s[1:])
        self.assertEqual(digit_ids(Tokenizer()),[[k,k+10] for k in range(1,6)])
        tree=ast.parse((ROOT/'judges/judge_probe.py').read_text());env={}
        for n in tree.body:
            if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id in ('ITEMS','TEMPLATE') for t in n.targets):exec(compile(ast.Module(body=[n],type_ignores=[]),'probe','exec'),env)
        self.assertEqual(TEMPLATE,env['TEMPLATE'])
        for k in 'ae':self.assertEqual(ITEMS[k],env['ITEMS'][k])
        text=item_prompt({'id':'hidden-id','prompt':'p','answer':'a'},'b')
        self.assertNotIn('hidden-id',text);self.assertNotIn(ITEMS['a'][1],text)
    def test_calibration_boundaries(self):
        labels=json.loads((ROOT/'calibration/calibration_labels.json').read_text())['labels']
        def rows(separation):
            scores={rid:dict.fromkeys('abcdefgh',3.) for rid in labels}
            for rid,l in labels.items():
                if l['role']=='warm':scores[rid]['a']+=separation
                if l['role']=='flattery':scores[rid]['e']=2.
            return {rid:judgment(s,.5) for rid,s in scores.items()}
        self.assertFalse(calibration_gate({},labels)['passed'])
        self.assertTrue(calibration_gate(rows(.75),labels,'gemma')['passed'])
        self.assertFalse(calibration_gate(rows(.749),labels,'gemma')['passed'])
        self.assertTrue(calibration_gate(rows(.5),labels,'llama')['passed'])
        self.assertFalse(calibration_gate(rows(.499),labels,'llama')['passed'])
        bad=rows(.75);next(iter(bad.values()))['items']['h']['digit_mass']=.499
        self.assertFalse(calibration_gate(bad,labels,'gemma')['passed'])
        # b-h are not Llama calibration items.
        self.assertTrue(calibration_gate(bad,labels,'llama')['passed'])
        bad=rows(.75);next(iter(bad.values()))['items']['a']['digit_mass']=.49
        self.assertFalse(calibration_gate(bad,labels)['passed'])
    def test_agreement_continuous(self):
        x=[1.,2.,3.,4.]
        self.assertTrue(agreement(x,[v+.75 for v in x])['passed'])
        self.assertFalse(agreement(x,[v+.751 for v in x])['passed'])
        self.assertFalse(agreement(x,list(reversed(x)))['passed'])
        self.assertFalse(agreement([3]*48,[3]*48)['passed'])
        self.assertFalse(agreement([None]*48,[3]*48)['passed'])
        self.assertEqual(agreement([1,None,3],[1,2,3])['missing_pairs'],1)
    def test_mass_readout(self):
        r=judgment({'a':3.125,'e':4.25});self.assertEqual(valid_scores(r)['a'],3.125)
        r['items']['a']['digit_mass']=.49;self.assertIsNone(valid_scores(r)['a']);self.assertEqual(valid_scores(r)['e'],4.25)
        with self.assertRaises(RuntimeError):valid_scores({'scores':{'a':3}})
    def test_normalize_continuous_and_missing(self):
        from study8.analysis.analyze import normalize
        cell={'prompt_id':'p','prompt_type':'neutral','source':'hostility','generation_context':'M','context':'M','arm':'generated','cell_key':['p','hostility','M','M','generated'],'ratings':{'O1':{'expected':4.1}},'answer_length':10,'answer_truncated':False,'forced_closure':False}
        mapping={'id':{'cell_key':cell['cell_key']}}
        row=judgment({'a':3.125,'b':2.75})
        result=normalize([cell],{'id':valid_scores(row)},mapping)[0]
        self.assertEqual(result['W'],3.125);self.assertEqual(result['b'],2.75)
        row['items']['a']['digit_mass']=.499
        result=normalize([cell],{'id':valid_scores(row)},mapping)[0]
        self.assertIsNone(result['W']);self.assertEqual(result['O1'],4.1)
    def test_archive_and_resume(self):
        from unittest.mock import patch
        import study8.src.prepare_pilot_judges as migration
        with tempfile.TemporaryDirectory(dir=ROOT/'tests') as tmp:
            d=Path(tmp);p=d/'judge_gemma.jsonl';append(p,{'id':'old','scores':None});before=p.read_bytes()
            (d/'validity.json').write_text('{"pilot_parse_success": {}}')
            with patch.object(migration,'ROOT',d):prepare(d)
            self.assertEqual((d/'judge_v02/judge_gemma.jsonl').read_bytes(),before)
            self.assertFalse(p.exists());self.assertTrue((d/'judge_v02/validity.json').exists())
            append(p,{'id':'new','method':METHOD});after=p.read_bytes()
            prepare(d);self.assertEqual(p.read_bytes(),after)
    def test_launcher(self):
        s=(ROOT/'run_pilot_judges.command').read_text()
        self.assertNotIn('study8.src.runner',s)
        self.assertLess(s.index('--judge gemma'),s.index('--judge llama'))
        # Empty/new v0.3 outputs survive repeated preparation; no archive needed.
        with tempfile.TemporaryDirectory(dir=ROOT/'tests') as tmp:
            d=Path(tmp);p=d/'judge_gemma.jsonl';append(p,{'id':'x','method':METHOD});before=p.read_bytes()
            prepare(d);prepare(d);self.assertEqual(p.read_bytes(),before)
if __name__=='__main__':unittest.main()
