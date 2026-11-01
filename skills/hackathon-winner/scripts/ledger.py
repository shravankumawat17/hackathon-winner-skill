#!/usr/bin/env python3
"""Session ledger: remembers every idea/tool/angle already suggested so answers never repeat.

Usage:
  ledger.py add   --kind idea --key rag-for-tax --text "one-line summary"
  ledger.py check --text "candidate suggestion" [--kind idea] [--strict]
  ledger.py list  [--kind tool]
  ledger.py lenses            # which research lens (L1-L10) was used least recently
  ledger.py reset

Ledger path: $HACKATHON_LEDGER or .hackathon/ledger.jsonl
"""
import argparse, json, os, re, sys, time

LENSES = ["L1", "L2", "L3", "L4", "L5", "L6", "L7", "L8", "L9", "L10"]
LENS_NAMES = {
    "L1": "Rubric intel", "L2": "Past winners", "L3": "Prior art / novelty",
    "L4": "Sponsor tech", "L5": "Feasibility spike", "L6": "Trend signal",
    "L7": "Cost and limits", "L8": "Data and licensing", "L9": "Failure modes",
    "L10": "Judge profile (technical)",
}
STOP = set("""a an the and or of to in on for with by from at as is are be this that it its into your our their
using use via app application system platform tool based new simple build built make makes help helps""".split())
PATH = os.environ.get("HACKATHON_LEDGER", os.path.join(".hackathon", "ledger.jsonl"))


def tokens(text):
    words = re.findall(r"[a-z0-9]+", text.lower())
    return {w[:-1] if len(w) > 4 and w.endswith("s") else w for w in words if w not in STOP and len(w) > 1}


def load():
    if not os.path.exists(PATH):
        return []
    rows = []
    with open(PATH, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    rows.append(json.loads(line))
                except json.JSONDecodeError:
                    continue
    return rows


def jaccard(a, b):
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def cmd_add(args):
    os.makedirs(os.path.dirname(PATH) or ".", exist_ok=True)
    row = {"ts": int(time.time()), "kind": args.kind, "key": args.key, "text": args.text}
    with open(PATH, "a", encoding="utf-8") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")
    print(f"added [{args.kind}] {args.key}")


def cmd_check(args):
    rows = [r for r in load() if not args.kind or r.get("kind") == args.kind]
    cand = tokens(args.text)
    worst = 0.0
    hits = []
    for r in rows:
        score = max(jaccard(cand, tokens(r.get("text", ""))), 1.0 if r.get("key") == args.text.strip().lower() else 0.0)
        if score >= 0.30:
            hits.append((score, r))
        worst = max(worst, score)
    hits.sort(key=lambda x: -x[0])
    if worst >= 0.50:
        print("REPEAT: this was already given. Do not present it as new; give a delta or something different.")
    elif worst >= 0.30:
        print("SIMILAR: state explicitly how this differs from earlier items.")
    else:
        print("NEW: no close match in ledger.")
    for score, r in hits[:5]:
        print(f"  {score:.2f}  [{r.get('kind')}] {r.get('key')}: {r.get('text')}")
    if args.strict and worst >= 0.50:
        sys.exit(2)


def cmd_list(args):
    rows = [r for r in load() if not args.kind or r.get("kind") == args.kind]
    if not rows:
        print("(ledger empty)")
    for r in rows:
        print(f"[{r.get('kind')}] {r.get('key')}: {r.get('text')}")


def cmd_lenses(_args):
    last = {l: 0 for l in LENSES}
    count = {l: 0 for l in LENSES}
    for r in load():
        if r.get("kind") == "lens":
            key = str(r.get("key", "")).upper()
            if key in last:
                last[key] = max(last[key], r["ts"])
                count[key] += 1
    order = sorted(LENSES, key=lambda l: (last[l], count[l]))
    print("Research lenses, least recently used first:")
    for l in order:
        print(f"  {l}  {LENS_NAMES[l]:<28} used {count[l]}x")
    print(f"Suggested next lens: {order[0]} ({LENS_NAMES[order[0]]})")


def cmd_reset(_args):
    if os.path.exists(PATH):
        os.remove(PATH)
    print("ledger cleared")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("add"); a.add_argument("--kind", required=True); a.add_argument("--key", required=True); a.add_argument("--text", required=True); a.set_defaults(fn=cmd_add)
    c = sub.add_parser("check"); c.add_argument("--text", required=True); c.add_argument("--kind"); c.add_argument("--strict", action="store_true"); c.set_defaults(fn=cmd_check)
    l = sub.add_parser("list"); l.add_argument("--kind"); l.set_defaults(fn=cmd_list)
    n = sub.add_parser("lenses"); n.set_defaults(fn=cmd_lenses)
    r = sub.add_parser("reset"); r.set_defaults(fn=cmd_reset)
    args = p.parse_args()
    args.fn(args)


if __name__ == "__main__":
    main()
