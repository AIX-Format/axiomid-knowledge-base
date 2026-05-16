---
title: "Memory Systems — Full Comparison"
last_updated: "2026-05-16"
status: "stable"
tags: [memory, comparison, iqra, piworker, gemclaw]
layer: "L2,L5,L6"
related:
  - "[[L2-iqra]]"
  - "[[L5-piworker-os]]"
  - "[[L6-gemclaw]]"
---

# Memory Systems — Full Comparison

## iqra (L2) — 03-memory/ — 4,115 lines ✅ **Reference**

| File | Lines | Function | Tech |
|------|-------|----------|------|
| memory.ts | 974 | IQRAMemory | Redis + Supabase + Qdrant + Google AI |
| micro_memory.ts | 1,003 | Local memory | SQLite + sqlite-vec + Ebbinghaus |
| memory_bridge.ts | 425 | Cache hierarchy | Hot→Warm→Cold LRU |
| pulse_369.ts | 571 | Memory lifecycle | 3-6-9 tick |
| turbo_compressor.ts | 394 | Embedding compression | SQ8 (768→uint8) |
| memory_topology.ts | 312 | 7-layer unified | PRISM architecture |
| pattern_memory.ts | 303 | Pattern storage | Qdrant |
| lancedb_plugin.ts | 133 | Deep archive | LanceDB |

**Unique features**: MemoryBridge (3-tier), Pulse369 (auto lifecycle), Ebbinghaus, SQ8, Quantum Memory

---

## PiWorker-OS (L5) — 3 files — 292 lines 🔴 Partially Duplicate

| File | Lines | Function | vs iqra |
|------|-------|----------|---------|
| neural-memory.ts | 165 | NeuralMemoryMesh (blackboard) | 🟢 **Unique** — agent-to-agent mesh |
| embedding-engine.ts | 26 | Google AI embedding | 🔴 **Duplicate** — iqra has this |
| vector-store.ts | 101 | In-memory vector store | 🔴 **Duplicate** — iqra Qdrant/LanceDB |

**Conclusion**: NeuralMemoryMesh → Unique. EmbeddingEngine + VectorStore → Duplicate.

---

## GemClaw (L6) — 1 file — 367 lines 🟡 Firebase-specific

| File | Lines | Function |
|------|-------|----------|
| memory-store.ts | 367 | Firestore CRUD + Web Worker search/decay |

**vs iqra**: Firestore ≠ Redis/Qdrant. Has Ebbinghaus (concept duplicate). Web Workers → Unique. Agent-scoped → Unique.

**Conclusion**: Firebase-based, different architecture. Keep as-is.

---

## Summary Table

| Feature | iqra (L2) | PiWorker (L5) | GemClaw (L6) |
|---------|-----------|---------------|--------------|
| Hot Cache (RAM) | ✅ MemoryBridge | ❌ | ❌ |
| Warm (SQLite) | ✅ MicroMemory | ❌ | ❌ |
| Cold (Redis) | ✅ IQRAMemory | ❌ | ❌ |
| Vector Search | ✅ Qdrant | ❌ VectorStore (weak) | ❌ |
| Archive (LanceDB) | ✅ | ❌ | ❌ |
| Embedding gen | ✅ Google AI | ✅ Google AI (duplicate) | ❌ |
| Ebbinghaus decay | ✅ MicroMemory | ❌ | ✅ memory-store |
| Agent mesh | ❌ | ✅ NeuralMemoryMesh (unique) | ❌ |
| Web Workers | ❌ | ❌ | ✅ Unique |
| Firestore | ❌ | ❌ | ✅ |

## Recommendations

1. **PiWorker-OS** EmbeddingEngine + VectorStore → delete. Use iqra IQRAMemory instead (~127 lines saved)
2. **PiWorker-OS** NeuralMemoryMesh → keep (unique)
3. **GemClaw** memory-store.ts → keep (Firebase-specific, different architecture)
