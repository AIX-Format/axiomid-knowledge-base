---
title: "AxiomID — Root Authority (L0)"
last_updated: "2026-05-16"
status: "stable"
tags: [identity, xp, wallet, axiomid]
layer: "L0"
related:
  - "[[stack-overview]]"
  - "[[L1-aix-format]]"
  - "[[pi-network]]"
  - "[[changelog]]"
---

# AxiomID — Root Authority (L0)

> ~2,000 lines TS | Next.js 16 + Prisma

## Core Flows

### Flow 1: Wallet Connection
```
User clicks "INITIALIZE SEQUENCE"
→ connectWallet() → window.ethereum.request()
→ POST /api/auth/connect {walletAddress}
→ prisma.user.findUnique/create({xp:0, tier:'Ghost'})
→ calculateTier(xp) → setUser(data.user)
```

### Flow 2: Action Claiming
```
User clicks CLAIM → POST /api/action/claim
→ ACTIONS.find(a => a.id === actionType)
→ check duplicate + daily cooldown
→ prisma.action.create({type, xp})
→ calculateTier(newXP) → update user
```

### Flow 3: Tier Calculation
```
TIERS = {Ghost:0, Spark:100, Pulse:500, Axiom:1000}
calculateTier(xp):
  xp >= 1000 → Axiom
  xp >= 500 → Pulse
  xp >= 100 → Spark
  else → Ghost
```

### Flow 4: Anti-Bot Score
```
POST /api/score
→ getClientIp(request) → isRateLimited(ip) ← 10 req/min
→ behaviorScore < 15 → BOT_DETECTED
→ VALID_STAMPS[stampId] → validate
```

## Prisma Schema (4 models)
- **User**: id, walletAddress, xp, tier
- **Action**: id, type, xp, userId → User
- **Vault**: id, userId → User, amount, currency, lockDate
- **Integration**: id, userId → User, provider, score

## XP Tier System
| Tier | XP | Badge |
|------|-----|-------|
| Ghost | 0 | Unverified |
| Spark | 100 | Basic PoH |
| Pulse | 500 | Active |
| Axiom | 1000 | Elite |

## Cyberpunk UI
- OLED Black: #0a0a0a, Neon Emerald: #00ff41, Electric Blue: #00d4ff
- Fonts: SF Mono, Geist | Bento Grid + Glassmorphism + Framer Motion
- Deployed at **axiomid.app** on Vercel ✅

انظر [[pi-network]] لتكامل Pi، و [[L1-aix-format]] للبروتوكول.
