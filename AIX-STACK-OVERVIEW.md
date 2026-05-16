# AIX Sovereign Stack — Overview
> Codename: Echo369 | Spec: AIX/1.0 | v0.369.0

## الـ 7 Repos والـ Layers

```
┌─────────────────────────────────────────────────────────────┐
│  L0 . axiomid-project  (Root Authority)                     │
│  "إثبات البشرية — Sybil-resistant identity"                   │
│  Next.js 16 + Prisma + Web3 Wallet + XP/Tier System        │
├─────────────────────────────────────────────────────────────┤
│  L1 . aix-format  (Protocol)                                │
│  "Universal Agent Passport — JSON-LD manifest standard"     │
│  @axiom/* packages + schema + validation + identity + pi   │
├─────────────────────────────────────────────────────────────┤
│  L2 . iqra  (Runtime)                                       │
│  "Sovereign AI OS — 7 Loops + Damir + MCTS + Quran Engine" │
├─────────────────────────────────────────────────────────────┤
│  L3 . aix-agent-skills  (Marketplace)                        │
│  "59 skills across 9 layers — x402 pay-per-request"        │
├─────┬────────┬────────┬─────────────────────────────────────┤
│ L4  │  L5    │  L6    │  Satellites                         │
│ Alpha│PiWorker│GemClaw │  تشتري skills من L3 عبر x402        │
│ Axiom │-OS    │(Voice) │                                      │
│(Trade)│(Pi)   │        │                                      │
└─────┴────────┴────────┴─────────────────────────────────────┘
```

## مبدأ التشغيل الأساسي

- **Money flows up**: الـ Satellites (L4-L6) يدفعوا لـ L3 عبر x402
- **Identity flows down**: L0 يصدّر `did:axiom:*` لكل الـ layers
- **Trust flows central**: L2 (iqra) TrustChain يسجل كل عملية
- **One-way dependency**: L3 → L2 → L1 (ممنوع reverse imports)

## لغة كل Repo

| Repo | اللغة الأساسية | Framework |
|------|---------------|-----------|
| axiomid-project | TypeScript (91%) | Next.js 16 |
| aix-format | TypeScript (52%) + JS (31%) + Rust (6%) | pnpm monorepo |
| iqra | TypeScript (86%) + Go (5%) | Next.js 15 |
| aix-agent-skills | Python (66%) + TS (16%) + Go (9%) | — |
| AlphaAxiom | Python (94%) | Tauri + Next.js |
| PiWorker-OS | TypeScript (42%) + Go (39%) | Next.js 15 + Go |
| GemClaw | TypeScript (95%) | Next.js 15 + Firebase |

## الملفات الدستورية المشتركة

كل repo عنده نسخة من `AGENTS.md` اللي بتوصف الـ AI agents instructions.
أهم ملف دستوري هو `AXIOM.md` في `aix-format` — الـ Supreme Constitution لكل المنظومة.

## 🚀 Current Deployment Status (2026-05-14)

### axiomid-project (L0)
- **Deployed**: https://axiomid-project.vercel.app ✅
- **Domain**: `axiomid.app` ← needs Vercel Dashboard reassignment ⏳
- **CI/CD**: GitHub Actions (ubuntu-latest) — auto-deploy on push to main
- **validation-key.txt**: Working correctly
- **Vercel Project**: `axiomid-project` (Node 22.x)
- **Env Vars Set**: NEXT_PUBLIC_*, NEXTAUTH_SECRET
- **Needs Manual**: DATABASE_URL, PI_API_KEY, Domain assignment

### Other Repos (Not yet deployed on this session)
- PiWorker-OS — has its own Vercel project (`piworker-os`)
- aix-format — has `aix-format-studio` on Vercel
- AlphaAxiom — has `frontend` on Vercel with `aitrading.axiomid.app`
- GemClaw — not on Vercel yet
- iqra — not on Vercel yet

### Final Status (2026-05-14 23:00)
- **axiomid.app** → deployed ✅ (200 OK)
- **validation-key.txt** → working ✅
- **www.axiomid.app** → redirect needed (307) — can fix later
- **aitrading.axiomid.app** → AlphaAxiom dashboard ✅
- **PI_API_KEY** → user will set manually
