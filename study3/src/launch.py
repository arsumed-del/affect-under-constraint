"""Detached project-local jobs; no scheduler and no automatic next stage."""
import os,subprocess,sys,json
from pathlib import Path
from .common import save_once,progress

def main():
    label,module,*args=sys.argv[1:]
    env=os.environ.copy();env['PYTORCH_ENABLE_MPS_FALLBACK']='1';env['PYTHONDONTWRITEBYTECODE']='1'
    log=Path(f'logs/{label}.log').open('xb')
    p=subprocess.Popen(['nohup','../.venv/bin/python','-B','-u','-m',module,*args],stdin=subprocess.DEVNULL,stdout=log,stderr=subprocess.STDOUT,start_new_session=True,env=env)
    c=subprocess.Popen(['nohup','caffeinate','-dimsu','-w',str(p.pid)],stdin=subprocess.DEVNULL,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL,start_new_session=True)
    save_once(f'logs/{label}_job.json',{'pid':p.pid,'caffeinate_pid':c.pid,'module':module,'args':args,'log':f'logs/{label}.log'})
    progress(f'{label} background job started: PID {p.pid}, caffeinate PID {c.pid}; log logs/{label}.log. ETA pending first completed cells.')
if __name__=='__main__':main()
