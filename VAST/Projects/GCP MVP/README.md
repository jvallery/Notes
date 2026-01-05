---
type: project
name: GCP MVP
status: active
last_contact: '2025-12-17'
created: '2026-01-05'
tags:
- type/project
- needs-review
---

# GCP MVP

## Key Facts

- A GCP performance Excel and introductions to the GCP performance lead and product marketing owner for a field performance calculator were to be shared with Jason Vallery.

- GCP performance Excel and field calculator enablement were to be shared, including introductions to the performance lead and product marketing owner responsible for the calculator.

- Jason Vallery planned to compare Google Anywhere Cache documentation to VAST Data Global Namespace to identify gaps and opportunities relevant to cloud strategy.

- Google Cloud and VAST have been collaborating for 6-12 months to define the first-generation storage-serving VM requirements for VAST on GCP, following 18+ months of architecture discussions.

- The group discussed using local SSD initially for VAST on GCP due to lower latency compared to HyperDisk and object storage, with later evaluation of HyperDisk and object tiers for other parts of the system.

- The TPU test review meeting is expected to include Nirav (Google contact), Rich Shanshee (Google contact), and Kartik (VAST participant) to walk through methodology and results.

- GCP MVP was described as close to launch and requires strong field collateral and an end-to-end demo video for Supercomputing.

- GCP MVP deployment networking will use routable IPs and requires a customer-provided IP range.

- A Google Cloud Platform meeting was requested to review TPU test setup after Google challenged benchmark results.

- The VAST Data Cloud Team tracked and completed a task to confirm Google Cloud Platform (GCP) GA timing after a bottleneck fix and to align the first 2-3 lighthouse customers.

- The VAST GCP Marketplace MVP will use fixed capacity pricing with a list price of $0.07 per GB for a fixed term and fixed price private offer.

- For the GCP Marketplace MVP, VAST will transact exclusively through the cloud marketplace and will not support BYOL (Bring Your Own License).

- The team is considering an overage allowance (example discussed: 10%) and charging overage at list PAYGO pricing if the marketplace and Tackle.io configuration can support it.

- First GCP Marketplace transactions were targeted for Nov-Dec 2025, with an intent to replicate the approach to AWS and Azure after the GCP MVP is operational.
## Recent Context

- 2026-01-05: Mentioned in: 1:1 with Lior Genzel, Google TPU strategy, private offers, and pipeline follow-ups

- 2026-01-05: Mentioned in: 1:1 with Lior Genzel, TPU strategy, private offer pricing, and pipeline follow-ups

- 2025-10-24: Mentioned in: 1:1 with Tomer Hagay, using cloud initiative to drive engineering maturity and AI-first dev workflows

- 2025-10-31: Mentioned in: GCP path for VAST on storage-serving VMs (Z4M), GSC co-placement, and RDMA/GPUDirect roadmap

- 2025-10-30: Mentioned in: Cloud marketplace support operating model, hyperscaler priority, and readiness plan (target 2026-02-01)

- 2025-10-28: Mentioned in: Cloud BU leadership aligns on dual-track GTM: GCP Marketplace MVP launch plus hyperscaler-scale MAI storyline

- 2025-10-30: Mentioned in: Cloud operations org design: distinct Customer Success, Support, and SRE roles with 2026-02-01 readiness target

- 2026-01-05: A task was tracked to confirm Google Cloud Platform (GCP) general availability (GA) timing after a b...

- 2025-10-28: The team aligned to launch the VAST GCP Marketplace MVP using private offers only, with fixed capaci...

- 2025-12-17: Jonsi Stephenson shared a Google Slides presentation titled "GCP Flow from customer to sales to cust...
## Tasks

```tasks
path includes GCP MVP
not done
```

## Topics

- GCP GA timing confirmation after bottleneck fix

- Lighthouse customer alignment for initial GCP launch

- GCP Marketplace MVP launch readiness and operational back-end requirements

- Private offers via Tackle.io and Salesforce integration

- Fixed capacity pricing model ($0.07/GB) and future unit-of-measure work

- Polaris entitlements, call-home, token enforcement, and metering

- Overage policy, marketplace limitations, and EULA language requirements

- GCP customer-to-sales-to-customer process flow documentation

- Google Slides collaboration (edit access)
## Key Decisions

- For the GCP Marketplace MVP, VAST will transact exclusively through cloud marketplaces and will not support BYOL (Bring Your Own License).

- VAST will use Tackle.io to generate and manage GCP Marketplace private offers and integrate offer data with Salesforce opportunities.

- The GCP Marketplace MVP will use fixed capacity pricing at $0.07/GB (list price) for private offers.

- Polaris will manage entitlement, call-home registration, and usage reporting for the GCP Marketplace MVP.