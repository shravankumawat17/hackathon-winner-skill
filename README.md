# hackathon-winner

A technical copilot **skill** that helps students win hackathons. It researches the event, rubric, sponsors and prior art with live tools, then gives blunt, evidence-backed verdicts and concrete architecture, stack, UI, workflow, deployment and demo plans, on a student budget.

Built on the open [Agent Skills](https://github.com/agentskills/agentskills) format (`SKILL.md` + `references/` + `scripts/` + `assets/`), so one repo works in Codex, OpenCode, Claude, Gemini CLI, Cursor-style agents, and ChatGPT.

## What it does differently

| Capability | How it is enforced |
|---|---|
| Technical answers only | Scope rule + integrity module; no motivation, flattery, or persuasion tactics |
| Says NO and gives a better path | GO / PIVOT / NO-GO verdicts, hard gates, `idea_scorecard.py` |
| Defends good ideas | Pushback protocol: holds position unless new evidence appears |
| Research before opinion | Research Gate: >=3 searches, >=1 primary source, A-D evidence grading, 10 research lenses |
| Full winning-team structure | Intake, rubric, architecture, stack, UI, harness, timeline, distribution, demo, Q&A |
| Diagrams everywhere | Mermaid library + templates, with ASCII fallback |
| Never repeats itself | Session ledger, lens rotation, delta answers, banned-defaults list |
| Student budget, full quality | $0-first cost ladder, dated free-tier snapshot, live re-verification, fallback chains |
| Asks when stuck | Structured question protocol (max 3, with recommended defaults) |
| Safe and honest | Disclosure of mocks, rules/ToS checks, secret scanner |

## Repo map

```
skills/hackathon-winner/
  SKILL.md                  router + rules (loaded when triggered)
  references/01..15-*.md    modules, loaded on demand
  scripts/                  ledger, idea_scorecard, timeline, cost_estimate, submission_check (Python 3, stdlib only)
  assets/templates/         profile, research brief, verdict card, architecture doc, demo script, README, preflight
  assets/diagrams/          ready Mermaid files
  assets/data/free_tiers.json  dated free-tier snapshot (verify before use)
AGENTS.md                   fallback for tools that read AGENTS.md instead of skills
CHATGPT_PASTE.md            short + full instructions for ChatGPT Projects / Custom GPTs
install.sh / install.ps1    copy the skill into the right folder for each tool
tools/validate_repo.py      checks frontmatter and structure
evals/test-prompts.md       scenarios to verify behavior
```

## Install (summary; details in INSTALL.md)

```bash
# any tool supporting the Skills CLI
npx skills add <your-github-user>/hackathon-winner-skill

# manual: OpenCode / Codex / Claude, project-level
./install.sh --opencode --codex --claude     # copies to .opencode/skills, .agents/skills, .claude/skills
```

ChatGPT: see INSTALL.md (native skill import where available, otherwise a Project with `CHATGPT_PASTE.md`).

## Use

Just talk about your hackathon. Examples:
- "I'm joining <hackathon>, 36 hours, team of 3 (Python + React). Here is the rules page: <url>"
- "Is this idea good enough to win? <idea>"
- "Which stack and architecture should I use? Student budget."
- "Plan the timeline and give me the diagrams."
- "Audit my repo before submission."

Optional helpers:
```bash
python skills/hackathon-winner/scripts/idea_scorecard.py --name "Idea A" --scores demo=4,feasibility=4,rubric=3,diff=4,depth=3,impact=4,cost=5,risk=3
python skills/hackathon-winner/scripts/timeline.py --hours 36 --start "2026-11-07 10:00" --team 3
python skills/hackathon-winner/scripts/cost_estimate.py --provider groq --burst-users 30 --reqs-per-user 6 --window-min 10
python skills/hackathon-winner/scripts/submission_check.py ./my-project
python skills/hackathon-winner/scripts/ledger.py lenses
```

## Maintaining it

Free tiers and tool limits change monthly. The skill never treats `free_tiers.json` as truth; it forces live verification. When you re-verify a provider, update the entry and `snapshot_date`.

## License
MIT
