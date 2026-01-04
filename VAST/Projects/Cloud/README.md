---
type: projects
title: Cloud
last_contact: unknown
created: '2026-01-03'
tags:
- type/projects
- generated
---

# Cloud

## Recent Context

- 2025-10-29: [[Sources/Transcripts/2025/2025-10-29 - Tackle and VAST kicked off onboarding to sell VAST’s SaaS via Google Cloud Marke.md|Tackle and VAST kicked off onboarding to sell VAST’s SaaS via Google Cloud Marke]] — Tackle and VAST kicked off onboarding to sell VAST’s SaaS via Google Cloud Marketplace using Tackle ...

- 2025-10-29: [[Sources/Transcripts/2025/2025-10-29 - Kickoff of VAST’s onboarding to Tackle to connect an existing GCP Marketplace li.md|Kickoff of VAST’s onboarding to Tackle to connect an existing GCP Marketplace li]] — Kickoff of VAST’s onboarding to Tackle to connect an existing GCP Marketplace listing and enable pri...

- unknown: [[Sources/Transcripts/2025/2025-10 - Cloud Marketplace MVP.md|Cloud Marketplace MVP]] — - [x] Define GA acceptance criteria for cloud MVP (spin up/down, DR/offload, etc.) and when to begin...

- 2025-11-03: [[Sources/Transcripts/2025/2025-11-03 - Team reviewed how cloud clusters must map to Salesforce assets (AccountSitePSN.md|Team reviewed how cloud clusters must map to Salesforce assets (AccountSitePSN]] — Team reviewed how cloud clusters must map to Salesforce assets (Account/Site/PSNT) to enable call-ho...

- 2025-10-28: [[Sources/Transcripts/2025/2025-10-28 - Cloud BU leadership aligned on a dual-track strategy (1) ship GCP MVP via marke.md|Cloud BU leadership aligned on a dual-track strategy (1) ship GCP MVP via marke]] — Cloud BU leadership aligned on a dual-track strategy: (1) ship GCP MVP via marketplace with strong c...

- 2025-10-30: [[Sources/Transcripts/2025/2025-10-30 - The group aligned on the cloud support operating model (Customer Success, Suppor.md|The group aligned on the cloud support operating model (Customer Success, Suppor]] — The group aligned on the cloud support operating model (Customer Success, Support, SRE), hyperscaler...

- unknown: [[Sources/Transcripts/2025/2025-10 - SaaS.md|SaaS]] — - [x] Draft cloud SaaS operating model requirements (DevOps/LifeSite rotations, telemetry, 24x7 supp...

- unknown: [[2025-10 - Google Tasks]] - A completed task to confirm Google Cloud Platform GA timing after a bottleneck fix and align the fir... (via Google)
- unknown: [[2025-10 - Asaf Levy]] - Completed action items from a working session with Asaf Levy to align on DataSpaces persistence desi... (via Asaf Levy)
- unknown: [[2025-11-4 - Planning sessions]] - Planning notes for a set of sessions with Jeff Denworth to align on VAST’s cloud-first product strat... (via Jeff Denworth)
- unknown: [[2025-10 - Jeff Denworth]] - Notes capturing planning topics with Jeff Denworth around travel, team reporting structure, cloud ac... (via Jeff Denworth)
- unknown: [[2025-10 - Lior Genzel]] - Note captures discussion points and completed follow-ups with Lior Genzel around Google TPU strategy... (via Lior Genzel)
- unknown: [[2025-10 - Shachar Feinblit]] - Checklist and Slack snippets related to coordinating with Shachar Feinblit, including setting up rec... (via Shachar Feinblit)
- unknown: [[_Open Topics]] - Open topics note for Shachar Feinblit, listing key internal Slack contacts by functional area (suppo... (via Shachar Feinblit)
- unknown: [[2025-10 - SaaS]] - A completed task to draft the operating model requirements for VAST Cloud SaaS, covering DevOps/Life...
- unknown: [[Available Capacity Calculations]] - Email-style note proposing replacing a fixed overhead percentage with a first-principles “available ...
- unknown: [[2025-10 - Cloud Marketplace MVP]] - Checklist of completed deliverables for a cloud marketplace MVP, including GA acceptance criteria, a...
- unknown: [[Pricing]] - Internal note to the Pricing v-team outlining principles and a recommended direction for VAST Cloud ... (via Pricing)
- unknown: [[2025-10 - Pricing Tasks]] - Checklist of completed pricing workstreams for cloud/private offers, discount policy, normalization ... (via Pricing)
- 2025-12-19: [[2025-12-19]] - Discussion between Jeff Denworth and Jason Vallery on VAST’s Microsoft/Azure strategy: what level of... (via Jeff Denworth)
- 2025-11-14: [[2025-11-14 - VAST’s cloud and federal teams aligned on responding to Google Distributed Cloud]] - VAST’s cloud and federal teams aligned on responding to Google Distributed Cloud’s RFP to replace Ne... (via Google)
- 2025-11-14: [[2025-11-14 - Internal sync to align on Walmart’s big data initiative, clarify requirements, a]] - Internal sync to align on Walmart’s big data initiative, focusing on clarifying disaster recovery re... (via Walmart)

## Key Facts

- Google Distributed Cloud has connected and air-gapped variants; NetApp is the incumbent storage partner.
- Google issued a US-based RFP to replace NetApp for GDC storage; VAST was invited to respond and is undergoing vendor due diligence.
- Google’s emphasis areas include air-gapped support, compliance/attestations (e.g., DISA STIG), ops model (updates, staffing, troubleshooting), multi-tenancy, quotas, encryption, and tags.
- Fort Meade "Gemini as a service" on-prem initiative is described as a Q4 commit and a near-term joint validation path.
- GDC deployments commonly run on Dell; HPE and Cisco are also in scope for hardware options.
- VAST recently launched Google Marketplace offers; broader partnership is still early.
- Resource risk: Greg may be heavily focused on Leidos next year, potentially impacting continuity.
- Google Z3 exists; Z4M is the next storage-serving VM with higher storage and network density.
- Z4M targets storage-serving use cases; CPU/RAM may be overprovisioned but pricing optimization is planned.
- Google is developing a Google Supercomputer (GSC) interface to provision AI/HPC infrastructure with co-placement optimization; VAST could be integrated as a selectable storage option with potential auto-deploy.

## Topics

Google Distributed Cloud RFP response strategy, Air-gapped/dark-site readiness and operational support model, Compliance evidence, certifications, and ATO considerations, Hardware platform options (Dell/HPE/Cisco) vs commodity VM shapes, RDMA and VM shape tradeoffs, Fort Meade on-prem Gemini validation path, Coordination between Google corporate GDC and Google Federal teams, Joint federal account alignment and co-selling, Google Marketplace offers and broader partnership tracks, TPU/model-builder partnership track, Z4M storage-serving VM roadmap (density, pricing optimization), Local SSD vs HyperDisk vs object storage tiers (latency/economics), Google Supercomputer (GSC) provisioning, co-placement, and partner integration, RDMA and GPUDirect Storage (A5X GPUs) and TPU RDMA timeline, Anywhere Cache (cost vs performance)

## Overview

Cloud-related work including confirming GCP GA timing and aligning initial lighthouse customers post-bottleneck fix.

## Status

| Field | Value |
|-------|-------|
| **Status** | active |
| **Owner** | Jason Vallery |

## Blockers

- ❌ Bottleneck fix required before confirming GA timing
- ❌ Risk of lift-and-shift approach without cloud primitives/control-plane stance
- ❌ MAI control-plane fragility and GPU issues may slow proof points
- ❌ Azure internal politics (Compute vs Storage) and long hardware qualification timelines
- ❌ Fragmentation risk if higher-layer opinionated services are built too early

## Next Steps

- [ ] Get Jeff approval for scope/ownership and ROB cadence
- [ ] Name single-threaded product owner for MAI/Apollo motion
- [ ] Green-light headcount plan (PMs/TPM/Product Ops/Tech Writer/Enablement)
- [ ] Endorse core-first prioritization and staged cloud plan with SLO gates
- [ ] Assign owners for PR/FAQ drafts and initial 6-pager(s)
- [ ] Define initial SLOs/SLIs, error budgets, and on-call RACI; baseline runbooks
- [ ] Create unified backlog with RICE scoring and define Cloud Design Qualifiers for 5.6
- [ ] Publish release/support/EOL policy and deal-override RAPID
- [ ] Clarify travel schedule and where the author should be (Ignite vs Supercomputing, Re:Invent, Tel Aviv, Iceland).
- [ ] Define reporting lines and scope of responsibility.

## Key Decisions

- ✅ Greg Castellucci will run point with Google Federal and coordinate with the corporate GDC team over the next few weeks.
- ✅ Jason Vallery will coordinate RFP content assembly and connect Greg with Google stakeholders.
- ✅ Alon Horev will conduct a 1:1 with Muninder Singh Sambi focused on AI, VM shapes/RDMA, and hardware tradeoffs.
- ✅ Leo will own the end-to-end formal RFP response and submission.
- ✅ Use the Fort Meade on-prem Gemini initiative as the primary near-term validation path/reference.
- ✅ Include Dell and HPE SKU recommendations and consider Cisco/commodity VM options in the architecture proposal.
- ✅ Proceed with local SSD-based Z4M for initial VAST on GCP; evaluate object/HyperDisk tiers later.
- ✅ Coordinate in-person sessions at Supercomputing and include key GCP stakeholders (Ilyas, Dean).
- ✅ Do not schedule an architecture/whiteboarding session until Walmart requirements are clarified.
- ✅ Lead with current capabilities plus forward hybrid roadmap narrative in the Mingming call.

## Collaborators

| Person | Role | Company |
|--------|------|---------|
| [[Director Hampson]] | Director (exact function not stated) | VAST Data |
| [[Ray Coetzee]] | Multi-tenancy SME (technical) |  |
| [[Michael Myrah]] | Partner PM (Azure Storage Hardware) | Microsoft |
| [[Amy Shapiro]] | CFO | VAST Data |
| [[Glenn Lockwood]] |  | OpenAI |
| [[Pete Iming]] |  |  |
| [[Shachar Feinblit]] |  |  |
| [[Juergen Willis]] | CVP of Azure Storage (retired) | Microsoft |
| [[Pradeep]] |  | Microsoft |
| [[Jack Kabat]] |  | Microsoft |
| [[John Mill]] |  |  |
| [[Brennan]] | Founder/executive (pricing influence) | VAST Data |
| [[Alon Horev]] |  |  |
| [[Liraz Ben Or]] | R&D (phase-gate process/operations for releases) | VAST Data |
| [[Jason Vallery]] | Product management (cloud); partnerships with hyperscale cloud providers | VAST Data |
| [[Asaf Levy]] |  |  |
| [[Tomer Hagay]] |  |  |
| [[Sourav]] |  |  |
| [[Josh Wentzell]] |  |  |
| [[Ike]] |  | VAST Data |
| [[Frank Ray]] | Likely Azure Networking commercial lead (uncertain) | Microsoft |
| [[Ronnie Borker]] | Runs Azure hardware | Microsoft |
| [[Ong]] |  | Microsoft |
| [[Greg Castellucci]] |  | VAST Data |
| [[Avi]] | Architecture (DataSpaces/replication/global namespace) |  |
| [[Rick Haselton]] |  |  |
| [[Rob Benoit]] | Runs Global Sales Engineering |  |
| [[Glenn Lockman]] |  |  |
| [[Qi]] | CVP (Azure Kubernetes, per transcript) | Microsoft |
| [[Suresh]] |  | Microsoft |
| [[Vikas]] |  |  |
| [[Ganesan]] |  |  |
| [[Girish]] |  |  |
| [[John Downey]] | Partner manager (high-performance file systems and primary storage) | Google |
| [[Morty]] |  |  |
| [[Noa Cohen]] | Release planning (major releases) | VAST Data |
| [[Rob Banga]] |  |  |
| [[Matt]] |  |  |
| [[Narayan]] | Azure Networking leader (overarching; uncertain) | Microsoft |
| [[Maneesh Sah]] |  |  |
| [[Vipin Sachdeva]] |  | Microsoft |
| [[Manish]] |  | Microsoft |
| [[Billy Kettler]] |  | Google |
| [[Paul]] | Sales Engineer (SE) for Mikey |  |
| [[Mike Kiernan]] |  | Microsoft |
| [[Kushal Datta]] |  |  |
| [[Randy Hayes]] |  | VAST Data |
| [[Ronnie Lazar]] |  |  |
| [[Anand]] |  | Microsoft |
| [[Arik Kishner]] | Account team member / seller (exact title not stated) | VAST Data |
| [[Joe Green]] |  | Microsoft |
| [[Kui]] |  | Microsoft |
| [[Andrew]] |  | Microsoft |
| [[Lior Genzel]] |  |  |
| [[Jeff Denworth]] |  |  |
| [[Eirikur Hrafnsson]] |  |  |
| [[Yancey]] | Control plane team lead (implied) | VAST Data |
| [[Nidhi]] |  | Microsoft |
| [[Jürgen]] |  |  |
| [[Timo Pervane]] |  |  |
| [[Hari]] | Systems Engineer | VAST Data |
| [[Mordechai Blaunstein]] |  |  |
| [[Andy Bernstein]] |  |  |
| [[Rob Gerard]] | CSI/CoSy program/project manager | VAST Data |
| [[Vishnu Charan TJ]] |  |  |
| [[Erez Zilber]] | Protocols architect | VAST Data |
| [[Egal]] |  | Microsoft |
| [[Ryan]] | Leads overlay team for database/data-engine services GTM | VAST Data |
| [[Kurt Niebuhr]] |  |  |
| [[FWOD]] | Manages database/pipeline SEs | VAST Data |
| [[Akanksha Mehrotra]] |  |  |
| [[Kanchan Mehrotra]] |  |  |
| [[Andy Perlsteiner]] |  |  |
| [[Renan]] |  | VAST Data |
| [[Olivia Borey]] |  |  |
| [[Eyal Traitel]] | Release planning (minor releases) | VAST Data |
| [[Sagi]] | Architect (implied) | VAST Data |
| [[Yogev Vankin]] |  |  |
| [[John]] | Alliances/partnerships lead (conventional channels; AMD/NVIDIA; control-plane partners) | VAST Data |
| [[Karl Vietmeier]] |  |  |
| [[Yonce]] |  |  |
| [[Carl]] |  | VAST Data |
| [[Nagender]] |  |  |
| [[Rosanne Kincaid–Smith]] |  | VAST Data |
| [[Amit]] |  |  |
| [[Rajat Monga]] | Leads inferencing stuff |  |
| [[Vipul]] |  |  |
| [[Jonsi Stephenson]] | CEO | VAST Data |
| [[Phil Wagstrom]] | Multi-tenancy SME |  |
| [[Jai Menon]] |  |  |
| [[Vipin]] |  | Microsoft |
| [[Tiffany Stonehill]] | Cloud field lead for AWS and Azure (exact title not stated) | VAST Data |
| [[Mikey]] |  |  |
| [[Deandre Jackson]] | Technical Enablement Director |  |

## Related People

- [[Director Hampson]]
- [[Ray Coetzee]]
- [[Michael Myrah]]
- [[Amy Shapiro]]
- [[Glenn Lockwood]]
- [[Pete Iming]]
- [[Shachar Feinblit]]
- [[Juergen Willis]]
- [[Pradeep]]
- [[Jack Kabat]]
- [[John Mill]]
- [[Brennan]]
- [[Alon Horev]]
- [[Liraz Ben Or]]
- [[Jason Vallery]]
- [[Asaf Levy]]
- [[Tomer Hagay]]
- [[Sourav]]
- [[Josh Wentzell]]
- [[Ike]]
- [[Frank Ray]]
- [[Ronnie Borker]]
- [[Ong]]
- [[Greg Castellucci]]
- [[Avi]]
- [[Rick Haselton]]
- [[Rob Benoit]]
- [[Glenn Lockman]]
- [[Qi]]
- [[Suresh]]
- [[Vikas]]
- [[Ganesan]]
- [[Girish]]
- [[John Downey]]
- [[Morty]]
- [[Noa Cohen]]
- [[Rob Banga]]
- [[Matt]]
- [[Narayan]]
- [[Maneesh Sah]]
- [[Vipin Sachdeva]]
- [[Manish]]
- [[Billy Kettler]]
- [[Paul]]
- [[Mike Kiernan]]
- [[Kushal Datta]]
- [[Randy Hayes]]
- [[Ronnie Lazar]]
- [[Anand]]
- [[Arik Kishner]]
- [[Joe Green]]
- [[Kui]]
- [[Andrew]]
- [[Lior Genzel]]
- [[Jeff Denworth]]
- [[Eirikur Hrafnsson]]
- [[Yancey]]
- [[Nidhi]]
- [[Jürgen]]
- [[Timo Pervane]]
- [[Hari]]
- [[Mordechai Blaunstein]]
- [[Andy Bernstein]]
- [[Rob Gerard]]
- [[Vishnu Charan TJ]]
- [[Erez Zilber]]
- [[Egal]]
- [[Ryan]]
- [[Kurt Niebuhr]]
- [[FWOD]]
- [[Akanksha Mehrotra]]
- [[Kanchan Mehrotra]]
- [[Andy Perlsteiner]]
- [[Renan]]
- [[Olivia Borey]]
- [[Eyal Traitel]]
- [[Sagi]]
- [[Yogev Vankin]]
- [[John]]
- [[Karl Vietmeier]]
- [[Yonce]]
- [[Carl]]
- [[Nagender]]
- [[Rosanne Kincaid–Smith]]
- [[Amit]]
- [[Rajat Monga]]
- [[Vipul]]
- [[Jonsi Stephenson]]
- [[Phil Wagstrom]]
- [[Jai Menon]]
- [[Vipin]]
- [[Tiffany Stonehill]]
- [[Mikey]]
- [[Deandre Jackson]]

## Related Customers

- [[Lambda]]
- [[Microsoft]]
- [[Zoom]]
- [[CoreWeave]]
- [[N-Scale]]
- [[Anthropic]]
- [[Google]]
- [[NBCU]]
- [[Two Sigma]]
- [[OpenAI]]
- [[Walmart]]

## Related

<!-- Wikilinks to related entities -->
