---
title: "Cross-Repo Architecture — 7 Repositories Integration"
last_updated: "2026-05-18"
status: "draft"
tags: [architecture, cross-repo, integration, graph, dependency]
layer: "all"
related:
  - "[[L0-axiomid]]"
  - "[[L1-aix-format]]"
  - "[[L2-iqra]]"
  - "[[L3-aix-agent-skills]]"
  - "[[L4-alphaaxiom]]"
  - "[[L5-piworker-os]]"
  - "[[L6-gemclaw]]"
  - "[[zero-agent-stack]]"
  - "[[stack-map]]"
---

# Cross-Repo Architecture — 7 Repositories Integration

> تحسين الاتصال بين الـ 7 repos بناءً على أبحاث arxiv والـ Knowledge Graph patterns

## Current State: الـ 7 Repos

```
┌────────────────────────────────────────────┐
│           AIX Sovereign Stack              │
├────────────────────────────────────────────┤
│ L0: axiomid-project    (Next.js + Prisma)  │ ← Root Authority
│ L1: aix-format         (pnpm monorepo)     │ ← Protocol & DNA
│ L2: iqra               (TS + AI)          │ ← Memory OS
│ L3: aix-agent-skills   (Skills)           │ ← Agent Skills
│ L4: AlphaAxiom         (Python + TS)      │ ← Trading
│ L5: PiWorker-OS        (Go + TS)          │ ← Pi Infrastructure
│ L6: GemClaw            (TS)              │ ← Gemini Integration
└────────────────────────────────────────────┘
```

### المشكلة حالياً

1. **لا يوجد Dependency Map** — مين يستخدم إيه من الـ repos الأخرى
2. **Shared interfaces مبعثرة** — types مكررة عبر الـ repos
3. **API contracts غير موثقة** — REST endpoints بين الـ services
4. **لا يوجد Cross-repo search** — البحث محصور في repo واحد
5. **Onboarding صعب** — المطور الجديد يحتاج يعرف 7 repos بدون خريطة

## Research-Based Solutions

### من arxiv.org وأبحاث 2025-2026

| الورقة | الفكرة | تطبيقها عندنا |
|--------|--------|---------------|
| **LogicLens** (2601.10773) | Structural + Semantic Code Graph + GraphRAG + ReAct Agent | بناء Knowledge Graph للـ 7 repos |
| **RPG: Repository Planning Graph** (2509.16198) | RPG → ZeroRepo → graph-guided generation | Zero CLI لتوليد cross-repo code |
| **KG-based Code Generation** (ICSE 2025) | Tree-sitter AST + embeddings + hybrid retrieval | Cross-repo semantic search |
| **GraphRAG للـ Code** | Graph + RAG للـ code retrieval | Agent يفهم 7 repos بذكاء |

### Architecture المقترحة: AIX Knowledge Graph

```
                    ┌───────────────────────┐
                    │   AIX Knowledge Graph  │
                    │  (Neo4j / Memgraph)    │
                    └──────────┬────────────┘
                               │
         ┌─────────────────────┼─────────────────────┐
         │                     │                     │
         ▼                     ▼                     ▼
┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
│ Structural Graph │  │  Semantic Graph │  │  Contract Graph │
│ (AST-level)      │  │ (Domain-level)  │  │ (API-level)     │
├─────────────────┤  ├─────────────────┤  ├─────────────────┤
│ classes,fns,     │  │ entities,business│  │ endpoints,types,│
│ deps,inheritance│  │ concepts,flows  │  │ schemas,contracts│
└─────────────────┘  └─────────────────┘  └─────────────────┘
```

### 1. Structural Graph (Tree-sitter + AST)

```
Repo: axiomid-project
  └── src/
      ├── app/api/auth/connect/route.ts
      │   ├── imports: prisma, tiers
      │   └── exports: POST /api/auth/connect
      ├── lib/pi-sdk.ts
      │   ├── uses: Window.postMessage
      │   └── exports: ensurePiSdk, patchPostMessageForSandbox
      └── lib/prisma.ts
          └── exports: prisma client

Repo: GemClaw
  └── يحتاج auth → يستخدم axiomid-project API

Edge: axiomid:connect ← REST ← GemClaw:agent
```

**ما ينقصنا حالياً**:
- ملف واحد يوثق REST endpoints بين الـ repos
- Shared types package لكل الـ repos
- API versioning

### 2. Semantic Graph (Domain Entities)

```
AIX Domain Entities:

User (axiomid) → has DID (axiomid) → signs Manifest (aix-format)
             → has Memory (iqra)
             → runs Skills (aix-agent-skills)
             → trades via AlphaAxiom
             → verified by Pi KYC (PiWorker-OS)
             → backed up by GemClaw
```

**ما ينقصنا**:
- Entity Relationship Diagram للـ 7 repos
- Domain events بين الـ repos
- Shared terminology dictionary

### 3. Contract Graph (APIs + Schemas)

```
API Contracts بين الـ repos:

axiomid → أي repos تستخدم API بتاعه؟
  - /api/auth/connect → يستخدمه GemClaw
  - /api/agent → يستخدمه aix-format
  - /api/did/* → يستخدمه الكل

iqra → memory API
  - /api/memory → يستخدمه axiomid (user context)
  - /api/memory/search → يستخدمه aix-format (agent memory)
```

## تحسينات مقترحة

### Phase 1: Foundation (فوري)

