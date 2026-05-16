---
title: "AIX Sovereign Stack — Changelog"
last_updated: "2026-05-16"
status: "stable"
tags: [changelog, updates, history]
layer: "all"
related:
  - "[[roadmap]]"
  - "[[decisions]]"
  - "[[sessions/session-2026-05-16]]"
---

# AIX Sovereign Stack — Changelog

## Session 4: 2026-05-16

### IQRA Deep Cleanup (7 items)
- `tsconfig.json.backup` deleted, 4 empty dirs + 3 `__pycache__` removed
- `qdrant.ts` → `reflection-store.ts` (rename + function rename)
- Updated 3 importers: `security.ts`, `damir_kernel.ts`, `discovery_loop.ts`
- `pattern_memory.ts`: syntax error fixed (extra `}`)
- `sovereign_identity.ts:61`: removed `${deepMemories}` (undefined variable)
- `memory_governor.ts`: added missing `WARM_LIMIT = 100`
- `05-rewards/`: constants unified (engine.ts imports from types.ts)

### Codebase Analysis
- Accurate sizing via 7 sub-agents: 214,200 lines total, ~136,544 real code
- Package-lock analysis: 6 locks = 59,656 lines (28%), 35% dep duplication
- TypeScript = 63% of real code (77,280 lines)
- Rust/napi-rs research: deferred for now

### PR Updates
- IQRA #110: pushed 7 fixes, commented re-review
- GemClaw #43: removed `lib/memory/` (6 files) + `cognitive-worker.ts`

### KDB Updates
- CODEBASE-SIZES.md v3 with real-code numbers
- SESSION-2026-05-16.md with 3rd and 4th sessions
- KDB restructured into wikigraph format with YAML frontmatter + `wikilinks`
- Quartz static site configured for GitHub Pages

---

## Session 3: 2026-05-15

### Cleanup Across Repos
- **IQRA**: 7 MemoryClient API routes added, LanceDBPlugin leftovers fixed
- **GemClaw**: 33 backup files deleted (~6,900 lines), 3 unused deps removed, 2 dead Firebase imports removed, typo fixed
- **PiWorker-OS**: plugins/ deleted (11 dirs, 38 files, ~865 lines), package.json fixed
- **aix-agent-skills**: 76→124 skills, 8 STUB files fixed, 38 THIN files filled

### Architecture Decisions
- AIX-0 compression plan designed: 31 KDB files → single AIX-0.md + archives
- Cross-system flows documented
- Memory systems comparison completed

---

## Session 2: 2026-05-14 (Evening)

### PR Merged
- **aix-format PR #207**: All @axiom/* packages at v0.1.0, merged

### axiomid.app Deployed
- Deployed on Vercel (axiom-id team, Node 22.x)
- validation-key.txt working
- Domain reassigned: axiomid.app ✅

---

## Session 1: 2026-05-14

### Initial Setup
- axiomid-project created
- Architecture designed (7 repos, 7 layers)
- Cross-system flows mapped
