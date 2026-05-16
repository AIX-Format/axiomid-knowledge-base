# AIX Wiki — Agent Instructions

> تعليمات لكل AI Agent للتعامل مع قاعدة المعرفة.

## Core Rules

1. **Every edit to a wiki file MUST update `last_updated`** in the YAML frontmatter
2. **Add [[wikilinks]]** to related documents when mentioning them
3. **Add relevant `tags`** and `repos` to frontmatter
4. **Keep status accurate**: `stable` | `in-progress` | `deprecated` | `draft`
5. **Never delete content** — mark as `deprecated` instead

## Workflow for Agent Edits

```
When modifying wiki/ files:
  1. Update `last_updated` to today's date
  2. Add [[wikilinks]] to related docs in body text
  3. Keep frontmatter `related` list current
  4. Run: python scripts/update-wiki.py --check
  5. If links valid: commit + push
```

## File Structure

```
wiki/
├── index.md              ← Dashboard — DO NOT edit manually (auto-generated stats)
├── *.md                  ← Core documents with YAML frontmatter
└── sessions/             ← Session logs
```

## Frontmatter Template

```yaml
---
title: "Document Title"
last_updated: "2026-05-16"
status: "stable"         # stable | in-progress | deprecated
tags: [tag1, tag2]
layer: "Lx"              # L0-L6 or "all"
repos: ["repo-name"]     # optional
related:
  - "[[related-doc]]"
---
```

## Wikilink Format

- Use `[[page-slug]]` to link to other documents
- Use `[[page-slug|Display Text]]` for custom display text
- Slugs are relative to wiki/: `L2-iqra` → `wiki/L2-iqra.md`
- Session links: `[[sessions/session-2026-05-16]]`

## When Creating a New Page

1. Copy `schemas/template.md`
2. Fill in all frontmatter fields
3. Add `[[wikilinks]]` from existing docs to this new page
4. Add this page to `wiki/index.md` quick navigation
5. Run `python scripts/update-wiki.py` to regenerate graph.json

## Validation

```bash
# Check all wikilinks resolve
python scripts/validate-links.py

# Regenerate graph.json + validate
python scripts/update-wiki.py
```
