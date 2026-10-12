import json,traceback
from pathlib import Path
from .common import *

def config():return json.loads(Path('checks_config.json').read_text())
def record_generation(g):
    return {k:getattr(g,k) for k in ['prompt_ids','token_ids','text','seconds','peak_driver_memory','thinking','answer','thinking_ids','answer_ids','forced_ids','thinking_truncated','answer_truncated','thinking_enabled','sampled_tokens']}
def guarded(main):
    try:main()
    except Exception:
        error=traceback.format_exc();append('results/errors.jsonl',{'error':error})
        with Path('DEVIATIONS.md').open('a') as f:f.write('\n## Check stopped\n\n```text\n'+error+'```\n')
        progress('BLOCKED: '+error.splitlines()[-1]+'; full error in results/errors.jsonl and DEVIATIONS.md. No design change or automatic scientific retry.')
        raise
