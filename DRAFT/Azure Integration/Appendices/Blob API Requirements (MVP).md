# Blob API Requirements (MVP)

**Purpose:** Define the minimum high‑fidelity subset of the Azure Blob REST API that VAST must implement so Azure-native data movers and AI client libraries work without client-side refactoring.

**Reference spec:** https://learn.microsoft.com/en-us/rest/api/storageservices/blob-service-rest-api

## Goals and Non-Goals

### Primary Goal

Enable standard Azure data movers (AzCopy, Azure Storage Mover, VAST SyncEngine) and AI-centric libraries (boostedblob, `azure-storage-blob` Python SDK) to interact with VAST as if it were a standard Azure Blob endpoint.

### Non-Goals

- Full emulation of Azure Blob Storage (page blobs, append blobs, full feature surface).
- ADLS Gen2 / HNS semantics (`dfs.core.windows.net` endpoint, ACL model, atomic directory renames).
- Table/Queue services (not Blob).

### Success Criteria

- `azcopy copy https://blob.core.windows.net/... https://vast-cluster/...` succeeds.
- Standard Python training scripts using `BlobServiceClient` function correctly for list/read/write operations (targeted subset).
- Server‑side copy operations (`PutBlockFromURL`) saturate available WAN links.

## Scope and Object Model

- **Blob type:** Block Blobs only (AI datasets/checkpoints/models overwhelmingly use block blobs).
- **Endpoint type:** Emulate the Blob Service endpoint (`blob.core.windows.net`), not the DFS endpoint (`dfs.core.windows.net`).
- **Directory model:** Directories are virtual (`/` delimiter). MVP does not support atomic directory renames or ACL semantics.

## Technical Specification (MVP)

This section defines the *compatibility contract* VAST will implement, including explicit mapping between Azure Blob concepts, VAST concepts, and S3 concepts (for multi‑protocol coherence).

### Endpoint & Namespace Model

VAST MUST support both request forms (production-friendly and emulator-style):

- **Virtual-host style (preferred):** `https://{account}.{blob_suffix}/{container}/{blob}`
- **Path style (emulator-compatible):** `https://{blob_host}/{account}/{container}/{blob}`

Namespace rules:

- **`{account}` (Azure “storage account”):** a logical tenant/routing label used for SAS/shared-key validation and request routing. In OAuth-only deployments, `{account}` MAY be treated as a pure routing label.
- **`{container}`:** maps **1:1** to a **VAST bucket** (and an **S3 bucket**) of the same name.
- **`{blob}`:** the remainder of the path after `{container}/`, URL-decoded once per RFC 3986. `/` is treated as a virtual directory delimiter.

Multi‑protocol safety constraints (Blob + S3 + NFS/SMB):

- **No file/dir conflicts:** a committed object at `a` MUST prevent creating any object under `a/` and vice-versa (filesystem coherence).
- **No empty or special path segments:** reject names containing `//`, `/.`, `/..`, or ending with `/.` or `/..`.
- **Reserved characters:** reject NUL; for SMB compatibility, prefer a conservative “portable path” subset (see: [Terminology & Conventions](Terminology%20%26%20Conventions.md)) and treat non-portable names as out-of-scope for file-protocol access.

**Note:** Azure Blob Storage allows many of these key patterns; these restrictions exist to guarantee coherent behavior across protocols in a shared VAST namespace.

### Concept Mapping (Blob ↔ VAST ↔ S3)

