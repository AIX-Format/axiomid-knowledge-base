---
title: "IQRA — Evolution + LLM + AIX Protocol"
last_updated: "2026-05-16"
status: "stable"
tags: [iqra, evolution, llm, protocols, cognitive]
layer: "L2"
related:
  - "[[L2-iqra]]"
  - "[[iqra-core-security]]"
  - "[[iqra-reading-status]]"
---

# IQRA — Evolution + LLM + AIX Protocol

> Group 5 (2,674 lines) + Group 6 (2,482 lines) + Group 7 (2,143 lines)

## Group 5: Evolution (2,674 lines)

### self_evolve.ts (212 lines)
```
IQRAEvolution.runEvolutionCycle()
  → readLog(FAILURES.md + REFLECTION.md)
  → callEconomyModel() → propose fix
  → validateMutation()
    ├── dangerousPatterns? → reject
    ├── too vague? → reject
    └── constitutionalKeywords? → pass
  → if critical: GitSkill.pushToBranch() + openPR()
```

### search_369.ts (212 lines) — I-MCTS
```
Search369.evolve(intention)
  → SELECT (UCB1) → EXPAND (gemma4Local)
  → SIMULATE (DeterministicSandbox + Go Engine)
  → BACKPROPAGATE (hybrid reward: resonance + H1 + LID)
```

### league_manager.ts (84 lines) — Adversarial
Creator → provides solution | Exploiter (Gemini) → finds holes | Auditor → final verdict

### tawbah_loop.ts (77 lines) — Self-Correction
Scan TAWBAH.md → extract uncorrected errors → proposeCorrection() → openPR()

### experience_buffer.ts (579 lines) — CER Memory
Circular buffer (max 1000). CER scoring: retention + quality + context + recency. Ebbinghaus forgetting.

### evolution.ts (191 lines) — 7/49 Cycle
- Every 7: runMinorCycle() → wisdom to WISDOM_7.md
- Every 49: runMajorCycle() → metamorphosis to METAMORPHOSIS.md

### closed_loop.ts (501 lines) — Self-Training
generate() → execute() → review() → export() as SERATrainingPoint

## Group 6: LLM + Cognitive (2,482 lines)

### ollama.ts (543 lines) — Local Provider
- Auto-detect: gemma3:1b → llama3.2 → gemma4:4b → gemma3:27b
- 5 IQRA local tools: get_verse, search_verses, damir_check, get_reward_stats, compute_shannon_hel

### groq.ts (132 lines) — Cloud Provider
- callGroqForResonance() → Llama 3.3 70B JSON
- callGroqForTruthValidation() → inverse mirror critic

### economy.ts (89 lines) — Multi-Provider Router
Priority: Ollama → GLM-4.7-Flash → Qwen-2.5-Coder → OpenRouter → OpenAI

### tools.ts (110 lines)
5 IQRA tools: get_verse, search_verses, damir_check, compute_shannon_hel, get_reward_stats

### cognitive/engine.ts (118 lines)
SovereignCognitiveOrchestrator.explore(): ArabicAnalyzer + MCTS + Quran API + Topology + Swarm

### cognitive/swarm.ts (122 lines) — PSO
30% EXPLORER + 70% EXPLOITER agents. Particle Swarm Optimization + Simulated Annealing.

### cognitive/analyzer.ts (154 lines)
Arabic NLP: removeDiacritics, tokenize, extractRoots, semanticCoherence, PMI, buildWordNetwork

## Group 7: AIX Protocol (2,143 lines)

### marketplace_loader.ts (489 lines)
- fromEnv() → config from env vars
- listSkills() → from skills.json
- loadSkill(id) → .md + .sig verification
- 3 signature policies: off | permissive | strict

### manifest_exporter.ts (196 lines)
- exportManifest() → AIXManifest from IQRA primitives
- signManifest() → two-pass Ed25519 signing
- verifyManifest() → checksum + Ed25519

### types.ts (237 lines)
AIXManifest types: AIXMeta, AIXPersona, AIXSecurity, AIXIdentityLayer, AIXTrustChain, AIXEvolution, AIXPiNetwork, AIXAbom

## Integration Chain
```
MissionControl → SkillLoader → CognitiveOrchestrator → Search369
→ LeagueManager → 4 Phases (Damir check each) → RewardEngine
→ ExperienceBuffer → IQRAEvolution → manifest_exporter → AIX manifest
```

## IQRA Is Ready For
1. **Brain Complete** — 7 Loops + MissionControl + Workers
2. **Security Complete** — Damir + TrustChain + Byzantine
3. **Evolution Complete** — Self-Evolve + MCTS + League
4. **Marketplace Ready** — SkillLoader + MarketplaceLoader
5. **Pi Integration Ready** — @axiom/pi exists, needs publish
