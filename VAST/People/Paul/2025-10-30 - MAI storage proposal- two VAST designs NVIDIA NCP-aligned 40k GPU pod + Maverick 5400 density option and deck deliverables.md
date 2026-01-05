---
type: people
title: 'MAI storage proposal: two VAST designs (NVIDIA NCP-aligned 40k GPU pod + Maverick 5400 density option) and deck deliverables'
date: '2025-10-30'
participants:
- Jason Vallery
- Paul
- Ray
- Alon Horev
source: transcript
source_ref: /Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-10-30 - Team aligned on presenting two VAST designs for MAI (1) an NVIDIA NCP reference.md
tags:
- type/people
- generated
person: Paul
---

# MAI storage proposal: two VAST designs (NVIDIA NCP-aligned 40k GPU pod + Maverick 5400 density option) and deck deliverables

**Date**: 2025-10-30
**Attendees**: Jason Vallery, Paul, Ray

## Summary

Internal VAST team aligned on presenting Microsoft MAI two VAST storage designs: a primary NVIDIA NCP reference-aligned high-performance pod sized around a 40k GPU training cluster, plus a second capacity and density-optimized Maverick 5400 option targeting 1 EB. The deck must include side-by-side capacity, performance, rack count, and power, plus narrative emphasis on checkpoint write throughput, Kubernetes CSI/COSI integration, file and object support, single-pane monitoring, and resilience during WAN outages from Azure Extended Zones dependencies.

## Action Items

- [?] Model an NVIDIA NCP-aligned high-performance pod design (approximately 41,472 GPUs, Series 1350) including usable capacity, sustained read and write performance, rack count, and total power, and include extrapolation toward 1 EB for Microsoft MAI. @Paul 📅 2025-10-30 ⏫ #task #proposed #auto

- [?] Validate and model a capacity-optimized Maverick 5400-based 1 EB design including C-node to D-node ratios, performance limits, rack count, and power, and document any gaps versus NVIDIA NCP alignment for Microsoft MAI. @Ray 📅 2025-10-30 ⏫ #task #proposed #auto

- [?] Produce a side-by-side comparison table and rack layout diagrams for the NVIDIA NCP-aligned design and the Maverick 5400 design, updating existing EnScale and Portugal deck templates for the Microsoft MAI meeting. @Paul 📅 2025-10-30 ⏫ #task #proposed #auto

- [?] Provide consolidated sustained performance estimates (read and write TB/s) and total power figures for both the NVIDIA NCP-aligned design and the Maverick 5400 design for Microsoft MAI. @Ray 📅 2025-10-30 ⏫ #task #proposed #auto

- [?] Add deck content covering Kubernetes integration (CSI and COSI), file and object support, monitoring and logging approach, and offline resiliency requirements (offline auth token or claims caching, internal DNS and routing) for Microsoft MAI isolated sites. @Paul 📅 2025-10-30 #task #proposed #auto

- [?] Create Azure Blob comparison columns (racks, performance, power, capacity) and a one-slide summary view for the Microsoft MAI proposal deck. @Myself 📅 2025-10-31 ⏫ #task #proposed #auto

- [?] Confirm with Kushal the expected cluster sizes, number of sites, and checkpointing approach to refine performance targets for the Microsoft MAI proposal. @Myself 📅 2025-10-31 #task #proposed #auto

- [?] Validate offline identity and RBAC behavior for isolated Microsoft MAI sites, including JWT claims caching and internal DNS and routing behavior, and document limitations. @Ray 📅 2025-11-05 #task #proposed #auto

- [?] Align on the data movement strategy for Microsoft MAI, including whether to use azcopy, service-to-service transfers (for example PutBlobFromURL), or a Sync Engine approach, and document required tooling assumptions for the proposal. @Myself 📅 2025-11-07 🔽 #task #proposed #auto

- [?] Model an NVIDIA NCP reference-aligned high-performance pod (approximately 41,472 GPUs, Series 1350) including usable capacity, sustained read/write performance, rack count, and total power, and include extrapolation toward 1 EB scale for the Microsoft MAI proposal. @Paul 📅 2025-10-30 ⏫ #task #proposed #auto

