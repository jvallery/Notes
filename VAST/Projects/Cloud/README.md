---
type: project
name: Cloud
status: active
last_contact: '2025-10-30'
created: '2026-01-05'
tags:
- type/project
- needs-review
---

# Cloud

## Key Facts

- Google issued a US-based RFP inviting VAST Data to respond as a potential replacement for NetApp as the storage solution for Google Distributed Cloud deployments.

- A multi-tenancy gap list exists for VAST Data; a major blocker is that authentication providers are limited to 8 and are configured at the host cluster level rather than tenant-scoped, requiring significant work to scale and tenantize.

- The proposed product vision is a "Neocloud-in-a-box": a repeatable foundation for GPU-dense, single-tenant sites and select non-Azure data centers that is software-first, hardware-flexible, and liquid-cooling-friendly.

- The FY26 prioritization proposal is core layers first (cloud primitives, control plane stance, tenancy, operability, SLOs) and to avoid building opinionated higher-layer services (for example Insight/Agent engines) until the base is proven at scale.

- The proposed operating model uses RAPID decision roles and a documented Decision Log to reduce churn and speed major decisions.

- The proposed Rhythm of Business cadence includes: Monday WBR (Product and Eng weekly business review), Tuesday RFE triage, Wednesday design review (FRDs and PR/FAQs), Thursday release readiness (ship/no-ship gates), Friday decision council (Jeff Denworth as Decider), plus monthly MBR and quarterly PI/OKR planning.

- The proposal asserts the current PM-to-development ratio is unsustainably low and requests minimum viable staffing: 1-2 Principal PMs (Cloud Platform and Azure/Microsoft), 1 TPM (release/readiness), 1 Product Ops lead, 1 Tech Writer, and 1 Sales/SE Enablement PM.

- Jason Vallery and Eyal Traitel discussed SaaS and multi-tenant readiness as key priorities for VAST on Cloud, with a multi-tenancy gap list to be shared via Confluence.

- A separate engineering workshop was planned to align on Polaris/Lifter API exposure and automation for Azure Native manageability.

- The proposed FY26 prioritization is core layers first, explicitly avoiding building opinionated higher-layer services until the base platform is proven at scale.

- The plan proposes adopting Amazon Working Backwards artifacts (PR/FAQ and a 6-pager) for both "VAST Cloud" and "VAST in Apollo" to force clarity before build.

- The proposed operating model uses RAPID decision roles and a documented Decision Log to speed decisions and avoid churn.

- The proposed Rhythm of Business includes weekly and monthly cadences with explicit quality gates for design, readiness, release, and postmortems.

- Jason Vallery stated that VAST Data does not have a generally available, transactable 'VAST on Cloud' offering today and described it as a roadmap journey; he referenced private offers with Google and an intent to unlock AWS and Azure in the future (no dates provided).

- Deandre Jackson observed that some VAST SEs are reluctant to discuss features they have not personally used, and he attributed part of this to a perception that code delivery is often late, which reduces confidence in discussing roadmap items.

- Aligned on a design where hyperscaler object storage (Azure Blob, Amazon S3, Google Cloud Storage) is the durable system of record, with VAST providing compute, caching, and global namespace access.

- Captured a design debate on metadata persistence: block storage (EBS, Persistent Disk, Premium Disk) versus premium object options (Premium Blob, S3 Express), with concern about Premium Blob ~3 ms time-to-first-byte for metadata-heavy workloads.

- Captured requirements for QoS/governance (identity-based quotas and prioritization across throughput, TPS, and capacity) and for a prefetch API plus cache-on-read semantics for GPU-adjacent caching.

- VAST Data intends to pursue deeper integration with Google Distributed Cloud (GDC) and aims to be part of the GDC SKU for on-prem TPU deployments.

- Cloud Product Management is evaluating how current Customer Success managed-services/SRE practices for CoreWeave and xAI should translate into a future VAST-as-a-Service operating model.

