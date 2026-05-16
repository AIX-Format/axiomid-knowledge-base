# 🔗 AIX Sovereign Stack — Cross-System Integration Flows
> آخر تحديث: 2026-05-15 | الـ Master Integration Document

## 🔄 Flow 1: Identity (L0 → L5)
```
L0 axiomid-project               L2 iqra                      L5 PiWorker-OS
─────────────────                ───────                      ─────────────
Wallet Auth (route.ts)           DID Generation (did.ts)       Agent Birth
  → prisma.user.findUnique         → generateKeyPair()           → pw-agt-${random}
  → calculateTier(xp)              → did:axiom:axiomid.app:     → did:axiom:axiomid.app:
  → Ghost/Spark/Pulse/Axiom        → Ed25519 keypair             → SovereignLedger.etch()
```

## 🔄 Flow 2: Money/Payments (L5 → L3 → L1)
```
L5 PiWorker-OS                  L3 Marketplace               L1 Protocol
─────────────────               ─────────────                ────────────
Treasury (treasury-vault.ts)    x402 Gateway (index.ts)      agent_payment_router.js
  → grossProfit * 10% tax        → GET /skills/:name/manifest  → status 402
  → reserves += tax              → x402Middleware               → X-Payment-Required
  → SovereignBridge.lockEscrow   → c.json(manifest)            → X-Payment-Amount
    → Go EscrowManager.LockFunds
    → Transaction{Status: LOCKED}
```

## 🔄 Flow 3: IQRA Brain Execution (L2)
```
iqraThink(brain.ts)
  → fitrahFilter (forbidden patterns + Damir)
  → isLocalMode?
    ├── true → detectSkill → executeWithSkill
    └── false → MissionControl (sovereign_orchestrator.ts)
          ├── 1. Resonance (Damir check)
          ├── 2. Research (Damir check)
          ├── 3. Validation (Damir check)
          └── 4. Execution (Damir check)
  → RewardEngine.grantFromReports()
  → appendToTrustChain()
  → SoulEngine.pulse() ← 3-6-9 geometry
    → counter % 3 = 0 → Reflection
    → counter % 6 = 0 → Evolution
    → counter % 9 = 0 → Wisdom
    → counter % 7 = 0 → Evolution Cycle
    → counter % 40 = 0 → Topological Flood
```

## 🔄 Flow 4: Memory 5-Layer (L2)
```
Hot (RAM) ← MemoryBridge ← 49 items, LRU eviction, <1ms
  ↓ promote at 9
Warm (SQLite) ← MicroMemory ← sqlite-vec, Ebbinghaus, <5ms
  ↓ archive at 27
Cold (Redis/Supabase) ← IQRAMemory ← 7-day TTL, <50ms
  ↓ vector store
Vector (Qdrant) ← semantic search, 768-dim, cosine
  ↓ deep archive
Archive (LanceDB) ← long-term, columnar, persistent
```

## 🔄 Flow 5: Trading → Tax (L4 → L5)
```
AlphaAxiom (signal_pipeline.py)
  → signal_generator.py: Gemini → JSON signal
  → position_sizing.py: fixed_fractional(2% risk)
  → risk_shield.py: 4 rules
    ├── max_position ≤ 20% equity
    ├── max_concurrent ≤ 3 positions
    ├── daily_loss ≤ 2%
    └── max_drawdown ≤ 5%
  → trading_core.py: CCXT create_order()
  → profit → PiWorker-OS Treasury
    → SOVEREIGN_TAX_RATE = 10%
    → reserves["Pi"] += tax
```

## 🔄 Flow 6: Pi Escrow (L5 Internal)
```
TypeScript (Brain)                    Go (Muscle)
AmrikyyTreasury.createEscrow()       EscrowManager.LockFunds()
  → SovereignBridge.lockEscrow()       → Transaction{Status:LOCKED}
    → sovereignClient.lockEscrow()     → SorobanBridge.SubmitTransaction()
      → HTTP POST to Go                 → Stellar ledger
        → gRPC auth interceptor
          → ConnectLite handler
```

## 🔄 Flow 7: Voice (L6 Internal)
```
GemClaw
  → WebSocket → wss://generativelanguage.googleapis.com/ws/...
  → Gemini 2.0 Flash (BidiGenerateContent)
  → AudioWorklet + SharedArrayBuffer (24kHz PCM)
  → Silero VAD (barge-in)
  → Aether Forge (11-step voice agent creation)
  → Neural Router → /api/neural/router → Google | Claude | DeepSeek | OpenAI
  → Zustand store → 5 slices (Auth, Agent, Cognitive, Sensory, UI)
```

## 🔄 Flow 8: Quran Engine (L2 Internal)
```
IQRA Quran Engine
  → Tadabbur Loop (pattern_engine.ts)
  → Multi-strategy Pattern Hunt (pattern_hunter.ts)
    ├── numerical ← 3, 7, 9, 19, 40, 369, 700
    ├── linguistic ← Arabic roots, Shannon H_EL
    └── topological ← Qalbin VM, persistent homology H0/H1
  → Shannon H_EL < 0.9685 = Quranic signature
  → NumericalValidator → sacred numbers
  → Go Engine (external) → LID, entropy, compression
```

## 📊 ملخص الـ Cross-System Dependencies

| Flow | المصدر | الوجهة | الوسيط |
|------|--------|--------|--------|
| Identity 🆔 | L0 axiomid-project | L2 iqra → L5 PiWorker | @axiom/identity |
| Payment 💰 | L5 PiWorker | L3 Marketplace → L1 | x402 protocol |
| Trading 💹 | L4 AlphaAxiom | L5 Treasury | profit → tax |
| Voice 🎙️ | L6 GemClaw | Gemini API | WebSocket proxy |
| Skills 🛠️ | L3 aix-agent-skills | L2 iqra runtime | MarketplaceLoader |
| Escrow 🔒 | L5 TS | L5 Go gRPC | SovereignBridge |
| Memory 🧠 | L2 iqra | Qdrant/Redis/SQLite | MemoryBridge |
