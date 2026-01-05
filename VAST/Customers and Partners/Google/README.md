---
type: account
name: Google
last_contact: '2025-12-15'
created: '2026-01-05'
tags:
- type/account
- needs-review
---

# Google

## Key Facts

- Google Distributed Cloud (GDC) provides a GCP-like experience deployed into private or hybrid data centers and includes an air-gapped variant targeted at government customers.

- Google Distributed Cloud deployments commonly run on Dell hardware, and have also involved HPE and Cisco gear.

- VAST Federal has active relationships with Google's DoD/IC organization led by Jan Niemus and is coordinating with Cisco on a federal proof of concept motion.

- Google Cloud Platform is Walmart’s current system of record for analytics ingestion pipelines using BigQuery and Google Cloud Storage.

- Google TPU strategy outside Google Cloud Platform (GCP) was discussed with an expected two-week timeline for disclosure and alignment with Google contacts Nirav (last name unknown) and Michelle (last name unknown) via prep meetings such as GTC-DC.

- Google issued a US-based RFP inviting VAST Data to respond as a potential replacement for NetApp as the storage solution for Google Distributed Cloud deployments.

- Google Distributed Cloud hardware commonly runs on Dell, and deployments have also involved HPE and Cisco gear.

- Walmart’s enterprise analytics run on Google Cloud Platform using BigQuery and Google Cloud Storage, and GCP is currently the source of truth for ingestion pipelines.

- Google TPU strategy outside Google Cloud Platform (GCP) was expected to be disclosed on an approximately two-week timeline and required alignment with Google contacts Nirav (last name unknown) and Michelle (last name unknown), plus prep meetings such as GTC-DC.

- Jason Vallery referenced private offers with Google as the current mechanism for VAST cloud-related transactions, while stating there is no transactable marketplace offer today.

- GCP design discussed included clustered VMs across placement groups and experimentation with GCP N and z3 instance families.

- Google Distributed Cloud (GDC) is emerging as Google's vehicle to deliver on-prem TPU deployments with tie-ins back to Google Cloud Platform (GCP).

- On Google Distributed Cloud (GDC), the only viable file storage options currently discussed were VAST Data and NetApp; NetApp's approach relies on reviving OnTap Select, a legacy stack previously end-of-life'd around 2019.

- VAST Data TPU testing using Google's model set reportedly showed about 20% better performance than Google's current managed Lustre stack, and a cross-region global namespace demo (Japan to Ohio) resonated with Google stakeholders.

- A Google Cloud marketplace private offer entitlement and pricing schema definition was called out as an immediate action to start approvals.

- VAST Data defined marketplace entitlements and a pricing schema for a Google private offer and began the approval process.

- VAST clusters exist or were being tracked on Google Cloud Platform (GCP) as of 2025-11-08.

- A Google RFP was expected to be TPU-oriented; the team should qualify scope and ensure the workload is not block I/O latency sensitive where NetApp typically excels.

- Google multi-region and caching patterns were referenced as a useful model for VAST Cloud region-spanning namespace and caching design.

- Google Cloud Platform does not provide a single API to move an IP directly between interfaces or VMs; the workflow is remove/unassign then reassign, creating a race window where the IP can be briefly unallocated.

- Google Managed Instance Groups (MIGs) can be configured with a pool of reserved static IPs for primary addresses, but this does not necessarily apply to alias IPs.

- Z4M is expected to launch with inter-node RDMA (Z4M to Z4M); GPU-direct storage RDMA between GPUs and Z4M is a separate enablement effort.

- Cross-project RDMA connectivity on GCP is expected to require Private Service Connect interfaces (PSCI); VPC peering is not expected to be supported for RDMA cross-project connections.

- Per-VM bandwidth is capped on the new shapes; adding NICs does not increase aggregate bandwidth, though it may still affect efficiency (queues or kernel behavior).

- Walmart’s analytics ingestion and processing for this workload runs on Google Cloud Platform (GCP) using BigQuery.

- Google Anywhere Cache was referenced as a comparative point for VAST Data Global Namespace caching and cloud architecture.

- Google Distributed Cloud storage service SKUs and pricing are based on IOPS per GB as the primary pivot, with throughput optimized secondarily.

- Multi-tenancy is a core part of Google Distributed Cloud architecture and will be relied on by the solution stack.

