---
type: "people"
title: "1:1 with Andy Perlsteiner, align on Field CTO pillars, cloud viability focus, and Sync Engine Blob gap"
date: "2025-10-30"
person: ""
participants: ["Jason Vallery", "Andy Perlsteiner"]
source: "transcript"
source_ref: "/Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-10-30 - Alignment call on roles, gaps, and collaboration. Andy outlined his team’s four.md"
tags:
  - "type/people"
  - "person/"
  - "generated"

---

# 1:1 with Andy Perlsteiner, align on Field CTO pillars, cloud viability focus, and Sync Engine Blob gap

**Date**: 2025-10-30
**With**: Jason Vallery, Andy Perlsteiner

## Summary

Jason Vallery and Andy Perlsteiner aligned on Andy’s Field CTO team scope, major process gaps (docs, training ownership, PRDs vs FRDs, release visibility), and how PM and field should collaborate. Jason shared his initial charter to make VAST on Cloud sellable (marketplace objects, CSP VM shapes, multi-tenancy toward SaaS, and pricing/legal alignment). They identified an urgent product gap, Sync Engine lacks PM ownership and needs Azure Blob source support for wave.ai’s December 2025 migration timeline.


## Action Items


- [?] Request an SE Lab Active Directory account and access via VPN and octo.selab.fastdata.com using the portal form so Jason Vallery can use client VMs and clusters for demos and validation. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Submit an IT ticket to obtain a licensed GitLab account for get.vastdata.com to enable self-serve access to repos and technical artifacts. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Meet with Josh (last name not provided) to obtain the VAST OVA and setup guidance for a home lab deployment. @Myself 📅 2025-10-31 ⏫ #task #proposed #auto

- [?] Deploy the VAST OVA in a home lab and validate basic S3, NFS, and SMB access, including any required tunneling or proxying for client connectivity. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Get added to VAST 5.5 implementation reviews by contacting Galit or Orly, and begin attending phase gates and implementation reviews for release hygiene. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Review the Confluence 5.4 'dev' release page, associated FRDs, and implementation review recordings to improve release visibility and technical context. @Myself 📅 2025-11-08 #task #proposed #auto

- [?] Add Jason Vallery to the biweekly Tomer Hagay to Octo and field sync distribution list and calendar invites to improve PM-field alignment. @Andy Perlsteiner 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Provide the sales team an update on Sync Engine Azure Blob source support status, given wave.ai’s early December 2025 migration start requirement. @Andy Perlsteiner 📅 2025-10-30 ⏫ #task #proposed #auto

- [?] Schedule and run a deep-dive with Andy Perlsteiner to walk through OpenAI architecture, data flows, workloads, and pain points to assess VAST fit as a global data plane. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Engage Phil Wagstrom to review VAST multi-tenancy hierarchy, admin model, and backlog implications for VAST on Cloud and SaaS direction. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Partner with Yonce (last name not provided) on the Azure Marketplace object launch plan required to make VAST on Cloud sellable. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Align with Tomer Hagay on prioritizing the multi-tenancy backlog for VAST on Cloud and SaaS readiness. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Work with Timo Pervane on cloud business model, pricing approach, and legal model alignment for VAST on Cloud. @Myself 📅 2025-11-08 #task #proposed #auto

- [?] Align wave.ai migration strategy with Yonce and cloud marketplace efforts to avoid conflicting approaches across teams. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Clarify formal Product Management ownership and process for Sync Engine to eliminate ad hoc acting PM coverage and unblock Azure Blob source support decisions. @Jeff Denworth 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Plan and deliver a knowledge share for engineering and field teams on Azure Blob API behavior and system implications for migrations and potential product support. @Myself 📅 2025-11-08 🔽 #task #proposed #auto




## Decisions


- Use Phil Wagstrom as the primary subject matter expert contact for VAST multi-tenancy hierarchy and admin model.

- Jason Vallery will proceed with hands-on learning using the VAST OVA and SE Lab access to validate basic functionality and improve PM-field collaboration.

- Schedule a follow-up deep-dive focused on OpenAI architecture, workloads, and VAST fit.




## Key Information


- Andy Perlsteiner has been at VAST Data for almost eight years and his role has evolved based on deep internal history and relationships.

- Andy Perlsteiner’s Field CTO team operates across four pillars: (1) pre-sales field escalation and POC support for SEs and sales, (2) lab management for demos, hosted POCs, benchmarks, and feature testing, (3) SE enablement and training for new releases and features, plus technical augmentation for Product Management, and (4) marketing support (webinars, blog posts, videos).

- VAST documentation is perceived as overly technical and not scenario-driven, described as reading like a 'car stereo manual'; scenario guides are ad hoc and arrive late.

- There are Product Management process gaps at VAST Data including unclear training ownership, engineering writing FRDs instead of PM-owned PRDs, limited release visibility, and limited access to builds and documentation for PMs.

- Jason Vallery’s stated charter is to make VAST on Cloud sellable by driving marketplace objects (partnering with Yonce), pushing CSPs starting with Microsoft Azure for better VM shapes, driving multi-tenancy backlog toward SaaS, and aligning cloud pricing and legal models with Timo Pervane.

- The current VAST on Cloud fit is viewed as economically weak versus first-party cloud capacity storage; the likely differentiated value is higher-level compute-adjacent workflows and a global data plane.

- OpenAI’s described pattern is multi-exabyte data lakes in three Microsoft Azure regions for CPU and analytics (Spark and Databricks), with GPUs distributed across 50+ regions plus CoreWeave and Oracle; they use GPU-adjacent cache and checkpoint back to central storage.

- VAST Data’s opportunity discussed is to provide a common global data plane and global namespace across cloud providers, described as 'data spaces'.

- VAST’s OVA exists but is unsupported; it requires approximately 128 GB RAM on the host, client networking requires tunneling or proxies, and it is a single-VM multi-container demo deployment.

- SE Lab access is via VPN and octo.selab.fastdata.com using an AD account; client VMs are available; there are multiple clusters including GA and 5.4, and some environments are tenant-admin only.

- GitLab access at get.vastdata.com is restricted and requires an IT ticket for a licensed account.

- Release hygiene guidance: attend phase gates and implementation reviews run by Galit and Orly, and review Confluence release pages (example: 5.4 dev) and FRDs.

- Multi-tenancy subject matter experts identified: Phil Wagstrom as primary and Ray Coetzee (UK) as another SME.

- A biweekly Tomer Hagay to Octo and field sync exists, and Jason Vallery was added to the OctoPM Monday sync.

- Sync Engine has no formal Product Manager; Andy Perlsteiner and an individual named Blake (last name not provided) are acting PMs.

- wave.ai has approximately 100 PB in Azure Blob Storage in Sweden and plans to migrate about 50 PB to CoreWeave while syncing checkpoints back to Azure; this requires Sync Engine to read from Azure Blob as a migration source.

- Aaron Zilber is investigating Azure Blob APIs for both implementation and migration-read use cases, and he is out of office for approximately 2.5 weeks during a period when early December 2025 migration start is needed.



---

*Source: [[2025-10-30 - Alignment call on roles, gaps, and collaboration. Andy outlined his team’s four]]*