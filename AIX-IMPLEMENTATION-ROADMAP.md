# AIX Implementation Roadmap
> آخر تحديث: 2026-05-15 — بعد جلسة التنظيف العميق

## ✅ تم إنجازه

- [x] **Phase 0** — Dead code: PiWorker-OS sandbox, axiomid-project 3 plan docs, iqra 6 docs
- [x] **Phase 1.1** — `@axiom/pi` package in `aix-format/packages/axiom-pi/`
- [x] **Phase 1.3** — PiWorker-OS DID: `did:piworker` → `did:axiom`
- [x] **Phase 1.5** — PiWorker-OS dependency: `@axiom/pi` added
- [x] **Phase 1.6** — `pi_kyc_adapter.ts` → thin wrapper
- [x] **Phase 5** — `axiomid.app` deployed on Vercel, validation-key.txt works
- [x] **Deep cleanup** — 3 repos: ~500 lines duplicate + 15 outdated docs removed

## ⏳ المتبقي حسب الأولوية

### 🥇 الأولوية العالية (High)

| # | المهمة | الـ Repo | التفاصيل |
|---|--------|----------|---------|
| 1 | **axiomid-project ← @axiom/pi** | axiomid-project | استبدال `src/lib/pi/env.ts` المحلي باستيراد من `@axiom/pi` |
| 2 | **iqra personas → did:axiom** | iqra | 6 default personas: `did:web:axiomid.app:*` → `did:axiom:axiomid.app:*` |
| 3 | **aix-core/infra.ts → @axiom/identity** | aix-format | استبدال `tweetnacl` بـ `@axiom/identity/ed25519` |
| 4 | **PR #198 v1.4.0** | aix-format | مراجعة Greptile concerns واتخاذ قرار |

### 🥈 الأولوية المتوسطة (Medium)

| # | المهمة | الـ Repo | التفاصيل |
|---|--------|----------|---------|
| 5 | **Payment unification (x402)** | PiWorker-OS + L3 | ربط PiWorker-OS بـ L3 x402 gateway بدل EscrowManager |
| 6 | **GemClaw neural router → iqra** | GemClaw + iqra | دمج 4 providers مع iqra LLM |
| 7 | **GemClaw → AxiomClaw** | GemClaw | Rename repo + code references |

### 🥉 الأولوية المنخفضة (Low)

| # | المهمة | الـ Repo | التفاصيل |
|---|--------|----------|---------|
| 8 | **BetrayalProtocol → iqra** | PiWorker-OS + iqra | نقل governance-engine.ts |
| 9 | **AlphaAxiom skills → L3** | AlphaAxiom + L3 | تحويل .aix skills إلى marketplace |
| 10 | **PiWorker-OS x402 Go → L3** | PiWorker-OS + L3 | توحيد x402 protocol |

### 🏗️ Tauri Desktop App (مستقبلي)

| # | المهمة | التفاصيل |
|---|--------|----------|
| 11 | **Tauri bootstrap** | إنشاء Tauri project يلف Next.js build output |
| 12 | **Native Pi SDK** | ربط Pi SDK مع Tauri Rust backend |
| 13 | **Desktop notifications** | Native OS notifications (System Tray, Badge) |
| 14 | **Offline mode** | IndexedDB + Tauri FS للعمل بدون إنترنت |
| 15 | **Auto-update** | Tauri updater للـ push التحديثات مباشرة |

**لماذا Tauri بدل Electron؟**
- Tauri: ~10MB (Rust binary + webview)
- Electron: ~150MB (Chromium كامل)
- الـ app خفيف لأن أغلب logic على السيرفر

**الوقت المقدر:** أسبوع واحد بعد ما الـ PWA يستقر

## الخلاصة
أقصر طريق لتكامل أعمق = **#1 + #2 + #3** (توحيد identity في باقي الـ stack)
