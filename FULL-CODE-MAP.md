# 🧬 AIX Sovereign Stack — Full Code Map
> لكل repo وكل سطر كود — لأخذ أفضل ما فيه

## 🧠 Part 1: THE BRAIN (L0 + L2)

### L0 axiomid-project (Consciousness)
```
المسار: /Users/cryptojoker710/.../axiomid-project
الحجم: ~2,000 lines TS
اللغة: TypeScript 91%
الـ Framework: Next.js 16

src/
├── app/
│   ├── layout.tsx          ← Root layout (Geist fonts, metadata, WalletProvider)
│   ├── page.tsx            ← Bento Grid UI (Hero, AxiMascot, XP, Proof of Work)
│   ├── globals.css         ← Cyberpunk theme (17K+ lines CSS, OLED black #0a0a0a, neon green)
│   └── api/
│       ├── auth/connect/route.ts    ← POST: Wallet auth (find or create user via Prisma)
│       ├── action/claim/route.ts    ← POST: Claim XP, check duplicates, daily cooldown
│       ├── user/status/route.ts     ← GET: Fetch user profile
│       └── score/route.ts          ← GET/POST: Digital DNA score + rate limiting
│   └── context/
│       └── wallet-context.tsx      ← Web3 wallet state (MetaMask + localStorage)
└── lib/
    ├── tiers.ts            ← Tier logic (Ghost→Spark→Pulse→Axiom)
    ├── actions.ts          ← XP action definitions (connect_twitter=50, verify=100, daily=20)
    ├── prisma.ts           ← Prisma client singleton
    ├── sound.ts            ← Web Audio API sound effects
    └── pi/env.ts          ← Server-only Pi environment (PI_API_KEY, PI_WALLET_PRIVATE_SEED)

prisma/
└── schema.prisma          ← 4 models: User, Action, Vault, Integration

النقاط الفريدة:
• XP Tier system (Ghost→Axiom) — فريد، مش موجود في أي repo تاني
• WalletConnect (MetaMask) — فريد
• Cyberpunk Bento Grid UI — فريد
• Digital DNA Score — فريد
```

