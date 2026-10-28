"""Deterministic, fully paired synthetic cells; never writes data/raw or main."""
from study6.src.common import SOURCES, CONDITIONS
from study6.src.assembly import plan

PATTERNS={'no_change':(-1.,-1.),'partial_attenuation':(-1.,-.5),
          'full_attenuation':(-1.,0.),'amplification':(-1.,-1.5),
          'reversal':(-1.,.5),'mixed_controls':(-1.,-.5),'missing_cells':(-1.,-.5)}

def generate(pattern,n=80):
    total,direct=PATTERNS[pattern]; ids=[f'synthetic{i:02d}' for i in range(n)]
    old=[]; new=[]
    def rating(value):
        # Exact expected value encoded with endpoint probabilities.
        probs={str(i):0. for i in range(10)}; probs['0']=1-value/9; probs['9']=value/9
        return {'sender':{'expected':value,'valid_mass':.99,'probabilities':probs}}
    for i,p in enumerate(ids):
        base=6.+(i%5)/16
        for c in CONDITIONS:
            for s in SOURCES:
                value=base+(total if s=='hostility' else -1. if pattern=='mixed_controls' and s=='technicality' else 0.)
                old.append({'prompt_id':p,'source':s,'condition':c,'ratings':rating(value),
                            'forced_closure':False,'answer_truncated':False})
    for p,s,c,arm in plan(ids,'main'):
        base=6.+(ids.index(p)%5)/16
        effect=(total-direct)/2 if arm=='swap' else direct if s=='hostility' else 0.
        new.append({'schema':'study6-v0.2-synthetic','cell_key':[p,s,c,arm],'mode':'synthetic',
                    'prompt_id':p,'source':s,'condition':c,'arm':arm,'ratings':rating(base+effect),
                    'answer_length':20,'answer_truncated':False,'EH_answer':None if arm=='generic' else .1,
                    'forced_closure':False})
    if pattern=='missing_cells':
        new=[r for r in new if r['cell_key']!=[ids[0],'hostility','R1','clamp']]
    return old,new,ids
