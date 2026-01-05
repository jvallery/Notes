---
type: "customer"
title: "MAI exabyte-scale storage proposal: NCP-aligned 41k-GPU pod plus Maverick 5400 capacity option"
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

# MAI exabyte-scale storage proposal: NCP-aligned 41k-GPU pod plus Maverick 5400 capacity option

**Date**: 2025-10-30
**Account**: [[]]
**Attendees**: Jason Vallery, Paul, Ray

## Summary

Jason Vallery, Paul, and Ray aligned on presenting Microsoft MAI two exabyte-scale VAST storage architectures: an NVIDIA NCP-aligned high-performance pod sized for ~41k GPUs as the baseline building block, and a high-density Maverick 5400 capacity-optimized 1 EB alternative with performance trade-offs. The narrative emphasizes AKS-led standalone control plane for neo-cloud/leased sites, local storage for checkpointing during WAN outages, Kubernetes integration (CSI/COSI), file plus object interfaces, and single-pane monitoring/logging where Azure services are unavailable.


## Action Items


- [?] Draft NCP-aligned design slides and rack diagrams for a 41,472-GPU pod (approximately 450 C-nodes, 180 D-nodes, approximately 215 PB usable) and extrapolate the design to a 1 EB reference. @Paul 📅 2025-10-30 ⏫ #task #proposed #auto

- [?] Compile performance, capacity, and power metrics for the NCP-aligned pod and produce a side-by-side metrics table for the deck. @Ray 📅 2025-10-30 ⏫ #task #proposed #auto

- [?] Design the capacity-optimized Maverick 5400 exabyte option and rack layout, including C-node to D-node ratio variants (for example 420:210 and 105:210). @Paul 📅 2025-10-30 ⏫ #task #proposed #auto

- [?] Model read/write performance and power for the Maverick 5400 option at the chosen C-node to D-node ratios and validate backend media throughput limits. @Ray 📅 2025-10-30 ⏫ #task #proposed #auto

- [?] Add deck bullets covering Kubernetes integration (CSI/COSI), file plus object support, single-pane monitoring/logging, and offline authentication and DNS resiliency. @Paul 📅 2025-10-30 ⏫ #task #proposed #auto

- [?] Create a one-slide or Excel view adding Azure Blob comparison columns for the 1 EB reference baseline for follow-on MAI discussions. @Myself 📅 2025-10-31 ⏫ #task #proposed #auto

- [?] Join the Microsoft MAI call to present the architecture and answer technical questions. @Paul 📅 2025-10-31 ⏫ #task #proposed #auto

- [?] Join the Microsoft MAI call to present performance and power modeling and explain NVIDIA NCP alignment. @Ray 📅 2025-10-31 ⏫ #task #proposed #auto

- [?] Confirm with Microsoft MAI the checkpointing method and sustained write throughput targets needed to meet checkpoint cadence. @Myself 📅 2025-10-31 ⏫ #task #proposed #auto

- [?] Validate with Microsoft MAI how the 160,000 GPUs are distributed across sites and what the maximum non-blocking training cluster size is. @Myself 📅 2025-10-31 #task #proposed #auto

- [?] Clarify with Microsoft MAI the standard data movement approach (azcopy scripting vs PutBlobFromURL pipelines vs custom vs VAST Sync Engine) and implications for the storage design. @Myself 📅 2025-11-05 #task #proposed #auto

- [?] Confirm NVIDIA acceptance or certification posture for a Maverick-based capacity-optimized design that may not be part of NVIDIA NCP certification. @Ray 📅 2025-11-05 #task #proposed #auto




## Decisions


- Present Microsoft MAI an NVIDIA NCP reference architecture aligned baseline option sized as a ~41,472 GPU pod with ~215 PB usable capacity, and extrapolate the design to a 1 EB reference scale.

- Present a second Microsoft MAI option as a capacity-optimized 1 EB design using Maverick 5400 with explicit performance trade-offs and C-node to D-node ratio variants.

- Use 1 EB as the common comparison baseline across the two options for racks, performance, capacity, and power.

- Defer direct Azure Blob comparison in the next MAI call and prepare it for follow-on 1:1 and broader stakeholder discussions.

- Avoid emphasizing Azure Lifter or RPaaS APIs in the narrative and prioritize compatibility with a thin, standalone control plane approach led by AKS.




## Key Information


- Microsoft MAI target environment discussed is approximately 160,000 GPUs, likely split across about 3 sites, with proposed sizing per approximately 40,000 GPU training clusters.

- Baseline architecture option for Microsoft MAI is an NVIDIA NCP-aligned pod supporting 41,472 GPUs with approximately 450 C-nodes and 180 D-nodes, delivering about 215 PB usable capacity per pod.

- Baseline NCP-aligned pod performance estimate is approximately 11 TB/s read and approximately 4 to 5 TB/s write per pod.

- Capacity-optimized alternative for Microsoft MAI is based on Maverick 5400 at 5.4 PB per 2U; an exabyte-class build is approximately 210 Mavericks usable after erasure coding.

- Maverick capacity option sizing discussed uses a typical C-node to D-node ratio near 2:1, with examples of approximately 420 C-nodes for performance or approximately 105 C-nodes as a minimal capacity-focused configuration with lower performance.

- Maverick rack density estimate is approximately 30 racks for about 1 EB, while a 1350-series based design would require approximately 4 to 5 times more racks for similar capacity.

- Azure Blob reference metric used for comparison is approximately 2.5 Tbps read/write per 100 PB, implying approximately 25 Tbps aggregate per 1 EB.

- Microsoft is deploying GPUs in leased data center capacity and neo-cloud sites that are not full Azure regions, limiting available Azure services and creating operational dependencies.

- Microsoft uses Azure Extended Zones to connect leased/neo-cloud GPU sites back to a nearby Azure region for services like authentication, DNS, networking plane, and control plane, but the WAN link becomes a failure point that can idle GPUs if it drops.

- AKS is leading an approach for a thin, standalone control plane for leased/neo-cloud sites to reduce dependency on adjacent Azure regions and avoid the heavy lift of turning a site into a full Azure region (estimated 60 to 80 racks of compute plus engineering work).

- Data movement approaches mentioned include OpenAI using PutBlobFromURL pipelines and Microsoft MAI using azcopy with scripting; VAST Sync Engine is considered optional and requires fit validation.

- Interfaces expected for the MAI environment include Kubernetes CSI and COSI, and likely both file and object access, with MAI preferring file today but moving toward object.

- Single-pane monitoring and logging in VAST is positioned as valuable for these sites because Azure Log Analytics and Kusto are typically unavailable in leased/neo-cloud environments.

- Jason Vallery joined VAST Data a little over a week before 2025-10-30, runs cloud product management, reports to Jeff Denworth, and previously spent 13 years in Microsoft object storage product management leadership including hardware responsibilities.



---

*Source: [[2025-10-30 - Team aligned on presenting two exabyte-scale storage options for MAI (1) an NVI]]*