# AIX Pi Network — Single App Deployment
> تطبيق واحد على Pi Network، 7 repos في الخلفية

## الـ Architecture على Pi Network

```
Pi Browser → https://axiomid.app (Vercel — واحد فقط)
                              │
                  ┌───────────┴───────────┐
                  │   Unified Dashboard    │
                  │    (Command Center)    │  ← L0: axiomid-project
                  │   Pi SDK Auth + XP     │
                  └───────────┬───────────┘
                              │
          ┌───────────────────┼───────────────────┐
          │                   │                   │
          ▼                   ▼                   ▼
   ┌──────────────┐   ┌──────────────┐   ┌──────────────┐
   │ @axiom/*     │   │ API Routes   │   │ External     │
   │ npm packages │   │ (in Vercel)  │   │ Services     │
   │ (L1)         │   │              │   │              │
   │ identity     │   │ /api/iqra/*  │   │ L3 x402 gw   │
   │ schema       │   │ /api/trade/* │   │ (Cloudflare) │
   │ pi-kyc       │   │ /api/voice/* │   │ L5 Go engine │
   └──────────────┘   └──────────────┘   └──────────────┘
```

## الوضع الحالي — axiomid.app ✅

**تم بالفعل**:
- [x] `public/validation-key.txt` — موجود
- [x] `vercel.json` headers — مضبوط (Content-Type: text/plain)
- [x] `DEPLOYMENT_GUIDE.md` — توثيق كامل
- [x] Pi SDK integration في `src/lib/pi/`

## المطلوب — الخطوات القادمة

### 1. Pi Developer Portal

- [ ] تسجيل الدخول في [Pi Developer Portal](https://pi-apps.developer portal)
- [ ] إنشاء Project باسم **AIX Sovereign Stack**
- [ ] النطاق: `axiomid.app`

### 2. إضافة Subdomains (اختياري)

كل satellite ممكن يكون subdomain منفصل:
- `app.axiomid.app` → PiWorker dashboard
- `ai.axiomid.app` → iqra interface  
- `trade.axiomid.app` → AlphaAxiom
- `voice.axiomid.app` → GemClaw

أو كلهم تحت مسار واحد `axiomid.app/*`

### 3. إنشاء `@axiom/pi` Package

دمج 3 ملفات في package واحد:
- `L1/packages/pi-kyc/` → `@axiom/pi`
- `L1/core/pi_kyc_adapter.ts` → `@axiom/pi`
- `PiWorker-OS/core/finance/pi-auth.ts` → `@axiom/pi`
- `axiomid-project/src/lib/pi/` → `@axiom/pi`

الـ API الموحّدة:
```typescript
// @axiom/pi
authenticateUser(scopes)       // Pi SDK login
verifyKyc(authResult)           // KYC proof + DID  
createPayment(tx, wallet)       // Pi payment
handleIncompletePayments(cb)    // incomplete payment handler
```

### 4. تفعيل Sandbox

- [ ] كل app: `NEXT_PUBLIC_PI_SANDBOX=true`
- [ ] Authorize Sandbox في Pi Mining App
- [ ] اختبار auth + payment + KYC

### 5. Production Go-Live

- [ ] `NEXT_PUBLIC_PI_SANDBOX=false`
- [ ] توليد API Keys لكل app
- [ ] ربط Mainnet wallet
- [ ] اختبار شامل

## تنبيهات Pi Network مهمة

- `validation-key.txt` **ليس سراً** — هو hash عام من Pi Developer Portal
- ممنوع خزن `PI_API_KEY` أو `PI_WALLET_PRIVATE_SEED` في client-side (server-only)
- كل payment يحتاج 3 callbacks: `onReadyForServerApproval`, `onReadyForServerCompletion`, `onCancel`
