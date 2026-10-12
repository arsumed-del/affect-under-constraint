"""Model-free numerical-path and access-guard tests; no approval files created."""
from contextlib import contextmanager
from types import SimpleNamespace
from pathlib import Path
from unittest.mock import patch
import copy
import torch
from .study3_spec import config,approval_guard,plan
from .main_model import Model
from .common import save_once,progress

class Cache:
    def __init__(self,n):self.n=n
    def get_seq_length(self):return self.n
class Tokenizer:
    def encode(self,text,**kwargs):return [4,8] if text=='</think>\n\n' else [8]
    def decode(self,ids,**kwargs):return ' '.join(map(str,ids))


def pulse_case(forced,pulse):
    cfg=copy.deepcopy(config());cfg['generation']['thinking_cap']=2 if forced else 5
    cfg['generation']['answer_cap']=5
    obj=object.__new__(Model);obj.thinking=True;obj.open_think=3;obj.close_think=4;obj.device='cpu';obj.tokenizer=Tokenizer();obj.ids=lambda messages:[1,2]
    events=[];active=[False]
    @contextmanager
    def steering(*args):
        active[0]=True
        try:yield
        finally:active[0]=False
    obj.steering=steering
    class Fake:
        generation_config=SimpleNamespace(eos_token_id=9)
        def __call__(self,input_ids,past_key_values=None,use_cache=True):
            ids=input_ids[0].tolist();events.append({'ids':ids,'fresh':past_key_values is None,'steering':active[0]})
            next_id={2:3,3:6,6:4,4:7,8:7,7:9,9:9}[ids[-1]]
            logits=torch.full((1,1,32),-100.);logits[0,0,next_id]=100.
            return SimpleNamespace(logits=logits,past_key_values=Cache((past_key_values.n if past_key_values else 0)+len(ids)))
    obj.model=Fake()
    g=obj.generate_main([],123,cfg,.0175,1.,torch.ones(3),pulse)
    fresh=[e for e in events if e['fresh']]
    assert len(fresh)==(2 if pulse else 1)
    if pulse:
        assert fresh[1]['steering'] is False and fresh[1]['ids']==g.answer_prefix_ids
        assert fresh[1]['ids'][-2:]==[4,8]
        idx=events.index(fresh[1]);assert all(not e['steering'] for e in events[idx:])
        assert g.steered_positions==5 and g.answer_ids==[7,9]
        assert g.pulse_cache_discarded and g.first_answer_from_unsteered_reencoding
    else:assert all(e['steering'] for e in events)
    assert not active[0] and g.thinking_truncated==forced
    return {'forced':forced,'pulse':pulse,'events':events,'sampled_tokens':g.sampled_tokens,'status':'PASS'}

def guards():
    cfg=config();calls=[];expected_hash='a'*64
    def sha_stub(path):calls.append(('hash',str(path)));assert 'test_prompts' not in str(path);return expected_hash
    cases={}
    for name,approved,deposit,body,dep in [
        ('missing approval',False,True,'','10.5281/zenodo.12345'),
        ('wrong hash',True,True,cfg['preregistration']+' config.yaml '+'b'*64,'10.5281/zenodo.12345'),
        ('missing deposit',True,False,cfg['preregistration']+' config.yaml '+expected_hash,''),
        ('missing DOI',True,True,cfg['preregistration']+' config.yaml '+expected_hash,'not deposited'),
        ('valid guard',True,True,cfg['preregistration']+' config.yaml '+expected_hash,'Published DOI 10.5281/zenodo.12345')]:
        def exists(p):
            calls.append(('exists',str(p)));assert 'test_prompts' not in str(p)
            return approved if p.name=='PREREG_APPROVED' else deposit
        def read(p,*a,**kw):
            calls.append(('read',str(p)));assert p.name in ['PREREG_APPROVED','ZENODO_DEPOSIT.md']
            return body if p.name=='PREREG_APPROVED' else dep
        with patch.object(Path,'is_file',exists),patch.object(Path,'read_text',read),patch('src.study3_spec.sha',sha_stub),patch('src.study3_spec.verify_manifest'):
            try:approval_guard(cfg);passed=True
            except RuntimeError:passed=False
        assert passed==(name=='valid guard');cases[name]='PASS'
    return {'cases':cases,'all_accesses':calls,'files_created':False,'test_file_touched':False}

def main():
    result={'pulse_cases':[pulse_case(f,p) for f in [False,True] for p in [False,True]],'guards':guards(),'plan_main_cells':len(list(plan(range(80)))),'plan_dry_cells':len(list(plan(range(2))))}
    assert result['plan_main_cells']==1360 and result['plan_dry_cells']==34
    save_once('results/stageD_engineering.json',result)
    progress('Stage D engineering checks PASS: natural/forced pulse cache discard and unsteered boundary; regular path unchanged; approval/hash/deposit guards fail closed without test-file access.')
if __name__=='__main__':main()
