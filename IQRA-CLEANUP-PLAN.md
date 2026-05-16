# 🧹 IQRA Cleanup Plan — 72K → 60K

## P0 — يحذف فوراً (مؤكد Dead)

| الملف | الحجم | السبب |
|-------|-------|-------|
| FAILURES.md (00-manifest) | 582 lines | Auto-generated, يعاد إنشاؤه تلقائياً |
| iqra_ingest_worker.ts | 3 lines | Stub فاضي |
| simple.test.ts | 5 lines | Test placeholder |
| debug_alias.test.ts | 8 lines | Debug temp file |
| test_discovery.ts | 9 lines | Unused script |
| verify_unification.ts | 11 lines | Temp verification |
| mission_control.e2e.ts | 14 lines | Stub test |
| curiosity_simple.test.ts | 20 lines | Stub test |
| **المجموع P0** | **~652 lines** | |

## P1 — يحتاج فحص (Dead محتمل)

| الملف | الحجم | الفحص |
|-------|-------|--------|
| `src/scripts_v2/*` العديد | ~5 files | هل scripts لسه مستخدمة؟ |
| `src/tests/unit/` tests قديمة | ? | Test لـ code محذوف؟ |
| `.iqra/` runtime cache | ? | Auto-generated, آمن يتشال |
| Go test files (*_test.go) | ~1,600 lines | Go tests — مفيدة، تبقى |

## P2 — Clean Room (ينقل لـ L3 بدل ما يتشال)

| الملف | الحجم | المصير |
|-------|-------|--------|
| `08-cognitive/skills/inverse_design.ts` | 87 lines | ✅ نقل لـ L3 |
| `08-cognitive/skills/topological_analyzer.ts` | 82 lines | ✅ نقل لـ L3 |
| `13-utils/sovereign_cipher.ts` | ~150 lines | 🆕 Skill للخدمات |

## التنفيذ (بالترتيب)
1. حذف P0 stubs
2. فحص P1 scripts
3. حذف P1 المؤكد
4. Go test files: تبقى (قيمة)
5. .iqra/ cache: يحذف (auto-generated)

## الإجمالي المتوقع
- P0: ~650 lines
- P1: ~500 lines (تقديري)
- Clean Room: ~200 lines (ينقل، لا يحذف)
- **صافي التنظيف: ~1,150 lines**
- **المتبقي: ~70,000 lines** (طبيعي للـ brain)
