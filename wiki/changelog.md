---
title: "AIX Sovereign Stack — Changelog"
last_updated: "2026-05-24"
status: "stable"
tags: [changelog, updates, history]
layer: "all"
related:
  - "[[roadmap]]"
  - "[[decisions]]"
  - "[[sessions/session-2026-05-24]]"
---

# AIX Sovereign Stack — Changelog

## Session 10: 2026-05-24 (Late Night Fixes)

### Critical Bug Fixes
- **Pi SDK v2 Auth Routing**: Fixed `wallet-context.tsx` to call `/api/auth/pi` (v2 `authenticate({scope, onIncompletePaymentFound})`) instead of `/api/auth/connect` with v1-style array callback. Pi SDK v2 has **no `Pi.init()`** — don't add it.
- **Vercel Build Error**: Fixed syntax error in `page.tsx:299-300` (extra `)` and `}`) causing 26s build failure.
- **KDB Vercel 404**: Fixed `.gitignore` — `content` matched `quartz/content/` too. Changed to `/content`.
- **Agent Routes**: Made Pi token verification conditional — only for `pi:*` wallets, skip for demo.
- **Homepage Cleanup**: Removed status/stats/missions cards that duplicated dashboard.
- **Test Fix**: `auth-connect.test.ts` tier `Ghost` → `Registered`.
- **Deleted empty `marketplace/` directory** (old standalone page, superseded by dashboard).