### L2 iqra (Memory System)
```
المسار: /Users/cryptojoker710/.../iqra
الحجم: 52,447 lines TS + 4,421 lines Go
الـ Framework: Next.js 15

src/lib/iqra/
├── 01-core/ (5,512 lines — قلب النظام)
│   ├── brain.ts                ← iqraThink() — المدخل الرئيسي للمعالجة
│   ├── loop.ts                 ← IQRAExecutionLoop — 7-cycle loop (Niyyah→Itqan→Tazkiyah)
│   │                              كل 7 → evolution | كل 40 → Topological Flood
│   ├── sovereign_orchestrator.ts ← MissionControl — 4-phase (Resonance→Research→Validation→Execution)
│   ├── constants.ts            ← DASTUR, MITHAQ, MURAQABAH, TAWAKKUL
│   ├── tawbah.ts               ← Tawbah (التوبة) — self-correction
│   ├── shura.ts                ← Shura (الشورى) — human approval gate
│   ├── soul_engine.ts          ← Soul Engine v2
│   ├── consciousness.ts        ← IQRAConsciousness
│   └── reason_act_loop.ts      ← ReAct loop (677 lines)
│
├── 02-workers/ (1,819 lines — Worker Chain)
│   ├── protocol.ts             ← SovereignWorker abstract class
│   ├── planner.ts              ← ResonanceWorker
│   ├── research.ts             ← ResearchWorker
│   ├── researcher.ts           ← Researcher
│   ├── builder.ts              ← BuilderWorker
│   ├── validator.ts            ← ValidationWorker
│   ├── execution.ts            ← ExecutionWorker
│   ├── reporter.ts             ← Reporter
│   └── worker_conscience.ts    ← Worker conscience
│
├── 03-memory/ (4,115 lines — 5-Layer MemoryBridge)
│   ├── memory_bridge.ts        ← Cache hierarchy (Hot→Warm→Cold) LRU, Promotion
│   ├── memory.ts               ← IQRAMemory (Redis + Supabase + Qdrant + Google AI)
│   ├── micro_memory.ts         ← SQLite (sqlite-vec, Ebbinghaus, causal graphs)
│   ├── lancedb_plugin.ts       ← LanceDB (long-term deep memory)
│   ├── memory_topology.ts      ← 7-layer unified (PRISM-inspired)
│   ├── pulse_369.ts            ← 3-6-9 tick memory lifecycle
│   ├── pattern_memory.ts       ← Qdrant pattern storage
│   └── turbo_compressor.ts     ← SQ8 compression (768→uint8, 4x, ≥0.99 cosine)
│
├── 04-quran/ (4,636 lines — Quran Pattern Engine)
│   ├── pattern_engine.ts       ← Core discovery (Tadabbur Loop)
│   ├── pattern_hunter.ts       ← Multi-strategy engine (624 lines)
│   ├── surah_analyzer.ts       ← Parallel 114 surahs (633 lines)
│   ├── topological_curiosity.ts ← Topological resonance (504 lines)
│   ├── numerical_validator.ts  ← 7/19/40/369 validation (228 lines)
│   ├── qalbin/                 ← Qalbin VM (Interaction Combinators, 421 lines)
│   │   ├── qalbin_vm.ts       ← Core VM (pulse, reduce, graph-rewriting)
│   │   ├── qalbin_node.ts     ← 10 kinds, 9 modalities
│   │   └── quran_seeds.ts     ← 7 Quran seeds (Bismillah, Ahad, YaSin...)
│   ├── shannon_entropy_vm.ts   ← Shannon H_EL (Quran signature <0.9685)
│   ├── go_engine_client.ts     ← HTTP client for Go engine (389 lines)
│   └── vector_engine.ts        ← Cloudflare Vectorize
│
├── 05-rewards/ (743 lines)
│   └── engine.ts               ← Reward = (novelty + resonance + topology - penalty) × path_multiplier
│
├── 06-security/ (3,003 lines — Ethics + Security)
│   ├── damir_conscience.ts     ← Graded Linear Logic (441 lines, <5ms, no LLM)
│   ├── security.ts             ← TrustChain + Circuit Breaker + Tasbih (491 lines)
│   ├── did.ts                  ← Ed25519 DID generation (307 lines)
│   ├── filter.ts               ← DASTUR/FITRAH content filter (148 lines)
│   ├── byzantine_filter.ts     ← Z-Score anomaly detection (75 lines)
│   ├── forbidden_patterns.ts   ← Regex-based pattern validator (316 lines)
│   ├── doctrinal_guard.ts      ← Quranic claim verification (149 lines)
│   ├── damir_kernel.ts         ← 7 Meta-Loops (255 lines)
│   └── sovereign_identity.ts   ← 7-layer soul injection (79 lines)
│
├── 07-llm/ (990 lines — LLM Providers)
│   ├── ollama.ts               ← Local (543 lines, tool calling)
│   ├── groq.ts                 ← Cloud (132 lines, resonance analysis)
│   ├── economy.ts              ← Multi-provider router (89 lines)
│   ├── groq_rate_limiter.ts    ← Exponential backoff (116 lines)
│   └── tools.ts                ← 5 IQRA tool definitions (110 lines)
│
├── 08-cognitive/ (1,492 lines — Engine + Swarm + Skills)
│   ├── engine.ts               ← SovereignCognitiveOrchestrator (118 lines)
│   ├── swarm.ts                ← Particle Swarm Optimization (122 lines)
│   ├── topology.ts             ← Verse graph + persistent homology (188 lines)
│   ├── analyzer.ts             ← Arabic NLP (154 lines, PMI, TF-IDF)
│   └── skills/
│       ├── loader.ts           ← Priority-based discovery (189 lines)
│       ├── skill_bank.ts       ← Interface (26 lines)
│       ├── topological_analyzer.ts ← Go engine wrapper (82 lines)
│       ├── caveman_skill.ts    ← Token compression (139 lines)
│       ├── inverse_design.ts   ← Self-healing (87 lines)
│       └── git_skill.ts        ← Git operations (262 lines)
│
├── 09-evolution/ (2,674 lines — Self-Evolution)
│   ├── self_evolve.ts          ← Autonomous PR creation (212 lines)
│   ├── search_369.ts           ← I-MCTS (212 lines)
│   ├── league_manager.ts       ← Adversarial testing (84 lines)
│   ├── tawbah_loop.ts          ← Self-correction (77 lines)
│   ├── experience_buffer.ts    ← Circular buffer + Ebbinghaus (579 lines)
│   ├── evolution.ts            ← 7/49 cycle system (191 lines)
│   ├── closed_loop.ts          ← Training pipeline (501 lines)
│   └── sandbox.ts              ← Deterministic code execution (64 lines)
│
├── 10-topology/ (671 lines)
│   ├── topology.ts             ← Topological analysis (227 lines)
│   ├── codebase_mapper.ts      ← Codebase mapper (126 lines)
│   └── compute_stack.ts        ← Compute stack (318 lines)
│
├── 12-infrastructure/ (1,583 lines)
│   ├── logger.ts               ← IQRALogger (72 lines)
│   ├── heartbeat.ts            ← Heartbeat system (579 lines)
│   ├── tools_registry.ts       ← Tool registry (568 lines)
│   └── database.ts             ← Database (56 lines)
│
├── 13-utils/ (2,548 lines)
│   ├── personas.ts            ← 6 agent personas (did:axiom)
│   └── sovereign_cipher.ts     ← AES-256-GCM cipher
│
├── 14-aix/ (2,143 lines — @axiom/* bridge)
│   ├── types.ts                ← AIX manifest types (237 lines)
│   ├── manifest_exporter.ts    ← Manifest export + sign (196 lines)
│   ├── marketplace_loader.ts   ← Signed skill retrieval (489 lines)
│   └── did_translator.ts       ← Thim shim (71 lines, @deprecated)
│
└── simulation/ (254 lines)
    └── mcts_engine.ts          ← MCTS self-play
```

