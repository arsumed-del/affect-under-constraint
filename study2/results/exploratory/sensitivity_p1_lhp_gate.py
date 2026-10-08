# EXPLORATORY (not preregistered): re-run the frozen analysis with the 4.0 coherence gate also applied to LHP.
# Run from study2/: python3 results/exploratory/sensitivity_p1_lhp_gate.py
import json, yaml, copy
from src.analyze import analyze_model
cfg=yaml.safe_load(open('config.yaml'))
c2=copy.deepcopy(cfg); c2['analysis']['coherence_gate_applies_to']=list(cfg['analysis']['coherence_gate_applies_to'])+['lhp']
out={}
for s in ['qwen2.5-3b-instruct','phi-3.5-mini-instruct','llama-3.2-3b-instruct']:
    recs=[json.loads(l) for l in open(f'data/raw/{s}_main.jsonl')]
    r=analyze_model(recs,c2)
    p1=r['outcomes']['P1']
    out[s]={'verdict':p1['verdict'],'excluded':[(e['condition'],e['direction'],e['normalized_alpha']) for e in r['excluded_cells']],
      'stats':{k:(round(v['estimate'],3) if v['estimate'] is not None else None, [round(x,3) if x is not None else None for x in v['ci']]) for k,v in p1['statistics'].items()},
      'tech_slope':(round(r['specificity']['P1']['technicality']['control']['estimate'],3), [round(x,3) for x in r['specificity']['P1']['technicality']['control']['ci']])}
print(json.dumps(out,indent=1))
