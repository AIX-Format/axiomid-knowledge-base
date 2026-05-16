# 🧬 AIX Format: Universal Agent Passport — Overview
> L1 Protocol · AIX/1.0 · Echo369 · ~42,000 lines

## System Purpose & Scope
AIX Format is the **DNA** of the AIX Sovereign Stack — an open, portable, signed JSON-LD manifest standard for AI agents. It's a pnpm monorepo containing the `@axiom/*` npm packages that every other layer depends on.

## Architecture
```
aix-format/
├── core/                  → Runtime parsers, validation (JS/TS)
│   ├── parser.js          → Multi-format parser (JSON/YAML/TOML)
│   ├── validation-engine  → Plugin-based validation
│   ├── abom-scanner.js    → Agent Bill of Materials scanner
│   ├── canonicalize.js    → JCS canonicalization (RFC 8785)
│   └── pi_kyc_adapter.ts  → Pi KYC adapter
│
├── packages/ (17 packages)
│   ├── @axiom/* (7)       → Published npm packages
│   │   ├── axiom-identity → Ed25519, DIDs, canonical
│   │   ├── axiom-schema   → AIX JSON Schema + TS types
│   │   ├── axiom-pi       → Pi Network integration
│   │   ├── axiom-validate → Manifest validation
│   │   ├── axiom-lint     → Linting tool
│   │   ├── axiom-health   → Health checker
│   │   └── axiom-autofix  → Auto-fixer
│   │
│   ├── @aix/* (3)         → Internal packages
│   │   ├── aix-core       → Core runtime library
│   │   ├── aix-zkkyc      → Zero-knowledge KYC
│   │   └── aix-rust-core  → Rust WASM bridge
│   │
│   └── Other (7)
│       ├── aix-agency     → Go module (agent orchestration)
│       ├── aix-dna        → Rust crate
│       ├── aix-types      → TS declarations
│       ├── mcp-gateway    → MCP gateway
│       ├── mcp-server     → MCP server
│       └── pi-kyc         → Pi KYC (deprecated → @axiom/pi)
│
├── schemas/               → JSON Schemas
│   └── aix.schema.json    → Master schema (38KB, 430+ properties)
│
└── apps/                  → Studio Next.js app
```

## @axiom/* Package Status (ALL at v0.1.0 ✅)

| Package | Built | Deps | Purpose |
|---------|-------|------|---------|
| @axiom/identity | ✅ | @noble/ed25519, hashes | Ed25519 keys, DIDs, JCS canonical |
| @axiom/schema | ✅ | — | AIX JSON Schema + TS codegen |
| @axiom/pi | ✅ | zod | Pi auth, KYC, payment, env |
| @axiom/validate | ✅ | ajv, zod | Manifest validation CLI |
| @axiom/lint | ✅ | — | Linting CLI |
| @axiom/health | ✅ | — | Health check CLI |
| @axiom/autofix | ✅ | — | Auto-fix CLI |

## Key Protocol: AIX Manifest (16 sections)
1. **meta** — Agent metadata (version, ID, name, lineage)
2. **persona** — Role, instructions, tone, constraints
3. **security** — Checksum, signature, encryption
4. **identity_layer** — DID, KYC tier, Ed25519 key, ZK-proof
5. **trustchain** — Append-only SHA-256 audit log
6. **evolution** — Self-improvement tracking
7. **skills** — MCP-flavored tool surface
8. **apis** — API integrations
9. **mcp** — MCP server configs
10. **memory** — Episodic, semantic, procedural
11. **economics** — x402 payments, wallets, treasury
12. **abom** — Agent Bill of Materials
13. **pi_network** — Pi Network config
14. **live_voice** — Voice integration
15. **requirements** — Hardware/software requirements
16. **meta_arbiter** — Subsystem orchestration

## Stack Position
```
L1 AIX Format (DNA)
  ↓ provides schemas, identity primitives, validation
L2 iqra (uses @axiom/* packages)
L3 aix-agent-skills (uses schema)
L4-L6 Satellites (use @axiom/pi, @axiom/identity)
```
