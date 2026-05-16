# 🧬 IQRA — Evolution + LLM + Cognitive + AIX Deep Map

## 5️⃣ Group 5: Evolution (2,674 lines)

### 📍 self_evolve.ts (212 lines)
```
IQRAEvolution.runEvolutionCycle()
  ├── 1. readLog(FAILURES.md) + (REFLECTION.md)
  ├── 2. callEconomyModel() → propose fix
  ├── 3. validateMutation()
  │   ├── dangerousPatterns? → reject
  │   ├── too vague? → reject  
  │   └── constitutionalKeywords? → pass
  └── 4. if critical: GitSkill.pushToBranch() + openPR()
```

### 📍 search_369.ts (212 lines) — I-MCTS
```
Search369.evolve(intention)
  ├── SELECT  ← UCB1 child selection
  ├── EXPAND  ← gemma4Local introspective expansion
  ├── SIMULATE ← DeterministicSandbox + Go Engine (H1, LID, entropy)
  └── BACKPROPAGATE ← hybrid reward (resonance + H1 + LID)
```

### 📍 league_manager.ts (84 lines) — Adversarial
```
LeagueManager.adjudicate(solution)
  ├── Creator → provides solution
  ├── Exploiter (Gemini) → finds holes
  └── Auditor → final verdict (isStable?)
```

### 📍 tawbah_loop.ts (77 lines) — Self-Correction
```
TawbahLoop.run()
  ├── scan TAWBAH.md → uncorrected errors (🛑)
  ├── extractRecentErrors() → top 3
  └── proposeCorrection() → InverseDesign → openPR()
```

### 📍 experience_buffer.ts (579 lines) — CER Memory
```
ExperienceBuffer ← Circular buffer (max 1000)
  ├── add() / addFromReport() ← store experiences
  ├── getRelevantExperiences() ← CER scoring (retention + quality + context + recency)
  ├── forgetStale() ← Ebbinghaus R(t)=e^(-t/S)
  ├── promoteToVerified() ← trust progression
  └── getStats()
```

### 📍 evolution.ts (191 lines) — 7/49 Cycle
```
SovereignEvolution
  ├── runMinorCycle(counter)  ← كل 7: wisdom to WISDOM_7.md
  └── runMajorCycle(counter)  ← كل 49: metamorphosis to METAMORPHOSIS.md
```

### 📍 closed_loop.ts (501 lines) — Self-Training
```
ClosedLoopOrchestrator.runCycle()
  ├── generate() ← failures + curiosity + evolution gaps
  ├── execute() ← Groq/Gemini/local
  ├── review() ← DoctrinalGuard + quality score
  └── export() → SERATrainingPoint
```

---

## 6️⃣ Group 6: LLM + Cognitive (2,482 lines)

### 📍 07-llm/ollama.ts (543 lines)
```
Gemma4Local
  ├── detectModel() → PREFERRED_MODELS: gemma3:1b→llama3.2→gemma4:4b→gemma3:27b
  ├── isAvailable() → /api/tags
  ├── call(messages, tools, maxToolCalls) → 5 IQRA functions
  ├── generate(prompt) → local text
  └── IQRA_LOCAL_TOOLS: get_verse, search_verses, damir_check, get_reward_stats, compute_shannon_hel
```

### 📍 07-llm/groq.ts (132 lines)
```
callGroqForResonance(ayah, data) → Llama 3.3 70B JSON output
callGroqForTruthValidation(ayah, data, resonance) → inverse mirror critic
```

### 📍 07-llm/economy.ts (89 lines) — Multi-Provider Router
```
callEconomyModel(input, context) → tries in order:
  1. Ollama local (highest privacy)
  2. GLM-4.7-Flash (Free Tier)
  3. Qwen-2.5-Coder (Low Cost)
  4. OpenRouter
  5. OpenAI
```

