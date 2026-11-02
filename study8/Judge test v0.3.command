#!/bin/zsh
cd "${0:A:h:h}"
export PYTHONDONTWRITEBYTECODE=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 TOKENIZERS_PARALLELISM=false
mkdir -p study8/logs
caffeinate -dimsu .venv/bin/python -B -u study8/judges/judge_probe.py 2>&1 | tee -a study8/logs/judge_probe_v03.log
echo; echo "Done. You can close this window."
