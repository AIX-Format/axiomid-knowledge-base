---
title: "AIX Cleanup Plan — Dead Code & Duplicates"
last_updated: "2026-05-16"
status: "stable"
tags: [cleanup, dead-code, duplicates, optimization]
layer: "all"
related:
  - "[[clean-room-skills]]"
  - "[[brain-build-plan]]"
  - "[[x402-plan]]"
---

# AIX Cleanup Plan

> إزالة dead code + دمج المكرر + الحفاظ على الفريد.

## 🔴 P0 — Delete (Confirmed Dead Code)

| File | Size | Reason |
|------|------|--------|
| PiWorker-OS/sandbox/executor.ts | 1 byte | Empty stub |
| PiWorker-OS/sandbox/isolated-executor.ts | 1 byte | Empty stub |
| axiomid-project/UI_UX_IMPROVEMENT_PLAN.md | ~15KB | Outdated plan |
| axiomid-project/Granular_Task_Breakdown.md | ~8KB | Outdated plan |
| axiomid-project/ENHANCEMENT_SUMMARY.md | ~5KB | Outdated plan |

## 🟡 P1 — Merge (Duplicate Code)

### 1. Identity Unification (Highest Priority)
- `axiom-identity` (L1) → **stays reference**
- Pi KYC → merge into `@axiom/pi`
- Pi auth (PiWorker-OS) → use `@axiom/pi`
- `did:web` (iqra) → migrate to `did:axiom`
- `did:piworker:` → migrate to `did:axiom`

### 2. Payment Unification
- `x402` L3 gateway → **stays reference**
- PiWorker-OS escrow → stays (unique Pi functionality)
- PiWorker-OS Go x402 → remove (use L3 gateway)

### 3. LLM Provider Unification
- iqra LLM providers → **stays reference**
- GemClaw neural/router → merge into iqra

## 🟢 P2 — Preserve (Unique Code)

### axiomid-project (Unique)
- XP Tier System (Ghost→Spark→Pulse→Axiom)
- Web3 Wallet Auth
- Bento Grid UI + AxiMascot
- Prisma schema

### iqra (Unique)
- DamirConscience — Graded Linear Logic ethics
- Quran Pattern Engine — Shannon entropy + topology
- MCTS self-play
- 7 Sovereign Loops
- 5-layer MemoryBridge

### PiWorker-OS (Unique)
- Betrayal Protocol — governance-engine
- 10% sovereign tax — treasury-vault
- Pi escrow (Go) — escrow-manager
- Stellar integration — soroban-bridge
- Plugin system — plugin-gateway

### GemClaw (Unique)
- Voice — Gemini Live API WebSocket + audio worklet
- Aether Forge — 11-step voice agent creation
- Neural intent engine — NLU classification

### AlphaAxiom (Unique)
- Signal Generator — Gemini-powered trading signals
- Risk Shield — 4 rules Aladdin
- Position Sizing — Kelly + ATR + Fixed Fractional
- Tauri desktop app + Ghost Mode

### Other (Unique)
- L1: aix.schema.json (430+ properties), abom-scanner, ZK KYC
- L3: orchestrator.py, Go engine (Shannon, LID, Homology)
