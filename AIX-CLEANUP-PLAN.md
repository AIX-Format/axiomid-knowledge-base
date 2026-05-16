# AIX Cleanup Plan
> إزالة dead code + دمج المكرر + الحفاظ على الفريد

## 🔴 P0 — يحذف (Dead Code مؤكد)

| الملف | الحجم | السبب |
|-------|-------|-------|
| `PiWorker-OS/sandbox/executor.ts` | 1 byte | stub فاضي |
| `PiWorker-OS/sandbox/isolated-executor.ts` | 1 byte | stub فاضي |
| `axiomid-project/UI_UX_IMPROVEMENT_PLAN.md` | ~15KB | outdated plan doc |
| `axiomid-project/Granular_Task_Breakdown.md` | ~8KB | outdated plan doc |
| `axiomid-project/ENHANCEMENT_SUMMARY.md` | ~5KB | outdated plan doc |

## 🟡 P1 — يدمج (Duplicate Code موجود في أكتر من repo)

### 1. توحيد الهوية (أعلى أولوية)

| الكود | المصدر | المصير |
|-------|--------|--------|
| `axiom-identity` (Ed25519 + DIDs + canonicalize) | `L1/packages/axiom-identity/` | **يبقى المرجع** |
| Pi KYC generation | `L1/core/pi_kyc_adapter.ts` | **يُدمج في `@axiom/pi`** |
| Pi KYC generation (package) | `L1/packages/pi-kyc/` | **يُدمج في `@axiom/pi`** |
| Pi auth | `PiWorker-OS/core/finance/pi-auth.ts` | **يستخدم `@axiom/pi` بدل standalone** |
| Pi env vars | `axiomid-project/src/lib/pi/env.ts` | **يستخدم `@axiom/pi`** |
| `did:web` | iqra identity | **يتحول إلى `did:axiom`** |
| `did:piworker:` | PiWorker-OS SovereignLedger | **يتحول إلى `did:axiom`** |

### 2. توحيد الدفع

| الكود | المصدر | المصير |
|-------|--------|--------|
| Payment router protocol | `L1/core/agent_payment_router.js` | **يبقى المرجع (abstract)** |
| x402 gateway | `L3/server/` (Cloudflare Workers) | **يبقى standalone (deployment)** |
| PiWorker-OS escrow + treasury | `PiWorker-OS/core/finance/` | **يبقى unique functionality** |
| PiWorker-OS Go sidecar | `PiWorker-OS/sidecar/finance/` | **يبقى unique (Go performance)** |

### 3. توحيد LLM Providers

| الكود | المصدر | المصير |
|-------|--------|--------|
| iqra LLM providers | `iqra/src/lib/iqra/07-llm/` | **يبقى المرجع** |
| GemClaw neural/router | `GemClaw/lib/neural/` | **يُدمج في iqra** (يضاف Anthropic + DeepSeek + OpenAI) |

## 🟢 P2 — يفضل (Unique Code — مش موجود في أي repo تاني)

### Unique Code في كل Repo

**axiomid-project**:
- `src/lib/tiers.ts` — XP tier system (Ghost → Spark → Pulse → Axiom) **فريد**
- `src/app/context/wallet-context.tsx` — Web3 wallet auth **فريد**
- `prisma/schema.prisma` — database schema (User, Action, Vault, Integration) **فريد**
- `src/app/page.tsx` — Bento Grid UI + AxiMascot **فريد**

**aix-format**:
- `schemas/aix.schema.json` — master schema (430+ properties) **فريد**
- `core/abom-scanner.js` — Agent Bill of Materials scanner **فريد**
- `core/validation-engine.js` — plugin-based validation **فريد**
- `packages/aix-zkkyc/` — Zero-knowledge KYC proofs **فريد**
- `packages/axiom-identity/` — identity primitives **فريد**
- `packages/axiom-schema/` — JSON Schema + codegen **فريد**

**iqra**:
- `DamirConscience` — Graded Linear Logic ethics engine **فريد**
- `Quran Pattern Engine` — Shannon entropy + topological analysis **فريد**
- `MCTS self-play` — Monte Carlo Tree Search simulation **فريد**
- `7 Sovereign Loops` — orchestration cycle **فريد**
- `5-layer MemoryBridge` — Hot/Warm/Cold/Vector/Archive **فريد**

**aix-agent-skills**:
- `orchestrator.py` — skill execution engine **فريد**
- `go-engine/` — Shannon entropy, LID, Homology **فريد**
- `templates/skill-template.md` — skill definition format **فريد**

**AlphaAxiom**:
- `signal_generator.py` — Gemini-powered trading signals **فريد**
- `risk_shield.py` — Aladdin Risk Shield (4 rules) **فريد**
- `position_sizing.py` — Kelly + ATR + Fixed Fractional **فريد**
- MCTS for trading **فريد**
- Desktop Tauri app + Ghost Mode overlay **فريد**

**PiWorker-OS**:
- `governance-engine.ts` — Betrayal Protocol **فريد**
- `treasury-vault.ts` — 10% sovereign tax **فريد**
- `escrow-manager.go` — Pi escrow (Go) **فريد**
- `soroban-bridge.go` — Stellar integration **فريد**
- `plugin-gateway.ts` — plugin system **فريد**

**GemClaw**:
- `voice/` — Gemini Live API WebSocket + audio worklet **فريد**
- `Aether Forge` — 11-step voice agent creation **فريد**
- `neural/intent-engine.ts` — NLU intent classification **فريد**
