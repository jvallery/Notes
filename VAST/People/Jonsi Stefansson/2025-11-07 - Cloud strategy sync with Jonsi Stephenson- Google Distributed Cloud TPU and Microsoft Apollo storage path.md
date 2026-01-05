---
type: people
title: 'Cloud strategy sync with Jonsi Stephenson: Google Distributed Cloud TPU and Microsoft Apollo storage path'
date: '2025-11-07'
person: Jonsi Stefansson
participants:
- Jason Vallery
- Jonsi Stephenson
source: transcript
source_ref: /Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-11-07 - We aligned on hyperscaler strategy across Google and Microsoft. On Google, GDC i.md
tags:
- type/people
- generated
---

# Cloud strategy sync with Jonsi Stephenson: Google Distributed Cloud TPU and Microsoft Apollo storage path

**Date**: 2025-11-07
**With**: Jason Vallery, Jonsi Stephenson

## Summary

Jason Vallery and Jonsi Stephenson aligned on hyperscaler strategy across Google and Microsoft. For Google, Google Distributed Cloud (GDC) is emerging as the vehicle for on-prem TPU deployments, where VAST is one of only two viable file options and VAST TPU benchmarks reportedly beat Google managed Lustre by about 20% plus a cross-region global namespace demo (Japan to Ohio). For Microsoft, Project Apollo and MAI storage requirements push VAST toward an Azure Storage hardware deployment path rather than LSVx VMs, with MAI Falcon (about 120k GPUs in Dallas) at risk if storage underperforms; Marketplace remains a required checkbox and a simpler managed cloud billing unit (vCPU plus capacity) is being pursued.

## Action Items

- [?] Share TPU benchmark write-up and numbers to support upcoming Google Distributed Cloud (GDC) meetings. @Jonsi Stephenson 📅 2025-11-14 ⏫ #task #proposed #auto

- [?] Attend internal pricing model meeting focused on simplifying cloud pricing to a managed unit (vCPU plus capacity). @Myself 📅 2025-11-10 ⏫ #task #proposed #auto

- [?] Prepare power, space, and GPU-throughput tables for Microsoft stakeholders, indexed by capacity and GPU count, to support the Nidhi briefing on Apollo, MAI, and Azure Storage hardware approach. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Coordinate with Kanchan Mehrotra and brief Nidhi on Microsoft Project Apollo, Microsoft AI Infrastructure (MAI), UK Met strategy, and the plan to run VAST Data on Azure Storage hardware. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Socialize the VAST-on-Azure-Storage-hardware approach with Maneesh Sah's organization via Kanchan Mehrotra, including connecting with Michael Myrah. @Myself 📅 2025-11-08 #task #proposed #auto

- [?] Define a proposal for a managed cloud billing unit (vCPU plus capacity) and circulate it for leadership buy-in to address competitiveness and transparency concerns. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Join Google Distributed Cloud (GDC) leadership sessions remotely due to travel and house move constraints. @Jonsi Stephenson 📅 2025-11-13 #task #proposed #auto

- [?] Attend Google Distributed Cloud (GDC) team meeting to position VAST Data using TPU benchmark results and integration narrative. @Myself 📅 2025-11-14 ⏫ #task #proposed #auto

- [?] Schedule an in-person dinner or 1:1 between Monday and Wednesday next week to continue hyperscaler strategy alignment. @Myself 📅 2025-11-12 🔽 #task #proposed #auto

- [?] Confirm Walmart meeting timing, attendees, and objectives for next week. @Myself 📅 2025-11-12 #task #proposed #auto

- [?] Request and obtain formal next-generation Azure Storage hardware specifications from Anson (Qi) for planning purposes. @Myself 📅 2025-11-08 #task #proposed #auto

- [?] Assess feasibility and implications of NVIDIA BlueField versus Fungible DPUs for Microsoft Project Apollo integration with VAST Data. @Myself 📅 2025-11-08 #task #proposed #auto

