---
type: "customer"
title: "MAI exabyte-scale storage options: NVIDIA NCP-aligned 41k-GPU pod baseline plus Maverick 5400 capacity variant"
date: "2025-10-30"
account: ""
participants: ["Jason Vallery", "Paul", "Ray"]
source: "transcript"
source_ref: "/Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-10-30 - Team aligned on presenting two exabyte-scale storage options for MAI (1) an NVI.md"
tags:
  - "type/customer"
  - "account/"
  - "generated"

---

# MAI exabyte-scale storage options: NVIDIA NCP-aligned 41k-GPU pod baseline plus Maverick 5400 capacity variant

**Date**: 2025-10-30
**Account**: [[]]
**Attendees**: Jason Vallery, Paul, Ray

## Summary

Internal VAST team aligned on how to present two exabyte-scale storage architectures to the Microsoft MAI team: an NVIDIA NCP-aligned high-performance pod sized around a 41,472-GPU building block, and a high-density Maverick 5400 capacity-optimized 1 EB alternative with performance trade-offs. The narrative emphasizes an AKS-led thin standalone control plane for neo-cloud and leased sites, local storage for checkpointing during WAN outages, Kubernetes integration (CSI/COSI), file plus object interfaces, and single-pane monitoring/logging for environments without full Azure services.


## Action Items


- [?] Draft NCP-aligned design slides and rack diagrams for a 41,472-GPU pod (approximately 450 C-nodes, 180 D-nodes, approximately 215 PB usable) and extrapolate the design to a 1 EB reference. @Paul 📅 2025-10-30 ⏫ #task #proposed #auto

- [?] Compile performance, capacity, and power metrics for the NVIDIA NCP-aligned pod and produce a side-by-side metrics table for the deck (racks, read/write performance, capacity, power). @Ray 📅 2025-10-30 ⏫ #task #proposed #auto

- [?] Design the capacity-optimized Maverick 5400 exabyte option and rack layout, including C:D ratio variants (for example 420:210 and 105:210) and document the performance trade-offs. @Paul 📅 2025-10-30 ⏫ #task #proposed #auto

- [?] Model read/write performance and power for the Maverick 5400 option at the chosen C:D ratios and validate backend media throughput limits that could cap gains from additional C-nodes. @Ray 📅 2025-10-30 ⏫ #task #proposed #auto

- [?] Add deck bullets covering Kubernetes integration (CSI/COSI), file plus object support, single-pane monitoring/logging, and offline resiliency requirements (offline auth, DNS) for WAN loss scenarios. @Paul 📅 2025-10-30 ⏫ #task #proposed #auto

- [?] Create a one-slide or Excel view adding Azure Blob comparison columns for the 1 EB reference baseline for a follow-on 1:1 with Microsoft MAI stakeholders. @Myself 📅 2025-10-31 ⏫ #task #proposed #auto

- [?] Join the Microsoft MAI call to present the architecture and answer technical questions. @Paul 📅 2025-10-31 #task #proposed #auto

- [?] Join the Microsoft MAI call to present performance and power modeling and explain NVIDIA NCP alignment. @Ray 📅 2025-10-31 #task #proposed #auto

- [?] Confirm Microsoft MAI checkpointing method and sustained write throughput targets during a 1:1 discussion to avoid mis-sizing the storage performance design. @Myself 📅 2025-10-31 ⏫ #task #proposed #auto

- [?] Validate how Microsoft MAI plans to distribute 160,000 GPUs across sites and determine the maximum non-blocking training cluster size to confirm pod sizing assumptions. @Myself 📅 2025-10-31 ⏫ #task #proposed #auto

- [?] Clarify Microsoft MAI data movement standard (azcopy vs PutBlobFromURL pipelines vs custom vs VAST Sync Engine) and capture implications for architecture and operations. @Myself 📅 2025-11-05 #task #proposed #auto

- [?] Confirm NVIDIA acceptance or certification posture for a Maverick-based capacity-optimized exabyte design that is not part of the NVIDIA NCP reference architecture. @Ray 📅 2025-11-05 #task #proposed #auto




## Decisions


- Present to the Microsoft MAI team two exabyte-scale VAST architectures: (1) an NVIDIA NCP reference architecture aligned 41,472-GPU pod as the baseline building block and (2) a capacity-optimized Maverick 5400-based 1 EB option with explicit performance trade-offs.

- Use 1 EB as the common comparison baseline across the two options (racks, read/write performance, capacity, and power).

- Avoid pricing and quoting in the Microsoft MAI call and keep messaging consistent with the NScale narrative so Microsoft receives a consistent VAST story whether via NScale or direct.

- Defer direct Azure Blob comparison in the immediate Microsoft MAI call and prepare it for follow-on 1:1 and broader stakeholder discussions.

- Do not emphasize Azure Lifter or RPaaS APIs in the narrative, prioritize compatibility with a thin standalone control plane led by AKS for leased or neo-cloud sites.




## Key Information


- Microsoft MAI target environment discussed is approximately 160,000 GPUs, likely split across about 3 sites, with proposed sizing around approximately 40,000-GPU training clusters per site/pod.

- Baseline architecture proposed for Microsoft MAI is an NVIDIA NCP-aligned pod supporting 41,472 GPUs with approximately 450 C-nodes and 180 D-nodes, delivering about 215 PB usable capacity per pod.

- Baseline performance estimate for the NVIDIA NCP-aligned pod is approximately 11 TB/s read and approximately 4 to 5 TB/s write per pod.

- Capacity-optimized alternative discussed is a Maverick 5400-based design at approximately 5.4 PB per 2U, with an exabyte-class build requiring about 210 Mavericks usable after erasure coding.

- Maverick capacity option sizing discussed includes a typical C:D ratio near 2:1, with example variants of approximately 420 C-nodes to 210 D-nodes for higher performance, or approximately 105 C-nodes to 210 D-nodes for minimal compute and lower performance.

- Rack density estimate for the Maverick 5400 option is approximately 30 racks for about 1 EB, while a 1350-series approach would require approximately 4 to 5 times more racks for similar capacity.

- Azure Blob reference point used for comparison is approximately 2.5 Tbps read/write per 100 PB, implying approximately 25 Tbps aggregate per 1 EB.

- Microsoft MAI neo-cloud and leased GPU sites are often managed via Azure Extended Zones, which depend on WAN connectivity back to a nearby Azure region for services like authentication, DNS, networking plane, and control plane, creating a failure point that can idle GPUs during link outages.

- AKS is described as leading a thin standalone control plane approach for these leased or neo-cloud sites to reduce dependency on a full Azure region and avoid the heavy lift of turning a site into a full Azure region (described as 60 to 80 racks of compute plus significant engineering).

- Data movement approaches mentioned include OpenAI using PutBlobFromURL pipelines and Microsoft MAI using azcopy with scripting, with VAST Sync Engine described as optional and requiring fit validation.

- Interface requirements discussed for Microsoft MAI include Kubernetes CSI and COSI integration, and likely needing both file and object interfaces, with MAI described as preferring file today but moving toward object.

- Single-pane monitoring and logging in VAST is positioned as valuable for these sites because Azure Log Analytics and Kusto are typically unavailable in leased or neo-cloud facilities.

- Jason Vallery stated he joined VAST Data a little over a week before 2025-10-30, runs product management for cloud, reports to Jeff Denworth, and previously spent 13 years at Microsoft in object storage product management leadership including hardware responsibilities.



---

*Source: [[2025-10-30 - Team aligned on presenting two exabyte-scale storage options for MAI (1) an NVI]]*