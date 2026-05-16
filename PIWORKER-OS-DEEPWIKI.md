# 🛡️ PiWorker-OS: The Body — Deep Flow Map
> L5 Satellite · Pi Network · 13,394 lines (5,294 TS + 8,100 Go)

## 🔄 الـ 7 Flows الرئيسية

### Flow 1: Agent Spawning (1a→1e)
```
AIX Package → spawnFromAix() → spawnAgent()
  ├── 1a: spawnFromAix(aixData) ← .aix package
  ├── 1b: agentId = pw-agt-${randomBytes(6).hex} ← unique ID
  ├── 1c: DNA: chromosomes, greed, cunning, cognition, riskAppetite
  ├── 1d: SovereignLedger.etch() ← record birth
  └── 1e: FleetManager.register() ← fleet tracking
```

### Flow 2: Financial Escrow (2a→2f)
```
TS Treasury ←→ Go Engine ←→ Stellar
  ├── 2a: AmrikyyTreasury.createEscrow(orderId, agentId, amount)
  ├── 2b: SovereignBridge.lockEscrow() ← sync with Go
  ├── 2c: sovereignClient.lockEscrow(req) ← HTTP call
  ├── 2d: Go EscrowManager.LockFunds() ← locks Pi coins
  ├── 2e: Transaction{ID, AgentID, Amount, Status: LOCKED}
  └── 2f: Local fallback: state.escrows[orderId] = LOCKED
```

### Flow 3: Physical Embodiment — VLA Robot (3a→3e)
```
PiWorker-OS ←→ Robot Hardware
  ├── 3a: OpenPiAdapter.dispatchTask()
  ├── 3b: PhysicalTaskPayload {intentId, agentId, subtaskLanguage, controlMode}
  ├── 3c: SovereignBridge.sendEmbodiedIntent() → Go bridge
  ├── 3d: sovereignClient.sendEmbodiedIntent() → HTTP
  └── 3e: pi-robot-bridge.ts → WebSocket → robot
```

### Flow 4: PoPW Settlement (4a→4e)
```
Proof of Physical Work ← Gemini Vision
  ├── 4a: OpenPiAdapter.settlePoPW()
  ├── 4b: verifyPhysicalTask(objective, visualFrame) ← Gemini Vision
  ├── 4c: model.generateContent([prompt, image]) ← vision API
  ├── 4d: AmrikyyTreasury.releaseEscrow() ← unlock funds
  └── 4e: SovereignBridge.commitPayment() ← Pi payment
```

### Flow 5: Brain-Muscle Bridge (5a→5e)
```
TypeScript ←→ Go gRPC ←→ Sovereign Engine
  ├── 5a: SovereignBridge.requestSimulation() ← TS
  ├── 5b: sovereignClient.requestSimulation() ← HTTP to Go
  ├── 5c: Go main.go mux.Handle("/sovereign.SovereignService/")
  ├── 5d: authUnaryInterceptor() ← Auth + gRPC interceptor
  └── 5e: pb.RegisterSovereignServiceServer() ← gRPC server
```

### Flow 6: Gemini Oracle (6a→6e)
```
PiWorker ←→ Google Gemini
  ├── 6a: analyzeOpportunity(input) ← main entry
  ├── 6b: isComplex = input.length > 1000
  ├── 6c: gemini-1.5-flash with responseMimeType: application/json
  ├── 6d: model.generateContent([prompt, input])
  └── 6e: JSON.parse(responseText) → ROIEvaluation
```

### Flow 7: Fleet Scaling (7a→7d)
```
PiWorker-OS ←→ Treasury
  ├── 7a: FleetManager.evaluateScaling()
  ├── 7b: AmrikyyTreasury.getStats() ← reserves
  ├── 7c: piReserve >= 200 && fleetSize < 10
  └── 7d: AgentRegistry.mintIdentity() ← new agent
```

## 🏗️ Architecture: TypeScript ←→ Go Bridge

```
TypeScript (Brain)                    Go (Muscle)
─────────────────                    ───────────
SovereignBridge                    main.go
  ├── requestSimulation()  HTTP →    ├── /sovereign.SovereignService/
  ├── lockEscrow()         HTTP →    ├── authUnaryInterceptor()
  ├── commitPayment()      HTTP →    ├── gRPC server
  ├── sendEmbodiedIntent() HTTP →    └── ConnectLite handler
  └── verifyTransaction()  HTTP →
```

## 💰 Key Constants
- SOVEREIGN_TAX_RATE = 10%
- Escrow lock/unlock مع Go Engine sync
- Physical PoPW عبر Gemini Vision
- VLA Robot dispatch عبر WebSocket
- gRPC Server مع Auth Interceptor
