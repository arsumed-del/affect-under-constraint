"""Lightweight progress estimate for the calibration-only dry run."""
import json,os,statistics
from .common import rows,progress
rs=rows('data/dry_run/qwen3-4b_v04.jsonl');job=json.load(open('logs/stageD_dry_v04_job.json'))
alive=[]
for field in ['pid','caffeinate_pid']:
 try:os.kill(job[field],0);alive.append(f'{field}={job[field]}')
 except ProcessLookupError:pass
think=[r['total_seconds'] for r in rs if r['mode']=='think']
if len(rs)<34:
 estimate=(34-len(rs))*statistics.mean(think)/60 if think else None
 progress(f'Stage D dry run: {len(rs)}/34 saved. Thinking-cell proxy ETA {estimate:.1f} min; pulse re-encoding and direction lengths may differ. Synthetic/engineering checks PASS. Active: {", ".join(alive)}.')
else:print({'cells':len(rs),'active':alive})