- The current VAST on Cloud fit is viewed as economically weak versus first-party cloud capacity storage; the likely differentiated value is higher-level compute-adjacent workflows and a global data plane.

- VAST’s OVA exists but is unsupported; it requires approximately 128 GB RAM on the host, client networking requires tunneling or proxies, and it is a single-VM multi-container demo deployment.

- Multi-tenancy subject matter experts identified: Phil Wagstrom as primary and Ray Coetzee (UK) as another SME.

- Neo cloud GPU-adjacent storage is viewed as an opportunity to keep GPUs productive during network disconnects by maintaining a GPU-to-local-storage ratio.

- Cloud work included tracking or operating VAST clusters across AWS, GCP, and Azure and capturing learnings from an Oracle Cloud POC.

- For VAST Cloud, a lift-and-shift approach was considered unlikely to meet price/performance targets, and the approach discussed was a performant layer over cloud object storage with a region-spanning namespace and caching.

- Global Namespace was treated as a key differentiator for cloud and region-spanning performance, with strict consistency and caching/prefetch mechanisms.

- VAST Data release intake comes from leadership-driven priorities (example: S3 RDMA), from architects (example: Asaf and Sagi), and from Sales Engineering requests filed in Salesforce and tied to opportunities.

- An updated deck is being prepared and will be sent for the Google Distributed Cloud (GDC) RFP.

- Walmart’s hybrid analytics requirements include replicating a hot working set from GCP to two on-prem sites and maintaining a single interaction model across environments.

- Jason Vallery and Tomer Hagay aligned that VAST Data cloud success likely requires a high-performance layer over object storage with a global cache, and that lift-and-shift is unlikely to win.

- VAST on Cloud (as described) runs on virtual machines in any cloud provider, which constrains price-performance and makes it better for exposing endpoints than for storing large volumes of data due to VM and local ephemeral storage capacity limits.

- A current VAST on Cloud scenario is burst-to-cloud where an on-premises VAST cluster remains the system of record and VAST on Cloud provides cloud-based caching and endpoints (NFS or S3) via VAST global namespace and global data spaces so cloud compute can access on-prem data.

- Liraz Ben Or stated cloud components should be integrated into the same phase-gate and QA process as core releases, rather than being released ad hoc outside governance.

- VAST Data cloud work is being repositioned as a serious investment area and a candidate for a PM-led operating model, including cloud design qualifiers for FRDs.

- VAST cloud engineering work is split across two teams led by Ronnie and Max, with one team focused on VMs and the other focused on platform aspects.

- The VAST Cloud SaaS operating model requirements include DevOps and LifeSite rotations, telemetry, and 24x7 support as core components.

- Benchmark methodology for the RFP evaluation uses 4K I/O, 80/20 read/write, uniform random reads, and a sub-2 ms latency target.

- Benchmarking should be performed with encryption-in-transit enabled (IPsec for file and block, TLS for S3).

- Vendor comparison focuses on IOPS per GB, read throughput per GB, write throughput per GB, and price per GB across small/medium/large configurations.

- This discussion centers on a hybrid cloud analytics architecture spanning GCP and two Walmart on-prem sites, including replication and API compatibility requirements.

- VAST Data hyperscaler go-to-market priority order for cloud marketplace is Google Cloud Platform (GCP) first, Microsoft Azure second, and Amazon Web Services (AWS) third.

- Cloud marketplace rollout plan is phased: private offers start approximately 2 months after 2025-10-30, public offers follow 6-8 months after private offers, and a full multi-tenant SaaS offering is targeted for VAST Data fiscal year 2028.

- For both private and public marketplace offers, the initial cloud delivery model is deployed inside the customer tenant (not VAST-hosted SaaS), and does not involve shipping hardware.

- The cloud support operating model is split into proactive Customer Success, reactive Support, and 24/7 SRE on-call coverage, with SaaS requiring a more traditional SRE model due to multi-tenant operational responsibility across multiple customers.

