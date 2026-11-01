#!/usr/bin/env python3
"""Hackathon schedule with hard gates and a Mermaid Gantt.

  timeline.py --hours 36 --start "2026-11-07 10:00" [--team 3] [--format md|mermaid|both]

Phase shares follow patterns reported by winner analyses: skeleton running by ~25%,
feature freeze ~72%, last ~15-18% for demo and submission.
"""
import argparse
from datetime import datetime, timedelta

PHASES = [
    ("P0 Rubric, research, idea lock", 0.00, 0.08, "Profile, research brief, GO verdict, demo script v0"),
    ("P1 Walking skeleton", 0.08, 0.25, "Ugly end-to-end path with fake data runs"),
    ("P2 Core build", 0.25, 0.55, "Deep component real; golden path on real data"),
    ("P3 Integrate + differentiator", 0.55, 0.72, "Sponsor API, eval harness; FEATURE FREEZE at end"),
    ("P4 Harden + deploy", 0.72, 0.82, "Fallback chain, replay mode, prod deploy, smoke test"),
    ("P5 Demo + submission", 0.82, 0.97, "Video, README, diagram, submission form, preflight"),
    ("Buffer", 0.97, 1.00, "Fix/resubmit only"),
]
GATES = [
    (0.25, "G1", "Golden path runs end to end. Else: cut to the single hardest flow."),
    (0.55, "G2", "Deep component is real. Else: simpler technique, disclose limits."),
    (0.72, "G3", "FEATURE FREEZE; deploy works. Else: bugs and demo only."),
    (0.82, "G4", "Prod URL + smoke test pass. Else: recorded video + local demo."),
    (0.95, "G5", "Submission complete. Else: submit now, polish later."),
]
TEAM = {1: "solo: slice-by-slice, AI agents for boilerplate, skip all unscored work",
        2: "A backend/AI core + infra | B frontend + demo + submission assets",
        3: "A backend/AI | B frontend/demo | C data/eval/integration",
        4: "A backend/AI | B frontend | C data/eval | D devops/deploy/tests/video",
        5: "A backend/AI | B frontend | C data/eval | D devops/deploy | E research + sponsor integration"}


def fmt(dt):
    return dt.strftime("%a %d %b %H:%M")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--hours", type=float, required=True)
    p.add_argument("--start", required=True, help='"YYYY-MM-DD HH:MM"')
    p.add_argument("--team", type=int, default=3)
    p.add_argument("--format", choices=["md", "mermaid", "both"], default="both")
    a = p.parse_args()
    start = datetime.strptime(a.start, "%Y-%m-%d %H:%M")
    at = lambda f: start + timedelta(hours=a.hours * f)
    end = at(1.0)
    if a.format in ("md", "both"):
        print(f"# Schedule: {a.hours:g}h, {fmt(start)} -> {fmt(end)}\n")
        print("| Phase | Start | End | Hours | Output |\n|---|---|---|---|---|")
        for name, s, e, out in PHASES:
            print(f"| {name} | {fmt(at(s))} | {fmt(at(e))} | {a.hours*(e-s):.1f} | {out} |")
        print("\n## Gates\n| Gate | Time | Pass condition / if failed |\n|---|---|---|")
        for f, g, msg in GATES:
            print(f"| {g} | {fmt(at(f))} | {msg} |")
        t = TEAM.get(max(1, min(5, a.team)), TEAM[5])
        print(f"\n## Roles ({a.team})\n{t}\n")
    if a.format in ("mermaid", "both"):
        print("```mermaid\ngantt\n  dateFormat  YYYY-MM-DD HH:mm\n  axisFormat  %d %H:%M")
        for i, (name, s, e, _o) in enumerate(PHASES):
            label = " ".join(name.replace(":", " ").replace(",", " ").split())
            print(f"  {label} :p{i}, {at(s).strftime('%Y-%m-%d %H:%M')}, {at(e).strftime('%Y-%m-%d %H:%M')}")
        print("```")


if __name__ == "__main__":
    main()
