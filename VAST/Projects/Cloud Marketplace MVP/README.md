---
type: project
name: Cloud Marketplace MVP
status: active
last_contact: '2026-01-05'
created: '2026-01-05'
tags:
- type/project
- needs-review
---

# Cloud Marketplace MVP

## Key Facts

- Internal Microsoft teams cannot procure software via Azure Marketplace, requiring a non-Marketplace procurement route for VAST software subscriptions.

- Product Marketing was to be reconnected with Jason Vallery and Jonsi Stephenson, including Polaris and marketplace content requirements.

- VAST Polaris and Lifter path targets an Azure Native Resource Provider (RP) plus an Azure Marketplace offer with full API exposure and automation parity with Azure UI.

- The staged plan includes a Crawl phase with private offers and single-tenant deployments, and the notes argue that Azure Marketplace offers are not the win path at scale.

- The notes claim Azure Marketplace VM options (LSv4 and LSv5) are not price/performance competitive at scale.

- Marketplace control plane from Yancey’s team was acquired by VAST, with Google first and Azure expected to follow (internal tracking suggests early next year).

- Marketplace control plane work (from Yancey's team) is being integrated; Google Marketplace is planned first, with Azure Marketplace targeted around February (year not specified).

- The VAST Data Azure Marketplace VM-based offer (on Azure L-series VMs) was described as a procurement checkbox and not density or performance competitive for real workloads.

- A Microsoft Azure Marketplace SKU update is needed by Friday (2026-01-09) as part of Cloud Marketplace MVP execution.

- Tackle will integrate with Salesforce for marketplace operations, and Polaris is the source of truth for metering and billing; metering cadence is hourly utilization with aggregates sent to hyperscalers and ERP.

- Jason Vallery's 12-month focus includes delivering cloud marketplace offers across AWS, Azure, and GCP and improving price/performance using cloud primitives and potential ODM hardware in CSP data centers.

- Cloud Marketplace MVP activation for GCP is expected to leverage an existing blanket private offer to avoid new approval cycles, but pricing components still need tuning.

- Azure Blob API support is positioned as an enabler for a VAST Azure Marketplace offer and Azure ecosystem integrations.

- Initial marketplace automation for VAST on Cloud starts with Google Cloud Platform (GCP), with Microsoft Azure and Amazon Web Services (AWS) planned to follow in approximately three months (timing stated in meeting notes, not a committed roadmap date).

- Marketplace private offers for VAST on Cloud are intended to burn down customer cloud commits once the offers are GA and transactable.

- Cloud Marketplace MVP work includes connecting VAST Data's existing Google Cloud Marketplace listing to Tackle, enabling private offers and optional metered overage, and configuring reporting export.

- Polaris is intended to be the metering source of truth with hourly usage reporting for cloud marketplace offers.

- Tackle-Salesforce-Polaris integration is required for marketplace flows, customer registration, and entitlement and role management.

- Cloud Marketplace MVP GA acceptance criteria included operational requirements such as spin up and spin down behavior and DR or offload capabilities, and these criteria were used to determine when to begin field marketing.

- A pricing and go-to-market package for the Cloud Marketplace MVP was assembled ahead of a February SCO and included a pricing model, user stories, and roadmap materials split into NDA and non-NDA versions.

- Competitive performance and pricing comparisons were prepared for the Cloud Marketplace MVP against Weka and Hammerspace using equivalent Azure L-series VM types.

- Tackle.io will be used to generate marketplace private offers and sync them to Salesforce opportunities for the MVP launch motion.

- VAST Data is onboarding Tackle to sell VAST SaaS via Google Cloud Marketplace by reusing an existing private-offer listing and integrating metering, reporting, and order notifications.

- Marketplace offers should expose tenant outcomes and avoid requiring customers to administer complex VAST clusters.

- Jeff Denworth requested that the Azure Marketplace SKU change request be completed and submitted by Friday (relative to the 2026-01-04 email date).

- Jeff Denworth requested an Azure Marketplace SKU change request to be completed by Friday (relative to the 2026-01-04 email date).
## Recent Context

- 2025-10-29: Mentioned in: Microsoft and VAST align parallel tracks: UK Met Azure LSV4 test cluster and Microsoft-hosted bare-metal dev system

- 2026-01-05: Mentioned in: 1:1 with Lior Genzel, Google TPU strategy, private offers, and pipeline follow-ups

- 2025-10-29: Mentioned in: Parallel tracks for UK Met: Azure LSV4 test cluster (early Dec) and Microsoft-hosted bare-metal dev system

- 2025-11-04: Mentioned in: Jeff Denworth planning sessions: Cloud north star, MAI/Apollo wedge, SLO-gated operating cadence

- 2025-10-28: Mentioned in: 1:1 with Kanchan Mehrotra (Koncha), align on MAI + UK Met Office as marquee wins to drive Azure hardware shape

- 2025-10-28: Mentioned in: 1:1 with Kanchan Mehrotra, align on MAI and UK Met Office to drive better Azure storage VM shape for VAST

- 2025-10-27: Mentioned in: 1:1 with Kurt Niebuhr, Azure GTM path for VAST high-density, low-power storage

- 2026-01-05: Mentioned in: Azure Sync: Marketplace SKU update, GDC RFP deck, and MAI unified cache pricing clarification

- 2025-10-30: Mentioned in: Cloud marketplace support operating model, hyperscaler priority, and readiness plan (target 2026-02-01)

- 2025-10-31: Mentioned in: 1:1 with Josh Wentzell, VAST on Cloud strategy gaps: multi-tenancy, VOC deployment friction, automation tooling

- 2025-10-28: Mentioned in: Cloud BU leadership aligns on dual-track GTM: GCP Marketplace MVP launch plus hyperscaler-scale MAI storyline

- 2025-10-28: Mentioned in: 1:1 with Erez Zilber, Azure Blob API support for OpenAI and Azure Marketplace

- 2025-10-29: Internal team aligned on leading VAST on Cloud with the global namespace value proposition and routi...

- 2025-10-29: Mentioned in: Tackle onboarding kickoff to connect VAST existing GCP Marketplace listing and enable private offers with overage metering

- 2025-10-30: Mentioned in: Cloud operations org design: distinct Customer Success, Support, and SRE roles with 2026-02-01 readiness target

- 2026-01-05: The transcript captures completed Product and Performance Team tasks for the Cloud Marketplace MVP, ...

- 2025-10-28: Mentioned in: GCP Marketplace MVP launch readiness, private offers via Tackle, fixed capacity pricing and Polaris entitlements

- 2025-10-29: Mentioned in: Tackle onboarding kickoff to sell VAST SaaS via Google Cloud Marketplace (reuse existing private offer listing)

- 2025-10-31: Mentioned in: 1:1 with Rob Benoit: cloud strategy, marketplace UX, and SE enablement gaps

- 2026-01-05: Jeff Denworth sent a weekly status email with three action items: submit an Azure Marketplace SKU ch...

- 2026-01-05: Jeff Denworth flagged three weekly status items: an Azure Marketplace SKU change request due Friday,...
## Tasks

```tasks
path includes Cloud Marketplace MVP
not done
```

## Topics

- VAST on Cloud positioning and talk track, emphasizing global namespace and data mobility

- MVP architecture for VAST on Cloud (8-node VM plus local NVMe per tenant) and current scaling limits

- Cloud economics and constraints driven by hyperscaler VM shapes and cost versus on-prem

- Marketplace automation, transactability, and private offer process across GCP, Azure, and AWS

- Hyperscaler engagement plan, including AWS FSx first-party path and larger Azure VM shapes

- Cloud Marketplace MVP GA acceptance criteria and field marketing readiness

- Pricing and go-to-market package preparation for February SCO

- Competitive benchmarking versus Weka and Hammerspace on Azure L-series VMs

- Azure Marketplace SKU change request deadline and submission

- Updated deck required for Google Distributed Cloud (GDC) RFP

- Microsoft MAI unified cache pricing follow-up
## Key Decisions

- Use a designated Slack channel as the primary intake route for all VAST on Cloud opportunities and support, with Tiffany Stonehill triaging AWS and Azure and Olivia triaging GCP and OCI.

- Lead VAST on Cloud positioning with the global namespace value proposition to move data to where compute runs across on-premises, public cloud, and NeoCloud providers.

- Proceed with marketplace-based deployment and private offers to enable commit burn-down and smoother fulfillment once offers are GA and transactable.

- Showcase VAST on Cloud demos at the Supercomputing conference to drive awareness and pipeline.