- Walmart’s analytics ingestion and processing for this environment runs on Google Cloud Platform (GCP) using BigQuery.

- Google Cloud launched Z3 as its first storage-optimized VM shape, optimized for compute workloads leveraging local storage, and it is a step toward storage-serving use cases due to higher storage and network density per VM.

- Google Cloud is developing Z4M as the next VM shape targeted at storage-serving workloads, increasing storage density and network density and aiming to match storage bandwidth to network bandwidth for storage-serving VMs.

- Google Cloud expects Z3 and Z4M to be overprovisioned on vCPU and memory for storage-serving use cases, and plans pricing optimization to make the cost model work despite overprovisioning.

- Google Cloud is developing a Google Supercomputer (GSC) provisioning interface to co-provision and co-place storage VMs and accelerator or compute VMs for AI/ML and HPC workloads, rather than provisioning independently without placement awareness.

- GCP challenged VAST Data TPU test results, questioning a reported ~23% performance improvement versus their current Managed Lustre results, and requested a review of the exact test setup.

- Google was a key partner context for the GCP MVP launch and Supercomputing booth presence, including a Google booth presentation requiring a demo.

- A Google Distributed Cloud (GDC) RFP requires understanding of control-plane integration needs such as API, monitoring, and billing for a GDC-aligned VAST deployment.

- Google was referenced as a competitor that could ship improved VM offerings sooner than Azure's one-year-out roadmap, affecting near-term platform decisions.

- The initial go-to-market motion for VAST Data on Google Cloud Marketplace is private offers to cross-sell existing on-prem customers, with a public offer later.

- Tackle onboarding for GCP requires a GCP service account JSON key and assignment of required IAM roles, plus enabling Google Cloud Marketplace reporting export for transaction reporting into Tackle.

- Google Cloud Platform challenged VAST's TPU test results and requested a meeting to review the test setup.

- Google Cloud Platform (GCP) GA timing was being confirmed after a bottleneck fix, with an effort to align the first 2-3 lighthouse customers.

- Jason Vallery raised the question of how much time to allocate across AWS, GCP, and other cloud initiatives.

- Google TPU partnership strategy was identified as a major opportunity to develop in parallel with Microsoft prioritization, with a risk that Google first-party storage could complicate competitive positioning.

- A Google RFP discussion with a TPU angle was planned for Thursday in Orlando, and the team intended to avoid block I/O-heavy pursuits where NetApp is strong.

- GCP Marketplace lacks native support for overage-at-PAYGO on fixed capacity private offers, potentially requiring a Tackle.io workaround.

- A federal connection was noted for a mutual customer context, involving sales engineering and operations considerations.

- VAST needs more native integration with Google Cloud Storage to support hybrid scenarios where data originates in Google Cloud and is brought on-prem.

- The team referenced a goal to show database acceleration results by NVIDIA GTC in March (conference timing), implying a public milestone target.

- Google was referenced as a topic to consider in relation to MAI POC and Microsoft hardware SKU discussions, but no specific linkage was captured.

- Google RFP review call attendees from Google included David Pollack (Partnerships Lead), Seiza Gersman and Gopal (procurement team overseeing the bid through completion), Kamal and Malikarjan (product management), and Jeff (storage engineering).

- Google described a regulatory compliance scenario requiring the ability to map a dataset or volume to a specific set of disks so that media associated with that dataset could be confiscated by regulators; Google noted the fallback is using disjoint clusters per dataset/tenant but that is suboptimal.

- A Google participant stated there are workload use cases requiring synchronous replication and zero RPO for files, and they believed VAST's element-level replication architecture might already support it or would soon.
## Recent Context

- 2025-11-14: Mentioned in: Google Distributed Cloud RFP debrief and federal coordination (air-gapped focus)

- 2025-11-06: Mentioned in: Walmart hybrid lakehouse architecture prep, SyncEngine + DataSpaces approach and Q4 two-cluster pilot

- 2026-01-05: Mentioned in: 1:1 with Lior Genzel, Google TPU strategy, private offers, and pipeline follow-ups

- 2026-01-05: Mentioned in: 1:1 with Lior Genzel, TPU strategy, private offer pricing, and pipeline follow-ups

