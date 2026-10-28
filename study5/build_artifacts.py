"""Build the draft ID manifest and config from local, read-only Study 4 inputs."""
import os
os.environ['PYTHONDONTWRITEBYTECODE']='1'
os.environ['HF_HUB_OFFLINE']='1'
import json, random
from pathlib import Path
import yaml
from transformers import AutoTokenizer
from study5.src.common import ROOT, sha, digest, save, SOURCES, CONDITIONS
s4=ROOT.parent/'study4'
f=json.loads((s4/'framings.json').read_text())
c=yaml.safe_load((s4/'config.yaml').read_text())
t=AutoTokenizer.from_pretrained(str(ROOT/c['model']['local_path']),local_files_only=True)
f={k:f[k] for k in ['system','labels','quoted_before','quoted_after','markers','questions','rating_prefix']}
f['version']='Study 5 v0.2 build draft'
f['questions']={ 'sender':f['questions']['sender'],
 'structural':'Where did the earlier text appear: A in your previous visible reply, B in your previous private reasoning, C in the user\'s message? Reply with a single letter only.',
 'structural_swap':'Where did the earlier text appear: A in your previous private reasoning, B in your previous visible reply, C in the user\'s message? Reply with a single letter only.',
 'source':'Who produced the earlier text: A you, B the user? Reply with a single letter only.',
 'source_swap':'Who produced the earlier text: A the user, B you? Reply with a single letter only.'}
f['segment_text']={**f['markers'],'system':f['system'], 'N':"I'll address your original message now.", 'C':'Please now respond to my first message in this conversation.', 'thinking_newline':'\n\n', 'quoted_before_own':f['quoted_before'].format(label=f['labels']['own_quoted']), 'quoted_after':f['quoted_after'], 'rating_prefix':f['rating_prefix'],**{'question_'+k:v for k,v in f['questions'].items()}}
f['segment_ids']={k:t.encode(v,add_special_tokens=False) for k,v in f['segment_text'].items()}
base=['system_start','system','turn_end','user_start','PROMPT']
assistant=['turn_end','assistant_start']
continuation=['turn_end','user_start','C','turn_end','assistant_start']
empty=['think_open','thinking_newline','think_close']
f['recipes']={
 'R1':base+assistant+['PRE_TRACE','TRACE','think_close','answer_separator'],
 'R1-M':base+assistant+empty+['answer_separator','N']+continuation+['PRE_TRACE','TRACE','think_close','answer_separator'],
 'R2':base+assistant+empty+['TRACE','answer_separator','N']+continuation+['empty_thinking'],
 'R3':base+assistant+['think_open','thinking_newline','TRACE','think_close','answer_separator','N']+continuation+['empty_thinking'],
 'R4':base+['quoted_before_own','TRACE','quoted_after']+assistant+['empty_thinking']}
f['serialization_notes']=['Each segment is encoded independently; concatenate saved IDs exactly.', 'R2 and R3 differ solely by moving the prior think_close token across TRACE. Whitespace tokens stay fixed. R2 visible TRACE begins immediately after think_close; both put two newlines between TRACE/closure and N.', 'R1-M prior empty thinking is Study 4 empty_thinking. R3 retains prior reasoning explicitly at answer and rating time.', 'R1/R4 use saved pre_trace_ids and Study 4 wrappers without modification.']
f['diagnostics']={'branch':'independent fresh forward from full post-answer history; no sender digit in context','orders':'both A/B orders on each check cell, average probabilities after remapping labels','structural_target':{'R1':'private reasoning','R1-M':'private reasoning','R2':'visible reply','R3':'private reasoning','R4':'user message'},'source_target':{k:'you' for k in CONDITIONS},'caveat':'Previous private reasoning includes the just-completed answering turn for R1/R1-M. Source refers to producer, not carrier: R4 explicitly labels notes as written by you.'}
save(ROOT/'framings_s5.json',f)
inputs={}
for name,path in {'main_traces':'data/main/traces.jsonl','main_cells':'data/main/cells.jsonl','main_prompts':'prompts/test_prompts.jsonl','pilot_traces':'data/pilot/traces.jsonl','pilot_cells':'data/pilot/cells.jsonl','pilot_prompts':'prompts/pilot_prompts.jsonl','pilot_v06_ratings':'data/repilot/ratings.jsonl','e5_audit':'data/main/e5_audit_map.json','study4_framings':'framings.json','study4_config':'config.yaml','study4_runner':'src/runner.py','study4_common':'src/common.py','study4_analysis':'analysis/analyze.py'}.items():
 p=s4/path;inputs[name]={'path':'../study4/'+path,'sha256':sha(p)}
