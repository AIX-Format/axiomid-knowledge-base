---
title: "x402 Payment Unification Plan"
last_updated: "2026-05-16"
status: "in-progress"
tags: [x402, payment, unification, pi, marketplace]
layer: "L1,L3,L5"
related:
  - "[[L3-aix-agent-skills]]"
  - "[[L5-piworker-os]]"
  - "[[L1-aix-format]]"
  - "[[pi-network]]"
---

# x402 Payment Unification Plan

> توحيد نظام الدفع عبر الـ Stack.

## Architecture Target

```
Agent (PiWorker-OS)
    │
    ├─ Requests skill from L3
    │   POST /skills/mcts-simulator/manifest
    │
    ├─ L3 returns 402 + x402 payload
    │   HTTP 402 Payment Required
    │   X-Payment-Header: {...}
    │
    ├─ PiWorker-OS signs payment
    │   via @axiom/pi → Pi SDK
    │
    ├─ Retries with X-PAYMENT
    │   GET /skills/mcts-simulator/manifest
    │   X-PAYMENT: signed_token
    │
    └─ L3 delivers manifest → agent executes
```

## Current State

| Component | Where | Function | Future |
|-----------|-------|----------|--------|
| x402 protocol | L3/server/ (Hono) | Skills marketplace gateway | **Stays** — single gateway |
| x402 Go | PiWorker-OS sidecar | x402 in Go | **Deleted** — use L3 gateway |
| Escrow | PiWorker-OS Go | Pi escrow (LOCKED/RELEASED) | **Stays** — unique for Pi |
| AmrikyyTreasury | PiWorker-OS TS | 10% tax | **Stays** — unique |
| agent_payment_router | aix-format/core/ | Protocol definition | **Stays** — reference |

## Execution Plan (3 Steps)

### Step 1: PiWorker-OS ← L3 x402
Instead of using its own x402.go, make HTTP calls to L3 gateway.

```typescript
// PiWorker-OS/core/finance/skill-purchase.ts
import { createPayment } from '@axiom/pi';

async function purchaseSkill(skillName: string, pricePi: number) {
  const payment = await createPayment({
    amount: pricePi,
    memo: `Skill: ${skillName}`,
  });
  const res = await fetch(`https://skills.axiomid.app/skills/${skillName}/manifest`, {
    headers: { 'X-PAYMENT': payment.identifier }
  });
  return res.json();
}
```

### Step 2: Pi as Payment Rail in L3
- L3 currently supports USDC on Base
- Add Pi as second payment rail

### Step 3: Remove x402.go from PiWorker-OS
- After PiWorker-OS uses L3 gateway
- Delete `sidecar/sovereign-engine/pkg/finance/pi402/`
- Keep `escrow-manager.go` (needed for Pi escrow)

## Benefits
- 🎯 Less code (remove duplicate x402)
- 🔗 Real integration between L5 and L3
- 💰 Pi payments enter ecosystem
- 🧹 Cleaner PiWorker-OS sidecar
