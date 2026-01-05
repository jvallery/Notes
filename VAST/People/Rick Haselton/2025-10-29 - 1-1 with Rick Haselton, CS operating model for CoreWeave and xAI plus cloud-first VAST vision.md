---
type: "people"
title: "1:1 with Rick Haselton, CS operating model for CoreWeave and xAI plus cloud-first VAST vision"
date: "2025-10-29"
person: ""
participants: ["Jason Vallery", "Rick Haselton"]
source: "transcript"
source_ref: "/Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-10-29 - Jason introduced his cloud-first vision for VAST (VAST-as-a-Service, multi-cloud.md"
tags:
  - "type/people"
  - "person/"
  - "generated"

---

# 1:1 with Rick Haselton, CS operating model for CoreWeave and xAI plus cloud-first VAST vision

**Date**: 2025-10-29
**With**: Jason Vallery, Rick Haselton

## Summary

Jason Vallery shared a cloud-first vision for VAST Data (VAST-as-a-Service, multi-cloud, GPU-adjacent caching plus central storage) and interviewed Rick Haselton on how Customer Success supports CoreWeave and xAI. Rick described a managed-services/SRE-style pod model with Slack-first comms, strict SLAs, and common operational issues (networking and C-node/D-node failures), plus a key product gap: xAI requested a single large filesystem across multiple clusters, which VAST cannot provide today.


## Action Items


- [?] Connect with Gordon Brown to review CoreWeave and xAI SLAs/SLOs, including response targets and any legal penalty clauses. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Draft an initial operating model for VAST-as-a-Service, clarifying SRE vs Customer Success roles, on-call expectations, communications model, and SLA posture. @Myself 📅 2025-11-08 #task #proposed #auto

- [?] Deep-dive with Rick Haselton on xAI workload patterns, including checkpointing behavior, GPU-adjacent caching needs, and end-to-end data flows, to inform cloud product design. @Myself 📅 2025-11-08 #task #proposed #auto

- [?] Assess feasibility and roadmap options for xAI's request for a multi-cluster single-namespace or single-filesystem experience, and document what VAST can offer today (replication and site-to-site namespace) versus gaps. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Obtain and review the legal SLA document(s) for CoreWeave and xAI, including any penalty clauses tied to SLA/SLO breaches. @Myself 📅 2025-11-08 ⏫ #task #proposed #auto

- [?] Validate the current after-hours and weekend coverage model across APJ/EMEA for critical incidents supporting CoreWeave and xAI. @Myself 📅 2025-11-08 #task #proposed #auto

- [?] Confirm the definitive location/provider for xAI cloud-resident data (for example, whether it is in Google Cloud Platform) and how data is repatriated and integrated with on-prem VAST clusters. @Myself 📅 2025-11-08 🔽 #task #proposed #auto

- [?] Review Slack alarm channel configurations and escalation paths used with CoreWeave and xAI to enable proactive outreach and incident notification. @Myself 📅 2025-11-08 🔽 #task #proposed #auto






## Key Information


- Rick Haselton is the technical lead in Customer Success for two of VAST Data's largest customers: CoreWeave (largest) and xAI (third largest).

- CoreWeave and xAI primarily operate on-premises clusters; xAI may keep some data in a public cloud but repatriates it to on-prem VAST clusters to run workloads.

- xAI requested that multiple VAST clusters (file and object) behave as one large cluster, effectively a single filesystem across clusters; VAST Data does not support a single filesystem spanning multiple clusters.

- VAST Data supports synchronous replication for S3 bucket data and supports a site-to-site global namespace, but these do not provide a single filesystem across disparate clusters.

- xAI stores massive raw training data in object clusters, approximately 314 PB used per cluster, and the clusters are rapidly filling (example sources mentioned: YouTube and Instagram).

- xAI previously used VAST Data for checkpointing and inferencing; checkpointing usage decreased recently but some activity returned in the Colossus environment.

- Customer Success engagement for CoreWeave and xAI is run like managed services or SRE, with close daily collaboration and rapid response expectations.

- Common operational issues for CoreWeave and xAI include networking problems and C-node and D-node failures; deeper Kubernetes/CSI questions are routed to vForce or R&D.

- Hardware RMAs for these customers are handled via VAST Data depots (Campbell or Sacramento); field work favors whole-node swaps with limited FRU replacements (example: fans).

- Primary communications with these customers are via Slack; urgent issues move to live calls; tickets are tracked in Salesforce for Customer Success and in Orion/Jira for vForce.

- Formal SLAs/SLOs exist for CoreWeave and xAI with legal penalties; an example cited was approximately a 30-minute response target for Sev1 incidents (needs confirmation with Gordon Brown).

- Staffing model includes weekday onsite coverage at xAI and after-hours coverage via APJ/EMEA; weekends are lighter but monitored, with a goal of proactive incident notification.

- Jason Vallery is VP of Cloud Product Management at VAST Data and previously spent 13 years at Microsoft focused on product management for Azure Blob Storage.



---

*Source: [[2025-10-29 - Jason introduced his cloud-first vision for VAST (VAST-as-a-Service, multi-cloud]]*