---
title: "AIX Knowledge Base — Dashboard"
last_updated: "2026-05-16"
status: "stable"
tags: [index, dashboard, overview, graph]
layer: "all"
related:
  - "[[stack-overview]]"
  - "[[roadmap]]"
  - "[[changelog]]"
  - "[[decisions]]"
  - "[[architecture]]"
---

# 🧬 AIX Sovereign Stack — Knowledge Graph

> Codename: Echo369 | Spec: AIX/1.0 | v0.369.0

## Stack Overview

| Layer | Repo | Role | Status | Lines |
|-------|------|------|--------|-------|
| **L0** | [[L0-axiomid]] | Identity & XP | ✅ Stable | ~2,759 TS |
| **L1** | [[L1-aix-format]] | Protocol & DNA | ✅ Stable | ~643 TS |
| **L2** | [[L2-iqra]] | Runtime & Memory | ✅ Stable | ~50,288 TS |
| **L3** | [[L3-aix-agent-skills]] | Marketplace | ✅ Stable | ~2,618 TS |
| **L4** | [[L4-alphaaxiom]] | Trading | ✅ Stable | ~8,923 PY |
| **L5** | [[L5-piworker-os]] | Pi Treasury | ✅ Stable | ~5,448 TS / 8,915 Go |
| **L6** | [[L6-gemclaw]] | Voice | ✅ Stable | ~24,531 TS |

**Total**: ~136,544 lines real code | 1,196 files | [[codebase-sizes|Full breakdown]]

## Latest Updates

- **IQRA Deep Cleanup**: All 7 major items completed (qdrant.ts → reflection-store.ts, syntax fix, constants unification, etc.)
- **GemClaw Cleanup**: Backup files removed, dead memory subsystem removed, dead Firestore imports removed
- **PiWorker-OS Cleanup**: plugins/ directory deleted, package.json fixed
- **KDB Restructure**: Wikigraph format implemented with YAML frontmatter + `wikilinks` + Quartz static site
- **AIX-0 Compression Plan**: 31 KDB files → single AIX-0.md reference + archive/ folder

## In Progress

- **AIX-0 Master Reference**: Creating unified reference document from all 31 KDB files
- **axiomid.app Pages**: /memory, /marketplace, /soul, /voice, /dashboard being built
- **Pi Developer Portal**: Domain claim pending user action

## Knowledge Graph Structure

```mermaid
graph LR
  L0[axiomid-project L0] --> L1[aix-format L1]
  L1 --> L2[iqra L2]
  L2 --> L3[aix-agent-skills L3]
  L3 --> L4[AlphaAxiom L4]
  L3 --> L5[PiWorker-OS L5]
  L3 --> L6[GemClaw L6]
  L4 --> L5
  L6 --> L2

  Style L0 fill:#00ff41,color:#000
  Style L1 fill:#00d4ff,color:#000
  Style L2 fill:#ff6b35,color:#000
  Style L3 fill:#ff00ff,color:#000
  Style L4 fill:#ffd700,color:#000
  Style L5 fill:#ff4444,color:#000
  Style L6 fill:#44ff44,color:#000
```

## Quick Navigation

| Category | Documents |
|----------|-----------|
| **Architecture** | [[stack-overview]], [[architecture]], [[human-body-architecture]], [[cross-system-flows]], [[stack-map]], [[decisions]] |
| **Roadmap** | [[roadmap]], [[changelog]], [[implementation-roadmap]], [[execution-plan-10h]] |
| **IQRA (L2)** | [[L2-iqra]], [[iqra-core-security]], [[iqra-evolution-llm]], [[iqra-reading-status]], [[memory-systems-comparison]] |
| **Plans & Cleanup** | [[cleanup-plan]], [[clean-room-skills]], [[brain-build-plan]], [[x402-plan]] |
| **Sessions** | [[sessions/session-2026-05-14]], [[sessions/session-2026-05-15]], [[sessions/session-2026-05-16]] |
| **Pi Network** | [[pi-network]] |
| **Sizing** | [[codebase-sizes]], [[full-code-map]], [[full-skills-map]] |
