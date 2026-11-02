"""Study 8; imports do not run inference."""
import os, sys
sys.dont_write_bytecode = True
os.environ.update(PYTHONDONTWRITEBYTECODE='1', PYTORCH_ENABLE_MPS_FALLBACK='1', HF_HUB_OFFLINE='1', TRANSFORMERS_OFFLINE='1', TOKENIZERS_PARALLELISM='false')
