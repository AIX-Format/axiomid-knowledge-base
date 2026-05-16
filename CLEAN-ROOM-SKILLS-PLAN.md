# 🧼 Clean Room — 7 Skills from IQRA Utils+Infra

الخطة: فهم الوظيفة ← رمي الكود القديم ← كتابة Skill جديد في L3.

---

## Skill 1: `persona-loader`
**المصدر:** `iqra/13-utils/personas.ts` (جزء من 2,548 lines)

**الغرض:** تحميل شخصيات agents من L3 marketplace بدل ما تكون hardcoded في iqra.

**API:**
```typescript
loadPersona(personaId: string): Promise<Persona>
listPersonas(): Promise<PersonaSummary[]>
getPersonaForRole(role: string): Promise<Persona>
```

**Operational Flow:**
1. Agent يستدعي `loadPersona("analyst")`
2. Skill يبحث في L3 marketplace عن شخصية "analyst"
3. يرجع Persona object (name, role, instructions, tone, constraints)
4. Agent يحقن الـ persona في system prompt

**Constitutional Alignment:** 
- No hardcoded personas — كل شخصية من marketplace
- Personas موقعة بـ Ed25519 — أصلية

---

## Skill 2: `sovereign-crypto`
**المصدر:** `iqra/13-utils/sovereign_cipher.ts`

**الغرض:** تشفير AES-256-GCM لأي agent.

**API:**
```typescript
encrypt(plaintext: string, key: Uint8Array): Promise<EncryptedPayload>
decrypt(payload: EncryptedPayload, key: Uint8Array): Promise<string>
generateKey(): Uint8Array
hash(data: string): string
```

**Operational Flow:**
1. Agent يريد تشفير رسالة
2. Skill يولد AES-256-GCM cipher مع IV عشوائي
3. يرجع `{ ciphertext, iv, tag }`
4. Agent يرسل الـ payload بأمان

**Constitutional Alignment:** 
- لا Mock — تشفير حقيقي
- لا Hardcoded keys — المستخدم يدبر المفاتيح

---

## Skill 3: `timeout-utils`
**المصدر:** `iqra/13-utils/timeout.ts` (~50 lines)

**الغرض:** Timeouts + retries + backoff لأي agent.

**API:**
```typescript
withTimeout<T>(promise: Promise<T>, ms: number): Promise<T>
withRetry<T>(fn: () => Promise<T>, options: RetryOptions): Promise<T>
exponentialBackoff(attempt: number): number
```

**Operational Flow:**
1. Agent يحدد timeout + retry policy
2. Skill ينفذ العملية مع timeout
3. لو فشلت → retry مع exponential backoff
4. لو استمر الفشل → يرجع error

**Constitutional Alignment:**
- Circuit Breaker: 3 فشل → يوقف
- لا Infinite retries — حد أقصى

---

## Skill 4: `system-heartbeat`
**المصدر:** `iqra/12-infrastructure/heartbeat.ts` (579 lines)

**الغرض:** مراقبة صحة الـ agent/system.

**API:**
```typescript
getHealth(): HealthStatus
getMetrics(): SystemMetrics
ping(): boolean
report(): HealthReport
```

**HealthStatus:**
```typescript
{
  status: 'healthy' | 'degraded' | 'down',
  uptime: number,
  cpu: number,
  memory: number,
  lastCheck: timestamp
}
```

**Operational Flow:**
1. Agent يطلب health check
2. Skill يجمع system metrics (CPU, RAM, uptime)
3. يحسب الـ health score
4. يرجع تقرير

**Constitutional Alignment:**
- لا Mock — قياسات حقيقية من النظام
- Circuit Breaker: 3 fail → degraded

---

## Skill 5: `skill-registry`
**المصدر:** `iqra/12-infrastructure/tools_registry.ts` (568 lines)

**الغرض:** Registry لاكتشاف وإدارة الـ skills — هو نفسه مفهوم L3 marketplace.

**API:**
```typescript
register(skill: SkillDefinition): void
discover(query: string): SkillDefinition[]
getSkill(id: string): SkillDefinition | null
listByTier(tier: SkillTier): SkillDefinition[]
```

**SkillDefinition:**
```typescript
{
  id: string,
  name: string,
  version: string,
  tier: 'BASIC' | 'PRO' | 'SOVEREIGN',
  description: string,
  api: APIDefinition,
  signature?: string  // Ed25519 signed
}
```

**Operational Flow:**
1. Agent يبحث عن skill: `discover("crypto")`
2. Skill يرجع list of matching skills
3. Agent يختار skill ويستدعيه
4. الـ skill ينفذ

**Constitutional Alignment:**
- Signature verification لكل skill
- Tier system: SOVEREIGN skills يتطلب human approval

---

## Skill 6: `vector-search`
**المصدر:** `iqra/12-infrastructure/qdrant.ts` (118 lines)

**الغرض:** Vector search موحّد — Qdrant أو أي vector DB.

**API:**
```typescript
search(query: string, limit?: number): Promise<SearchResult[]>
upsert(id: string, vector: number[], payload: any): Promise<void>
delete(id: string): Promise<void>
```

**Operational Flow:**
1. Agent يرسل query نصية
2. Skill يحول النص لـ embedding (text-embedding-004)
3. يبحث في vector DB
4. يرجع top-K results

**Constitutional Alignment:**
- Fallback: SHA-256 hash لو offline
- No fake embeddings

---

## Skill 7: `universal-logger`
**المصدر:** `iqra/12-infrastructure/logger.ts` (72 lines)

**الغرض:** Structured logging لكل agents — موحّد عبر الـ stack.

**API:**
```typescript
log(level: LogLevel, message: string, context?: object): void
info(message: string, context?: object): void
warn(message: string, context?: object): void
error(message: string, error?: Error): void
setLevel(level: LogLevel): void
```

**Operational Flow:**
1. Agent يريد تسجيل حدث
2. يمرر message + level + optional context
3. Skill يكتب structured log
4. يرسل لـ central log (console / file / remote)

**Constitutional Alignment:**
- لا تسجيل secrets — filter تلقائي
- Structured logs — يمكن تحليلها آلياً

---

## 🗺️ Migration Path

```
IQRA اليوم                                   ← بعد Clean Room
───────────────────────────────────────────
13-utils/personas.ts         →  L3 skill: persona-loader  
13-utils/sovereign_cipher.ts →  L3 skill: sovereign-crypto
13-utils/timeout.ts          →  L3 skill: timeout-utils
12-infra/heartbeat.ts        →  L3 skill: system-heartbeat
12-infra/tools_registry.ts   →  L3 skill: skill-registry
12-infra/qdrant.ts           →  L3 skill: vector-search
12-infra/logger.ts           →  L3 skill: universal-logger

في IQRA: 4,264 lines → thin wrappers تستدعي L3 skills
في L3: 7 new skills في marketplace
```

## 💰 الفائدة

| قبل | بعد |
|-----|-----|
| 4,264 lines في IQRA (مش مربوط بـ L3) | ~1,400 lines skills في L3 |
| IQRA بس يستخدمهم | أي Agent (PiWorker, GemClaw, إلخ) |
| صيانة منفصلة | صيانة موحّدة في L3 |
| بدون signature | Ed25519 signed skills |
