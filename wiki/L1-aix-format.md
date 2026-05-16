---
title: "AIX Format — Protocol & DNA (L1)"
last_updated: "2026-05-16"
status: "stable"
tags: [protocol, dna, packages, schema, identity]
layer: "L1"
related:
  - "[[stack-overview]]"
  - "[[L0-axiomid]]"
  - "[[L2-iqra]]"
  - "[[pi-network]]"
---

# AIX Format — Protocol & DNA (L1)

> ~42,000 lines | pnpm monorepo | 17 packages

## Architecture

```
aix-format/
├── core/               → Runtime parsers, validation
│   ├── parser.js       → Multi-format parser (JSON/YAML/TOML)
│   ├── validation-engine → Plugin-based validation
│   ├── abom-scanner.js → Agent Bill of Materials scanner
│   ├── canonicalize.js → JCS canonicalization (RFC 8785)
│   └── pi_kyc_adapter.ts → Pi KYC adapter
├── packages/ (17 packages)
│   ├── @axiom/* (7)    → Published npm packages
│   │   ├── axiom-identity → Ed25519, DIDs, canonical
│   │   ├── axiom-schema   → AIX JSON Schema + TS types
│   │   ├── axiom-pi       → Pi Network integration
│   │   ├── axiom-validate → Manifest validation CLI
│   │   ├── axiom-lint     → Linting CLI
│   │   ├── axiom-health   → Health check CLI
│   │   └── axiom-autofix  → Auto-fix CLI
│   ├── @aix/* (3)      → Internal packages
│   └── Other (7)
├── schemas/            → JSON Schemas
│   └── aix.schema.json → Master schema (38KB, 430+ properties)
└── apps/               → Studio Next.js app
```

## @axiom/* Package Status (ALL v0.1.0 ✅)

| Package | Status | Purpose |
|---------|--------|---------|
| @axiom/identity | ✅ Built | Ed25519 keys, DIDs, JCS canonical |
| @axiom/schema | ✅ Built | AIX JSON Schema + TS codegen |
| @axiom/pi | ✅ Built | Pi auth, KYC, payment |
| @axiom/validate | ✅ Built | Manifest validation CLI |
| @axiom/lint | ✅ Built | Linting CLI |
| @axiom/health | ✅ Built | Health check CLI |
| @axiom/autofix | ✅ Built | Auto-fix CLI |

## AIX Manifest Protocol (16 Sections)

1. **meta** — Agent metadata
2. **persona** — Role, instructions, tone
3. **security** — Checksum, signature, encryption
4. **identity_layer** — DID, KYC tier, Ed25519 key
5. **trustchain** — SHA-256 audit log
6. **evolution** — Self-improvement tracking
7. **skills** — MCP-flavored tool surface
8. **apis** — API integrations
9. **mcp** — MCP server configs
10. **memory** — Episodic, semantic, procedural
11. **economics** — x402 payments, wallets
12. **abom** — Agent Bill of Materials
13. **pi_network** — Pi Network config
14. **live_voice** — Voice integration
15. **requirements** — Hardware/software
16. **meta_arbiter** — Subsystem orchestration