- Operational readiness target date for the cloud support machine (support desk, SRE on-call, processes) is 2026-02-01.

- The team expects significant networking complexity in cloud deployments, which may increase support ticket volume compared to on-prem deployments.

- Cloud operations requires analytics (Tableau) for churn risk, feature usage, and consumption forecasting based on cloud customer telemetry.

- Legal and compliance work is needed to define data custodian obligations for SaaS and to define a SOC2 and FedRAMP certification path.

- Candidate cloud customers discussed include Microsoft (including MAI), UKMET via Microsoft, NBCU, Sigma, Jump Trading, Citadel, and Zoom (exploring AWS).

- Multi-tenancy in VAST has API and documentation gaps, including unclear tenant-scoped API usage and non-intuitive behavior when making API calls against a tenant context.

- Tenant admin capabilities in VAST are incomplete relative to cluster admin, forcing tenant admins to rely on cluster admins for tasks that should be tenant-scoped in a SaaS multi-tenant model.

- Tenant visibility gaps include limited ability for a tenant admin to see or filter available VIP pools for their tenant.

- VOC deployment is not streamlined and lacks preflight checks and a guided wizard, which can cause failures late in the deployment process.

- Large customers prefer Terraform and Ansible for automation; when Terraform provider coverage is incomplete, customers fall back to direct REST API calls, which creates state-management pain.

- VAST does not have a maintained official Ansible module; a beta exists but is not maintained, and the team prioritizes Terraform provider maturity first.

- Josh Wentzell shared a loopback OVA link for hands-on work; the loopback OVA can be spun up via AWX or Cosmodrome in Oracle Cloud Infrastructure (OCI).

- Jason Vallery is driving a cloud-first vision for VAST Data that includes VAST-as-a-Service, multi-cloud, and GPU-adjacent caching plus central storage patterns.

- Cloud BU leadership agreed to a dual-track go-to-market strategy: (1) ship the GCP MVP via cloud marketplace for enterprise burst use cases, and (2) pursue hyperscaler-scale first-party engagements such as Microsoft MAI with a hardware-optimized story and Polaris-managed operations.

- The Google Distributed Cloud (GDC) RFP surfaced via Cisco and may require VAST Data to integrate with Google's control plane for API, monitoring, and billing.

- VAST Data decided to make cloud a top priority and is scaling cloud go-to-market hiring and execution.

- VAST on Cloud differentiator is VAST Data's global namespace, enabling data mobility across on-premises, public cloud, and NeoCloud providers so customers can move data to where compute runs.

- The current VAST on Cloud MVP architecture is an 8-node VAST cluster per cloud tenant running on cloud VMs with local NVMe, positioned as a lift-and-shift performance product.

- Engineering headcount focused on cloud grew from 5 to 25, enabling faster roadmap velocity for VAST on Cloud.

- VAST Data's cloud control plane (Polaris) must receive subscription lifecycle events and potentially usage events from the marketplace integration, and needs defined endpoints and schema.

- The cloud go-to-market plan is phased: private marketplace offers first (approximately 2 months from 2025-10-30), public marketplace offers 6-8 months after private offers, and a full multi-tenant SaaS offering targeted for FY2028.

- For cloud operations, the team is adopting three distinct roles: Customer Success (proactive best practices and adoption), Support (reactive ticket handling), and SRE (24/7 operations, on-call rotation, and multi-tenant operational ownership for SaaS).

- The team set a target date of 2026-02-01 to be operationally ready with a 'cloud support machine' including 24/7 coverage expectations.

- Cloud support is expected to see more networking-related tickets and fewer or no hardware-related tickets compared to on-prem deployments.

- The Cloud Team was assigned ownership of confirming Google Cloud Platform (GCP) GA timing post bottleneck fix and aligning the first 2-3 lighthouse customers.

