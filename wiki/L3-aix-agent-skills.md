---
title: "AIX Agent Skills — Marketplace (L3)"
last_updated: "2026-05-16"
status: "stable"
tags: [skills, marketplace, x402, payment, governance]
layer: "L3"
related:
  - "[[stack-overview]]"
  - "[[L2-iqra]]"
  - "[[pi-network]]"
  - "[[x402-plan]]"
---

# AIX Agent Skills — Marketplace (L3)

> ~5,500 lines | 124 skills | x402 payment | Cloudflare Workers

## الرئيسية 6 Flows

### Flow 1: x402 Payment Gateway
```
GET /skills/:name/manifest
→ isPaid(entry)?
  ├── FREE → bypass
  └── PAID → x402 middleware
        → verify X-PAYMENT header
        → 402 if missing, next if verified
→ loadManifest(entry.file) → return manifest
```

### Flow 2: Skill Orchestration (Python CLI)
```
orchestrator.py
→ get_skill_file(skill_name) ← lookup skills.json
→ extract_python(skill_file) ← regex extract
→ subprocess.run(timeout=10s) ← isolated sandbox
→ constitutional authorization
→ per-layer gate → ALLOW/BLOCK
```

### Flow 3: Constitutional Governance (4 Layers)
```
Proposal → {agent_id, action, context, risk_class}
→ Absolute Layer (HaramGuard) → hard BLOCK
→ Interpretive Layer (EthicalFilter) → confidence score
→ Consensus Layer → shura-council
→ persist verdict + reasoning to trust-chain
```

### Flow 4: Skill Quality Evaluation
```
skill-evaluator
→ read manifest → extract I/O → parse dependencies
→ select models → build test cases → sandbox isolation
→ 3x runs per test case → aggregate score 0-100
→ save to .idx/evaluations/{id}/{ver}.json
→ visual badge: eval-pass-87/100
```

### Flow 5: Skills Registry (TypeScript)
```
skills-registry.ts
→ import skills.json → build Map<name, entry>
→ duplicate detection → price validation
→ priceFor(entry) → toPublic(entry)
→ GET /skills → listSkills().map(toPublic)
```

### Flow 6: Go Engine (Parallel Compute)
```
Go engine → parallel_engine.go (worker pool)
→ LID analysis (Local Intrinsic Dimension)
→ Shannon entropy (H_EL Quranic signature)
→ Persistent homology (H0/H1/H2)
→ TurboQuant compression (vector compression)
```

## Skills Marketplace Summary

| القسم | العدد | التفاصيل |
|-------|-------|---------|
| Skills | 124 | عبر 9 layers (L0→L8) |
| Tiers | 6 | SOVEREIGN → ADVANCED_INFRA → PRO → ADVANCED_TOOL → BASIC_TOOL → UNCLASSIFIED |
| Payment | x402 | HTTP 402, USDC على Base + Pi |
| Architecture | Hono | Cloudflare Workers |
| Governance | 4 Layers | Absolute → Interpretive → Consensus → Audit |
| Evaluation | 0-100 | sandbox, 3x runs, badge |
| Go Engine | LID/Shannon/Homology | External microservice |
