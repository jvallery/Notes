---
type: people
title: Phil Wagstrom
created: '2026-01-03'
last_contact: '2025-11-07'
auto_created: true
tags:
- type/people
- needs-review
---

# Phil Wagstrom

## Contact Information

| Field | Value |
|-------|-------|
| **Role** | Multi-tenancy SME |
| **Company** |  |
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
WHERE !completed AND contains(text, "Phil Wagstrom")
SORT due ASC
```


## Tasks They Own

_Action items this person is responsible for:_

```dataview
TASK
WHERE contains(text, "@PhilWagstrom") AND !completed
SORT due ASC
```

## Key Facts

- Andy’s team operates across four pillars: field escalation/POC support, lab management/benchmarks, SE enablement/training plus PM augmentation, and marketing support.
- Documentation is currently feature/button-oriented and not scenario-driven; scenario guides are ad hoc and late.
- PM process gaps include training ownership, PRDs vs FRDs (engineering writes FRDs), release visibility, and access to builds/docs.
- OVA is a single-VM multi-container demo; requires ~128GB RAM host; client networking requires tunneling/proxies; unsupported.
- SE Lab access requires VPN plus an AD account via octo.selab.fastdata.com; multiple clusters exist with varying admin levels.
- GitLab access is restricted and requires an IT ticket for a licensed account.
- Implementation reviews are run by Galit/Orly; Confluence release pages (e.g., 5.4 dev) list features, owners, and FRDs.
- Sync Engine lacks a formal PM; Andy and Blake are acting PMs.
- OpenAI architecture pattern described: multi-exabyte lakes in 3 Azure regions; GPUs in 50+ regions plus other providers; GPU-adjacent cache with checkpoints back to central.
- Urgent need: Sync Engine must read from Azure Blob to support large migrations (wave.ai) on a December timeline; key engineer Aaron Zilber is OOO ~2.5 weeks.

## Topics Discussed

Roles and responsibilities between PM and Field CTO org, Documentation and field training ownership gaps, Release process: phase gates, implementation reviews, FRDs/Confluence, Hands-on enablement: OVA, SE Lab, GitLab access, VAST on Cloud viability and cloud economics, Multi-tenancy backlog toward SaaS, OpenAI architecture and global data plane opportunity, Sync Engine ownership gap and Azure Blob-source migration needs, Warm intro mapping via LinkedIn mutuals, Investor vectors for introductions, NVIDIA relationship strategy (events vs 1:1 intros), Outreach messaging strategy (pipeline components vs platform narrative), Persona targeting (data/pipeline teams vs exec-only), Salesforce history audit before re-engagement, Target account prioritization and expansion (e.g., Black Forest Labs)

## Recent Context

- 2025-11-07: [[2025-11-07 - Working session to brute-force warm paths into priority model builders using Lin]] - Working session for the Model Builder Turbine project to map warm introduction paths into priority m... (via Model Builder Turbine)
- 2025-10-30: [[2025-10-30 - Alignment call on roles, gaps, and collaboration. Andy outlined his team’s four]] - Weekly 1:1 alignment between Jason Vallery and Andy Perlsteiner covering Andy’s team charter, major ... (via Andy Perlsteiner)

## Profile

**Role**: Multi-tenancy SME (Andy’s team)
**Relationship**: Internal SME contact

**Background**:
- Primary SME for multi-tenancy; understands hierarchy and admin model (tenants/clusters/admin mapping).

## Key Decisions

- ✅ Use Phil Wagstrom as primary multi-tenancy SME contact.
- ✅ Proceed with OVA and SE Lab access for Jason’s learning.
- ✅ Schedule a follow-up focused on OpenAI architecture and needs.
- ✅ Reframe outreach to focus on concrete pipeline components (Kafka for RL, real-time vector DB) rather than platform narratives.
- ✅ Use an NVIDIA-customer event (via AI Circle) as the primary NVIDIA intro mechanism; direct 1:1 intros from NVIDIA reps are unlikely.
- ✅ Broaden persona targeting to include data/pipeline owners, not just CTO-level contacts.
- ✅ Defer direct Google/Microsoft-introduced paths where conflicts exist to reduce hyperscaler conflict risk.

## Related Projects

- [[Cloud]]

## Related




---
*Last updated: *