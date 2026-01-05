---
type: projects
title: Microsoft Azure Engagement Plan
created: '2026-01-03'
last_updated: '2025-12-15'
status: complete
auto_created: true
tags:
- type/projects
- needs-review
- status/complete
last_contact: '2026-01-02'
---

# Microsoft Azure Engagement Plan

## Status

| Field | Value |
|-------|-------|
| **Status** | complete |
| **Owner** | Jeff Denworth |

## Overview

Draft a Microsoft networking engagement plan focused on minimizing egress (e.g., ExpressRoute Direct Local) for VAST’s Azure offerings.

## Open Tasks

```dataview
TASK
FROM this.file.folder
WHERE !completed
SORT due ASC
```

## Recent Context

- 2025-12-15: [[2025-12-15 - Microsoft MAI strategy and next steps]] (via Microsoft)

- 2025-11-07: 2025-11-07 - Org map and cloud focus (via Jeff Denworth)

- 2025-09-16: [[2025-09-16 - Jason VAST role exploration]] (via Microsoft)

- 2025-10-27: [[2025-10-27 - VAST into Azure GTM]] (via Microsoft)

- 2025-10-30: [[2025-10-30 - Two VAST designs for MAI]] (via Microsoft)

- 2025-11-06: [[2025-11-06 - VAST adoption in Microsoft programs]] (via Microsoft)

- 2025-12-19: [[2025-12-19 - Microsoft strategy and SCO prep]] (via Microsoft)

- 2026-01-04: Mentioned in: Microsoft Weekly VAST GTM Meeting reschedule request (week of 2026-01-05)

- 2026-01-02: Google Docs notification email shows two open comments from Jonsi Stefansson on the document 'VAST a...
## Key Facts

- The Weekly VAST GTM Meeting is a recurring Microsoft Teams meeting used to coordinate Microsoft engagement status, pipeline, deal timelines, and Azure Marketplace onboarding blockers for VAST Data.

- The document text claims that integrating VAST with Azure Blob allows customers to place the long-tail dataset on HDD-based object storage while reserving VAST flash for the GPU-adjacent working set, as a hedge against flash component price volatility.

## Topics

- VAST cold data tiering to Azure Blob: VAST object format versus native Azure Blob format

- Ecosystem accessibility and direct readability of data stored in Azure Blob

- Messaging on flash supply constraints and VAST data reduction efficiencies (DRR)