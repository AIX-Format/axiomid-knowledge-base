---
title: "Architectural Decisions (ADRs)"
last_updated: "2026-05-16"
status: "stable"
tags: [decisions, architecture, adr]
layer: "all"
related:
  - "[[architecture]]"
  - "[[roadmap]]"
  - "[[changelog]]"
  - "[[x402-plan]]"
  - "[[brain-build-plan]]"
---

# Architectural Decisions (ADRs)

## ADR-0001: TypeScript is the Strategic Language

**Status**: Accepted ✅  
**Date**: 2026-05-16

**Context**: 63% of real code (77,280 lines) is TypeScript, 5 of 7 repos already in TS.

**Decision**: TypeScript is the strategic language. Keep Go in PiWorker-OS (8,915 lines — rewrite has no benefit). Keep Python in AlphaAxiom (8,923 lines — isolated trading/bioinf service). Rust via napi-rs reserved for future hot-path optimization.

---

## ADR-0002: Skills Live ONLY in L3

**Status**: Accepted ✅  
**Date**: 2026-05-15

**Context**: Skills were scattered across IQRA, PiWorker-OS, and GemClaw.

**Decision**: `aix-agent-skills` (L3) is the single source of truth for all skills. IQRA retains skill loader (reads from L3, never executes). Clean Room plan moves 7 IQRA utilities to L3.

---

## ADR-0003: Memory Lives ONLY in IQRA (L2)

**Status**: Accepted ✅  
**Date**: 2026-05-15

**Context**: PiWorker-OS had neural-memory.ts, GemClaw had memory-store.ts.

**Decision**: IQRA is the single memory system. Other repos call IQRA's REST API (MemoryClient). No direct npm imports from IQRA.

---

## ADR-0004: axiomid.app is the One App

**Status**: Accepted ✅  
**Date**: 2026-05-14

**Context**: 7 repos, each could have its own UI.

**Decision**: axiomid.app is the single frontend. Marketplace, Memory, Soul, Voice, Dashboard are all pages inside it. Each repo deploys independently on Vercel but axiomid.app is the unified interface.

---

## ADR-0005: Monorepo Deferred

**Status**: Accepted ✅  
**Date**: 2026-05-16

**Context**: 6 package-lock.json files = 59,656 lines (28% of total), 35% dep duplication.

**Decision**: Defer pnpm monorepo until development velocity demands it. Keep independent repos for now. pnpm would reduce 6 locks → 1 lock (~10K lines).

---

## ADR-0006: x402 is the Unified Payment Protocol

**Status**: Accepted ✅  
**Date**: 2026-05-15

**Context**: PiWorker-OS has its own payment system (EscrowManager, SorobanBridge).

**Decision**: L3 x402 gateway is the standard. PiWorker-OS escrow (Pi coins) stays unique. PiWorker-OS Go x402 → removed in favor of L3 gateway. See [[x402-plan]].

---

## ADR-0007: DID Unification → did:axiom

**Status**: Proposed 📝  
**Date**: 2026-05-15

**Context**: IQRA uses `did:web`, PiWorker-OS uses `did:piworker:`.

**Decision**: All DIDs → `did:axiom:axiomid.app:*`. IQRA and PiWorker-OS need migration.

---

## ADR-0008: AIX-0 Master Reference

**Status**: In Progress 🔄  
**Date**: 2026-05-16

**Context**: 31 KDB files (3,556 lines) with overlapping content.

**Decision**: Create single AIX-0.md (~1,200 lines) as master reference. AGENTS.md workflow rules. Archive 15 old files. Zero data loss.

---

## ADR-0009: No Docker, Vercel Only

**Status**: Accepted ✅  
**Date**: 2026-05-14

**Context**: Containerization would add complexity.

**Decision**: Vercel hosts the frontend (axiom-id team, Node 22.x). No Docker. Pi Browser is primary target.

---

## ADR-0010: Dark Theme + Bento Grid Design System

**Status**: Accepted ✅  
**Date**: 2026-05-14

**Context**: Need consistent UI across all pages.

**Decision**: Dark theme, Bento Grid, neon-green/electric-blue, glass morphism. Framer Motion for animations. Applied to all axiomid.app pages.
