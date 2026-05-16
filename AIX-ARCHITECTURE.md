# AIX Architecture — How They Connect
> Dependency direction: L3 → L2 → L1 (one-way)

## 1. تدفق الهوية (Identity Flow)

```
axiomid-project (L0)
    │  يصدر did:axiom:axiomid.app:* DIDs
    ▼
aix-format/packages/axiom-identity (L1)
    │  @axiom/identity package — canonical identity primitives
    │  ├── Ed25519 key generation
    │  ├── JCS canonicalization (RFC 8785)
    │  ├── DID translation (axiom ↔ web)
    │  ├── Pi KYC claims
    │  └── ZK proofs (Groth16 via snarkjs)
    ▼
iqra (L2) + PiWorker-OS (L5) + AlphaAxiom (L4) + GemClaw (L6)
    ─── كلهم يستخدموا did:axiom لهويات agents
```

**Problem**: iqra حالياً يستخدم `did:web` و PiWorker-OS يستخدم `did:piworker:` — المفروض كلهم `did:axiom:axiomid.app:*`

## 2. تدفق الدفع (Payment Flow)

```
aix-format (L1)
    │  agent_payment_router.js — defines protocol
    │  ├── x402 (HTTP 402 / crypto)
    │  ├── Stripe ACP (Shared Payment Tokens)
    │  └── PayPal AP2 (Mandates)
    ▼
aix-agent-skills (L3)
    │  x402 gateway على Cloudflare Workers
    │  skills (59) تباع بـ USDC على Base
    ▼
AlphaAxiom (L4) + PiWorker-OS (L5) + GemClaw (L6)
    ─── يشتوا skills من L3
```

**Problem**: PiWorker-OS عنده نظام payment كامل خاص (EscrowManager, SorobanBridge, AmrikyyTreasury) بدل ما يستخدم x402.

## 3. تدفق التشغيل (Orchestration Flow)

```
iqra (L2) هو قلب التشغيل
    │  7 Sovereign Loops:
    │  1. Read & Map (استيعاب السياق)
    │  2. Evaluate (فلتر أخلاقي عبر Damir)
    │  3. Plan (MCTS strategic simulation)
    │  4. Verify (تحقق قبل التنفيذ)
    │  5. Prioritize (توزيع الموارد)
    │  6. Fix (Tawbah Loop — تصحيح ذاتي)
    │  7. Evolve (تطوير ذاتي عبر Reward Engine)
    ▼
    MissionControl يدير 4 مراحل:
    Resonance → Research → Validation → Execution
    كل مرحلة تتحقق بـ DamirConscience
```

**Problem**: PiWorker-OS عنده MAS-ZERO fleet management منفصل بدل استخدام iqra كـ runtime. المفروض يتكامل مع iqra ودمج BetrayalProtocol في iqra.

## 4. تدفق المصادر (LLM Provider Flow)

```
GemClaw (L6)                              iqra (L2)
    │  neural/router                           │  LLM Providers
    ├── Google Gemini                           ├── Groq (llama-3.3-70b)
    ├── Anthropic Claude                        ├── Ollama (gemma3:4b local)
    ├── DeepSeek                               └── Google Gemini
    └── OpenAI
```

**Problem**: نفس الـ providers يتكرروا. المفروض iqra يكون المرجع وGemClaw يستخدم iqra للـ routing.

## 5. تدفق المهارات (Skills Flow)

```
aix-agent-skills (L3)                          AlphaAxiom (L4)
    59 skills بصيغة Markdown + Python             .aix trading skills بصيغة YAML
    ├── orchestrator.py                          ├── aggressive_scalper.aix
    ├── server/ (x402 gateway)                   └── hot-reload system
    └── Go engine (Shannon, LID, Homology)
```

**Problem**: AlphaAxiom عنده skills format خاص. المفروض يتحولوا إلى L3 format ويشتري من marketplace.

## 🔄 الـ FLOWS الأساسية

### 💰 Money Flows UP (L4-L6 → L3 → L1)
```
AlphaAxiom (L4): Trading Signal Pipeline
  signal_generator.py → position_sizing.fixed_fractional()
  → risk_shield.check() (4 rules: 20%/3pos/2%/5%)
  → engine.execute_trade()
  → profit → PiWorker-OS Treasury (10% tax)

PiWorker-OS (L5): Treasury Financial Flow
  processInflow(grossProfit) → SOVEREIGN_TAX_RATE(10%) → reserves
  createEscrow() → SovereignBridge.lockEscrow() → Go Engine
  deductUsageFee() → plugin payments
```

### 🆔 Identity Flows DOWN (L0 → L1 → L2 → L3)
```
axiomid-project (L0): Wallet Auth Flow
  POST /api/auth/connect
  → prisma.user.findUnique/create
  → calculateTier(xp) → Ghost/Spark/Pulse/Axiom
  → POST /api/action/claim → update XP → new tier

iqra (L2): MissionControl Worker Chain
  Resonance (Gemini Flash) → ResourceFactory → Damir check
  → Research (Gemini Pro) → Damir check
  → Validation (Gemini Flash) → Damir check
  → Execution (Groq) → Damir check
  → RewardEngine → ExperienceBuffer
```

### 🎙️ Voice Flow (L6 → L1)
```
GemClaw (L6): Neural Router
  NeuralRouter.generate(provider, messages)
  → POST /api/neural/router (server-side proxy)
  → Routes to: Google | Anthropic | DeepSeek | OpenAI
  → Returns NeuralResponse with text + latency
```
