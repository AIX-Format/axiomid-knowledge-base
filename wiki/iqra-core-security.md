---
title: "IQRA — Core Runtime & Security Deep Map"
last_updated: "2026-05-16"
status: "stable"
tags: [iqra, core, security, damir, runtime]
layer: "L2"
related:
  - "[[L2-iqra]]"
  - "[[iqra-evolution-llm]]"
  - "[[iqra-reading-status]]"
---

# IQRA — Core Runtime & Security Deep Map

> Group 1 (7,331 lines) + Group 4 (3,003 lines)

## Group 1: Core Runtime (7,331 lines)

### brain.ts (250 lines)
```
iqraThink() → Main IQRA entry point
  ├── CavemanSkill.compressPrompt()  ← 60% linguistic compression
  ├── validateSoulInjection()
  ├── validateInput()                ← Zod validation
  ├── fitrahFilter()                 ← Damir ethical check
  │   └── globalDamir.check()        ← intention → accept/reject
  └── isLocalMode() → true/false
      ├── true  → detectSkill() → executeWithSkill()
      └── false → MissionControl.run()
```

### sovereign_orchestrator.ts (434 lines)
```
MissionControl.run()
  ├── 0. Halting Check (Tawbah — 7+ uncorrected errors)
  ├── classifyMission() → type
  ├── SkillLoader.getSkillContent()
  ├── SovereignCognitiveOrchestrator.explore() ← MCTS + topology
  ├── Search369.evolve() ← I-MCTS pulse
  ├── LeagueManager.adjudicate() ← adversarial testing
  ├── FithrahBaseline.verifyAlignment()
  └── 4 phases: Resonance → Research → Validation → Execution
      ← TawbahLoop.run() if FAIL
  └── RewardEngine.grantFromReports()
```

### loop.ts (195 lines)
```
IQRAExecutionLoop.runTask()
  ├── loadState() → .iqra_loop_state
  ├── Every 3 errors → Tasbih Reset
  ├── Every 7 cycles → extractWisdom() + EvolutionCycle
  └── Every 40 cycles → Topological Flood
```

### reason_act_loop.ts (677 lines)
7-Phase Cognitive Cycle: Observe → Retrieve Memory → Reason → Validate → Execute → Reflect → Save Pattern

### 02-workers/ (1,819 lines)
SovereignWorker (abstract) + 4 Implementations:
- ResonanceWorker → Initial analysis
- ResearchWorker → Deep research
- ValidationWorker → Strict verification
- ExecutionWorker → Final execution

## Group 4: Security & Ethics (3,003 lines)

### damir_conscience.ts (441 lines) — The Heart
```
DamirConscience
  ├── check(action) → ConscienceVerdict
  │   ├── _checkIntention()  ← FORBIDDEN_INTENTIONS
  │   ├── Tawheed trinity    ← Rabb, Malik, Ilah
  │   └── _checkResource()   ← consumed? fake?
  ├── execute(action) → boolean
  ├── reset() → Tawbah
  └── report() → stats (integrity_score)
```

### security.ts (491 lines) — TrustChain + Circuit Breaker
- TrustChain: SHA-256 append-only
- Circuit Breaker: 3 failures → OPEN, 60s → HALF_OPEN
- Tasbih Triplet: 3 internal resets
- Sab'iyyah Wisdom: every 7 cycles
- Barakah Report: every 700 successes → ×2
- Humility Threshold: 9 failures → ASK_HUMAN.md

### byzantine_filter.ts (75 lines)
- Z-Score > 3.0 = anomaly
- Topological break > 0.4 = deviation

### forbidden_patterns.ts (316 lines) — 13 Patterns
4 Categories: SECURITY (critical), ETHICAL (high), SYSTEM (medium), DATA (low)

### damir_kernel.ts (255 lines) — 7 Meta-Loops
Loops named after Quran chapters: Al-Fatiha, Yasin, Al-Kahf, Ar-Rahman, Al-Waqiah, Al-Mulk, Al-Ikhlas

### contracts.ts (353 lines) — Worker Constraints
- VALIDATOR: cannot modify code
- REPORTER: cannot write code
- BUILDER: cannot self-approve
- RESEARCHER: cannot decide reward alone
- PLANNER: cannot implement

### did.ts (307 lines) — Ed25519 DID
SovereignDID.generateBundle(), fromPrivateKey(), generateGitHubDID(), rotateKeys()

### Integration: MissionControl → Security
```
MissionControl.run()
  → ResourceFactory.forWorker()
  → getMissionDamir().check(action)
    → ForbiddenPatternsValidator.validate()
  → ByzantineFilter.detectZScore()
  → appendToTrustChain()
```