- Pricing model concepts under discussion included VDU/VCU and a fixed ratio pricing approach for VAST Data cloud offerings.

- Workload mix (training vs inference) and single-tenant vs multi-tenant requirements materially shape GPU cluster design and site placement decisions.

- Sites without strong fiber connectivity to hyperscaler hero regions are effectively limited to inference workloads rather than training workloads.

- Neoclouds increasingly build near power sources, and network backhaul becomes a bottleneck for AI workloads.

- Hybrid on-prem and cloud licensing conversion was identified as a future complexity for revenue recognition and may require a conversion model later.

- Multi-cloud is technically possible, but hyperscalers may resist cross-cloud messaging, creating GTM positioning risk.

- The meeting asserted that data gravity is shifting as compute chases power, increasing the importance of moving data to distributed compute locations.

- VAST’s Polaris control plane needs subscription and fulfillment event notifications and entitlement metadata from Google Cloud Marketplace (potentially via Tackle) to fulfill orders and gate entitlements.

- The Google Distributed Cloud RFP evaluation includes a total cost of ownership comparison between HDD-based configurations and QLC flash-based configurations.

- The Google Distributed Cloud RFP discussion included security requirements such as self-encrypting drives (SED), air-gapped security details, and certifications.

- The Google Distributed Cloud RFP discussion included governance requirements for multi-tenancy, including QoS/quotas, tags, and policy-based management to apply controls per tenant or workload.

- Operational requirements discussed for the Google Distributed Cloud RFP included how to manage, troubleshoot, patch, and perform remote patching in constrained environments.

- Preferred VAST-in-cloud approach is object storage for the capacity tier plus bare metal for performance, because cloud VM economics are poor at scale; GCP Z3 helps but becomes expensive at size.

- DataSpaces/global namespace is positioned as a key differentiator for hybrid and multi-cloud AI data mobility.

- VAST's current approach of running VAST on public cloud virtual machines is not viable at the anticipated Walmart big data scale, so the team is prioritizing a hybrid roadmap with deeper native integration to Google Cloud Storage.

- The meeting was a walkthrough of VAST Data's submitted proposal for the Google Distributed Cloud RFP, focusing on the technical requirements tab and items marked 'No' (including B8 and B16).
## Recent Context

- 2025-11-14: VAST cloud and federal teams aligned on responding to Google Distributed Cloud's US-based RFP to rep...

- 2025-10-29: Mentioned in: 1:1 with Eyal Traitel, VAST release planning (major/minor, hotfix/service packs) and multi-tenancy gaps

- 2025-11-04: Mentioned in: Jeff Denworth planning sessions, Cloud North Star, MAI/Apollo wedge, and ROB proposal

- 2025-11-14: VAST’s cloud and federal teams aligned on responding to Google Distributed Cloud’s US-based RFP to r...

- 2025-10-29: Mentioned in: 1:1 with Eyal Traitel, release planning (major/minor), hotfix/service pack flow, and SaaS multi-tenancy gaps

- 2025-10-29: Mentioned in: Parallel tracks for UK Met: Azure LSV4 test cluster (early Dec) and Microsoft-hosted bare-metal dev system

- 2025-11-04: Mentioned in: Jeff Denworth planning sessions: Cloud north star, MAI/Apollo wedge, SLO-gated operating cadence

- 2025-10-30: Mentioned in: 1:1 with Deandre Jackson, SE enablement cadence, S3/Object course, and VAST on Cloud status

- 2025-10-20: Mentioned in: 1:1 with Yogev Vankin: Multi-cloud global namespace, object-store tiering, GPU-adjacent cache, and metadata persistence

- 2025-11-07: Mentioned in: Cloud strategy 1:1 with Jonsi Stephenson, Google GDC TPU positioning and Microsoft Apollo storage path

- 2025-10-29: Mentioned in: 1:1 with Rick Haselton, CoreWeave and xAI Customer Success operating model and workload patterns