### 📍 07-llm/tools.ts (110 lines)
```
IQRA_TOOLS (5): get_verse, search_verses, damir_check, compute_shannon_hel, get_reward_stats
IQRA_TOOLS_LITE (3): get_verse, search_verses, damir_check
IQRA_QURAN_TOOLS (2): get_verse, search_verses
```

### 📍 08-cognitive/engine.ts (118 lines)
```
SovereignCognitiveOrchestrator.explore(query)
  ├── ArabicAnalyzer.extractRoots() → جذور عربية
  ├── MCTSEngine.run() → self-play simulation
  ├── QuranApiClient.search() → fetch real verses
  ├── SmartTopology.calculateLinguisticBettiNumbers() → H0, H1
  └── SwarmEngine.solve() → PSO optimization
```

### 📍 08-cognitive/swarm.ts (122 lines) — PSO
```
SwarmEngine.solve(focusWords, bettiReward)
  ├── 30% EXPLORER agents + 70% EXPLOITER agents
  ├── Particle Swarm Optimization (inertia + cognitive + social)
  └── Simulated Annealing cooling
```

### 📍 08-cognitive/analyzer.ts (154 lines)
```
ArabicAnalyzer
  ├── removeDiacritics() + tokenize()
  ├── extractRoots() ← dictionary + prefix/suffix stripping
  ├── semanticCoherence() ← Jaccard
  ├── calculatePMI() ← Pointwise Mutual Information
  └── buildWordNetwork() ← PMI-weighted
```

### 📍 08-cognitive/skills/loader.ts (189 lines)
```
SkillLoader
  ├── discovery: IQRA_MARKETPLACE_PATH > ./aix-agent-skills/ > ../aix-agent-skills/ > node_modules/
  ├── loadManifest() → skills.json
  ├── getSkillContent(name) → .md file
  └── read-only (never executes code)
```

---

## 7️⃣ Group 7: AIX Protocol (2,143 lines)

### 📍 14-aix/marketplace_loader.ts (489 lines)
```
MarketplaceLoader ← signed L3 skill retrieval
  ├── fromEnv() → config from env vars
  ├── listSkills() → skills.json
  ├── loadSkill(id) → .md + .sig verification
  ├── SignaturePolicy: off | permissive | strict
  └── Cache: TTL-based in-memory
```

### 📍 14-aix/manifest_exporter.ts (196 lines)
```
exportManifest(input) → AIXManifest (from IQRA primitives)
signManifest(manifest, privateKey) → two-pass signing
verifyManifest(manifest) → checksum + Ed25519
```

### 📍 14-aix/types.ts (237 lines)
```
AIXManifest, AIXMeta, AIXPersona, AIXSecurity, AIXIdentityLayer
AIXTrustChain, AIXEvolution, AIXPiNetwork, AIXAbom
AxiomDID, DID, PublicKey, Signature types
```

---

## 🔗 التكامل بين الـ Groups

```
MissionControl (G1)
    ↓
SkillLoader (G6) ← reads from L3 marketplace
    ↓
SovereignCognitiveOrchestrator (G6) ← MCTS + swarm + topology
    ↓
Search369.evolve() (G5) ← I-MCTS
    ↓
LeagueManager.adjudicate() (G5) ← adversarial test
    ↓
4 Phases (G1) ← each with Damir check (G4)
    ↓
RewardEngine (G1) + ExperienceBuffer (G5)
    ↓
IQRAEvolution (G5) ← auto PR if critical
    ↓
manifest_exporter (G7) → AIX manifest
```

## 🎯 الخلاصة: IQRA جاهز للـ 3 أشياء

1. **Brain Complete** — 7 Loops + MissionControl + Workers = ~7,331 lines قيمة
2. **Security Complete** — Damir + TrustChain + Byzantine = ~3,003 lines فريدة
3. **Evolution Complete** — Self-Evolve + MCTS + League = ~2,674 lines
4. **Marketplace Ready** — SkillLoader + MarketplaceLoader = ~678 lines
5. **Pi Integration Ready** — @axiom/pi موجود، بس يحتاج publish
