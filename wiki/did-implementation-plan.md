---
title: "DID Implementation Plan — axiomid.app + aix-format"
last_updated: "2026-05-18"
status: "draft"
tags: [did, identity, plan, implementation, axiomid, aix-format]
layer: "L0, L1"
related:
  - "[[L0-axiomid]]"
  - "[[L1-aix-format]]"
  - "[[decisions]]"
  - "[[pi-network]]"
---

# DID Implementation Plan

> بناءً على W3C DID Core v1.0 + DIF standards
> axiomid-project (L0) = مصدر الهوية | aix-format (L1) = هيكل الهوية

## Part 1: axiomid-project — Root Authority (L0)

### 1.1 Identity Schema (Prisma)

```prisma
model DID {
  id              String   @id @default(cuid())
  did             String   @unique             // did:axiom:axiomid.app:<uid>
  userId          String   @unique
  user            User     @relation(fields: [userId], references: [id])
  publicKeyEd25519 String                     // multibase encoded
  status          DIDStatus @default(ACTIVE)  // ACTIVE | ROTATED | REVOKED | COMPROMISED
  revokedAt       DateTime?
  revokedReason   String?                      // hack | abuse | key_loss | migration
  createdAt       DateTime  @default(now())
  updatedAt       DateTime  @updatedAt
}

model DIDGuardian {
  id           String   @id @default(cuid())
  didId        String
  did          DID      @relation(fields: [didId], references: [id])
  guardianDid  String                        // did:axiom of guardian
  label        String                        // "family" | "device" | "institution"
  weight       Int      @default(1)
  assignedAt   DateTime @default(now())
}

model DIDRecovery {
  id              String   @id @default(cuid())
  didId           String
  did             DID      @relation(fields: [didId], references: [id])
  threshold       Int      @default(2)       // M-of-N: minimum approvals
  totalGuardians  Int      @default(3)
  createdAt       DateTime @default(now())
  lastRotation    DateTime?
}

enum DIDStatus {
  ACTIVE
  ROTATED
  REVOKED
  COMPROMISED
}
```

### 1.2 DID Revocation

**آلية الإلغاء (Revocation) — 3 مستويات:**

#### Level 1: Soft Revocation (Key Rotation)
- الـ DID Controller يوقع طلب بـ private key قديم
- يتم إضافة `verificationMethod` جديد ونقل `authentication` إليه
- الـ key القديم يُضاف إلى `key_archive` مع timestamp
- DID Document يبقى ACTIVE لكن الـ key القديم revoked

#### Level 2: Hard Revocation (DID Deactivation)
- الـ DID يتغير حالته لـ `REVOKED`
- DID Document يُستبدل بـ "tombstone":
```json
{
  "id": "did:axiom:axiomid.app:abc123",
  "status": "REVOKED",
  "revokedAt": "2026-05-18T10:00:00Z",
  "reason": "key_compromise",
  "newDID": "did:axiom:axiomid.app:def456"
}
```
- `/api/auth/did/:did` يرجع 410 Gone
- أي Verifiable Credential صادرة بهذا الـ DID تصبح باطلة

#### Level 3: Abuse Revocation (Admin + DAO)
- في حالة إساءة استخدام الـ Agent
- يتطلب M-of-N multisig من الـ Guardians أو الـ DAO
- الـ User يضاف إلى القائمة السوداء مع hash لهويته
- يمكنه إنشاء DID جديد فقط بعد فترة تبريد (cool-off period)

**API Endpoints:**
```
POST   /api/did/create              ← إنشاء DID جديد
GET    /api/did/:did                ← استعلام DID Document
POST   /api/did/:did/rotate        ← تدوير المفاتيح
POST   /api/did/:did/revoke        ← إلغاء DID (soft/hard)
GET    /api/did/:did/status        ← حالة الـ DID
POST   /api/did/:did/recover       ← استرداد DID
```

### 1.3 Social Recovery

**آلية الاسترداد الاجتماعي:**

1. **Setup**: المستخدم يختار 3-5 Guardians (أصدقاء، أجهزة، مؤسسات)
2. **Threshold**: M-of-N (مثلاً 2 من 3)
3. **Recovery Flow**:
   ```
   Key Lost → POST /api/did/recover
   → Guardians يتلقون إشعار (email/push)
   → كل Guardian يوافق بـ signing challenge
   → M signatures تجمع → يتم تدوير الـ keys
   → DID Document يتم تحديثه مع `key_rotation` في TrustChain
   ```
