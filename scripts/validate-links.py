#!/usr/bin/env python3
"""
AIX Wikilink Validator
======================
Validates all [[wikilinks]] across wiki/ directory.
Run as part of CI or agent workflow.

Usage:
    python scripts/validate-links.py
"""

import os
import re
import sys
from pathlib import Path

WIKI_DIR = Path(__file__).parent.parent / "wiki"
WIKILINK_RE = re.compile(r"\[\[([^\]|\\]+)(?:\|[^\]]+)?\]\]")

def get_all_slugs() -> set[str]:
    """Get all document slugs from wiki/ directory."""
    slugs = set()
    for fpath in WIKI_DIR.rglob("*.md"):
        rel = fpath.relative_to(WIKI_DIR).with_suffix("")
        slugs.add(str(rel))
    return slugs


def validate():
    slugs = get_all_slugs()
    errors = []

    for fpath in sorted(WIKI_DIR.rglob("*.md")):
        rel = fpath.relative_to(WIKI_DIR)
        content = fpath.read_text(encoding="utf-8")
        links = WIKILINK_RE.findall(content)

        for link in links:
            if link not in slugs:
                errors.append(f"  [{rel}] [[{link}]] → NOT FOUND")

    if errors:
        print(f"❌ {len(errors)} broken wikilink(s):")
        for err in errors:
            print(err)
        return False
    else:
        total_links = sum(len(WIKILINK_RE.findall(f.read_text(encoding="utf-8"))) for f in WIKI_DIR.rglob("*.md"))
        print(f"✅ All wikilinks valid ({len(slugs)} docs, {total_links} links)")
        return True


if __name__ == "__main__":
    success = validate()
    sys.exit(0 if success else 1)
