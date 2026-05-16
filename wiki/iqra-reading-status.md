---
title: "IQRA Reading Status"
last_updated: "2026-05-16"
status: "stable"
tags: [iqra, reading-status, progress]
layer: "L2"
related:
  - "[[L2-iqra]]"
  - "[[iqra-core-security]]"
  - "[[iqra-evolution-llm]]"
---

# IQRA Reading Status

> 52,447 lines TS — Tracking what's been read.

## ✅ READ PERSONALLY (17,633 lines — 33.6%)

| Group | Folder | Lines | Status |
|-------|--------|-------|--------|
| **G1** | 01-core | 5,512 | ✅ Read — 7 Loops, MissionControl, brain |
| **G1** | 02-workers | 1,819 | ✅ Read — Worker protocol + 4 workers |
| **G4** | 06-security | 3,003 | ✅ Read — Damir, TrustChain, DID, filters |
| **G5** | 09-evolution | 2,674 | ✅ Read — SelfEvolve, MCTS, League, Tawbah |
| **G6** | 07-llm | 990 | ✅ Read — Ollama, Groq, Economy, Tools |
| **G6** | 08-cognitive | 1,492 | ✅ Read — Engine, Swarm, Skills, Analyzer |
| **G7** | 14-aix | 2,143 | ✅ Read — Manifest, Marketplace, DID, Types |

## 📖 READ VIA SUB-AGENT (8,751 lines — 16.7%)

| Group | Folder | Lines | Status |
|-------|--------|-------|--------|
| **G2** | 03-memory | 4,115 | 📖 Via sub-agent — MemoryBridge 5-layer |
| **G3** | 04-quran | 4,636 | 📖 Via sub-agent — Quran Engine |

## ❌ NOT YET READ (26,063 lines — 49.7%)

| Group | Folder | Lines | Key Files |
|-------|--------|-------|----------|
| **G0** | 00-manifest | 133 | DASTŪR, MĪTHĀQ, FITRAH docs |
| **Rewards** | 05-rewards | 743 | engine.ts, ledger.ts |
| **Topology** | 10-topology | 671 | topology.ts, codebase_mapper.ts |
| **Infra** | 12-infrastructure | 1,583 | logger, heartbeat, tools_registry |
| **Utils** | 13-utils | 2,548 | personas, timeouts, cipher, prompts |
| **Sim** | simulation | 254 | mcts_engine.ts |

## Recommendation

The remaining 26,063 lines are mostly:
- **13-utils** (2,548) — Personas + Utilities (lower value)
- **12-infrastructure** (1,583) — Logger + Tools Registry (worth reading)
- **10-topology** (671) — Topological analysis (specialized)
- **05-rewards** (743) — Reward engine (valuable)
- **00-manifest** (133) — Constitutional docs (valuable)
- **simulation** (254) — MCTS (valuable)

**Tip**: 13-utils and 12-infrastructure are lowest value — read only key files.
