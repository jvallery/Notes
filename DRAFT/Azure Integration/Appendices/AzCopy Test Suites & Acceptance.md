# AzCopy Test Suites & Acceptance (Blob API)

**Purpose:** Document what test suites exist in `Azure/azure-storage-azcopy` and how to use them as an acceptance gate for the VAST Blob API façade.

**Upstream repo:** https://github.com/Azure/azure-storage-azcopy

## 1) What Tests Exist in AzCopy (Upstream)

AzCopy has multiple “layers” of tests. Not all of them are usable as‑is for validating a non‑Azure Blob endpoint.

### A) Go “unit” tests (some are live / integration)

- Location: `cmd/`, `common/`, `ste/`, `sddl/`, `traverser/`, `mock_server/` (Go `_test.go` files).
- How CI runs them: `go test ./cmd`, `go test ./common`, `go test ./common/parallel`, `go test ./ste`, `go test ./sddl` (see `azure-pipelines.yml` + `azurePipelineTemplates/run-ut.yml`).
- Reality: many “unit” tests assume Azure URLs such as `https://{account}.blob.core.windows.net/…` and/or require real Azure credentials in environment variables.
- Implication: these are excellent for understanding client expectations, but they are **not directly runnable against a partner/custom Blob endpoint** without modifying the tests (or standing up DNS that makes `*.blob.core.windows.net` resolve to your endpoint, which is not realistic).

### B) Go E2E tests (new framework)

- Location: `e2etest/`.
- How CI runs them: `go test ./e2etest -tags olde2etest` and `go test ./e2etest -run "TestNewE2E/.*"` (see `azurePipelineTemplates/run-e2e.yml`).
- Also assumes Azure endpoint suffixes (`blob.core.windows.net`, `dfs.core.windows.net`, `file.core.windows.net`) in helpers.
- Implication: same as above — useful for coverage discovery, not a drop-in harness for a partner endpoint.

### C) “Smoke tests” (parameterized, best fit for partner endpoints)

- Location: `testSuite/`
  - Runner: `testSuite/scripts/run.py` (Python `unittest`)
  - Test cases: `testSuite/scripts/test_*.py`
  - Validator + utilities: `go build ./testSuite` (produces a `test-validator` binary)
- How CI runs it (Linux): builds AzCopy + the validator, then runs `python ./testSuite/scripts/run.py`.
- Key property: the smoke tests are **parameterized by SAS URLs** (for Blob/File) and can therefore be pointed at **any** endpoint that is compatible with the Azure Blob REST API + the Azure Go SDK.
- Implication: this is the most practical upstream test suite to treat as an acceptance gate for the VAST Blob API façade.

## 2) Recommended “AzCopy Gate” for the VAST Blob API Façade

The upstream smoke runner (`testSuite/scripts/run.py`) includes tests for *non‑MVP* surfaces (page blobs, DFS/BlobFS, Azure Files, S3, GCP). For a Blob REST façade MVP, define explicit gating subsets:

### Gate A — Blob API MVP (Block Blob)

Run these upstream smoke tests:

- `testSuite/scripts/test_upload_block_blob.py` (`Block_Upload_User_Scenarios`)
- `testSuite/scripts/test_blob_download.py` (`Blob_Download_User_Scenario`)
- `testSuite/scripts/test_blob_sync.py` (`Blob_Sync_User_Scenario`)
- `testSuite/scripts/test_blob_piping.py` (`BlobPipingTests`)
- `testSuite/scripts/test_service_to_service_copy.py` (`Service_2_Service_Copy_User_Scenario`)
  - Configure `S3_TESTS_OFF=1` and `GCP_TESTS_OFF=1` to skip non‑Blob sources.

### Gate B — Blob parity expansion (adds Page Blob)

Add:

- `testSuite/scripts/test_upload_page_blob.py` (`PageBlob_Upload_User_Scenarios`)

This expands the required REST surface substantially (page blob create/put page/get page ranges, alignment rules, page tiers).

### Gate C — Multi-service parity expansion

Add BlobFS/DFS and Azure Files suites and (optionally) S3/GCP service‑to‑service tests. This is outside the Blob façade MVP described in [Blob API Requirements (MVP)](Blob%20API%20Requirements%20%28MVP%29.md).

