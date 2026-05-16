# 🧠 Memory Systems — Full Comparison (All Repos)

## iqra (L2) — 03-memory/ — 4,115 lines ✅ **المرجع**

| الملف | الأسطر | الوظيفة | التقنية |
|-------|--------|---------|---------|
| memory.ts | 974 | IQRAMemory — main memory | Redis + Supabase + Qdrant + Google AI |
| micro_memory.ts | 1,003 | Local memory | SQLite + sqlite-vec + Ebbinghaus |
| memory_bridge.ts | 425 | Cache hierarchy | Hot→Warm→Cold LRU |
| pulse_369.ts | 571 | Memory lifecycle | 3-6-9 tick (promote/archive/purge) |
| turbo_compressor.ts | 394 | Embedding compression | SQ8 (768→uint8) |
| memory_topology.ts | 312 | 7-layer unified | PRISM architecture |
| pattern_memory.ts | 303 | Pattern storage | Qdrant |
| lancedb_plugin.ts | 133 | Deep archive | LanceDB |
| **Total** | **4,115** | **Memory system كامل** | |

**الميزات الفريدة:** MemoryBridge (3-tier cache), Pulse369 (auto lifecycle), Ebbinghaus, SQ8, Quantum Memory

---

## PiWorker-OS (L5) — 3 files — 292 lines 🔴 **جزئياً مكرر**

| الملف | الأسطر | الوظيفة | مقابل iqra |
|-------|--------|---------|-----------|
| neural-memory.ts | 165 | **NeuralMemoryMesh** (blackboard) | 🟢 **فريد** — agent-to-agent mesh |
| embedding-engine.ts | 26 | Google AI embedding generation | 🔴 **مكرر** — iqra IQRAMemory.generateEmbedding() |
| vector-store.ts | 101 | In-memory vector store + cosine | 🔴 **مكرر** — iqra Qdrant/LanceDB أوسع |

**الخلاصة:**
- NeuralMemoryMesh → **Unique** — concept مختلف (mesh مش cache)
- EmbeddingEngine + VectorStore → **Duplicate** — iqra IQRAMemory أفضل

---

## GemClaw (L6) — 1 file — 367 lines 🟡 **Firebase-specific**

| الملف | الأسطر | الوظيفة |
|-------|--------|---------|
| memory-store.ts | 367 | Firestore CRUD + Web Worker search/decay |

**المقارنة مع iqra:**
- Firestore بدل Redis/Qdrant ← 🔴 **مختلف تماماً**
- Memory decay (Ebbinghaus) ← 🟡 **مكرر المفهوم** مع iqra MicroMemory
- م. Web Workers ← 🟢 **فريد** — iqra ماعندوش worker-based search
- Agent-scoped memories ← 🟢 **فريد** — iqra memory عام

**الخلاصة:** مختلف تماماً—Firestore-based، مع Web Workers. لا يمكن مقارنته مباشرة مع iqra.

---

## axiomid-project (L0) — Prisma Schema — 58 lines 🟢 **مختلف**

ليس memory system — هو identity storage (User, Action, Vault).

---

## aix-format (L1) — 0 lines 🟢 **لا يوجد**

Protocol layer — مش محتاج memory.

---

## AlphaAxiom (L4) — 0 lines 🟢 **لا يوجد**

Trading engine — ماعندوش memory system.

---

## جدول المقارنة النهائي

| الميزة | iqra (L2) | PiWorker (L5) | GemClaw (L6) |
|--------|-----------|---------------|--------------|
| Hot Cache (RAM) | ✅ MemoryBridge | ❌ | ❌ |
| Warm (SQLite) | ✅ MicroMemory | ❌ | ❌ |
| Cold (Redis) | ✅ IQRAMemory | ❌ | ❌ |
| Vector Search | ✅ Qdrant | ⚠️ VectorStore (ضعيف) | ❌ |
| Archive (LanceDB) | ✅ | ❌ | ❌ |
| Embedding gen | ✅ Google AI | ✅ Google AI (مكرر) | ❌ |
| Ebbinghaus decay | ✅ MicroMemory | ❌ | ✅ memory-store.ts |
| Agent mesh | ❌ | ✅ NeuralMemoryMesh (فريد) | ❌ |
| Web Workers | ❌ | ❌ | ✅ فريد |
| Firestore | ❌ | ❌ | ✅ |

## التوصيات

1. **PiWorker-OS EmbeddingEngine + VectorStore** → يحذف. يستخدم iqra IQRAMemory بدالهم (~127 lines أقل)
2. **PiWorker-OS NeuralMemoryMesh** → يفضل (فريد)
3. **GemClaw memory-store.ts** → يفضل (مرتبط بـ Firebase، مختلف architecture)
