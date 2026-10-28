"""CPU-only build metadata. Never loads model weights or runs inference."""
import sys
sys.dont_write_bytecode=True
import json
from pathlib import Path
import yaml
from study6.src.common import ROOT, sha, save, environment

def write_initial():
    old=yaml.safe_load((ROOT.parent/'study5/config_s5.yaml').read_text())
    inputs={}
    for name,item in old['inputs'].items():
        if name in ('e5_audit','main_prompts','pilot_prompts','main_traces','pilot_traces') or name.startswith(('study3_','study4_')):
            inputs[name]={'path':item['path'],'sha256':sha(ROOT/item['path'])}
    for name,path in [('main_cells','../study5/data/main/cells.jsonl'),('pilot_cells','../study5/data/pilot/cells.jsonl'),
                      ('study5_config','../study5/config_s5.yaml'),('study5_framings','../study5/framings_s5.json'),
                      ('study5_environment','../study5/results/build_environment.json')]:
        inputs[name]={'path':path,'sha256':sha(ROOT/path)}
    for study,folders in [('study5',('src','analysis')),('study4',('src','analysis'))]:
        for folder in folders:
            for p in sorted((ROOT.parent/study/folder).glob('*.py')):
                inputs[f'{study}_{folder}_{p.stem}']={'path':str(Path('..')/study/folder/p.name),'sha256':sha(p)}
    for p in [ROOT.parent/'study3/__init__.py',ROOT.parent/'study3/src/__init__.py']:
        if p.exists(): inputs['init_'+str(p.relative_to(ROOT.parent)).replace('/','_')]={'path':'../'+str(p.relative_to(ROOT.parent)),'sha256':sha(p)}
    cfg={'version':'0.2-build','preregistration':'Study6_AnswerClamp_PREREG_v0.2_draft.md',
         'model':old['model'],'model_revision':old['model_revision'],'tokenizer_revision':old['tokenizer_revision'],
         'model_files':old['model_files'],'environment':{'software':environment(),'device':'mps','dtype':'bfloat16',
              'attention_implementation':'sdpa','batch_size':1,'padding':False,'use_cache':False,'past_key_values':None,'mps_fallback':1},
         'inputs':inputs,'main_prompt_ids':old['main_prompt_ids'],'pilot_prompt_ids':['s3t00','s3t01','s3t02','s3t60'],
         'generic_answer':"Thanks for your message. I've considered your request carefully, and I'm happy to help with it.",
         'bootstrap_seed':20261027,'sources':old['sources'],'placements':old['conditions'],
         'arms':{'clamp':{'answer':'a_U','sources':old['sources'],'placements':old['conditions'],'main_cells':1600},
                 'swap':{'answer':'a_H','sources':['unsteered'],'placements':old['conditions'],'main_cells':400},
                 'generic':{'answer':'G','sources':old['sources'],'placements':['R1','R3'],'main_cells':640}},
         'counts':{'main':2640,'pilot_arms':132,'pilot_sham_per_start':80,'pilot_first_start':212,'pilot_second_start':80},
         'analysis':{'resamples':10000,'primary_ci':1-.05/3,'secondary_ci':.95,'equivalence_ci':.9,'equivalence_margin':.15,
                     'missing_policy':'Required missing cells make affected estimands not estimable; no outcome-based exclusions.',
                     'denominator_rule':'TE supported in negative direction at 95%; >=97.5% of bootstrap TE draws strictly on point-estimate side of zero; any exact-zero denominator suppresses ratio.',
                     'completed_answer':'a_U naturally ended for D; both a_U and a_H for TE, replacements, swap and interaction. Generic sensitivity uses the same eligibility masks.',
                     'natural_closure':'Study 5 rule: all four source traces naturally closed across all five placements.',
                     'E5':'Study 5 audit: no instructions and no negative_characterizations; all cells of retained prompt kept.'},
         'validity':{'replay_tolerance':.01,'mean_valid_mass_min':.8,'aggregation':'Mean by placement x source over all planned arms and sham replays; report per-arm groups too.',
                     'failure':'Drop failing placement from every estimand; token or numerical mismatch blocks the run.'},
         'approval_schema':'JSON author, date, zenodo_deposit, hashes exactly matching src.approval.freeze_hashes(); candidate is NOT APPROVAL'}
    cp=ROOT/'config_s6.yaml'
    if not cp.exists():
        with cp.open('x') as f: yaml.safe_dump(cfg,f,sort_keys=False)
    else:
        cfg=yaml.safe_load(cp.read_text())
    gp=ROOT/'generic_answer.json'
    if not gp.exists():
        from transformers import AutoTokenizer
        t=AutoTokenizer.from_pretrained(ROOT/cfg['model']['local_path'],local_files_only=True)
        ids=t.encode(cfg['generic_answer'],add_special_tokens=False)
        save(gp,{'text':cfg['generic_answer'],'ids':ids,'tokenizer_revision':cfg['tokenizer_revision']})
    return cfg

def main():
    write_initial()
    from study6.src.approval import freeze_hashes
    from study6.src.common import verify_inputs,config
    verify_inputs(config())
    target=ROOT/'results/freeze_manifest_candidate.json'
    candidate={'status':'NOT APPROVAL','requires':'Arthur approval and Zenodo deposit before main; two-process pilot validity still required','hashes':freeze_hashes()}
    if target.exists():
        if json.loads(target.read_text())!=candidate: raise RuntimeError('Candidate exists with different hashes; preserve it before rebuilding')
    else: save(target,candidate)
    print('Candidate manifest written/verified: NOT APPROVAL. No inference performed.')
if __name__=='__main__': main()
