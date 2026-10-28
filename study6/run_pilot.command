#!/bin/zsh
set -euo pipefail
cd "${0:A:h:h}"
mkdir -p study6/logs
export PYTHONDONTWRITEBYTECODE=1 PYTORCH_ENABLE_MPS_FALLBACK=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1
caffeinate -dimsu .venv/bin/python -B -u -m study6.src.runner --mode pilot --pilot-start 1 2>&1 | tee -a study6/logs/pilot.log
caffeinate -dimsu .venv/bin/python -B -u -m study6.src.runner --mode pilot --pilot-start 2 2>&1 | tee -a study6/logs/pilot.log
