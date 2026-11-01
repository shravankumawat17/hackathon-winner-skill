# Install

Skill folder to install: `skills/hackathon-winner/` (the whole folder, including `references/`, `scripts/`, `assets/`). Folder name must stay `hackathon-winner`.

## 1. Skills CLI (many agents)
```bash
npx skills add <your-github-user>/hackathon-winner-skill
```

## 2. OpenCode
OpenCode discovers skills from `.opencode/skills/`, `.claude/skills/`, and `.agents/skills/` (project, walking up to the git root) and from `~/.config/opencode/skills/`, `~/.claude/skills/`, `~/.agents/skills/` (global).
```bash
git clone https://github.com/<you>/hackathon-winner-skill && cd hackathon-winner-skill
./install.sh --opencode            # project-level: .opencode/skills/hackathon-winner
./install.sh --opencode --global   # ~/.config/opencode/skills/hackathon-winner
```
Optionally copy `AGENTS.md` to your project root so the rules apply even when the skill is not auto-selected. Ask OpenCode to "use the hackathon-winner skill".

## 3. OpenAI Codex (CLI / app / IDE)
```bash
./install.sh --codex               # .agents/skills/hackathon-winner
./install.sh --codex --global      # ~/.agents/skills/hackathon-winner
```
Invoke with `$hackathon-winner` or `/skills`. Restart Codex if it does not appear. `AGENTS.md` is a fallback.

## 4. Claude Code / Claude
```bash
./install.sh --claude              # .claude/skills/hackathon-winner
./install.sh --claude --global     # ~/.claude/skills/hackathon-winner
```
Claude app/web: zip the skill folder (`hackathon-winner.zip`, the folder at the zip root) and upload it in Settings, Capabilities, Skills (where your plan allows).

## 5. Gemini CLI, Cursor, Copilot, Windsurf, others
Use the Skills CLI (1), or copy the skill folder to the tool's skills directory, or point the tool at `AGENTS.md`.

## 6. ChatGPT
Two options:
1. **Native skills** (rolling out on some plans; disabled by default on Enterprise/Edu until an admin enables it): create/import a skill and upload `dist/hackathon-winner.zip` (folder at the zip root). Select with `@hackathon-winner`.
2. **Project fallback** (works everywhere): create a Project, paste the FULL block from `CHATGPT_PASTE.md` into the Project instructions, and upload `skills/hackathon-winner/references/*.md` and `assets/templates/*.md` as Project files. Short block (<1,500 chars) is for Custom Instructions.
ChatGPT cannot run the bundled scripts unless Code Interpreter/Python is available; the instructions include an inline ledger fallback.

## Windows
Use `install.ps1` (PowerShell): `./install.ps1 -Opencode -Codex -Claude [-Global]`.

## Verify
```bash
python tools/validate_repo.py
```
In your agent, ask: "Use hackathon-winner: I have a 24h hackathon, should I build a chat-with-PDF app?" Expected: a first-line NO-GO with evidence-backed pivots, a diagram, and a research-gate note.
