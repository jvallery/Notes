---
type: "projects"
title: "MAI-Azure politics and VAST positioning: GPU-adjacent storage with deep Azure Blob integration"
date: "2025-12-16"
project: ""
participants: ["Jason Vallery", "Unknown participant (called \"Nancy\" in transcript)", "Jeff Denworth", "Lior Genzel", "Manish Sah", "Kushal Dada", "Mustafa Suleyman", "Satya Nadella", "Vamsi (unknown last name)", "Niti (unknown last name)", "Bolol (unknown last name)", "Garish (unknown last name)", "Ong (unknown last name)"]
source: "transcript"
source_ref: "/Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-12-16 08:35 - G24 Flight School 🧑‍🚀:  VAST Story: Business Acumen .md"
tags:
  - "type/projects"
  - "project/"
  - "generated"

---

# MAI-Azure politics and VAST positioning: GPU-adjacent storage with deep Azure Blob integration

**Date**: 2025-12-16
**Project**: [[]]
**Attendees**: Jason Vallery, Unknown participant (called "Nancy" in transcript), Jeff Denworth, Lior Genzel, Manish Sah, Kushal Dada, Mustafa Suleyman, Satya Nadella, Vamsi (unknown last name), Niti (unknown last name), Bolol (unknown last name), Garish (unknown last name), Ong (unknown last name)

## Summary

Discussion focused on Microsoft AI Infrastructure (MAI) dissatisfaction with Azure after the Inflection acquisition, the resulting internal Azure initiatives (Apollo and Bifrost), and how a VAST vs Bifrost comparison escalated tensions. The group aligned on a partnership framing where Azure Blob serves central exabyte-scale data lakes and VAST provides power and space efficient GPU-adjacent storage in Azure, neoclouds, and on-prem, enabled by deep integration with Azure Blob.


## Action Items


- [?] Brief the participant (unknown, called "Nancy" in transcript) on the MAI, Apollo, and Bifrost context and likely pushback points before their 1:1 meetings with Ong and Manish Sah on 2025-12-17. @Myself 📅 2025-12-17 ⏫ #task #proposed #auto

- [?] Prepare a crisp talk track for Microsoft that frames the win-win as Azure Blob for central data lakes and VAST for GPU-adjacent storage, including why Blob is hard to deploy efficiently outside Azure regions and how deep integration would work at a high level. @Myself 📅 2025-12-17 ⏫ #task #proposed #auto

- [?] Validate internally with VAST legal and leadership (including Jeff Denworth) the safe messaging and handling of any Microsoft internal specifications to avoid claims of misuse of confidential information. @Myself 📅 2025-12-20 ⏫ #task #proposed #auto




## Decisions


- Position the Microsoft MAI partnership as a carve-out where Azure Blob is the central exabyte-scale data lake and VAST Data provides GPU-adjacent storage with a small footprint, enabled by deep integration for data movement between Blob and VAST.




## Key Information


- Microsoft AI Infrastructure (MAI) had significant issues running an early Azure supercomputer deployment in July 2025, including storage, Kubernetes, control plane, node reliability, and networking problems across the stack.

- Mustafa Suleyman, who runs Microsoft AI, escalated internally that MAI could not be on the current Azure solution after the problematic Azure supercomputer deployment.

- The escalation triggered an internal Azure effort referred to as Project Apollo, described as creating a net new Azure approach to address MAI needs.

- Manish Sah is leading an internal Microsoft project called Bifrost, positioned to MAI as a solution to fix performance and other issues across the Azure stack, including work such as a new client driver and other improvements.

- A Microsoft contact managing the Bifrost team described Bifrost as "lipstick on a pig" and said the team has roughly 30+ developers working on it.

- Kushal Dada is a key stakeholder at MAI and owns the relationship between Microsoft AI and Azure, which are described as two very different internal organizations.

- Kushal Dada contacted Jason Vallery after Jason left Microsoft and joined VAST Data to ask what an MAI deployment on VAST would look like, especially for a large supercomputer not located in Azure.

- Jason Vallery stated he received internal Azure Storage and Bifrost specifications from the Microsoft HPC AI team (described as Niti's former team) during post-Microsoft employment, and he was careful to document that the request came in his new role at VAST Data.

- Jeff Denworth was concerned that Jason Vallery could end up in a legal situation similar to another participant's situation, where Microsoft sues VAST Data due to use of internal Microsoft information.

- Lior Genzel raised a specific Microsoft contact (named Bolol, last name unknown) in a meeting with a Microsoft person named Garish (last name unknown), and the transcript claims that contact "almost got fired" as a result.

- Jason Vallery created a PowerPoint comparing VAST Data versus Microsoft's Bifrost solution and shared it back to Microsoft, which contributed to Manish Sah being angry because it portrayed Bifrost negatively and implied access to internal details.

- Vamsi (last name unknown) was upset that the VAST team did not provide clarity on why they were in Redmond, who they were meeting with, and what the agenda was; Jason Vallery offered to include Vamsi in meetings.

- The proposed VAST positioning for Microsoft MAI is to integrate deeply with Azure Blob so Azure Blob remains the central exabyte-scale data lake, while VAST provides GPU-adjacent storage for staging, checkpoints, and training data near disaggregated GPU fleets in Azure, neoclouds (for example Nebius), and on-prem.

- Jason Vallery asserted that deploying Azure Blob outside Azure regions (for example in Nebius facilities and other non-Azure cloud providers) is difficult and inefficient due to networking and footprint constraints, creating an opening for VAST to provide a small-footprint GPU-adjacent deployment integrated with Blob.

- Jason Vallery recommended avoiding bringing VAST database and higher-level data services into the Microsoft MAI partnership conversation, and instead focusing narrowly on enabling MAI's GPU-adjacent storage needs with Blob integration.



---

*Source: [[2025-12-16 08:35 - G24 Flight School 🧑‍🚀:  VAST Story: Business Acumen ]]*