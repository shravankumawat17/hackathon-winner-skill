# 13 - Anti-repetition and freshness

Goal: every response adds something the user has not seen in this project/session. Repetition is a defect.

## Contents
- Ledger
- Protocol
- Lens rotation
- Delta answers
- Banned defaults
- Inline ledger fallback
- Script

## Ledger
A list of everything already given: ideas, tools, architectures, angles, diagrams, claims, research lenses. Stored in `.hackathon/ledger.jsonl` (shell available) or carried inline (no shell).

## Protocol (every substantive turn)
1. **Before answering**: read the ledger; list what you are about to suggest; run `python scripts/ledger.py check --text "<summary>"` for each new suggestion. `REPEAT` means do not present it as new; `SIMILAR` means state the difference.
2. **While answering**: include >=1 element not in the ledger (new evidence, new angle, new tool, deeper layer, new failure mode, new metric).
3. **After answering**: `python scripts/ledger.py add --kind <idea|tool|angle|diagram|claim|lens> --key <slug> --text "<one-line summary>"`.

## Lens rotation
Run `python scripts/ledger.py lenses` to see which research lens (L1-L10) was used least recently. Prefer that lens for the next research pass unless the question demands another.

## Delta answers
If the user asks the same or a near-identical question again: do not restate. Output `Delta since last answer:` then (a) what changed in the evidence, (b) the next layer of detail, (c) an alternative not previously proposed. If nothing new exists, say so in one line and offer a specific test (spike, benchmark, new search) that could produce new information.

## Banned defaults
Do not propose any of the saturated ideas in `03-idea-court.md` unless a wedge is stated. Do not reuse the same example projects, same stack combo, or same architecture diagram twice; vary archetype, modality, and constraint. Do not open with generic advice ("scope small", "practice your pitch") unless it is converted into a specific, checkable action for this project.

## Re-evaluation exception
You may revisit an earlier item only with new evidence. Mark it: `Re-evaluated: <item>. New evidence: <source/date>.`

## Inline ledger fallback (no shell)
End each reply with one compact line: `Ledger: ideas[a,b] tools[x,y] lenses[L3,L7] diagrams[arch,gantt]`. Before replying, read your previous Ledger lines. The user can ask `show ledger` to display it.

## Script
`scripts/ledger.py`: `add`, `check`, `list`, `lenses`, `reset`. File location from `HACKATHON_LEDGER` or default `.hackathon/ledger.jsonl`. Add `.hackathon/` to `.gitignore`.
