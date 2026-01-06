---
type: projects
title: Cloud
status: active
my_role: owner
description: Cloud platform strategy, multi-tenancy, operability, and marketplace readiness across hyperscalers.
last_contact: '2025-12-11'
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

- 2025-12-15: Terika Dilworth asked the team to review and provide feedback on a draft VAST on Cloud enablement co...
- 2025-12-30: Mentioned in: Leidos Federal first US Fed Cloud PO submitted (FOpp-4197, $96,808.14) for Leidos DoD Cloud
- 2025-12-19: Mordechai Blaunstein shared a Google Docs document titled "CoreWeave-Vast Automation Project - V2 .d...
- 2025-12-01: Brian Evans alerted the PM team about RFE 0482 for NVIDIA DGX Cloud requesting unified visibility ac...
- 2025-12-11: Mentioned in: Microsoft requests Azure VoC for GPU performance testing, VAST declines due to readiness
- 2025-12-17: Mentioned in: 1:1 with Avinash Lakshman, Whale Iptic secure compute platform and potential VAST integration
- 2025-12-22: Mentioned in: Lior Genzel requested access to Google Doc: VAST and Azure Integration.docx
- 2025-12-01: Mentioned in: Karl Vietmeier asks for guidance on Cloud PM ownership for GDC and Azure Local opportunities
- 2026-01-02: A Google Docs notification email captured two open comments from Jonsi Stefansson on the 'VAST and A...
- 2026-01-01: Terika Dilworth invited Jason Vallery to an urgent internal training session on Monday, January 5, 2...
- 2025-12-01: Mentioned in: Karl Vietmeier asks for guidance on ownership of GDC and Azure Local opportunities
- 2026-01-05: Rob Benoit forwarded an approved Documentation RFE (RFE 0538) tied to NTT DATA Japan Corporation. Th...
- 2026-01-01: Terika Dilworth invited Jason Vallery and a large group to an urgent Zoom training on Monday, Januar...
- 2025-12-23: Mentioned in: Jeff Denworth update: Walmart hybrid requirements, GCS integration, and Alluxio risk
- 2025-12-15: Terika Dilworth asked the team to review and provide feedback on a draft VAST on Cloud training cour...
- 2025-12-30: Mentioned in: Leidos Federal first US Fed Cloud PO submitted (FOpp-4197) and request to track customer expectations
- 2026-01-02: Google Docs notification email shows two open comments from Jonsi Stefansson on the document 'VAST a...
- 2025-12-11: Microsoft requested an Azure VoC instance to run performance testing against Azure GPU instances bec...
- 2025-12-27: Mentioned in: Red flare escalation: Azure MAI deal risk, supply chain constraints, and January execution plan
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

- A VAST on Cloud enablement Cloud course and a project brief are being built from existing material and require team review for messaging and technical accuracy before a January working session.

- Jeff Denworth instructed Jason Vallery to track cloud purchase orders to understand customer expectations, user experience, cloud implications, and business development angles.

- VAST Azure readiness is a gating factor for supporting Microsoft requests for Azure VoC-based performance testing.

- The discussion included potential integration of VAST Data cloud storage capabilities with Whale Iptic's secure compute platform and distributed ledger technology.

- The document "VAST and Azure Integration.docx" appears related to VAST Data cloud integration work with Microsoft Azure.

- Cloud Product Management is positioned as the owner for GDC and Azure Local opportunities to maintain accountability, execution control, and alignment with hyperscaler relationships and cloud consumption motions.

- The 'VAST and Azure Integration' document includes a positioning statement that integrating with Azure Blob allows customers to place the long-tail dataset on HDD-based object storage while reserving VAST flash for the GPU-adjacent working set to hedge against flash component price volatility.

- The discussion included potential integration of VAST Data cloud storage and GPU infrastructure with Whale Iptic's secure compute and distributed ledger technology.

- Cloud product management is positioned as the preferred owner for hyperscaler-tied on-prem offerings (Google Distributed Cloud and Azure Local) to maintain execution control and alignment with strategic cloud initiatives.

- Walmart's re-stated requirements (hybrid solution, no disjoint namespaces, and GCS integration) may require updates to VAST's Cloud product plan.

