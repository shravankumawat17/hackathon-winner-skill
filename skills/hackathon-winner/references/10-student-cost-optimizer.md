# 10 - Student cost optimizer

Goal: **zero-to-low cost with no loss in golden-path quality.** Cost cutting never degrades the demo; if it would, say so and price the minimal upgrade.

## Contents
- Cost ladder
- Rules
- AI cost levers
- Free-tier snapshot (dated, verify)
- Demo-day capacity planning
- Student and sponsor credits
- Downgrade vs upgrade decision
- Script

## Cost ladder
| Level | Meaning | Use when |
|---|---|---|
| L0 | Free tier, no card | Default |
| L1 | Student/sponsor/event credits | L0 fails a requirement |
| L2 | Under about $10 total, one-time | A single measurable quality or reliability gain |
| L3 | Anything more | Only with an explicit user decision |
Always present L0 first. Escalate only with a measured reason.

## Rules
1. Verify every limit and price on the **official page today** (lens L7). Free tiers changed repeatedly in 2026: models moved to paid tiers, limits were reduced or stopped being published, terms changed for some regions.
2. Limits are often per **organization/project**, not per key; extra accounts do not multiply capacity and may violate terms.
3. Read terms: some free tiers log or train on prompts, restrict end-user serving in some regions, or prohibit reselling/building a competing service. Never put real personal data through a free tier that logs prompts.
4. Treat published limits as ceilings; confirm real behavior with a real call and check response headers.
5. Build a **fallback chain**, not a single point of failure.
6. Cache everything deterministic. Most demo traffic is repeated.

## AI cost levers
- Route: small/fast model for classification, extraction, routing; stronger model only for the final reasoning step.
- Cache responses and embeddings; dedupe identical prompts.
- Trim context: retrieve top-k, summarize history, avoid resending large documents.
- Structured outputs reduce retries.
- Local/open models on a laptop GPU or free notebook GPUs for embeddings, STT, small LLMs (check quotas; they change).
- Embeddings: a local open model removes per-call cost; vector search in the app DB or an embedded store.
- Batch non-interactive work before the demo; precompute.
- Use event/sponsor-provided credits for the heavy path; ask organizers on day one.

## Free-tier snapshot
Source file: `assets/data/free_tiers.json` (dated, sourced, with confidence). **A snapshot is a lead, not a fact.** Re-verify before use; the data file carries `verified` dates and the cost script warns when stale (older than 30 days).
As of the snapshot date (2026-11-01), multi-source reports indicated:
- Gateway/aggregator free model slices exist with tight request caps that rise only after a small prepaid balance; per-account governance; some free providers may log prompts; terms may prohibit resale.
- Fast-inference providers offer per-model free rate limits (requests/min, requests/day, tokens/min, tokens/day), counted per organization.
- Large-vendor free tiers: flagship models are generally paid; lighter models free; some no longer publish per-model numbers (check the console); some features (e.g., search grounding) need billing; some regions require paid services for end-user serving.
- Edge platforms offer daily free inference quotas (units differ by provider).
- Some previously free programs closed to new users in 2026.
Conclusion: plan for **two independent providers plus a cache**, not one.

## Demo-day capacity planning
Burst model: `users x requests_per_user / window_minutes` = RPM needed. Compare to the lowest limit in your chain. If RPM or RPD is exceeded: cache hits, smaller model, queue with visible progress, replay mode. Run `scripts/cost_estimate.py --burst-users 30 --reqs-per-user 6 --window-min 10 --provider groq`.

## Student and sponsor credits (research current offers; programs change)
GitHub's student developer pack | cloud student credits (major clouds) | hackathon sponsor credits (ask organizers) | MLH partner perks | education plans of design/dev tools | free notebook GPU quotas. Always verify eligibility, region, expiry, and whether a card is required.

## Downgrade vs upgrade decision
Downgrade (cheaper) only if the golden-path metric does not drop measurably. Test it: run the golden set on both. Upgrade (paid) only if the free option fails the metric or reliability; give the exact $ and what it buys, one option, no list.

## Script
`python scripts/cost_estimate.py --help` estimates spend, free-tier headroom, and burst feasibility.