4. **Guardian Types**:
   - **Human Guardians**: أصدقاء موثوقين (كل واحد عنده axiomid account)
   - **Device Guardians**: هاتف آخر، hardware key
   - **Institutional Guardians**: خدمة احتياطية (مؤقت)

**Endpoints:**
```
POST   /api/did/:did/guardians              ← تعيين Guardians
GET    /api/did/:did/guardians              ← قائمة Guardians
POST   /api/did/:did/guardians/:gid         ← تحديث Guardian
DELETE /api/did/:did/guardians/:gid         ← إزالة Guardian
POST   /api/did/recover/:did                ← بدء Recovery
GET    /api/did/recover/:did/status         ← حالة Recovery
POST   /api/did/recover/:did/approve       ← Guardian يوافق
```

### 1.4 DID Schema Documentation

توثيق كامل لـ DID Document الخاص بـ `did:axiom`:

```json
{
  "@context": [
    "https://www.w3.org/ns/did/v1",
    "https://w3id.org/security/suites/ed25519-2020/v1",
    "https://axiomid.app/ns/did/v1"
  ],
  "id": "did:axiom:axiomid.app:abc123",
  "alsoKnownAs": ["https://axiomid.app/u/username"],

  "controller": "did:axiom:axiomid.app:abc123",

  "verificationMethod": [{
    "id": "did:axiom:axiomid.app:abc123#key-1",
    "type": "Ed25519VerificationKey2020",
    "controller": "did:axiom:axiomid.app:abc123",
    "publicKeyMultibase": "z6MkhaXgBZDvB..."
  }],

  "authentication": [
    "did:axiom:axiomid.app:abc123#key-1"
  ],

  "assertionMethod": [
    "did:axiom:axiomid.app:abc123#key-1"
  ],

  "keyAgreement": [],

  "capabilityInvocation": [
    "did:axiom:axiomid.app:abc123#key-1"
  ],

  "capabilityDelegation": [],

  "service": [{
    "id": "did:axiom:axiomid.app:abc123#agent",
    "type": "AgentService",
    "serviceEndpoint": "https://axiomid.app/api/agent/did:axiom:axiomid.app:abc123"
  }, {
    "id": "did:axiom:axiomid.app:abc123#trustchain",
    "type": "TrustChainService",
    "serviceEndpoint": "https://axiomid.app/api/trustchain/did:axiom:axiomid.app:abc123"
  }],

  "axiom": {
    "tier": "Axiom",
    "status": "ACTIVE",
    "recovery": {
      "threshold": 2,
      "guardians": 3
    },
    "key_archive": [{
      "keyId": "#key-0",
      "rotatedAt": "2026-05-01T00:00:00Z",
      "reason": "scheduled_rotation"
    }],
    "permissions": {
      "agent": ["read", "write", "execute"],
      "admin": ["rotate", "revoke", "recover"]
    }
  }
}
---

## Part 2: aix-format — Protocol Body (L1)

### 2.1 Digital Signatures (JCS + Ed25519)

**باستخدام @axiom/identity الموجود:**

```typescript
import { sign, verify } from '@axiom/identity'

// التوقيع
const manifest = loadManifest('agent.aix.yaml')
const signature = await sign(manifest, privateKey)
// { "protected": <base64-header>, "payload": <base64-manifest>, "signature": <base64> }

// التحقق
const isValid = await verify(manifest, signature, didDocument)
// يعيد boolean + public key المستخدم
```

**تنسيق التوقيع في manifest:**

```yaml
security:
  signature:
    type: "JcsEd25519Signature2020"
    created: "2026-05-18T10:00:00Z"
    proofPurpose: "assertionMethod"
    verificationMethod: "did:axiom:axiomid.app:abc123#key-1"
    signatureValue: "z3pAVLMv6gmMN..."
  signer:
    did: "did:axiom:axiomid.app:abc123"
    domain: "axiomid.app"