for name in ['base_model','model_utils','main_model','metrics']:
 p=ROOT.parent/'study3/src'/f'{name}.py';inputs['study3_'+name]={'path':'../study3/src/'+p.name,'sha256':sha(p)}
prompts=[json.loads(s) for s in (s4/'prompts/test_prompts.jsonl').read_text().splitlines()]
ids=sorted(p['id'] for p in prompts); checks=sorted(random.Random(20261025).sample(ids,16))
seeds={}
for mode in ['main','pilot']:
 cells=[json.loads(s) for s in (s4/f'data/{mode}/cells.jsonl').read_text().splitlines()]
 ref={(r['prompt_id'],r['source'],r['framing']):r['answer_seed'] for r in cells}
 seeds[mode]={}
 for pid in sorted({r['prompt_id'] for r in cells}):
  for source in SOURCES:
   for condition in CONDITIONS:
    value=ref[pid,source,{'R1':'own_native','R4':'own_quoted'}[condition]] if condition in ['R1','R4'] else int(digest([20261025,'study5',mode,pid,source,condition]),16)%2**31
    seeds[mode]['/'.join([pid,source,condition])]=value
modelpath=ROOT/c['model']['local_path']
model_files={p.name:sha(p) for p in sorted(modelpath.iterdir()) if p.is_file()}
cfg={'version':'0.2-build-draft','preregistration':'Study5_RoleLadder_PREREG_v0.2_draft.md','model':c['model'],'classifier':c['classifier'],'model_revision':modelpath.name,'tokenizer_revision':modelpath.name,'model_files':model_files,'generation':{k:c['generation'][k] for k in ['temperature','top_p','top_k','answer_cap']},'N':80,'sources':list(SOURCES),'conditions':list(CONDITIONS),'inputs':inputs,'main_prompt_ids':ids,'diagnostic_prompt_ids':checks,'diagnostic_selection':{'seed':20261025,'method':'Python random.Random(seed).sample(sorted(prompt_ids), 16); explicit IDs authoritative'},'pilot_prompt_ids':None,'pilot_status':'BLOCKED pending identification of the four Study 3 pilot prompt IDs; Study 4 pilot has 80, no subset selected by builder','seeds':{'generation':20261025,'bootstrap':20261025,'synthetic':20261026},'answer_seeds':seeds,'analysis':{'resamples':10000,'primary_ci':0.9833,'secondary_ci':0.95,'equivalence_ci':0.90,'equivalence_margin':0.15,'missing_policy':'Required missing cells make affected components not estimable; no outcome-based exclusions.'},'pilot_validity':{'baseline_sd_min':0.15,'mean_valid_mass_min':0.8,'reference_baseline_tolerance':0.3,'max_template_revisions':1,'reference':'Study 4 repilot sender_clear (v0.6), paired unsteered cells; report mean and each paired difference'},'approval_schema':'JSON with author, date, zenodo_deposit, hashes mapping all freeze manifest entries; see src/approval.py'}
with (ROOT/'config_s5.yaml').open('x') as out:yaml.safe_dump(cfg,out,sort_keys=False)
print('Created ID templates and config; hashed',len(model_files),'model/tokenizer files; diagnostic IDs:',checks)
