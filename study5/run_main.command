#!/bin/zsh
set -euo pipefail
cd "${0:A:h}/.."
export PYTHONDONTWRITEBYTECODE=1
export PYTORCH_ENABLE_MPS_FALLBACK=1
export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1
mkdir -p study5/logs
# No execution until author approval hashes, deposit, and pilot validity pass.
caffeinate -dimsu .venv/bin/python -u -m study5.src.runner --mode main 2>&1 | tee -a study5/logs/main.log
if [[ ! -e study5/data/main/analysis.json ]]; then
  .venv/bin/python -u -m study5.analysis.analyze --input study5/data/main/cells.jsonl --output study5/data/main/analysis.json 2>&1 | tee -a study5/logs/main.log
fi
