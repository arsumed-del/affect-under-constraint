"""Stage 1 only; calibration prompts, append-only checkpoints."""
import os
os.environ['PYTORCH_ENABLE_MPS_FALLBACK'] = '1'
import gc
import json
import math
import traceback
from pathlib import Path
import torch
import yaml
from .model_utils import Model, cell_seed

def main():
    cfg = yaml.safe_load(Path('config.yaml').read_text())
    prompt = json.loads(Path('prompts/calibration_prompts.jsonl').read_text().splitlines()[0])
    spec = cfg['models'][0]
    print('Loading Qwen in bfloat16 on MPS', flush=True)
    model = Model(spec)
    messages = model.messages(prompt['text'])
    print(f'Loaded; decoder layer index {model.layer_index}', flush=True)
    norms = []
    def capture(module, args, output):
        h = output[0] if isinstance(output, tuple) else output
        norms.append(h.float().norm(dim=-1).mean().item())
    handle = model.layer.register_forward_hook(capture)
    with torch.inference_mode():
        model.model(input_ids=model.tensor(model.ids(messages)), use_cache=False)
    handle.remove()
    norm = sum(norms)/len(norms)
    rng = torch.Generator().manual_seed(777)
    vector = torch.randn(model.model.config.hidden_size, generator=rng)
    vector /= vector.norm()
    seed = cell_seed(spec['id'], prompt['id'], 'neutral', 'none', 0)
    question = Path(cfg['prompts']['downstream']).read_text().strip()
    results = {'layer_index':model.layer_index, 'smoke_prompt':prompt['id'], 'smoke_norm':norm}
    checkpoint = Path('results/stage1_cells.jsonl')
    done = {row['name']:row for row in (json.loads(line) for line in checkpoint.read_text().splitlines())} if checkpoint.exists() else {}
    for name, alpha, v in [('unhooked',0,None), ('zero_hook',0,vector), ('random_large',16,vector)]:
        if name in done:
            results[name] = done[name]
            print(f'Resuming: completed {name} skipped', flush=True)
            continue
        print(f'Running {name}', flush=True)
        generation = model.generate(messages, seed, alpha=alpha, norm=norm, vector=v)
        row = {'name':name,'alpha':alpha,'token_ids':generation.token_ids,'text':generation.text,'seconds':generation.seconds,'tokens_per_second':len(generation.token_ids)/generation.seconds,'peak_driver_memory':generation.peak_driver_memory}
        if name == 'unhooked':
            row['ratings'] = model.ratings(messages, generation, question)
        results[name] = row
        with Path('results/stage1_cells.jsonl').open('a') as f:
            f.write(json.dumps(row)+'\n')
        print(json.dumps(row), flush=True)
        del generation
        gc.collect()
        torch.mps.empty_cache()
    openers = json.loads(Path(cfg['prompts']['openers']).read_text())
    results['opener_logprobs'] = {k:[model.opener_logprob(messages,s) for s in seq] for k,seq in openers.items()}
    ratings = results['unhooked']['ratings']
    results['checks'] = {
        'zero_hook_identical':results['unhooked']['token_ids']==results['zero_hook']['token_ids'],
        'large_random_changes_text':results['unhooked']['text']!=results['random_large']['text'],
        'hook_removed':len(model.layer._forward_hooks)==0,
        'finite_openers':all(math.isfinite(x) for seq in results['opener_logprobs'].values() for x in seq),
        'ratings_agree':abs(ratings['hidden']-ratings['text_only'])<=0.05,
    }
    Path('results/stage1_smoke.json').write_text(json.dumps(results,indent=2)+'\n')
    Path('results/stage1_smoke.md').write_text('# Stage 1 smoke test\n\n'+json.dumps(results['checks'],indent=2)+'\n\nBaseline text:\n\n'+results['unhooked']['text']+'\n\nLarge random steering text:\n\n'+results['random_large']['text']+'\n\nFull timings, memory, ratings, and opener scores: stage1_smoke.json.\n')
    print('SMOKE_COMPLETE '+json.dumps(results['checks']), flush=True)

if __name__ == '__main__':
    try:
        main()
    except Exception:
        error = traceback.format_exc()
        Path('results/stage1_error.txt').write_text(error)
        print(error, flush=True)
        raise
