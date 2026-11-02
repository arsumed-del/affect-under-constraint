#!/bin/zsh
set -euo pipefail
cd "${0:A:h:h}"
export PYTHONDONTWRITEBYTECODE=1 PYTORCH_ENABLE_MPS_FALLBACK=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 TOKENIZERS_PARALLELISM=false
mkdir -p study8/logs
{
  .venv/bin/python -B -u -m study8.src.audit --mode main
  caffeinate -dimsu .venv/bin/python -B -u -m study8.analysis.analyze --mode main
} 2>&1 | tee -a study8/logs/analyze.log
