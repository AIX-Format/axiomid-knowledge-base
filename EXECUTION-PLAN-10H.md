# 🔥 AIX Sovereign Stack — 10-Hour Execution Plan
> خطة تنفيذ كاملة — Hour by Hour

## 🕐 Hour 1-2: Package Unification

### Task 1.1 — توحيد versions (15 min)
```
@axiom/identity: 1.3.0 → 0.1.0
@axiom/schema: 1.3.0 → 0.1.0  
@axiom/pi: 0.1.0 ✅
@axiom/validate: 0.1.0 ✅
@axiom/lint: 0.1.0 ✅
@axiom/health: 0.1.0 ✅
@axiom/autofix: 0.1.0 ✅
جميعها 0.1.0
```

### Task 1.2 — Fix tsconfig.json لكل package (20 min)
| Package | الإصلاح |
|---------|---------|
| axiom-pi | إضافة `types: ["node"]` ✅ (خلصنا) |
| axiom-identity | إضافة `types: ["node"]` |
| axiom-schema | إضافة `types: ["node"]` |
| axiom-validate | إنشاء tsconfig.json |
| axiom-lint | إنشاء tsconfig.json |
| axiom-health | إنشاء tsconfig.json |
| axiom-autofix | إنشاء tsconfig.json |

### Task 1.3 — npm install لكل package (30 min)
```
لكل package: cd packages/$pkg && npm install --silent
```

### Task 1.4 — Build (30 min)
```
لكل package: npx tsc
الـ 4 packages الأساسية: axiom-identity, axiom-schema, axiom-pi
الـ 3 tools: axiom-validate, axiom-lint, axiom-health, axiom-autofix
```

### Task 1.5 — Push التغييرات (15 min)
```
git add -A && git commit -m "chore: unify @axiom/* packages to v0.1.0"
git push origin main
```

---

## 🕐 Hour 3-4: Brain — iqra Integration

### Task 2.1 — ربط iqra بـ @axiom/identity (30 min)
**الملفات المتأثرة:**
```
iqra/src/lib/iqra/06-security/did.ts
  قبل: import { generateKeyPair, codec } from '#aix/ed25519_signer'
  بعد: import { generateKeyPair, codec } from '@axiom/identity'

iqra/src/lib/iqra/14-aix/ed25519_signer.ts
  SHIM كامل — يُحذف (كل الحمولة نقلت لـ @axiom/identity)
  توفير: 46 lines

iqra/src/lib/iqra/14-aix/canonical.ts
  SHIM كامل — يُحذف
  توفير: 15 lines

iqra/src/lib/iqra/14-aix/index.ts
  إزالة الـ exports القديمة (canonicalizeJSON, canonicalizeJSONBytes, generateKeyPair...)
  بدلها: import { ... } from '@axiom/identity'
```

**التبعيات:**
- @axiom/identity لازم يكون package.json في iqra

### Task 2.2 — إضافة Gemini Provider (40 min)
**ملف جديد:** `iqra/src/lib/iqra/07-llm/gemini.ts`
```
import { GoogleGenerativeAI } from '@google/generative-ai'

export class GeminiProvider {
  async generate(prompt: string): Promise<string> { ... }
  async analyzeOpportunity(input: string): Promise<ROIEvaluation> { ... }
}
```
**المصدر:** كود من PiWorker-OS `core/brain/gemini-multimodal-oracle.ts` (184 lines)
**الدمج:** الاقتصاص لأساسيات الـ inference + إزالة PiWorker-specific logic

**ملف متأثر:** `iqra/src/lib/iqra/07-llm/economy.ts`
- إضافة GeminiProvider كمزود رابع (بعد Ollama, Groq, OpenRouter)

### Task 2.3 — BetrayalProtocol Integration (30 min)
**ملف جديد:** `iqra/src/lib/iqra/06-security/betrayal_integration.ts`
```
// 150 lines — يلف DamirConscience + ByzantineFilter في واجهة BetrayalProtocol

export interface BetrayalCheck {
  action_id: string
  agent_id: string
  intention: string
  economic_context?: EconomicContext
}

export class BetrayalGuard {
  async evaluate(check: BetrayalCheck): Promise<{ 
    allowed: boolean
    reason: string
    risk_level: 'low' | 'medium' | 'high' | 'critical'
  }> {
    // 1. DamirConscience.check() — فحص أخلاقي
    // 2. ByzantineFilter.detectZScore() — فحص شذوذ
    // 3. ForbiddenPatternsValidator.validate() — فحص أنماط
    // 4. Score مرجح → قرار
  }
}
```

