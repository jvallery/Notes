# Azure Integration — TODO

This file tracks the remaining collateral, placeholders, and “still-to-write” sections for the VAST + Azure integration doc set.

## Doc Set (Audience-Specific)

- [?] Tighten [VAST/Executive Overview](VAST/Executive%20Overview.md) narrative for exec readability (shorter, fewer jargon terms) #task #proposed #auto
- [?] Expand [VAST/Engineering Delivery Plan](VAST/Engineering%20Delivery%20Plan.md) into an actionable milestone plan (owners, acceptance criteria, risks) #task #proposed #auto
- [?] Tighten [Microsoft/Executive Overview](Microsoft/Executive%20Overview.md) into a Microsoft-ready brief (clear “why Azure wins” + asks) #task #proposed #auto
- [?] Expand [Microsoft/Engineering Alignment & Asks](Microsoft/Engineering%20Alignment%20%26%20Asks.md) with concrete asks per service/team and validation plan #task #proposed #auto

## Consistency & Governance

- [?] Expand and maintain a shared terminology appendix; enforce naming conventions across all docs #task #proposed #auto
- [?] Decide whether “Tuscany” is an internal codename vs external term; standardize on “migration‑on‑read proxy” for Microsoft-facing collateral if needed #task #proposed #auto
- [?] Add an explicit “assumptions + non-goals” section to each audience doc to prevent scope creep #task #proposed #auto

## Extracted Placeholders (from legacy monolith)

- [?] Expand integration work detail (identity, encryption, security) and restructure “What/Why” as workstream subsections #task #proposed #auto
- [?] Cross-reference workloads ↔ Azure services; tie both to required enablement work; improve PaaS + IaaS narrative cohesion #task #proposed #auto
- [?] Add equivalent Azure PaaS service mapping into the workload matrix and update doc links #task #proposed #auto

## Collateral to Develop (Implied by the Current Content)

- [?] Create 1–2 reference architectures with diagrams + deployment steps for “Crawl” (W2, W5) #task #proposed #auto
- [?] Define “AzCopy gate” + “SDK gate” execution plan (test cases, environment, pass/fail) #task #proposed #auto
- [?] Specify the Blob API façade “account + endpoint model” (DNS, certs, account naming, container↔bucket mapping, key lifecycle for SAS/shared-key modes) #task #proposed #auto
- [?] Define authZ mapping for Blob API façade (Entra principals/claims → VAST users/groups/policies; least-privilege patterns) #task #proposed #auto
- [?] Document private connectivity playbooks (PLS + DNS + throughput tuning) for repeatable deployments #task #proposed #auto
- [?] Produce an “ask list” for Microsoft by Azure team (Storage, Private Link, AI Foundry, Fabric, Synapse, Databricks) #task #proposed #auto
- [?] Extend the Azure services matrix with priority (Crawl/Walk/Run) + owner (VAST/Microsoft/Customer) for each row #task #proposed #auto
- [?] Add per-workload “related Azure services” mapping (W1–W10) and link to the services matrix #task #proposed #auto
- [?] Create a shared “one-slide” architecture diagram (governance tier ↔ performance tier flows) for reuse across executive collateral #task #proposed #auto
- [?] Convert the services matrix “blockers” into a validation checklist and capture results per Azure service #task #proposed #auto

## Backlog Sections to Write (from legacy outline)

### Strategic Context & Business Case

- [?] Economics of GPU starvation: why “good enough” storage fails #task #proposed #auto
- [?] Supply chain & media constraints: flash volatility, HDD capacity tier, procurement lead times #task #proposed #auto
- [?] Success metrics & measurement framework (utilization, throughput, cost, time-to-train, ops burden) #task #proposed #auto

### Platform Overviews & Capability Alignment

- [?] VAST platform overview (modules + how they map to Azure scenarios) #task #proposed #auto
- [?] Protocol surfaces summary (NFS/SMB/S3/Blob API/Kafka) with “when to use what” #task #proposed #auto
- [?] DRR model and capacity math (what customers actually pay for) #task #proposed #auto
- [?] Resiliency & failure model (fail‑in‑place, erasure/parity, snapshots) #task #proposed #auto
- [?] Azure platform overview (storage/compute/analytics/integration services relevant to this integration) #task #proposed #auto
- [?] Key architectural constraints (control plane vs data plane, managed VNet walls, picker-based vs endpoint-based services) #task #proposed #auto

