---
title: "10-Hour Execution Plan"
last_updated: "2026-05-16"
status: "in-progress"
tags: [plan, execution, timeline]
layer: "all"
related:
  - "[[roadmap]]"
  - "[[implementation-roadmap]]"
  - "[[brain-build-plan]]"
---

# 10-Hour Execution Plan

> خطة تنفيذ كاملة — Hour by Hour.

## 🕐 Hour 1-2: Package Unification

### Task 1.1 — Unify Versions (15 min)
- All @axiom/* packages → v0.1.0

### Task 1.2 — Fix tsconfig (20 min)
- Add `types: ["node"]` to each package

### Task 1.3 — npm install (30 min)
- `cd packages/$pkg && npm install --silent`

### Task 1.4 — Build (30 min)
- `npx tsc` for each package

## 🕐 Hour 3-4: Brain — iqra Integration

### Task 2.1 — iqra ← @axiom/identity (30 min)
- Replace `#aix/ed25519_signer` with `@axiom/identity`
- Delete shim files (ed25519_signer.ts, canonical.ts)

### Task 2.2 — Gemini Provider (40 min)
- New file: `iqra/07-llm/gemini.ts`
- Source: PiWorker-OS gemini-multimodal-oracle.ts (184 lines)

### Task 2.3 — BetrayalProtocol (30 min)
- New file: `iqra/06-security/betrayal_integration.ts`
- Wraps DamirConscience + ByzantineFilter

## 🕐 Hour 5-6: Body — PiWorker-OS + Cross-Repo

### Task 3.1 — Update package.json (15 min)
- Remove @axiom/pi dep (not yet published)
- Revert to standalone pi-integration

### Task 3.2 — PiWorker-OS ← iqra LLM (30 min)
- Connect to iqra Gemini provider

### Task 3.3 — PiWorker-OS ← iqra Memory (20 min)
- Use IQRAMemory instead of standalone VectorStore

### Task 3.4 — Clean PiWorker-OS (30 min)
- Remove: governance-engine.ts, bounty-scanner.ts, order-ingestion.ts, google-connector.ts, social-bridge.ts

## 🕐 Hour 7-8: Deployment + Publish

### Task 4.1 — npm publish (45 min)
```
Publish order:
1. @axiom/schema (no deps)
2. @axiom/identity (depends on schema)
3. @axiom/pi (standalone)
4. @axiom/validate (depends on schema)
5. @axiom/lint (standalone)
6. @axiom/health (standalone)
7. @axiom/autofix (standalone)
```

### Task 4.2 — Pi Domain Claim Guide (15 min)
### Task 4.3 — Vercel Verification (15 min)

## 🕐 Hour 9-10: Knowledge Base + Documentation

### Task 5.1 — AGENTS.md per repo (30 min)
### Task 5.2 — Update KB (30 min)
### Task 5.3 — Final Review (30 min)

## Summary

| Hour | Task | Outputs |
|------|------|---------|
| 1-2 | Package Unification | 7 packages @ 0.1.0, built |
| 3-4 | Brain: iqra | @axiom/identity, Gemini, BetrayalProtocol |
| 5-6 | Body: PiWorker-OS | Cross-repo integrations + cleanup |
| 7-8 | Deploy + Publish | npm publish, Pi claim, Vercel |
| 9-10 | Knowledge Base | All docs updated |
