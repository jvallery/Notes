---
type: people
title: Arik Kishner
created: '2026-01-03'
last_contact: '2025-10-29'
auto_created: true
tags:
- type/people
- needs-review
- company/vast-data
---

# Arik Kishner

## Contact Information

| Field | Value |
|-------|-------|
| **Role** | Account team member / seller (exact title not stated) |
| **Company** | VAST Data |
| **Department** | _Unknown_ |
| **Email** | _Unknown_ |
| **Phone** | _Unknown_ |
| **LinkedIn** | _Unknown_ |
| **Location** | _Unknown_ |

## Relationship

_How do you work with this person? What is your dynamic?_

## Background

_Career history, expertise, interests, personal details shared..._


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
WHERE !completed AND contains(text, "Arik Kishner")
SORT due ASC
```


## Tasks They Own

_Action items this person is responsible for:_

```dataview
TASK
WHERE contains(text, "@ArikKishner") AND !completed
SORT due ASC
```

## Key Facts

- Tiffany Stonehill covers AWS and Azure; Olivia Borey covers GCP and OCI.
- Jason Vallery joined as VP of Product Management for Cloud and reports to Jeff Denworth; previously spent 13 years leading Microsoft object storage PM.
- Global namespace is positioned as the key differentiator to move data to where compute runs (on-prem, public cloud, cross-cloud, Neo clouds).
- Supported AWS VM shapes are ~120 TB nodes; Azure is ~23 TB nodes today with discussions for ~300 TB nodes next year.
- Cloud VM cost cited as ~$0.20/GB-month (~20x on-prem hardware cost).
- MVP is an 8-node HA VAST cluster on cloud VMs; same product as on-prem, optimized for ease of deployment and performance.
- Marketplace automation targets: GCP first; Azure and AWS within ~3 months.
- Cloud providers often sponsor POCs; VAST cloud spend can burn down customer cloud commits via marketplace/private offers once GA.
- AWS FSx first-party program is being pursued; more field opportunities help accelerate hyperscaler support.
- Cloud engineering team grew from ~5 to ~25 engineers, increasing velocity.

## Topics Discussed

VAST on Cloud positioning and global namespace, Marketplace automation and transacting via cloud marketplaces, VM shape constraints and cloud TCO vs on-prem, Object storage integration roadmap (e.g., S3) and SyncEngine bridge, Hyperscaler partnerships/programs (AWS FSx) and influencing roadmaps, Field intake process via Slack and Salesforce, Multi-tenancy and tenant-level peering limitations, SE enablement, collateral, and Supercomputing demos, VAST on Cloud positioning and talk track (global namespace, data-to-compute), MVP architecture (8-node VM/NVMe cluster per tenant) and deployment mechanics, Marketplace rollout and private offers; commit burn-down, Hyperscaler dependencies: VM shapes, AWS FSx first-party path, Object storage integration roadmap (S3) and SyncEngine, Handling multi-PB opportunities and expectation setting (Visa ~20PB), Customer learnings from ICE/NYSE evaluation (burst to AWS vs on-prem)

## Recent Context

- 2025-10-29: [[2025-10-29 - Team aligned on positioning and mechanics for VAST on Cloud. Emphasis on using g]] - Group office hours aligned the team on positioning and operating mechanics for VAST on Cloud, emphas... (via VAST on Cloud Office Hours)
- 2025-10-29: [[2025-10-29 - Team aligned on positioning and go-to-market for VAST on Cloud. Current MVP is a]] - Group meeting to align positioning and go-to-market for VAST on Cloud, including MVP architecture, m... (via VAST on Cloud Office Hours)

## Profile

**Role**: Account team member / seller (exact title not stated) at VAST Data (Sales/Field (implied))
**Relationship**: Internal collaborator (field)

**Background**:
- Raised a large-scale cloud copy requirement (~20 PB) and asked about scalability/TCO and architecture options; to follow up offline with Lior.
- Raised Visa account requirement for ~20PB full copy in AWS and asked about scalability/TCO improvements and newer architectures.

## Key Decisions

- ✅ Use the VAST on Cloud Slack channel as the primary intake for opportunities; Tiffany (AWS/Azure) and Olivia (GCP/OCI) lead engagement.
- ✅ Proceed with MVP 8-node HA VAST on Cloud clusters via marketplace automation (GCP first; Azure/AWS to follow).
- ✅ Actively pursue hyperscaler programs (e.g., AWS FSx) and larger VM shapes to improve cost/performance.
- ✅ Use Slack channel as the primary route for VAST on Cloud deals and support (Tiffany: AWS/Azure; Olivia: GCP/OCI).
- ✅ Lead with global namespace to enable data to move to compute across on-prem, cloud, and NeoClouds.
- ✅ Proceed with marketplace-based deployment and private offers to enable commit burn-down and smoother fulfillment.
- ✅ Showcase VAST on Cloud demos at Supercomputing to drive awareness and pipeline.

## Related Projects

- [[Cloud]]

## Related




---
*Last updated: *