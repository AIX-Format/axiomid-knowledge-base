---
title: "AIX API Registry — Cross-Repo Endpoints"
last_updated: "2026-05-18"
status: "draft"
tags: [api, registry, endpoints, cross-repo, contracts]
layer: "all"
related:
  - "[[cross-repo-architecture]]"
  - "[[L0-axiomid]]"
  - "[[L1-aix-format]]"
  - "[[L2-iqra]]"
  - "[[stack-map]]"
---

# AIX API Registry — Cross-Repo Endpoints

> سجل مركزي لـ API endpoints بين الـ 7 repos

## axiomid-project (L0)

| Endpoint | Method | Auth | Consumers | Description |
|----------|--------|------|-----------|-------------|
| `/api/auth/connect` | POST | Pi accessToken | GemClaw, aix-format | ربط المحفظة + تسجيل الدخول |
| `/api/agent` | POST | accessToken | aix-format | إنشاء Agent |
| `/api/agent/activate` | POST | accessToken | — | تفعيل Agent |
| `/api/action/claim` | POST | walletAddress | — | مطالبة XP |
| `/api/user/status` | GET | walletAddress | — | حالة المستخدم |
| `/api/did/create` | POST | accessToken | — | إنشاء DID |
| `/api/did/:did` | GET | public | aix-format, iqra | قراءة DID Document |
| `/api/did/:did/rotate` | POST | DID signature | — | تدوير المفاتيح |
| `/api/did/:did/revoke` | POST | DID signature + M-of-N | — | إلغاء DID |
| `/api/did/:did/recover` | POST | Guardian signatures | — | استرداد DID |
| `/api/trustchain/:did` | GET | public | aix-format | سجل التعديلات |

## aix-format (L1)

| Endpoint | Method | Auth | Consumers | Description |
|----------|--------|------|-----------|-------------|
| `/api/manifest/validate` | POST | DID signature | axiomid | التحقق من manifest |
| `/api/manifest/sign` | POST | private key | — | توقيع manifest |
| `/api/schema/:version` | GET | public | axiomid | JSON Schema للإصدارات |

## iqra (L2)

| Endpoint | Method | Auth | Consumers | Description |
|----------|--------|------|-----------|-------------|
| `/api/memory` | POST | DID signature | axiomid, aix-format | إنشاء ذكرى |
| `/api/memory/search` | POST | DID signature | axiomid, aix-format | بحث في الذكريات |
| `/api/memory/:id` | GET | DID signature | — | قراءة ذكرى معينة |
| `/api/patterns` | POST | DID signature | — | تحليل الأنماط |

## PiWorker-OS (L5)

| Endpoint | Method | Auth | Consumers | Description |
|----------|--------|------|-----------|-------------|
| `/api/kyc/status` | GET | Pi accessToken | axiomid | حالة KYC |
| `/api/pi/payment` | POST | Pi accessToken | axiomid | إنشاء دفعة Pi |
| `/api/governance/status` | GET | DID signature | — | حالة الحوكمة |

## Shared Types

كل API يستخدم types من `@aix/shared-types`:

```typescript
// API Response standard
interface APIResponse<T> {
  success: boolean
  data?: T
  error?: string
  meta?: {
    did?: string
    timestamp: string
    signature?: string
  }
}
```

---

## التوثيق المقترح لكل Endpoint

كل API endpoint يحتاج في `CROSS-REF.md`:

```markdown
### POST /api/auth/connect

**Owner**: axiomid-project
**Auth**: Pi accessToken (JWT) أو public
**Body**: { walletAddress, piUid?, piUsername?, accessToken? }
**Response**: { user: User }

**Consumers**:
- [[L6-gemclaw|GemClaw]] → `src/lib/auth-client.ts` (line 42)
- [[L1-aix-format|aix-format]] → `packages/axiom-identity/src/auth.ts` (line 15)

**Changes History**:
- 2026-05-14: إضافة accessToken validation
- 2026-05-17: تحسين type validation (CodeRabbit)
```
