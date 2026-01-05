---
created: '2026-01-03'
last_contact: '2025-12-17'
tags:
- type/customer
- generated
title: Google
type: customer
---

# Google

## Account Status

| Field | Value |
|-------|-------|
| **Status** | Partner |
| **Industry** | _Unknown_ |

## Key Contacts

- [[Jai Menon]]
- [[Olivia Kim]]
- [[Henry Perez]]
- [[Jan Niemus]]
- [[John Downey]]
- [[Billy Kettler]]
- [[Muninder Singh Sambi]]
- [[Ben]]

- [[Alon Horev]]
- [[Jason Vallery]]
- [[Tomer Hagay]]
- [[Violet]]

- [[Jonsi Stefansson]]

- [[Mordechai Blaunstein]]

- [[Lior Genzel]]

- [[Jeff Denworth]]
- [[Jason Vallery]]

- [[Lior Genzel]]
- [[Jason Vallery]]
- [[Kamal Vyas]]
- [[David Pawlak]]
## Open Tasks

```tasks
path includes Google
not done
```

## Recent Context

- 2025-12-15: [[2025-12-15 - Google GDC RFP review]]

- 2025-10-01: Confirmed need to validate GCP GA timing post-bottleneck fix and align on first 2–3 lighthouse customers. [[2025-10-01 - Confirm GCP GA timing]]

- 2025-11-14: Coordinated response to Google Distributed Cloud RFP (air-gapped readiness, compliance evidence, ops model) and aligned on Fort Meade on-prem validation path. ([[2025-11-14 - GDC RFP federal coordination]])

- 2025-11-13: [[2025-11-13 - GDC RFP security and ops]]

- 2025-10-31: Discussed Z4M roadmap, local SSD vs HyperDisk/object tiering, GSC co-placement/provisioning integration, and RDMA/GPUDirect enablement; identified ILB/egress economics as key blockers and planned Supercomputing in-person follow-ups. ([[2025-10-31 - GCP path for VAST Z4M]])

- 2025-10-29: [[2025-10-29 - VAST x Tackle GCP onboarding]]

- 2025-10-29: VAST Tackle onboarding kickoff for existing GCP Marketplace listing; discussed IAM/service account access, reporting export, private offers + metered overages, and Polaris/Salesforce metadata + SSO/event flow.

- 2025-10-28: Discussed GCP VIP/IP management, RDMA constraints on Z4M, and cross-project connectivity via PSCI; agreed on pros/cons doc and networking follow-up. ([[2025-10-28 - GCP RDMA IP failover options]])

- 2025-10-28: Aligned on GCP Marketplace MVP launch using private offers (Tackle.io + Salesforce) with Polaris as entitlement/metering source of truth; key open items: overage handling/EULA and finance billing/recon readiness. ([[2025-10-28 - GCP MVP launch alignment]])

- 2025-10-28: Dual-track GTM aligned for GCP MVP marketplace launch + hyperscaler-scale (Microsoft/MAI) track; routable IP networking confirmed; collateral/QA/support readiness flagged. [[2025-10-28 - Dual-track GCP MVP launch]]

- 2025-10-31: [[2025-10-31 - Aligning on VAST cloud strategy]] (via VAST)

- 2025-11-05: [[2025-11-05 - Walmart hybrid analytics requirements]] (via Walmart)

- 2025-10-01: TPU strategy outside GCP; align Google contacts; pricing/private offer; pipeline review (Zoom, UK Met, NBCU). [[2025-10-01 - TPU strategy and pipeline]]

- 2025-12-15: The email discusses follow-up questions from a Google RFP regarding encryption key granularity and t

- 2025-12-17: Jonsi Stefansson shared a Google Slides presentation titled 'GCP Flow from customer to sales to cust

- 2025-12-19: Mordechai Blaunstein shared a document titled 'CoreWeave-Vast Automation Project - V2 .docx' with yo

- 2025-12-22: Lior Genzel is requesting access to the document 'VAST and Azure Integration.docx' via Google Docs.

- 2025-12-22: Jeff Denworth assigned an action item to Jason Vallery regarding the VAST and Azure Integration prop

- 2025-12-17: The email discusses the follow-up on a meeting regarding VAST Data's GDC Storage RFP proposal, addre