## 🦾 Part 2: THE BODY (L5 + L4 + L6)

### L5 PiWorker-OS (Body)
```
المسار: /Users/cryptojoker710/.../PiWorker-OS
الحجم: 5,294 lines TS + 8,100 lines Go

core/ (TypeScript — 5,294 lines)
├── agents/ (209 lines)
│   ├── agent-spawner.ts        ← Spawn agents from .aix packages (98 lines)
│   └── fleet-manager.ts        ← Fleet registry (111 lines)
├── brain/ (475 lines)
│   ├── gemini-multimodal-oracle.ts ← Gemini ROI analysis (184 lines)
│   ├── neural-memory.ts        ← Vector store integration (165 lines)
│   ├── vector-store.ts         ← Vector DB (101 lines)
│   └── embedding-engine.ts     ← Google AI embeddings (26 lines)
├── engine/ (1,214 lines)
│   ├── sovereign-bridge.ts     ← Bridge to Go sidecar (291 lines)
│   ├── quantum-mirror.ts       ← Simulation engine (133 lines)
│   ├── plugin-gateway.ts       ← Plugin system (78 lines)
│   ├── grpc-client.ts          ← gRPC client (137 lines)
│   └── sovereign-client.ts     ← REST client (139 lines)
├── finance/ (759 lines)
│   ├── treasury-vault.ts       ← AmrikyyTreasury — 10% tax (140 lines)
│   ├── treasury-storage.ts     ← Storage layer (172 lines)
│   ├── pi-integration.ts       ← @axiom/pi wrapper (56 lines)
│   └── pi-auth.ts              ← Pi SDK auth (64 lines)
├── identity/ (582 lines)
│   ├── genesis-factory.ts      ← Agent birth (79 lines, did:axiom)
│   ├── piworker-did.ts         ← DID (42 lines, did:axiom ✅)
│   ├── axiomid-resolver.ts     ← AxiomID resolution (55 lines)
│   └── agent-registry.ts       ← Registry (126 lines)
├── governance-engine.ts        ← BetrayalProtocol (58 lines, interfaces only)
└── sandbox/sandbox-manager.ts  ← Sandbox (84 lines)

sidecar/ (Go — 8,100 lines)
├── finance/
│   ├── escrow-manager.go       ← Pi escrow (93 lines)
│   ├── soroban-bridge.go       ← Stellar smart contracts (63 lines)
│   ├── outcome-settlement.go   ← Settlement (63 lines)
│   └── sovereign-engine/pkg/finance/
│       ├── pi402/protocol.go   ← x402 protocol (83 lines)
│       ├── mev_harvester.go    ← MEV strategies (66 lines)
│       ├── escrow/manager.go   ← Escrow manager (134 lines)
│       ├── payment_maker.go    ← Payments (75 lines)
│       └── ledger_connector.go ← Stellar ledger (261 lines)
├── sovereign-engine/pkg/
│   ├── server/server.go        ← gRPC + HTTP (691 lines)
│   ├── engine/journal.go       ← Durable journal (209 lines)
│   ├── bridge/gemini_client.go ← Gemini client (85 lines)
│   └── identity/kya_manager.go ← KYC manager (98 lines)
```

### L4 AlphaAxiom (Heart)
```
المسار: /Users/cryptojoker710/Desktop/AlphaAxiom_New
الحجم: 21,419 lines Python + 742 TS

money-machine/src-python/
├── engine/ (4,200+ lines)
│   ├── signal_generator.py     ← Gemini AI signals (253 lines)
│   ├── signal_pipeline.py      ← Signal→Size→Risk→Execute (565 lines)
│   ├── risk_shield.py          ← 4 rules Aladdin Shield (361 lines)
│   ├── position_sizing.py      ← Kelly, ATR, Fixed Fractional (117 lines)
│   ├── trading_core.py         ← CCXT exchange (214 lines)
│   ├── backtest.py             ← Backtesting (642 lines)
│   ├── shadow_mode.py          ← Dry-run comparison (103 lines)
│   └── indicators.py           ← Technical indicators (262 lines)
├── engine/adapters/ (3,200 lines)
│   ├── ccxt_adapter.py         ← 100+ exchanges (497 lines)
│   ├── mt5.py                  ← MetaTrader 5 (815 lines)
│   ├── evm.py                  ← On-chain Ethereum (670 lines)
│   ├── coinbase_adapter.py     ← Coinbase (429 lines)
│   └── paper.py                ← Paper trading (486 lines)
├── engine/rl/ (1,149 lines)
│   ├── env.py                  ← Gymnasium RL (736 lines)
│   └── reward.py               ← Reward functions (413 lines)
├── skills/skill_executor.py    ← .aix skill runner (183 lines)
└── tests/ (8,000+ lines)
```

