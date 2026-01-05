---
type: "people"
title: "1:1 with Jonsi Stephenson, MAI-Azure dynamics, Bifrost vs VAST positioning, and Azure Blob integration angle"
date: "2026-01-05"
person: ""
participants: ["Jason Vallery", "Jonsi Stephenson"]
source: "transcript"
source_ref: "/Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/Jonsi:Jason 1-1 .md"
tags:
  - "type/people"
  - "person/"
  - "generated"

---

# 1:1 with Jonsi Stephenson, MAI-Azure dynamics, Bifrost vs VAST positioning, and Azure Blob integration angle

**Date**: 2026-01-05
**With**: Jason Vallery, Jonsi Stephenson

## Summary

Jason Vallery debriefed Jonsi Stephenson on Microsoft MAI and Azure internal politics driving scrutiny of VAST, including Manish Sah's Bifrost initiative and sensitivity around internal specs being compared to VAST. Jonsi and Jason aligned on a potential 'better together' story where VAST focuses on high-performance file and GPU-adjacent storage while integrating tightly with Azure Blob for object storage and global namespace needs across Azure and external GPU clouds.


## Action Items


- [?] Brief Jonsi Stephenson before his Microsoft 1:1 meetings (including likely pushback from Manish Sah's organization and how to frame the VAST vs Bifrost comparison and Azure Blob integration narrative). @Myself 📅 2026-01-06 ⏫ #task #proposed #auto




## Decisions


- Jonsi Stephenson will proceed with scheduled 1:1 meetings now that the temporary restraining order is lifted.

- Jason Vallery and Jonsi Stephenson will position a potential Microsoft partnership narrative around tighter VAST integration with Azure Blob, with VAST focusing on high-performance file and GPU-adjacent storage rather than being the primary object store.




## Key Information


- Jonsi Stephenson said a temporary restraining order that previously limited his ability to take meetings is no longer in place, and the remaining legal focus is on a solicitation-related issue.

- Jason Vallery stated that a key Microsoft AI Infrastructure stakeholder named Kushal Dada owns the relationship between Microsoft AI and Azure, and Kushal Dada contacted Jason after Jason left Microsoft to ask what a VAST-based approach would look like.

- Jason Vallery stated that after Microsoft acquired Inflection, Microsoft pushed Inflection onto Azure under an 'eat our own dog food' principle, and Inflection's first Azure supercomputer (delivered around July 2025) had major issues across storage, Kubernetes, control plane, reliability, and networking, triggering escalation by Mustafa Suleyman (head of Microsoft AI).

- Jason Vallery stated that the escalation led to an internal project called Apollo to create a 'net new Azure' approach, and that this environment triggered a review of VAST within Manish Sah's organization.

- Jason Vallery stated that Manish Sah is running a project called Bifrost with roughly 30 developers to address performance and other issues across the stack (including a new client driver), and that Bifrost is being pitched to MAI as the solution to their problems.

- Jason Vallery stated he met the manager of the Bifrost team for coffee and that person characterized Bifrost as 'lipstick on a pig' (a negative internal assessment).

- Jason Vallery stated that an internal Microsoft HPC AI team (not the storage team) provided him internal Azure Storage and Bifrost specifications, and Jason was careful to frame that the information came to him in his post-Microsoft role to avoid legal exposure for VAST.

- Jason Vallery stated he created a PowerPoint comparing VAST versus the Bifrost solution and that this comparison angered Manish Sah because it made Bifrost look inefficient in power and space relative to VAST.

- Jason Vallery stated that a specific person in Niti's organization named 'Bolol' nearly got fired after Lior Genzel raised the issue in a meeting with a person named 'Garish' (both names uncertain from transcript).

- Jason Vallery stated that Vamsi (last name not provided) was upset that VAST did not clearly explain the agenda for being in Redmond and who VAST was meeting with, and Jason offered to include Vamsi in meetings.

- Jonsi Stephenson proposed a 'better together' approach with Microsoft where VAST invests engineering effort into deep integration with Azure Blob, positioning VAST as the high-performance filer and GPU-adjacent storage while Azure Blob remains the object store, enabling a global namespace spanning Azure, Nebius, Nscale, and other GPU cloud providers.

- Jason Vallery described an AI infrastructure pattern: central data lakes (Spark, Azure Databricks, custom apps) in large CPU-heavy regions, plus a global disaggregated fleet of GPUs (Azure, neo-clouds, on-prem) with GPU-adjacent storage for staging and checkpoints.



---

*Source: [[Jonsi:Jason 1-1 ]]*