| Azure Blob concept | VAST concept (target) | S3 concept | Compatibility notes |
| --- | --- | --- | --- |
| Storage account | Tenant / endpoint routing label | (none; endpoint/tenant) | `{account}` is derived from host/path; used for SAS/shared-key validation if enabled. |
| Container | Bucket / top-level namespace root | Bucket | Names align exactly. Container policies map to bucket policies (MVP coarse-grain). |
| Blob name | Object path within bucket | Object key | Same canonical string across Blob + S3; `/` denotes “virtual directories”. |
| Block (uncommitted) | Staged part | Multipart upload part | Invisible until commit (`PutBlockList` / MPU complete). |
| `ETag` | Strong version identifier | `ETag` | Opaque; MUST NOT be treated as MD5. Prefer same value across protocols. |
| `Last-Modified` | Commit timestamp / mtime | `Last-Modified` | RFC 1123; stable for sync/diff logic. |
| `x-ms-meta-*` | User metadata KV | `x-amz-meta-*` | Keys normalized to lowercase; values preserved byte-for-byte. |
| `Content-Type`, `Content-Encoding`, `Cache-Control`, `Content-MD5` | System metadata | System metadata | Persist and return consistently across protocols. |
| SAS token | Pre-signed authorization | Pre-signed URL | MVP targets OAuth; SAS/shared-key are compatibility modes. |
| Shared Key | Account key | Access key/secret | Compatibility mode only; not required if OAuth is sufficient. |
| Copy from URL (`Put*FromURL`) | Server-side fetch + stage/commit | CopyObject / UploadPartCopy | Required for lake→edge hydration; supports byte-range fetch. |

### Example: Same Object Across Protocols

Given `{container} = datasets` and `{blob} = imagenet/train/000001.jpg`:

- **Blob:** `https://{account}.{blob_suffix}/datasets/imagenet/train/000001.jpg`
- **S3:** `s3://datasets/imagenet/train/000001.jpg`
- **NFS/SMB (if exported):** `{export_root}/datasets/imagenet/train/000001.jpg`

### Metadata & Header Translation (Blob ↔ S3)

To keep multi‑protocol clients coherent, define one internal metadata model and translate protocol-specific headers at the edge:

- **User metadata**
  - **Blob ingress:** accept `x-ms-meta-*` headers and store as user metadata with keys normalized to lowercase.
  - **S3 ingress:** accept `x-amz-meta-*` headers and store into the same user metadata map (lowercase keys).
  - **Egress:** return all stored keys as `x-ms-meta-*` (Blob) or `x-amz-meta-*` (S3); preserve values byte-for-byte.
- **System metadata**
  - Persist and return `Content-Type`, `Content-Encoding`, `Cache-Control`, and `Content-MD5` consistently across protocols.
  - If a client supplies `Content-MD5` on upload, validate it and reject mismatches (`400 Bad Request`) rather than silently accepting corrupt uploads.

### Multi‑Protocol Coherence Rules (MVP)

The Blob façade is not “a separate store”; it is another access path into the same VAST namespace as S3 and file protocols. MVP guarantees:

- **Read-after-write consistency:** after a successful `PutBlob` or `PutBlockList`, subsequent `HEAD`/`GET` and list operations MUST reflect the committed object (no “eventual list” behavior).
- **Atomic publication:** uncommitted blocks (from `PutBlock`/`PutBlockFromURL`) MUST NOT be visible via Blob, S3, NFS, or SMB until the corresponding `PutBlockList` commits them.
- **Single-writer versioning:** overwrites create a new version (`ETag` changes). Conditional headers (`If-Match`, `If-None-Match`, `If-Range`) gate updates/reads based on that version.
- **Metadata coherence:** the committed object’s system metadata + user metadata MUST be readable consistently via Blob (`x-ms-meta-*` / headers) and S3 (`x-amz-meta-*` / headers) for the same object key.

### Upload Semantics (Block Blob ↔ Multipart Upload)

Design intent: `PutBlock`/`PutBlockList` is semantically equivalent to an S3 multipart upload (stage parts → atomically complete).

- **`PutBlob` (single-shot):** atomic create/overwrite of a Block Blob.
- **`PutBlock` / `PutBlockFromURL` (stage):**
  - `blockid` is Base64-encoded; after decoding, enforce Azure’s 64-byte block ID limit.
  - Reusing a `blockid` overwrites the previous uncommitted block of the same ID.
  - `PutBlockFromURL` MUST support `x-ms-copy-source` and byte-range staging via `x-ms-source-range`.
