---
title: "AIX Sovereign Stack — Overview"
last_updated: "2026-05-16"
status: "stable"
tags: [stack, architecture, layers, overview]
layer: "all"
related:
  - "[[architecture]]"
  - "[[human-body-architecture]]"
  - "[[L0-axiomid]]"
  - "[[L1-aix-format]]"
  - "[[L2-iqra]]"
  - "[[L3-aix-agent-skills]]"
  - "[[L4-alphaaxiom]]"
  - "[[L5-piworker-os]]"
  - "[[L6-gemclaw]]"
---

# AIX Sovereign Stack — Overview

> Codename: Echo369 | Spec: AIX/1.0 | v0.369.0

## الـ 7 Repos والـ Layers

```
L0 . axiomid-project  (Root Authority)      → Next.js 16 + Prisma + XP/Tier
L1 . aix-format       (Protocol/DNA)         → @axiom/* packages + schema
L2 . iqra             (Runtime/Brain)        → 7 Loops + Damir + Quran Engine
L3 . aix-agent-skills (Marketplace/Hands)    → 59 skills, x402 pay-per-request
L4 . AlphaAxiom      (Trading/Heart)        → Python trading engine
L5 . PiWorker-OS     (Pi Treasury/Body)     → TS + Go escrow
L6 . GemClaw         (Voice)                → Gemini Live + Aether Forge
```

## مبدأ التشغيل الأساسي

- **Money flows up**: Satellites (L4-L6) → L3 → L1
- **Identity flows down**: L0 → L1 → L2 → L3 → L4/L5/L6
- **Trust flows central**: L2 (iqra) TrustChain يسجل كل عملية
- **One-way dependency**: L3 → L2 → L1 (ممنوع reverse imports)

## لغة كل Repo

| Repo | اللغة الأساسية | Framework |
|------|---------------|-----------|
| axiomid-project | TypeScript (91%) | Next.js 16 |
| aix-format | TypeScript (52%) + Rust (6%) | pnpm monorepo |
| iqra | TypeScript (86%) + Go (5%) | Next.js 15 |
| aix-agent-skills | Python (66%) + TS (16%) | — |
| AlphaAxiom | Python (94%) | Tauri + Next.js |
| PiWorker-OS | TypeScript (42%) + Go (39%) | Next.js 15 + Go |
| GemClaw | TypeScript (95%) | Next.js 15 + Firebase |

## Deployment Status

- **axiomid.app** → deployed ✅ (Vercel, Node 22.x)
- **validation-key.txt** → working ✅
- **aitrading.axiomid.app** → AlphaAxiom dashboard ✅
- **@axiom/identity v1.3.0** → built ✅
- **@axiom/schema v1.3.0** → built ✅
- **@axiom/pi v0.1.0** → built ✅

انظر [[architecture]] للتفاصيل المعمارية، و [[roadmap]] للخطوات القادمة.
