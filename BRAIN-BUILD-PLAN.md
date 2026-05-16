# 🧠 Brain Build Plan — Detailed Code Migration

## المبدأ: كل كود من أي Repo يندمج في iqra أو يرتبط به

### 🔵 Code Moving FROM PiWorker-OS TO iqra

#### 1. Gemini Oracle → iqra 07-llm/gemini.ts
**المصدر:** PiWorker-OS `core/brain/gemini-multimodal-oracle.ts` — 184 lines
**الوجهة:** iqra `src/lib/iqra/07-llm/gemini.ts`

**ما نأخذه:**
- `GoogleGenerativeAI` setup (line 22) 
- `analyzeOpportunity()` (lines 27-101) — مع إزالة PiWorker-specific ROI
- `verifyPhysicalTask()` (lines 107-133) — يفضل
- `performAutonomousAudit()` (lines 141-184) — مع إزالة PluginGateway/Treasury

**ما نتركه في PiWorker-OS:**
- `PluginGateway` logic (line 3, 142-184) — خاص بـ PiWorker
- `AmrikyyTreasury` calls (line 4, 171) — خاص بـ PiWorker
- `REASONING_BUDGET_LIMIT` — ينتقل مع الـ code أو يفضل

**الملف الجديد في iqra (تقديراً 120 lines):**
```typescript
// 07-llm/gemini.ts
import { GoogleGenerativeAI } from '@google/generative-ai'
export class GeminiProvider {
  private genAI: GoogleGenerativeAI
  
  constructor(apiKey?: string) { ... }
  
  async generate(prompt: string): Promise<string> { ... }
  async analyzeImage(image: Buffer, mimeType: string, prompt: string): Promise<string> { ... }
}
```

#### 2. BetrayalProtocol → iqra 06-security/betrayal_integration.ts
**المصدر:** PiWorker-OS `core/governance-engine.ts` — 58 lines (interfaces only)
**الوجهة:** iqra `src/lib/iqra/06-security/betrayal_integration.ts`

**ما نأخذه:**
- `IBetrayalProtocol` interface — المفاهيم
- `EconomicContext` interface — السياق الاقتصادي
- `EconomicRiskLevel` enum — مستويات المخاطرة

**الملف الجديد في iqra (تقديراً 150 lines):**
```typescript
// 06-security/betrayal_integration.ts
import { globalDamir, DamirConscience } from './damir_conscience'
import { ByzantineFilter } from './byzantine_filter'

export class BetrayalGuard {
  // يلف DamirConscience + ByzantineFilter + ForbiddenPatternsValidator
  // في واجهة BetrayalProtocol الموحّدة
}
```

#### 3. Agent Spawning Logic → iqra Worker Protocol
**المصدر:** PiWorker-OS `core/agents/agent-spawner.ts` — 98 lines
**الوجهة:** PiWorker-OS يحتفظ بالـ spawning لكن يستخدم iqra SovereignWorker

**التغيير:** 
- `spawnAgent()` يستدعي `iqra SovereignWorker.execute()` بدل standalone
- `spawnFromAix()` يستخدم iqra manifest_exporter لقراءة .aix packages
- يضيف `new SovereignWorker(provider)` من iqra 02-workers/protocol.ts

### 🟢 Code Staying IN PiWorker-OS (Body)

| الملف | السبب |
|-------|-------|
| `treasury-vault.ts` | 10% tax — فريد |
| `escrow-manager.go` | Pi escrow في Go — فريد |
| `soroban-bridge.go` | Stellar — فريد |
| `plugin-gateway.ts` | نظام plugin خاص |
| `fleet-manager.ts` | Fleet management خاص |
| `sovereign-bridge.ts` | Bridge للـ Go sidecar |

### 🔴 Code اللي يتشال (Duplicate)

| الملف | السبب |
|-------|-------|
| `governance-engine.ts` (58 lines) | interfaces only, يندمج في iqra |
| `pi-auth.ts` (64 lines) | يستخدم @axiom/pi (لما ينشر) |
| `pi-integration.ts` (56 lines) | يستخدم @axiom/pi |

### 🟡 Code اللي يتغير (Connect to iqra)

| الملف | التغيير |
|-------|---------|
| `gemini-multimodal-oracle.ts` | يبقى thin wrapper يستدعي iqra GeminiProvider |
| `neural-memory.ts` | يستخدم iqra MemoryBridge بدل standalone vector store |
| `agent-spawner.ts` | يستخدم iqra SovereignWorker |
| `embedding-engine.ts` | يستخدم iqra IQRAMemory.generateEmbedding() |

## Build Order

```
1. @axiom/schema (v0.1.0)          → build + publish
2. @axiom/identity (v0.1.0)        → build + publish  
3. @axiom/pi (v0.1.0)              → build + publish
4. iqra Gemini Provider            → إضافة ملف جديد
5. iqra BetrayalGuard              → إضافة ملف جديد
6. iqra → @axiom/identity          → ربط الـ imports
7. PiWorker-OS → iqra LLM          → ربط
8. PiWorker-OS → iqra Memory       → ربط
9. npm publish @axiom/validate     → 
10. npm publish @axiom/lint         →
11. npm publish @axiom/health       →
12. npm publish @axiom/autofix      →
```

## Pi Domain Claim — Steps
1. افتح https://pi-apps.developer portal
2. سجل حساب ب Pi Wallet بتاعك
3. أنشئ مشروع جديد: `axiomid.app`
4. Instruction: حط `validation-key.txt` في `public/` (موجود ✅)
5. Instruction: تأكد إن `https://axiomid.app/validation-key.txt` يرجع الـ hash
6. Instruction: إختر Sandbox mode للاختبار
7. Instruction: أضف Pi SDK في الواجهة
