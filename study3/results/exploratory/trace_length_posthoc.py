"""Exploratory, NOT preregistered: trace length and total carryover (Study 3, Section 4.5 of the paper).
Run from study3/: python3 trace_length_posthoc.py  (needs numpy). Reads data/raw/qwen3-4b_main.jsonl."""
import json, random
import numpy as np
rows = [json.loads(l) for l in open('data/raw/qwen3-4b_main.jsonl')]
I = {(r['prompt_id'], r['mode'], r['route'], r['direction'], r['dose_fraction']): r for r in rows}
P = sorted({r['prompt_id'] for r in rows}); D = ['hostility', 'technicality', 'random']
rng = random.Random(20261012)
idx = [[rng.randrange(80) for _ in range(80)] for _ in range(10000)][:2000]
def fit(ps, delta):
    X, Y = [], []
    for p in ps:
        for d in D:
            r = I[(p, 'think', 'regular', d, 1.0)]
            y = r['C'] - (I[(p, 'direct', 'regular', d, 1.0)]['C'] if delta else 0)
            X.append([1, d == 'hostility', d == 'technicality', len(r['thinking_ids']) / 100]); Y.append(y)
    return np.linalg.lstsq(np.array(X, float), np.array(Y), rcond=None)[0]
for delta in (False, True):
    b = fit(P, delta); bs = np.array([fit([P[i] for i in ix], delta) for ix in idx])
    print('outcome', 'delta_C' if delta else 'C_think')
    for j, name in [(1, 'hostility vs random'), (2, 'technicality vs random'), (3, 'per 100 trace tokens')]:
        print(f'  {name}: {b[j]:+.3f} [{np.percentile(bs[:, j], 2.5):+.3f}, {np.percentile(bs[:, j], 97.5):+.3f}]')
L = [len(I[(p, 'think', 'regular', 'hostility', 1.0)]['thinking_ids']) for p in P]
C = [I[(p, 'think', 'regular', 'hostility', 1.0)]['C'] for p in P]
print('corr(length, C) within hostility:', round(float(np.corrcoef(L, C)[0, 1]), 3))
