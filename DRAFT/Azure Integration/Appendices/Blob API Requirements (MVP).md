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
- System properties: persist `Content-Type`, `Content-Encoding`, `Content-MD5`, and `Cache-Control`

## Semantics Contract (Compatibility‑Critical)

### Headers

- `ETag`: strong ETags (quoted strings). VAST internal versions must map deterministically.
- `Last-Modified`: RFC 1123 format (critical for sync logic: “copy only if newer”).
- `Content-MD5`: if provided by the client on upload, VAST must validate and reject mismatches (`400 Bad Request`).

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

- MVP: simple mapping — Azure container → VAST bucket; container access policy → bucket policy.
- Roadmap: fine‑grained ACL mapping (POSIX ACLs ↔ Azure RBAC) is deferred.

## Performance Targets

- Concurrency: support 1,000+ concurrent `PutBlock` requests per VIP to saturate high‑bandwidth links.
- Keep‑alive: aggressive HTTP/1.1 connection reuse to avoid TLS handshake overhead on small operations.
- Large objects: validate support for 4TB+ objects (via block list).

## Compatibility Harness (Gates)

### AzCopy Gate

- Test: full suite of AzCopy copy (upload/download), sync (differential), and remove.
- Pass criteria: zero errors, checksum validation passes, no manual flags required (other than endpoint override).

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
- Drift policy: ignore unknown parameters/headers rather than failing with `400`, so newer clients degrade gracefully.

## Open Items

Tracked in: [TODO](../TODO.md)
