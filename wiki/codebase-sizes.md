---
title: "Codebase Sizes — Full Line Count"
last_updated: "2026-05-16"
status: "stable"
tags: [sizing, statistics, lines-of-code]
layer: "all"
related:
  - "[[full-code-map]]"
  - "[[stack-map]]"
---

# Codebase Sizes

> Last counted: 2026-05-16 (v3 — 7 sub-agents, one per repo)

## Total Files & Lines by Repo

| Repo | Layer | Files | Total Lines | % |
|------|-------|-------|-------------|---|
| iqra | L2 | 379 | **77,981** | 36.4% |
| GemClaw | L6 | 222 | **61,542** | 28.7% |
| axiomid-project | L0 | 187 | **27,765** | 13.0% |
| PiWorker-OS | L5 | 155 | **19,651** | 9.2% |
| aix-agent-skills | L3 | 199 | **14,576** | 6.8% |
| AlphaAxiom | L4 | 34 | **9,100** | 4.2% |
| aix-format | L1 | 20 | **3,585** | 1.7% |
| **Total** | | **1,196** | **214,200** | **100%** |

## Lines by Language (code only — excluding JSON + MD + YAML + CSS)

| Language | Lines | % |
|----------|-------|---|
| TypeScript (.ts) | 77,280 | 63.1% |
| TypeScript React (.tsx) | 12,574 | 10.3% |
| JavaScript (.js) | 13,820 | 11.3% |
| Python (.py) | 11,566 | 9.4% |
| Go (.go) | 8,915 | 7.3% |
| **Total (real code)** | **124,155** | **100%** |

## Real Code (after excluding locks + PNG binaries)

| Category | Lines |
|----------|-------|
| All files (wc -l) | 214,200 |
| − package-lock.json (6 files) | −59,656 |
| − PNG binaries counted as lines | −~18,000 |
| **Real code** | **~136,544** |
| − MD/YAML/CSS/JSON config | −~30,389 |
| **Actual code (TS/JS/Python/Go)** | **~124,155** |

## Package-lock.json Analysis (6 files)

| Repo | Lock Lines |
|------|-----------|
| GemClaw | 22,005 |
| IQRA | 15,412 |
| axiomid-project | 11,395 |
| GemClaw (functions/) | 7,451 |
| PiWorker-OS | 2,785 |
| aix-agent-skills | 608 |
| **Total** | **59,656** |

- 140 installs across 7 repos, 91 unique packages = 35% duplication
- `typescript` duplicated in 6 repos, `@types/node` in 5, `next`/`react` in 3
- pnpm monorepo would reduce 59,656 lines → ~10,000 lines

## Key Takeaways

- **TypeScript** = 63% of real code — dominant language (5 of 7 repos)
- **package-lock.json** = 59,656 lines (28% of total)
- **PNG noise** = ~18,000 lines counted
- **If monorepo**: ~116K total instead of 136K
