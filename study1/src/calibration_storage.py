"""Reviewer-authorized, write-once calibration records per model."""
from pathlib import Path


def calibration_paths(model_id):
    if model_id == 'Qwen/Qwen2.5-3B-Instruct':
        return Path('data/calibration.json'), Path('results/calibration_hash.sha256')
    if model_id == 'google/gemma-2-2b-it':
        return Path('data/calibration_gemma-2-2b-it.json'), Path('results/calibration_hash_gemma.sha256')
    raise ValueError(f'Unspecified model: {model_id}')
