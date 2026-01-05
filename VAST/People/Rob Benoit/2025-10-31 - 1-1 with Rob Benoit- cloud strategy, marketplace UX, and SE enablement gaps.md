---
type: "people"
title: "1:1 with Rob Benoit: cloud strategy, marketplace UX, and SE enablement gaps"
date: "2025-10-31"
person: ""
participants: ["Jason Vallery", "Rob Benoit", "Glenn Lockwood", "Carl Rounds"]
source: "transcript"
source_ref: "/Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-10-31 - Intro discussion covering VAST-in-cloud strategy, field enablement gaps, and SE.md"
tags:
  - "type/people"
  - "person/"
  - "generated"

---

# 1:1 with Rob Benoit: cloud strategy, marketplace UX, and SE enablement gaps

**Date**: 2025-10-31
**With**: Jason Vallery, Rob Benoit, Glenn Lockwood, Carl Rounds

## Summary

Jason Vallery and Rob Benoit aligned on a VAST-in-cloud approach that uses object storage for capacity economics and bare metal for performance, with DataSpaces/global namespace as a key differentiator for hybrid and multi-cloud AI. They also surfaced field enablement and SE bandwidth gaps, including fragmented content ownership and heavy install burden, and agreed to connect at Tech Summit to continue the feedback loop between field pain points and the cloud roadmap.


## Action Items


- [?] Schedule coffee with Rob Benoit during VAST Data Tech Summit. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Share initial VAST Data cloud roadmap context with VAST Data SE leadership. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Provide a consolidated list of field pain points for using VAST Data on hyperscalers and in cloud deployments, to feed into the cloud roadmap feedback loop. @Rob Benoit 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Confirm the time and location for the Tech Summit meeting with Rob Benoit. @Myself 📅 2025-11-08 🔽 #task #proposed #auto

- [?] Loop in Yancey (last name not provided) and relevant owners on marketplace offer plans and bare-metal instance strategy for hyperscalers, as needed. @Myself 📅 2025-11-08 🔽 #task #proposed #auto




## Decisions


- Jason Vallery and Rob Benoit decided to meet in person at VAST Data Tech Summit to continue the discussion and deepen alignment between cloud roadmap priorities and field SE pain points.




## Key Information


- Jason Vallery reports to Jeff Denworth and is chartered to make VAST Data successful on hyperscalers and cloud marketplaces, including evolving the product for frontier AI scenarios (for example OpenAI and Microsoft AI Infrastructure).

- Jason Vallery previously worked at Microsoft Azure Storage, focused on object storage APIs/SDKs and later led major parts of the object storage platform as a Group Product Manager with an AI storage focus.

- Jason Vallery became OpenAI's primary storage relationship owner starting in 2018 and supported OpenAI's growth on Azure to many exabytes, learning their capacity management and dataset organization patterns.

- Glenn Lockwood joined VAST Data in July 2025 and previously worked closely with Jason Vallery at Microsoft.

- Rob Benoit leads the global pre-sales Sales Engineering organization at VAST Data and had been at VAST Data for about nine months as of 2025-10-31.

- Rob Benoit spent 18 years at NetApp and previously ran technology enablement (go-to-market enablement, labs, POC environments, field CTOs, solution architects) and earlier ran the Americas SE organization.

- Rob Benoit has a systems administration and networking background, including Cisco and Unix engineering roles at financial services companies (including Goldman Sachs), before moving into storage and then NetApp.

- Rob Benoit partnered with Yancey (last name not provided) at NetApp on go-to-market for NetApp cloud business, including marketplace offerings and first-party hyperscaler services such as Azure NetApp Files and AWS FSx for ONTAP.

- Carl Rounds worked with Rob Benoit at NetApp for many years (including as solution specialists and field CTOs) and later moved to Microsoft; Jason Vallery worked with Carl Rounds for most of his time in Azure Storage, where Carl focused on partner and go-to-market work.

- VAST Data cloud deployment is complex compared to single-image marketplace products (for example a standalone ONTAP instance), and marketplace offers should focus on tenant outcomes rather than requiring customers to administer VAST clusters.

- For large-scale VAST-in-cloud deployments, cloud VM economics are poor; the preferred approach is object storage for the capacity tier and bare metal for performance, with GCP Z3 helping but becoming expensive at scale.

- VAST DataSpaces and the global namespace are a major differentiator for hybrid and multi-cloud AI data mobility patterns, including an OpenAI-style pattern of a central CPU-adjacent data lake plus GPU-adjacent working set caches across many regions and clouds.

- Field enablement and solution content ownership is fragmented at VAST Data, with duplicative Confluence documentation and unclear owners; many SEs are storage-centric and there are gaps in enterprise data, AI, and app/platform selling skills.

- SE bandwidth is constrained by onsite installs (rack-and-stack taking about two weeks), reducing selling time; a new partner program was created to offload rack-and-stack, but cabling errors can cause multi-day delays.

- High networking skills are required across the SE organization, including 400G networking, leaf-spine architectures, VXLAN, and BGP.

- Tech Summit was approved for approximately 200 attendees with a cost a little over $500k, and Renan (last name not provided) supports investment in SE.



---

*Source: [[2025-10-31 - Intro discussion covering VAST-in-cloud strategy, field enablement gaps, and SE]]*