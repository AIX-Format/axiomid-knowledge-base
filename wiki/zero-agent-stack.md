---
title: "Zero Agent Stack — Vercel Labs Tools for AI Agents"
last_updated: "2026-05-18"
status: "draft"
tags: [zero, agents, tooling, vercel, browser, systems, language]
layer: "all"
related:
  - "[[stack-overview]]"
  - "[[L3-aix-agent-skills]]"
  - "[[L1-aix-format]]"
  - "[[L5-piworker-os]]"
  - "[[cross-repo-architecture]]"
  - "[[changelog]]"
---

# Zero Agent Stack — Vercel Labs Tools for AI Agents

> مجموعة أدوات Vercel Labs للـ AI Agents — نُشرت May 2026
> AIX-Format/zero forked من vercel-labs/zero

## Overview

فيرسل لابس أطلقت في مايو 2026 مجموعة متكاملة من الأدوات المصممة خصيصًا للـ AI Agents. كل أداة تحل مشكلة محددة في الـ agent workflow.

| الأداة | التاريخ | Stars | الغرض |
|--------|---------|-------|-------|
| **Zero** | May 16 | 2.1k | لغة برمجة للـ Agents |
| **agent-browser** | Feb 2026 | 32.7k | أتمتة المتصفح CLI |
| **opensrc** | May 2026 | جديد | جلب source code للـ packages |
| **zero-native** | May 2026 | 3.6k | تطبيقات Desktop/Mobile بـ Zig + Web UI |

## 1. Zero — Programming Language for Agents

### ما هو Zero؟

Zero هي **لغة systems جديدة من Vercel Labs** مصممة خصيصًا لتكون:
- مفهومة من Humans + AI Agents
- مخرجات compiler مهيكلة (JSON) قابلة للقراءة من الـ Agents
- explicit capabilities (مافيش hidden globals)
- tiny binaries (بدون GC إجباري أو runtime)

**الحالة**: Experimental v0.1.2 (نزلت 16 مايو 2026)
**الـ Compiler**: مكتوب بـ C (65.9%) + JavaScript (27.9%)
**الـ Source**: `AIX-Format/zero` (fork)

### الميزات الأساسية

```
pub fun main(world: World) -> Void raises {
    check world.out.write("hello from zero\n")
}
```

- **Capability-based I/O**: `world: World` يمرر capabilities صراحة
- **JSON diagnostics**: `zero check --json` → diagnostics مع رموز fix لكل خطأ
- **Agent-native**: `zero fix --plan --json` → خطة إصلاح machine-readable
- **No hidden allocator**: allocation و cleanup صريحة
- **C ABI**: interop مع C مباشر
- **cross-compilation**: `--target linux-musl-x64`

### Standard Library Modules

| Module | الوظيفة |
|--------|---------|
| `std.crypto` | Ed25519, SHA-256, hashing |
| `std.http` | HTTP client |
| `std.json` | JSON parsing/serialization |
| `std.fs` | File system operations |
| `std.net` | Networking |
| `std.time` | Time and duration |
| `std.codec` | Encoding (CRC32, varint, readU16...) |
| `std.parse` | Parsing (digits, identifiers) |
| `std.mem` | Memory (span, len, eqlBytes) |
| `std.args` | CLI arguments |
| `std.env` | Environment variables |
| `std.proc` | Process management |

### الأهم لمشاريعنا: `std.crypto`

```zero
use std.crypto

pub fun main(world: World) -> Void raises {
    // Ed25519 signing للـ DID
    let keypair = std.crypto.ed25519.generate()
    let signature = std.crypto.ed25519.sign(keypair.secret, "message")
    let valid = std.crypto.ed25519.verify(keypair.public, "message", signature)

    // SHA-256 للـ TrustChain
    let hash = std.crypto.sha256("data")
}
```

## 2. agent-browser — Browser Automation CLI

### ما هو؟

CLI لأتمتة المتصفح مخصص للـ AI Agents. يستخدم **snapshot refs** بدلاً من CSS selectors.
مكتوب بـ Rust (CLI) مع daemon في الخلفية، لا يحتاج Node.js.

**Stars**: 32.7k ⭐
**التركيب**: `npm install -g agent-browser`

### الميزات الرئيسية

```
agent-browser open example.com
agent-browser snapshot           # Accessibility tree + refs (@e1, @e2...)
agent-browser click @e2          # Click by snapshot ref
agent-browser fill @e3 "text"    # Fill by ref
agent-browser screenshot --annotate  # Screenshot مع refs مرئية
agent-browser eval "JS code"     # تنفيذ JavaScript
agent-browser chat "instruction" # AI chat: وصف طبيعي
```

### لماذا يهمنا؟

