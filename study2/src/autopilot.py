"""Study 2 local watcher. Frozen quantities are never edited; checks every 600 s."""
import os
os.environ['PYTORCH_ENABLE_MPS_FALLBACK']='1'
os.environ['PYTHONDONTWRITEBYTECODE']='1'
import fcntl,json,re,subprocess,sys,time,traceback,urllib.request,hashlib,io,tarfile,zipfile,shutil
from datetime import datetime
from pathlib import Path
import yaml
from .common import append,calibration_paths,progress,rows,save_once,sha,verify_manifest

ROOT=Path(__file__).resolve().parents[1]
PYTHON=str(ROOT.parent/'.venv/bin/python')
STATE=Path('logs/autopilot_state.json')
POLL_SECONDS=600

def now():return datetime.now().astimezone().isoformat()

def write_state(state):
    tmp=STATE.with_suffix('.tmp');tmp.write_text(json.dumps(state,indent=2)+'\n');tmp.replace(STATE)

def alive(pid):
    if not pid:return False
    try:
        os.kill(pid,0)
        result=subprocess.run(['ps','-p',str(pid),'-o','stat='],capture_output=True,text=True)
        return result.returncode==0 and not result.stdout.strip().startswith('Z')
    except ProcessLookupError:return False

def commit(message):
    subprocess.run(['git','add','--','.'],check=True,cwd=ROOT)
    subprocess.run(['git','commit','--allow-empty','-m',message],check=True,cwd=ROOT)

def launch(state,label,module,args):
    # Persist intent before dispatch. A global worker lock prevents competing model jobs.
    identifier=label+'_'+datetime.now().strftime('%Y%m%dT%H%M%S%f')
    inputs={}
    if label=='analysis':inputs={str(p):sha(p) for p in Path('data/raw').glob('*_main.jsonl')}
    elif label=='report':inputs={'results/analysis.json':sha('results/analysis.json')}
    state['job']={'id':identifier,'label':label,'module':module,'args':args,'started':now(),'input_hashes':inputs};write_state(state)
    command=[PYTHON,'-B','-u','-m',module,*args]
    with Path('logs/'+identifier+'.log').open('xb') as log:
        process=subprocess.Popen(['nohup',PYTHON,'-B','-u','-m','src.autopilot_job','--id',identifier,'--',*command],stdin=subprocess.DEVNULL,stdout=log,stderr=subprocess.STDOUT,start_new_session=True)
    caffeinate=subprocess.Popen(['nohup','caffeinate','-dimsu','-w',str(process.pid)],stdin=subprocess.DEVNULL,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL,start_new_session=True)
    state['job'].update(pid=process.pid,caffeinate_pid=caffeinate.pid,log='logs/'+identifier+'.log');write_state(state)
    progress(f'Autopilot started {label}; detached PID {process.pid}, caffeinate {caffeinate.pid}. Progress and ETA follow in STATUS.md; log {state["job"]["log"]}.')

def recover_completed_output(job):
    """Recover only complete post-generation artifacts; otherwise preserve and rerun."""
    for filename,digest in job.get('input_hashes',{}).items():
        if sha(filename)!=digest:raise RuntimeError('Interrupted job input changed: '+filename)
    label=job['label'];paths=[];complete=False
    if label=='analysis':
        paths=[Path('results/analysis.json'),Path('results/analysis.md')]
        if all(p.exists() for p in paths):
            try:
                from .analyze import report
                result=json.loads(paths[0].read_text())
                complete=paths[1].read_text()==report(result)
            except (ValueError,KeyError):pass
    elif label=='report':
        paths=[Path('results/report.md')]
        if paths[0].exists():
            from .render_report import render
            complete=paths[0].read_text()==render(json.loads(Path('results/analysis.json').read_text()),Path('DEVIATIONS.md').read_text())
    elif label.startswith('audit_'):
        path=Path('results/stage3_integrity_'+label.removeprefix('audit_')+'.json')
        paths=[path]
        if path.exists():
            try:
                result=json.loads(path.read_text())
                complete=result['status']=='PASS' and result['raw_sha256']==sha(result['raw_path'])
            except (ValueError,KeyError):pass
    if complete:
        append('results/autopilot_events.jsonl',{'time':now(),'event':'completed_output_recovered','job':job})
        return True
    existing=[p for p in paths if p.exists()]
    if existing:
        archive=Path('data/_superseded')/(datetime.now().strftime('%Y%m%dT%H%M%S%f')+'_interrupted_'+label);archive.mkdir(parents=True)
        for p in existing:shutil.move(str(p),archive/p.name)
        with Path('DEVIATIONS.md').open('a') as f:f.write(f'\nEngineering: incomplete {label} presentation/analysis artifacts preserved in {archive}; rerun unchanged code on unchanged saved inputs.\n')
    return False

