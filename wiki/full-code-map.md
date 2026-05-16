---
title: "Full Code Map — Every Repo"
last_updated: "2026-05-16"
status: "stable"
tags: [code, structure, map, all-repos]
layer: "all"
related:
  - "[[codebase-sizes]]"
  - "[[stack-map]]"
  - "[[L2-iqra]]"
  - "[[L5-piworker-os]]"
  - "[[L6-gemclaw]]"
---

# Full Code Map

> كل سطر من كل repo — لأخذ أفضل ما فيه.

## L0 axiomid-project (Consciousness)

```
الحجم: ~2,759 lines TS | Next.js 16

src/app/
├── layout.tsx          ← Root layout (Geist fonts, WalletProvider)
├── page.tsx            ← Bento Grid UI (Hero, AxiMascot, XP)
├── globals.css         ← Cyberpunk theme (17K+ lines CSS)
└── api/
    ├── auth/connect/route.ts    ← POST: Wallet auth
    ├── action/claim/route.ts    ← POST: Claim XP
    ├── user/status/route.ts     ← GET: User profile
    └── score/route.ts          ← POST: Digital DNA score

النقاط الفريدة: XP Tier system (Ghost→Axiom), WalletConnect, Cyberpunk Bento Grid, Digital DNA Score
```

## L2 iqra (Memory System)

```
الحجم: 52,447 lines TS + 4,421 lines Go | Next.js 15

src/lib/iqra/
├── 01-core/ (5,512 lines)        ← brain.ts, loop.ts, MissionControl
├── 02-workers/ (1,819 lines)     ← SovereignWorker + 4 workers
├── 03-memory/ (4,115 lines)      ← MemoryBridge 5-layer
├── 04-quran/ (4,636 lines)       ← Quran Pattern Engine
├── 05-rewards/ (743 lines)       ← Reward engine
├── 06-security/ (3,003 lines)    ← Damir Conscience, TrustChain, DID
├── 07-llm/ (990 lines)           ← Ollama, Groq, Gemini providers
├── 08-cognitive/ (1,492 lines)   ← Engine, Swarm, Skills
├── 09-evolution/ (2,674 lines)   ← Self-Evolve, MCTS, League
├── 10-topology/ (671 lines)      ← Topological analysis
├── 12-infrastructure/ (1,583 lines) ← Logger, Heartbeat, Registry
├── 13-utils/ (2,548 lines)       ← Personas, Cipher
├── 14-aix/ (2,143 lines)         ← AIX manifest bridge
└── simulation/ (254 lines)       ← MCTS self-play
```

## L5 PiWorker-OS (Body)

```
الحجم: 5,294 lines TS + 8,100 lines Go

core/ (TypeScript — 5,294 lines)
├── agents/ (209 lines)         ← agent-spawner, fleet-manager
├── brain/ (475 lines)          ← gemini-oracle, neural-memory
├── engine/ (1,214 lines)       ← sovereign-bridge, quantum-mirror
├── finance/ (759 lines)        ← treasury-vault, pi-integration
└── identity/ (582 lines)       ← genesis-factory, piworker-did

sidecar/ (Go — 8,100 lines)
├── finance/                    ← escrow-manager, soroban-bridge
└── sovereign-engine/pkg/       ← server, engine, bridge, identity
```

## L6 GemClaw (Voice)

```
الحجم: 29,453 lines TS | Next.js 15 + Firebase

app/ (2,486 lines — 20 files)
├── page.tsx                   ← Landing + voice session
├── forge/page.tsx             ← Aether Forge
├── dashboard/page.tsx         ← Agent dashboard
└── workspace/page.tsx         ← Voice interaction space

components/ (9,488 lines — 53 files)
├── ConversationalAgentCreator ← Voice-based agent creation
├── ForgeArchitect.tsx         ← 11-step voice forge
└── Workspace.tsx              ← Voice interaction canvas

lib/ (13,721 lines — 87 files)
├── voice/synthesis-engine.ts  ← Voice synthesis
├── neural/router.ts           ← Multi-model proxy
├── agents/skill-registry.ts   ← Skill registry
└── store/useGemclawStore.ts   ← Zustand 5-slice state
```

## What to Take from Each Repo

| Repo | Key Unique Code |
|------|----------------|
| axiomid-project | XP Tier System, WalletConnect, Cyberpunk UI |
| iqra | 7 Loops, MissionControl, MemoryBridge, Damir, Quran Engine, Evolution |
| L3 | 124 skills marketplace, x402 gateway, Constitutional Governance |
| AlphaAxiom | RiskShield, Signal Generator, RL Environment |
| PiWorker-OS | TreasuryVault, EscrowManager (Go), SovereignBridge |
| GemClaw | useLiveAPI, Aether Forge, Neural Router |

## Duplicate Analysis

| Function | Best | Weakest | Decision |
|----------|------|---------|----------|
| TrustChain | iqra (191 refs) | aix-format (concept) | Take iqra |
| x402 | L3 (Hono) | PiWorker Go (duplicate) | Take L3 |
| Neural Router | iqra (990 lines) | GemClaw (235 lines) | Merge |
| Gemini Calls | PiWorker (184 lines) | — | Add to iqra |
| Agent Memory | iqra (4,115 lines) | PiWorker (165 lines) | Take iqra |
