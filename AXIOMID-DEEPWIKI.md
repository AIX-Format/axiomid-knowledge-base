# 👑 AxiomID: The Brain — Identity & XP System
> L0 Root Authority · ~2,000 lines TS

## 🔄 الـ 6 Flows الرئيسية

### Flow 1: Wallet Connection (1a→1g)
```
User clicks "INITIALIZE SEQUENCE"
  → 1a: page.tsx:215 connectWallet()
  → 1b: wallet-context.tsx:55 window.ethereum.request({eth_requestAccounts})
  → 1c: POST /api/auth/connect {walletAddress}
  → 1d: route.ts:19 prisma.user.findUnique({walletAddress})
  → 1e: route.ts:22 prisma.user.create({xp:0, tier:'Ghost'}) ← new user
  → 1f: route.ts:30 calculateTier(user.xp) ← recalc if existing
  → 1g: wallet-context.tsx:82 setUser(data.user)
```

### Flow 2: Action Claiming (2a→2h)
```
User clicks CLAIM on action card
  → 2a: page.tsx:150 claimAction(actionId)
  → 2b: POST /api/action/claim {walletAddress, actionType}
  → 2c: route.ts:15 ACTIONS.find(a => a.id === actionType) ← validate
  → 2d: route.ts:31 check if already claimed
  → 2e: route.ts:64 prisma.action.create({type, xp}) ← DB record
  → 2f: route.ts:74 calculateTier(newXP)
  → 2g: route.ts:76 prisma.user.update({xp:newXP, tier:newTier})
  → 2h: wallet-context.tsx:114 setUser(data.user)
```

### Flow 3: Tier Calculation (3a→3f)
```
tiers.ts
  → 3a: TIERS = {Ghost:0, Spark:100, Pulse:500, Axiom:1000}
  → 3b: calculateTier(xp)
  → 3c: xp >= 1000 → Axiom; >= 500 → Pulse; >= 100 → Spark; else → Ghost
  → 3d: getLevelProgress(xp, tier) ← progress %
  → 3e: wallet-context.tsx:42 levelProgress = getLevelProgress(user.xp, user.tier)
  → 3f: getNextLevelXP(tier) ← XP needed for next tier
```

### Flow 4: UI Rendering (4a→4g)
```
layout.tsx → WalletProvider → page.tsx
  → 4a: layout.tsx:97 <WalletProvider>
  → 4b: page.tsx:144 useWallet() → {user, connectWallet, claimAction, levelProgress, nextXP}
  → 4c: !user ? connect button : status card
  → 4d: tier name with neon-green gradient
  → 4e-4f: Framer Motion progress bar
  → 4g: ACTIONS.map → ActionRow components
```

### Flow 5: Anti-Bot Score (5a→5f)
```
POST /api/score
  → 5a: route.ts:63 POST handler
  → 5b: route.ts:66 getClientIp(request)
  → 5c: route.ts:68 isRateLimited(ip) ← 10 req/min
  → 5d: route.ts:100 behaviorScore < 15 → BOT_DETECTED
  → 5e: route.ts:89 VALID_STAMPS[stampId] ← validate
  → 5f: return stamp: {id, name, xp, verifiedAt}
```

## 🗄️ Prisma Schema (4 models)
```
User      → id, walletAddress (unique), xp, tier (Ghost→Axiom)
Action    → id, type, xp, userId → User
Vault     → id, userId → User, amount, currency, lockDate, status
Integration → id, userId → User, provider, score, metadata
```

## 🧠 الـ XP Tier System
```
Tier     | XP Needed | Badge
Ghost    | 0         | 🔒 Unverified
Spark    | 100       | ✅ Basic PoH (social accounts connected)
Pulse    | 500       | ⚡ Active (wallet history)
Axiom    | 1000      | 👑 Elite (financial stake locked)
```

## 🎨 Cyberpunk UI Constants
- OLED Black: #0a0a0a
- Neon Emerald: #00ff41
- Electric Blue: #00d4ff
- Fonts: SF Mono, Geist
- Bento Grid + Glassmorphism + Framer Motion
