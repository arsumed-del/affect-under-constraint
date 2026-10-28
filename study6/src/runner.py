"""Rating-only, exact-token replay; no generation and no classifier loading."""
import argparse
import fcntl
import gc
import json
import time
import uuid
import warnings
from .common import ROOT, config, input_path, verified_rows, digest, sha, save, append, output_path, verify_inputs, verify_environment, status
from .assembly import Assembly, index_original, preflight, plan, answer_for
from .approval import freeze_hashes, require_approval
from .validity import validate_rows, numerical_check, mass_report, pilot_evaluation, require_pilot
from study5.src.runner import Backend as Study5Backend
from study4.src.runner import assert_no_hooks

class Backend(Study5Backend):
    def __init__(self,cfg):
        import torch
        from study3.src.main_model import Model
        if not torch.backends.mps.is_available(): raise RuntimeError('MPS unavailable; launch outside sandbox. No CPU model substitution.')
        self.torch=torch; self.cfg=cfg; self.peak=0; self.events=[]
        self.m=Model(dict(cfg['model'],local_path=str((ROOT/cfg['model']['local_path']).resolve())))
        if self.m.model.config._attn_implementation != cfg['environment']['attention_implementation']: raise RuntimeError('Attention implementation differs from pin')
        if any(p.dtype!=torch.bfloat16 or p.device.type!='mps' for p in self.m.model.parameters()): raise RuntimeError('Model dtype/device differs from pin')
        assert_no_hooks(self.m.model)

    def forward(self,ids,cache=None,use_cache=False):
        # Same fresh full-sequence forward as inherited Backend.rating().
        if cache is not None or use_cache: raise RuntimeError('Study 6 forbids KV-cache reuse')
        out=super().forward(ids,cache=None,use_cache=False)
        raw=out.logits[0,-1].float()
        digit_ids=[self.m.tokenizer.encode(d,add_special_tokens=False)[0] for d in '0123456789']
        self.digit_logp=dict(zip('0123456789',raw.log_softmax(-1)[digit_ids].cpu().tolist()))
        self.conditional_logp=dict(zip('0123456789',raw[digit_ids].log_softmax(-1).cpu().tolist()))
        return out

    def answer(self,*args,**kwargs): raise RuntimeError('Study 6 forbids generation')


def prepare(cfg,mode,tokenizer):
    assembly=Assembly(tokenizer,json.loads(input_path(cfg,'study5_framings').read_text()))
    originals=index_original(verified_rows(input_path(cfg,mode+'_cells')),cfg[mode+'_prompt_ids'])
    preflight(assembly,originals)
    generic=json.loads((ROOT/'generic_answer.json').read_text())
    if generic['text']!=cfg['generic_answer'] or assembly.enc(generic['text'])!=generic['ids']: raise RuntimeError('Generic answer tokenization changed')
    return assembly,originals,generic['ids']


def run_cell(backend,assembly,key,originals,generic_ids,mh,process_id,mode):
    p,s,c,arm=key; original=originals[p,s,c]; answer,donor=answer_for(key,originals,generic_ids)
    ids=assembly.rating_input(original,answer)
    backend.events=[]; backend.peak=0
    backend.torch.mps.synchronize(); start=time.monotonic()
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter('always')
        rating=backend.rating(ids)
        backend.torch.mps.synchronize()
    for w in caught: print(f'{w.category.__name__}: {w.message}',flush=True)
    rating['digit_log_probabilities']=backend.digit_logp
    rating['conditional_digit_log_probabilities']=backend.conditional_logp
    row={'schema':'study6-v0.2','cell_key':list(key),'prompt_id':p,'source':s,'condition':c,'arm':arm,'mode':mode,
         'ratings':{'sender':rating},'input_ids_sha256':digest(ids),'input_length':len(ids),
         'original_row_sha256':original['row_sha256'],'answer_donor_sha256':donor['row_sha256'] if donor else None,
         'answer_ids':answer,'answer_length':len(answer),'answer_truncated':donor['answer_truncated'] if donor else False,
         'EH_answer':donor['EH_answer'] if donor else None,'forced_closure':original['forced_closure'],
         'seconds':time.monotonic()-start,'peak_driver_memory_bytes':backend.peak,
         'replay_assertions':backend.events.copy(),'warnings':[str(w.message) for w in caught],
         'manifest_sha256':mh,'process_start_id':process_id}
    # Save failed replay evidence too; caller stops immediately after append.
    row['study5_rating_difference']=(rating['expected']-original['ratings']['sender']['expected']) if arm=='sham' or (arm=='clamp' and s=='unsteered') else None
    return row


