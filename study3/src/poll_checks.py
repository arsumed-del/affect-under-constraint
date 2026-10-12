"""Read-only job polling plus progress log; no scientific calculations."""
import os,statistics,time
from .common import rows,progress
rs=rows('data/checks/stageA_cells.jsonl')
full=[r['total_seconds'] for r in rs if r['mode']=='think' and r['dose_fraction']==1]
job=__import__('json').load(open('logs/stageA_job.json'))
alive=[]
for key in ['pid','caffeinate_pid']:
 try:os.kill(job[key],0);alive.append(key)
 except ProcessLookupError:pass
if len(rs)<80 and full:
 estimate=(80-len(rs))*statistics.mean(full)/60
 progress(f'Stage A: {len(rs)}/80 cells saved; {80-len(rs)} full-dose thinking cells remain. Block-specific ETA about {estimate:.1f} min. Active: {", ".join(alive)}.')
else:print({'saved':len(rs),'active':alive})