- 2025-10-30: Mentioned in: 1:1 with Andy Perlsteiner, align on Field CTO pillars, cloud viability focus, and Sync Engine Blob gap

- 2025-10-28: Mentioned in: 1:1 with Kanchan Mehrotra, align on MAI and UK Met Office to drive better Azure storage VM shape for VAST

- 2026-01-05: Mentioned in: Yogev Vankin - Oracle Cloud POC learnings and AWS/GCP/Azure cluster status summary request

- 2025-10-24: Mentioned in: 1:1 with Tomer Hagay, AI-first development workflows, release discipline, and Global Namespace for cloud

- 2025-10-29: Mentioned in: 1:1 with Eyal Traitel, release intake and SaaS blockers (multi-tenancy gaps)

- 2026-01-05: Mentioned in: Azure Sync: Marketplace SKU update, GDC RFP deck, and MAI unified cache pricing clarification

- 2025-11-05: Mentioned in: Walmart Analytics hybrid replication requirements (GCP BigQuery to two on-prem sites)

- 2025-10-24: Mentioned in: 1:1 with Tomer Hagay, using cloud initiative to drive engineering maturity and AI-first dev workflows

- 2025-12-18: Mentioned in: Azure integration recording, outline and MVP focus on Blob API compatibility for GPU-adjacent VAST

- 2025-10-29: Mentioned in: Liraz Ben Or walked Jason through VAST 4 phase-gate release management (5.4-5.6) and sustaining vForce model

- 2025-10-29: Mentioned in: Jason Vallery 1:1 with Tomer Hagay, align on PM-led cloud model and cloud design qualifiers (multi-tenancy)

- 2025-10-28: Mentioned in: 1:1 with Shachar Feinblit, weekly cadence and Tel Aviv visit planning (Nov 23-26, 2025)

- 2026-01-05: A task was tracked to draft the operating model requirements for VAST Cloud SaaS, covering DevOps an...

- 2025-12-19: Mentioned in: GDC storage service benchmarking inputs, encryption constraints, and IOPS-per-GB SKU pivot

- 2025-10-29: Internal VAST team aligned on how to position VAST on Cloud around the global namespace, specificall...

- 2025-11-05: Mentioned in: Walmart Analytics 2, hybrid GCP BigQuery to two on-prem sites with strong consistency goals

- 2025-10-30: The team aligned on a cloud support operating model that separates Customer Success (proactive), Sup...

- 2025-10-31: Mentioned in: 1:1 with Josh Wentzell, VAST on Cloud strategy gaps: multi-tenancy, VOC deployment friction, automation tooling

- 2025-10-29: Mentioned in: 1:1 with Rick Haselton, CS operating model for CoreWeave and xAI plus cloud-first VAST vision

- 2025-10-28: Cloud BU leadership aligned on a dual-track strategy: ship the GCP MVP via marketplace with strong c...

- 2025-10-31: Mentioned in: 1:1 with Karl Vietmeier, align on VAST cloud strategy and GDC opportunity

- 2025-09-16: Mentioned in: 1:1 with Jeff Denworth: accelerated cloud GTM hiring, Azure GTM role for Jason, and Microsoft egress strategy

- 2025-10-29: Mentioned in: VAST on Cloud positioning and GTM alignment, MVP architecture, marketplace plan, and hyperscaler constraints

- 2025-10-29: Mentioned in: Tackle onboarding kickoff to connect VAST existing GCP Marketplace listing and enable private offers with overage metering

- 2025-10-30: The team aligned on a distinct operating model for cloud deployments with separate Customer Success ...

- 2026-01-05: Mentioned in: Google: Confirm GCP GA timing after bottleneck fix and align lighthouse customers

- 2026-01-05: Mentioned in: 1:1 with Jeff Denworth - travel planning, scope ownership, and cloud team alignment

- 2025-10-22: Mentioned in: 1:1 with Rosanne Kincaid–Smith: Dhammak GPU cloud buildout and Microsoft partnership positioning

