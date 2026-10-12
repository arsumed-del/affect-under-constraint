"""Unfrozen operational monitor: status and hourly data commits, no inference changes."""
import json,os,time,subprocess,statistics,traceback
from pathlib import Path
from .common import rows,progress
from .study3_spec import config,plan,key

def main():
    cfg=config();job=json.loads(Path('logs/stageE_main_job.json').read_text());last_commit=0
    baseline=rows(cfg['outputs']['dry_run'])
    proxies={(m,route):statistics.mean(r['total_seconds'] for r in baseline if r['mode']==m and r['route']==route) for m,route in [('direct','regular'),('think','regular'),('think','pulse')]}
    while True:
        data=rows(cfg['outputs']['raw']);done={key(r) for r in data}
        # IDs are only available after the approved main run has begun. Estimate
        # remaining counts by fixed design totals, without independently opening prompts.
        estimates={}
        for group,total in [(('direct','regular'),560),(('think','regular'),560),(('think','pulse'),240)]:
            observed=[r['total_seconds'] for r in data if (r['mode'],r['route'])==group]
            rate=statistics.mean(observed) if len(observed)>=20 else proxies[group]
            estimates[group]=(total-len(observed))*rate
        eta=sum(estimates.values())/3600
        try:os.kill(job['pid'],0);alive=True
        except ProcessLookupError:alive=False
        progress(f'Stage E main: {len(data)}/1360 cells saved; stratified ETA about {eta:.1f} hours. Worker PID {job["pid"]} {"active" if alive else "exited"}; frozen files unchanged by monitor.')
        if time.time()-last_commit>=3600 or not alive:
            paths=['data/raw/qwen3-4b_main.jsonl','STATUS.md']
            paths=[p for p in paths if Path(p).exists()]
            subprocess.run(['git','add','--',*paths],check=True)
            subprocess.run(['git','commit','-m',f'Stage E checkpoint: {len(data)} of 1360 cells','--',*paths],check=True)
            last_commit=time.time()
        if not alive:
            if len(data)!=1360:
                error=f'Main worker exited with {len(data)}/1360 cells; inspect logs/stageE_main.log before any restart.'
                progress('BLOCKED — '+error)
                with Path('DEVIATIONS.md').open('a') as f:f.write('\n## Stage E worker stopped\n\n'+error+'\n')
            return
        time.sleep(60)
if __name__=='__main__':main()
