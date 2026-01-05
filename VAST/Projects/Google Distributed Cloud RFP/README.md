---
type: projects
title: Google Distributed Cloud RFP
created: '2026-01-03'
last_updated: '2025-12-15'
status: active
auto_created: true
tags:
- type/projects
- needs-review
- status/active
last_contact: '2025-12-15'
---

# Google Distributed Cloud RFP

## Status

| Field | Value |
|-------|-------|
| **Status** | active |
| **Owner** | Leo |

## Overview

Response effort to Google Distributed Cloud RFP to replace NetApp as storage partner, with heavy emphasis on air-gapped/dark-site readiness, compliance evidence, and operational model details.

## Open Tasks

```dataview
TASK
FROM this.file.folder
WHERE !completed
SORT due ASC
```

## Recent Context

- 2025-12-15: [[2025-12-15 - Google GDC RFP review]] (via Google)

- 2025-11-14: [[2025-11-14 - GDC RFP federal coordination]] (via Google)

- 2025-11-13: [[2025-11-13 - GDC RFP security and ops]] (via Google)

- 2025-11-07: [[2025-11-07 - Org map and cloud strategy]] (via Jeff Denworth)

- 2025-11-07: 2025-11-07 - Org map and cloud focus (via Jeff Denworth)

- 2025-10-31: [[2025-10-31 - Aligning on VAST cloud strategy]] (via VAST)

- 2025-11-07: [[2025-11-07 - Hyperscaler strategy Google and Microsoft]] (via Jonsi Stephenson)

- 2025-12-17: Mentioned in: Google GDC Storage RFP follow-up: FIPS, SEDs, BYOH partners, and scheduling next review

- 2025-12-15: Internal email thread between Jason Vallery, Alon Horev, and Tomer Hagay to answer Google Distribute...

- 2026-01-05: Mentioned in: Weekly status: Azure Marketplace action items (SKU change request, GDC RFP deck, MAI unified cache pricing)
## Key Facts

- Google requested a one-hour call for VAST Data to walk through and clarify the GDC Storage RFP proposal submission, including FIPS compliance, pricing scope, SEDs, and BYOH partner options.

- Jeff Denworth requested an updated deck to support the Google Distributed Cloud (GDC) RFP effort.
## Topics

- Google Distributed Cloud (GDC) RFP follow-up questions on encryption and compliance

- FIPS considerations for data-at-rest encryption and self-encrypting drives (SEDs)

- VAST encryption key granularity via encryption groups at tenant and path levels

- Mapping encryption groups to S3 buckets, NFS exports, and encrypted paths

- S3 SSE-C support via x-amz-server-side-encryption-customer-* headers in VAST 5.4

## Key Decisions

- Route Google Distributed Cloud (GDC) RFP encryption follow-up questions to Violet as the primary subject matter expert.
