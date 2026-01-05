# VAST + Azure Integration — Engineering Alignment & Asks (Microsoft)

**Audience:** Microsoft engineering stakeholders across storage, networking (Private Link), identity (Entra), and key Azure services (AI Foundry/Fabric/Synapse/Databricks/etc.).

**Goal:** Align on the MVP (“Crawl”) integration contract and identify the key platform constraints + asks required to deliver Crawl/Walk/Run successfully.

## 1) Integration Surfaces (High Level)

- **Azure Blob API façade (on VAST):** REST compatibility layer for standard Azure tools and SDKs.
- **Private connectivity:** Private Link Service exposure for VAST endpoints + DNS patterns; managed‑VNet constraints for Azure PaaS.
- **Identity & security alignment:** Entra ID tokens/managed identity, optional SAS/shared key compatibility where required by tooling.
- **Tiering + federation:** Azure Blob Storage (“Blob”) as durable capacity tier; VAST as performance tier with defined sync semantics.

## 2) MVP Definition (Crawl)

Primary spec: [Blob API Requirements (MVP)](../Appendices/Blob%20API%20Requirements%20%28MVP%29.md)

MVP characteristics:

- Block Blobs only; no ADLS Gen2 (dfs endpoint) / HNS semantics in MVP.
- Strict fidelity where tooling is brittle (XML list responses, XML error bodies).
- Copy-from-URL primitives for lake→edge hydration at scale (range-based PutBlockFromURL).
- Clear throttling + retry behavior aligned with client expectations.

## 3) Networking + Managed VNet Constraints

We expect two classes of connectivity:

- **Customer VNet (“easy mode”):** VNet peering / ExpressRoute + Private Endpoints to a VAST Private Link Service.
- **Managed VNet (“wall”):** Synapse/Fabric/other managed services often require “managed private endpoints” and approval workflows; some services constrain FQDN endpoints or PLS usage.

Asks / alignment topics:

- Validate which services can target partner **PLS** endpoints (and any approval workflow constraints).
- Confirm DNS patterns required for managed private endpoints and non-Azure-hosted endpoints.

## 4) Azure Service Integrations (Priority + Blockers)

Canonical matrix: [Azure Native Services Integration Matrix](../Appendices/Azure%20Native%20Services%20Integration%20Matrix.md)

We propose aligning first on the most common AI data-plane consumers:

- Azure AI Foundry patterns (orchestration app in customer VNet)
- Databricks (Classic + Serverless private connectivity)
- Synapse managed private endpoints
- Fabric / OneLake shortcuts constraints
- Azure AI Search private outbound patterns

## 5) “Run” End State (Managed Offering Requirements)

For a legitimate managed-service destination, we expect:

- Entra ID integration + CMK via Key Vault
- Azure Monitor/Log Analytics integration
- Marketplace/private offer procurement and billing alignment
- Managed lifecycle with operational SLOs

## 6) Open Questions / Asks (Initial)

- **Blob API contract:** confirm minimum semantics required by AzCopy/SDKs for partner endpoints (error schemas, headers, conditional behavior).
- **Serverless private connectivity:** validate Databricks Serverless + other serverless compute planes targeting partner PLS endpoints.
- **Fabric shortcuts:** confirm private-network options for S3-compatible shortcuts and the limitations around FQDN/PLS.
- **Managed private endpoint ops:** define/automate approval flows for managed services (Synapse/others).

## References

- Blob API MVP requirements: [Blob API Requirements (MVP)](../Appendices/Blob%20API%20Requirements%20%28MVP%29.md)
- Terminology & conventions: [Terminology & Conventions](../Appendices/Terminology%20%26%20Conventions.md)
- Workloads + reference topologies: [Workloads & Reference Topologies](../Appendices/Workloads%20%26%20Reference%20Topologies.md)
