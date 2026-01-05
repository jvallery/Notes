---
type: "people"
title: "1:1 with Kanchan Mehrotra (Koncha), align on MAI and UK Met Office to drive Azure hardware shape for VAST"
date: "2025-10-28"
person: ""
participants: ["Jason Vallery", "Kanchan Mehrotra"]
source: "transcript"
source_ref: "/Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-10-28 - Jason and Koncha aligned on using MAI and UK Met Office as marquee wins to push.md"
tags:
  - "type/people"
  - "person/"
  - "generated"

---

# 1:1 with Kanchan Mehrotra (Koncha), align on MAI and UK Met Office to drive Azure hardware shape for VAST

**Date**: 2025-10-28
**With**: Jason Vallery, Kanchan Mehrotra

## Summary

Jason Vallery and Kanchan Mehrotra aligned to use Microsoft AI Infrastructure (MAI) and the UK Met Office as marquee wins to create executive pull for an Azure hardware shape that is economically viable for VAST. They agreed to run a dual track, keep the Azure Marketplace offer moving while escalating the need for better VM shapes and networking, and coordinate Supercomputing touchpoints and messaging.


## Action Items


- [?] Meet Kushal (MAI) on Friday to discuss VAST opportunities and clarify the meaning of the MAI hint that capacity is "not really Azure". @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Reconnect with Vipin Sachdeva (MAI) to re-engage VAST with MAI stakeholders and champions. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Build an internal comparative economics deck for a 1 EB deployment comparing VAST on Azure LSv4, Azure LSv5, and on-prem versus Azure Blob (HDD and Flash) to support the Azure hardware shape ask. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Coordinate a review meeting with Nidhi to walk through the comparative deck and align on the MAI plus UK Met Office plan. @Kanchan Mehrotra 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Meet UK Met Office stakeholders (Mike Kiernan, Nico, Allen) at Supercomputing to push the VAST path and surface Azure LSv5 networking needs. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Speak with Egal to push on Azure LSv5 VM shape and networking and bandwidth requirements and align on non-committal timeline expectations. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Align the joint VAST-Azure story for Supercomputing and Ignite (booths and panel narrative) with Andrew, Joe Green, and Lior. @Kanchan Mehrotra 📅 2025-11-08 #task #proposed #auto

- [?] Check whether Suresh will attend Supercomputing and, if yes, set up a Neo cloud GPU-adjacent storage discussion with Jason Vallery; if not attending, schedule the discussion for a later date. @Kanchan Mehrotra 📅 2025-11-08 #task #proposed #auto

- [?] Provide input and content for Egal’s keynote slide that references VAST. @Myself 📅 2025-11-08 #task #proposed #auto

- [?] Progress the Azure Marketplace offer (initially LSv4-based), track ETA, and prepare to brief sellers once the offer is credible and aligned with a viable SKU path. @TBD 📅 2025-11-08 #task #proposed #auto

- [?] After the Friday MAI meeting, clarify MAI’s incremental opportunity and where capacity will be delivered (Azure vs non-Azure) and share the findings with stakeholders. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Validate Neo cloud GPU-adjacent storage ratio guidance with Suresh and Anand and explore Microsoft usage models (lease vs first-party deployment vs Azure-sold) that could enable VAST. @Kanchan Mehrotra 📅 2025-11-08 #task #proposed #auto

- [?] Keep Kurt informed so sellers remember VAST when qualifying third-party GPU deals that need GPU-adjacent storage. @Myself 📅 2025-11-08 🔽 #task #proposed #auto

- [?] Track Wave’s 40 PB request and assess whether there is a viable Azure configuration with current SKUs or whether alternatives are required, then report back with a recommendation. @Myself 📅 2025-11-08 #task #proposed #auto

- [?] Confirm Nidhi’s Ignite and Supercomputing schedule and lock a time for Nidhi to review the comparative economics deck and align on the MAI plus UK Met Office approach. @Kanchan Mehrotra 📅 2025-11-08 #task #proposed #auto




## Decisions


- Prioritize Microsoft AI Infrastructure (MAI) and the UK Met Office as flagship wins to create executive pull for an Azure hardware shape and networking profile that is economically viable for VAST.

- Run a dual track: continue shipping Azure Marketplace offers while simultaneously driving a leadership-backed path to improved Azure VM shapes and networking for VAST.

- Defer broad seller-led sales pushes for VAST on Azure until there is a credible Azure product and SKU path that meets customer economics.




## Key Information


- Kanchan Mehrotra is starting to work more on Microsoft AI Infrastructure (MAI) and OpenAI-related engagements, including technical-side support and follow-through on third-party GPU (3P GPU) deals in Azure.

- Microsoft has high demand for third-party GPU (3P GPU) capacity, but near-term deal execution is constrained primarily by supply, not demand.

- Jason Vallery’s cloud strategy constraint for VAST on Azure is that current L-series VM shapes with local NVMe create an unfavorable compute-to-storage ratio, making exabyte-scale deployments economically and physically impractical.

- VAST can deliver approximately 1 EB of storage in about 20 racks versus approximately 240 racks for Azure Blob storage, implying roughly 10x rack density advantage for VAST in comparable logical capacity scenarios.

- Azure LSv4 is described as a poor fit for VAST due to too many CPU cores, weak networking, and low NVMe density, leading to poor cost-performance and customer sticker shock.

- Azure LSv5 is described as committed by Egal’s team but expected to be roughly a year or more out, and networking plans may still be insufficient for UK Met Office price-performance targets.

- MAI has existing affinity for VAST, with champions including Kushal and Vipin Sachdeva.

- Azure NetApp Files is considered a viable prior-art pattern for bringing partner hardware into Azure, and could be a model for VAST via OEM/ODM-qualified hardware.

- Marketplace control plane from Yancey’s team was acquired by VAST, with Google first and Azure expected to follow later, tracked internally as early next year.



---

*Source: [[2025-10-28 - Jason and Koncha aligned on using MAI and UK Met Office as marquee wins to push]]*