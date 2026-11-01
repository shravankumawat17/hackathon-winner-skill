# 01 - Intake and rubric extraction

Goal: convert the event into a **Hackathon Profile** (template: `assets/templates/hackathon-profile.md`) and a **weighted rubric table**. Every later decision (idea, stack, scope, demo) is derived from these two artifacts.

## Contents
- Intake order
- What to fetch yourself vs ask
- Rubric to build-decision mapping
- Event-type adjustments
- Sponsor and track strategy
- Rules compliance gate

## Intake order
1. If the user gave a URL, fetch it, then fetch linked rules, FAQ, judging, prizes, sponsor pages. Do not summarize from the landing page alone.
2. If only a name was given, search for the official page, then the Devpost/Devfolio/Unstop/DoraHacks listing, then last edition's winners.
3. Fill the profile. Mark each field `found (source)` or `unknown`.
4. Ask the user only for unknowns that are **blocking** (see `14-decisions-and-questions.md`).

## Fields (all required before a verdict)
Event name and edition | duration and exact deadline with timezone | online/in-person | team size limits | tracks and sponsor prizes | judging criteria and weights | submission format (repo, video length, deck, live demo) | rules on pre-existing code, AI-generated code, open-source licenses, datasets | mandatory tech (sponsor API/SDK/cloud) | team skills and hardware | budget | target platform.

## Fetch vs ask
Fetch: rules, rubric, deadlines, sponsor APIs, prior winners, judge list.
Ask: team skills, budget, hardware, preferences between two equally valid directions, anything private.

## Rubric to build-decision mapping
Rubrics rarely say what they reward. Translate:

| Criterion (typical) | Technical translation | Build consequence |
|---|---|---|
| Innovation / originality | A novel *combination* or a novel constraint, verified against prior art | Run the prior-art lens before committing; name the new part in one sentence |
| Technical implementation | A genuinely built core component, correct engineering, evidence | One deep component (own retrieval, own agent loop, own pipeline, own model fine-tune), plus tests/evals and a measured number |
| Impact / problem-solving | Specific user, quantified pain, working solution on realistic data | Use real or realistic datasets, show before/after metric |
| Design / UX | One clean flow, no dead ends, fast feedback | See `06-ui-for-demos.md` |
| Presentation / demo | Demo runs end to end, explainable in 3 minutes | See `09-demo-engineering-and-qa.md` |
| Sponsor tech usage | Deep, load-bearing use of the sponsor SDK, not a logo integration | Make the sponsor API part of the core path or do not claim the prize |
| Feasibility / scalability | Credible path beyond demo | One architecture slide, one cost-per-user number |
| Completeness | Everything promised works | Cut scope until true |

Weights: if the organizer publishes weights, use them. If not, ask organizers (Discord/Slack/email) for the weights; until then, use the default weights in `scripts/idea_scorecard.py` and label them an assumption.

## Event-type adjustments
| Type | Decision shift |
|---|---|
| 24h in-person | Walking skeleton by 25% of the clock, one flow, offline-safe demo, hardware loaded early |
| 36-48h | Same plus one extra differentiator and an eval number |
| Online multi-day/week | Depth, docs, tests, deploy, video quality; judges read the repo, so README and architecture matter more |
| AI/GenAI track | A wrapper loses; need grounding, tool use, evals, or a proprietary data angle |
| Hardware/IoT | Integration risk dominates: order/borrow parts first, test sensors in the first 10%, record backup video |
| Web3 | Testnet only, verified contract, one real on-chain action in demo, audit-style notes |
| Social good | Real data/partner/regulatory grounding, accessibility, low-bandwidth/regional-language support if applicable |
| Corporate/sponsor challenge | Solve the sponsor's stated problem using their API in the core path |

## Sponsor and track strategy
- Primary: **one** main track you can win.
- Secondary: at most **two** sponsor prizes where the sponsor tech is load-bearing and takes <15% of build time.
- Verify each sponsor prize's actual criteria and whether stacking is allowed.
- Ask organizers for sponsor credits and mentors early; sponsors often provide free quota (verify).

## Rules compliance gate
Before any build advice, check: team size, code written during the event only or allowed prior work, AI-code policy, dataset/license limits, required submission assets, eligibility (student status, region), IP/ownership terms. A rules violation is an automatic NO-GO for the idea. See `15-integrity-and-rules.md`.
