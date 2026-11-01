#!/usr/bin/env python3
"""Deterministic idea scorecard with hard gates.

Score each criterion 0-5 (5 = best). Risk is inverted: 5 = low risk.

Single idea:
  idea_scorecard.py --name "Idea A" --scores demo=4,feasibility=4,rubric=3,diff=4,depth=3,impact=4,cost=5,risk=3

Compare ideas from JSON ([{"name":..., "scores":{...}, "noncompliant":false}, ...]):
  idea_scorecard.py --ideas ideas.json

Override weights (auto-normalised to 100), e.g. when the rubric stresses impact:
  idea_scorecard.py ... --weights impact=25,depth=15

Verdict: >=75 GO | 60-74 PIVOT | <60 NO-GO. Any hard gate failure forces NO-GO.
"""
import argparse, json, sys

CRITERIA = {
    # key: (label, default weight)
    "demo": ("Demo-ability (3-min end-to-end)", 15),
    "feasibility": ("Feasibility in time budget", 20),
    "rubric": ("Rubric fit", 15),
    "diff": ("Differentiation vs prior art", 15),
    "depth": ("Technical depth", 10),
    "impact": ("Impact clarity", 10),
    "cost": ("Cost fit (free/student tier, demo-day burst)", 10),
    "risk": ("Risk (5 = low)", 5),
}
GATES = {"demo": 2, "feasibility": 2, "diff": 2, "cost": 2}  # score must be >= value (matches G1,G2,G3,G5 in 03-idea-court.md)


def parse_kv(s):
    out = {}
    for part in filter(None, (s or "").split(",")):
        k, _, v = part.partition("=")
        out[k.strip()] = float(v)
    return out


def weights(override):
    w = {k: float(v[1]) for k, v in CRITERIA.items()}
    for k, v in override.items():
        if k not in w:
            sys.exit(f"unknown criterion '{k}'. valid: {', '.join(CRITERIA)}")
        w[k] = v
    total = sum(w.values())
    return {k: v * 100.0 / total for k, v in w.items()}


def evaluate(idea, w):
    sc = idea["scores"]
    missing = [k for k in CRITERIA if k not in sc]
    if missing:
        sys.exit(f"{idea.get('name','idea')}: missing scores for {', '.join(missing)}")
    for k, v in sc.items():
        if k in CRITERIA and not 0 <= v <= 5:
            sys.exit(f"{k} must be 0-5")
    total = sum(sc[k] / 5.0 * w[k] for k in CRITERIA)
    failed = [f"{CRITERIA[k][0]} < {m}" for k, m in GATES.items() if sc[k] < m]
    if idea.get("noncompliant"):
        failed.append("Rules/terms compliance")
    if failed:
        verdict = "NO-GO (gate)"
    elif total >= 75:
        verdict = "GO"
    elif total >= 60:
        verdict = "PIVOT"
    else:
        verdict = "NO-GO"
    # biggest weighted shortfall first
    shortfall = sorted(CRITERIA, key=lambda k: -(w[k] * (5 - sc[k]) / 5.0))[:2]
    return {"name": idea.get("name", "idea"), "score": round(total, 1), "verdict": verdict,
            "gates_failed": failed, "fix_first": [CRITERIA[k][0] for k in shortfall]}


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--name", default="idea")
    p.add_argument("--scores")
    p.add_argument("--ideas")
    p.add_argument("--weights", default="")
    p.add_argument("--noncompliant", action="store_true")
    p.add_argument("--json", action="store_true", help="machine-readable output")
    a = p.parse_args()
    w = weights(parse_kv(a.weights))
    ideas = []
    if a.ideas:
        with open(a.ideas, encoding="utf-8") as f:
            ideas = json.load(f)
    elif a.scores:
        ideas = [{"name": a.name, "scores": parse_kv(a.scores), "noncompliant": a.noncompliant}]
    else:
        p.error("provide --scores or --ideas")
    results = sorted((evaluate(i, w) for i in ideas), key=lambda r: -r["score"])
    if a.json:
        print(json.dumps({"weights": w, "results": results}, indent=2))
        return
    print("Weights (%): " + ", ".join(f"{k}={w[k]:.0f}" for k in CRITERIA))
    print(f"{'Idea':<34}{'Score':>7}  Verdict        Fix first")
    for r in results:
        gate = f"  [gate: {'; '.join(r['gates_failed'])}]" if r["gates_failed"] else ""
        print(f"{r['name'][:33]:<34}{r['score']:>7}  {r['verdict']:<13}  {', '.join(r['fix_first'])}{gate}")


if __name__ == "__main__":
    main()