- 2025-10-30: Mentioned in: 1:1 with Deandre Jackson, SE enablement cadence, S3/Object course, and VAST on Cloud status

- 2025-10-20: Mentioned in: 1:1 with Yogev Vankin: Multi-cloud global namespace, object-store tiering, GPU-adjacent cache, and metadata persistence

- 2025-11-07: Mentioned in: Cloud strategy 1:1 with Jonsi Stephenson, Google GDC TPU positioning and Microsoft Apollo storage path

- 2025-10-27: Mentioned in: Cloud pricing alignment with new on-prem model, capacity-only launch then Feb 1 normalization decision

- 2026-01-05: Mentioned in: Pricing vTeam task list and deliverables (Oct-Nov 2025)

- 2026-01-05: Mentioned in: Yogev Vankin - Oracle Cloud POC learnings and AWS/GCP/Azure cluster status summary request

- 2025-11-07: Mentioned in: 1:1 with Jeff Denworth, org map, onboarding, and cross-cloud strategy priorities

- 2025-10-24: Mentioned in: 1:1 with Tomer Hagay, AI-first development workflows, release discipline, and Global Namespace for cloud

- 2025-10-28: VAST and Google discussed VIP/IP management and failover approaches on Google Cloud Platform, compar...

- 2025-11-05: Mentioned in: Walmart Analytics hybrid replication requirements (GCP BigQuery to two on-prem sites)

- 2025-10-24: Mentioned in: 1:1 with Tomer Hagay, using cloud initiative to drive engineering maturity and AI-first dev workflows

- 2025-12-19: Mentioned in: GDC storage service benchmarking inputs, encryption constraints, and IOPS-per-GB SKU pivot

- 2025-11-05: Mentioned in: Walmart Analytics 2, hybrid GCP BigQuery to two on-prem sites with strong consistency goals

- 2025-10-31: Google Cloud outlined how VAST can run on upcoming storage-serving VM shapes (Z4M) with higher stora...

- 2025-10-30: Mentioned in: Cloud marketplace support operating model, hyperscaler priority, and readiness plan (target 2026-02-01)

- 2025-10-28: Mentioned in: Cloud BU leadership aligns on dual-track GTM: GCP Marketplace MVP launch plus hyperscaler-scale MAI storyline

- 2025-10-31: Mentioned in: 1:1 with Karl Vietmeier, align on VAST cloud strategy and GDC opportunity

- 2025-10-30: Mentioned in: 1:1 with Lior Genzel: MAI testing path, deck updates, and Azure VM politics

- 2025-10-29: VAST and Tackle kicked off onboarding to connect VAST's existing live Google Cloud Marketplace listi...

- 2025-10-30: Mentioned in: Cloud operations org design: distinct Customer Success, Support, and SRE roles with 2026-02-01 readiness target

- 2026-01-05: Mentioned in: Google: Confirm GCP GA timing after bottleneck fix and align lighthouse customers

- 2026-01-05: Mentioned in: 1:1 with Jeff Denworth - travel planning, scope ownership, and cloud team alignment

- 2025-10-27: Mentioned in: 1:1 with Jeff Denworth: cloud pipeline synthesis, pricing/consumption debate, and event planning (Tel Aviv, Tech Summit, Supercomputing)

- 2025-11-07: Mentioned in: Org map, priorities, and cloud strategy alignment (1:1 with Jeff Denworth)

- 2025-10-28: Mentioned in: GCP Marketplace MVP launch readiness, private offers via Tackle, fixed capacity pricing and Polaris entitlements

- 2025-10-29: VAST Data and Tackle kicked off onboarding to sell VAST’s SaaS through Google Cloud Marketplace usin...

