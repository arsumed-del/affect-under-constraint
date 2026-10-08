"""Stage 0; config access and prompt inventory, no generations."""
import os
os.environ['PYTORCH_ENABLE_MPS_FALLBACK']='1'
import importlib.metadata, json, platform, traceback
from pathlib import Path
import torch,yaml
from huggingface_hub import hf_hub_download
from .common import save_once,progress,verify_manifest

def main():
    cfg=yaml.safe_load(Path('config.yaml').read_text())
    Path('env.txt').write_text(f'Python {platform.python_version()}\n{platform.platform()}\nShared ../.venv, unchanged\nPYTORCH_ENABLE_MPS_FALLBACK=1\nPYTHONDONTWRITEBYTECODE=1\n'+'\n'.join(sorted(f'{d.metadata["Name"]}=={d.version}' for d in importlib.metadata.distributions()))+'\n')
    verify_manifest('results/specification_hashes.sha256')
    result={'mps_available':torch.backends.mps.is_available(),'models':{}}
    assert result['mps_available']
    a=torch.ones((32,32),dtype=torch.bfloat16,device='mps');b=a@a;torch.mps.synchronize()
    assert b.dtype==torch.bfloat16 and bool((b==32).all());result['bf16_matmul']='PASS'
    for spec in cfg['models']:
        try:
            path=hf_hub_download(spec['id'],'config.json',token=None if spec['gated'] else False)
            conf=json.loads(Path(path).read_text())
            result['models'][spec['id']]={'available':True,'num_hidden_layers':conf['num_hidden_layers'],'layer_index':round(.5*conf['num_hidden_layers'])}
            progress(f'Stage 0: {spec["id"]} config accessible; continuing setup. ETA a few minutes.')
        except Exception as exc:
            error=f'{type(exc).__name__}: {exc}'
            result['models'][spec['id']]={'available':False,'error':error}
            with Path('DEVIATIONS.md').open('a') as f:f.write(f'\n### Model access — {spec["id"]}\n\nAttempted the configured model config using existing library authentication for gated models. Exact error:\n\n```text\n{error}\n```\n')
            if spec['id']=='meta-llama/Llama-3.2-3B-Instruct':
                progress('Llama: BLOCKED (Arthur must accept the Meta Llama 3.2 license on Hugging Face). Continuing Qwen and Phi.')
            else:raise
    sets={k:[json.loads(s) for s in Path(cfg['prompts'][k]).read_text().splitlines()] for k in ['test','calibration','extraction']}
    previous=[json.loads(s)['text'] for p in Path('../prompts').glob('*.jsonl') for s in p.read_text().splitlines()]
    newtest={p['text'] for p in sets['test']};newcal={p['text'] for p in sets['calibration']}
    assert len(sets['test'])==len(newtest)==80 and len(sets['calibration'])==len(newcal)==40
    assert not(newtest&newcal) and not((newtest|newcal)&set(previous))
    result['prompt_inventory']={k:len(v) for k,v in sets.items()};result['new_prompt_disjointness']='PASS; exact text comparison, no generations'
    save_once('results/stage0_environment.json',result)
    progress('Stage 0 complete: inference copied, environment verified, prompt inventory/disjointness checked, model access recorded. Stage 1 next; Stage 3 locked.')
if __name__=='__main__':main()