- 2025-10-28: Mentioned in: GCP Marketplace MVP launch readiness, private offers via Tackle, fixed capacity pricing and Polaris entitlements

- 2025-10-22: Mentioned in: 1:1 with Rosanne Kincaid–Smith, Microsoft GPU capacity posture and Dhammak anchor-tenant strategy (2025-10-22)

- 2025-10-29: Mentioned in: Tackle onboarding kickoff to sell VAST SaaS via Google Cloud Marketplace (reuse existing private offer listing)

- 2025-11-13: Mentioned in: Google Distributed Cloud RFP discussion, security, multi-tenancy, and hardware options

- 2025-10-31: Mentioned in: 1:1 with Rob Benoit: cloud strategy, marketplace UX, and SE enablement gaps

- 2025-11-14: Mentioned in: Walmart big data DR requirements gating architecture session; plan Mingming expectations call

- 2025-12-15: Mentioned in: Google Distributed Cloud RFP review, technical requirement gaps (B8, B16)
## Tasks

```tasks
path includes Cloud
not done
```

## Topics

- Google Distributed Cloud (GDC) RFP to replace NetApp storage for connected and air-gapped deployments

- Air-gapped operational readiness requirements: updates, staffing model, troubleshooting practices, and compliance evidence

- Security and compliance artifacts for federal: certifications, ATO posture, DISA STIG alignment, encryption, and attestations

- Multi-tenancy, quotas, tagging integration, and tenant isolation expectations for GDC

- Hardware and deployment options for GDC: Dell, HPE, Cisco, and potential commodity VM shapes with RDMA

- Air-gapped readiness requirements: compliance/attestations, encryption, multi-tenancy, quotas, tags integration, and operations model (updates, staffing, troubleshooting)

- Stakeholder mapping and alignment between Google corporate GDC and Google Federal teams

- Fort Meade "Gemini as a service" on-prem initiative as a rapid joint validation reference

- Hardware and deployment options for GDC: Dell, HPE, Cisco, and commodity VM shapes with RDMA

- DevOps and LifeSite rotations for SaaS operations

- Telemetry requirements for VAST Cloud

- 24x7 support model for VAST Cloud SaaS

- VAST on Cloud positioning: global namespace as differentiator for data mobility to compute

- Field enablement: battle cards, talk tracks, and routing opportunities through Slack plus Salesforce

- Customer scenario: ICE (New York Stock Exchange) evaluated AWS burst but chose VAST on-prem after cost and complexity analysis

- Customer scenario: moving workloads off GCP back to on-prem and using VAST for hybrid migration

- Cloud support operating model: Customer Success vs Support vs SRE, including 24/7 coverage

- Phased cloud marketplace rollout: private offers, public offers, and FY28 SaaS

- Hyperscaler prioritization: GCP, Azure, AWS sequencing

- Marketplace operations stack: Salesforce, Tackle, Polaris, ERP integration and hourly metering

- Cloud telemetry and analytics requirements (Tableau) for churn, usage, and forecasting

- GCP MVP launch readiness via marketplace and required field collateral

- Supercomputing conference demo requirements across VAST, Google, and Microsoft booths

- MAI hyperscaler-scale opportunity and required storyline, diagrams, and deck

- Polaris role in lifecycle management and marketplace integration

- GCP MVP networking decision: routable IPs and customer-provided IP ranges

- Cloud org design and responsibility split across Customer Success, Support, and SRE

- 24/7 operations readiness and on-call rotation planning for cloud and future SaaS

- Marketplace commercialization phases: private offers, public offers, and FY2028 SaaS

- Microsoft Azure near-term prioritization and target account focus

- Tackle-Salesforce-Polaris integration for marketplace flows and entitlements
## Key Decisions

- Greg Castellucci will run point for engagement with Google Federal and coordinate with the corporate Google Distributed Cloud team for the RFP pursuit and validation motion.

