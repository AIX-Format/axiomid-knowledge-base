---
title: "Clean Room — 7 Skills from IQRA to L3"
last_updated: "2026-05-16"
status: "stable"
tags: [skills, clean-room, iqra, marketplace, migration]
layer: "L2,L3"
related:
  - "[[L2-iqra]]"
  - "[[L3-aix-agent-skills]]"
  - "[[cleanup-plan]]"
  - "[[full-skills-map]]"
---

# Clean Room — 7 Skills from IQRA Utils+Infra

> نقل 7 skills من IQRA (L2) إلى L3 marketplace.

## Skill 1: persona-loader
**Source**: iqra/13-utils/personas.ts

**Purpose**: Load agent personas from L3 marketplace instead of hardcoded in IQRA.

```typescript
loadPersona(personaId: string): Promise<Persona>
listPersonas(): Promise<PersonaSummary[]>
getPersonaForRole(role: string): Promise<Persona>
```

## Skill 2: sovereign-crypto
**Source**: iqra/13-utils/sovereign_cipher.ts

**Purpose**: AES-256-GCM encryption for any agent.

```typescript
encrypt(plaintext: string, key: Uint8Array): Promise<EncryptedPayload>
decrypt(payload: EncryptedPayload, key: Uint8Array): Promise<string>
generateKey(): Uint8Array
hash(data: string): string
```

## Skill 3: timeout-utils
**Source**: iqra/13-utils/timeout.ts (~50 lines)

**Purpose**: Timeouts + retries + backoff for any agent.

```typescript
withTimeout<T>(promise: Promise<T>, ms: number): Promise<T>
withRetry<T>(fn: () => Promise<T>, options: RetryOptions): Promise<T>
exponentialBackoff(attempt: number): number
```

## Skill 4: system-heartbeat
**Source**: iqra/12-infrastructure/heartbeat.ts (579 lines)

**Purpose**: System/agent health monitoring.

```typescript
getHealth(): HealthStatus
getMetrics(): SystemMetrics
ping(): boolean
report(): HealthReport
```

## Skill 5: skill-registry
**Source**: iqra/12-infrastructure/tools_registry.ts (568 lines)

**Purpose**: Registry for discovering and managing skills.

```typescript
register(skill: SkillDefinition): void
discover(query: string): SkillDefinition[]
getSkill(id: string): SkillDefinition | null
listByTier(tier: SkillTier): SkillDefinition[]
```

## Skill 6: vector-search
**Source**: iqra/12-infrastructure/qdrant.ts (118 lines)

**Purpose**: Unified vector search.

```typescript
search(query: string, limit?: number): Promise<SearchResult[]>
upsert(id: string, vector: number[], payload: any): Promise<void>
delete(id: string): Promise<void>
```

## Skill 7: universal-logger
**Source**: iqra/12-infrastructure/logger.ts (72 lines)

**Purpose**: Structured logging for all agents.

```typescript
log(level: LogLevel, message: string, context?: object): void
info(message: string, context?: object): void
warn(message: string, context?: object): void
error(message: string, error?: Error): void
setLevel(level: LogLevel): void
```

## Migration Path

```
IQRA Today                              After Clean Room
────────────────────────────────────    ─────────────────────────────
13-utils/personas.ts      →  L3 skill: persona-loader
13-utils/sovereign_cipher.ts → L3 skill: sovereign-crypto
13-utils/timeout.ts       →  L3 skill: timeout-utils
12-infra/heartbeat.ts     →  L3 skill: system-heartbeat
12-infra/tools_registry.ts → L3 skill: skill-registry
12-infra/qdrant.ts        →  L3 skill: vector-search
12-infra/logger.ts        →  L3 skill: universal-logger

In IQRA: 4,264 lines → thin wrappers calling L3 skills
In L3: 7 new skills in marketplace
```

## Benefit

| Before | After |
|--------|-------|
| 4,264 lines in IQRA (not connected to L3) | ~1,400 lines skills in L3 |
| Only IQRA uses them | Any Agent (PiWorker, GemClaw, etc.) |
| Separate maintenance | Unified maintenance in L3 |
| Without signature | Ed25519 signed skills |
