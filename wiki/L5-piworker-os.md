---
title: "PiWorker-OS — Pi Treasury & Body (L5)"
last_updated: "2026-05-16"
status: "stable"
tags: [pi-network, treasury, escrow, go, fleet]
layer: "L5"
related:
  - "[[stack-overview]]"
  - "[[L4-alphaaxiom]]"
  - "[[L2-iqra]]"
  - "[[pi-network]]"
  - "[[x402-plan]]"
  - "[[brain-build-plan]]"
---

# PiWorker-OS — Pi Treasury & Body (L5)

> 5,294 lines TS + 8,100 lines Go | Next.js 15 + Go sidecar

## الرئيسية 7 Flows

### Flow 1: Agent Spawning
```
spawnFromAix(aixData) → spawnAgent()
→ agentId = pw-agt-${randomBytes(6).hex}
→ DNA: chromosomes, greed, cunning, cognition, riskAppetite
→ SovereignLedger.etch() (record birth)
→ FleetManager.register()
```

### Flow 2: Financial Escrow
```
AmrikyyTreasury.createEscrow(orderId, agentId, amount)
→ SovereignBridge.lockEscrow() → Go EscrowManager.LockFunds()
→ Transaction{ID, AgentID, Amount, Status: LOCKED}
→ Local fallback: state.escrows[orderId] = LOCKED
```

### Flow 3: PoPW Settlement (Proof of Physical Work)
```
OpenPiAdapter.settlePoPW()
→ verifyPhysicalTask(objective, visualFrame) ← Gemini Vision
→ model.generateContent([prompt, image])
→ AmrikyyTreasury.releaseEscrow()
→ SovereignBridge.commitPayment()
```

### Flow 4: Brain-Muscle Bridge (TS ←→ Go)
```
SovereignBridge.requestSimulation() → HTTP → Go
→ authUnaryInterceptor() → gRPC server
→ pb.RegisterSovereignServiceServer()
```

### Flow 5: Gemini Oracle
```
analyzeOpportunity(input)
→ isComplex = input.length > 1000
→ gemini-1.5-flash with responseMimeType: application/json
→ model.generateContent([prompt, input])
→ JSON.parse(responseText) → ROIEvaluation
```

### Flow 6: Fleet Scaling
```
FleetManager.evaluateScaling()
→ AmrikyyTreasury.getStats() ← reserves
→ piReserve >= 200 && fleetSize < 10
→ AgentRegistry.mintIdentity() ← new agent
```

## Architecture: TypeScript ←→ Go Bridge

```
TypeScript (Brain)                    Go (Muscle)
─────────────────                    ───────────
SovereignBridge                    main.go
  ├── requestSimulation()  HTTP →   ├── /sovereign.SovereignService/
  ├── lockEscrow()         HTTP →   ├── authUnaryInterceptor()
  ├── commitPayment()      HTTP →   ├── gRPC server
  ├── sendEmbodiedIntent() HTTP →   └── ConnectLite handler
  └── verifyTransaction()  HTTP →
```

## Key Constants
- SOVEREIGN_TAX_RATE = 10%
- Escrow lock/unlock with Go Engine sync
- Physical PoPW via Gemini Vision
- gRPC Server with Auth Interceptor

## Unique Code (لا يوجد في أي repo آخر)
- **TreasuryVault**: 10% sovereign tax
- **EscrowManager** (Go): Pi escrow
- **SorobanBridge** (Go): Stellar integration
- **PluginGateway**: Plugin system
- **SovereignBridge**: Bridge to Go sidecar
