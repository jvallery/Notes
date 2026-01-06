---
type: projects
title: Cloud
status: active
my_role: owner
description: Cloud platform strategy, multi-tenancy, operability, and marketplace readiness across hyperscalers.
last_contact: '2025-12-15'
created: '2026-01-05'
tags:
- type/projects
- status/active
- needs-review
---

# Cloud

**Owner**: Jason Vallery

## Status

| Field | Value |
|-------|-------|
| **Status** | active |
| **Owner** | Jason Vallery |
| **My Role** | owner |

## Overview

Workstream for VAST on Cloud: platform primitives, control plane stance, tenancy, operability/SLOs, and marketplace transactability.

## Open Tasks

```tasks
path includes VAST/Projects/Cloud/
not done
```

## Recent Context

- 2026-01-05: [[2026-01-05 - VAST Cloud SaaS operating model requirements draft DevOps, telemetry, 24x7 support]]
- 2025-12-15: [[2025-12-15 - Review requested- VAST on Cloud Course and Project Brief feedback due January 7, 2026]]
- 2025-11-14: [[2025-11-14 - Google Distributed Cloud RFP debrief and federal coordination air-gapped focus]]
- 2025-10-30: [[2025-10-30 - Cloud operations org design- distinct Customer Success, Support, and SRE roles with 2026-02-01 readiness target]]
- 2025-10-30: [[2025-10-30 - Cloud marketplace support operating model, hyperscaler priority, and readiness plan target 2026-02-01]]
- 2025-10-29: [[2025-10-29 - VAST on Cloud positioning, intake process, and near-term roadmap constraints VM shapes, marketplace automation, object storage integration]]
- 2025-10-28: [[2025-10-28 - Cloud BU leadership aligns on dual-track GTM- GCP Marketplace MVP launch plus hyperscaler-scale MAI storyline]]

- 2025-12-22: Mentioned in: Lior Genzel requested access to Google Doc: VAST and Azure Integration.docx
- 2026-01-05: Internal VAST thread coordinating a Microsoft workback plan, including a CoreWeave MFN-driven pricin...
- 2026-01-05: Mentioned in: Microsoft Teams meeting invite: Sync on PRD for VAST on Azure
- 2026-01-02: A Google Docs notification email captured two open comments from Jonsi Stefansson on the document 'V...
- 2025-12-01: Brian Evans alerted the PM team about RFE 0482 for NVIDIA DGX Cloud requesting unified visibility ac...
- 2025-12-01: Mentioned in: Karl Vietmeier asks for guidance on ownership of GDC and Azure Local opportunities
- 2026-01-05: Itzik Reich asked Noa Cohen whether TLS support for VAST Block protocol would ship in VAST release 5...
- 2026-01-05: Rob Benoit forwarded an approved Documentation RFE (Salesforce RFE 0538) tied to NTT DATA Japan Corp...
- 2025-12-15: Terika Dilworth asked the team to review and provide feedback on a draft VAST on Cloud training cour...
- 2025-12-11: Mentioned in: Microsoft requests Azure VoC for GPU performance testing, VAST plans to decline
## Key Facts

- No generally available, transactable “VAST on Cloud” offering exists today; current work is roadmap plus early marketplace/private-offer motions.
- FY26 prioritization is core layers first (cloud primitives, control plane stance, tenancy, operability/SLOs) before building higher-layer services.
- Marketplace offers are necessary for transactability, but VM economics can be non-competitive at scale; longer-term paths include cloud primitives and potentially CSP data-center hardware.
- Multi-tenancy gaps exist; a key blocker is limited identity provider scale and tenant-scoping constraints.
- Preferred architecture is hyperscaler object storage as the durable system of record, with VAST providing compute-adjacent caching and global namespace access.
- Control plane requirements include entitlements/fulfillment notifications and metering integration (e.g., marketplace/private offers).
- Google Distributed Cloud (GDC) is a strategic opportunity: Google issued a US-based RFP to replace NetApp for Distributed Cloud deployments.
- Hybrid-scale customer requirements (e.g., Walmart) drive deeper native cloud object integration expectations (especially GCS API compatibility).