- 2026-01-02: The email discusses comments on a document about integrating VAST with Azure, focusing on data stora

- 2025-12-22: Jeff Denworth assigned an action item related to the VAST and Azure Integration proposal document.

- 2026-01-02: The email discusses comments on a document about integrating VAST with Azure, focusing on data forma

- 2025-12-15: The email discusses follow-up questions from a Google RFP regarding encryption key granularity and s

- 2025-12-22: Lior Genzel is requesting access to the document titled 'VAST and Azure Integration.docx' via Google

- 2025-12-17: The email discusses follow-up questions regarding VAST Data's GDC Storage RFP proposal, including FI
- 2025-12-17: Exploring Collaboration Opportunities with Welliptic
## Key Facts

## Topics

- Google Distributed Cloud
- RFP
- encryption key granularity
- self-encrypting drives
- FIPS certification

- GCP
- customer flow
- sales process

- document sharing
- CoreWeave-Vast Automation Project

- document sharing
- VAST and Azure Integration

- VAST Data
- Azure
- Integration Proposal

- FIPS compliance
- pricing
- hardware partnerships
- GDC Storage RFP

- VAST integration
- Azure Blob
- data formats
- flash memory market
- supply chain
## Opportunities

- GDC Storage RFP: provide normalized performance + pricing data in Google Excel template for VAST (NVMe/TCP, NFSv4, S3)
- Align first 2–3 lighthouse customers for GCP GA rollout
- TPU strategy outside GCP (pending disclosure; prep meetings such as GTC-DC).
- Cloud deployment capacity/overhead modeling aligned to GCP fault-domain structure and rolling update budgets (MIG maxUnavailable/maxSurge).
- Google private offer marketplace entitlements and pricing schema; approval process initiated
- Similar proxy/tiering conversation as Walmart; relationship with existing cloud stores and namespace integration
- Google Distributed Cloud RFP to replace NetApp storage
- Fort Meade on-prem "Gemini as a service" validation (Q4 commit)
- Joint federal account alignment (FBI, State, Army referenced as opportunities)
- Potential TPU/model-builder partnership track

## Blockers

- ❌ Template requests Self-Encrypting Drives (FIPS 140-2/3), but VAST does not support SEDs; must position software-based dual encryption instead
- ❌ Potential mismatch between requested '112TiB usable' sizing and nearest sellable SKU; must document nearest-SKU approach with extra explanatory rows
- ❌ GA timing dependent on post-bottleneck fix
- ❌ Two-week timeline for disclosure of TPU strategy outside GCP.
- ❌ Sub-zonal availability domain support varies by region/zone; wide EC (e.g., 7+1) depends on actual availability domain guarantees.

## Collaborators

| Person | Role | Company |
|--------|------|---------|
| [[Jai Menon]] |  |  |
| [[Jeff Denworth]] |  |  |
| [[Jason Vallery]] | Finance |  |
| [[Olivia Kim]] |  | Google |
| [[Henry Perez]] |  | Google |
| [[Jan Niemus]] | Runs DoD/IC organization | Google |
| [[Randy Hayes]] |  | VAST Data |
| [[Ben]] | Product Manager (block storage) | Google |
| [[John Downey]] | Partner manager (high-performance file systems and primary storage) | Google |
| [[Tomer Hagay]] | Product/pricing stakeholder |  |
| [[Billy Kettler]] |  | Google |
| [[Lior Genzel]] |  |  |
| [[Greg Castellucci]] |  | VAST Data |
| [[Muninder Singh Sambi]] | Leader for Google Distributed Cloud (GDC); oversees GDC supply chain (new in role) | Google |
| [[Eirikur Hrafnsson]] |  |  |
| [[Jonsi Stephenson]] | CEO | VAST Data |
| [[Jason Vallery]] | Product management (cloud); partnerships with hyperscale cloud providers | VAST Data |

## Related

<!-- Wikilinks to related entities -->

## Related Projects

- [[Google Distributed Cloud RFP]]

- [[GCP Flow from customer to sales to customer]]

- [[CoreWeave-Vast Automation Project]]

- [[VAST and Azure Integration]]

- [[GDC Storage RFP]]