# 02 - Research engine

Research is the main pillar. The goal is not "gather links" but to **reduce the probability of building the wrong thing**. Every research pass ends in a decision, a kill, or a named unknown.

## Contents
- Principles
- Research lenses (the 10)
- Tool order and host mapping
- Query templates
- Evidence grading
- Freshness rules
- Executable spikes
- Parallel fan-out
- Stop rule and output
- No-tools fallback

## Principles
1. Primary source beats secondary beats blog beats memory.
2. Fetch the page, do not trust the snippet.
3. Search for the **disconfirming** evidence first (who already built this, why it failed, where limits bite).
4. Every claim in an answer carries `source | date | grade`.
5. Prefer last 90 days for anything about tools, models, prices, limits, trends.
6. Different answer each time: rotate lenses (see `13-anti-repetition.md`).

## Research lenses
| # | Lens | Question answered | Best sources |
|---|---|---|---|
| L1 | Rubric intel | What does this event actually reward? | Official rules/FAQ, organizer Discord/announcements, judge bios |
| L2 | Past winners | What did winners of this event/series build, and why? | Devpost/Devfolio/DoraHacks galleries, winner blog posts, project READMEs |
| L3 | Prior art / novelty | Does this already exist? What is the gap? | GitHub search, Product Hunt, Hugging Face Spaces, app stores, arXiv, Google |
| L4 | Sponsor tech | What does the sponsor SDK/API enable, limit, and charge? | Sponsor docs, changelogs, quickstarts, example repos, sponsor staff talks |
| L5 | Feasibility spike | Can we build the risky 20% in hours? | Run a minimal prototype/API call; library issues; benchmarks |
| L6 | Trend signal | What are builders and judges currently excited or tired of? | HN, Reddit, GitHub trending, release notes, conference talks (last 90 days) |
| L7 | Cost and limits | What will it cost and where will free tiers break on demo day? | Official pricing/limits pages, status pages, `scripts/cost_estimate.py` |
| L8 | Data and licensing | Is there usable data, and are we allowed to use it? | Dataset licenses, API ToS, Kaggle/HF datasets, government open data |
| L9 | Failure modes | How do projects of this type fail in demos? | Postmortems, GitHub issues of chosen libs, "limitations" sections, judge write-ups |
| L10 | Judge profile (technical) | What do the judges' own work/interests imply technically? | Judges' public GitHub, talks, papers, company stack |

Pick lenses by the question. A verdict needs at least L1 or L2, L3, and L7 or L5.

## Tool order and host mapping
Use equivalents available in the host:
- **Web search + page fetch** (Claude: web search/fetch; ChatGPT: browsing/search, deep research for broad sweeps; OpenCode: webfetch/websearch where enabled; Codex/Gemini CLI: built-in web search).
- **Code search**: GitHub search UI/API, `gh search repos|code`, sourcegraph-style tools.
- **Shell/Python** for executable verification and scripts in this repo.
- **MCP servers** if connected: GitHub, docs-lookup, browser automation (Playwright), database, Figma.
- **Subagents/tasks** for parallel lenses.
Use whichever exist; state in one line which you used if it affects confidence.

## Query templates (replace `<YEAR>` with the real current year)
- Rubric: `"<hackathon>" judging criteria`, `"<hackathon>" rules AI generated code`
- Winners: `site:devpost.com "<theme>" winner`, `"<hackathon>" winners <YEAR> github`, `"<hackathon>" winning project architecture`
- Prior art: `site:github.com "<core noun>" "<core verb>" hackathon`, `<idea keywords> open source`, `<idea keywords> product hunt`, `site:huggingface.co/spaces <keywords>`
- Sponsor: `<sponsor> API free tier limits <YEAR>`, `<sponsor> quickstart`, `<sponsor> changelog`
- Trend: `<topic> hacker news`, `<topic> release notes <month> <YEAR>`
- Failure: `<library> issues rate limit`, `<tech> production problems`, `<tech> limitations`
Use 1-6 words; start broad, then narrow. Never repeat an identical query.

## Evidence grading
| Grade | Meaning |
|---|---|
| A | Primary/official source dated within 30 days, or verified by an executed test in this session |
| B | Reputable secondary source or official source older than 30 days |
| C | Blog/forum/video; single source |
| D | Model memory or unverified; **must be labeled** |
Rule: never base a GO/NO-GO or a cost decision on C/D alone. If sources conflict, show both and say which you trust and why.

## Freshness rules
- Tools, models, prices, free-tier limits, API terms: must be grade A/B and dated. These change monthly; several free-tier limits and terms changed during 2026.
- Concepts and architectures: older sources are fine.
- Always print the date you verified.

## Executable spikes (when a shell exists and the user has keys)
Smallest test that kills the biggest risk: auth works, endpoint reachable, latency p50/p95 over ~10 calls, rate-limit headers, structured-output validity rate, library installs cleanly. Report numbers. Never request or echo secrets; read keys from environment variables the user sets locally.

## Parallel fan-out
If subagents exist, launch one per lens with a one-line question and a fixed output schema:
`finding | source URL | date | grade | implication`
Then merge, resolve conflicts, and decide. Do not return raw dumps.

## Stop rule and output
Stop when each decision-critical claim is grade A/B, or when two more searches change nothing. Produce a **Research Brief** (`assets/templates/research-brief.md`): decision, evidence table, contradictions, unknowns, next verification.

## No-tools fallback
State: "No live research tools in this session." Mark claims `D`, give the exact searches/commands for the user to run (from the templates above), and keep the verdict provisional. Never present memory as verified fact.