- Jason Vallery will coordinate assembly of the Google Distributed Cloud RFP response content, including required technical and operational details, and will connect Greg Castellucci with relevant Google stakeholders.

- Alon Horev will pursue a 1:1 meeting with Muninder Singh Sambi to cover AI approach, VM shapes, RDMA considerations, and hardware tradeoffs for Google Distributed Cloud air-gapped deployments.

- A person referred to as "Leo" will own the end-to-end formal RFP response submission for Google Distributed Cloud.

- The team will use the Fort Meade "Gemini as a service" on-prem initiative as the primary near-term joint validation path and reference point, subject to what can be cited in the RFP.

- The proposal will include recommended Dell and HPE SKUs and will consider Cisco and commodity VM deployment options as part of the architecture approach.

- Greg Castellucci will run point with Google Federal and coordinate with the corporate Google Distributed Cloud team for the RFP pursuit and near-term validation planning.

- Jason Vallery will coordinate assembly of the Google Distributed Cloud RFP response content and connect Greg Castellucci with relevant Google stakeholders.

- Alon Horev will schedule and conduct a 1:1 with Muninder Singh Sambi to discuss AI approach, VM shapes, RDMA, and hardware tradeoffs for air-gapped Google Distributed Cloud deployments.

- A person referred to as "Leo" will own the end-to-end formal Google Distributed Cloud RFP response and submission (identity to be clarified).

- VAST will use the Fort Meade on-prem "Gemini as a service" effort as the primary near-term joint validation path and reference, subject to confirmation of what can be cited.

- The proposal will include recommended Dell and HPE hardware SKUs and will consider Cisco and commodity VM options for deployment.

- Use the dedicated VAST on Cloud Slack channel as the primary intake path for field opportunities, with opportunities also registered in Salesforce for tracking and rapid support.

- Position VAST on Cloud primarily around VAST's global namespace and the ability to move data to where compute runs across on-prem, public cloud, cross-cloud, and Neo clouds.

- VAST Data cloud hyperscaler priority order is Google Cloud Platform (GCP) first, Microsoft Azure second, and Amazon Web Services (AWS) third.

- VAST Data will proceed with a phased cloud marketplace rollout: private offers first, then public offers 6-8 months later, and a full multi-tenant SaaS offering targeted for FY28.

- VAST Data will adopt a separated cloud operating model with distinct functions for Customer Success (proactive), Support (reactive), and 24/7 SRE on-call coverage.

- VAST Data cloud support operational readiness target date is 2026-02-01.

- Tackle to Salesforce integration and Polaris as the metering and billing system of record are gating requirements for cloud marketplace operations.

- Pursue a dual-track go-to-market strategy: ship the GCP MVP via marketplace for enterprise adoption while also pursuing hyperscaler-scale first-party engagements (for example Microsoft MAI) with a hardware-optimized story and Polaris-managed operations.

- Use routable IPs for the GCP MVP deployment model, and defer alias IPs and a Google SaaS Runtime approach until after MVP launch.

- Adapt the Enscale solution deck for Microsoft MAI positioning, emphasizing a Kubernetes-led control plane (Project Apollo) and Polaris for lifecycle management.

- Avoid CoreWeave-style lock-in in any Enscale or Nscale resale arrangement by retaining VAST feature and control exposure contractually and technically.

- Adopt a distinct cloud operating model with separate Customer Success, Support, and SRE responsibilities, including 24/7 SRE on-call coverage for SaaS operations.

- Prioritize Microsoft Azure opportunities in the near term due to pent-up demand and large opportunities, with Google Cloud Platform and AWS following.

- Use Polaris as the metering source of truth with hourly usage reporting for cloud marketplace offers.

- Reaffirm the phased cloud commercialization plan: private offers first, public offers next, and full SaaS targeted for FY2028.

- Prepare cloud enablement and documentation content for SKO for Sales Engineering, Support, and Customer Success.