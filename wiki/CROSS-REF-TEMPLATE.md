---
title: "CROSS-REF Template — لكل Repo"
last_updated: "2026-05-18"
status: "draft"
tags: [template, cross-ref, documentation]
layer: "all"
related:
  - "[[cross-repo-architecture]]"
  - "[[API-REGISTRY]]"
---

# CROSS-REF Template

> ينسخ هذا الملف في جذر كل repo كـ `CROSS-REF.md`

```markdown
# Cross-Ref: [REPO-NAME] — [REPO-DESCRIPTION]

> آخر تحديث: [DATE]

## Services التي نقدمها

| Service/API | Description | Consumers |
|-------------|-------------|-----------|
| `[endpoint]` | [وصف] | [قائمة الـ repos] |

## Services التي نستخدمها

| Service/API | Owner | Usage |
|-------------|-------|-------|
| `[endpoint]` | [axiomid/iqra/...] | [فين يستخدم] |

## Shared Types المستخدمة

| Type | Package | Usage |
|------|---------|-------|
| `User` | `@aix/shared-types` | [فين يستخدم] |

## Dependencies على Repos أخرى

| Dependency | Repo | Version | Usage |
|-----------|------|---------|-------|
| `MemoryClient` | iqra | ^1.0.0 | للوصول للذكريات |

## API Endpoints

### [endpoint name]

**Method**: POST
**Path**: `/api/...`
**Auth**: ...
**Request**:
\`\`\`typescript
interface Request {
  ...
}
\`\`\`
**Response**:
\`\`\`typescript
interface Response {
  ...
}
\`\`\`

---

## Automation (للـ agents)

هذا الملف يستخدم من قبل الـ AI agents في `aix-agent-skills` لفهم العلاقات بين الـ repos.

**الأمر**: `zero search --ref [REPO-NAME]`
**الـ agent** يقرأ هذا الملف قبل أي cross-repo عملية.
```