| الاستخدام | كيف |
|-----------|-----|
| **اختبار Pi Sandbox** | فتح Pi Browser وما يقوم بأتمتة flow الـ auth |
| **Testing UX** | اختبار واجهة axiomid.app تلقائياً |
| **E2E للـ agents** | اختبار agent skills في متصفح حقيقي |
| **وكيل تصفح** | الـ agent يقدر يتصفح ويختار UI بنفسه |

### Security Features

```
agent-browser --allowed-domains "axiomid.app,sandbox.minepi.com"
agent-browser --confirm-actions eval,download
agent-browser --content-boundaries  # فصل output الـ agent عن محتوى الصفحة
```

## 3. opensrc — Package Source for Agents

### ما هو؟

CLI: `opensrc path <package>` → يجيب source code لأي package ويحفظه cache.

```
npm install -g opensrc

# Search source code
rg "parse" $(opensrc path zod)
cat $(opensrc path pypi:requests)/src/requests.py

# Works مع registries: npm, PyPI, crates.io, GitHub
```

### لماذا يهمنا؟

أي agent يقدر يقرأ source الـ dependencies بدلاً من type definitions فقط:
- `opensrc path @axiom/identity` → يشوف source الـ DID logic
- `opensrc path minepi/pi-sdk-js` → يشوف implementation الـ Pi SDK
- `opensrc path prisma` → يفهم Prisma internals

**مفهرس في**: `Moeabdelaziz007/opensrc` (fork)

## 4. zero-native — Desktop/Mobile Apps

### ما هو؟

إطار لتطبيقات Desktop و Mobile تستخدم Zig + Web UI. 
`zero-native`:
- System WebView (macOS WKWebView, Linux WebKitGTK)
- أو Chromium عبر CEF
- Bridge بين Zig و JavaScript

### لماذا يهمنا؟

- **تطبيق axiomid Desktop**: تشغيل axiomid.app كـ native desktop app
- **Agent Panel**: نافذة native لإدارة الـ agents
- **Tiny binary**: أصغر من Electron بفرق كبير

---

## Integration Plan لكل Layer

```
┌─────────────────────────────────────────────────────┐
│                   Vercel Agent Stack                │
├────────────┬──────────┬──────────┬──────────────────┤
│ Zero       │ browser  │ opensrc  │ zero-native      │
│ (لغة agents)│(أتمتة ويب)│(source) │ (native UI)      │
└────┬───────┴────┬─────┴────┬─────┴────────┬─────────┘
     │            │          │              │
     ▼            ▼          ▼              ▼
┌─────────────────────────────────────────────────────┐
│              AIX Sovereign Stack (7 Layers)          │
└─────────────────────────────────────────────────────┘
```

| Layer | Zero | agent-browser | opensrc | zero-native |
|-------|------|---------------|---------|-------------|
| **L0 axiomid** | DID resolution CLI | اختبار auth flow | تحليل Pi SDK | Desktop wallet |
| **L1 aix-format** | `std.crypto` للتوقيع | Validate manifest UI | قراءة @axiom/* packages | Editor للـ manifest |
| **L2 iqra** | Memory query tools | Visualize knowledge graph | قراءة memory adapters | Native memory viewer |
| **L3 aix-agent-skills** | Agent-native tools (`--json`) | اختبار skills في المتصفح | فتح source الـ dependencies | Agent dashboard |
| **L4 AlphaAxiom** | Trading CLI | مراقبة السوق | تحليل quant libs | Trading terminal |
| **L5 PiWorker-OS** | Tiny CLI بديل Go | اختبار KYC flow | قراءة Pi KYC SDK | Native KYC app |
| **L6 GemClaw** | Backup/cleanup CLI | اختبار Gemini UI | فتح Google AI SDK | — |

### أولوية التطبيق

1. **Zero CLI للتوقيع الرقمي** (L1) — `std.crypto` للتوقيع Ed25519
2. **agent-browser لاختبار auth** (L0) — أتمتة flow الـ Pi
3. **opensrc لتحليل الـ SDKs** (L0, L5) — فهم الـ Pi SDK و Prisma
4. **zero-native لـ Desktop** (L0, L3) — مستقبلًا

---

## Skills لكل Agent

عشان نستفيد من الـ stack، نضيف skills في `aix-agent-skills`:

```
aix-agent-skills/
└── skills/
    ├── zero/
    │   └── SKILL.md     ← استخدام Zero CLI
    ├── agent-browser/
    │   └── SKILL.md     ← أتمتة المتصفح
    └── opensrc/
        └── SKILL.md     ← فتح source dependencies
```

---

## الأمان والمخاطر

- **Zero experimental (v0.1.2)**: ما يصح للإنتاج، بس للتجارب والـ CLI tools
- **agent-browser 32.7k stars**: ناضج، يستخدم في الإنتاج (Vercel نفسه)
- **opensrc جديد**: يحتاج تقييم
- **zero-native pre-release**: للتجارب فقط

**ما يأخذ مكان TypeScript**: TypeScript يبقى الـ strategic language (ADR-0001). Zero يخدم حالات محددة.
