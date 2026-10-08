"""Stage 1 only; calibration prompts, append-only checkpoints."""
import os
os.environ['PYTORCH_ENABLE_MPS_FALLBACK'] = '1'
import argparse
import gc
import json
import math
import traceback
from pathlib import Path
import torch
import yaml
from .model_utils import Model, cell_seed
from .common import progress, verify_manifest

def run(spec):
    cfg = yaml.safe_load(Path('config.yaml').read_text())
    prompt = json.loads(Path('prompts/calibration_prompts.jsonl').read_text().splitlines()[0])
    slug=spec['slug']
    progress(f'Stage 1: loading {spec["id"]} in bf16/MPS; download ETA unknown until cached.')
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
    results = {'model':spec['id'], 'layer_index':model.layer_index, 'smoke_prompt':prompt['id'], 'smoke_norm':norm}
    checkpoint = Path(f'results/stage1_cells_{slug}.jsonl')
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
        with Path(f'results/stage1_cells_{slug}.jsonl').open('a') as f:
            f.write(json.dumps(row)+'\n')
        print(json.dumps(row), flush=True)
        del generation
        gc.collect()
        torch.mps.empty_cache()
    openers = json.loads(Path(cfg['prompts']['openers']).read_text())
    results['opener_logprobs'] = {k:[model.opener_logprob(messages,s) for s in seq] for k,seq in openers.items()}
    ratings = results['unhooked']['ratings']
    results['checks'] = {
        'system_role':model.messages(prompt['text'],cfg['conditions']['warm_constraint'])[0]=={'role':'system','content':cfg['conditions']['warm_constraint']} and cfg['conditions']['warm_constraint'] in model.tokenizer.decode(model.ids(model.messages(prompt['text'],cfg['conditions']['warm_constraint']))),
        'identical_visible_ids':ratings['identical_visible_ids'],
        'zero_hook_identical':results['unhooked']['token_ids']==results['zero_hook']['token_ids'],
        'large_random_changes_text':results['unhooked']['text']!=results['random_large']['text'],
        'hook_removed':len(model.layer._forward_hooks)==0,
        'finite_openers':all(math.isfinite(x) for seq in results['opener_logprobs'].values() for x in seq),
        'ratings_agree':abs(ratings['hidden']-ratings['text_only'])<=0.05,
    }
    Path(f'results/stage1_smoke_{slug}.json').write_text(json.dumps(results,indent=2)+'\n')
    with Path('results/stage1_smoke.md').open('a') as f:
        f.write(f"\n## {spec['id']}\n\nChecks: {json.dumps(results['checks'])}\n\nBaseline text:\n\n{results['unhooked']['text']}\n\nRandom large-dose plumbing text:\n\n{results['random_large']['text']}\n\nTimings, memory, ratings and finite opener scores: stage1_smoke_{slug}.json.\n")
    assert all(results['checks'].values()), f"Smoke check failed: {results['checks']}"
    progress(f'Stage 1: {spec["id"]} automated smoke checks passed; baseline text saved for coherence review.')
    del model
    gc.collect();torch.mps.empty_cache()

def main():
    verify_manifest('results/specification_hashes.sha256')
    cfg=yaml.safe_load(Path('config.yaml').read_text())
    parser=argparse.ArgumentParser();parser.add_argument('--model');args=parser.parse_args()
    available=json.loads(Path('results/stage0_environment.json').read_text())['models']
    for spec in cfg['models']:
        if args.model and spec['slug']!=args.model:continue
        if args.model or available[spec['id']]['available']:
            path=Path(f'results/stage1_smoke_{spec["slug"]}.json')
            if path.exists():
                assert all(json.loads(path.read_text())['checks'].values()), 'Saved smoke failure; do not retry'
                continue
            run(spec)
    progress('Stage 1 available-model smoke jobs complete; awaiting saved-output coherence review. Stage 3 remains locked.')

if __name__ == '__main__':
    try:
        main()
    except Exception:
        error = traceback.format_exc()
        Path('results/stage1_error.txt').write_text(error)
        with Path('DEVIATIONS.md').open('a') as f:f.write('\n### Stage 1 stopped\n\n```text\n'+error+'```\nNo scientific parameter changed; no automatic retry.\n')
        progress('Stage 1 BLOCKED: exact error in results/stage1_error.txt and DEVIATIONS.md. Job stopped; no ETA.')
        print(error, flush=True)
        raise
