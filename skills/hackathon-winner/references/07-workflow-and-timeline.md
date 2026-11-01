# 07 - Workflow, roles, and timeline

Goal: a schedule with hard gates so scope is cut early, not at hour 20.

## Contents
- Phase model
- Gates and cut ladder
- Role map
- Git workflow
- Checkpoint rules
- Script

## Phase model (percent of total hours; derived from published winner patterns, adapt to the event)
| Phase | Share | Output |
|---|---|---|
| P0 Rubric, research, idea lock | 0-8% | Profile, research brief, verdict GO, one-sentence pitch, demo script v0 |
| P1 Walking skeleton | 8-25% | Ugly end-to-end path with fake data, deployed or runnable |
| P2 Core build | 25-55% | The deep component is real; golden path works with real data |
| P3 Integrate + differentiator | 55-72% | Sponsor integration, eval harness, second-priority features. **Feature freeze at 72%** |
| P4 Harden + deploy | 72-82% | Error states, fallback chain, cached demo mode, production deploy, smoke test |
| P5 Demo + submission | 82-97% | Recorded video, README, architecture diagram, submission form, preflight |
| Buffer | 97-100% | Resubmit/fix only |
Research from several winner analyses points the same way: a rough skeleton early beats raw skill, and the last 15-20% belongs to demo and submission.

## Gates and cut ladder
| Gate | Condition | If failed |
|---|---|---|
| G1 (25%) | Golden path runs end to end | Cut P2 features to the single hardest flow; drop all P1/P2 items |
| G2 (55%) | Deep component real, demo-able | Replace with simpler technique; disclose limits |
| G3 (72%) | Feature freeze, deploy works | No new features. Bugs and demo only |
| G4 (82%) | Production URL + smoke test pass | Fall back to recorded video + local demo |
| G5 (95%) | Submission complete | Submit now; polish after |

Cut ladder: P0 must-have for demo | P1 improves score | P2 nice to have. Cut from the bottom the moment a gate fails.

## Role map (technical ownership)
| Team size | Split |
|---|---|
| 1 | You: slice-by-slice, demo-first; use AI agents for boilerplate; skip everything unscored |
| 2 | A: backend/AI core + infra; B: frontend + demo + submission assets |
| 3 | + C: data/eval/integration |
| 4 | + D: devops, deploy, tests, README, video |
| 5 | + E: research/prior art + sponsor integration |
Everyone owns directories, not tasks; merge to trunk every 1-2 hours; one integrator owns deploy.

## Git workflow
Trunk-based, short branches, protected main (if available), tag `v-demo-ready` at each gate, never force-push, `.gitignore` and secrets check before the first push.

## Checkpoint rules
- Re-read the rubric at each gate.
- Every checkpoint: does the golden path still work on the deployed build?
- A new idea after P0 is only accepted if it replaces something of equal or greater cost and raises a top-weighted criterion.

## Script
`python scripts/timeline.py --hours 36 --start "YYYY-MM-DD HH:MM" --team 3` prints the schedule, gates with clock times, and a Mermaid Gantt.