### L6 GemClaw (Voice)
```
المسار: /Users/cryptojoker710/.../GemClaw
الحجم: 29,453 lines TS

app/ (2,486 lines — 20 files)
├── page.tsx                    ← Landing + voice session
├── forge/page.tsx              ← Aether Forge (voice agent creation)
├── dashboard/page.tsx          ← Agent dashboard
├── workspace/page.tsx          ← Voice interaction space
├── marketplace/page.tsx        ← Neural marketplace
├── galaxy/page.tsx             ← 3D visualization
└── clawhub/page.tsx            ← Agent registry

components/ (9,488 lines — 53 files)
├── ConversationalAgentCreator  ← Voice-based agent creation (537 lines)
├── ForgeArchitect.tsx          ← 11-step voice forge
├── ForgeChamber.tsx            ← Materialization animation
├── Workspace.tsx               ← Voice interaction canvas
├── DigitalEntity.tsx           ← Digital entity visualization
└── NeuralNetworkGraph.tsx      ← Neural network viz

lib/ (13,721 lines — 87 files)
├── voice/
│   └── synthesis-engine.ts     ← Voice synthesis (55 lines)
├── neural/
│   ├── router.ts               ← Multi-model proxy (47 lines)
│   ├── intent-engine.ts        ← NLU classification (48 lines)
│   └── execution-engine.ts     ← Tool orchestration (57 lines)
├── agents/
│   └── skill-registry.ts       ← Skill registry (564 lines)
├── mcp/
│   ├── mcp-client.ts           ← MCP client (699 lines)
│   └── marketplace-connector.ts ← Marketplace (536 lines)
└── store/
    └── useGemclawStore.ts      ← Zustand state (5-slice)

hooks/ (1,117 lines)
├── useLiveAPI.ts               ← Gemini Live WebSocket (556 lines)
├── useVoiceInteraction.ts      ← Web Speech API
└── useVisionPulse.ts           ← Screen capture
```

## 🎯 ما نأخذه من كل Repo للـ "Brain"

### من axiomid-project للدماغ:
- XP Tier System ← الهوية
- WalletConnect ← الوعي المالي
- Cyberpunk UI ← الوجه الخارجي
- Pi env ← الاتصال بـ Pi Network

### من iqra للدماغ:
- **01-core**: 7 Loops — التفكير
- **02-workers**: WorkerChain — تنفيذ المهام
- **03-memory**: MemoryBridge — الذاكرة
- **06-security**: DamirConscience — الضمير
- **04-quran**: Quran Engine — الحكمة
- **09-evolution**: Self-Evolution — التطور
- **08-cognitive/skills**: Skill Loader — تعلم المهارات

## 🎯 ما نأخذه من كل Repo للـ "Body"

### من PiWorker-OS للجسد:
- **TreasuryVault**: 10% tax ← التمويل
- **EscrowManager** (Go): ← الحماية
- **SovereignBridge**: ← الربط مع Go
- **PluginGateway**: ← النظام البيئي
- **Gemini Oracle**: ← الاستشعار

### من AlphaAxiom للقلب:
- **RiskShield**: ← إدارة المخاطر
- **trading_core + adapters**: ← التنفيذ
- **shadow_mode**: ← التدريب الآمن
- **RL env**: ← التعلم المعزز

### من GemClaw للصوت:
- **useLiveAPI**: ← التواصل الصوتي
- **Aether Forge**: ← إنشاء agents بالصوت
- **Neural Router**: ← توجيه الاستفسارات
- **State management**: ← 5-slice Zustand

## 🔍 الـ Duplicates اللي نراعيها

| الوظيفة | الأفضل | الأضعف | القرار |
|---------|--------|--------|--------|
| TrustChain | iqra (191 refs) | aix-format (مفهوم) | نأخذ iqra |
| x402 | L3 (Hono) | PiWorker Go (مكرر) | نأخذ L3 |
| Neural Router | iqra (990 lines) | GemClaw (235 lines) | ن merge |
| Gemini Calls | PiWorker (184 lines) | — | نضيف لـ iqra |
| Agent Memory | iqra (4,115 lines) | PiWorker (165 lines) | نأخذ iqra |