- [?] Share TPU benchmark write-up and numbers for upcoming Google meetings. @Jonsi Stephenson 📅 2025-11-14 ⏫ #task #proposed #auto

- [?] Attend internal pricing model meeting to advance a simpler managed cloud billing unit (vCPU plus capacity). @Myself 📅 2025-11-10 ⏫ #task #proposed #auto

- [?] Prepare power, space, and GPU-throughput tables for Microsoft (capacity-indexed and GPU-indexed) to support the Nidhi briefing on Apollo and MAI storage planning. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Coordinate with Kanchan Mehrotra and brief Nidhi on Microsoft Apollo, Microsoft AI Infrastructure (MAI), UK Met strategy, and the Azure Storage hardware plan for VAST at scale. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Join Google Distributed Cloud leadership sessions remotely due to travel and house move constraints. @Jonsi Stephenson 📅 2025-11-13 #task #proposed #auto

- [?] Attend Google Distributed Cloud team meeting to advance GDC integration and TPU on-prem positioning. @Myself 📅 2025-11-14 ⏫ #task #proposed #auto

- [?] Schedule an in-person dinner or 1:1 with Jonsi Stephenson (Mon to Wed next week) to continue hyperscaler strategy alignment. @Myself 📅 2025-11-12 🔽 #task #proposed #auto

- [?] Request and obtain formal next-generation Azure Storage hardware specifications from Anson (Qi) for planning. @Myself 📅 2025-11-08 #task #proposed #auto

- [?] Assess feasibility and implications of NVIDIA BlueField versus Fungible DPUs for Microsoft Apollo integration with VAST Data. @Myself 📅 2025-11-08 #task #proposed #auto

## Decisions

- Use VAST Data real-workload TPU benchmark results and the cross-region global namespace demo as primary evidence in upcoming Google Distributed Cloud (GDC) leadership discussions.

- Prioritize the Azure Storage hardware path (running VAST Data on Azure Storage hardware) over Azure LSVx VMs for large-scale GPU and exabyte-scale throughput requirements.

- Treat Microsoft Azure as a distinct sell-to motion (first-party or Azure Storage hardware aligned) separate from Marketplace sell-through, while still making Marketplace listing a near-term priority.

- Use real-workload benchmarks rather than synthetic benchmarks as the standard for TPU and storage evaluations with Google.

- Use VAST Data real-workload TPU benchmark results (not synthetic benchmarks) as the standard evidence set for Google TPU and storage evaluations in upcoming Google Distributed Cloud discussions.

- Pursue deeper integration with Google Distributed Cloud and aim for VAST Data to be part of the GDC SKU for on-prem TPU deployments tied back to GCP.

- Prioritize the Azure Storage hardware deployment path for large-scale Microsoft AI Infrastructure (MAI) and supercomputer deployments rather than relying on Azure LSVx VM approaches.

- Treat Microsoft Azure as two distinct motions: a first-party or Azure Storage hardware path for MAI and Apollo scale needs, and a separate Marketplace sell-through motion as a required checkbox.

## Key Information

- Google Distributed Cloud (GDC) is emerging as Google's vehicle to deliver on-prem TPU deployments with tie-ins back to Google Cloud Platform (GCP).

- On Google Distributed Cloud (GDC), the only viable file storage options currently discussed were VAST Data and NetApp; NetApp's approach relies on reviving OnTap Select, a legacy stack previously end-of-life'd around 2019.

- VAST Data TPU testing using Google's model set reportedly showed about 20% better performance than Google's current managed Lustre stack, and a cross-region global namespace demo (Japan to Ohio) resonated with Google stakeholders.

- Two Sigma is described as running NVIDIA GPUs on-prem and adopting Google TPUs for training; they want VAST Data across on-prem and GCP via Google Marketplace and are behind on cloud commit targets.

- Microsoft Project Apollo is described as a Linux and Kubernetes control plane for supercomputers with Microsoft AI Infrastructure (MAI) as the first tenant; DPUs are under consideration (NVIDIA BlueField vs Fungible).

