#!/bin/zsh
set -euo pipefail
cd "${0:A:h:h}"
mkdir -p study7/logs
export PYTHONDONTWRITEBYTECODE=1 PYTORCH_ENABLE_MPS_FALLBACK=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1
caffeinate -dimsu .venv/bin/python -B -u -m study7.src.runner --mode pilot 2>&1 | tee -a study7/logs/pilot.log
