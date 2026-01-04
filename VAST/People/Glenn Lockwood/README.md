---
type: people
title: Glenn Lockwood
created: '2026-01-03'
last_contact: '2025-11-07'
auto_created: true
tags:
- type/people
- needs-review
- company/openai
---

# Glenn Lockwood

## Contact Information

| Field | Value |
|-------|-------|
| **Role** | Principal Engineer |
| **Company** | VAST Data |
| **Department** | _Unknown_ |
| **Email** | _Unknown_ |
| **Phone** | _Unknown_ |
| **LinkedIn** | _Unknown_ |
| **Location** | San Francisco Bay Area |

## Relationship

_How do you work with this person? What is your dynamic?_

## Background

Glenn Lockwood has extensive experience in high-performance computing (HPC) and AI infrastructure. He served as a Principal Engineer at Microsoft, focusing on supporting large-scale AI supercomputers, including those used by OpenAI. Prior to Microsoft, he was a Storage Architect at Berkeley Lab, where he led the design of large-scale storage systems. He holds a Ph.D. in Materials Science from Rutgers University.


## Projects

_What projects are you collaborating on with this person?_

```dataview
LIST
FROM "VAST/Projects" OR "Personal/Projects"
WHERE contains(file.outlinks, this.file.link)
```


## Open Tasks

```dataview
TASK
FROM ""
WHERE !completed AND contains(text, "Glenn Lockwood")
SORT due ASC
```


## Tasks They Own

_Action items this person is responsible for:_

```dataview
TASK
WHERE contains(text, "@GlennLockwood") AND !completed
SORT due ASC
```

## Key Facts

- John owns alliances/partnerships for conventional channels (incl. AMD/NVIDIA) and control-plane partner ecosystem for Tier-2 cloud-in-a-box.
- Morty owns Neo cloud feature requirements; moving to Jason’s team but must keep Neo focus.
- Customer Success under Rob is effectively reactive support, not proactive CS.
- SE org is critical to Jason’s success; Hari called out as a top SE.
- China posture agreed: software-only sales outpost; avoid CAPEX/headcount build-out.
- Need a crisp, quantified Azure Storage gaps narrative ('dagger' slide) and a repeatable measurement rubric across clouds.
- Win/loss analysis should be routine and tied to Sales Ops; cloud is a platform, product gaps apply across deployment environments.
- Confluence is the engineering-respected source of truth for FRDs/requirements; coordinate taxonomy with Alon (A.L.) and Tomer.
- Kurt is global pre-sales lead for AI Infra under Zia; his team scores constrained GPU allocations and must approve any allocation of constrained SKUs.
- Kurt’s proposal: GA Azure Extended Zones as network-only plus AKS NodeJoin (ACAS FlexNode) to connect neo/sovereign cloud training sites to Azure for global inference.


- Jason Vallery reports to Jeff Denworth; charter is making VAST successful on hyperscalers and marketplaces.
- Jason Vallery is ex-Microsoft Azure Storage GPM (object storage/AI storage) and was OpenAI’s primary storage relationship owner starting in 2018.
- Rob Benoit leads the global pre-sales SE org; 18 years at NetApp; strong networking/sysadmin background.
- VAST cloud deployment is complex; marketplace should expose tenant outcomes rather than cluster administration.
- Cloud VM economics are poor for VAST at scale; preferred approach is object storage for capacity tier plus bare metal for performance.
- GCP Z3 helps but becomes expensive at larger sizes; bare metal instances are preferred.
- VAST DataSpaces/global namespace is a major differentiator for hybrid/multi-cloud AI data mobility.
- OpenAI pattern: central CPU-adjacent data lake plus GPU-adjacent working set caches across many regions/clouds.
- Field enablement/content ownership is fragmented with duplicative Confluence docs and unclear owners.
- SE bandwidth is constrained by installs (rack/stack ~2 weeks); a new partner program was created to offload rack-and-stack but cabling errors can cause multi-day delays.
## Topics Discussed

Org chart and key leaders across marketing, alliances, SE, sales, finance, Multi-cloud strategy mandate (Azure/AWS/GCP/Oracle) and complement vs compete framing, Cloud packaging and serverless/pipelines gaps, Neo cloud requirements ownership and team transition, Customer Success vs support operating model, SE engagement strategy and Tech Summit embedding, China go-to-market posture (software-only), Azure Storage limitations and messaging for Microsoft, Google RFP triage and no-bid criteria for block/latency-heavy asks, Confluence as FRD system of record and documentation taxonomy, Win/loss cadence and product MBR rhythm, Azure GTM path for VAST storage (BizDev-led engagement), VAST density/power advantages vs Azure Blob and Marketplace L-series limitations, OEM/ODM hardware path into Azure data centers and Apollo decision-making, Azure Extended Zones (network-only) and AKS NodeJoin (ACAS FlexNode) GA proposal