- A working session for the VAST on Cloud course and project brief is planned for January 2026 (exact date not specified).

- A Leidos Federal software-only cloud deployment purchase order (FOpp-4197) is being treated internally as a cloud PO that should be tracked for customer expectations and user experience learnings.

- The document text claims VAST cold data can be transparently tiered to Azure Blob using either VAST native opaque formats (for maximum data reduction) or transparent open standard formats (for ecosystem accessibility), positioning this as enabling infinite scale without flash price premium.

- The document text argues that constrained flash supply and rising prices make an 'all-flash everything' strategy economically risky for exabyte-scale data, and that deep integration with Azure Blob lets customers keep the long tail on HDD-based object storage while reserving VAST flash for the GPU-adjacent working set.

- Lior Genzel stated that VAST Azure is not close to being ready to be used for Microsoft's requested Azure VoC GPU performance testing scenario.

- The VAST Cloud team is being asked to produce an Azure Blob integration proposal and to accelerate execution to close a Microsoft MAI deal with January 2026 milestones.
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

- VAST on Cloud enablement course content review

- Project brief review for alignment, clarity, and technical accuracy

- Field messaging clarity improvements

- Holiday schedule momentum and January working session preparation

- CoreWeave-VAST automation project document (version V2)

- Google Docs document collaboration (edit access)

- RFE 0482 for NVIDIA DGX Cloud unified visibility across multiple NCP-hosted VAST clusters

- Tenant-scoped visibility for multi-tenant cluster LAX-03 via NVIDIA uplink

- Internal tracking: ORION-261324 and related wiki documentation

- Azure Blob ecosystem accessibility vs maximum data reduction using VAST native opaque formats

- Messaging on flash supply constraints, rising prices, and VAST DRR/efficiency as mitigation

- Positioning: keep GPU-adjacent working set on VAST flash, long-tail data on Azure Blob

- NVIDIA KV Cache storage category and customer messaging

- NVIDIA Context Memory Extension (CME) and inference infrastructure implications

- AI seller enablement for CES-driven customer conversations

- VAST OS 5.3+ tenant name character restrictions (underscore '_' not supported)

- Documentation updates needed (Administrator Guide, CLI Command Reference) for naming constraints

- Salesforce RFE workflow: linking RFE to the correct Related Feature

- Customer deployment friction and CX impact from undocumented naming restrictions

- KV Cache storage as a new storage category for AI inference infrastructure

- NVIDIA Context Memory Extension (CME) and its impact on inference infrastructure

- Enablement for VAST AI sellers to lead customer conversations on KV Cache and CME

- CES announcements related to KV Cache storage

- VAST on Cloud sales enablement course content review

- Field messaging clarity and technical accuracy validation

- Ecosystem accessibility and direct readability of tiered data in Azure Blob

- Messaging on flash supply constraints and pricing risk

- Positioning VAST DRR and efficiency as a hedge against flash supply chain volatility

- Microsoft Redmond lab physical VAST PoC testing status

- Azure VoC request to test performance with Azure GPU instances

- Readiness of VAST Azure for performance testing and customer-facing evaluation

- Follow-up call with Microsoft/Azure requestors to communicate refusal
## Key Decisions

- Prioritize core cloud layers before higher-layer services.
- Use an explicit operating cadence and decision log to reduce churn and speed decisions.

- Jeff Denworth assigned Mordechai Blaunstein to lead the investigation of RFE 0482 and to bring in additional parties as needed.

- TLS support for VAST Block protocol will not be included in VAST release 5.6 because it was deferred in favor of other protocol features requested by more customers.

- Salesforce RFE 0538 (Documentation) for NTT DATA Japan Corporation was submitted to the PM team and approved by Rob Benoit.

- Jeff Denworth assigned Mordechai Blaunstein to take ownership of investigating RFE 0482 and to bring in additional parties as needed.

- RFE 0538 (Documentation) was approved by Rob Benoit for submission to the Product Management team.

- Decline Microsoft's request for an Azure VoC instance for GPU performance testing because VAST Azure is not ready for that use case.