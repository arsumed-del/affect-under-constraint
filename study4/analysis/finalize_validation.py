"""Recover the summary from saved, verified simulations; no new draws."""
import json
import numpy as np
from study4.src.common import ROOT, save, verified_rows
out=ROOT/'validation/synthetic'
replicates=verified_rows(out/'null_coverage_replicates.jsonl')
assert len(replicates)==500 and [r['replicate'] for r in replicates]==list(range(500))
coverage={}
for name,component in replicates[0]['components'].items():
    nominal=component['ci_level']
    actual=sum(r['components'][name]['ci'][0]<=0<=r['components'][name]['ci'][1] for r in replicates)/500
    se=float(np.sqrt(nominal*(1-nominal)/500))
    coverage[name]={'nominal':nominal,'coverage':actual,'monte_carlo_se':se,'within_4_mc_se':bool(abs(actual-nominal)<=4*se)}
assert all(c['within_4_mc_se'] for c in coverage.values())
patterns={k:json.loads((out/(k+'_analysis.json')).read_text())['primary']['hypotheses'] for k in ['planted','p1_only','p2','s5','writer_only','notes_only','null']}
from .analyze import conjunction
support={}
for h in ['P1','P2','S1','S2','S3','S4','S5','comparator']:
    support[h]=sum(conjunction([v for k,v in r['components'].items() if k.startswith(h+':')])=='supported' for r in replicates)/500
summary={'patterns':patterns,'boundary_cases':json.loads((out/'boundaries.json').read_text()),'null_datasets':500,'bootstrap_resamples_per_dataset':10000,'coverage':coverage,'null_conjunction_support_rate':support,'passed':True,'coverage_tolerance':'4 binomial Monte Carlo standard errors; diagnostic, no tuning or reruns','recovery':'Summary reconstructed from complete checksummed saved results after NumPy boolean JSON export error; no simulation rerun.'}
save(out/'summary.json',summary)
print(json.dumps(summary,indent=2))
