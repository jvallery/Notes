---
type: "people"
title: "1:1 with Rob Banga: VAST-in-cloud strategy, marketplace outcomes, and SE enablement gaps"
date: "2025-10-31"
person: ""
participants: ["Jason Vallery", "Rob Banga"]
source: "transcript"
source_ref: "/Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-10-31 - Intro discussion covering VAST-in-cloud strategy, field enablement gaps, and SE.md"
tags:
  - "type/people"
  - "person/"
  - "generated"

---

# 1:1 with Rob Banga: VAST-in-cloud strategy, marketplace outcomes, and SE enablement gaps

**Date**: 2025-10-31
**With**: Jason Vallery, Rob Banga

## Summary

Jason Vallery and Rob Banga aligned that VAST cloud success requires an object storage capacity tier plus bare metal for performance economics, and that DataSpaces and the global namespace are key differentiators for hybrid and multi-cloud AI data mobility. They also surfaced field enablement and documentation ownership gaps, plus SE bandwidth constraints driven by rack-and-stack installs and high networking complexity. They agreed to meet at Tech Summit and keep a two-way feedback loop between field pain points and the cloud roadmap.


## Action Items


- [?] Schedule coffee with Rob Banga during Tech Summit and send calendar details (time and location). @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Share initial VAST Data cloud roadmap context with SE leadership to establish a feedback loop between field pain points and cloud roadmap priorities. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Provide a consolidated list of field pain points for current VAST Data product usage in cloud and hyperscaler environments (including marketplace and bare metal needs). @Rob Banga 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Loop in Yancey (last name not stated) and relevant owners on marketplace and bare-metal plans as needed after Tech Summit alignment. @Myself 📅 2025-11-08 🔽 #task #proposed #auto




## Decisions


- Jason Vallery and Rob Banga decided to meet in person at Tech Summit for a follow-up conversation to go deeper on cloud strategy and SE field needs.




## Key Information


- Jason Vallery reports to Jeff Denworth and his charter is to make VAST Data successful on hyperscalers and cloud marketplaces, including evolving the product for frontier AI scenarios (for example OpenAI and Microsoft AI Infrastructure).

- Jason Vallery previously worked at Microsoft in Azure Storage, focused on object storage APIs/SDKs and later as a Group Product Manager owning much of the object storage platform with an AI storage focus.

- Jason Vallery was the primary storage relationship owner for OpenAI starting in 2018 and learned OpenAI's patterns for capacity management and dataset organization at very large scale.

- Rob Banga leads the global pre-sales SE organization at VAST Data and had been at VAST Data for about nine months as of Friday, 2025-10-31.

- Rob Banga spent 18 years at NetApp and previously ran technology enablement (go-to-market enablement, labs, POC environments, field CTOs, solution architects) and earlier ran the Americas SE organization.

- Rob Banga has a systems administration and networking background, including Cisco and Unix engineering roles at financial services companies (including Goldman Sachs), before moving into storage and then NetApp.

- Rob Banga partnered closely with Yancey (last name not stated) at NetApp on go-to-market for NetApp cloud business, including marketplace offerings across Azure, AWS, and Google, and first-party services such as Azure NetApp Files and AWS FSx for ONTAP.

- VAST Data cloud deployment is complex compared to single-image marketplace products (for example ONTAP), so marketplace offers should focus on tenant outcomes rather than requiring customers to administer VAST clusters.

- Cloud VM economics are poor for VAST Data at large scale, so the preferred approach is object storage for the capacity tier plus bare metal instances for performance; GCP Z3 helps but becomes expensive at scale.

- VAST Data's DataSpaces and global namespace are viewed as major differentiators for hybrid and multi-cloud AI data mobility patterns.

- OpenAI's data pattern described was a central CPU-adjacent data lake plus a GPU-adjacent working set cache distributed across many regions and clouds.

- Field enablement and solution content ownership for VAST Data is fragmented, with duplicative Confluence documentation and unclear owners, creating inconsistency and delays.

- SE bandwidth is constrained by onsite installs (rack-and-stack taking about two weeks), reducing time available for selling and prospecting; a new partner program was created to offload rack-and-stack but cabling errors can cause multi-day delays.

- High networking skills are required across the SE organization, including 400G networking, leaf-spine architectures, VXLAN, and BGP.

- Tech Summit was approved for about 200 attendees with a little over $500k cost, and Renan (last name not stated) supports investment in the SE organization.

- Carl Rounds (last name inferred from transcript as 'Carl Rounds') worked with Rob Banga at NetApp and later worked at Microsoft; Jason Vallery has worked with Carl Rounds for most of his time in Azure Storage and spoke with him on 2025-10-31.



---

*Source: [[2025-10-31 - Intro discussion covering VAST-in-cloud strategy, field enablement gaps, and SE]]*