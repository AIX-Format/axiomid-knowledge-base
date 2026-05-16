---
title: "Jules AI — 7 Prompts for Automation"
last_updated: "2026-05-16"
status: "stable"
tags: [prompts, automation, jules, testing]
layer: "all"
related:
  - "[[cleanup-plan]]"
  - "[[L1-aix-format]]"
---

# Jules AI — 7 Prompts for Automation

> Prompts for Jules AI to automate tasks across the AIX Sovereign Stack.

## 1. Generate Unit Tests for @axiom/pi
Test authenticateUser, verifyKyc, createPayment, getPiEnv. Use vi.mock() for Pi SDK.

## 2. Update AGENTS.md for axiomid-project
L0 Root Authority — Next.js 16 app at axiomid.app. Include identity system, Pi integration, deployment.

## 3. Generate Tests for axiomid-project API Routes
Test POST /api/auth/connect, POST /api/action/claim, GET /api/user/status, POST /api/score.

## 4. Document @axiom/pi README
Pi Network integration package. API reference + usage examples + env vars.

## 5. Create @axiom/identity/pi.test.ts
Test Pi Domain Claims: createPiClaim, verifyPiClaim, bootstrapPiClaim, edge cases.

## 6. Clean Up Old pi-kyc
Replace body with `export * from "@axiom/pi"`, update package.json.

## 7. Generate JSON Schema for @axiom/pi
Document KycInput, KycResult, KycProof, IdentityLayer shapes.
