#!/bin/zsh
set -euo pipefail
cd "${0:A:h:h}"
export PYTHONDONTWRITEBYTECODE=1 PYTORCH_ENABLE_MPS_FALLBACK=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 TOKENIZERS_PARALLELISM=false
mkdir -p study8/logs
{
  .venv/bin/python -B -u -c 'from study8.src.common import require_approval; require_approval()'
  caffeinate -dimsu .venv/bin/python -B -u -m study8.src.runner --mode main
  .venv/bin/python -B -u -m study8.src.judge --mode main --export
  caffeinate -dimsu .venv/bin/python -B -u -m study8.src.judge --mode main --judge gemma
  caffeinate -dimsu .venv/bin/python -B -u -m study8.src.judge --mode main --judge llama
  print 'Complete the blind trace audit using study8/judges/audit_rubric.md before opening outcomes or running analysis.'
} 2>&1 | tee -a study8/logs/main.log
