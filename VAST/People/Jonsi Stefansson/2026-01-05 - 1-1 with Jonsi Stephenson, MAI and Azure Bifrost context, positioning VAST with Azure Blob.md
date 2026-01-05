---
type: "people"
title: "1:1 with Jonsi Stephenson, MAI and Azure Bifrost context, positioning VAST with Azure Blob"
date: "2026-01-05"
person: ""
participants: ["Jonsi Stefanson", "Jason Vallery"]
source: "transcript"
source_ref: "/Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/Jonsi:Jason 1-1 .md"
tags:
  - "type/people"
  - "person/"
  - "generated"

---

# 1:1 with Jonsi Stephenson, MAI and Azure Bifrost context, positioning VAST with Azure Blob

**Date**: 2026-01-05
**With**: Jonsi Stefanson, Jason Vallery

## Summary

Jason Vallery debriefed Jonsi Stephenson on Microsoft MAI, Azure internal politics around the Bifrost project, and why Microsoft stakeholders are upset about a VAST vs Bifrost comparison. Jonsi and Jason aligned on a potential "better together" positioning where VAST provides high-performance file and GPU-adjacent storage while Azure Blob remains the object store and global namespace integration target.


## Action Items


- [?] Brief Jonsi Stephenson before his Microsoft meetings (including likely pushback topics from Manish Sah's organization) and align on messaging that the Bifrost comparison was produced in Jason Vallery's VAST role in response to MAI requests. @Myself 📅 2026-01-06 ⏫ #task #proposed #auto

- [?] Verify identities and correct names for: Kushal (MAI-Azure relationship owner), "Niti" (HPC AI org reference), "Garish" (Microsoft contact), and "Bolol" (person nearly fired) to ensure accurate stakeholder mapping and follow-up. @Myself 📅 2026-01-10 #task #proposed #auto




## Decisions


- Position VAST Data to Microsoft MAI and Azure as a "better together" solution where Azure Blob remains the object store and VAST provides high-performance file and GPU-adjacent storage, enabled by deeper Azure Blob integration and a global namespace approach.




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

*Source: [[Jonsi:Jason 1-1 ]]*