- [?] Validate and model a capacity and density-optimized 1 EB design using Maverick 5400, including C-node to D-node ratios, performance limits, rack count, and power, and document any gaps versus NVIDIA NCP reference alignment for the Microsoft MAI proposal. @Ray 📅 2025-10-30 ⏫ #task #proposed #auto

- [?] Produce a side-by-side comparison table and rack layout diagrams for both Microsoft MAI designs (NVIDIA NCP-aligned pod and Maverick 5400 density option) and update existing EnScale and Portugal deck templates with the new content. @Paul 📅 2025-10-30 ⏫ #task #proposed #auto

- [?] Provide consolidated sustained read and write performance estimates (TB/s) and total power figures for both Microsoft MAI designs so the deck can present side-by-side comparisons. @Ray 📅 2025-10-30 ⏫ #task #proposed #auto

- [?] Add proposal narrative content covering Kubernetes integration (CSI and COSI), file plus object support, monitoring and logging, and offline authentication and DNS behavior into the Microsoft MAI deck. @Paul 📅 2025-10-30 #task #proposed #auto

- [?] Create Azure Blob comparison columns (racks, performance, power, capacity) and prepare a one-slide view for the Microsoft MAI meeting. @Myself 📅 2025-10-31 ⏫ #task #proposed #auto

- [?] Confirm with Kushal the Microsoft MAI cluster sizes, site count, and checkpointing approach to refine performance targets for the proposal. @Myself 📅 2025-10-31 #task #proposed #auto

- [?] Validate offline identity and RBAC behavior for isolated MAI sites, including JWT claims caching and internal DNS and routing requirements, and document limitations for the proposal. @Ray 📅 2025-11-05 #task #proposed #auto

- [?] Align on a data movement strategy for Microsoft MAI, including azcopy versus service-to-service approaches like PutBlobFromURL versus a Sync Engine approach, and document required tooling assumptions for the proposal. @Myself 📅 2025-11-07 🔽 #task #proposed #auto

## Decisions

- Lead the Microsoft MAI proposal with an NVIDIA NCP reference architecture-aligned high-performance pod design sized around a 40k GPU training cluster to maximize credibility and consistency with InScale messaging.

- Include a second capacity and density-optimized design based on Maverick 5400 targeting 1 EB usable capacity, even if it is not fully aligned to NVIDIA NCP, to show a broader design space.

- Use the ~40k GPU pod as the standard building block and extrapolate the design to reach 1 EB scale for Microsoft MAI.

- Focus the narrative on sustained write throughput for checkpointing and resilience during WAN outages, rather than emphasizing heavyweight Azure Extended Zones or full Azure region dependencies.

- Emphasize Kubernetes CSI and COSI integration plus file and object support as day-one requirements for Microsoft MAI.

- Include a second capacity and density-optimized 1 EB design option based on Maverick 5400 to show an alternative point in the design space.

- Use the ~40k GPU pod as the standard building block and extrapolate to reach 1 EB scale in the proposal tables and diagrams.

- Focus the narrative on sustained write throughput for checkpointing and resilience during WAN outages to an adjacent Azure region.

- Emphasize Kubernetes integration (CSI and COSI) plus file and object support in the proposal, and avoid emphasizing Lifter or RPaaS to keep the control plane footprint minimal for isolated sites.

## Key Information

- Jason Vallery joined VAST Data a little over a week before 2025-10-30 and runs Product Management for Cloud, reporting to Jeff Denworth.

- Jason Vallery previously worked at Microsoft for about 13 years in product management leadership in the object storage team, including hardware responsibilities.

- Microsoft MAI target environment discussed is approximately 160,000 GPUs likely split across about three sites, with single training clusters around 40,000 GPUs.

- Microsoft MAI uses remote Azure Blob as the system of record today, and the VAST proposal positions local storage as a high-performance cache for checkpointing and data pre-staging.

