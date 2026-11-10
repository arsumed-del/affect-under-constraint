"""Exploratory trace-length analysis (see LENGTH_ANALYSIS_PLAN.md). Not preregistered."""
import json
import sys
from pathlib import Path

import numpy as np

ROOT = Path(sys.argv[1])
OUT = Path(sys.argv[2])
B = 10_000
rng = np.random.default_rng(20261109)
SOURCES = ["hostility", "technicality", "random", "unsteered"]
CAP = 1024


def expected(probs):
    p = np.array([probs[str(d)] for d in range(10)], dtype=float)
    return float((p / p.sum()) @ np.arange(10))


def load_s4():
    data = {}
    for line in open(ROOT / "study4/data/main/cells.jsonl"):
        r = json.loads(line)
        if r.get("mode") != "main" or r["framing"] != "own_native":
            continue
        n = len(r["trace_ids"])
        data.setdefault(r["prompt_id"], {})[r["source"]] = (
            n, expected(r["ratings"]["sender"]["probabilities"]), n >= CAP - 1 or r["forced_closure"])
    return {"Study 4 (warmth instruction)": data}


def load_s8():
    sets = {c: {} for c in "NMP"}
    for line in open(ROOT / "study8/data/main/cells.jsonl"):
        r = json.loads(line)
        if r.get("mode") != "main" or r["arm"] != "generated" or r["context"] != r["generation_context"]:
            continue
        n = r["trace_length"]
        sets[r["context"]].setdefault(r["prompt_id"], {})[r["source"]] = (
            n, expected(r["ratings"]["O1"]["probabilities"]), n >= CAP - 1 or r["forced_closure"])
    names = {"N": "no message", "M": "kindness stake", "P": "accuracy stake"}
    return {f"Study 8 {c} ({names[c]})": d for c, d in sets.items()}


def complete(d):
    return {p: v for p, v in d.items() if all(s in v for s in SOURCES)}


def boot(prompts, stat):
    est = stat(prompts)
    idx = np.arange(len(prompts))
    draws = []
    for _ in range(B):
        sample = [prompts[i] for i in rng.choice(idx, len(idx))]
        draws.append(stat(sample))
    lo, hi = np.nanpercentile(draws, [2.5, 97.5])
    return est, lo, hi


def auc(a, b):
    a, b = np.asarray(a), np.asarray(b)
    gt = (a[:, None] > b[None, :]).mean()
    eq = (a[:, None] == b[None, :]).mean()
    return float(gt + 0.5 * eq)


def slope_within(rows):
    x = np.array([r[0] for r in rows]) / 100.0
    y = np.array([r[1] for r in rows])
    if len(x) < 3 or x.std() == 0:
        return float("nan")
    return float(np.polyfit(x, y, 1)[0])


def adjusted(rows_by_src):
    """OLS rating ~ length/100 + source dummies (unsteered reference). Returns (len coef, hostility coef)."""
    X, y = [], []
    for s, rows in rows_by_src.items():
        for n, r, _ in rows:
            X.append([1.0, n / 100.0] + [1.0 if s == t else 0.0 for t in SOURCES[:3]])
            y.append(r)
    beta, *_ = np.linalg.lstsq(np.array(X), np.array(y), rcond=None)
    return float(beta[1]), float(beta[2])


def analyze(name, d, keep=lambda v: True):
    d = complete(d)
    prompts = sorted(d)
    res = {"n_prompts": len(prompts)}
    res["mean_length"] = {s: float(np.mean([d[p][s][0] for p in prompts])) for s in SOURCES}
    res["capped"] = {s: int(sum(d[p][s][2] for p in prompts)) for s in SOURCES}
    res["mean_rating"] = {s: float(np.mean([d[p][s][1] for p in prompts])) for s in SOURCES}
    # A1
    for other in SOURCES[1:]:
        res[f"A1_len_H_minus_{other}"] = boot(prompts, lambda ps, o=other: float(np.mean([d[p]["hostility"][0] - d[p][o][0] for p in ps])))
        res[f"A1_auc_H_vs_{other}"] = auc([d[p]["hostility"][0] for p in prompts], [d[p][other][0] for p in prompts])
    # A3
    res["A3_within_hostility_slope_per100"] = boot(prompts, lambda ps: slope_within([d[p]["hostility"] for p in ps if keep(d[p]["hostility"])]))
    res["A3_adjusted_length_coef_per100"] = boot(prompts, lambda ps: adjusted({s: [d[p][s] for p in ps if keep(d[p][s])] for s in SOURCES})[0])
    # A4
    res["A4_hostility_effect_unadjusted"] = boot(prompts, lambda ps: float(np.mean([d[p]["hostility"][1] - d[p]["unsteered"][1] for p in ps])))
    res["A4_hostility_effect_length_adjusted"] = boot(prompts, lambda ps: adjusted({s: [d[p][s] for p in ps if keep(d[p][s])] for s in SOURCES})[1])
    return res


def did(d_a, d_b, other):
    da, db = complete(d_a), complete(d_b)
    prompts = sorted(set(da) & set(db))
    f = lambda ps: float(np.mean([(da[p]["hostility"][0] - da[p][other][0]) - (db[p]["hostility"][0] - db[p][other][0]) for p in ps]))
    return boot(prompts, f)


def main():
    sets = {**load_s4(), **load_s8()}
    results = {"plan": "LENGTH_ANALYSIS_PLAN.md", "status": "exploratory, not preregistered", "datasets": {}}
    for name, d in sets.items():
        print(f"Analyzing {name}...", flush=True)
        results["datasets"][name] = {
            "all": analyze(name, d),
            "excluding_capped": analyze(name, d, keep=lambda v: not v[2]),
        }
    s8 = {k[8]: v for k, v in sets.items() if k.startswith("Study 8")}
    print("Analyzing A2 (constraint dependence)...", flush=True)
    results["A2_Study8"] = {f"M_minus_N_vs_{o}": did(s8["M"], s8["N"], o) for o in SOURCES[1:]}
    results["A2_Study8"].update({f"P_minus_N_vs_{o}": did(s8["P"], s8["N"], o) for o in SOURCES[1:]})
    OUT.write_text(json.dumps(results, indent=1))
    print("Done.", flush=True)


if __name__ == "__main__":
    main()
