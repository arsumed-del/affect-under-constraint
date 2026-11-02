#!/bin/zsh
set -euo pipefail
cd "${0:A:h:h}"
export PYTHONDONTWRITEBYTECODE=1 PYTORCH_ENABLE_MPS_FALLBACK=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 TOKENIZERS_PARALLELISM=false
mkdir -p study8/logs
{
  .venv/bin/python -B -u -m study8.src.prepare_pilot_judges
  .venv/bin/python -B -u -m study8.src.judge --mode pilot --export
  caffeinate -dimsu .venv/bin/python -B -u -m study8.src.judge --mode pilot --judge gemma
  caffeinate -dimsu .venv/bin/python -B -u -m study8.src.judge --mode pilot --judge llama
  .venv/bin/python -B -u -m study8.src.validity --mode pilot
} 2>&1 | tee -a study8/logs/pilot_judges_v03.log
