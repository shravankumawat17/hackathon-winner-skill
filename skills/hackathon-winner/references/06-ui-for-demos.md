# 06 - UI and UX implementation for demos

Goal: a UI that makes the technical core legible in under 30 seconds. Technical implementation guidance only.

## Contents
- Principles
- Screen budget
- Component and framework choices
- Showing the technical work
- States that break demos
- Accessibility and responsiveness
- Tools
- Checklist

## Principles
1. **One flow, three screens max**: input, processing/result, detail. No settings, onboarding, or admin.
2. **First 30 seconds**: the judge sees the core result without signing up or configuring anything. Pre-load a demo account and seed data.
3. **Streaming feedback**: show progress and partial output; never a blank spinner longer than ~2 seconds.
4. **Make the AI/engineering visible**: citations, tool-call timeline, confidence, before/after, metrics.
5. **Consistency over novelty**: one component library, one spacing scale, one accent color, one icon set.

## Screen budget
| Screen | Must contain |
|---|---|
| Entry / input | Prefilled example, one primary action |
| Result / live | Streaming output, trace/citations, key metric |
| Detail / proof | Eval numbers, architecture mini-diagram, data source |

## Component and framework choices (verify current versions and limits)
| Situation | Pick | Why |
|---|---|---|
| Team knows React | React-based meta-framework + Tailwind + a copy-paste component kit | Fast, polished defaults, easy deploy |
| ML/data demo, UI lightly scored | Streamlit or Gradio class tools | UI in hours, built-in widgets |
| Mobile feel required | PWA with responsive layout; cross-platform native only if a device API is core | One codebase, instant link |
| Dashboard | Chart library already in your stack; avoid custom charting | Time |
| Maps | Open map tiles and library; check usage terms | $0 |
| Real-time | SSE/WebSocket with optimistic UI | Perceived speed |
Pick what the team already knows; do not learn a new UI stack during the event.

## Showing the technical work
- **Trace drawer**: steps, tool calls, latency per step, tokens, cost.
- **Citations**: sentence-level links to sources for retrieval systems.
- **Eval card**: baseline vs system, n, metric.
- **Architecture mini-diagram** on an "About/How it works" panel (Mermaid-rendered or static image).
- **Replay controls** for pre-recorded runs, clearly labeled as replay.

## States that break demos
Empty state (seed data) | loading | error with retry | rate-limit message with graceful fallback | offline | long text overflow | mobile viewport | slow network. Build and test each once.

## Accessibility and responsiveness (cheap, verifiable points)
Contrast ratio >= 4.5:1 for body text | keyboard focus visible | labels on inputs | semantic headings | alt text | responsive down to ~375px | prefers-color-scheme support if the kit provides it.

## Tools (verify free limits)
Design: free education plan of a design tool, or skip design and use a component kit. UI generators (v0/Lovable/Bolt-class) can scaffold screens fast: use for first drafts, then own the code. Screenshots/recording: built-in OS recorder or OBS. Icons: an open icon set.

## Checklist
- [ ] Demo account/seed data loaded
- [ ] Core result visible in <30 s from page load
- [ ] No auth wall on the demo path
- [ ] Trace/citations/metrics visible
- [ ] Empty/error/rate-limit states handled
- [ ] Works at 375px and 1440px
- [ ] Contrast and focus checked
- [ ] Production build deployed and tested from a different network
