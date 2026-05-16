---
title: "Pi Network — Integration & Deployment Plan"
last_updated: "2026-05-16"
status: "stable"
tags: [pi-network, deployment, domain-claim, validation-key]
layer: "L0,L5"
related:
  - "[[L0-axiomid]]"
  - "[[L5-piworker-os]]"
  - "[[L1-aix-format]]"
  - "[[roadmap]]"
---

# Pi Network — Integration & Deployment

> تطبيق واحد على Pi Network، 7 repos في الخلفية.

## Architecture on Pi Network

```
Pi Browser → https://axiomid.app (Vercel — one app only)
                        │
            ┌───────────┴───────────┐
            │   Unified Dashboard    │  ← L0: axiomid-project
            │   Pi SDK Auth + XP     │
            └───────────┬───────────┘
                        │
        ┌───────────────┼───────────────┐
        │               │               │
        ▼               ▼               ▼
 ┌──────────────┐ ┌──────────────┐ ┌──────────────┐
 │ @axiom/*     │ │ API Routes   │ │ External     │
 │ npm packages │ │ (in Vercel)  │ │ Services     │
 └──────────────┘ └──────────────┘ └──────────────┘
```

## Current Status — axiomid.app ✅

- [x] `public/validation-key.txt` — موجود
- [x] `vercel.json` headers — مضبوط (Content-Type: text/plain)
- [x] DEPLOYMENT_GUIDE.md — توثيق كامل
- [x] Pi SDK integration في `src/lib/pi/`

## Required Steps

### 1. Pi Developer Portal
- [ ] تسجيل الدخول في Pi Developer Portal
- [ ] إنشاء Project باسم **AIX Sovereign Stack**
- [ ] النطاق: `axiomid.app`

### 2. Subdomains (Optional)
- `app.axiomid.app` → PiWorker dashboard
- `ai.axiomid.app` → iqra interface
- `trade.axiomid.app` → AlphaAxiom
- `voice.axiomid.app` → GemClaw

### 3. @axiom/pi Package — Unified API
```typescript
authenticateUser(scopes)       // Pi SDK login
verifyKyc(authResult)           // KYC proof + DID
createPayment(tx, wallet)       // Pi payment
handleIncompletePayments(cb)    // incomplete payment handler
```

### 4. Sandbox Activation
- [ ] `NEXT_PUBLIC_PI_SANDBOX=true`
- [ ] Authorize Sandbox in Pi Mining App
- [ ] Test auth + payment + KYC

### 5. Production Go-Live
- [ ] `NEXT_PUBLIC_PI_SANDBOX=false`
- [ ] Generate API Keys per app
- [ ] Connect Mainnet wallet
- [ ] Full testing

## Important Notes
- `validation-key.txt` is NOT a secret — public hash from Pi Developer Portal
- NEVER store `PI_API_KEY` or `PI_WALLET_PRIVATE_SEED` client-side
- Every payment needs 3 callbacks: `onReadyForServerApproval`, `onReadyForServerCompletion`, `onCancel`
