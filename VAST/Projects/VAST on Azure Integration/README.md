---
type: projects
title: VAST on Azure Integration
last_contact: unknown
created: '2026-01-03'
tags:
- type/projects
- generated
---

# VAST on Azure Integration

## Recent Context

- unknown: [[Outline]] - Outline section for the VAST on Azure Integration project defining deployment variants and a workloa...
- unknown: [[Azure + VAST Integration Opportunities and Approach v2]] - Draft strategy and roadmap for integrating VAST with Microsoft Azure, centered on a minimal Blob RES...
- unknown: [[Azure + VAST Integration Opportunities and Approach v1]] - Working draft strategy document for integrating VAST with Microsoft Azure, centered on positioning V...
- 2026-01-03: [[2026-01-03 - Prep for Microsoft AI talks]] - Jonsi Stephenson and Jason Vallery aligned messaging and strategy for upcoming Microsoft AI discussi... (via Jonsi Stephenson)
- 2025-12-19: [[2025-12-19]] - Discussion between Jeff Denworth and Jason Vallery on VAST’s Microsoft/Azure strategy: what level of... (via Jeff Denworth)
- 2025-12-18: [[2025-12-18 1303 - New Recording]] - Brainstorming and outlining a joint document describing how VAST will integrate with Microsoft Azure...
- 2025-10-30: [[2025-10-30 - Alignment call on roles, gaps, and collaboration. Andy outlined his team’s four]] - Weekly 1:1 alignment between Jason Vallery and Andy Perlsteiner covering Andy’s team charter, major ... (via Andy Perlsteiner)
- 2025-10-28: [[2025-10-28 - Jason and Kanchan aligned to pursue MAI and UK Met Office as flagship wins to un]] - Weekly 1:1 between Jason Vallery (VAST) and Kanchan Mehrotra (Microsoft) aligning on a dual-track pl... (via Kanchan Mehrotra)
- 2025-10-27: [[2025-10-27 - Jason and Kurt aligned on a go-to-market path to bring VAST’s high-density, lowe]] - Weekly 1:1 where Jason Vallery and Kurt Niebuhr aligned on a Microsoft Azure go-to-market path for V... (via Kurt Niebuhr)
- 2025-10-06: [[2025-10-06 - Jason updated Jai that he has a complex, high-variance offer from VAST and an ex]] - Weekly 1:1 between Jason Vallery and Jai Menon discussing Jason’s pending job decision between VAST ... (via Jai Menon)
- 2025-10-06: [[2025-10-06 - Jason has a complex VAST offer with risky, sales-linked compensation and a more]] - Weekly 1:1 between Jason Vallery and Jai Menon focused on Jason’s decision to leave Microsoft due to... (via Jai Menon)
- 2025-10-06: [[2025-10-06 - Jason briefed Jai on offers from VAST and Crusoe, noting VAST’s complex, risky c]] - Weekly 1:1 between Jason Vallery and Jai Menon discussing Jason’s competing offers from VAST and Cru... (via Jai Menon)
- 2025-10-06: [[2025-10-06 - Jason shared he has a complex, risky offer from VAST and a more stable option fr]] - Weekly 1:1 between Jai Menon and Jason Vallery focused on Jason’s decision to leave Microsoft, compa... (via Jai Menon)

## Key Facts

- Andy’s team operates across four pillars: field escalation/POC support, lab management/benchmarks, SE enablement/training plus PM augmentation, and marketing support.
- Documentation is currently feature/button-oriented and not scenario-driven; scenario guides are ad hoc and late.
- PM process gaps include training ownership, PRDs vs FRDs (engineering writes FRDs), release visibility, and access to builds/docs.
- OVA is a single-VM multi-container demo; requires ~128GB RAM host; client networking requires tunneling/proxies; unsupported.
- SE Lab access requires VPN plus an AD account via octo.selab.fastdata.com; multiple clusters exist with varying admin levels.
- GitLab access is restricted and requires an IT ticket for a licensed account.
- Implementation reviews are run by Galit/Orly; Confluence release pages (e.g., 5.4 dev) list features, owners, and FRDs.
- Sync Engine lacks a formal PM; Andy and Blake are acting PMs.
- OpenAI architecture pattern described: multi-exabyte lakes in 3 Azure regions; GPUs in 50+ regions plus other providers; GPU-adjacent cache with checkpoints back to central.
- Urgent need: Sync Engine must read from Azure Blob to support large migrations (wave.ai) on a December timeline; key engineer Aaron Zilber is OOO ~2.5 weeks.

## Topics

Roles and responsibilities between PM and Field CTO org, Documentation and field training ownership gaps, Release process: phase gates, implementation reviews, FRDs/Confluence, Hands-on enablement: OVA, SE Lab, GitLab access, VAST on Cloud viability and cloud economics, Multi-tenancy backlog toward SaaS, OpenAI architecture and global data plane opportunity, Sync Engine ownership gap and Azure Blob-source migration needs, Job offer evaluation (VAST vs Crusoe vs Microsoft), Compensation structure risk (commission + equity), Microsoft Apollo scope ambiguity and stakeholder complexity, Career trajectory and path to Partner, VAST cloud control plane and VAST on Azure go-to-market, OpenAI-related sales motion / Project Stargate involvement, Offer comparison (VAST vs Crusoe vs staying at Microsoft)

