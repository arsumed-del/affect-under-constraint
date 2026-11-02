import unittest,json
from transformers import AutoTokenizer
from study7.src.common import *
from study7.src.assembly import Assembly
from study7.src.runner import load,plan,validate_resume,reproduce
from study6.src.assembly import Assembly as Clamp
class Build(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.c=config();cls.t=AutoTokenizer.from_pretrained(ROOT/cls.c['model']['local_path'],local_files_only=True);cls.a=Assembly(cls.t,json.loads((ROOT/'framings_s7.json').read_text()))
 def test_real_rows(self):
  count=0
  for mode in ['pilot','main']:
   prompts,traces,orig,clamps=load(self.c,mode)
   clamp=Clamp(self.t,json.loads(path(self.c,'study5_framings').read_text()))
   for p,s,l,arm in plan(self.c,mode):
    ids,bounds=self.a.assemble(prompts[p]['text'],traces[p,s],l)
    self.assertEqual(ids[bounds[0]:bounds[1]],traces[p,s]['trace_ids'])
    if l=='G':self.assertEqual(ids,orig[p,s]['answer_prefix_ids'])
    if l=='N':self.assertEqual(ids[:3],self.a.marker('user_start'))
    ans=orig[p,s]['answer_ids'] if arm=='generated' else orig[p,'unsteered']['answer_ids']
    branch=self.a.branch(ids+ans,'O1')
    if l=='G':
     self.assertEqual(branch,orig[p,s]['branch_ids']['sender'] if arm=='generated' else clamp.rating_input(orig[p,s],ans))
     if arm=='fixed':self.assertEqual(digest(branch),clamps[p,s]['input_ids_sha256'])
    count+=1
  self.assertEqual(count,2016)
 def test_N_template(self):
  text=self.t.apply_chat_template([{'role':'user','content':'CHECK'}],tokenize=False,add_generation_prompt=True,enable_thinking=True)
  self.assertNotIn('system',text);self.assertTrue(text.startswith('<|im_start|>user\n'))
 def test_counts_seeds(self):
  self.assertEqual(len(plan(self.c,'main')),1920);self.assertEqual(len(self.c['check_ids']),16)
 def test_reproduction_stops(self):
  p,t,o,c=load(self.c,'pilot');k=next(iter(o));r=dict(level='G',prompt_id=k[0],source=k[1],arm='generated',answer_ids=[],ratings={'O1':{'expected':0}},cell_key=[])
  with self.assertRaises(RuntimeError):reproduce(r,o,c)
if __name__=='__main__':unittest.main()
