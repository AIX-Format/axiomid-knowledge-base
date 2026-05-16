---
title: "Implementation Roadmap"
last_updated: "2026-05-16"
status: "in-progress"
tags: [roadmap, implementation, phases]
layer: "all"
related:
  - "[[roadmap]]"
  - "[[execution-plan-10h]]"
  - "[[decisions]]"
---

# Implementation Roadmap

> آخر تحديث: 2026-05-16 — بعد جلسة التنظيف العميق.

## ✅ Completed

- [x] **Phase 0** — Dead code: PiWorker-OS sandbox, axiomid-project 3 plan docs, iqra 6 docs
- [x] **Phase 1** — `@axiom/pi` package, PiWorker-OS DID migration, deep cleanup
- [x] **Phase 5** — `axiomid.app` deployed on Vercel, validation-key.txt works
- [x] **Deep cleanup** — 3 repos: ~500 lines duplicate + 15 outdated docs removed

## ⏳ Remaining by Priority

### 🥇 High Priority

| # | Task | Repo | Details |
|---|------|------|---------|
| 1 | axiomid-project ← @axiom/pi | axiomid-project | Replace local pi/env.ts with @axiom/pi |
| 2 | iqra personas → did:axiom | iqra | Migrate DID formats |
| 3 | aix-core/infra.ts → @axiom/identity | aix-format | Replace tweetnacl with @axiom/identity |

### 🥈 Medium Priority

| # | Task | Repo | Details |
|---|------|------|---------|
| 5 | Payment unification (x402) | PiWorker-OS + L3 | Connect PiWorker-OS to L3 x402 |
| 6 | GemClaw neural → iqra | GemClaw + iqra | Unify LLM providers |
| 7 | GemClaw → AxiomClaw | GemClaw | Rename repo |

### 🥉 Low Priority

| # | Task | Repo | Details |
|---|------|------|---------|
| 8 | BetrayalProtocol → iqra | PiWorker-OS + iqra | Migrate governance-engine |
| 9 | AlphaAxiom .aix → L3 | AlphaAxiom + L3 | Convert skills to marketplace |
| 10 | PiWorker-OS x402 Go → L3 | PiWorker-OS + L3 | Unify x402 protocol |

### 🏗️ Tauri Desktop (Future)

| # | Task | Details |
|---|------|---------|
| 11 | Tauri bootstrap | Create Tauri wrapping Next.js build |
| 12 | Native Pi SDK | Pi SDK with Tauri Rust backend |
| 13 | Desktop notifications | Native OS notifications |
| 14 | Offline mode | IndexedDB + Tauri FS |
| 15 | Auto-update | Tauri updater |

**Why Tauri over Electron?**: ~10MB (Rust + webview) vs ~150MB (Chromium).

**Estimated**: 1 week after PWA stabilizes.

## Summary

Shortest path to deeper integration: **#1 + #2 + #3** (unify identity across the stack).