## Overview

Architecture and GTM outline for integrating VAST with Microsoft Azure, including deployment variants (ODM/Edge, Azure IaaS, future Azure bare metal, hybrid), workload reference patterns, and a roadmap for Blob API compatibility, federation, networking, security, operations, and commercial packaging.

## Status

| Field | Value |
|-------|-------|
| **Status** | active |
| **Owner** | Myself |

## Blockers

- ❌ Managed VNet constraints for Azure first-party services (e.g., serverless/managed networking) may limit direct connectivity patterns.
- ❌ Blob API compatibility scope and semantics (auth, error model, throttling, SDK/tool expectations) require validation via conformance gates.
- ❌ Identity integration requirements (Entra ID/OAuth validation, managed identity patterns, RBAC/ACL mapping) are dependencies for MVP.
- ❌ Private Link / Private Link Service operational workflow (DNS, approvals, automation) is a dependency for private-first connectivity.
- ❌ Potential API drift and performance variance across Azure VM/storage options (Lasv4/Lasv5, NVMe locality, quotas/SKU availability).

## Next Steps

- [ ] Finalize workload-to-variant mapping and reference topologies for W1–W9.
- [ ] Define Blob API Compatibility MVP scope (block blobs), semantics contract, and authentication approach (Entra ID/OAuth as MVP requirement).
- [ ] Build and run compatibility harness gates (AzCopy, Azure Storage SDK for Python, optional .NET/Java, high-concurrency clients).
- [ ] Specify namespace/metadata federation patterns (VAST master vs Blob master vs proxy/migration-on-read) and reconciliation mechanisms (Event Grid, Change Feed, scans).
- [ ] Detail networking patterns (Private Link/PLS, DNS, ExpressRoute/vWAN, managed VNet bridging) and validate throughput/scale limits.
- [ ] Define security/compliance posture (CMK, enclave patterns, audit/forensics) and shared responsibility model.
- [ ] Create validation plan with KPIs, benchmarks, and pilot plan (reference customers/regions/exit criteria).
- [ ] Document commercial packaging options (Marketplace private offer/managed app/BYOL), MACC alignment, and metering/billing architecture.
- [ ] Define and lock the AzCopy Compatibility Contract (exact REST calls/headers/versions/semantics) and build automated regression suite
- [ ] Implement Blob façade MVP operations required by AzCopy (list/head/get-range/put blob/put block/put block list/delete/from-url copy)

## Key Decisions

- ✅ Use Phil Wagstrom as primary multi-tenancy SME contact.
- ✅ Proceed with OVA and SE Lab access for Jason’s learning.
- ✅ Schedule a follow-up focused on OpenAI architecture and needs.
- ✅ Do not pursue Microsoft compensation changes for Jason.
- ✅ Jason to proceed with final diligence on VAST and decide between VAST and Crusoe.
- ✅ Do not pursue an internal compensation/scope package at this time.
- ✅ Jason will not stay at Microsoft.
- ✅ Jason will choose between VAST and Crusoe by 2025-10-08 (leaning VAST pending de-risking).
- ✅ Do not pursue a Microsoft counteroffer given compensation constraints and unclear scope.
- ✅ Proceed toward a decision between VAST and Crusoe with intent to resign by Wednesday.

## Collaborators

| Person | Role | Company |
|--------|------|---------|
| [[Nidhi]] |  | Microsoft |
| [[Renan]] | CEO | VAST Data |
| [[Louie]] |  | OpenAI |
| [[Yonce]] |  |  |
| [[Kanchan Mehrotra]] |  | Microsoft |
| [[Mustafa]] | MAI advocate/sponsor (power constrained) | Microsoft |
| [[Kushal Datta]] |  |  |
| [[Alon Horev]] |  |  |
| [[Vipin Sachdeva]] |  | Microsoft |
| [[Kurt Niebuhr]] |  |  |
| [[Lior Genzel]] |  |  |
| [[Jeff Denworth]] |  |  |
| [[Kishore Inampudi]] |  |  |
| [[Jonsi Stephenson]] | CEO | VAST Data |
| [[Igal]] |  | Microsoft |
| [[Yancey]] |  |  |
| [[Jason Vallery]] | Product management (cloud); partnerships with hyperscale cloud providers | VAST Data |

## Related People

- [[Nidhi]]
- [[Renan]]
- [[Louie]]
- [[Yonce]]
- [[Kanchan Mehrotra]]
- [[Mustafa]]
- [[Kushal Datta]]
- [[Alon Horev]]
- [[Vipin Sachdeva]]
- [[Kurt Niebuhr]]
- [[Lior Genzel]]
- [[Jeff Denworth]]
- [[Kishore Inampudi]]
- [[Jonsi Stephenson]]
- [[Igal]]
- [[Yancey]]
- [[Jason Vallery]]

## Related Customers

- [[VAST Data]]
- [[Microsoft]]
- [[OpenAI]]
- [[Walmart]]

## Related

<!-- Wikilinks to related entities -->