### Deployment Variants & Reference Topologies

- [?] Variant catalog write-up (A/B/C/D) with selection guidance #task #proposed #auto
- [?] Selection framework (customer/region/requirements → variant mapping) #task #proposed #auto
- [?] Performance profiles (capacity/bandwidth/IOPS/latency) #task #proposed #auto
- [?] DRR & efficiency profiles (effective capacity, power, rack density) #task #proposed #auto
- [?] Regional constraints (quotas, SKU availability, reservations) #task #proposed #auto
- [?] Supply chain & procurement implications (lead times, substitution options) #task #proposed #auto
- [?] Reliability, failure domains, and HA options #task #proposed #auto
- [?] DR/BC reference designs (RPO/RTO targets, replication patterns) #task #proposed #auto

### Integration Architecture Overview

- [?] Layered integration model (data plane / namespace+metadata / control plane / ops plane / commercial plane) #task #proposed #auto
- [?] Network models (customer VNet vs managed VNet vs public endpoint tradeoffs) #task #proposed #auto
- [?] Core integration patterns library (direct mount, direct object, Blob API, virtualization, bridging, PLS, cross-region replication) #task #proposed #auto

### Namespace & Metadata Federation (Federation Plane)

- [?] Problem statement: split-brain namespace and why federation is required #task #proposed #auto
- [?] Federation patterns (VAST master vs Blob master vs proxy/migration-on-read) #task #proposed #auto
- [?] Change detection & reconciliation (Event Grid vs Change Feed vs scans) #task #proposed #auto
- [?] Metadata mapping model (mtime/etag/content-type/custom metadata) #task #proposed #auto
- [?] Security mapping (identity + ACL semantics + drift control) #task #proposed #auto
- [?] Stub/hydration design (metadata-only stubs, cache policies, pinning) #task #proposed #auto
- [?] Consistency/concurrency guarantees + conflict resolution #task #proposed #auto
- [?] Scale architecture (sharding, checkpointing, lag tracking, backpressure) #task #proposed #auto
- [?] Observability & operations (sync health, lag, reconciliation metrics) #task #proposed #auto

### Tiering, Lifecycle & Data Formats

- [?] Tiering modes (opaque vs transparent vs hybrid) #task #proposed #auto
- [?] Policy framework (hot/warm/cold, retention, compliance, residency) #task #proposed #auto
- [?] Cost & transfer considerations (egress, cross-region, cache amplification) #task #proposed #auto
- [?] Portability & exit strategy #task #proposed #auto

### Networking & Connectivity

- [?] Connectivity design principles (private-first, deterministic routing) #task #proposed #auto
- [?] Private endpoints & Private Link fundamentals (what Azure services expect) #task #proposed #auto
- [?] Private Link Service (PLS) model for VAST endpoints (S3/Blob/NFS) #task #proposed #auto
- [?] PLS alias & connection approval workflow (who approves, how automated) #task #proposed #auto
- [?] DNS architecture (private zones, split-horizon, managed VNet DNS) #task #proposed #auto
- [?] Customer VNet connectivity (peering/routing/NSGs/ExpressRoute) #task #proposed #auto
- [?] Managed VNet connectivity patterns (Fabric/Synapse/serverless) #task #proposed #auto
- [?] Throughput & scale limits (SLB, SNAT, conntrack, timeouts, keep-alive) #task #proposed #auto
- [?] Cross-region backbone patterns (global peering, vWAN, replication paths) #task #proposed #auto

### Identity, Security, Compliance & Governance

- [?] Threat model & security posture #task #proposed #auto
- [?] Identity integration (Entra ID, managed identity patterns, compatibility modes) #task #proposed #auto
- [?] Key management (Key Vault, rotation, customer-managed keys) #task #proposed #auto
- [?] Perimeter controls (NSP, firewalls, egress policies, exfiltration control) #task #proposed #auto
- [?] Shared responsibility model (VAST vs Microsoft vs customer) #task #proposed #auto
