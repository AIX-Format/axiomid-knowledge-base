# 🤖 Prompts for Jules AI — AIX Sovereign Stack

## 1. توليد Unit Tests لـ @axiom/pi
```
You are working in AIX-Format/aix-format repo at packages/axiom-pi/.
Write comprehensive Vitest unit tests for each module:
- src/auth.ts: Test authenticateUser (browser + server mode, Pi SDK mock)
- src/kyc.ts: Test verifyKyc (valid UID, invalid UID, JWT expiry, blockchain anchor, VLA device)
- src/payment.ts: Test createPayment (success, error, cancellation)
- src/env.ts: Test getPiEnv (with env vars, missing PI_API_KEY throws)

Use vi.mock() for Pi SDK. Follow existing test patterns from packages/axiom-identity/test/.
Write tests to packages/axiom-pi/test/{module}.test.ts
```

## 2. تحديث AGENTS.md لـ axiomid-project
```
Write AGENTS.md for AIX-Format/axiomid-project.
This is the L0 Root Authority — a Next.js 16 app serving axiomid.app.
Include:
- Project overview (Human Authorization Protocol)
- Architecture (Next.js App Router, Prisma, Vercel)
- Identity system (did:axiom, XP tiers Ghost→Axiom)
- Pi Network integration (validation-key.txt, @axiom/pi)
- Key directories (src/, prisma/, public/)
- Coding rules (strict TypeScript, no hardcoded secrets)
- Deployment (GitHub Actions → Vercel)

Language: Arabic + English
Save to: AGENTS.md
```

## 3. توليد Tests لـ axiomid-project API routes
```
Generate Vitest unit tests for AIX-Format/axiomid-project API routes:
- src/app/api/auth/connect/route.ts: POST creates/finds user, validates wallet
- src/app/api/action/claim/route.ts: POST claims XP, checks duplicates, daily cooldown
- src/app/api/user/status/route.ts: GET fetches user status
- src/app/api/score/route.ts: GET returns config, POST validates stamps + rate limiting

Use mocked Prisma client. Test edge cases (missing params, not found, rate limited).
Save to: src/app/api/__tests__/{route}.test.ts
```

## 4. توثيق @axiom/pi README
```
Write README.md for packages/axiom-pi/ in AIX-Format/aix-format.
Include:
- Purpose: Unified Pi Network integration for AIX Sovereign Stack
- API reference: authenticateUser, verifyKyc, createPayment, getPiEnv
- Usage examples for browser (Pi SDK) and server (env vars)
- Environment variables (PI_API_KEY, NEXT_PUBLIC_PI_SANDBOX)
- Badge: npm, license, stack layer

Language: English
Save to: packages/axiom-pi/README.md
```

## 5. إنشاء @axiom/identity/pi.test.ts
```
Write comprehensive tests for AIX-Format/aix-format/packages/axiom-identity/src/pi.ts.
This module handles Pi Domain Claims (Ed25519 signed manifests for .well-known/pi-claim.json).
Test:
- createPiClaim: generates valid claim with correct structure
- verifyPiClaim: verifies a valid claim, rejects tampered claim
- bootstrapPiClaim: creates self-signed bootstrap claim
- Edge cases: missing domain, invalid DID, expired timestamps

Save to: packages/axiom-identity/test/pi-domain-claim.test.ts
```

## 6. تنظيف pi-kyc القديم
```
In AIX-Format/aix-format/repo:
1. Read packages/pi-kyc/src/index.ts — it duplicates logic now in @axiom/pi
2. Replace its body with: 'export * from "@axiom/pi";'
3. Update packages/pi-kyc/package.json to add @axiom/pi as dependency
4. Verify the build works with: cd packages/pi-kyc && npx tsc --noEmit
```

## 7. توليد JSON Schema لـ @axiom/pi
```
Generate a JSON Schema document for the @axiom/pi package API.
Document the shape of:
- KycInput (user.uid, accessToken, signature?, publicKey?)
- KycResult (identity_layer, kyc_proof)
- KycProof (version, provider, uid_hash, etc.)
- IdentityLayer (id, authority, issuedAt)

Save as JSON Schema for documentation purposes.
Save to: packages/axiom-pi/schemas/pi-kyc.schema.json
```
