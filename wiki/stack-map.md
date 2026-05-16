---
title: "AIX Stack — Full Map"
last_updated: "2026-05-16"
status: "stable"
tags: [stack, packages, dependencies, map]
layer: "all"
related:
  - "[[stack-overview]]"
  - "[[codebase-sizes]]"
  - "[[full-code-map]]"
---

# AIX Stack — Full Map

## Stack Architecture

```
🧠 L0 axiomid-project (Brain)     → axiomid.app on Vercel
🧬 L1 aix-format (DNA)            → @axiom/* npm packages
🧠 L2 iqra (Memory System)        → 52K lines TS, 7 Loops
🦾 L3 aix-agent-skills (Hands)    → 124 skills + roles + personas + tools + MCPs
💰 L4 AlphaAxiom (Heart)          → 21K Python, trading engine
🛡️ L5 PiWorker-OS (Body)         → 13K TS+Go, escrow + treasury
🎙️ L6 GemClaw (Voice)            → 29K TS, voice + Aether Forge
```

## @axiom/* Package Status

| Package | Ver | Built | Deps | Notes |
|---------|-----|-------|------|-------|
| @axiom/identity | 1.3.0 | ✅ | @noble/ed25519, @noble/hashes | Reference |
| @axiom/schema | 1.3.0 | ✅ | — | AIX Schema |
| @axiom/pi | 0.1.0 | ✅ | zod | Pi integration |
| @axiom/validate | 0.1.0 | ✅ | ajv, zod | Manifest validation |
| @axiom/lint | 0.1.0 | ✅ | — | Linting CLI |
| @axiom/health | 0.1.0 | ✅ | — | Health check CLI |
| @axiom/autofix | 0.1.0 | ✅ | — | Auto-fix CLI |

## L3 aix-agent-skills — Full Inventory

| Section | Count | Description |
|---------|-------|-------------|
| **Skills** | 124 | Executable capabilities |
| **Roles** | — | Agent roles (Sovereign, Builder, Guardian...) |
| **Personas** | 9 | Personalities |
| **Tools** | 7 | MCP tools |
| **MCPs** | — | Model Context Protocol servers |
| **APIs** | 7 | analytics, registry, orchestrator, memory, trustchain, topology, skills |
| **Layers** | 9 | L0 Sovereignty → L8 Simulation |
| **Tiers** | 6 | SOVEREIGN → UNCLASSIFIED |

## Actual Dependencies

```
PiWorker-OS   → @axiom/pi (added but unpublished)
iqra          → @noble/ed25519 (direct, not via @axiom/identity)
aix-format    → workspace:* (local interdependency)
axiomid-project → next, prisma, framer-motion (no @axiom/* yet)
```

## Unification Plan

1. **Publish @axiom/* on npm** — needs npm login + npm publish
2. **Connect iqra to @axiom/identity** — replace direct @noble/ed25519
3. **Connect PiWorker-OS to @axiom/pi** — replace local dep
4. **L3 ← L2/L4/L5/L6** — all satellites buy skills from L3
5. **GemClaw neural → iqra LLM** — unify providers