## 3) Running the Upstream Smoke Tests Against a Partner Endpoint

### Build artifacts

From the AzCopy repo root:

- Build AzCopy: `go build -o azcopy`
- Build the validator: `go build -o test-validator ./testSuite`

### Environment variables (minimal for Gate A)

Set these before running tests:

- `AZCOPY_EXECUTABLE_PATH` = absolute path to `azcopy`
- `TEST_SUITE_EXECUTABLE_LOCATION` = absolute path to `test-validator`
- `TEST_DIRECTORY_PATH` = local working directory (tests create `test_data/` under this)
- `CONTAINER_SAS_URL` = destination container URL *with SAS* for Blob tests (target your VAST Blob façade)
- `S2S_SRC_BLOB_ACCOUNT_SAS_URL` = Azure Blob account/container SAS URL used as *source* for `Put*FromURL` tests (real Azure recommended)
- `S2S_DST_BLOB_ACCOUNT_SAS_URL` = destination account/container SAS URL (target your VAST Blob façade)
- Disable non‑Blob sources: `S3_TESTS_OFF=1`, `GCP_TESTS_OFF=1`

Notes:

- The upstream runner supports reading a `test_suite_config.ini`, but it is optional if env vars are already set.
- The smoke tests will create and delete blobs inside the configured containers/accounts.

### Execute Gate A (example)

Run from `testSuite/scripts/` so `utility.py` imports resolve:

- `python -m unittest test_upload_block_blob.Block_Upload_User_Scenarios`
- `python -m unittest test_blob_download.Blob_Download_User_Scenario`
- `python -m unittest test_blob_sync.Blob_Sync_User_Scenario`
- `python -m unittest test_blob_piping.BlobPipingTests`
- `python -m unittest test_service_to_service_copy.Service_2_Service_Copy_User_Scenario`

## 4) Blob API Requirements Implied by the Smoke Tests (MVP)

Gate A exercises AzCopy via the Azure Go SDK (`sdk/storage/azblob`) and the validator uses SDK operations directly. To pass Gate A, the VAST Blob façade must support (at minimum):

### Block Blob upload/download core

- `PUT Blob` (single-shot uploads)
- `PUT Block` + `PUT Block List` (chunked uploads)
- `GET Block List` (`comp=blocklist`) for verification and some resume flows
- `GET Blob` (range + full) and `HEAD Blob` (`GetProperties`)
- `DELETE Blob` (including tolerant handling of `x-ms-delete-snapshots: include`)
- `GET List Blobs` (flat + prefix/delimiter semantics used by `sync` and directory-style operations)

### Properties + metadata

- Persist and return:
  - `x-ms-meta-*`
  - `Content-Type`, `Content-Encoding`, `Cache-Control`, `Content-Disposition`, `Content-Language`
  - Blob MD5:
    - accept `x-ms-blob-content-md5` on upload/commit
    - return `Content-MD5` on `HEAD` and (when available) `GET`
  - Block blob tier:
    - accept `x-ms-access-tier` (e.g., `Hot`, `Cool`, `Archive`) on upload/commit
    - return `x-ms-access-tier` on `HEAD` (`GetProperties`)
- API version tolerance:
  - the validator sets `x-ms-version` via `ServiceAPIVersionOverride` (commonly `2017-04-17`); the façade must accept older `x-ms-version` values and behave correctly.

### Service-to-service copy (hydration)

To support lake→edge hydration scenarios and AzCopy S2S tests:

- `PutBlobFromURL` (`UploadBlobFromURL` in the Go SDK) for small objects
- `PutBlockFromURL` (`StageBlockFromURL` in the Go SDK) with `x-ms-source-range` for large objects
- `PutBlockList` to commit
- Support (or safely ignore) `x-ms-copy-source-authorization` when copying from protected sources.

## 5) Using This to Refine MVP Scope

If “pass AzCopy tests” is the acceptance criterion, start by explicitly choosing the gate level (A/B/C) and treating the corresponding REST surface as the MVP scope. Gate A aligns to the current definition in [Blob API Requirements (MVP)](Blob%20API%20Requirements%20%28MVP%29.md), with the addition of access-tier + full property/header fidelity needed by the smoke tests.