```

### 2.2 TrustChain

سجل التعديلات حسب W3C PROV standard:

```yaml
trustchain:
  - event: "created"
    timestamp: "2026-05-01T00:00:00Z"
    signer: "did:axiom:axiomid.app:abc123#key-0"
    previous_hash: null
    hash: "sha256:a1b2c3d4..."
    signature: "z..."
    reason: "Initial creation"

  - event: "updated"
    timestamp: "2026-05-10T12:00:00Z"
    signer: "did:axiom:axiomid.app:abc123#key-1"
    previous_hash: "sha256:a1b2c3d4..."
    hash: "sha256:e5f6g7h8..."
    signature: "z..."
    reason: "Added skills section"
    diff_summary: "+15 lines, -3 lines"

  - event: "signed"
    timestamp: "2026-05-18T10:00:00Z"
    signer: "did:axiom:axiomid.app:abc123#key-1"
    previous_hash: "sha256:e5f6g7h8..."
    hash: "sha256:i9j0k1l2..."
    signature: "z..."
    reason: "Digital signature applied"
```

**API Endpoints:**
```
GET    /api/trustchain/:did              ← سجل التعديلات الكامل
GET    /api/trustchain/:did?from=TS      ← تعديلات منذ تاريخ
POST   /api/trustchain/:did/verify       ← التحقق من السلسلة
GET    /api/trustchain/:did/:hash        ← تفاصيل تعديل معين
```

### 2.3 Versioning

```yaml
meta:
  version: "2.1.0"
  semver:
    major: 2    # تغييرات غير متوافقة
    minor: 1    # إضافات متوافقة
    patch: 0    # إصلاحات
  last_updated: "2026-05-18T10:00:00Z"
  compatibility:
    min_schema_version: "2.0.0"
    max_schema_version: "3.0.0"

evolution:
  versions:
    - version: "1.0.0"
      date: "2026-01-15"
      changes: "Initial release"
    - version: "2.0.0"
      date: "2026-03-01"
      changes: "New identity layer, breaking changes"
    - version: "2.1.0"
      date: "2026-05-18"
      changes: "Added TrustChain, digital signatures"
  changelog:
    "2.1.0":
      added: ["trustchain", "permissions", "signing"]
      changed: ["identity_layer → DID-based"]
      deprecated: []
```

### 2.4 Permissions

```yaml
permissions:
  agent:
    - resource: "skills/*"
      actions: ["read", "execute"]
      condition: "owner"
    - resource: "memory/*"
      actions: ["read", "write"]
      condition: "owner"
  sharing:
    - resource: "skills/public"
      actions: ["read"]
      condition: "any_verified_did"
    - resource: "profile/public"
      actions: ["read"]
      condition: "any"
  delegation:
    - delegate: "did:axiom:axiomid.app:xyz789"
      resource: "skills/trading"
      actions: ["execute"]
      expires: "2026-12-31T00:00:00Z"
  admin:
    rotate_keys: "self"
    revoke_did: "self | guardians:2-of-3"
    update_permissions: "self"
```

## Implementation Order

### Phase 1 (Foundation) — Week 1
- [ ] axiomid: Prisma schema (DID, Guardian, Recovery models)
- [ ] axiomid: `/api/did/create` + `GET /api/did/:did`
- [ ] axiomid: توليد Ed25519 keypair عند إنشاء DID
- [ ] aix-format: استخدام `@axiom/identity` لتوقيع manifest
- [ ] aix-format: TrustChain السجل الأول (created)

### Phase 2 (Revocation + Rotation) — Week 2
- [ ] axiomid: `POST /api/did/:did/rotate`
- [ ] axiomid: `POST /api/did/:did/revoke` (soft + hard)
- [ ] axiomid: key_archive في DID Document
- [ ] axiomid: `GET /api/did/:did/status`
- [ ] aix-format: TrustChain يدعم rotation events

### Phase 3 (Social Recovery) — Week 3
- [ ] axiomid: Social Recovery setup + Guardian management
- [ ] axiomid: Recovery flow (challenge → approve → rotate)
- [ ] axiomid: إشعارات Guardians
- [ ] axiomid: M-of-N threshold verification

### Phase 4 (Permissions + Doc) — Week 4
- [ ] aix-format: Permissions section في manifest
- [ ] aix-format: Versioning + semver enforcement
- [ ] axiomid: Full DID schema documentation + playground
- [ ] aix-format: TrustChain verification CLI
- [ ] Integration tests بين axiomid و aix-format

## Security Considerations

- **Rate Limiting**: 5 recoveries per DID per 30 days
- **Revocation Irreversibility**: Hard revocation لا يمكن التراجع عنه
- **Guardian Collusion**: M-of-N مع random selection
- **Key Storage**: private keys في Prisma encrypted (`@default(cuid())` + DB encryption) — وليس في localStorage
- **CORS**: فقط `axiomid.app` + `app.axiomid.app` يمكنهما استدعاء API
