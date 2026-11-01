#!/usr/bin/env python3
"""Pre-submission repo audit: hygiene, reproducibility, and accidental secret exposure.

  submission_check.py [path] [--json]

Checks (PASS/WARN/FAIL): README sections, LICENSE, .gitignore, .env.example, secrets patterns,
tracked .env files, demo/video links, architecture diagram, run instructions, tests/smoke,
large files. Output never prints secret values, only file and line.
"""
import argparse, json, os, re, sys

SKIP_DIRS = {".git", "node_modules", ".venv", "venv", "__pycache__", "dist", "build", ".next", ".hackathon"}
SECRET_PATTERNS = {
    "generic API key assignment": re.compile(r"""(?i)\b(api[_-]?key|secret|token|passwd|password)\b\s*[:=]\s*['"][A-Za-z0-9_\-/+=]{16,}['"]"""),
    "OpenAI-style key": re.compile(r"\bsk-[A-Za-z0-9_\-]{20,}\b"),
    "Google API key": re.compile(r"\bAIza[0-9A-Za-z_\-]{35}\b"),
    "GitHub token": re.compile(r"\b(ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9]{30,}\b"),
    "AWS access key id": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "Private key block": re.compile(r"-----BEGIN (RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "Slack token": re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{10,}\b"),
}
TEXT_EXT = {".py", ".js", ".ts", ".tsx", ".jsx", ".json", ".yml", ".yaml", ".toml", ".env", ".md", ".txt", ".sh", ".html", ".css", ".ini", ".cfg", ".ipynb", ""}


def walk(root):
    for dp, dn, fn in os.walk(root):
        dn[:] = [d for d in dn if d not in SKIP_DIRS]
        for f in fn:
            yield os.path.join(dp, f)


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("path", nargs="?", default=".")
    p.add_argument("--json", action="store_true")
    a = p.parse_args()
    root = os.path.abspath(a.path)
    files = list(walk(root))
    rel = lambda f: os.path.relpath(f, root)
    names = {os.path.basename(f).lower() for f in files}
    res = []
    add = lambda status, check, detail="": res.append({"status": status, "check": check, "detail": detail})

    readme = next((f for f in files if os.path.basename(f).lower() in ("readme.md", "readme.rst", "readme.txt")), None)
    rtext = ""
    if readme:
        rtext = open(readme, encoding="utf-8", errors="ignore").read()
        add("PASS", "README present", rel(readme))
        low = rtext.lower()
        for label, keys in {"run instructions": ("how to run", "getting started", "quickstart", "installation", "usage", "run locally"),
                            "architecture section/diagram": ("architecture", "```mermaid", "system design"),
                            "tech stack": ("tech stack", "built with", "stack"),
                            "limitations/mocks disclosure": ("limitation", "mock", "known issues", "real vs"),
                            "evaluation/results": ("evaluation", "results", "benchmark", "accuracy", "latency")}.items():
            add("PASS" if any(k in low for k in keys) else "WARN", f"README: {label}")
        add("PASS" if re.search(r"https?://\S*(youtu|vimeo|loom|drive\.google|\.mp4)", rtext, re.I) else "WARN", "README: demo video link")
        add("PASS" if re.search(r"(?i)(live demo|demo:|deployed|https?://[^ )]+\.(app|dev|io|vercel|netlify|onrender|fly|hf)\b)", rtext) else "WARN", "README: live demo/URL")
    else:
        add("FAIL", "README present")

    add("PASS" if any(n.startswith("license") or n.startswith("copying") for n in names) else "WARN", "LICENSE present")
    add("PASS" if ".gitignore" in names else "FAIL", ".gitignore present")
    add("PASS" if any(n in names for n in (".env.example", "env.example", ".env.sample")) else "WARN", ".env.example present")
    add("PASS" if any(n in names for n in ("makefile", "docker-compose.yml", "docker-compose.yaml", "compose.yaml", "dockerfile", "package.json", "pyproject.toml", "requirements.txt")) else "WARN", "dependency/run manifest")
    tests = any(("test" in rel(f).lower() or "smoke" in rel(f).lower()) for f in files)
    add("PASS" if tests else "WARN", "tests or smoke script present")

    tracked_env = [rel(f) for f in files if os.path.basename(f).lower() in (".env", ".env.local", ".env.production")]
    add("FAIL" if tracked_env else "PASS", "no .env files in tree", ", ".join(tracked_env))

    leaks = []
    big = []
    for f in files:
        try:
            if os.path.getsize(f) > 25 * 1024 * 1024:
                big.append(rel(f))
            ext = os.path.splitext(f)[1].lower()
            if ext not in TEXT_EXT or os.path.getsize(f) > 2 * 1024 * 1024:
                continue
            with open(f, encoding="utf-8", errors="ignore") as fh:
                for n, line in enumerate(fh, 1):
                    for label, rx in SECRET_PATTERNS.items():
                        if rx.search(line) and "example" not in os.path.basename(f).lower():
                            leaks.append(f"{rel(f)}:{n} ({label})")
        except OSError:
            continue
    add("FAIL" if leaks else "PASS", "no secret-like strings", "; ".join(leaks[:15]) + (" ... rotate any real key and purge git history" if leaks else ""))
    add("WARN" if big else "PASS", "no files >25MB", ", ".join(big))

    order = {"FAIL": 0, "WARN": 1, "PASS": 2}
    res.sort(key=lambda r: order[r["status"]])
    if a.json:
        print(json.dumps(res, indent=2))
    else:
        for r in res:
            print(f"[{r['status']}] {r['check']}" + (f"  -> {r['detail']}" if r["detail"] else ""))
        c = {s: sum(1 for r in res if r["status"] == s) for s in order}
        print(f"\nSummary: {c['FAIL']} FAIL, {c['WARN']} WARN, {c['PASS']} PASS")
    sys.exit(1 if any(r["status"] == "FAIL" for r in res) else 0)


if __name__ == "__main__":
    main()
