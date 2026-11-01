# 11 - Tool arsenal

How to use: pick by **capability**, verify current free tier (lens L7), prefer what the team knows, and keep vendors minimal. Names below are option classes to evaluate, not endorsements. Cost-first order within each row.

## Contents
- Research tools
- Build tools (coding agents)
- AI/LLM
- App stack
- Data and storage
- Integrations and automation
- Hardware
- Testing and observability
- Deployment
- Demo and docs

## Research tools
| Need | Tools |
|---|---|
| Event/rules | Official site, Devpost/Devfolio/Unstop/DoraHacks pages, organizer Discord/Slack |
| Past winners | Devpost galleries, project READMEs, winner blog posts |
| Prior art | GitHub search (`gh search`), Hugging Face Spaces, Product Hunt, app stores, arXiv, Google Scholar |
| Trends | Hacker News, relevant subreddits, GitHub trending, release notes |
| Limits/prices | Official pricing/limits pages, status pages, `scripts/cost_estimate.py` |
| Verification | Shell, Python, curl, API clients, browser automation |
Use host-native search/fetch/deep-research, MCP servers, and subagents when present.

## Build tools (coding agents/IDEs)
Terminal agents (e.g., Claude Code, Codex CLI, OpenCode, Gemini CLI class) | IDE agents (Cursor, Copilot, Windsurf class) | scaffolders. Select by: what is free for you now, what the team knows, whether it reads `AGENTS.md`/skills. Check student plans and free quotas today.

## AI / LLM
| Need | Option classes |
|---|---|
| Hosted LLM APIs | Vendor free tiers, aggregator gateways with free models, fast-inference providers, edge platforms |
| Open models local | Ollama/llama.cpp/LM Studio class on laptop; free notebook GPUs for bursts |
| Embeddings | Local open embedding models; hosted free embeddings |
| STT/TTS | Open STT models locally; hosted free tiers; browser Web Speech API |
| Vision | Hosted multimodal free tiers; open vision models; OCR libraries |
| Orchestration | Provider SDKs directly; light agent frameworks; workflow graph libraries. Pick the one you can debug. Avoid heavy frameworks unless they remove real work |
| Structured output | Schema validation libraries (Pydantic/Zod class) + provider JSON modes |
| Guardrails/evals | Simple custom evals first; open eval libraries if time |
Always use an OpenAI-compatible client abstraction where possible to enable fallback.

## App stack
| Layer | Options |
|---|---|
| Web | React meta-frameworks, Svelte/Vue equivalents, Python web frameworks; Tailwind + component kits |
| ML demo UI | Streamlit, Gradio class |
| Mobile | PWA, cross-platform frameworks |
| Backend | Node/TypeScript or Python (FastAPI class) monolith |
| Realtime | SSE, WebSocket, managed realtime services |
| Auth | Skip for demo path; if needed, managed auth free tier |

## Data and storage
SQLite/Postgres (hosted free tiers), pgvector or embedded vector stores, object storage free tiers, spreadsheet/CSV for seed data, open datasets (government, Kaggle, Hugging Face) with license check.

## Integrations and automation
Sponsor APIs, webhooks, workflow automation tools, email/SMS test modes, payment **test mode**, maps with open tiles, browser automation (Playwright class), MCP servers for tool access.

## Hardware
ESP32/Arduino/Raspberry Pi class boards, common sensors, BLE/serial/MQTT, mock-device simulators, spare cables, power banks.

## Testing and observability
Unit/integration test runners, record/replay libraries, load tools, tracing/logging (open LLM observability tools), error tracking free tiers, uptime pings.

## Deployment
See `08-distribution-and-submission.md`. Use container-based reproducibility (`docker compose`) for the run-anywhere path.

## Demo and docs
Screen recorders (OBS/built-in), diagram tools (Mermaid, Excalidraw), slide tools, README templates in `assets/templates/`.

## Selection rule
1. Team familiarity. 2. Free tier survives demo-day load. 3. Fewest vendors. 4. Fallback exists. 5. Terms allow the use. If two options tie, choose the one with better docs and recent releases.