### Vercel Deployments Status
- **axiomid-project** (https://axiomid.app): Production ✅, Preview fixed ✅
- **KDB** (https://axiomid-knowledge-base.vercel.app): Build fixed ✅, domain alias needs Vercel Dashboard fix

### Architecture Rules Added
- See [[sessions/session-2026-05-24#Session-10-2026-05-24-Late-Night-Fixes|Session 10 Rules]] for agent guidelines.

## Session 9: 2026-05-24 (Evening)

### Pi SDK & Sandbox Payments Implementation
* **Pi.init Integration:** Implemented client-side `Pi.init` with automatic versioning and `sandbox` environment detection.
* **Sandbox Container Fixes:** Set script tag `data-sandbox="true"` inside `pi-sdk.ts`.
* **Server Payments API:** Created backend API routes for `/api/pi/payment/approve` and `/api/pi/payment/complete` communicating with Pi Platform API using the `PI_API_KEY`.
* **Promise-Wrapped payment flow:** Integrated required SDK callbacks (`onReadyForServerApproval`, `onReadyForServerCompletion`, `onCancel`, `onError`) in `createPiPayment` and linked them to the server API endpoints.
* **Dynamic /dashboard Marketplace:** Loaded `skills.json` and `personas.json` from `aix-agent-skills` repository dynamically. Replaced hardcoded dashboard marketplace with a tabbed interface showcasing real agent skills and Arabic IQRA personas.
* **Wallet Context Updates:** Migrated all wallet authentication flows to use `/api/auth/connect` to resolve 401/403 errors with demo wallets.
* **Vercel Deploy:** Deployed the Next.js app to production Vercel (`https://axiomid.app`).

## Session 8: 2026-05-24 (Afternoon)

### Knowledge Base & Link Validation
* **Fixed 4 broken wikilinks** in `API-REGISTRY.md` and `cross-repo-architecture.md` (realigned to L0-L6 layer filenames).
* Validated all 212 wikilinks across 42 files and updated the central dependency graph (`graph/graph.json`).
* Added `session-2026-05-24.md` documenting current changes.

### L0 App Planning & Design
* Designed professional tier system: `Registered`, `Verified`, `Trusted`, `Sovereign`.
* Created implementation plan for the glassmorphic Mission Control dashboard (`/dashboard` route) integrating GemClaw, IQRA, terminal outputs, and Pi Wallet payments.

## Session 7: 2026-05-18 (Evening)

### iqra Deep Cleanup
- **55 dead files deleted** (~7.9KB): dead tests (root `tests/`), stale scripts (`src/scripts_v2/` 46 files → kept 6 active), legacy configs (`setup.yaml` with Qdrant refs, `e2e-mission.yml`), runtime leftover (`git-sovereign.ts`), frontend remnant (`SacredCard.tsx`), generated logs (`WISDOM_7.md`, `METAMORPHOSIS.md`)
- **Reusable code preserved**: `knowledge_mcp_server.py` (LightRAG MCP), `aix_export.ts` (manifest CLI), `analyze_surahs.ts`, `enforce_headers.py`, `fix_imports_smart.cjs`, `start_iqra_ecosystem.sh`, `auto_improve.ts`, `dashboard/template.html`
- **Git speed fixed**: added node_modules to `.git/info/exclude`, enabled `untrackedcache` + `fscache`
- **Cleanup commit pushed**: `db2e324`

### PiWorker-OS Cleanup + PRs
- **5 dead files deleted**: `task.md`, `bootstrap.js`, `go.work.sum`, `PHASE_10_HARDENING.md`, `PHASE_11_RING3_ISOLATION.md`
- **PR #60 merged**: lint-staged 17.0.5
- **PR #58 resolved**: DID migration branch rebased (0 conflicts), already closed
- **PR #44 merged**: Security gates — PR checklist, Semgrep scan, contract tests, security governance policy
- **PR #39 closed**: Superseded by cleanup commits
- **ix-format PR #198 pending**: v1.4.0 hardening (conflicts)

### Architecture Progress
- rebase fix/adr-0001-remove-qdrant-lancedb branch
- API Proxy route live at `axiomid.app/api/proxy/iqra/*`
- iqra-core package structure ready

## Session 6: 2026-05-18 (Morning)

### Pi SDK Sandbox postMessage Debugging
- **Root cause**: `sendSDKMessage` → `window.parent.postMessage(l, f)` with hardcoded `"https://sandbox.minepi.com"` origin; top-level page has `window.parent === window` with `https://axiomid.app` origin → mismatch error
- **Strategy 1** (`window.postMessage` override): `writable: true` on prototype — assignment creates own property that shadows prototype; Chrome does not block via WindowProxy. **Untested.**
- **Strategy 2** (`Object.defineProperty(window, "parent")`): tested, failed — Chrome WindowProxy blocks defineProperty on window for `parent`
- **Strategy 3** (`Window.prototype.parent` getter): tested, failed — extension own-property shadows prototype

### CSP & SDK Loading
- `'unsafe-inline'` added to `script-src` (Pi extension injected scripts)
- Preconnect `Link` for `https://sandbox.minepi.com`
- Hybrid `ensurePiSdk()`: extension `window.Pi` → CDN fallback (3 retries); never deletes existing Pi

### Accessibility
- `h3` → `h2` heading hierarchy; `userScalable: true`

### Cross-Repo PR Analysis
- **GemClaw** (9 PRs): #43 cleanup (-4935 lines, reviewed), 8 dependabot
- **PiWorker-OS** (12 PRs): #58 KYC fix, #44 security checklist, #39 e2e tests, 9 dependabot/CI
- **aix-agent-skills** (1 PR): #54 loadManifest fix (+12/-8, clean)
- **aix-format** (6 PRs): #198 v1.4.0 hardening, 5 dependabot
- **axiomid-project** (4 PRs): #39 Pi SDK+PWA, #37 SIWE, CI bumps, coderabbit tests
- **iqra** (6 PRs): #110 ADR-0001 Qdrant/LanceDB removal, 5 dependabot

---

## Session 5: 2026-05-17

### CodeRabbit Review — axiomid-project
- **`connect/route.ts`**: explicit type validation for `walletAddress`, `piUid`, `piUsername` — 400 on malformed payloads
- **`agent/activate/route.ts`**: `accessToken` validation against Pi API before accepting `walletAddress`; sanitized response (no `apiKeyHash`)
- **`agent/route.ts`**: `accessToken` validation; SHA-256 hash API key before storage; all responses sanitized via `select`
- **`error.tsx`** / **`global-error.tsx`**: stack traces only in dev mode; prod shows generic message + `digest`
- **`global-error.tsx`**: added `lang="en"` + `:focus-visible` keyboard focus on RETRY
- **`privacy/page.tsx`**: raw URL → semantic `<a>` with `target="_blank" rel="noopener noreferrer"`
- **`pi/env.ts`**: `readOptional` noted but skipped (intentional)
- **TypeScript**: clean compile, 0 errors

---

## Session 4: 2026-05-16

### IQRA Deep Cleanup (7 items)
- `tsconfig.json.backup` deleted, 4 empty dirs + 3 `__pycache__` removed
- `qdrant.ts` → `reflection-store.ts` (rename + function rename)
- Updated 3 importers: `security.ts`, `damir_kernel.ts`, `discovery_loop.ts`
- `pattern_memory.ts`: syntax error fixed (extra `}`)
- `sovereign_identity.ts:61`: removed `${deepMemories}` (undefined variable)
- `memory_governor.ts`: added missing `WARM_LIMIT = 100`
- `05-rewards/`: constants unified (engine.ts imports from types.ts)

### Codebase Analysis
- Accurate sizing via 7 sub-agents: 214,200 lines total, ~136,544 real code
- Package-lock analysis: 6 locks = 59,656 lines (28%), 35% dep duplication
- TypeScript = 63% of real code (77,280 lines)
- Rust/napi-rs research: deferred for now

### PR Updates
- IQRA #110: pushed 7 fixes, commented re-review
- GemClaw #43: removed `lib/memory/` (6 files) + `cognitive-worker.ts`

### KDB Updates
- CODEBASE-SIZES.md v3 with real-code numbers
- SESSION-2026-05-16.md with 3rd and 4th sessions
- KDB restructured into wikigraph format with YAML frontmatter + `wikilinks`
- Quartz static site built (34→143 pages), **deployed on Vercel**: https://axiomid-knowledge-base.vercel.app

### axiomid.app Production
- Deployed to Vercel, aliased to https://axiomid.app
- **Ghost.build Postgres** database `axiomid-db` provisioned and connected
- **UserAgent model**: one AI agent per user with publicId for cross-product use
- **Agent API**: create/fetch/activate endpoints live (`/api/agent*`)
- Pi domain claimed (pending Vercel config)

---

## Session 3: 2026-05-15

### Cleanup Across Repos
- **IQRA**: 7 MemoryClient API routes added, LanceDBPlugin leftovers fixed
- **GemClaw**: 33 backup files deleted (~6,900 lines), 3 unused deps removed, 2 dead Firebase imports removed, typo fixed
- **PiWorker-OS**: plugins/ deleted (11 dirs, 38 files, ~865 lines), package.json fixed
- **aix-agent-skills**: 76→124 skills, 8 STUB files fixed, 38 THIN files filled

### Architecture Decisions
- AIX-0 compression plan designed: 31 KDB files → single AIX-0.md + archives
- Cross-system flows documented
- Memory systems comparison completed

---

## Session 2: 2026-05-14 (Evening)

### PR Merged
- **aix-format PR #207**: All @axiom/* packages at v0.1.0, merged

### axiomid.app Deployed
- Deployed on Vercel (axiom-id team, Node 22.x)
- validation-key.txt working
- Domain reassigned: axiomid.app ✅

---

## Session 1: 2026-05-14

### Initial Setup
- axiomid-project created
- Architecture designed (7 repos, 7 layers)
- Cross-system flows mapped
