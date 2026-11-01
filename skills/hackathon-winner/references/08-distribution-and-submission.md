# 08 - Distribution, deployment, and submission

Goal: judges can open it in 10 seconds, run it in one command, and understand it from the repo.

## Contents
- Deliver three ways
- Deployment matrix
- Repo hygiene
- README structure
- Submission platforms
- Preflight
- Post-event

## Deliver three ways (always)
1. **Live URL or installable artifact**, no login on the demo path.
2. **One-command local run** (`make demo` or `docker compose up`) with seed data.
3. **Recorded fallback** video of the golden path (screen recording, captions, 2-3 min or per rules).

## Deployment matrix (verify free-tier limits, cold starts, and ToS before choosing)
| Project type | Typical $0 option class | Notes |
|---|---|---|
| Static / SPA / SSR web | Edge/static hosts (Vercel, Netlify, Cloudflare Pages class) | Check commercial-use and bandwidth limits |
| API server | Container/PaaS hosts with free tiers (Render, Fly, Railway, Cloud Run class) | Free instances may sleep: warm before demo or use always-on trick allowed by ToS |
| ML demo | Hugging Face Spaces class | Quick public demo; hardware limits apply |
| Database | Hosted Postgres/SQLite-edge/serverless DB free tiers | Seed script, backups of demo data |
| Mobile | PWA link; APK/TestFlight/Expo Go for native | App-store review will not fit; ship direct artifacts |
| Browser extension | Unpacked ZIP + install steps + video | Store review takes days |
| CLI / library | npm/PyPI/GitHub release; `uvx`/`npx` one-liner | Include sample project |
| MCP server | Published package + config snippet | Include client config example |
| Hardware | Photos, schematic, wiring diagram, video | Bring the device; backup power and cables |
| Smart contract | Testnet deployment + verified source + explorer link | |

## Repo hygiene
LICENSE | README | `.env.example` | no secrets in history | `.gitignore` | architecture diagram in README | run instructions that work on a clean machine (test them) | tests/smoke | releases/tags | meaningful commit history | credits for third-party code and data. Run `python scripts/submission_check.py <repo>`.

## README structure
`assets/templates/submission-readme.md`: one-line pitch | demo link and video | problem (2 lines) | solution | architecture diagram | tech stack with why | what is real vs mocked | how to run (3 commands) | evaluation results | limitations | team and credits | license.

## Submission platforms
Devpost, Devfolio, Unstop, DoraHacks, MLH-style forms differ per event. Typical fields: title, tagline, description, built-with, links (repo, demo, video), images, team, prize tracks. **Verify the exact fields and deadlines on the event page.** Submit early, then edit; late edits are often allowed until the deadline. Check each sponsor prize has its own checkbox/field.

## Preflight (T-60 min)
Template: `assets/templates/preflight-checklist.md`. Includes: deploy from clean checkout, smoke test on mobile data, keys and quotas verified, caches warmed, demo mode toggle tested, video uploaded and playable logged out, repo public, links open in a private window.

## Post-event
Tag release, add results, write a short technical post-mortem. Distribution beyond the event (package registries, community posts) is optional; keep the repo healthy.
