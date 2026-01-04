---
type: projects
title: Cloud
last_contact: unknown
created: '2026-01-03'
tags:
- type/projects
- generated
---

# Cloud

## Status

| Field | Value |
|-------|-------|
| **Status** | active |
| **Owner** | Jason Vallery |

## Overview

Cloud-related work including confirming GCP GA timing and aligning initial lighthouse customers post-bottleneck fix.

## Open Tasks

```tasks
path includes Cloud
not done
```

## Recent Context

- 2025-12-19: [[2025-12-19]] - Discussion between Jeff Denworth and Jason Vallery on VAST’s Microsoft/Azure strategy: what level of... (via Jeff Denworth)
- 2025-11-14: [[2025-11-14 - VAST’s cloud and federal teams aligned on responding to Google Distributed Cloud]] - VAST’s cloud and federal teams aligned on responding to Google Distributed Cloud’s RFP to replace Ne... (via Google)
- 2025-11-14: [[2025-11-14 - Internal sync to align on Walmart’s big data initiative, clarify requirements, a]] - Internal sync to align on Walmart’s big data initiative, focusing on clarifying disaster recovery re... (via Walmart)
- 2025-11-03: [[Sources/Transcripts/2025/2025-11-03 - Team reviewed how cloud clusters must map to Salesforce assets (AccountSitePSN.md|Team reviewed how cloud clusters must map to Salesforce assets (AccountSitePSN]] — Team reviewed how cloud clusters must map to Salesforce assets (Account/Site/PSNT) to enable call-ho...
- 2025-10-30: [[Sources/Transcripts/2025/2025-10-30 - The group aligned on the cloud support operating model (Customer Success, Suppor.md|The group aligned on the cloud support operating model (Customer Success, Suppor]] — The group aligned on the cloud support operating model (Customer Success, Support, SRE), hyperscaler...
- 2025-10-29: [[Sources/Transcripts/2025/2025-10-29 - Tackle and VAST kicked off onboarding to sell VAST’s SaaS via Google Cloud Marke.md|Tackle and VAST kicked off onboarding to sell VAST’s SaaS via Google Cloud Marke]] — Tackle and VAST kicked off onboarding to sell VAST’s SaaS via Google Cloud Marketplace using Tackle ...
- 2025-10-29: [[Sources/Transcripts/2025/2025-10-29 - Kickoff of VAST’s onboarding to Tackle to connect an existing GCP Marketplace li.md|Kickoff of VAST’s onboarding to Tackle to connect an existing GCP Marketplace li]] — Kickoff of VAST’s onboarding to Tackle to connect an existing GCP Marketplace listing and enable pri...
- 2025-10-28: [[Sources/Transcripts/2025/2025-10-28 - Cloud BU leadership aligned on a dual-track strategy (1) ship GCP MVP via marke.md|Cloud BU leadership aligned on a dual-track strategy (1) ship GCP MVP via marke]] — Cloud BU leadership aligned on a dual-track strategy: (1) ship GCP MVP via marketplace with strong c...
- unknown: [[Sources/Transcripts/2025/2025-10 - Cloud Marketplace MVP.md|Cloud Marketplace MVP]] — - [x] Define GA acceptance criteria for cloud MVP (spin up/down, DR/offload, etc.) and when to begin...
- unknown: [[Sources/Transcripts/2025/2025-10 - SaaS.md|SaaS]] — - [x] Draft cloud SaaS operating model requirements (DevOps/LifeSite rotations, telemetry, 24x7 supp...
- unknown: [[2025-10 - Google Tasks]] - A completed task to confirm Google Cloud Platform GA timing after a bottleneck fix and align the fir... (via Google)
- unknown: [[2025-10 - Asaf Levy]] - Completed action items from a working session with Asaf Levy to align on DataSpaces persistence desi... (via Asaf Levy)
- unknown: [[2025-11-4 - Planning sessions]] - Planning notes for a set of sessions with Jeff Denworth to align on VAST’s cloud-first product strat... (via Jeff Denworth)
- unknown: [[2025-10 - Jeff Denworth]] - Notes capturing planning topics with Jeff Denworth around travel, team reporting structure, cloud ac... (via Jeff Denworth)
- unknown: [[2025-10 - Lior Genzel]] - Note captures discussion points and completed follow-ups with Lior Genzel around Google TPU strategy... (via Lior Genzel)
- unknown: [[2025-10 - Shachar Feinblit]] - Checklist and Slack snippets related to coordinating with Shachar Feinblit, including setting up rec... (via Shachar Feinblit)
- unknown: [[_Open Topics]] - Open topics note for Shachar Feinblit, listing key internal Slack contacts by functional area (suppo... (via Shachar Feinblit)
- unknown: [[2025-10 - SaaS]] - A completed task to draft the operating model requirements for VAST Cloud SaaS, covering DevOps/Life...
- unknown: [[Available Capacity Calculations]] - Email-style note proposing replacing a fixed overhead percentage with a first-principles “available ...
- unknown: [[2025-10 - Cloud Marketplace MVP]] - Checklist of completed deliverables for a cloud marketplace MVP, including GA acceptance criteria, a...
- unknown: [[Pricing]] - Internal note to the Pricing v-team outlining principles and a recommended direction for VAST Cloud ... (via Pricing)
- unknown: [[2025-10 - Pricing Tasks]] - Checklist of completed pricing workstreams for cloud/private offers, discount policy, normalization ... (via Pricing)

## Key Facts

- Google Distributed Cloud has connected and air-gapped variants; NetApp is the incumbent storage partner.
- Google issued a US-based RFP to replace NetApp for GDC storage; VAST was invited to respond and is undergoing vendor due diligence.
- Google’s emphasis areas include air-gapped support, compliance/attestations (e.g., DISA STIG), ops model (updates, staffing, troubleshooting), multi-tenancy, quotas, encryption, and tags.
- Fort Meade "Gemini as a service" on-prem initiative is described as a Q4 commit and a near-term joint validation path.
- GDC deployments commonly run on Dell; HPE and Cisco are also in scope for hardware options.
- VAST recently launched Google Marketplace offers; broader partnership is still early.
- Resource risk: Greg may be heavily focused on Leidos next year, potentially impacting continuity.
- Google Z3 exists; Z4M is the next storage-serving VM with higher storage and network density.
- Z4M targets storage-serving use cases; CPU/RAM may be overprovisioned but pricing optimization is planned.
- Google is developing a Google Supercomputer (GSC) interface to provision AI/HPC infrastructure with co-placement optimization; VAST could be integrated as a selectable storage option with potential auto-deploy.

## Topics

Google Distributed Cloud RFP response strategy, Air-gapped/dark-site readiness and operational support model, Compliance evidence, certifications, and ATO considerations, Hardware platform options (Dell/HPE/Cisco) vs commodity VM shapes, RDMA and VM shape tradeoffs, Fort Meade on-prem Gemini validation path, Coordination between Google corporate GDC and Google Federal teams, Joint federal account alignment and co-selling, Google Marketplace offers and broader partnership tracks, TPU/model-builder partnership track, Z4M storage-serving VM roadmap (density, pricing optimization), Local SSD vs HyperDisk vs object storage tiers (latency/economics), Google Supercomputer (GSC) provisioning, co-placement, and partner integration, RDMA and GPUDirect Storage (A5X GPUs) and TPU RDMA timeline, Anywhere Cache (cost vs performance)

## Blockers

- ❌ Bottleneck fix required before confirming GA timing
- ❌ Risk of lift-and-shift approach without cloud primitives/control-plane stance
- ❌ MAI control-plane fragility and GPU issues may slow proof points
- ❌ Azure internal politics (Compute vs Storage) and long hardware qualification timelines
- ❌ Fragmentation risk if higher-layer opinionated services are built too early

## Related

<!-- Wikilinks to related entities -->
