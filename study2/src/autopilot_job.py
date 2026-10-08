"""Durable detached job wrapper: one lock, append-only outcomes, no scientific choices."""
import os
os.environ['PYTORCH_ENABLE_MPS_FALLBACK']='1'
os.environ['PYTHONDONTWRITEBYTECODE']='1'
import argparse,fcntl,json,subprocess,sys,time,traceback
from pathlib import Path
from .common import append

def main():
    p=argparse.ArgumentParser();p.add_argument('--id',required=True);p.add_argument('command',nargs=argparse.REMAINDER);a=p.parse_args()
    lock=Path('logs/autopilot_worker.lock').open('a')
    fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
    command=a.command[1:] if a.command and a.command[0]=='--' else a.command
    append('logs/autopilot_job_events.jsonl',{'id':a.id,'event':'started','pid':os.getpid(),'time':time.time(),'command':command})
    try:
        child=subprocess.Popen(command,stdin=subprocess.DEVNULL)
        append('logs/autopilot_job_events.jsonl',{'id':a.id,'event':'child','pid':child.pid,'time':time.time()})
        code=child.wait()
    except Exception:
        code=1;traceback.print_exc()
    append('logs/autopilot_job_events.jsonl',{'id':a.id,'event':'finished','returncode':code,'time':time.time()})
    sys.exit(code)
if __name__=='__main__':main()