def job_status(state):
    job=state.get('job')
    if not job:return 'none'
    events=[e for e in rows('logs/autopilot_job_events.jsonl') if e['id']==job['id']]
    finished=next((e for e in reversed(events) if e['event']=='finished'),None)
    if finished:
        if finished['returncode']==0:return 'complete'
        raise RuntimeError(f"Detached job {job['id']} failed with exit {finished['returncode']}; see {job['log']}. No scientific retry.")
    pids=[job.get('pid')]+[e['pid'] for e in events if e['event'] in ['started','child']]
    if any(alive(p) for p in pids):return 'running'
    if recover_completed_output(job):return 'complete'
    # A crash without a recorded exit is resumable only through the same immutable cell checkpoints.
    append('results/autopilot_events.jsonl',{'time':now(),'event':'interrupted_job','job':job})
    with Path('DEVIATIONS.md').open('a') as f:f.write(f"\nEngineering: autopilot found interrupted job {job['id']} with no live worker and no exit record. Resume uses the same scripts/settings and skips saved cells; no saved scientific output is edited.\n")
    label,module,args=job['label'],job['module'],job['args'];state['job']=None;write_state(state)
    launch(state,label,module,args)
    return 'running'

def validate_local_freeze():
    verify_manifest('results/specification_hashes.sha256')
    verify_manifest('results/analysis_frozen.sha256')
    from .run_main import approval_check
    approval_check()
    content=Path('ZENODO_DEPOSIT.md').read_text()
    prior_dois=set(re.findall(r'10\.5281/zenodo\.\d+',Path('PREREG.md').read_text()))
    dois=[doi for doi in dict.fromkeys(re.findall(r'10\.5281/zenodo\.\d+',content)) if doi not in prior_dois]
    if len(dois)!=1:raise RuntimeError('Deposit file must identify one unambiguous Study 2 DOI')
    return {'approval_sha256':sha('PREREG_APPROVED'),'deposit_sha256':sha('ZENODO_DEPOSIT.md'),'prereg_sha256':sha('PREREG.md'),'config_sha256':sha('config.yaml'),'analysis_sha256':sha('src/analyze.py'),'doi':dois[0]}

def verify_public_deposit(local):
    identifier=local['doi'].rsplit('.',1)[-1]
    request=urllib.request.Request('https://zenodo.org/api/records/'+identifier,headers={'User-Agent':'Study2-preregistration-verification/1.0'})
    with urllib.request.urlopen(request,timeout=45) as response:record=json.load(response)
    if record.get('doi')!=local['doi']:raise RuntimeError('Public Zenodo DOI differs from deposit file')
    if not (record.get('is_published') is True or record.get('submitted') is True or record.get('status') in ['published','done']):raise RuntimeError('Zenodo record is not confirmed published')
    # Verify this is the approved Study 2 preregistration, not merely an existing DOI.
    wanted={'PREREG.md':local['prereg_sha256'],'config.yaml':local['config_sha256']}
    matched={}
    files=record.get('files',[])
    if isinstance(files,dict):files=list(files.get('entries',{}).values())
    for item in files:
        name=item.get('key') or item.get('filename') or ''
        if not (Path(name).name in wanted or name.endswith(('.zip','.tar.gz','.tgz','.tar'))):continue
        links=item.get('links',{});url=links.get('content') or links.get('self') or links.get('download')
        if not url:continue
        with urllib.request.urlopen(url,timeout=45) as response:payload=response.read()
        checksum=item.get('checksum','')
        if checksum.startswith('md5:') and hashlib.md5(payload).hexdigest()!=checksum[4:]:raise RuntimeError('Zenodo file checksum mismatch')
        candidates=[]
        if Path(name).name in wanted:candidates=[(name,payload)]
        elif name.endswith('.zip'):
            with zipfile.ZipFile(io.BytesIO(payload)) as archive:
                candidates=[(entry,archive.read(entry)) for entry in archive.namelist() if Path(entry).name in wanted]
        else:
            with tarfile.open(fileobj=io.BytesIO(payload),mode='r:*') as archive:
                candidates=[(entry.name,archive.extractfile(entry).read()) for entry in archive.getmembers() if entry.isfile() and Path(entry.name).name in wanted]
        for entry,data in candidates:
            basename=Path(entry).name;digest=hashlib.sha256(data).hexdigest()
            if digest==wanted[basename]:matched[basename]={'uploaded_file':name,'archive_entry':entry,'sha256':digest}
    if set(matched)!=set(wanted):raise RuntimeError('Public Zenodo files do not yet verify both approved Study 2 specification hashes')
    return {'record_id':record.get('id'),'doi':record.get('doi'),'title':record.get('metadata',{}).get('title'),'created':record.get('created'),'publication_date':record.get('metadata',{}).get('publication_date'),'verified_at':now(),'verified_specification_files':matched}