- Azure LSVx virtual machines are not viable for exabyte-scale or large GPU cluster throughput, pushing the preferred approach toward running VAST Data on Azure Storage hardware (notably a Gen9 flash SKU with about 40Gb NICs mentioned in notes).

- MAI 'Falcon' build is described as a roughly 120,000 GPU build in Dallas targeted for April, with risk that storage underperformance could strand GPUs; the team is exploring swapping Azure Storage's software stack for VAST Data on Azure Storage hardware.

- Microsoft stakeholders require a Marketplace listing as a credibility and process checkbox for VAST Data motions in Azure.

- Leadership concern was raised that current cloud pricing may be uncompetitive; a simpler managed pricing unit based on vCPU plus capacity was discussed to improve transparency and competitiveness.

- A Google contact asked Jonsi Stephenson friend-to-friend whether VAST Data would consider being acquired by Google; Jason Vallery responded that VAST Data is 'for sale for the right price' but that replicating the CoreWeave-style deal is more interesting to keep options open.

- Jonsi Stephenson stated the CoreWeave deal headline number is being 'fluffed' and described a structure with about $270M base and additional stage-gated amounts tied to deliverables like ease of management and feature exposure; he believed VAST Data can deliver the commitments over a multi-year term.

- Edge or minimal-footprint deployments like the McDonald's scenario (described as a few 'pizza box' servers per site) are not a fit for VAST Data's current footprint and deployment model.

---

- Jonsi Stephenson reported that a Google contact who leads "Google Corta" asked friend-to-friend whether VAST Data would consider being acquired by Google.

- Jason Vallery stated that VAST Data would be "for sale for the right price" but that replicating the CoreWeave-style partnership model is more interesting because it keeps options open with other partners.

- Jonsi Stephenson stated the CoreWeave deal is being discussed publicly as a larger number, but the true revenue is about $270 million to $278 million with additional stage-gated requirements that could add about $400 million, and the deal term is about six years.

- Jonsi Stephenson believes VAST Data can deliver the CoreWeave stage-gated requirements, and does not see glaring delivery risks, but noted the deal has attracted significant attention.

- Google Distributed Cloud (GDC) is expected to become Google's primary vehicle to deliver TPUs on-prem because Google needs tie-ins back to Google Cloud Platform (GCP) and a surrounding software stack beyond just shipping TPU hardware.

- Jonsi Stephenson stated that for GDC file storage options, only VAST Data and NetApp are currently present, and NetApp is relying on a revived OnTap Select software stack that was previously end-of-life notified in 2019.

- VAST Data TPU testing using Google's model set reportedly showed about 20% better performance than Google's current managed Lustre stack, and a cross-region global namespace demo between Japan and Ohio resonated with Google stakeholders.

- Jason Vallery stated that VAST Data cannot scale down to the minimal footprint required for edge-style deployments like a McDonald's restaurant footprint described as "a couple of pizza boxes".

- Two Sigma is described as running NVIDIA GPUs on-prem and adopting Google TPUs for training, and wants VAST Data across on-prem and GCP via Marketplace, but is behind on cloud commitments.

- Microsoft Project Apollo is described as a Linux and Kubernetes control plane for supercomputers with Microsoft AI Infrastructure (MAI) as the first tenant, and DPUs are under consideration (NVIDIA BlueField versus Fungible).

- Azure LSVx VMs are described as not viable for exabyte-scale or large GPU cluster throughput, pushing VAST Data toward running on Azure Storage hardware (Gen9 flash SKU with about 40Gb NICs).

- MAI Falcon build is described as about 120,000 GPUs planned for April in Dallas, with risk of GPU stranding if storage underperforms; the team is exploring swapping Azure Storage software for VAST on Azure Storage hardware.

- Microsoft stakeholders require a Marketplace listing as a credibility and alignment checkbox for VAST Data motions in Azure.

- Leadership concern was noted that current cloud pricing may be uncompetitive; a simpler managed billing unit based on vCPU plus capacity is being pursued for transparency and competitiveness.