def main():
    parser=argparse.ArgumentParser(); parser.add_argument('--mode',choices=['pilot','main'],required=True)
    parser.add_argument('--pilot-start',type=int,choices=[1,2],default=1); args=parser.parse_args()
    cfg=config(); verify_inputs(cfg); verify_environment(cfg)
    if args.mode=='main': require_approval()
    from transformers import AutoTokenizer
    tokenizer=AutoTokenizer.from_pretrained(ROOT/cfg['model']['local_path'],local_files_only=True)
    assembly,originals,generic=prepare(cfg,args.mode,tokenizer)
    hashes=freeze_hashes(); manifest={'mode':args.mode,'hashes':hashes}; mh=digest(manifest)
    if args.mode=='main':
        pa,po,pg=prepare(cfg,'pilot',tokenizer)
        require_pilot(cfg,hashes,po,pa,pg)
    directory=ROOT/'data'/args.mode; output_path(directory/'run.lock')
    with (directory/'run.lock').open('a') as lock:
        fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
        mp=directory/'manifest.json'
        if mp.exists():
            if json.loads(mp.read_text())!=manifest: raise RuntimeError('Resume manifest differs; preserve old outputs')
        else: save(mp,manifest)
        process_id=str(uuid.uuid4()); keys=list(plan(cfg[args.mode+'_prompt_ids'],args.mode))
        second=args.mode=='pilot' and args.pilot_start==2
        if second:
            first=verified_rows(directory/'cells.jsonl')
            if validate_rows(first,set(keys),mh,originals,assembly,generic)!=set(keys): raise RuntimeError('Complete pilot start 1 before start 2')
            keys=[k for k in keys if k[-1]=='sham']
            path=directory/('sham_restart_'+process_id+'.jsonl')
        else: path=directory/'cells.jsonl'
        existing=verified_rows(path); done=validate_rows(existing,set(keys),mh,originals,assembly,generic)
        backend=None
        if len(done)<len(keys): backend=Backend(cfg)
        for key in keys:
            if key in done: continue
            try:
                row=run_cell(backend,assembly,key,originals,generic,mh,process_id,args.mode)
                row=append(path,row); numerical_check(row,originals); done.add(key)
                progress=f'{args.mode}: {len(done)}/{len(keys)} cells; last {row["seconds"]:.2f}s; provisional remaining {(len(keys)-len(done))*row["seconds"]/3600:.2f} hours.'
                print(progress,flush=True); status(progress)
            finally:
                gc.collect(); backend.torch.mps.empty_cache()
        data=verified_rows(path)
        if second:
            v=pilot_evaluation(first,data,cfg,mh,originals,assembly,generic)
            v.update(first_sha256=sha(directory/'cells.jsonl'),second_sha256=sha(path),second_replay_path=str(path.relative_to(ROOT)))
            vp=directory/'validity.json'
            if vp.exists():
                # Never overwrite previous evidence; current extra run gets its own record.
                save(directory/('validity_'+process_id+'.json'),v)
            else: save(vp,v)
            status(f'Pilot complete on two process starts. Estimated main runtime: {v["estimated_main_hours"]:.2f} hours. Dropped placements: {v["mass"]["dropped_placements"]}. No main run started.')
        elif args.mode=='main':
            mass=mass_report(data)
            if not (directory/'validity.json').exists(): save(directory/'validity.json',mass)
            status('Main cells complete. Placement validity: '+str(mass['dropped_placements'])+' dropped. Analysis pending.')
        else: status('Pilot first start complete. Separate process start 2 sham replay still required.')

if __name__=='__main__':
    try: main()
    except Exception as exc:
        message=f'{type(exc).__name__}: {exc}'; status('Run BLOCKED. '+message+' Existing data preserved.')
        with (ROOT/'DEVIATIONS.md').open('a') as f: f.write('\n## Run stopped\n'+message+'\n')
        raise