- 2025-11-13: Discussed requirements and open questions for the Google Distributed Cloud RFP, focusing on TCO (HDD...

- 2025-11-14: Mentioned in: Walmart big data DR requirements gating architecture session; plan Mingming expectations call

- 2025-11-03: Mentioned in: 5.5 release plan review: feature freeze next week, beta January 2026, restricted release March 2026; scope deferrals and hardware supply risks

- 2025-11-03: Mentioned in: Lior Genzel: MAI POC and Microsoft hardware SKU questions

- 2025-12-15: Google participants walked VAST through the submitted Google Distributed Cloud RFP response, focusin...
## Tasks

```tasks
path includes Google
not done
```

## Topics

- GCP VIP failover design options: alias IP vs route-based failover vs Internal Load Balancer (ILB)

- GCP IP lifecycle and the unassign then reassign race window during failover

- MIG static IP pools and whether they can reserve VIPs and reduce reassignment risk

- RDMA constraints on GCP Z4M shapes, including separate RDMA interface or subnet and dual-interface model (RDMA plus TCP)

- Cross-project RDMA connectivity constraints: PSCI required, VPC peering unsupported

- GCP Z3 and Z4M storage-serving VM roadmap, including storage and network density targets

- Cost and pricing optimization for overprovisioned CPU and memory on storage-serving VMs

- Google Supercomputer (GSC) interface for co-placement and co-provisioning of storage and accelerator VMs

- Local SSD vs HyperDisk vs object storage tradeoffs for latency, performance, and economics

- RDMA and GPUDirect Storage enablement for A5X GPUs and later TPU RDMA

- Connecting an existing Google Cloud Marketplace listing to Tackle

- GCP access requirements: service account JSON key, IAM roles, and reporting export

- Private offers strategy and pricing structure (fixed price plus metered overage)

- Meter design options (single vs multiple meters, unit clarity, penny-meter pattern)

- Subscription lifecycle event notifications into VAST Polaris control plane

- Tackle onboarding process and required access for Google Cloud Marketplace integration

- Reusing VAST’s existing private-offer-only Google Cloud Marketplace listing and GCP project/product number

- Private offer pricing structure: fixed-price contracts plus overage charging when usage exceeds entitlement

- Metering design options including multiple meters and a penny-based meter for variable pricing

- Marketplace subscription and fulfillment event notifications into VAST Polaris control plane

- Google Distributed Cloud RFP requirements and evaluation criteria

- HDD vs QLC TCO analysis for GDC deployments

- Security requirements: SED, air-gapped operations, certifications

- Separation of duties and two-person rule (two-signed rule) for sensitive operations

- Multi-tenancy controls: QoS, quotas, tags, policy-based management

- Google Distributed Cloud RFP proposal walkthrough and validation of technical requirements responses

- Requirement B8: physical media or disk-level mapping of datasets/volumes versus cluster-wide sharding in VAST Data

- Regulatory compliance scenario: ability to confiscate media tied to a specific dataset/volume

- Requirement B16: synchronous replication across zones, and the tradeoff between zero RTO/RPO and performance/latency

- Current VAST Data replication capabilities (snapshot-based, cluster-to-cluster block-level sync replication) and potential file replication approaches
## Key Decisions

- Create a shared pros and cons document to re-evaluate GCP VIP and failover options (alias IP, route-based failover, and Internal Load Balancer) including pricing and feature tradeoffs.

- Engage Google networking for a focused follow-up deep dive on RDMA networking design and cross-project connectivity constraints.

- Start sizing and capacity planning work by collecting near-term testing projections first, then longer-term customer volume projections.

- Start VAST on GCP using local SSD-backed storage-serving VM shapes (Z4M path) for initial deployments due to latency advantages, and evaluate HyperDisk and object-tier approaches later for capacity and metadata offload.

- Coordinate in-person working sessions at Supercomputing and include additional Google Cloud stakeholders (Ilyas and Dean) to accelerate alignment on GSC integration, networking, and RDMA enablement.

- VAST Data will start with Google Cloud Marketplace and reuse the existing live listing, including reusing the existing GCP project and product number, rather than creating a new GCP project.

- VAST Data will lead with private offers for the initial sales motion on Google Cloud Marketplace, with optional metered overage capability; a public offer can follow later.

- Tackle will manage the marketplace integration workflow, including listing content migration into Tackle and configuration for private offers and metering.

- Start onboarding with Google Cloud Marketplace as the first priority for selling VAST SaaS via Tackle; public offers may follow later.

- Reuse the existing Google Cloud Marketplace listing and the existing GCP project and product number, rather than creating a new GCP project.

- Use private offers as the initial sales motion, with Tackle supporting listing content population and technical integration once access is granted.

- Proceed through the Google Distributed Cloud RFP technical requirements tab top-to-bottom, starting with the items VAST marked as 'No' (including B8 and B16), to clarify gaps and scenarios.