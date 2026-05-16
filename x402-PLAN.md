# x402 Payment Unification Plan

## Architecture Target

```
Agent (PiWorker-OS)
    │
    ├─ يطلب skill من L3
    │   POST /skills/mcts-simulator/manifest
    │
    ├─ L3 يرجع 402 + x402 payload
    │   HTTP 402 Payment Required
    │   X-Payment-Header: {...}
    │
    ├─ PiWorker-OS يوقع الـ payment
    │   via @axiom/pi → Pi SDK
    │
    ├─ يعيد الطلب مع X-PAYMENT
    │   GET /skills/mcts-simulator/manifest
    │   X-PAYMENT: signed_token
    │
    └─ L3 يسلم الـ manifest → agent يشغله
```

## اللي موجود حالياً

| المكون | أين | الوظيفة | سيصير |
|--------|-----|---------|-------|
| `x402 protocol` | L3/server/ (Hono + x402-hono) | Skills marketplace gateway | **يبقى** — gateway واحد |
| `x402 Go` | PiWorker-OS/sidecar/finance/pi402/ | x402 في Go | **يُحذف** — PiWorker-OS يستخدم L3 gateway |
| `Escrow` | PiWorker-OS Go | Pi escrow (LOCKED/RELEASED) | **يبقى** — فريد لـ Pi coins |
| `AmrikyyTreasury` | PiWorker-OS TS | 10% tax | **يبقى** — فريد |
| `agent_payment_router` | aix-format/core/ | Protocol definition | **يبقى** — المرجع |

## خطة التنفيذ (3 خطوات)

### الخطوة 1: PiWorker-OS يرتبط بـ L3 x402
- بدل ما يستخدم x402.go بتاعه، يعمل HTTP call لـ L3 gateway
- الـ Pi payment يتم عبر `@axiom/pi`
```typescript
// PiWorker-OS/core/finance/skill-purchase.ts
import { createPayment } from '@axiom/pi';

async function purchaseSkill(skillName: string, pricePi: number) {
  // 1. Pay via Pi SDK
  const payment = await createPayment({
    amount: pricePi,
    memo: `Skill: ${skillName}`,
  });
  
  // 2. Get skill from L3 gateway
  const res = await fetch(`https://skills.axiomid.app/skills/${skillName}/manifest`, {
    headers: { 'X-PAYMENT': payment.identifier }
  });
  
  return res.json();
}
```

### الخطوة 2: Pi كـ payment rail في L3
- L3 gateway حالياً يدعم USDC على Base
- إضافة Pi كـ payment rail ثاني
```typescript
// L3/server/src/pi-rail.ts
import { verifyPayment } from '@axiom/pi';

export async function verifyPiPayment(paymentId: string): Promise<boolean> {
  // Verify via Pi Platform API
  const { apiKey } = getPiEnv();
  return verifyPayment(paymentId, apiKey);
}
```

### الخطوة 3: إزالة x402.go من PiWorker-OS
- بعد ما PiWorker-OS يستخدم L3 gateway
- نحذف `sidecar/sovereign-engine/pkg/finance/pi402/`
- نحتفظ بـ `escrow-manager.go` (مطلوب لـ Pi escrow)

## المكاسب
- 🎯 كود أقل (إزالة duplicate x402)
- 🔗 تكامل حقيقي بين L5 و L3
- 💰 Pi payments تدخل ecosystem
- 🧹 نظافة في PiWorker-OS sidecar
