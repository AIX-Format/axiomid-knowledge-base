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

## ⚠️ CRITICAL ARCHITECTURE RULES (DO NOT VIOLATE)

### Core Architecture
1. **KDB is NOT connected to axiomid-project code.** They are separate Vercel deployments. KDB is ONLY a wiki for agents/team.
2. **Do NOT modify axiomid-project files from KDB directory** and vice versa. Each has its own git repo.

### Pi SDK v2 Rules (axiomid-project)
3. **Pi SDK v2 has NO `Pi.init()` method.** Do NOT add `Pi.init()` calls. The SDK auto-initializes via CDN script tag with `data-sandbox` attribute.
4. **Auth format**: `Pi.authenticate({ scope: [...], onIncompletePaymentFound: fn })` — NOT the v1 array format `Pi.authenticate([scopes], callback)`.
5. **Auth endpoint**: `/api/auth/pi` for Pi SDK auth, `/api/auth/connect` for demo wallets. Do NOT switch them.
6. **Do NOT delete `/api/auth/pi/route.ts`** — it's the primary Pi auth endpoint.

### KDB Rules
7. **`.gitignore`**: Use `/content` not `content` — otherwise Quartz finds 0 files on Vercel.
8. **Frontmatter**: `last_updated`, `tags`, `related` must be accurate.

### aix-format Integration
9. **Copy-local** for Pi KYC/identity code — do NOT use npm link, monorepo, or git submodule.
10. **One-way dependency**: L0 (axiomid) → L1 (aix-format) → L2 (iqra). Never reverse.

### Git Rules
11. **Never force-push main branch** without explicit confirmation.
12. **Always check `git status`** before committing — stage only intended files.

## Validation

```bash
# Check all wikilinks resolve
python scripts/validate-links.py

# Regenerate graph.json + validate
python scripts/update-wiki.py
```
