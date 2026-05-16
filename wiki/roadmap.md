---
title: "AIX Sovereign Stack — Roadmap"
last_updated: "2026-05-16"
status: "in-progress"
tags: [roadmap, planning, high-priority]
layer: "all"
related:
  - "[[changelog]]"
  - "[[implementation-roadmap]]"
  - "[[execution-plan-10h]]"
  - "[[decisions]]"
---

# AIX Sovereign Stack — Roadmap

## ✅ Completed

### Phase 0: Foundation
- [x] axiomid.app deployed on Vercel ✅
- [x] validation-key.txt working ✅
- [x] @axiom/* all 7 packages built at v0.1.0 ✅
- [x] IQRA deep cleanup (7 major items) ✅
- [x] GemClaw cleanup (backups removed, memory subsystem removed) ✅
- [x] PiWorker-OS cleanup (plugins/ deleted, package.json fixed) ✅

### Phase 1: Code Quality
- [x] Dead code removed from 3 repos (~500 lines)
- [x] 15 outdated docs removed
- [x] IQRA qdrant.ts → reflection-store.ts rename
- [x] IQRA pattern_memory.ts syntax error fixed
- [x] IQRA sovereign_identity.ts undefined var removed
- [x] IQRA memory_governor.ts missing constant added
- [x] IQRA 05-rewards constants unified

### Phase 2: Knowledge Base
- [x] Accurate codebase sizing (7 sub-agents)
- [x] Package-lock analysis (59,656 lines, 35% dep duplication)
- [x] Rust/napi-rs research (deferred)
- [x] KDB restructured into wikigraph format with Quartz

## 🔄 In Progress

### Phase 3: AIX-0 Compression
- [ ] Read all 31 KDB files → extract unique content
- [ ] Create AIX-0.md master reference (~1,200 lines)
- [ ] Create AGENTS.md workflow rules
- [ ] Archive 15 old files

### Phase 4: axiomid.app Pages
- [ ] Build `/memory` page — Bento Grid with 7 quantum memory layers
- [ ] Build `/marketplace` page — skills.json Bento Grid + Pi payments
- [ ] Build `/soul` page — persona editor
- [ ] Build `/voice` page — GemClaw TTS/STT
- [ ] Build `/dashboard` page — PiWorker-OS status

### Phase 5: Pi Network
- [ ] Pi Developer Portal domain claim (user action needed)
- [ ] Test Pi SDK integration
- [ ] Sandbox mode testing

## 📅 Next Up

### Phase 6: Cross-Repo Integration (Medium Priority)
- [ ] iqra → @axiom/identity (replace direct @noble/ed25519)
- [ ] PiWorker-OS → @axiom/pi (use published package)
- [ ] GemClaw neural router → iqra LLM (unify providers)
- [ ] Payment unification (PiWorker-OS → L3 x402)

### Phase 7: Architecture Unification (Lower Priority)
- [ ] BetrayalProtocol → iqra
- [ ] AlphaAxiom .aix skills → L3 marketplace
- [ ] DID unification (all → did:axiom:axiomid.app:*)
- [ ] PiWorker-OS x402 Go → L3 gateway

### Phase 8: Monorepo Migration (Future)
- [ ] pnpm workspaces → single pnpm-lock.yaml
- [ ] Shared packages between repos
- [ ] Turborepo 2.0 for build orchestration

### Phase 9: Desktop App (Future)
- [ ] Tauri bootstrap (after PWA stabilizes)
- [ ] Native Pi SDK
- [ ] Desktop notifications
- [ ] Offline mode
- [ ] Auto-update

## Key Decisions

See [[decisions]] for full list of architectural decisions.

## Current Blockers
1. **Pi Developer Portal domain claim** — user action needed
2. **npm publish @axiom/** — needs npm login
