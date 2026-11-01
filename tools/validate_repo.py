#!/usr/bin/env python3
"""Validate skill structure: frontmatter, naming, referenced files, script syntax."""
import os, re, sys, py_compile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS = os.path.join(ROOT, "skills")
errors, warnings = [], []

for name in sorted(os.listdir(SKILLS)):
    d = os.path.join(SKILLS, name)
    md = os.path.join(d, "SKILL.md")
    if not os.path.isdir(d):
        continue
    if not os.path.exists(md):
        errors.append(f"{name}: SKILL.md missing"); continue
    text = open(md, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        errors.append(f"{name}: no YAML frontmatter"); continue
    fm = m.group(1)
    nm = re.search(r"^name:\s*(.+)$", fm, re.M)
    desc = re.search(r"^description:\s*(.+)$", fm, re.M | re.S)
    if not nm or nm.group(1).strip() != name:
        errors.append(f"{name}: frontmatter name must equal directory name")
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name) or len(name) > 64:
        errors.append(f"{name}: invalid skill name")
    if not desc:
        errors.append(f"{name}: description missing")
    else:
        dl = len(desc.group(1).strip())
        if dl > 1024: errors.append(f"{name}: description {dl} chars > 1024")
        print(f"{name}: description {dl}/1024 chars")
    lines = text.count("\n") + 1
    print(f"{name}: SKILL.md {lines} lines")
    if lines > 500: warnings.append(f"{name}: SKILL.md over 500 lines")
    for ref in set(re.findall(r"`((?:references|scripts|assets)/[\w./-]+)`", text)):
        if not os.path.exists(os.path.join(d, ref)):
            errors.append(f"{name}: referenced file missing: {ref}")
    for ref in set(re.findall(r"`(\d\d-[\w-]+\.md)`", text)):
        if not os.path.exists(os.path.join(d, "references", ref)):
            errors.append(f"{name}: reference module missing: {ref}")
    for f in os.listdir(os.path.join(d, "scripts")) if os.path.isdir(os.path.join(d, "scripts")) else []:
        if f.endswith(".py"):
            try: py_compile.compile(os.path.join(d, "scripts", f), doraise=True)
            except py_compile.PyCompileError as e: errors.append(f"{name}/scripts/{f}: {e}")
    rd = os.path.join(d, "references")
    if os.path.isdir(rd):
        for f in os.listdir(rd):
            n = open(os.path.join(rd, f), encoding="utf-8").read().count("\n")
            if n > 300 and "Contents" not in open(os.path.join(rd, f), encoding="utf-8").read():
                warnings.append(f"references/{f}: >300 lines without a contents list")

for w in warnings: print("WARN:", w)
for e in errors: print("ERROR:", e)
print("OK" if not errors else f"{len(errors)} error(s)")
sys.exit(1 if errors else 0)