- Microsoft currently manages leased GPU facilities using Azure Extended Zones, which connect facilities back to a nearby Azure region for services like authentication, DNS, networking plane, and control plane, creating a WAN link failure point that can idle GPUs if the link drops.

- Microsoft MAI control plane direction discussed is a thin, standalone AKS-led Kubernetes interface intended to run inside the facility with minimal dependency on an adjacent Azure region.

- NVIDIA NCP largest modeled pod referenced is about 41,472 GPUs with roughly 450 C-nodes and 180 D-nodes (Series 1350), delivering about 215 PB usable per pod, with indicative performance around 11 TB/s read and 4 to 5 TB/s write (subject to per-pod attachment limits).

- Blob throughput comparison guidance referenced is approximately 2.5 Tbps per 100 PB with symmetric read and write, to be used as a comparison column in the deck.

- OpenAI moves data via PutBlobFromURL, while Microsoft MAI uses azcopy today (as referenced in the meeting notes).

- Kubernetes integration requirements called out for Microsoft MAI include CSI and COSI, and the solution must support both file and object interfaces, with OpenAI workloads described as mostly object-oriented.

- Single-pane monitoring and logging within VAST is positioned as a differentiator for isolated sites because Kusto and Log Analytics are not available on-site.

- Resilience requirements for isolated MAI sites include offline behavior such as token or claims caching and internal DNS and routing so GPU clusters can continue operating during WAN outages.

- Decision stakeholders at Microsoft for the MAI storage approach were described as including AKS, Azure Networking (Extended Zones), and Azure Storage, with potential escalation to Scott Guthrie.

- VAST intends to keep the proposal consistent with InScale positioning, because Microsoft is engaging both InScale and VAST directly and VAST wants a consistent story regardless of whether Microsoft buys through InScale or directly from VAST.

---

- Microsoft MAI target environment discussed was approximately 160,000 GPUs likely split across about three sites, with single training clusters around 40,000 GPUs.

- Microsoft MAI currently uses remote Azure Blob Storage for storage in these leased GPU facilities, and the team is evaluating local storage for checkpointing and data pre-staging to reduce dependency on Azure Extended Zones connectivity.

- Azure Extended Zones were described as a networking approach that connects a leased facility back to the nearest Azure region where services like authentication, DNS, networking plane, and control plane live, creating a WAN link failure point that can idle GPUs if the link drops.

- Microsoft MAI control plane direction discussed was a thin, standalone AKS-led Kubernetes interface that can run inside the facility with minimal dependencies on the adjacent Azure region.

- The team planned to present two VAST designs for Microsoft MAI: (1) an NVIDIA NCP reference-aligned high-performance pod sized around a 40k GPU cluster as the primary template, and (2) a capacity and density-optimized option using Maverick 5400 targeting 1 EB scale.

- NVIDIA NCP largest modeled pod referenced was approximately 41,472 GPUs with about 450 C-nodes and about 180 D-nodes (Series 1350), with about 215 PB usable per pod, and indicative performance around 11 TB/s read and 4-5 TB/s write (subject to pod attachment limits).

- Blob throughput guidance used for comparison was approximately 2.5 Tbps per 100 PB with symmetric read and write.

- OpenAI data movement was described as using PutBlobFromURL, while Microsoft MAI uses azcopy today.

- Kubernetes integration requirements called out were CSI and COSI, and the MAI environment needs both file and object access (with OpenAI described as mostly object).

- Single-pane monitoring and logging within VAST was positioned as a differentiator because Kusto and Log Analytics are not available on-site in these isolated facilities.

- Offline resiliency requirements discussed included token and claims caching plus internal DNS and routing so GPUs can continue running during WAN outages.

- Decision stakeholders at Microsoft for this MAI storage direction were described as including AKS, Azure Networking (Extended Zones), and Azure Storage, with potential escalation to Scott Guthrie.

- Alon Horev suggested VAST align the proposal with the approach used with InScale to keep messaging consistent for Microsoft MAI.
