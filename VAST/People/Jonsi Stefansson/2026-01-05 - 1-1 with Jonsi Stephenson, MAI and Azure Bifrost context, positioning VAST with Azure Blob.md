---
type: people
title: 1:1 with Jonsi Stephenson, MAI and Azure Bifrost context, positioning VAST with Azure Blob
date: '2026-01-05'
person: Jonsi Stefansson
participants:
- Jonsi Stefanson
- Jason Vallery
- Jonsi Stephenson
source: transcript
source_ref: /Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/Jonsi:Jason 1-1 .md
tags:
- type/people
- generated
---

# 1:1 with Jonsi Stephenson, MAI and Azure Bifrost context, positioning VAST with Azure Blob

**Date**: 2026-01-05
**With**: Jonsi Stefanson, Jason Vallery

## Summary

Jason Vallery debriefed Jonsi Stephenson on Microsoft MAI and Azure internal politics driving scrutiny of VAST, including Manish Sah's Bifrost initiative and sensitivity around internal specs being compared to VAST. Jonsi and Jason aligned on a potential 'better together' story where VAST focuses on high-performance file and GPU-adjacent storage while integrating tightly with Azure Blob for object storage and global namespace needs across Azure and external GPU clouds.

## Action Items

- [?] Brief Jonsi Stephenson before his Microsoft meetings (including likely pushback topics from Manish Sah's organization) and align on messaging that the Bifrost comparison was produced in Jason Vallery's VAST role in response to MAI requests. @Myself 📅 2026-01-06 ⏫ #task #proposed #auto

- [?] Verify identities and correct names for: Kushal (MAI-Azure relationship owner), "Niti" (HPC AI org reference), "Garish" (Microsoft contact), and "Bolol" (person nearly fired) to ensure accurate stakeholder mapping and follow-up. @Myself 📅 2026-01-10 #task #proposed #auto

- [?] Brief Jonsi Stephenson before his Microsoft 1:1 meetings (including likely pushback from Manish Sah's organization and how to frame the VAST vs Bifrost comparison and Azure Blob integration narrative). @Myself 📅 2026-01-06 ⏫ #task #proposed #auto

## Decisions

- Position VAST Data to Microsoft MAI and Azure as a "better together" solution where Azure Blob remains the object store and VAST provides high-performance file and GPU-adjacent storage, enabled by deeper Azure Blob integration and a global namespace approach.

- Jonsi Stephenson will proceed with scheduled 1:1 meetings now that the temporary restraining order is lifted.

- Jason Vallery and Jonsi Stephenson will position a potential Microsoft partnership narrative around tighter VAST integration with Azure Blob, with VAST focusing on high-performance file and GPU-adjacent storage rather than being the primary object store.

## Key Information

- Jonsi Stephenson said a temporary restraining order that prevented him from taking meetings has ended, and he can now take 1:1 meetings again.

- Jonsi Stephenson said the remaining legal case is now primarily focused on a solicitation allegation, and he believes his contract has no consequences related to that allegation.

- Jason Vallery stated that Microsoft MAI preferred VAST Data and had used VAST prior to Microsoft acquiring Inflection AI, and that MAI and Azure are distinct internal organizations with a relationship owner on the MAI side.

- Jason Vallery stated that a key MAI stakeholder named Kushal (last name unclear in transcript) owns the relationship between Microsoft AI (MAI) and Azure, and that Kushal contacted Jason after Jason left Microsoft to ask what an MAI deployment on VAST would look like.

- Jason Vallery stated that after Microsoft acquired Inflection AI, Microsoft pushed Inflection to run on Azure under an "eat our own dog food" principle, and Inflection's first Azure supercomputer (July, year not specified) had major issues across storage, Kubernetes, control plane, reliability, and networking.

- Jason Vallery stated that the Azure issues triggered an escalation by Mustafa Suleyman (head of Microsoft AI) and led to a project called Apollo to create a "net new Azure" approach.

- Jason Vallery stated that Manish Sah's organization initiated a review of VAST Data capabilities (logging, monitoring, manageability, performance, and scale) to understand why MAI preferred VAST.

- Jason Vallery stated that Manish Sah is running a project called Bifrost, staffed with roughly 30+ developers, intended to address performance and other issues across the Azure stack (including a new says client driver) and pitched to MAI as a comprehensive solution.

- Jason Vallery stated he had coffee with the person managing the Bifrost team, who described Bifrost as "lipstick on a pig" (a superficial fix rather than a fundamental redesign).

- Jason Vallery stated he spoke with Microsoft's HPC AI team (formerly led by Niti, exact identity unclear) and received internal Azure Storage and Bifrost specifications, and he was careful to document that the request came to him after he joined VAST Data due to concerns about Microsoft alleging misuse of internal information.

- Jason Vallery stated that a specific person in the Microsoft HPC AI organization (name unclear in transcript, possibly "Bolol") nearly got fired after the internal information flow was raised in a meeting, and that Lior Genzel raised it with a Microsoft contact named Garish (identity unclear).

- Jason Vallery stated he created a PowerPoint comparing VAST Data versus the Microsoft Bifrost solution and that this made Manish Sah angry because it portrayed Bifrost negatively and highlighted internal details.

- Jason Vallery stated that during a Redmond visit he met multiple people in Manish Sah's organization for informal catch-ups, and that Vamsi (likely a Microsoft contact, identity unclear) was upset because VAST did not clearly communicate the purpose of the trip, the agenda, or who VAST was meeting with.

- Jonsi Stephenson proposed a "better together" approach where VAST Data invests engineering effort to integrate tightly with Azure Blob so Azure Blob remains the object store while VAST provides a high-performance file system and GPU-adjacent storage, enabling a global namespace spanning Azure, Nebius, Nscale, and other GPU cloud providers.

- Jason Vallery described an AI infrastructure pattern: centralized data lakes (Spark and Azure Databricks in large Azure regions on CPU) plus a disaggregated fleet of GPUs (in Azure, neo-clouds, or on-prem) with GPU-adjacent storage for staging and checkpoints.

---

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
