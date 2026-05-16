---
title: "AIX Architecture — Cross-System Flows"
last_updated: "2026-05-16"
status: "stable"
tags: [architecture, flows, identity, payment, orchestration]
layer: "all"
related:
  - "[[stack-overview]]"
  - "[[human-body-architecture]]"
  - "[[cross-system-flows]]"
  - "[[L2-iqra]]"
---

# AIX Architecture — Cross-System Flows

## 1. Identity Flow (L0 → L5)

```
axiomid-project (L0)                    iqra (L2)                      PiWorker-OS (L5)
─────────────────                      ───────                        ─────────────
Wallet Auth → prisma.user               DID Generation                  Agent Birth
→ calculateTier(xp)                     → did:axiom:axiomid.app:        → pw-agt-${random}
→ Ghost/Spark/Pulse/Axiom               → Ed25519 keypair               → SovereignLedger.etch()
```

**Problem**: iqra يستخدم `did:web` و PiWorker-OS يستخدم `did:piworker:` — المفروض كلهم `did:axiom:axiomid.app:*`

## 2. Payment Flow (L5 → L3 → L1)

```
PiWorker-OS Treasury                    L3 x402 Gateway                 L1 Protocol
→ grossProfit * 10% tax                 → GET /skills/:name/manifest    → status 402
→ reserves += tax                       → x402Middleware                → X-Payment-Required
→ SovereignBridge.lockEscrow            → c.json(manifest)
    → Go EscrowManager.LockFunds
```

**Problem**: PiWorker-OS عنده نظام payment خاص (EscrowManager) بدل استخدام x402 الموحد.

## 3. IQRA Brain Execution (L2)

```
iqraThink()
→ fitrahFilter (forbidden patterns + Damir)
→ isLocalMode?
  ├── true → detectSkill → executeWithSkill
  └── false → MissionControl:
        1. Resonance (Damir check)
        2. Research (Damir check)
        3. Validation (Damir check)
        4. Execution (Damir check)
→ RewardEngine.grantFromReports()
→ appendToTrustChain()
→ SoulEngine.pulse() ← 3-6-9 geometry
```

## 4. Memory 5-Layer (L2)

| Layer | Storage | Speed | TTL | Size |
|-------|---------|-------|-----|------|
| **HOT** | RAM (Map) | <1ms | 1 hour | 49 items (7×7) |
| **WARM** | SQLite (sqlite-vec) | <5ms | 7 days | Unlimited |
| **COLD** | Redis/Supabase | <50ms | 30 days | Unlimited |
| **VECTOR** | Qdrant | <100ms | ∞ | Unlimited |
| **ARCHIVE** | LanceDB | <200ms | ∞ | Unlimited |

## 5. Trading → Tax (L4 → L5)

```
AlphaAxiom → signal_generator.py → position_sizing.py
→ risk_shield.py (4 rules: max 20% equity, max 3 positions, daily loss 2%, max drawdown 5%)
→ trading_core.py → profit → PiWorker-OS Treasury (10% tax)
```

## 6. Voice Flow (L6)

```
GemClaw → WebSocket Gemini 2.0 Flash (BidiGenerateContent)
→ AudioWorklet + SharedArrayBuffer (24kHz PCM)
→ Silero VAD (barge-in)
→ Aether Forge (11-step voice agent creation)
→ Neural Router → Google | Claude | DeepSeek | OpenAI
```

انظر [[cross-system-flows]] للتفاصيل الكاملة، و [[L2-iqra]] لمعمارية IQRA.
