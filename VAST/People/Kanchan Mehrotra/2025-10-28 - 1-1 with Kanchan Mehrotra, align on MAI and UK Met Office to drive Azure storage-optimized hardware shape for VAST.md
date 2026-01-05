---
type: "people"
title: "1:1 with Kanchan Mehrotra, align on MAI and UK Met Office to drive Azure storage-optimized hardware shape for VAST"
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

# 1:1 with Kanchan Mehrotra, align on MAI and UK Met Office to drive Azure storage-optimized hardware shape for VAST

**Date**: 2025-10-28
**With**: Jason Vallery, Kanchan Mehrotra

## Summary

Jason Vallery and Kanchan Mehrotra aligned to prioritize Microsoft AI Infrastructure (MAI) and the UK Met Office as flagship customer pulls to justify an Azure hardware shape that makes VAST economics and networking viable. They agreed on a dual-track plan, advance marketplace listing work while escalating with marquee customers, and Jason will build an economics comparison deck and engage Igal Figlin’s team on LSv5 shape and networking requirements.


## Action Items


- [?] Meet with MAI contact Kushal to gather MAI requirements, deployment constraints, and next steps for VAST on Azure, then report outcomes back to Kanchan Mehrotra. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Connect with Vipin Sachdeva to re-open the MAI conversation and align with Kushal on MAI’s needs for VAST on Azure. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Build an internal NDA-shareable economics deck comparing 1 EB deployments across VAST on Azure LSv4, VAST on Azure LSv5, VAST on-prem, and Azure Blob Storage (HDD and Flash), including $/performance and rack and power implications. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Share MAI meeting notes with Kanchan Mehrotra and propose a joint support and escalation plan for MAI and UK Met Office. @Myself 📅 2025-11-08 #task #proposed #auto

- [?] Engage Igal Figlin to discuss LSv5 hardware shape, networking requirements, and a customer-driven pipeline anchored by MAI and UK Met Office. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Meet UK Met Office leaders (Mike Kiernan, Nico, and Alan) at Supercomputing to advance the VAST approach and validate constraints, especially networking and price-performance targets. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Coordinate Supercomputing and Ignite joint story, including panel participation, booth content, and keynote slide alignment with Kanchan Mehrotra, Lior Genzel, and Andrew Stack. @Myself 📅 2025-11-08 #task #proposed #auto

- [?] Set up a session with Nidhi to review the MAI and UK Met Office case, including the economics deck, and align internal stakeholders on priority and next steps (post-Supercomputing if needed). @Kanchan Mehrotra 📅 2025-11-08 #task #proposed #auto

- [?] Confirm whether Suresh will attend Supercomputing and, if yes, schedule a discussion on Neo cloud GPU-adjacent storage scenarios with Suresh and Anand. @Kanchan Mehrotra 📅 2025-11-08 🔽 #task #proposed #auto

- [?] Advance the Azure marketplace offer with Yancey’s team, including control plane integration, listing readiness, and billing model alignment. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Sync with Kanchan Mehrotra the week after the MAI Friday call to decide the support plan and escalation path for MAI and UK Met Office. @Myself 📅 2025-11-08 #task #proposed #auto

- [?] Check with Lior Genzel on outcomes and asks from Lior’s dinner with Igal Figlin, then capture and circulate any follow-ups needed for LSv5 shape and networking. @Myself 📅 2025-11-08 🔽 #task #proposed #auto

- [?] Confirm Wave’s current GPU status and determine whether a VAST proposal is viable on Azure given current LSv4 constraints, or whether to steer Wave to alternate paths. @Kanchan Mehrotra 📅 2025-11-08 🔽 #task #proposed #auto

- [?] Validate UK Met Office networking constraints against planned Azure LSv5 networking capabilities with Igal Figlin’s team and document gaps and required changes. @Kanchan Mehrotra 📅 2025-11-08 #task #proposed #auto




## Decisions


- Prioritize Microsoft AI Infrastructure (MAI) and the UK Met Office as near-term anchor wins to drive an Azure hardware shape suitable for VAST, rather than pursuing a broad Azure sales motion immediately.

- Run a dual-track plan: advance the Azure marketplace listing work while simultaneously pursuing flagship customer escalations (MAI and UK Met Office) to create internal pull for improved Azure storage-optimized hardware shapes.

- Engage Nidhi to re-energize internal advocacy only after the marketplace offer and the customer story (including economics) are ready to present.




## Key Information


- Kanchan Mehrotra is shifting focus to work more on OpenAI and Microsoft AI Infrastructure (MAI) engagements, including technical problem-solving and operationalizing third-party GPU capacity inside Azure.

- GPU supply constraints, not demand, are limiting Microsoft’s ability to allocate third-party GPU capacity to customers, slowing new large third-party GPU deals despite continued high demand.

- VAST’s current hyperscaler go-to-market constraint is reliance on compute SKUs with local NVMe (for example Azure L-series), where the compute-to-storage ratio makes VAST deployments financially non-viable at exabyte scale.

- Azure LSv4 is the only current Azure option for VAST’s NVMe-based deployment approach, but it has poor economics and networking characteristics for scale, including too many CPU cores per storage, weak networking, and low drive density.

- LSv5 is planned and committed by Igal Figlin’s team, but it is far out and may still be bandwidth-limited for UK Met Office requirements.

- VAST claims an exabyte-scale deployment can be delivered with approximately 20 VAST racks versus approximately 240 racks of Azure Blob Storage for the same logical capacity, implying about 10x higher rack density for VAST.

- VAST claims power consumption for exabyte-scale storage in MAI Falcon-type clusters can be approximately one-fifth compared to alternatives, driven by higher density and fewer racks.

- Azure Storage is unlikely to champion VAST internally, so progress requires support via Igal Figlin’s team and customer-driven escalations from marquee lighthouse accounts.

- Target lighthouse customers identified for driving Azure hardware shape changes are Microsoft AI Infrastructure (MAI) and the UK Met Office, with existing MAI relationships including Kushal and Vipin Sachdeva.

- MAI already has CoreWeave capacity available, and VAST capacity exists in CoreWeave, while MAI interest in running VAST on Azure remains active.

- Marketplace control plane work from Yancey’s team is being integrated, with Google marketplace first and Azure marketplace targeted around February (year not specified).

- Neo cloud GPU-adjacent storage was identified as an opportunity to keep GPUs productive during network disconnects by targeting a GPU-to-local-storage ratio and deploying storage adjacent to GPU capacity.

- VAST has a high-performance KV-store called Undivided Attention positioned for long-term memory use cases, and Microsoft previously declined to build a similar capability.



---

*Source: [[2025-10-28 - Jason and Kanchan aligned to pursue MAI and UK Met Office as flagship wins to un]]*