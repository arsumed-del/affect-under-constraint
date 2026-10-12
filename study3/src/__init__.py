import os
from pathlib import Path
_CACHE=Path(__file__).resolve().parents[1]/'.cache'
os.environ['HF_HOME']=str(_CACHE/'huggingface')
os.environ['HF_HUB_CACHE']=str(_CACHE/'huggingface/hub')
os.environ['XDG_CACHE_HOME']=str(_CACHE)
os.environ['PYTORCH_ENABLE_MPS_FALLBACK']='1'
os.environ['PYTHONDONTWRITEBYTECODE']='1'
