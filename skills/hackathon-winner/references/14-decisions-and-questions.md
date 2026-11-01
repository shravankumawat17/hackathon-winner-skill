# 14 - Decisions and clarifying questions

Goal: decide fast; ask only when the answer changes the decision and cannot be found.

## Contents
- Decide vs ask
- Blocking questions
- Question format
- Host question tools
- Decision records
- Stuck protocol

## Decide vs ask
| Situation | Action |
|---|---|
| Answer is findable (rules, limits, prior art) | Research it |
| Options differ in score by a clear margin | Decide, state why |
| Options near-tie and depend on a private fact (skills, preference, hardware, budget) | **Ask** |
| Choice is irreversible/expensive (paid plan, hardware order) | **Ask** |
| You lack tools to verify a claim that decides the outcome | Ask the user to run one specific check |

## Blocking questions (typical)
Team skills/languages | hardware available | budget ceiling | deadline/timezone | which track/prize to target | allowed prior code | demo environment (projector, wifi, laptop).

## Question format
- Ask **immediately** when blocked; do not produce a long speculative answer first.
- Max **3** questions per turn; one if possible.
- Each question: 2-4 mutually exclusive options plus a **recommended default** and one-line consequence of each.
- Provide the provisional plan that applies if the user does not answer.

Example:
`Q1. Team backend skill? (a) Python [recommended: fastest path to your AI core], (b) TypeScript, (c) mixed. Default if no answer: (a).`

## Host question tools
Use the host's structured question/choice UI when available (Claude: ask-user tool; OpenCode: question tool; ChatGPT: native clarifying prompt/choices; Codex/Gemini CLI/others: equivalent prompts). If none, ask as a numbered multiple-choice list in plain text and stop. Do not continue with assumptions that could waste hours.

## Decision records
One line each, kept in `DECISIONS.md` or the answer: `ID | Decision | Alternatives | Evidence | Revisit trigger`.

## Stuck protocol
If you cannot decide after research: (1) state the two leading options, (2) the single fact that would decide, (3) the cheapest test to get it (spike or question), (4) ask. Never hide indecision behind generic advice.
