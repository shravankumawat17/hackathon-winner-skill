# 03 - Idea Court: verdicts, pivots, and defending

Goal: decide whether an idea can win, say it bluntly, and offer a better one when it cannot.

## Contents
- Gates
- Scoring
- Verdict card
- Saturated ideas and the wedge test
- Generating ideas when the user has none
- Pivot toolkit
- Defend / reverse protocol
- Pre-mortem

## Gates (any failure = NO-GO until fixed)
| Gate | Test |
|---|---|
| G1 Demo-ability | One end-to-end flow shown in <=3 minutes with a visible result |
| G2 Feasibility | Core build fits in <=60% of the available hours with the team's actual skills |
| G3 Differentiation | After prior-art search, you can state the new part in one sentence |
| G4 Rubric fit | Maps to at least two top-weighted criteria |
| G5 Cost | Runs the full demo on free/student tier including demo-day burst (`scripts/cost_estimate.py`) |
| G6 Compliance | Rules, data licenses, API terms allow it (`15-integrity-and-rules.md`) |

## Scoring
Run `python scripts/idea_scorecard.py` with 0-5 scores per criterion and the event's weights. Thresholds: **>=75 GO, 60-74 PIVOT, <60 NO-GO**. Gates override. Scores must be justified by research evidence, not feeling; if a score is a guess, grade it D.

## Verdict card
Template: `assets/templates/verdict-card.md`. Required lines: Verdict | Reason in one sentence | Strongest evidence | Biggest risk | Pivot or replacement | Kill criterion (the hour/test at which to abandon).

## Saturated ideas and the wedge test
Judges see these constantly. They are **NO-GO as stated** and become eligible only with a wedge:
chat-with-PDF/RAG chatbot, generic ChatGPT wrapper, resume/cover-letter analyzer, generic mental-health chatbot, expense tracker, to-do/habit app, generic study-buddy, plain "AI tutor", generic recommendation engine, "Uber for X" without a technical core.

Wedge test (need >=2): (1) proprietary or hard-to-get data, (2) a measurable evaluation showing it beats the naive baseline, (3) real integration with a system of record/hardware/sponsor API in the core path, (4) a narrow, named user with a verified workflow, (5) a technique the prior art lacks (verified), (6) offline/low-resource/regional constraint that changes the architecture.

## Generating ideas when the user has none
Constraint-first, not brainstorm-first:
1. Profile: rubric weights x sponsor tech x team skills x accessible data/hardware.
2. Mine L2/L3/L6: what won before, what is under-served, what is newly possible (last 90 days).
3. Produce **3** candidates, each with: user, painful workflow, core technical component, data source, demo flow in 5 steps.
4. Score all three with the script; present the top one as the recommendation, the other two as ranked fallbacks with their kill criteria.
5. Do not output a long list. Do not reuse candidates already in the ledger.

## Pivot toolkit (choose the smallest change that clears the failed gate)
Narrow the user | swap the modality (text to voice/vision/sensor) | replace the "chat" interface with an automated workflow | add a measurable eval or benchmark | bind to a sponsor API in the core path | move from cloud to on-device/offline | add a proprietary or scraped-with-permission dataset | turn the product into a developer tool/MCP server/SDK | shrink to the single hardest flow.

## Defend / reverse protocol
- Evidence supports the idea and the user pushes back with no new evidence: **Hold.** Output: `Holding: <verdict>. Strongest evidence: <claim | source | date>. To change my mind, show: <specific counter-evidence or test>.`
- New evidence appears (user's or yours): re-run the relevant lens, then `Reversing: <what changed and source>` or `Holding: <why>`.
- Never reverse because the user is frustrated, repeats themselves, or claims authority.
- Never defend a position against better evidence out of consistency. Updating on evidence is required.
- NO-GO overruled by the user: give the single failure mode once, then give the lowest-risk build plan.

## Pre-mortem (mandatory for GO and PIVOT)
List the 3 most likely ways this fails on demo day, each with a cheap mitigation and a test. Typical: rate limit hit by judges, API latency, empty-state data, auth wall, wifi, model non-determinism, hardware not connecting.
