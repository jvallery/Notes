---
type: "people"
title: "1:1 with Kanchan Mehrotra, align on MAI and UK Met Office to drive better Azure storage VM shape for VAST"
date: "2025-10-28"
person: ""
participants: ["Jason Vallery", "Kanchan Mehrotra"]
source: "transcript"
source_ref: "/Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-10-28 - Jason and Kanchan aligned to pursue MAI and UK Met Office as flagship wins to un.md"
tags:
  - "type/people"
  - "person/"
  - "generated"

---

# 1:1 with Kanchan Mehrotra, align on MAI and UK Met Office to drive better Azure storage VM shape for VAST

**Date**: 2025-10-28
**With**: Jason Vallery, Kanchan Mehrotra

## Summary

Jason Vallery and Kanchan Mehrotra aligned to prioritize Microsoft AI Infrastructure (MAI) and the UK Met Office as flagship customer wins to create pull for an Azure hardware shape that makes VAST economics and networking viable. They agreed on a dual-track plan: progress Azure Marketplace readiness while escalating requirements with Igal Figlin's team and MAI stakeholders, and coordinate messaging at Supercomputing and a follow-on internal alignment session with Nidhi.


## Action Items


- [?] Meet with MAI stakeholder Kushal to gather requirements and next steps for deploying VAST in MAI contexts (Azure region vs Neo cloud). @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Connect with Vipin Sachdeva to re-open the MAI conversation and align with Kushal on MAI requirements and stakeholder alignment for VAST. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Build an internal NDA-shareable economics deck comparing 1 exabyte across VAST on Azure LSv4, Azure LSv5, on-prem, and Azure Blob Storage (HDD and Flash), including $/performance and scaling constraints. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Share MAI meeting notes with Kanchan Mehrotra and propose a joint plan for MAI and UK Met Office escalations and Azure hardware shape requirements. @Myself 📅 2025-11-08 #task #proposed #auto

- [?] Engage Igal Figlin to discuss LSv5 shape, networking needs, and a customer-driven pipeline anchored by MAI and the UK Met Office. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Meet UK Met Office leaders (Mike Kiernan, Nico, Alan) at Supercomputing to push the VAST approach and validate constraints and success criteria. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Coordinate Supercomputing and Ignite joint story and VAST booth content with Kanchan Mehrotra, Lior Genzel, and Andrew Stack, including panel participation and keynote slide alignment. @Myself 📅 2025-11-08 #task #proposed #auto

- [?] Set up a session with Nidhi to review the MAI and UK Met Office case and the economics deck, scheduled for Supercomputing week or immediately after Supercomputing if needed. @Kanchan Mehrotra 📅 2025-11-08 #task #proposed #auto

- [?] Confirm whether Suresh will attend Supercomputing and, if yes, schedule a discussion on Neo cloud GPU-adjacent storage scenarios and requirements. @Kanchan Mehrotra 📅 2025-11-08 🔽 #task #proposed #auto

- [?] Advance the Azure Marketplace offer with Yancey's team, including control plane integration, listing requirements, and billing readiness. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Sync with Kanchan Mehrotra the week after the MAI Friday call to decide the support plan and escalation path for MAI and UK Met Office. @Myself 📅 2025-11-08 #task #proposed #auto

- [?] Check with Lior Genzel on outcomes from his dinner with Igal Figlin and capture any asks or next steps relevant to LSv5 and networking requirements. @Myself 📅 2025-11-08 🔽 #task #proposed #auto

- [?] Confirm Wave's current GPU status and whether a VAST proposal is viable on Azure given current LSv4 constraints, or whether to steer to alternate paths. @Kanchan Mehrotra 📅 2025-11-08 🔽 #task #proposed #auto

- [?] Validate UK Met Office networking constraints versus planned LSv5 capabilities with Igal Figlin's team to determine feasibility and required shape changes. @Kanchan Mehrotra 📅 2025-11-08 #task #proposed #auto




## Decisions


- Prioritize Microsoft AI Infrastructure (MAI) and the UK Met Office as near-term anchor wins, rather than pursuing a broad Azure sales motion.

- Run a dual-track plan: advance Azure Marketplace readiness while driving flagship customer escalations to influence Azure hardware shape and networking requirements.

- Engage Nidhi to amplify internal advocacy after the Azure Marketplace offer and the MAI and UK Met Office story are ready.




## Key Information


- Kanchan Mehrotra is increasingly focused on Microsoft OpenAI engagement and Microsoft AI Infrastructure (MAI), including technical problem-solving and supporting 3P GPU customer deployments in Azure.

- Microsoft has strong demand for 3P GPU deals in Azure, but GPU supply constraints are limiting how much capacity can be allocated to 3P customers.

- For VAST deployments on Azure, the current viable compute option is Azure LSv4, but its economics and networking are not suitable for large-scale VAST storage deployments because it has too many CPU cores relative to storage, weak networking, and low drive density.

- LSv5 is planned and is described as committed by Igal Figlin's team, but it is far out and may still be bandwidth-limited for UK Met Office requirements.

- VAST claims that delivering approximately 1 exabyte of capacity can require about 20 VAST racks versus about 240 racks of Azure Blob Storage, implying roughly 10x rack density improvement for the same logical capacity.

- VAST claims power consumption for storage in MAI Falcon-type clusters can be approximately one-fifth compared to alternatives, driven by higher density and fewer racks.

- Azure Storage is unlikely to champion VAST as a partner; progress likely requires support via Igal Figlin's team and customer-driven pull from marquee lighthouse customers.

- MAI already has CoreWeave capacity available, and VAST capacity exists in CoreWeave, while MAI interest in VAST on Azure remains active.

- Marketplace control plane work (from Yancey's team) is being integrated; Google Marketplace is planned first, with Azure Marketplace targeted around February (year not specified).

- Neo cloud GPU-adjacent storage is viewed as an opportunity to keep GPUs productive during network disconnects by maintaining a GPU-to-local-storage ratio.

- VAST has a high-performance KV-store called Undivided Attention that is positioned as suitable for long-term memory use cases; Microsoft previously declined to build a similar KV-store internally.



---

*Source: [[2025-10-28 - Jason and Kanchan aligned to pursue MAI and UK Met Office as flagship wins to un]]*