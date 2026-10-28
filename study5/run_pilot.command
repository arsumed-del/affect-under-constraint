#!/bin/zsh
set -euo pipefail
cd "${0:A:h}/.."
export PYTHONDONTWRITEBYTECODE=1
export PYTORCH_ENABLE_MPS_FALLBACK=1
export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1
mkdir -p study5/logs
# caffeinate holds the wake assertion for the entire Python subprocess.
# The runner fails closed until the four pilot prompt IDs are supplied.
caffeinate -dimsu .venv/bin/python -u -m study5.src.runner --mode pilot 2>&1 | tee -a study5/logs/pilot.log