- **`PutBlockList` (commit):**
  - Commits a blob atomically; the block list order defines the final byte stream.
  - Finalizes `ETag` and `Last-Modified` and makes the object visible across all protocols.

### Listing Semantics (Prefix/Delimiter/Pagination)

VAST MUST implement Azure list semantics in a way that maps cleanly to prefix/delimiter listing patterns used by S3 and hierarchical file browsing:

- **Ordering:** lexicographic by blob name.
- **Virtual directories:** `delimiter=/` returns `BlobPrefix` entries for “folders” (common prefixes) plus `Blob` entries for objects at the current level.
- **Pagination:** honor `maxresults` and `marker`; return `NextMarker` correctly (SDK parsers depend on it).
- **Property fidelity:** include the properties used by AzCopy/SDKs for diff logic (at minimum `Last-Modified`, `ETag`, `Content-Length`, `Content-Type`, `Content-MD5`, and access tier when set).

## MVP REST Surface Area

### Container Operations (Minimum Needed for Tools/SDKs)

- Create container (`PUT`)
- Delete container (`DELETE`)
- Get container properties (`HEAD`) — required by AzCopy validation checks
- List containers (`GET`) — required for root-level browsing

### Uploads (Block Blobs)

- Put Blob
  - Must respect `x-ms-blob-type: BlockBlob`
- Put Block
  - Must accept Base64-encoded block IDs
  - Must support out-of-order block arrival
- Put Block List
  - Commits a blob from uncommitted blocks
  - Must support latest/committed/uncommitted block lists
  - Finalizes `ETag` and `Last-Modified`
- Get Block List (`GET ?comp=blocklist`)
  - Strongly recommended for upload resume and integrity workflows (AzCopy and some SDK flows)

### Downloads / Existence

- Get Blob (range)
  - Range support is mandatory for AI loaders and resume-capable tools
  - Must return `206 Partial Content` for ranges (not `200 OK`)
- Head Blob / Get blob properties (`HEAD`)
  - Used by clients to check existence, size (`Content-Length`), and freshness (`ETag`)

### Listing

- List Blobs (prefix/delimiter/pagination)
  - XML fidelity is mandatory: SDK parsers are brittle
  - Must support `delimiter=/` to emulate folder browsing
  - Must support `maxresults` and return a valid `NextMarker` for continuation

### Deletes

- Delete Blob
  - Must return `202 Accepted` on success
  - Must return `404 Not Found` with an XML error body if the blob is missing

### Server‑Side Copy (Hydration Engine)

- `PutBlobFromURL` / `PutBlockFromURL` (and fallbacks)
  - This is the engine for “central lake → edge” hydration
  - VAST acts as the client, fetching data from the source URL provided in the header
  - Critical for large objects: AzCopy splits large files into blocks; VAST must fetch specific byte ranges (`x-ms-source-range`) from the source URL and stage them as blocks
  - Enables parallelized server-side copying of multi‑GB checkpoints

### Metadata / Properties

- User metadata: support `x-ms-meta-*` headers on `PUT`/`HEAD`
- System properties: persist `Content-Type`, `Content-Encoding`, `Cache-Control`, `Content-Disposition`, and `Content-Language`
- Blob MD5: accept `x-ms-blob-content-md5` on upload/commit and return `Content-MD5` on `HEAD` (and on `GET` when available)
- Block blob access tier: accept `x-ms-access-tier` (e.g., `Hot`, `Cool`, `Archive`) on upload/commit and return `x-ms-access-tier` on `HEAD`

## Semantics Contract (Compatibility‑Critical)

### Headers

- `ETag`: strong ETags (quoted strings). MUST be an opaque version identifier (not MD5) and should be consistent across Blob and S3 for the same object.
- `Last-Modified`: RFC 1123 format (critical for sync logic: “copy only if newer”) and should align with file/S3 mtime semantics for the committed object.
- `Content-MD5`: if provided by the client as a *request integrity* check, validate and reject mismatches (`400 Bad Request`).
  - For stored blob MD5, AzCopy uses `x-ms-blob-content-md5` on upload/commit and expects `Content-MD5` to be returned on `HEAD`/`GET`.

