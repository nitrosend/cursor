#!/usr/bin/env python3
"""Validate the Cursor and Grok Build manifests and every skill before a release."""
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []


def require(ok, message):
    if not ok:
        errors.append(message)


cursor = json.loads((ROOT / ".cursor-plugin/plugin.json").read_text())
grok = json.loads((ROOT / ".grok-plugin/plugin.json").read_text())
require(cursor["name"] == grok["name"] == "nitrosend", "Plugin name must stay 'nitrosend'")
require(cursor["version"] == grok["version"], "Cursor and Grok versions differ")
require(re.fullmatch(r"\d+\.\d+\.\d+", cursor["version"]), "Version must be semver")
changelog = (ROOT / "CHANGELOG.md").read_text()
require(f"## {cursor['version']}" in changelog, "CHANGELOG has no entry for this version")
for manifest in (cursor, grok):
    require(0 < len(manifest["description"]) <= 700, "Description missing or over 700 characters")
    keywords = manifest.get("keywords", [])
    require(len(set(keywords)) == len(keywords), "Duplicate keywords")
require(all("nitrosend" in k for k in grok.get("keywords", [])),
        "Grok keywords must be brand-specific (xAI pushes back generic terms)")
for rel in (cursor["mcpServers"], grok["mcpServers"], cursor["logo"]):
    require((ROOT / rel).is_file(), f"Missing file: {rel}")
require(cursor.get("skills") == "./skills/", "Skills folder not declared")

banned = re.compile(r"\bSMS\b|TCPA|\bStripe\b|—")
skills = sorted((ROOT / "skills").glob("*/SKILL.md"))
require(skills, "No skills found")
for path in skills:
    folder = path.parent.name
    parts = path.read_text().split("---\n", 2)
    require(len(parts) == 3 and parts[0] == "" and parts[2].strip(), f"{folder}: bad frontmatter")
    if len(parts) != 3:
        continue
    front = parts[1]
    name = re.search(r"^name:\s*(.+)$", front, re.M)
    require(name and name.group(1).strip() == folder, f"{folder}: name must match folder")
    require(re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", folder) and len(folder) <= 64, f"{folder}: invalid name")
    desc = front.split("description:", 1)[1] if "description:" in front else ""
    desc = re.sub(r"\s+", " ", desc.replace(">", "", 1)).strip()
    require(0 < len(desc) <= 1024, f"{folder}: description missing or over 1024 characters")
    require(not banned.search(path.read_text()), f"{folder}: mentions SMS, TCPA, Stripe or an em dash")
    require(not re.search(r"\bClaude (Desktop|plugin|Cowork)\b|/nitrosend:", path.read_text()),
            f"{folder}: Claude-only wording")

if errors:
    print("\n".join(errors))
    sys.exit(1)
print(f"OK: {len(skills)} skills, version {cursor['version']}")
