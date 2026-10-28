#!/bin/zsh
cd "${0:A:h:h}"
export PYTHONDONTWRITEBYTECODE=1
.venv/bin/python -B -u -m study6.analysis.analyze 2>&1 | tee -a study6/logs/analysis.log
echo; echo "Done. You can close this window."