**الملف المحذوف:** PiWorker-OS `core/governance-engine.ts` (58 lines, interfaces فقط)
**ملف متأثر:** PiWorker-OS يستدعي `BetrayalGuard` بدل الـ interfaces

### Task 2.4 — Push iqra changes (20 min)
```
git add -A && git commit -m "refactor: integrate iqra with @axiom/identity, add Gemini provider, unify BetrayalProtocol"
git push origin main
```

---

## 🕐 Hour 5-6: Body — PiWorker-OS + Cross-Repo

### Task 3.1 — تحديث PiWorker-OS package.json (15 min)
```
حذف @axiom/pi (لأنه مش منشور بعد — نرجع للـ standalone implementation)

core/finance/pi-integration.ts
  قبل: import { createPayment } from '@axiom/pi'
  بعد: import { authenticateSovereignWallet } from './pi-auth'
```

### Task 3.2 — PiWorker-OS ← iqra LLM (30 min)
**ملف متأثر:** `core/brain/gemini-multimodal-oracle.ts`
- يستدعي `iqra 07-llm/gemini.ts` بدل GoogleGenerativeAI المباشر
- أو: يضيف `@axiom/llm` package (option للتفكير)

### Task 3.3 — PiWorker-OS ← iqra Memory (20 min)
**ملف متأثر:** `core/brain/neural-memory.ts`
- يستخدم `IQRAMemory` من iqra بدل standalone VectorStore
- يحافظ على PiWorker-specific logic (server-only, sovereignClient)

### Task 3.4 — تنظيف PiWorker-OS (30 min)
```
الملفات اللي تتشال (نقل محتواها لـ iqra أو هي dead):
❌ core/governance-engine.ts (نقل لـ iqra 06-security)
❌ core/engine/bounty-scanner.ts (45 lines, low value)
❌ core/engine/order-ingestion.ts (70 lines, duplicate)
❌ core/integrations/google-connector.ts (45 lines, يمكن org)
❌ core/integrations/social-bridge.ts (25 lines, stub)
```

### Task 3.5 — Push PiWorker-OS changes (20 min)

---

## 🕐 Hour 7-8: Deployment + Publish

### Task 4.1 — npm publish (45 min)
```
npm login (محتاج منك account)
npm publish --access public

الترتيب:
1. @axiom/schema (لا تبعيات داخلية)
2. @axiom/identity (يعتمد على @axiom/schema)
3. @axiom/pi (مستقل)
4. @axiom/validate (يعتمد على @axiom/schema)
5. @axiom/lint (مستقل)
6. @axiom/health (مستقل)
7. @axiom/autofix (مستقل)
```

### Task 4.2 — Pi Domain Claim — Guide (15 min)
خطوات تسجيل axiomid.app في Pi Developer Portal.

### Task 4.3 — Vercel Dashboard verification (15 min)
- التحقق من https://axiomid.app 200 OK
- التحقق من validation-key.txt
- اختبار الـ API routes

---

## 🕐 Hour 9-10: Knowledge Base + Documentation

### Task 5.1 — AGENTS.md لكل repo (30 min)
- axiomid-project/AGENTS.md ✅ (محدث)
- PiWorker-OS/AGENTS.md (يحتاج تحديث @axiom/pi refs)
- iqra/AGENTS.md (محدث)

### Task 5.2 — تحديث KB (30 min)
- SESSION-2026-05-15.md
- STACK-MAP.md
- FULL-CODE-MAP.md
- IQRA-PIWORKER-MERGE.md

### Task 5.3 — Final Review (30 min)
- مراجعة كل التغييرات
- التأكد من builds
- التأكد من git status نظيف

---

## 📊 Summary

| Hour | المهمة | المخرجات |
|------|--------|---------|
| 1-2 | Package Unification | 7 packages @ 0.1.0, built |
| 3-4 | Brain: iqra | @axiom/identity, Gemini, BetrayalProtocol |
| 5-6 | Body: PiWorker-OS | Cross-repo integrations + cleanup |
| 7-8 | Deploy + Publish | npm publish, Pi claim, Vercel |
| 9-10 | Knowledge Base | All docs updated |