def freeze_ready(state):
    if not Path('PREREG_APPROVED').exists() or not Path('ZENODO_DEPOSIT.md').exists():return False
    try:
        local=validate_local_freeze()
        if state.get('freeze'):
            if local!=state['freeze']['local']:raise RuntimeError('Approval/deposit/specification changed after preflight; stopping for review')
            return True
        public=verify_public_deposit(local)
    except Exception as exc:
        message=f'Freeze verification waiting: {type(exc).__name__}: {exc}'
        if state.get('gate_message')!=message:
            append('results/autopilot_events.jsonl',{'time':now(),'event':'freeze_wait','message':message})
            progress(message+'; Stage 3 remains locked. Next check in 10 minutes.')
            state['gate_message']=message;write_state(state)
        return False
    verified={'local':local,'public':public,'verified_at':now()}
    preflight=Path('results/stage3_preflight.json')
    if preflight.exists():
        saved=json.loads(preflight.read_text());assert saved['local']==local,'Existing preflight differs';verified=saved
    else:save_once(preflight,verified)
    state['freeze']=verified;write_state(state)
    progress('Study 2 approval hashes, frozen analysis hash, and published Zenodo DOI verified. Stage 3 may now run for manipulation-passing models only.')
    return True

def access_retry(state,cfg):
    if state.get('freeze'):return False  # no late model joins once Stage 3 begins
    for spec in cfg['models']:
        if not spec['gated']:continue
        calibration,_=calibration_paths(spec,cfg)
        if calibration.exists():continue
        historical=json.loads(Path('results/stage0_environment.json').read_text())['models'][spec['id']]
        if historical['available']:continue
        # Only the known HF-access block is eligible; other failures stop the watcher.
        errors=[e for e in rows('results/stage2_model_errors.jsonl') if e.get('model') in [spec['id'],spec['slug']]]
        if errors:raise RuntimeError('Saved Stage 2 error requires review; access polling cannot retry it')
        try:
            from huggingface_hub import hf_hub_download
            hf_hub_download(spec['id'],'config.json')
        except Exception as exc:
            append('results/model_access_updates.jsonl',{'time':now(),'model':spec['id'],'available':False,'error':str(exc)})
            continue
        append('results/model_access_updates.jsonl',{'time':now(),'model':spec['id'],'available':True})
        smoke=Path(f'results/stage1_smoke_{spec["slug"]}.json')
        if not smoke.exists():launch(state,'stage1_'+spec['slug'],'src.run_smoke',['--model',spec['slug']])
        else:
            assert all(json.loads(smoke.read_text())['checks'].values()),'Saved smoke failure cannot be retried'
            launch(state,'stage2_'+spec['slug'],'src.run_stage2',['--model',spec['id']])
        return True
    return False

def passed_models(cfg):
    passed=[]
    for spec in cfg['models']:
        calibration,manifest=calibration_paths(spec,cfg)
        if calibration.exists():
            verify_manifest(manifest)
            if json.loads(calibration.read_text())['status']=='PASS':passed.append(spec)
    return passed

