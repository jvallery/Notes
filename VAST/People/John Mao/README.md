---
type: people
title: John Mao
created: '2026-01-03'
last_contact: '2025-12-19'
auto_created: true
tags:
- type/people
- needs-review
---

# John Mao

## Contact Information

| Field | Value |
|-------|-------|
| **Role** | Alliances team lead |
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
WHERE !completed AND contains(text, "John Mao")
SORT due ASC
```


## Tasks They Own

_Action items this person is responsible for:_

```dataview
TASK
WHERE contains(text, "@JohnMao") AND !completed
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

Roles and responsibilities between PM and Field CTO org, Documentation and field training ownership gaps, Release process: phase gates, implementation reviews, FRDs/Confluence, Hands-on enablement: OVA, SE Lab, GitLab access, VAST on Cloud viability and cloud economics, Multi-tenancy backlog toward SaaS, OpenAI architecture and global data plane opportunity, Sync Engine ownership gap and Azure Blob-source migration needs, Azure Blob API vs Tuscany trade-offs, OpenAI storage architecture and internal competition (Rockset/FoundationDB/RocksDB), AZCopy as Blob API MVP target, ABFS driver and Spark/Databricks integration considerations, Tiering/offload to Azure Blob and flash vs HDD supply dynamics, Namespace/metadata synchronization with existing cloud object data (change feed, eventual consistency), Azure Key Vault / customer-managed keys gap

## Recent Context

- 2025-12-19: [[2025-12-19]] - Discussion between Jeff Denworth and Jason Vallery on VAST’s Microsoft/Azure strategy: what level of... (via Jeff Denworth)
- 2025-10-30: [[2025-10-30 - Alignment call on roles, gaps, and collaboration. Andy outlined his team’s four]] - Weekly 1:1 alignment between Jason Vallery and Andy Perlsteiner covering Andy’s team charter, major ... (via Andy Perlsteiner)

## Profile

**Role**: Alliances team lead (Alliances)
**Relationship**: Unclear

**Background**:
- Referenced in a thread about OpenAI/Rockset acquisition and internal dynamics; used as context for OpenAI’s internal storage competition.
- Runs alliances; technical staff sometimes use SE lab carve-outs for partner integration POCs.

## Key Decisions

- ✅ Use Phil Wagstrom as primary multi-tenancy SME contact.
- ✅ Proceed with OVA and SE Lab access for Jason’s learning.
- ✅ Schedule a follow-up focused on OpenAI architecture and needs.
- ✅ Do not prioritize building 'append blob' support speculatively for OpenAI; only consider if/when OpenAI asks or if pipelines will take years to move and VAST wants that data.
- ✅ Define Blob API MVP for Microsoft AI as AZCopy compatibility rather than full Blob API breadth.

## Related Projects

- [[VAST on Azure Integration]]

## Related




---
*Last updated: *