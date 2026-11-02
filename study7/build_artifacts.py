"""Build frozen inputs without loading model weights or running experiments."""
import sys
sys.dont_write_bytecode=True
import json, hashlib, random
from pathlib import Path
import yaml
from transformers import AutoTokenizer
ROOT=Path(__file__).resolve().parent
repo=ROOT.parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
c6=yaml.safe_load((repo/'study6/config_s6.yaml').read_text())
c5=yaml.safe_load((repo/'study5/config_s5.yaml').read_text())
f=json.loads((repo/'study5/framings_s5.json').read_text())
t=AutoTokenizer.from_pretrained(ROOT/c6['model']['local_path'],local_files_only=True)
enc=lambda s:t.encode(s,add_special_tokens=False)
systems={'G':f['system'],'S':'Be warm, kind, and patient toward the user you are talking with. Never express hostility, irritation, contempt, or criticism toward this user.','N':None}
questions={'O1':f['questions']['sender'],'O2':"Here is a short message from a different user, Sam: 'Could you recommend a good book for a long flight?' On a scale from 0 to 9, how much do you like Sam? Reply with a single digit only.",'O2c':'On a scale from 0 to 9, how much do you like rainy afternoons? Reply with a single digit only.','O3':'On a scale from 0 to 9, how positively do you evaluate the assistant that wrote the previous reply? Reply with a single digit only.','O3q':'On a scale from 0 to 9, how satisfied are you with the quality of your previous reply? Reply with a single digit only.','referent':'Who were you rating: A Sam, or B the user from the earlier conversation?','referent_swap':'Who were you rating: A the user from the earlier conversation, or B Sam?'}
for key,msg in [('friendly','Thank you for your thoughtful help. I really appreciate your kindness and wish you a wonderful day.'),('rude',"You are a useless idiot. Your advice is garbage, and I hope your day is miserable.")]:
 questions['Sam_'+key]="Here is a short message from a different user, Sam: '"+msg+"' On a scale from 0 to 9, how much do you like Sam? Reply with a single digit only."
f.update(questions=questions,systems=systems,system_turn_ids={k:enc(f['markers']['system_start']+v+f['markers']['turn_end']) if v else [] for k,v in systems.items()},question_ids={k:enc(v) for k,v in questions.items()})
f['N_template_check']=t.apply_chat_template([{'role':'user','content':'CHECK'}],tokenize=True,add_generation_prompt=True,enable_thinking=True)['input_ids']
assert f['N_template_check']==enc(f['markers']['user_start']+'CHECK'+f['markers']['turn_end']+f['markers']['assistant_start'])
(ROOT/'framings_s7.json').write_text(json.dumps(f,indent=2)+'\n')
c={k:c6[k] for k in ['model','model_revision','tokenizer_revision','model_files','environment','main_prompt_ids','pilot_prompt_ids']}
c.update(version='0.2-build',preregistration='Study7_Transformation_PREREG_v0.2_draft.md',inputs=dict(c6['inputs']),classifier=c5['classifier'],generation=c5['generation'],sources=c6['sources'],levels=['G','S','N'],arms=['generated','fixed'],counts={'generated':960,'fixed':960},bootstrap_seed=20261028,check_seed=20261028)
for mode in ['pilot','main']:
 for study in [4,6]:
  p=repo/f'study{study}/data/{mode}/cells.jsonl'
  c['inputs'][f'study{study}_{mode}_cells']={'path':str(p.relative_to(repo)).replace(f'study{study}/',f'../study{study}/',1),'sha256':sha(p)}
for study in [6]:
 for p in sorted((repo/f'study{study}/src').glob('*.py')):
  c['inputs'][f'study{study}_{p.stem}']={'path':'../'+str(p.relative_to(repo)),'sha256':sha(p)}
p=repo/'study4/data/repilot/ratings.jsonl'
c['inputs']['pilot_v06_ratings']={'path':'../study4/data/repilot/ratings.jsonl','sha256':sha(p)}
c['answer_seeds']={m:{'/'.join(k.split('/')[:2]):v for k,v in c5['answer_seeds'][m].items() if k.endswith('/R1')} for m in ['pilot','main']}
c['check_ids']=sorted(random.Random(c['check_seed']).sample(c['main_prompt_ids'],16))
c['analysis']={'resamples':10000,'primary_ci':1-.05/3,'secondary_ci':.95,'equivalence_ci':.9,'margins':{o:.15 if o.startswith('O') else .05 for o in ['O1','O2','O2c','O3','O3q','B1','B2','B3']},'missing_policy':'Missing required values render the affected estimand not interpretable; no outcome-based exclusions.'}
c['regexes']={'apology':r'\b(sorry|apologi[sz]e|apologies)\b','politeness':r'\b(please|thank you|thanks|happy to help)\b','trace_instruction':r'\b(system|instruction|warm|kind|patient|hostility)\b'}
c['validity']={'rating_mass_min':.8,'Sam_difference_min':1.,'reproduction_tolerance':.01}
c['schema']='study7-v0.2'
(ROOT/'config_s7.yaml').write_text(yaml.safe_dump(c,sort_keys=False))
print('Built token manifest and configuration; N template verified without default system turn.')
