---
title: "IQRA Core API — Memory + Proxy Endpoints"
last_updated: "2026-05-18"
status: "draft"
tags: [iqra, api, memory, proxy, axiomid, l2]
layer: "L2"
related:
  - "[[L2-iqra]]"
  - "[[L0-axiomid]]"
  - "[[cross-repo-architecture]]"
  - "[[changelog]]"
---

# IQRA Core API — Memory + Proxy Endpoints

> واجهة REST لـ IQRA — الدماغ والذاكرة المركزية للـ AIX Stack

## العمارة

```
PiWorker / GemClaw / أي Satellite
        │
        ▼ POST https://axiomid.app/api/proxy/iqra/...
        │
   ┌────┴────┐
   │  Proxy  │ ← Rate Limit + Auth (Tier) + Timeout + Logging
   └────┬────┘
        │
        ▼ http://iqra.internal/api/...
        │
   ┌────┴────┐
   │  IQRA   │ ← Memory Manager / Damir Conscience / Mission Control
   └─────────┘
```

## Memory API

### POST /api/memory/store
تخزين ذكرى جديدة.

```json
{
  "did": "did:axiom:axiomid.app:abc123",
  "type": "episodic",
  "content": "نفذ المستخدم مهمة كذا",
  "metadata": { "source": "piworker", "tier": "Spark" },
  "layer": "hot"
}
```

**Response:** `{ id: "mem_xxx", ok: true }`

### GET /api/memory/fetch?id=
جلب ذكرى محددة.

**Response:**
```json
{
  "id": "mem_xxx",
  "did": "did:axiom:...",
  "type": "episodic",
  "content": "...",
  "metadata": {},
  "layer": "warm",
  "createdAt": "2026-05-18T..."
}
```

### POST /api/memory/search
بحث في الذكريات.

```json
{
  "did": "did:axiom:...",
  "query": "what happened yesterday",
  "limit": 10,
  "layer": "warm"
}
```

**Response:**
```json
{
  "results": [
    { "id": "mem_xxx", "content": "...", "similarity": 0.92, "layer": "warm" }
  ]
}
```

### POST /api/memory/layer
نقل ذكرى بين الطبقات (Hot → Warm → Cold → Vector → Archive).

```json
{
  "id": "mem_xxx",
  "targetLayer": "cold"
}
```

### POST /api/memory/resonate
Resonance Loop — تنشيط الذكريات المرتبطة.

```json
{
  "did": "did:axiom:...",
  "intensity": 0.7
}
```

**Tier requirement:** Spark+

## Conscience API

### POST /api/conscience/check
فحص أخلاقي لـ Agent أو إجراء.

```json
{
  "type": "agent",
  "dna": { "name": "Omar", "capabilities": ["trade", "analyze"] },
  "context": { "creator": "did:axiom:..." }
}
```

**Response:**
```json
{
  "approved": true,
  "score": 0.94,
  "notes": "Agent aligns with sovereign values",
  "violations": []
}
```

**Tier requirement:** Pulse+

## Mission API

### POST /api/mission/register
تسجيل مهمة جديدة.

```json
{
  "agent": "did:axiom:...",
  "type": "analysis",
  "params": { "target": "market" }
}
```

### GET /api/mission/:id
حالة المهمة.

---

## كيفية استخدام الـ Proxy من أي Satellite

### من PiWorker-OS (Go)

```go
resp, err := http.Post(
    "https://axiomid.app/api/proxy/iqra/memory/store",
    "application/json",
    strings.NewReader(`{"did":"did:axiom:...","type":"execution","content":"done"}`),
)
```

### من GemClaw (TypeScript)

```typescript
await fetch('https://axiomid.app/api/proxy/iqra/conscience/check', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ type: 'agent', dna, context }),
})
```

### من أي مكان (cURL)

```bash
curl -X POST https://axiomid.app/api/proxy/iqra/memory/store \
  -H "Content-Type: application/json" \
  -d '{"did":"did:axiom:...","type":"episodic","content":"test"}'
```

## Tier Requirements

| الـ Endpoint | الـ Tier المطلوب |
|-------------|-----------------|
| /api/memory/store | أي (بدون شرط) |
| /api/memory/fetch | أي (بدون شرط) |
| /api/memory/search | أي (بدون شرط) |
| /api/memory/layer | Spark+ |
| /api/memory/resonate | Spark+ |
| /api/conscience/* | Pulse+ |
| /api/mission/* | Pulse+ |

## المتغيرات البيئية

| المتغير | الشرح |
|---------|-------|
| `IQRA_INTERNAL_URL` | الـ URL الداخلي لـ iqra (افتراضي: http://localhost:3000) |
| `IQRA_API_KEY` | مفتاح API للتواصل الداخلي |
