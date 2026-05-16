# 🗺️ AIX Sovereign Stack — Full Map
> آخر تحديث: 2026-05-16

## 🧬 الـ Stack Architecture

```
🧠 L0 axiomid-project (Brain)     → axiomid.app on Vercel
🧬 L1 aix-format (DNA)            → @axiom/* npm packages
🧠 L2 iqra (Memory System)        → 52K lines TS, 7 Loops
🦾 L3 aix-agent-skills (Hands)    → Skills + Roles + Personas + Tools + MCPs
💰 L4 AlphaAxiom (Heart)          → 21K Python, trading engine
🛡️ L5 PiWorker-OS (Body)         → 13K TS+Go, escrow + treasury
🎙️ L6 GemClaw (Voice)            → 29K TS, voice + Aether Forge
```

## 📦 @axiom/* Package Status

| Package | Ver | Built | Deps | Notes |
|---------|-----|-------|------|-------|
| @axiom/identity | 1.3.0 | ✅ | @noble/ed25519, @noble/hashes | المرجع |
| @axiom/schema | 1.3.0 | ✅ | — | AIX Schema |
| @axiom/pi | 0.1.0 | ✅ | zod | Pi integration |
| @axiom/validate | 0.1.0 | ❌ | ajv, zod | يحتاج build |
| @axiom/lint | 0.1.0 | ❌ | — | يحتاج build |
| @axiom/health | 0.1.0 | ❌ | — | يحتاج build |
| @axiom/autofix | 0.1.0 | ❌ | — | يحتاج build |

## 🛒 L3 aix-agent-skills — Full Inventory

مش مجرد skills — ده **سوق متكامل**:

| القسم | العدد | الوصف |
|-------|-------|-------|
| **Skills** | 59 | قدرات قابلة للتنفيذ (Python) |
| **Roles** | — | أدوار للـ agents (Sovereign, Builder, Guardian...) |
| **Personas** | 9 | شخصيات (Sovereign Constitution, Backend Architect...) |
| **Tools** | 7 | MCP tools (skills-mcp, trustchain-mcp, topology-mcp...) |
| **MCPs** | — | Model Context Protocol servers |
| **APIs** | 7 | analytics, registry, orchestrator, memory, trustchain, topology, skills |
| **Layers** | 9 | L0 Sovereignty → L8 Simulation |
| **Tiers** | 6 | SOVEREIGN → ADVANCED_INFRA → PRO → ADVANCED_TOOL → BASIC_TOOL → UNCLASSIFIED |

الـ L3 هو الـ **Marketplace** لكل الـ ecosystem — L4/L5/L6 يشتروا منه.

## 🔗 الـ Dependencies الفعلية

```
PiWorker-OS → @axiom/pi (مضاف لكن مش منشور)
iqra → @noble/ed25519 (مباشر، مش عبر @axiom/identity)
aix-format → workspace:* (كل package يعتمد على الآخر محلياً)
axiomid-project → next, prisma, framer-motion (لا @axiom/*)
```

## 🎯 الخطة للتوحيد

1. **نشر @axiom/* على npm** — يحتاج npm login + npm publish
2. **ربط iqra بـ @axiom/identity** — بدل @noble/ed25519 المباشر
3. **ربط PiWorker-OS بـ @axiom/pi (Published)** — بدل الـ local dep
4. **L3 ← L2/L4/L5/L6** — كل الـ Satellites يشتروا skills من L3
5. **GemClaw neural → iqra LLM** — توحيد providers
