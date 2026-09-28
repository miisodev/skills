"""Release checks for this repository's skills.

- every skills/<name>/SKILL.md has valid frontmatter (name matches folder, description <= 1024 chars)
- every relative file path mentioned in a SKILL.md exists
- production: every check ID referenced across references resolves, and the scoring
  script runs cleanly on the example payload
"""
import re
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
ALLOWED = {"name", "description", "license", "allowed-tools", "metadata", "compatibility"}
errors = []

skills = sorted(p.parent for p in (ROOT / "skills").glob("*/SKILL.md"))
if not skills:
    errors.append("no skills found under skills/")

for skill in skills:
    text = (skill / "SKILL.md").read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        errors.append(f"{skill.name}: missing frontmatter")
        continue
    fm = yaml.safe_load(m.group(1))
    if set(fm) - ALLOWED:
        errors.append(f"{skill.name}: unexpected frontmatter keys {sorted(set(fm) - ALLOWED)}")
    if fm.get("name") != skill.name:
        errors.append(f"{skill.name}: name {fm.get('name')!r} does not match folder")
    if not re.fullmatch(r"[a-z0-9-]{1,64}", str(fm.get("name", ""))):
        errors.append(f"{skill.name}: name must be lowercase letters, digits and hyphens")
    desc = fm.get("description", "")
    if not desc or len(desc) > 1024:
        errors.append(f"{skill.name}: description missing or over 1024 characters ({len(desc)})")
    for ref in sorted(set(re.findall(r"`((?:references|assets|scripts)/[\w./-]+\.\w+)`", text))):
        if not (skill / ref).exists():
            errors.append(f"{skill.name}: SKILL.md references missing file {ref}")

prod = ROOT / "skills" / "production"
if prod.exists():
    defined, refs = set(), set()
    for f in (prod / "references").glob("*-audit.md"):
        s = f.read_text(encoding="utf-8")
        defined |= set(re.findall(r"^\| ([A-Z0-9]+-\d\d) \|", s, re.M))
        refs |= set(re.findall(r"\b([A-Z][A-Z0-9]{1,3}-\d\d)\b", s))
    missing = sorted(refs - defined)
    if missing:
        errors.append(f"production: unresolved check references {missing}")
    with tempfile.TemporaryDirectory() as tmp:
        r = subprocess.run([sys.executable, str(prod / "scripts" / "readiness.py"),
                            str(prod / "assets" / "example-payload.json"),
                            "--md", str(Path(tmp) / "r.md"), "--json", str(Path(tmp) / "r.json")],
                           capture_output=True, text=True)
        if r.returncode != 0:
            errors.append(f"production: readiness.py failed on the example payload: {r.stderr.strip()}")
    print(f"production: {len(defined)} checks, references resolved")

for e in errors:
    print(f"error: {e}")
print(f"{len(skills)} skills checked, {len(errors)} errors")
sys.exit(1 if errors else 0)
