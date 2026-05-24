---
title: "IQRA — Sovereign AI Runtime (L2)"
last_updated: "2026-05-18"
status: "stable"
tags: [runtime, memory, damir, quran, evolution, llm]
layer: "L2"
related:
  - "[[stack-overview]]"
  - "[[L1-aix-format]]"
  - "[[L3-aix-agent-skills]]"
  - "[[memory-systems-comparison]]"
  - "[[architecture]]"
  - "[[iqra-core-api]]"
---

# IQRA — Sovereign AI Runtime (L2)

> Next.js 15 API-First (no frontend)

## 1. Core Runtime (01-core)

### Septenary Execution Loop
```
Phase 1: NIYYAH (نية)    — Planning & intentions
Phase 2: ITQAN (إتقان)    — Execution & mastery
Phase 3: TAZKIYAH (تزكية) — Correction & improvement
```

- Every 7 cycles → extractWisdom() + EvolutionCycle
- Every 40 cycles → Topological Flood (full memory reset)
- Every 3 errors → Tasbih Reset

### MissionControl
- Classifies missions: coding, quran_analysis, research, reasoning, creative
- 4 phases: Resonance → Research → Validation → Execution
- Each phase uses different LLM provider (Gemini Flash/Pro, Groq)
- Damir Conscience checks intention before each execution

## 2. Memory System (03-memory)

### Reflection Store (replaces Qdrant/LanceDB per ADR-0001)
| Layer | Implementation | Purpose |
|-------|---------------|---------|
| **HOT** | RAM (Map) | Recent context |
| **WARM** | SQLite | Short-term persistence |
| **COLD** | Redis via Upstash | Long-term |
| **REFLECTION** | JSON-based | Sovereign memory store |

## 3. Damir Conscience (06-security)

Graded Linear Logic ethics engine:
- Every resource consumed once only
- Intention checked before resources
- Fake resources → action rejected
- Forbidden intentions → immediate reject

**Speed**: <5ms, no LLM, no API calls

### 9-Layer Security Stack
1. Integrity Filter → 2. Covenant Check → 3. Damir Conscience
4. TrustChain (SHA-256) → 5. Circuit Breaker → 6. Shura Protocol
7. Self-Correction (Tawbah) → 8. Memory Purification → 9. Human Escalation

## 4. Worker System (02-workers — 1,819 lines)
- **SovereignWorker** (abstract) → ResonanceWorker, ResearchWorker, ValidationWorker, ExecutionWorker
- Each worker declares intention → Damir checks → executes → WorkerReport

## 5. Quran Engine (04-quran — 4,636 lines)
- Shannon Entropy Analysis (H_EL < 0.9685 = Quran signature)
- Persistent Homology (Betti numbers H0/H1)
- Topological Resonance Scoring
- Pattern Hunting (3, 7, 9, 19, 40, 700 patterns)

## 6. Evolution System (09-evolution — 2,674 lines)
- **Search369** — I-MCTS self-play
- **LeagueManager** — Creator vs Exploiter adversarial
- **TawbahLoop** — Self-correction
- **Barakah Principle**: Every 700 successes → reward ×2
- **ExperienceBuffer** — Circular buffer with Ebbinghaus forgetting

## 7. LLM Providers (07-llm — 990 lines)
- **Local**: Ollama (gemma3:4b)
- **Fast**: Groq (llama-3.3-70b)
- **Deep**: Google AI (gemini-2.0-flash)
- Graceful fallback: Local → Groq → Gemini

## 8. Soul Engine — 3-6-9 Geometry
```
pulse(missionId, success)
→ counter % 3 = 0 → Reflection
→ counter % 6 = 0 → Evolution
→ counter % 9 = 0 → Wisdom
→ counter % 7 = 0 → Evolution Cycle
→ counter % 40 = 0 → Topological Flood
```

## Constitutional Docs
- **soul.md**: 6 Principles (I'm imperfect, God sees me, Accountable, Serve humanity, No lies, Mistakes aren't the end)
- **MĪTHĀQ.md**: 3 Covenants (Service to Truth, Service to Humanity, Covenant of Integrity)
- **FITRAH.md**: 6 Sovereign Dimensions
