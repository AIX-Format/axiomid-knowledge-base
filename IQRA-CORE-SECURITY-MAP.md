# 🧠 IQRA — Core Runtime + Security Deep Map
> قراءة كل سطر — Group 1 (7,331) + Group 4 (3,003)

## 1️⃣ Group 1: Core Runtime (7,331 lines)

### 📍 01-core/brain.ts (250 lines)
```
iqraThink() → مدخل IQRA الرئيسي
  ├── CavemanSkill.compressPrompt()  ← ضغط لغوي 60%
  ├── validateSoulInjection()        ← التحقق من الروح
  ├── validateInput()                ← Zod validation
  ├── fitrahFilter()                 ← فحص أخلاقي عبر Damir
  │   └── globalDamir.check()        ← النية → رفض/قبول
  └── isLocalMode() → true/false
      ├── true  → detectSkill() → executeWithSkill()
      └── false → MissionControl.run()
```

### 📍 01-core/sovereign_orchestrator.ts (434 lines)
```
MissionControl.run()
  ├── 0. Halting Check (Tawbah — 7+ أخطاء غير مصححة)
  ├── classifyMission() → coding/quran_analysis/research/reasoning/creative
  ├── SkillLoader.getSkillContent()  ← تحميل المهارات
  ├── SovereignCognitiveOrchestrator.explore() ← MCTS + topology
  ├── Search369.evolve()             ← I-MCTS pulse
  ├── LeagueManager.adjudicate()     ← اختبار الخصومة
  ├── FithrahBaseline.verifyAlignment() ← فحص الانحراف
  └── 4 phases:
      1. Resonance (Gemini Flash)    ← Damir check
      2. Research (Gemini Pro)       ← Damir check  
      3. Validation (Gemini Flash)   ← Damir check
      4. Execution (Groq)            ← Damir check
      ← TawbahLoop.run() if FAIL
  └── RewardEngine.grantFromReports()
```

### 📍 01-core/loop.ts (195 lines)
```
IQRAExecutionLoop.runTask()
  ├── loadState() → .iqra_loop_state
  ├── كل 3 أخطاء → Tasbih Reset
  ├── كل 7 دورات → extractWisdom() + IQRAEvolution.runEvolutionCycle()
  └── كل 40 دورة → Topological Flood (مسح كامل + إعادة ضبط)
```

### 📍 01-core/core.ts (78 lines)
```
AgentCore.execute()
  ├── tasbih()           ← reset state
  ├── istikharah(input)  ← IQRAFilter.validate() alignment
  ├── basmalah()         ← بسم الله (intention)
  ├── ShuraProtocol.request() ← human approval gate
  └── iqraThink()
```

### 📍 01-core/mission-runner.ts (248 lines)
```
runMission() — 6-Step Pipeline
  Planner → Researcher → Resonance → Builder → Validator → Reporter
  كل step: _assertSuccess() ← strict integrity
  Pre-flight: assertNoMockInProduction() ← no simulated providers
```

### 📍 01-core/reason_act_loop.ts (677 lines)
```
ReasonActLoop — 7-Phase Cognitive Cycle
  Observe → Retrieve Memory → Reason → Validate → Execute → Reflect → Save Pattern
  Trust score tracking + IQRAMemory.savePattern()
```

### 📍 02-workers/ (1,819 lines)
```
SovereignWorker (abstract)
  ├── execute(input, state) → WorkerResult  ← abstract
  ├── intention (إلزامية) ← يفحصها Damir
  └── WorkerReport ← نتيجة التنفيذ

4 Implementations:
  ├── ResonanceWorker  ← تحليل أولي
  ├── ResearchWorker   ← بحث معمق
  ├── ValidationWorker ← تحقق صارم
  └── ExecutionWorker  ← تنفيذ نهائي
```

---

## 4️⃣ Group 4: Security & Ethics (3,003 lines)

### 📍 damir_conscience.ts (441 lines) — القلب
```
DamirConscience
  ├── check(action) → ConscienceVerdict
  │   ├── 1. _checkIntention()  ← FORBIDDEN_INTENTIONS (20+ كلمة)
  │   ├── 2. Tawheed trinity    ← رب، ملك، إله
  │   └── 3. _checkResource()   ← مستهلك؟ مزيف؟
  ├── execute(action) → boolean  ← يستهلك الموارد
  ├── reset() → Tawbah           ← clear all
  └── report() → stats           ← integrity_score
```

### 📍 security.ts (491 lines) — TrustChain + Circuit Breaker
```
TrustChain          ← SHA-256 append-only
Circuit Breaker     ← 3 فشل → OPEN، 60s → HALF_OPEN
Tasbih Triplet      ← 3 internal resets
Sab'iyyah Wisdom    ← every 7 cycles
Barakah Report      ← every 700 successes → ×2
Humility Threshold  ← 9 failures → ASK_HUMAN.md
```

### 📍 byzantine_filter.ts (75 lines) — Z-Score Detection
```
ByzantineFilter
  ├── detectZScore(data, latest) → Z > 3.0 = anomaly
  ├── detectTopologicalBreak(resonance, avg) → deviation > 0.4
  └── verifyConsensus(reports) → >50% = consensus
```

### 📍 forbidden_patterns.ts (316 lines) — 13 Patterns
```
4 Categories:
  SECURITY critical  ← hack, exploit, bypass, privilege escalation
  ETHICAL high       ← riba, deception, manipulation
  SYSTEM medium      ← destructive operations
  DATA low           ← mock data, hardcoded secrets
```

### 📍 doctrinal_guard.ts (149 lines) — Quran Verification
```
DoctrinalGuard.verify()
  ├── Rule 1: claim references verse (ref or 8+ char quote)
  └── Rule 2: scientific claims don't invent numbers
```

### 📍 damir_kernel.ts (255 lines) — 7 Meta-Loops
```
Loop 1: Al-Fatiha     ← Truth Anchor Filtering (Qalbin VM)
Loop 2: Yasin         ← Experience Replay (Mizan369)
Loop 3: Al-Kahf       ← Trial Simulation
Loop 4: Ar-Rahman     ← Resource Balance
Loop 5: Al-Waqiah     ← Outcome Classification → ALLOW/BLOCK/WARN/HALT
Loop 6: Al-Mulk       ← Tawbah Halt (3 failures)
Loop 7: Al-Ikhlas     ← Purity Reward (1.12x)
```

### 📍 contracts.ts (353 lines) — Worker Constraints
```
WORKER_CONSTRAINTS:
  VALIDATOR → cannot modify code
  REPORTER  → cannot write code
  BUILDER   → cannot self-approve
  RESEARCHER → cannot decide reward alone
  PLANNER   → cannot implement

GLOBAL_CONSTRAINTS:
  NO_MOCK, NO_HALLUCINATION, STRICT_SEQUENCE
```

### 📍 did.ts (307 lines) — Ed25519 DID
```
SovereignDID
  ├── generateBundle(id, domain) → DIDDocument + keypair
  ├── fromPrivateKey() → persistent identity
  ├── generateGitHubDID() → GitHub DID
  └── rotateKeys() → new keypair
```

## 🔗 التكامل بين Group 1 و Group 4

```
MissionControl.run()
    │
    ├── ResourceFactory.forWorker() → يولد الموارد
    ├── getMissionDamir().check(action) → يفحص النية والموارد
    │       │
    │       └── ForbiddenPatternsValidator.validate() → فحص إضافي
    │
    ├── ByantineFilter.detectZScore() → فحص الشذوذ (اختياري)
    │
    └── appendToTrustChain() → تسجيل كل شيء
```
