# 📊 AIX Sovereign Stack — Full Line Count
> آخر تحديث: 2026-05-16 (v3 — عد دقيق لكل repo بـ sub-agents بعد تنظيف IQRA) | Counted by 7 sub-agents, one per repo, using `find` + `wc -l`

## Total Files & Lines by Repo

| Repo | Layer | ملفات | **Total Lines** | % |
|------|-------|-------|----------------|---|
| **iqra** | L2 | 379 | **77,981** | 36.4% |
| **GemClaw** | L6 | 222 | **61,542** | 28.7% |
| **axiomid-project** | L0 | 187 | **27,765** | 13.0% |
| **PiWorker-OS** | L5 | 155 | **19,651** | 9.2% |
| **aix-agent-skills** | L3 | 199 | **14,576** | 6.8% |
| **AlphaAxiom** | L4 | 34 | **9,100** | 4.2% |
| **aix-format** | L1 | 20 | **3,585** | 1.7% |
| **المجموع** | | **1,196** | **214,200** | **100%** |

## Lines by Language (all repos)

| Language | Lines | % |
|----------|-------|---|
| TypeScript (.ts) | 77,280 | 36.1% |
| TypeScript React (.tsx) | 12,574 | 5.9% |
| JavaScript (.js) | 13,820 | 6.5% |
| Python (.py) | 11,566 | 5.4% |
| Go (.go) | 8,915 | 4.2% |
| JSON (.json) | 64,044 | 29.9% |
| Markdown (.md) | 22,568 | 10.5% |
| YAML (.yml/.yaml) | 3,251 | 1.5% |
| CSS (.css) | 182 | 0.1% |
| **Total** | **214,200** | **100%** |

## Lines by Language (code only — excluding JSON + MD + YAML + CSS)

| Language | Lines | % |
|----------|-------|---|
| TypeScript (.ts) | 77,280 | 63.1% |
| TypeScript React (.tsx) | 12,574 | 10.3% |
| JavaScript (.js) | 13,820 | 11.3% |
| Python (.py) | 11,566 | 9.4% |
| Go (.go) | 8,915 | 7.3% |
| **Total (real code)** | **124,155** | **100%** |

## الـ 7 Repos بالترتيب (code only)

```
1. iqra (L2)            50,288 lines (src/ فقط)  🧠 Brain
2. GemClaw (L6)         24,531 lines (TS/TSX)    🎙️ Voice
3. axiomid-project (L0)  2,759 lines (TS/TSX)    👑 Identity  ⚠️ فيه 10,974 JS هو Next.js generated
4. PiWorker-OS (L5)      5,448 TS + 8,915 Go     🛡️ Body
5. aix-agent-skills (L3) 2,618 lines (TS)         🦾 Hands
6. AlphaAxiom (L4)       8,923 lines (Python)     💰 Trading
7. aix-format (L1)        643 lines (TS)          🧬 DNA
```

## Skills Registry

| Metric | Value |
|--------|-------|
| Skills in skills.json | **124** (76 existing + 48 from GemClaw) |
| Skill .md files in skills/ | **122** |
| Skill tiers | 5 (SOVEREIGN, ADVANCED_INFRASTRUCTURE, ADVANCED_TOOL, PRO, BASIC_TOOL) |
| Personas | **9** (1 Sovereign + 2 PRO + 6 Archetype) |
| Implementation repos | iqra (caveman, git, inverse_design, topological), GemClaw (voice), PiWorker-OS (content-arbitrage) |

## Cleanup History

### Skills Cleanup (2026-05-16)
- **aix-agent-skills**: Expanded from 76→124 skills, fixed 8 STUB files, filled TODO sections in 38 THIN files
- **GemClaw**: Removed 15 duplicate skill definition files (backed up) — all skills now live in L3
- **PiWorker-OS**: Removed 11 empty plugin stubs + 2 core files (plugin-gateway.ts, skill.ts) — plugin system migrated to L3

### Cleanup Phase 2 (2026-05-16 v2)
- **GemClaw**: +33 backup files deleted = ~6,900 lines stale code removed; 3 unused deps removed; 2 dead Firebase imports removed; 1 typo fixed
- **PiWorker-OS**: plugins/ deleted entirely (11 dirs, 38 files, ~865 lines stubs); package.json fixed
- **iqra**: +7 MemoryClient API routes added, 2 LanceDBPlugin leftovers fixed

### IQRA Deep Cleanup (2026-05-16 v3)
- `tsconfig.json.backup` — حذف
- 4 empty dirs + 3 `__pycache__` — حذف
- `qdrant.ts` → `reflection-store.ts` — rename + update 3 importers + function rename
- `pattern_memory.ts` — syntax error fix (extra `}`)
- `sovereign_identity.ts` — removed `${deepMemories}` (undefined var)
- `memory_governor.ts` — added missing `WARM_LIMIT` constant
- `05-rewards/` — unified constants (engine.ts imports from types.ts)

## تفصيل package-lock.json (6 ملفات)

| الريبو | الملف | سطور |
|-------|-------|------|
| GemClaw | `package-lock.json` | 22,005 |
| IQRA | `package-lock.json` | 15,412 |
| axiomid-project | `package-lock.json` | 11,395 |
| GemClaw | `functions/package-lock.json` | 7,451 |
| PiWorker-OS | `package-lock.json` | 2,785 |
| aix-agent-skills | `aix-constitutional-runtime/package-lock.json` | 608 |
| **المجموع** | | **59,656** |

### تكرار dependencies (35%)
- 140 تثبيت عبر 7 ريپوزات، 91 پكيدج unique فقط
- `typescript` مكرر في 6 ريپوزات، `@types/node` في 5، `next`/`react` في 3
- pnpm monorepo يخلي 59,656 سطر → ~10,000 سطر

## Real Code (بعد استبعاد locks + PNG binaries)

| الفئة | سطور |
|-------|------|
| All files (wc -l) | 214,200 |
| − package-lock.json (6 files) | −59,656 |
| − PNG binaries counted as lines | −~18,000 |
| **الكود الحقيقي** | **~136,544** |
| − MD/YAML/CSS/JSON config | −~30,389 |
| **الكود الفعلي (TS/JS/Python/Go)** | **~124,155** |

ملاحظة: لو تم monorepo بـ pnpm (lock واحد بدل 6)، الـ total هيكون **~116K** بدل 136K.

## ملاحظات
- **العد الجديد (v3):** 214,200 lines إجمالي (بما فيهم package-lock.json + PNG binaries)
- **الكود الحقيقي**: ~136,544 lines (بدون locks + PNG)
- **الكود الفعلي**: 124,155 lines (بدون JSON/MD/YAML/CSS/locks/PNG)
- **TypeScript** = 63% من الكود الفعلي — اللغة المهيمنة بـ 5 من 7 ريپوزات
- **package-lock.json** = 59,656 سطر (28% من الـ total) — أغلبها في GemClaw (29,456)
- **Last counted with sub-agents**: 2026-05-16 (7 sub-agents, one per repo)
