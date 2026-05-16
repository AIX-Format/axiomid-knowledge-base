---
title: "Brain Build Plan — Code Migration"
last_updated: "2026-05-16"
status: "in-progress"
tags: [migration, iqra, piworker, integration]
layer: "L2,L5"
related:
  - "[[L2-iqra]]"
  - "[[L5-piworker-os]]"
  - "[[cleanup-plan]]"
  - "[[implementation-roadmap]]"
---

# Brain Build Plan — Code Migration

> كل كود من أي Repo يندمج في iqra أو يرتبط به.

## 🔵 Code Moving FROM PiWorker-OS TO iqra

### 1. Gemini Oracle → iqra 07-llm/gemini.ts
**Source**: PiWorker-OS `core/brain/gemini-multimodal-oracle.ts` (184 lines)
**Destination**: iqra `07-llm/gemini.ts` (~120 lines)

**What we take**: GoogleGenerativeAI setup, analyzeOpportunity(), verifyPhysicalTask()
**What stays**: PluginGateway logic, AmrikyyTreasury calls

### 2. BetrayalProtocol → iqra 06-security/betrayal_integration.ts
**Source**: PiWorker-OS `core/governance-engine.ts` (58 lines)
**Destination**: iqra `06-security/betrayal_integration.ts` (~150 lines)

**New file wraps**: DamirConscience + ByzantineFilter + ForbiddenPatternsValidator
**Deleted from PiWorker-OS**: governance-engine.ts

### 3. Agent Spawning → iqra Worker Protocol
**Source**: PiWorker-OS `core/agents/agent-spawner.ts` (98 lines)
**Change**: spawnAgent() uses iqra SovereignWorker instead of standalone

## 🟢 Code Staying IN PiWorker-OS

| File | Reason |
|------|--------|
| treasury-vault.ts | 10% tax — unique |
| escrow-manager.go | Pi escrow in Go — unique |
| soroban-bridge.go | Stellar — unique |
| plugin-gateway.ts | Plugin system |
| fleet-manager.ts | Fleet management |
| sovereign-bridge.ts | Go sidecar bridge |

## 🔴 Code to Delete (Duplicate)

| File | Reason |
|------|--------|
| governance-engine.ts (58 lines) | Interfaces only, merge into iqra |
| pi-auth.ts (64 lines) | Use @axiom/pi |
| pi-integration.ts (56 lines) | Use @axiom/pi |

## 🟡 Code to Change (Connect to iqra)

| File | Change |
|------|--------|
| gemini-multimodal-oracle.ts | Thin wrapper calling iqra GeminiProvider |
| neural-memory.ts | Use iqra MemoryBridge |
| agent-spawner.ts | Use iqra SovereignWorker |
| embedding-engine.ts | Use iqra IQRAMemory.generateEmbedding() |

## Build Order

```
1. @axiom/schema (v0.1.0)          → build + publish
2. @axiom/identity (v0.1.0)        → build + publish
3. @axiom/pi (v0.1.0)              → build + publish
4. iqra Gemini Provider            → new file
5. iqra BetrayalGuard              → new file
6. iqra → @axiom/identity          → connect imports
7. PiWorker-OS → iqra LLM          → connect
8. PiWorker-OS → iqra Memory       → connect
9-12. Publish remaining @axiom/*   → validate, lint, health, autofix
```
