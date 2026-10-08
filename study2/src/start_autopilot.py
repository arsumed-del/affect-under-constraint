"""Install services only in the Study 2 folder; register for this login session."""
import os,json,plistlib,subprocess,sys,time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
os.chdir(ROOT)
sys.path.insert(0,str(ROOT))
from src.common import progress,save_once,verify_manifest

def service_pid(label):
    r=subprocess.run(['launchctl','list',label],capture_output=True,text=True)
    import re
    match=re.search(r'"PID"\s*=\s*(\d+)',r.stdout)
    return int(match.group(1)) if match else None

def main():
    verify_manifest('results/specification_hashes.sha256');verify_manifest('results/analysis_frozen.sha256')
    folder=ROOT/'services';folder.mkdir(exist_ok=True);(ROOT/'logs').mkdir(exist_ok=True)
    suffix=str(os.getuid())+'.study2.affect-steering'
    definitions={
        'keepawake':{'Label':suffix+'.keepawake','ProgramArguments':['/usr/bin/caffeinate','-dimsu']},
        'autopilot':{'Label':suffix+'.autopilot','ProgramArguments':['/usr/bin/nohup',str(ROOT.parent/'.venv/bin/python'),'-B','-u','-m','src.autopilot']},
    }
    pids={}
    for name,definition in definitions.items():
        definition.update(WorkingDirectory=str(ROOT),RunAtLoad=True,KeepAlive=True,ThrottleInterval=60,StandardOutPath=str(ROOT/'logs'/f'{name}.log'),StandardErrorPath=str(ROOT/'logs'/f'{name}.log'),EnvironmentVariables={'PYTORCH_ENABLE_MPS_FALLBACK':'1','PYTHONDONTWRITEBYTECODE':'1'})
        path=folder/(name+'.plist')
        if path.exists():assert plistlib.loads(path.read_bytes())==definition,'Existing service definition changed'
        else:path.write_bytes(plistlib.dumps(definition))
        pid=service_pid(definition['Label'])
        if not pid:
            r=subprocess.run(['launchctl','bootstrap',f'gui/{os.getuid()}',str(path)],capture_output=True,text=True)
            if r.returncode:
                raise RuntimeError(f'launchctl registration failed for {name}: {r.stderr}')
            for _ in range(10):
                time.sleep(.5);pid=service_pid(definition['Label'])
                if pid:break
        if not pid:raise RuntimeError(f'{name} failed to start')
        os.kill(pid,0);pids[name]=pid
    record={'pids':pids,'services':{k:v['Label'] for k,v in definitions.items()},'keepawake_duration':'indefinite (no timeout; at least 96 hours while Mac remains powered)','restart':'launchd restarts crashed services during this login session','reboot_limitation':'No outside-study2 files permitted. These services are not installed in a system/user LaunchAgents directory, so after reboot/login run study2/src/start_autopilot.py to register them again.','first_idle_gate_check':'within 10 minutes of launch','started':time.time()}
    with (ROOT/'logs/services.json').open('w') as f:json.dump(record,f,indent=2)
    with (ROOT/'STATUS.md').open('a') as f:f.write('\n## Detached services\n\n'+json.dumps(record,indent=2)+'\n')
    runtime=sum(json.loads(p.read_text())['estimated_main_hours'] for p in (ROOT/'results').glob('stage2b_timing_*.json'))
    progress(f'READY FOR FREEZE. Estimated Stage 3 runtime: {runtime:.2f} hours. Watcher PID {pids["autopilot"]}, persistent keep-awake PID {pids["keepawake"]} verified running. Approval/deposit checked every 10 minutes; Stage 3 starts only after both verify. Reboot requires project-local service restart; crash restart is automatic.')
if __name__=='__main__':main()
