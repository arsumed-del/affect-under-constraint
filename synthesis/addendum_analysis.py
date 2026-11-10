"""Exploratory addendum A5-A7 (see LENGTH_ANALYSIS_PLAN.md addendum). Not preregistered."""
import json
import sys
from pathlib import Path

import numpy as np

ROOT = Path(sys.argv[1])
OUT = Path(sys.argv[2])
B = 10_000
rng = np.random.default_rng(20261109)
SOURCES = ["hostility", "technicality", "random", "unsteered"]


def expected(probs):
    p = np.array([probs[str(d)] for d in range(10)], dtype=float)
    return float((p / p.sum()) @ np.arange(10))


def boot(prompts, stat):
    est = stat(prompts)
    idx = np.arange(len(prompts))
    draws = [stat([prompts[i] for i in rng.choice(idx, len(idx))]) for _ in range(B)]
    lo, hi = np.nanpercentile(draws, [2.5, 97.5])
    return [est, float(lo), float(hi)]


# ---------- data: (length, rating, trace_eh) per prompt x source ----------
def load_s4():
    d = {}
    for line in open(ROOT / "study4/data/main/cells.jsonl"):
        r = json.loads(line)
        if r.get("mode") != "main" or r["framing"] != "own_native":
            continue
        d.setdefault(r["prompt_id"], {})[r["source"]] = (
            len(r["trace_ids"]), expected(r["ratings"]["sender"]["probabilities"]), float(r["EH_trace"]))
    return d


def load_s8():
    trace_eh = {}
    for line in open(ROOT / "study8/data/main/traces.jsonl"):
        t = json.loads(line)
        trace_eh[t["row_sha256"]] = float(t["classifier"]["eh"])
    sets = {c: {} for c in "NMP"}
    for line in open(ROOT / "study8/data/main/cells.jsonl"):
        r = json.loads(line)
        if r.get("mode") != "main" or r["arm"] != "generated" or r["context"] != r["generation_context"]:
            continue
        sets[r["context"]].setdefault(r["prompt_id"], {})[r["source"]] = (
            r["trace_length"], expected(r["ratings"]["O1"]["probabilities"]), trace_eh[r["trace_sha256"]])
    return sets


def fit(rows_by_src, with_eh):
    X, y = [], []
    for s, rows in rows_by_src.items():
        for n, r, eh in rows:
            x = [1.0, n / 100.0] + ([eh * 10] if with_eh else []) + [1.0 if s == t else 0.0 for t in SOURCES[:3]]
            X.append(x)
            y.append(r)
    beta, *_ = np.linalg.lstsq(np.array(X), np.array(y), rcond=None)
    k = 3 if with_eh else 2
    return beta, k


def a5(d):
    d = {p: v for p, v in d.items() if all(s in v for s in SOURCES)}
    prompts = sorted(d)
    rows = lambda ps: {s: [d[p][s] for p in ps] for s in SOURCES}
    out = {}
    out["length_coef_per100_adj_source_and_EH"] = boot(prompts, lambda ps: float(fit(rows(ps), True)[0][1]))
    out["EH_coef_per0.1_adj_source_and_length"] = boot(prompts, lambda ps: float(fit(rows(ps), True)[0][2]))
    out["hostility_effect_adj_length_and_EH"] = boot(prompts, lambda ps: float(fit(rows(ps), True)[0][3]))
    out["hostility_effect_adj_EH_only"] = boot(prompts, lambda ps: float(_eh_only(rows(ps))))
    out["mean_trace_EH"] = {s: float(np.mean([d[p][s][2] for p in prompts])) for s in SOURCES}
    return out


def _eh_only(rows_by_src):
    X, y = [], []
    for s, rows in rows_by_src.items():
        for n, r, eh in rows:
            X.append([1.0, eh * 10] + [1.0 if s == t else 0.0 for t in SOURCES[:3]])
            y.append(r)
    beta, *_ = np.linalg.lstsq(np.array(X), np.array(y), rcond=None)
    return beta[2]


# ---------- A6: Study 7 continuous warmth compliance ----------
def a6():
    d = {}
    for line in open(ROOT / "study7/data/main/cells.jsonl"):
        r = json.loads(line)
        if r.get("mode") != "main" or r["arm"] != "generated":
            continue
        c = r["answer_classifier"]
        d.setdefault(r["prompt_id"], {})[(r["source"], r["level"])] = (float(c["ew"]), float(c["eh"]))
    prompts = sorted(p for p, v in d.items() if all((s, l) in v for s in SOURCES for l in "NSG"))
    out = {"n_prompts": len(prompts)}
    for s in SOURCES:
        for i, name in enumerate(["EW", "EH"]):
            out[f"{name}_{s}_G_minus_N"] = boot(prompts, lambda ps, s=s, i=i: float(np.mean([d[p][(s, "G")][i] - d[p][(s, "N")][i] for p in ps])))
    for i, name in enumerate(["EW", "EH"]):
        out[f"{name}_interaction_hostility_vs_unsteered"] = boot(prompts, lambda ps, i=i: float(np.mean([
            (d[p][("hostility", "G")][i] - d[p][("hostility", "N")][i]) - (d[p][("unsteered", "G")][i] - d[p][("unsteered", "N")][i]) for p in ps])))
    out["mean_EW"] = {f"{s}_{l}": float(np.mean([d[p][(s, l)][0] for p in prompts])) for s in SOURCES for l in "NG"}
    return out


# ---------- A7: descriptive pooled estimate ----------
def a7(prev):
    est = []
    for name, v in prev["datasets"].items():
        e, lo, hi = v["all"]["A4_hostility_effect_unadjusted"]
        est.append((name, e, (hi - lo) / 3.92))
    w = np.array([1 / se ** 2 for _, _, se in est])
    m = float(np.sum(w * np.array([e for _, e, _ in est])) / w.sum())
    se = float(np.sqrt(1 / w.sum()))
    q = float(np.sum(w * (np.array([e for _, e, _ in est]) - m) ** 2))
    return {"inputs": est, "pooled": [m, m - 1.96 * se, m + 1.96 * se], "Q": q, "k": len(est),
            "caveat": "inputs share prompts; not independent; descriptive only"}


def main():
    prev = json.loads((OUT.parent / "length_results.json").read_text())
    res = {"status": "exploratory addendum, not preregistered"}
    print("A5 Study 4...", flush=True)
    res["A5"] = {"Study 4": a5(load_s4())}
    for c, d in load_s8().items():
        print(f"A5 Study 8 {c}...", flush=True)
        res["A5"][f"Study 8 {c}"] = a5(d)
    print("A6 Study 7...", flush=True)
    res["A6"] = a6()
    res["A7"] = a7(prev)
    OUT.write_text(json.dumps(res, indent=1))
    print("Done.", flush=True)


if __name__ == "__main__":
    main()
