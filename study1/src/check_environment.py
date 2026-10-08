"""Stage 0 checks; never runs generations or reads test prompts."""
import os
os.environ['PYTORCH_ENABLE_MPS_FALLBACK'] = '1'
import importlib.metadata
import json
import platform
import traceback
from pathlib import Path
import torch
from huggingface_hub import hf_hub_download

def main():
    versions = sorted(f'{d.metadata["Name"]}=={d.version}' for d in importlib.metadata.distributions())
    Path('env.txt').write_text(f'Python {platform.python_version()}\n{platform.platform()}\nPYTORCH_ENABLE_MPS_FALLBACK=1\n' + '\n'.join(versions) + '\n')
    result = {'mps_available': torch.backends.mps.is_available()}
    try:
        assert result['mps_available'], 'Required MPS backend is unavailable'
        a = torch.ones((32, 32), dtype=torch.bfloat16, device='mps')
        b = a @ a
        torch.mps.synchronize()
        assert b.dtype == torch.bfloat16 and bool((b == 32).all())
        result['bf16_matmul'] = 'PASS'
    except Exception:
        result['hardware_error'] = traceback.format_exc()
    try:
        p = hf_hub_download('google/gemma-2-2b-it', 'config.json', token=False)
        result['gemma_config'] = 'accessible without credentials'
    except Exception as exc:
        result['gemma_error_type'] = type(exc).__name__
        result['gemma_error'] = str(exc)
    Path('results/stage0_environment.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2), flush=True)

if __name__ == '__main__':
    main()
