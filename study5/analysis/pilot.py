"""Descriptive pilot criteria only; never select templates by effect sizes."""
import numpy as np
from study5.src.common import CONDITIONS, verified_rows, input_path

def evaluate(data,cfg):
    ids=cfg['pilot_prompt_ids']
    if not ids or len(ids)!=4:raise ValueError('Four fixed pilot IDs required')
    reference={(r['prompt_id'],r['source'],r['framing']):r for r in verified_rows(input_path(cfg,'pilot_v06_ratings'))}
    out={}
    for c in CONDITIONS:
        group=[r for r in data if r['condition']==c]
        baseline={r['prompt_id']:r['ratings']['sender']['expected'] for r in group if r['source']=='unsteered'}
        complete=len(group)==16 and len({(r['prompt_id'],r['source']) for r in group})==16 and set(baseline)==set(ids)
        sd=float(np.std(list(baseline.values()),ddof=1)) if complete else None
        mass=float(np.mean([r['ratings']['sender']['valid_mass'] for r in group])) if complete else None
        entry={'complete':complete,'baseline_sd':sd,'mean_valid_mass':mass,'reference_differences':None}
        passed=complete and sd>=.15 and mass>=.8
        if c in ['R1','R4'] and complete:
            frame={'R1':'own_native','R4':'own_quoted'}[c]
            diffs={pid:baseline[pid]-reference[pid,'unsteered',frame]['sender_clear']['expected'] for pid in ids}
            entry['reference_differences']=diffs
            entry['reference_mean_difference']=float(np.mean(list(diffs.values())))
            passed=passed and abs(entry['reference_mean_difference'])<=.3
        entry['pass']=bool(passed);out[c]=entry
    return {'all_pass':all(x['pass'] for x in out.values()),'conditions':out,'cells':len(data),
            'estimated_main_hours':float(np.mean([r['seconds'] for r in data])*1600/3600),
            'note':'No automatic revisions or dropped conditions. Review failures under the one-revision rule before author approval.'}