#### 1.1 CROSS-REF.md في كل Repo
كل repo يحتوي ملف `CROSS-REF.md` يوثق:
```markdown
# Cross-Ref: Repo → AIX Stack

## يستخدم من
- [[L0-axiomid|axiomid-project]] → /api/auth/connect (للـ auth)
- [[L2-iqra|iqra]] → MemoryClient (للمستخدم)

## يستخدم عندنا
- `src/lib/api-client.ts` → يتصل بـ axiomid و iqra

## Shared Types
- `User` (من axiomid) عبر `@aix/shared-types`
```

#### 1.2 Shared Types Package
إضافة `@aix/shared-types` في `aix-format/packages/@aix/shared-types`:

```typescript
// User من L0
export interface AIXUser {
  did: string
  walletAddress: string
  tier: Tier
  xp: number
}

// DID من L0
export interface DIDDocument {
  id: string
  verificationMethod: VerificationMethod[]
  service: Service[]
}

// Manifest من L1
export interface AIXManifest {
  meta: Meta
  security: Security
  identity_layer: IdentityLayer
  trustchain: TrustChainEntry[]
}

// Memory من L2
export interface MemoryEntry {
  id: string
  type: 'episodic' | 'semantic' | 'procedural'
  content: string
  timestamp: string
}
```

#### 1.3 API Registry
ملف `API-REGISTRY.md` في جذر KDB يوثق كل API endpoint بين الـ repos:

| Endpoint | Owner | Consumers | Method | Auth |
|----------|-------|-----------|--------|------|
| `/api/auth/connect` | axiomid | GemClaw, aix-format | POST | Pi accessToken |
| `/api/agent` | axiomid | aix-format | POST | JWT |
| `/api/did/:did` | axiomid | aix-format, iqra | GET | public |
| `/api/memory/search` | iqra | axiomid, aix-format | POST | DID signature |
| `/api/trustchain/:did` | axiomid | aix-format | GET | public |

### Phase 2: Knowledge Graph (شهر 1-2)

#### 2.1 Tree-sitter Parsing Script
نستخدم `scripts/parse-repos.py`:

```python
# كل ليلة: parse الـ 7 repos وبناء JSON graph
# المخرجات: cross-repo-deps.json
# - classes, functions, imports, exports
# - REST endpoints (المسارات + الـ methods)
# - Dependencies بين الـ repos
```

#### 2.2 GraphRAG للـ Agents
كل agent يقدر يسأل:
```
"Show me all repos that use the User model"
"Which API endpoints does GemClaw depend on?"
"Trace the auth flow from Pi SDK → axiomid → agent"
"Find all places where DID verification happens"
```

**الأدوات**:
- `graphify` (github/safishamsi/graphify) — يحول أي codebase لـ knowledge graph
- Memgraph + Cypher queries
- أو Hugging Face + NetworkX

#### 2.3 Cross-Repo Semantic Search

```
opensrc path @axiom/shared-types    # يجيب source
opensrc path AIX-Format/axiomid-project  # (مستقبلاً)

# أو Zero CLI:
zero search --query "where is User model used?" --repos all
```

### Phase 3: Zero Integration (شهر 2-3)

#### 3.1 Zero CLI للـ Cross-Repo

```
aix-repo list          # قائمة الـ repos والـ status
aix-repo graph         # Dependency graph
aix-repo search "User"  # Search في كل الـ repos
aix-repo diff          # مقارنة shared types عبر الـ repos
```

#### 3.2 Agent Skills للـ 7 Repos

كل agent في `aix-agent-skills` يقدر:
- يقرأ الـ cross-ref docs
- يبحث في API registry
- يفهم entity relationships
- يتبع الـ data flow عبر الـ layers

### Phase 4: Automated Consistency (شهر 3+)

#### 4.1 CI Checks
```yaml
# GitHub Action: أسبوعياً
- name: Cross-Repo Consistency
  run: |
    aix-repo check-types    # أنواع مشتركة متطابقة؟
    aix-repo check-apis     # API contracts صحيحة؟
    aix-repo check-deps     # Dependencies موثقة؟
```

#### 4.2 ZeroRepo-Style Generation
استخدام Zero + Knowledge Graph لتوليد cross-repo code:
- توليد API clients تلقائياً
- توليد shared types تلقائياً
- التحقق من compatibility

## مقارنة: Before vs After

| Before | After |
|--------|-------|
| معرفة manual بـ 7 repos | Knowledge Graph واحد |
| Types مكررة في كل repo | `@aix/shared-types` |
| API endpoints غير موثقة | API Registry واحد |
| Onboarding: 3 أيام | Onboarding: 1 ساعة (بعد الخريطة) |
| Agent يفكر في repo واحد | Agent يفكر في الـ 7 layers |
| Dependency discovery بـ grep | Dependency graph + search |

## التنفيذ

### أول أسبوع (فوري)
- [ ] إضافة `CROSS-REF.md` في كل repo
- [ ] إنشاء `@aix/shared-types` في aix-format
- [ ] إنشاء `API-REGISTRY.md` في KDB

### الأسبوع 2-4
- [ ] Tree-sitter parsing script
- [ ] Cross-repo dependency JSON
- [ ] تحديث كل SKILL.md في aix-agent-skills بـ cross-repo context
- [ ] إضافة Zero CLI للـ cross-repo commands

### الشهر 2
- [ ] Knowledge Graph (Memgraph أو graphify)
- [ ] GraphRAG للـ agents
- [ ] CI checks للـ consistency
