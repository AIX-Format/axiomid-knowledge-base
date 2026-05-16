# 🦾 AIX Agent Skills Marketplace (L3) — Payment, Orchestration & Governance
> L3 Marketplace · ~5,500 lines

## 🔄 الـ 6 Flows الرئيسية

### Flow 1: x402 Payment Gateway (Cloudflare Worker) 1a→1g
```
HTTP GET /skills/:name/manifest
  → 1a: app.use('/skills/:name/manifest', middleware)
  → 1b: getSkill(name) ← lookup
  → 1c: isPaid(entry)?
      ├── FREE → next() bypass
      └── PAID → paymentMiddleware(x402)
            → 1d: wallet validation + price resolution + facilitator config
            → 1e: verify X-PAYMENT header
                  → 402 if missing
                  → next if verified
  → 1f: loadManifest(entry.file) ← .md content
  → 1g: return c.body(body) ← stream manifest
```

### Flow 2: Skill Orchestration (Python CLI) 2a→2f
```
orchestrator.py
  → 2a: run_skill(skill_name, inputs_json)
  → 2b: get_skill_file(skill_name) ← lookup in skills.json
  → 2c: extract_python(skill_file) ← regex ```python\n(.*?)```
  → 2d: subprocess.run(timeout=10s) ← isolated sandbox
  → 2e: constitutional authorization ← verify covenant signature
  → 2f: per-layer gate ← consult sovereign-constitution → ALLOW/BLOCK
```

### Flow 3: Constitutional Governance (4 Layers) 3a→3f
```
Proposal → {agent_id, action, context, risk_class}
  → 3a: receive proposal
  → 3b: hash → ConstitutionDB ← binding precedent?
  → 3c: Absolute Layer (HaramGuard) → hard BLOCK if violated
  → 3d: Interpretive Layer (EthicalFilter) → 4-question consultation → confidence score
  → 3e: Consensus Layer → escalate → shura-council (if ambiguous/red-class)
  → 3f: persist verdict + reasoning to trust-chain (immutable ledger)
```

### Flow 4: Skill Quality Evaluation 4a→4g
```
skill-evaluator
  → 4a: read manifest → extract I/O → parse dependencies
  → 4b: select models via model-council → build test cases → assertions
  → 4c: skill-sandbox isolation
  → 4d: 3x runs per test case (statistical reliability)
  → 4e: aggregate score 0-100
  → 4f: save to .idx/evaluations/{id}/{ver}.json
  → 4g: visual badge: eval-pass-87/100-brightgreen
```

### Flow 5: Skills Registry (TypeScript) 5a→5g
```
skills-registry.ts
  → 5a: import skills.json
  → 5b: build Map<name, entry>
  → 5c: duplicate detection
  → 5d: price_usdc validation
  → 5e: priceFor(entry) → price resolution
  → 5f: toPublic(entry) → public projection
  → 5g: GET /skills → listSkills().map(toPublic)
```

### Flow 6: Go Engine (Parallel Compute) 6a→6f
```
Go engine (external microservice)
  → 6a: main.go ← HTTP server
  → 6b: parallel_engine.go ← worker pool
  → 6c: LID analysis ← Local Intrinsic Dimension
  → 6d: Shannon entropy ← H_EL Quranic signature
  → 6e: Persistent homology ← topological analysis H0/H1/H2
  → 6f: TurboQuant compression ← vector compression
```

## 📊 Skills Marketplace Summary
| القسم | العدد | التفاصيل |
|-------|-------|---------|
| Skills | 59 | عبر 9 layers (L0→L8) |
| Tiers | 6 | SOVEREIGN → ADVANCED_INFRA → PRO → ADVANCED_TOOL → BASIC_TOOL → UNCLASSIFIED |
| Payment | x402 | HTTP 402, USDC على Base |
| Architecture | Hono | Cloudflare Workers |
| Governance | 4 Layers | Absolute → Interpretive → Consensus → Audit |
| Evaluation | 0-100 | sandbox, 3x runs, badge |
| Go Engine | LID/Shannon/Homology/Compression | External microservice |
