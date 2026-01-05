---
type: "people"
title: "G24 Flight School: VAST Story, Business Acumen (MAI, Bifrost, Azure Blob integration positioning)"
date: "2025-12-16"
person: ""
participants: ["Jason Vallery", "TBD"]
source: "transcript"
source_ref: "/Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-12-16 08:35 - G24 Flight School 🧑‍🚀:  VAST Story: Business Acumen .md"
tags:
  - "type/people"
  - "person/"
  - "generated"

---

# G24 Flight School: VAST Story, Business Acumen (MAI, Bifrost, Azure Blob integration positioning)

**Date**: 2025-12-16
**With**: Jason Vallery, TBD

## Summary

Discussion centered on Microsoft MAI politics after Inflection integration, the internal Azure response projects Apollo and Bifrost, and how VAST should position a win-win partnership with Azure Blob. Jason Vallery explained why Microsoft stakeholders are upset about a VAST vs Bifrost comparison and recommended a clear workload carve-out: Azure Blob for exabyte-scale central data lakes and VAST for GPU-adjacent storage in Azure and non-Azure GPU fleets (Nebius, neoclouds, on-prem).


## Action Items


- [?] Brief the other meeting participant before their 1:1 meetings with Microsoft contacts (including Ong and Manish Sah) on the MAI, Apollo, and Bifrost context, the VAST vs Bifrost comparison sensitivity, and the recommended Azure Blob plus VAST GPU-adjacent positioning. @Myself 📅 2025-12-17 ⏫ #task #proposed #auto

- [?] Validate and document a clear external-safe narrative for how internal Azure Storage and Bifrost information was obtained and used, ensuring VAST Data avoids any implication of using Microsoft confidential information. @Myself 📅 2025-12-19 ⏫ #task #proposed #auto

- [?] Draft a partnership pitch outline for Microsoft that frames the workload split (Blob for central data lakes, VAST for GPU-adjacent storage) and specifies the deep integration points needed with Azure Blob for data movement across Azure regions and non-Azure GPU sites (Nebius, neoclouds, on-prem). @Myself 📅 2025-12-23 #task #proposed #auto




## Decisions


- Position the VAST Data and Microsoft Azure partnership as a workload carve-out: Azure Blob for central exabyte-scale data lakes in large Azure regions, and VAST Data for GPU-adjacent storage in Azure and non-Azure GPU fleets (Nebius, neoclouds, on-prem).

- Avoid leading with VAST higher-level database and data services in the Microsoft MAI partnership pitch, and focus the ask on deep integration with Azure Blob to enable data movement between central Azure regions and GPU-adjacent VAST deployments.




## Key Information


- Microsoft MAI preferred VAST Data prior to Inflection's acquisition by Microsoft, and MAI had been using VAST before being pushed to run on Azure.

- A key MAI stakeholder named Kushaldada owns the relationship between Microsoft AI and Azure and contacted Jason Vallery after Jason left Microsoft to ask what a VAST-based approach would look like.

- After Inflection joined Microsoft, a priority was to integrate them into Azure due to Microsoft's 'eat our own dog food' culture, and their first Azure supercomputer (delivered around July 2025 per transcript context) had major issues across storage, Kubernetes, control plane, reliability, and networking.

- Mustafa Suleyman escalated internally that Microsoft AI could not be on the current Azure solution, which triggered significant pressure on Azure and kicked off a project called Apollo to create a net-new Azure approach.

- Manish Sah initiated or sponsored a project called Bifrost, staffed with roughly 30+ developers, intended to address performance and other issues across the Azure stack (including mention of a new client driver) and was pitched to MAI as a comprehensive fix.

- Jason Vallery stated he received internal Azure Storage and Bifrost specifications from the HPC AI team (described as Niti's former team) after he joined VAST Data, and he was careful to frame that the information came to him in his new role to avoid legal exposure.

- Jason Vallery created a comparison presentation of VAST Data versus Microsoft's Bifrost solution and shared it back into Microsoft context, which contributed to Manish Sah being upset because it portrayed Bifrost negatively and implied access to internal details.

- A Microsoft individual referred to as 'BoloL' in Niti's former organization was mentioned as nearly being fired after Lior Genzel raised the issue in a meeting with a Microsoft contact named 'Garish' (exact identity unclear).

- Vamsi (Microsoft contact) was frustrated that VAST did not clearly explain the agenda and meeting plan for a Redmond trip, though Jason Vallery offered to include Vamsi in meetings.

- Jason Vallery recommended positioning a partnership model where Azure Blob serves central, exabyte-scale data lakes in large Azure regions (CPU-heavy analytics like Spark and Azure Databricks), while VAST Data provides GPU-adjacent storage for staging, checkpoints, and training data across Azure, neoclouds (Nebius), and on-prem GPU fleets.

- Jason Vallery stated Azure Blob is difficult for Microsoft to deploy efficiently outside Azure regions (for example in Nebius facilities and other non-Azure cloud providers) due to power, network efficiency, and networking issues, creating an opening for VAST to provide a small-footprint GPU-adjacent deployment integrated with Blob.



---

*Source: [[2025-12-16 08:35 - G24 Flight School 🧑‍🚀:  VAST Story: Business Acumen ]]*