VAST-in-cloud strategy and cloud economics, Marketplace packaging (tenant outcomes vs cluster admin), Bare metal instances vs cloud VMs, Object storage capacity tiering, DataSpaces/global namespace for hybrid/multi-cloud AI, OpenAI reference architecture patterns, Field enablement and solution content ownership, SE org maturity and enterprise selling gaps, Install/rack-and-stack burden and partner program, Networking complexity requirements for deployments, Tech Summit follow-up
## Recent Context

- 2025-11-07: [[2025-11-07 - Reviewed org landscape and key players; aligned that Jason will deeply understan]] - Weekly 1:1 between Jason Vallery and Jeff Denworth reviewing VAST’s org landscape and key players, a... (via Jeff Denworth)
- 2025-11-07: [[2025-11-07 - Working session to brute-force warm paths into priority model builders using Lin]] - Working session for the Model Builder Turbine project to map warm introduction paths into priority m... (via Model Builder Turbine)
- 2025-11-06: [[2025-11-06 - Aaron walked through updated slides for next week’s SE conference covering two p]] - Review of updated AI pipeline slides for an upcoming VAST SE Tech Summit, covering model training (c... (via AI Pipelines Collateral)
- 2025-10-31: [[2025-10-31 - Jason (now at VAST) and Kushal discussed deploying VAST for Apollo’s training wo]] - 1:1 between Jason Vallery (VAST Data) and Kushal Datta (Microsoft Apollo) to evaluate deploying VAST... (via Kushal Datta)
- 2025-10-28: [[2025-10-28 - Introductory 1-1 covering backgrounds, finance org context, and cloud solutions]] - Introductory 1:1 between Jason Vallery and Timo Pervane focused on finance org context, Cloud Soluti... (via Timo Pervane)
- 2025-10-27: [[2025-10-27 - Jason and Kurt aligned on a go-to-market path to bring VAST’s high-density, lowe]] - Weekly 1:1 where Jason Vallery and Kurt Niebuhr aligned on a Microsoft Azure go-to-market path for V... (via Kurt Niebuhr)


- 2025-10-31: [[2025-10-31 - Intro discussion covering VAST-in-cloud strategy, field enablement gaps, and SE]] - Weekly 1:1 between Jason Vallery and Rob Benoit to align on VAST’s cloud strategy, marketplace packa... (via Rob Banga)
## Profile

**Role**: OpenAI
**Relationship**: External connector

**Background**:
- Potential connector into Thinking Machines; has relationship with Christian Gibson; previously provided a summary doc of a meeting with an engineer contact.
- Asked to validate engineering reality of KV cache depiction (current NFS; future GPU-direct-to-object).
- Previously worked closely with Jason at OpenAI; left in July and joined VAST (per transcript).

## Key Decisions

- ✅ Carl to move to ProServe under Rob.
- ✅ FRDs and detailed customer requirements will be authored/maintained in Confluence.
- ✅ Jason will own multi-cloud strategy end-to-end and catalog in-flight opportunities from a product requirements lens.
- ✅ Establish a monthly touchpoint between Jason and Brandon.
- ✅ Pursue a BizDev-led path (Joe Vane/Harish) to secure executive sponsorship (John Tinter) and engage Ronnie Booker’s org, rather than focusing on Nidhi/Manish.
- ✅ Treat the Azure Marketplace VM-based VAST offer as a checkbox while pushing a hardware/OEM storage-dense path for real density wins.
- ✅ Use fine-tuning/reinforcement learning phrasing in the training loop (with online RL as a continuous-loop concept).
- ✅ Represent embeddings as precomputed in the vectorization phase (not inline during inference).
- ✅ Add Database to data preparation and logging/archives in the diagrams (and optionally for KV cache metadata).
- ✅ Show current KV cache access via NFS in inference depictions; GPU-direct-to-object is a future option.

## Related Customers

- [[VAST Data]]
- [[OpenAI]]

## Related Projects

- [[AI Pipelines Collateral]]
- [[Model Builder Turbine]]
- [[Cloud]]

## Related




---
*Last updated: *