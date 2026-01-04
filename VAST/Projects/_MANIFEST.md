# Entity Manifest

> **Auto-generated manifest** - Synced with folder structure.
> Edit this file to add aliases, change status, or update metadata.
> Run `backfill.py sync-manifests` to sync with folders.

## Entities

| Name | Status | Owner | Description |
|------|--------|-------|-------------|
| 5.5 Features | active |  |  |
| AI Pipelines Collateral | active |  |  |
| AI Talk | active |  |  |
| Cloud | active |  |  |
| GSI Team | active |  |  |
| Model Builder Turbine | active |  |  |
| OVA | active |  |  |
| Platform Learning | active |  |  |
| Pricing | active |  |  |
| VAST on Azure Integration | active |  |  |
| Marketplace L-series Offer Complement (SKUs/OEM path) | complete | Jason Vallery | Assess complementing the Marketplace L-series offer with higher-density storage SKUs or an OEM hardware path. |
| Microsoft BizDev Education & Intros to Ronnie | complete | Jason Vallery | Educate Microsoft BizDev (density/power, single-namespace story) and secure intros to Ronnie via John Tinter. |
| Microsoft Comparison Slide (LSv4/LSv5/OEM-ODM/Azure Storage) | complete | Myself | Create a comparison slide for conversations covering LSv4, v5, OEM/ODM, and Azure Storage. |
| Azure GA Milestones Alignment (Lifter program) | complete | Jeff Denworth | Validate Azure GA milestones and align with Lifter program phases (Feb GA vs Sep 1P milestone). |
| Microsoft Azure Engagement Plan | complete | Jeff Denworth | Draft a Microsoft networking engagement plan focused on minimizing egress (e.g., ExpressRoute Direct Local) for VAST’s Azure offerings. |
| EB Power Savings to GPUs One-Pager | complete | Jason Vallery | Create a one-pager converting VAST EB power savings into additional GPUs per site; share with MAI (Mustafa), Kushal, and Vipin. |
| Microsoft ROI Data Usage Validation | complete | Jason Vallery | Validate what Microsoft data can be used in ROI comparisons before sharing with Nidhi. |
| Win/Loss + Product MBR cadence | proposed | Jason Vallery | Lightweight recurring win/loss analysis and product monthly business review tied to Sales Ops to identify repeatable wins, losses, and product gaps. |
| BlockFuse/C-Store | active | Krishnan | Caching/storage proposals for MAI (C-Store-based) and related BlockFuse/BlobFuse approaches; performance/scale claims under review. |
| DeltaZero | active | Jai Menon | Positioned as a follow-on to Bifrost for further Blob performance enhancements; positioning still in progress. |
| Cisco POC (DoD/IC) | active | Greg Castellucci | Proof of concept with Google DoD/IC team and Cisco gear to validate VAST stack with Google Gemini for DoD/IC go-to-market; originated from a canceled IC solicitation and subsequent teaming discussions. |
| BlobFuse | active |  | BlobFuse-based approaches considered for MAI caching/data access; must scale to ~100k nodes and integrate with AKS/Spark. |
| Polaris | active |  | System of record for cloud entitlements, metering/usage reporting, call-home registration, and integration hub with marketplaces and Salesforce/Tackle for the GCP MVP launch. |
| Project Stargate | active |  | OpenAI-related initiative referenced as 'Project Stargate'; VAST has a newly started sell-to relationship and Jason would have dotted-line involvement in the prospective VAST role. |
| Project Apollo | active | AKS team (Microsoft) | AKS-led initiative to build a slimmed-down Azure control plane/topology for single-tenant GPU sites (lease power/space) without full Azure region overhead; potential path to make VAST the standard storage for Apollo deployments via a thin VAST control plane integration. |
| AC Store | active | Krishnan | Internal proposal (Krishnan’s team) as part of caching strategy options for MAI. |
| VAST-as-a-Service | proposed | Jason Vallery | Future cloud/SaaS operating model for VAST (multi-tenant service) informed by current managed-services/SRE-style support for large on-prem AI customers (CoreWeave, XAI). |
| Enscale deck | active |  | Adapt Enscale solution/deck to support Microsoft/MAI storyline; emphasize Kubernetes-led control plane and Polaris-managed operations; avoid CoreWeave-style lock-in in any resale. |
| Alluxio/DAX evaluation | active | Jai Menon | Evaluate Alluxio/DAX as a single cache solution supporting both training and inference/KB caching; review performance data and fit for MAI requirements. |
| NeoCloud in a box | active | Morty | Packaging VAST portfolio as a blueprint for NeoClouds to offer AI cloud services beyond GPU-as-a-service, including storage, event streaming, analytics/warehouse, telemetry, and potentially serverless functions. |
| Salesforce integration for marketplace transaction flow and data sync | active |  | Integrate Salesforce to support marketplace transaction flow and data synchronization for cloud offers. |
| MAI unified cache | active | Jai Menon | Define and deliver a single, pluggable caching solution for MAI that prioritizes training workloads first and later supports inference/KB caching; must scale to ~100k nodes and run on AKS + Spark, potentially with multi-region logical pooling. |
| Bifrost | active | Jai Menon | Blob performance initiative including a direct read path from compute to capacity nodes (bypassing FE/table for reads) to improve latency/throughput; positioned as near-term focus to support MAI scale. |
| Confluence FRDs taxonomy | active | Jason Vallery | Make Confluence the authoritative home for FRDs/customer requirements with templates, tagging, and links to Salesforce opportunities. |
| Google RFP | active | Jason Vallery | Prepare for Google RFP discussions; quickly triage whether requirements are block/latency-heavy (NetApp advantaged) vs object/throughput-heavy (better VAST fit). |
| Google Marketplace offers | active | Jason Vallery | Recently launched Google Marketplace offers; broader partnership and integration still early. |
| Fairwater | active |  | Referenced as a comparable large-scale site/footprint; potentially related to the reported 'Matt UK' supercomputer deal and used as a scale comparison for DFW enrichment sites. |
| PSC Interfaces for Cross-Project RDMA | active | Google networking team | Assess requirement to use Private Service Connect interfaces (PSCI) for cross-project RDMA connectivity (VPC peering not supported) and implications for complexity, performance, and architecture. |
| Enlightenment API | on-hold |  | Prior project related to redirects/enlightenment API; explicitly stated as not the same as current Bifrost direct path work. |
| Cloud control plane | active | Jan C. Stefansson | Planned cloud control plane build at VAST (via acquired company 'Red Stapler'); Jason would own PM portion and manage/coordinate PM work. |
| OpenAI cache evaluation | active | Jason Vallery | Evaluate OpenAI’s caching code/IP as a candidate for MAI’s unified cache: confirm legal/IP and repo access, review architecture and readiness, assess scalability to ~100k nodes, and fit with AKS+Spark; compare against BlobFuse, Alluxio/DAX, and AC Store. |
| Apollo | blocked |  | Microsoft initiative with unclear scope/boundaries and many stakeholders; tight timeline with data centers going live, creating execution risk and making it hard to define Jason’s role and success criteria. |
| VAST database updates | active |  |  |
| Z4M RDMA Networking (GCP) | active | Ben | Define and validate networking model for RDMA-enabled Z4M instances on GCP, including dual-interface (RDMA + TCP) expectations, subnet/VPC constraints, and bandwidth/NIC topology. |
| Neo | active | Morty | Neo cloud feature requirements workstream; core to current business; Morty owns requirements and must remain focused even as he moves to Jason’s team. |
| Fort Meade "Gemini as a service" on-prem validation | active | Greg Castellucci | In-flight Fort Meade initiative to run Gemini on-prem ("Gemini as a service") as a rapid joint validation/reference for air-gapped GDC; described as a Q4 commit and double-digit PB opportunity. |
| Cloud-in-a-box (Tier-2 clouds) | proposed | Jason Vallery | Alliance-driven blueprint for Tier-2 clouds using control-plane partners to deliver a packaged AI pipeline solution (GPU-as-a-service orchestration + required services). |
| TPU track (Google chips for model builders) | proposed |  | Parallel partnership track where Google sells TPUs to model builders and wants storage to keep accelerators productive; discussed as separate from the immediate GDC RFP. |
| Alluxio/DAX | active |  | Candidate caching solution; now supports inference caching including KB caching, aiming to be a single cache for training and inference. |
| AI caching strategy for MAI | active | Jai Menon | Define and execute a unified, pluggable caching strategy for MAI at extreme scale, prioritizing training cache requirements first and adding inference/KB caching later; evaluate OpenAI cache/IP and alternatives (BlobFuse/Blockfuse, AC Store, Alluxio/DAX). |
| GCP MVP | active |  | Near-term Google Cloud marketplace MVP launch; requires routable IP deployment flow, demos, collateral, QA/support readiness, maintenance handling, and marketplace offer activation/pricing tuning. |
| Google Distributed Cloud RFP | active | Leo | Response effort to Google Distributed Cloud RFP to replace NetApp as storage partner, with heavy emphasis on air-gapped/dark-site readiness, compliance evidence, and operational model details. |
| Building an AI cloud with VAST | active | Jason Vallery | Planned 45-minute SCO session for Jason: explain why VAST is used, where it’s going, and how a NeoCloud can integrate VAST into a cloud services portfolio (multi-tenancy best practices, control plane direction, mapping VAST capabilities to AI lab/enterprise use cases). |
| OpenAI VAST POC (CoreWeave cluster) | on-hold | Jason Vallery | Pending proof-of-concept to evaluate VAST as GPU-adjacent warm storage (and potentially caching/global namespace capabilities) using a CoreWeave cluster; intended to enable moving Applied clusters to Research by insulating from weak connectivity/Azure variability. |
| OpenAI cache IP feasibility evaluation | active | Jason Vallery | Assess feasibility of using OpenAI cache IP/code for MAI: confirm IP/access, review code quality/architecture, validate scalability to ~100k nodes, and evaluate operational fit with AKS/Spark; determine whether cache is unified for training and inference or separate implementations. |
| C-Store proposals | active |  | Internal proposals (Krishnan and team) around using a C-Store approach as part of caching strategy; needs evaluation against MAI requirements and other options. |
| Terraform Static VIP Reservation | active | Ronnie Lazar | Provide Terraform examples/snippets showing how static VIP IPs are provisioned/reserved on GCP to ensure they remain allocated even when not attached to a VM interface. |
| AI caching strategy for MAI scale | active | Jai Menon | Define a unified, pluggable caching approach to meet MAI training-first requirements and later inference/KB caching, at extreme scale (target ~100k nodes) in an AKS + Spark environment; compare multiple options and align with Blob performance improvements. |
| Blockfuse/BlobFuse | active |  | BlobFuse/Blockfuse caching and data access work in progress; needs review of latest progress and performance numbers and whether it can scale to ~100k nodes and integrate with AKS/Spark. |
| VIP/Failover Design (GCP RDMA) | active | Ben | Re-evaluate VIP and failover approaches on GCP for RDMA workloads (ILB vs alias IP vs route-based), including latency/convergence, pricing/feature tradeoffs, and IP reassignment race window risks. |

## Aliases

_Add nickname mappings here:_

<!-- Example: - "Nick" → Full Name -->