### Conditional Requests

- Optimistic concurrency: support `If-Match` and `If-None-Match`.
- Range resume: support `If-Range` to ensure data hasn’t changed while resuming a download.

### Error Model (XML Errors)

Azure SDKs do not rely solely on HTTP status codes; they parse the XML error body to determine retry logic.

- Requirement: on 4xx/5xx errors, return `Content-Type: application/xml` with the standard Azure error schema.
- Critical codes: `BlobNotFound`, `ContainerNotFound`, `ContainerAlreadyExists`, `LeaseIdMissing` (if locking is touched).

### Throttling Model

- Behavior: on overload, return `503 Service Unavailable`.
- Retry behavior: include the `Retry-After` header.
- Avoid `429`: while Azure uses `429`, AzCopy handles `503` more gracefully for “server busy” states in third‑party implementations.

## Authentication and Authorization (MVP)

### Entra ID / OAuth Token Validation (MVP Requirement)

- Mechanism: validate JWT signatures using Microsoft’s OIDC discovery keys.
- Identity mapping: map token `oid` (object ID) or `appid` (service principal ID) to a VAST user/group for permission checks.

### Managed Identity Patterns

- Support access from Azure resources using system-assigned or user-assigned managed identities.
- Validate the specific token audience claims used by MSI.

### SAS Tokens (Compatibility Mode)

- Support service SAS (container/blob scope).
- Validation: recompute the signature based on parameters (`sp`, `st`, `se`, `sv`, etc.) and the shared account key to allow/deny the request.

### Shared Key (Compatibility Mode)

- Legacy support for tools configured with connection strings.
- Validation: implement the CanonicalizedResource/CanonicalizedHeaders signing algorithm defined in Azure docs.

### Authorization Mapping

- MVP: simple mapping — Azure container → VAST bucket (same name); container access policy → bucket policy, using the same underlying principal model as S3 and file protocols.
- Roadmap: fine‑grained ACL mapping (POSIX ACLs ↔ Azure RBAC) is deferred.

## Performance Targets

- Concurrency: support 1,000+ concurrent `PutBlock` requests per VIP to saturate high‑bandwidth links.
- Keep‑alive: aggressive HTTP/1.1 connection reuse to avoid TLS handshake overhead on small operations.
- Large objects: validate support for 4TB+ objects (via block list).

## Compatibility Harness (Gates)

### AzCopy Gate

- Test: use upstream AzCopy “smoke tests” (`testSuite/scripts`) as the primary compatibility gate (parameterized by SAS URLs, so it can target partner endpoints).
- Pass criteria: pass Gate A (Block Blob MVP) as defined in [AzCopy Test Suites & Acceptance](AzCopy%20Test%20Suites%20%26%20Acceptance.md); expand to Gate B/C only if scope requires page blobs / DFS / Files.

### High‑Concurrency Clients Gate

- Test: `boostedblob` (used by OpenAI).
- Why: these libraries aggressively optimize concurrency/pipelining; server‑side locking bottlenecks show up quickly.

### Azure Storage SDK Gate (Python)

- Test: `azure-storage-blob` flows:

```python
ContainerClient.list_blobs()
BlobClient.upload_blob(max_concurrency=N)
BlobClient.download_blob()
```

## Forward Compatibility & API Drift Strategy

- Versioning: advertise a specific Azure Storage API version (e.g., `2021-08-06`).
- Compatibility: accept older `x-ms-version` values (e.g., `2017-04-17` used by some harnesses) and apply the same MVP semantics.
- Drift policy: ignore unknown parameters/headers rather than failing with `400`, so newer clients degrade gracefully.

## Open Items

Tracked in: [TODO](../TODO.md)