- The requested document title indicates content related to VAST integration with Microsoft Azure, which is relevant to VAST's Cloud workstream.

- The Cloud program includes work related to a PRD for VAST on Azure.

- The 'VAST and Azure Integration' document includes a positioning statement that cold data can be transparently tiered to Azure Blob using either VAST native opaque formats (for maximum data reduction) or transparent open standard formats (for ecosystem accessibility), to enable infinite scale without flash price premium.

- The 'VAST and Azure Integration' document argues that constrained flash supply and rising prices make an all-flash exabyte-scale strategy economically risky, and that deep integration with Azure Blob allows customers to place the long-tail dataset on HDD-based object storage while keeping VAST flash for the GPU-adjacent working set.

- Mordechai Blaunstein referenced internal tracking for the approach: ORION-261324 and an internal wiki page (vastdata.atlassian.net/wiki/x/lQDInQE).

- Cloud product management is proposed as the owning function for Google Distributed Cloud (GDC) and Azure Local opportunities to maintain execution control and alignment with strategic cloud initiatives.

- A VAST on Cloud working session is planned for January 2026 (exact date not specified) to review the Cloud course and project brief.

- VAST Azure (part of VAST cloud efforts) was described by Lior Genzel as not close to being ready for Microsoft to use for Azure GPU performance testing via an Azure VoC instance.
## Topics

- Multi-tenancy and tenant-scoped auth/quotas
- Control plane, fulfillment, metering, and marketplace operations
- Operability, SLOs, support model, and release readiness
- Cloud primitives (storage tiers, metadata persistence, QoS/governance)
- GTM positioning: global namespace + data mobility vs raw storage economics

- Microsoft workback plan for VAST proposal

- CoreWeave MFN clause and pricing comparison for Microsoft negotiations

- Hardware vs software pricing split scenarios (Azure bare metal SKUs vs VAST ODM hardware)

- TCO model refinement including COGS, power, and opportunity cost to Microsoft

- Davos readiness for Microsoft competitive positioning

- VAST cold data tiering to Azure Blob: VAST object format vs native Azure Blob format

- Ecosystem accessibility and direct readability of data stored in Azure Blob

- Messaging on flash supply constraints, rising flash prices, and hedging strategy using Azure Blob

- Positioning VAST DRR/efficiencies as mitigation for flash supply chain volatility

- RFE 0482 for NVIDIA DGX Cloud: unified visibility across VAST clusters deployed at multiple NCPs

- Dual-uplink visibility for dedicated cluster LAX-02 (lambda.cloud.vastdata.com and nvidiadgxc.cloud.vastdata.com)

- Tenant-scoped visibility for multi-tenant cluster LAX-03 via nvidiadgxc.cloud.vastdata.com

- Service Aware VIP Pool design for multi-VIP access to VMS (GUI/CLI/REST/SSH/CSI)

- Internal tracking links: Salesforce RFE record and ORION-261324

- TLS support for VAST Block protocol

- VAST release 5.6 protocol feature prioritization

- Google Distributed Cloud (GDC) RFP requirements

- Potential minor release after VAST 5.6 to add TLS for Block

- Test timing coordination with Maroun (last name not provided)

- Salesforce RFE process: linking an RFE to the correct Related Feature

- VAST OS 5.3+ tenant naming restrictions (underscore not allowed)

- Documentation updates needed: Administrator Guide and CLI Command reference

- Customer deployment delays caused by undocumented configuration constraints

- VAST on Cloud sales enablement training course content review

- Project brief review for VAST on Cloud initiative

- Field messaging clarity and technical accuracy for cloud positioning
## Key Decisions

- Prioritize core cloud layers before higher-layer services.
- Use an explicit operating cadence and decision log to reduce churn and speed decisions.

- Jeff Denworth assigned Mordechai Blaunstein to lead the investigation of RFE 0482 and to bring in additional parties as needed.

- TLS support for VAST Block protocol will not be included in VAST release 5.6 because it was deferred in favor of other protocol features requested by more customers.

- Salesforce RFE 0538 (Documentation) for NTT DATA Japan Corporation was submitted to the PM team and approved by Rob Benoit.