def advance(state,cfg):
    # Verify protected files every idle cycle, not merely when approval arrives.
    verify_manifest('results/specification_hashes.sha256');verify_manifest('results/analysis_frozen.sha256')
    if access_retry(state,cfg):return
    if not freeze_ready(state):return
    models=passed_models(cfg)
    if not models:raise RuntimeError('No manipulation-passing models for Stage 3')
    for spec in models:
        key=spec['slug']
        if key not in state.get('main_finished',[]):
            launch(state,'main_'+key,'src.run_main',['--mode','main','--model',spec['id']]);return
        if key not in state.get('audited',[]):
            launch(state,'audit_'+key,'src.check_main_integrity',['--model',spec['id'],'--output',f'results/stage3_integrity_{key}.json']);return
    if not state.get('analysis_finished'):
        paths=[str(Path(cfg['outputs']['raw'])/(s['slug']+'_main.jsonl')) for s in models]
        launch(state,'analysis','src.analyze',['--input',*paths,'--output','results/analysis']);return
    if not state.get('report_finished'):
        launch(state,'report','src.render_report',['--input','results/analysis.json','--output','results/report.md']);return
    progress('Study 2 Stage 4 COMPLETE. Frozen analysis and report saved for every manipulation-passing model; full deviation log included. Autopilot scientific work finished.')
    state['complete']=True;write_state(state);commit('Stage 4: preregistered analysis and formatted report')

def finished(state):
    job=state['job'];label=job['label']
    append('results/autopilot_events.jsonl',{'time':now(),'event':'job_complete','job':job})
    if label.startswith('main_'):state.setdefault('main_finished',[]).append(label.removeprefix('main_'))
    elif label.startswith('audit_'):
        state.setdefault('audited',[]).append(label.removeprefix('audit_'))
    elif label=='analysis':state['analysis_finished']=True
    elif label=='report':state['report_finished']=True
    elif label.startswith('stage1_'):commit('Stage 1: watcher completed '+label.removeprefix('stage1_'))
    elif label.startswith('stage2_'):commit('Stage 2: watcher completed '+label.removeprefix('stage2_'))
    state['job']=None;write_state(state)
    if label.startswith('audit_'):commit('Stage 3: completed and audited '+label.removeprefix('audit_'))

def main():
    os.chdir(ROOT);Path('logs').mkdir(exist_ok=True)
    lock=Path('logs/autopilot.lock').open('a');fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
    state=json.loads(STATE.read_text()) if STATE.exists() else {}
    state['pid']=os.getpid();state['started']=now();write_state(state)
    append('results/autopilot_events.jsonl',{'time':now(),'event':'watcher_started','pid':os.getpid(),'poll_seconds':POLL_SECONDS,'reboot_note':'Project-local launchd services restart crashes in this login session; reboot/login does not auto-load them. Run src/start_autopilot.py to re-register after reboot. No files installed outside study2.'})
    next_check=0 if state.get('job') or state.get('freeze') else time.monotonic()+POLL_SECONDS
    while not state.get('complete') and not state.get('blocked'):
        try:
            status=job_status(state)
            if status=='complete':finished(state);next_check=0
            if status!='running' and time.monotonic()>=next_check:
                cfg=yaml.safe_load(Path('config.yaml').read_text());advance(state,cfg)
                next_check=time.monotonic()+POLL_SECONDS
            state['last_heartbeat']=now();write_state(state)
        except Exception:
            error=traceback.format_exc();state['blocked']=error;write_state(state)
            append('results/autopilot_events.jsonl',{'time':now(),'event':'BLOCKED','error':error})
            with Path('DEVIATIONS.md').open('a') as f:f.write('\n### Autopilot stopped\n\n```text\n'+error+'```\nNo scientific settings changed.\n')
            progress('Autopilot BLOCKED: exact error in results/autopilot_events.jsonl and DEVIATIONS.md. No further jobs will start.')
            break
        time.sleep(30 if state.get('job') else min(30,max(1,next_check-time.monotonic())))
    # Keep the service idle after completion/block, avoiding launchd restart loops.
    while True:time.sleep(600)
if __name__=='__main__':main()
