---
type: "projects"
title: "Cloud BU leadership aligns on dual-track GTM: GCP Marketplace MVP plus hyperscaler-scale MAI story"
date: "2025-10-28"
project: ""
participants: ["Jason Vallery", "Asaf Levy", "Eirikur Hrafnsson", "Jonsi Stephenson", "Kirstin Bordner", "Lior Genzel", "Ronnie Lazar", "Brian Moore", "TBD (Unknown participant labeled \"Remote\")"]
source: "transcript"
source_ref: "/Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-10-28 - Cloud BU leadership aligned on a dual-track strategy (1) ship GCP MVP via marke.md"
tags:
  - "type/projects"
  - "project/"
  - "generated"

---

# Cloud BU leadership aligns on dual-track GTM: GCP Marketplace MVP plus hyperscaler-scale MAI story

**Date**: 2025-10-28
**Project**: [[]]
**Attendees**: Jason Vallery, Asaf Levy, Eirikur Hrafnsson, Jonsi Stephenson, Kirstin Bordner, Lior Genzel, Ronnie Lazar, Brian Moore, TBD (Unknown participant labeled "Remote")

## Summary

Cloud BU leadership aligned on a dual-track strategy: ship the GCP Marketplace MVP with strong collateral and demos, while also pursuing hyperscaler-scale opportunities like Microsoft MAI with a hardware-optimized story and Polaris-managed operations. Engineering confirmed the GCP MVP will use routable IPs and highlighted QA/support readiness, deployment validation, and maintenance handling across failure domains as key risks.


## Action Items


- [?] Share the GCP performance Excel and introduce Jason Vallery to the performance lead and the Product Marketing owner for the field sizing calculator. @Lior Genzel 📅 2025-10-29 ⏫ #task #proposed #auto

- [?] Push Product Marketing to deliver customer, internal enablement, and CSP seller decks plus battlecards and datasheets for the GCP Marketplace MVP; share the latest deck draft with Cloud BU leadership. @Brian Moore 📅 2025-10-31 ⏫ #task #proposed #auto

- [?] Review Cloud BU decks and positioning and propose a standardized performance and TCO benchmark framework for apples-to-apples comparisons across clouds and instance types. @Myself 📅 2025-10-31 ⏫ #task #proposed #auto

- [?] Schedule and run an internal working session with the Enscale technical team to refine the Microsoft MAI storyline and architecture. @Asaf Levy 📅 2025-10-29 ⏫ #task #proposed #auto

- [?] Deliver a Microsoft MAI presentation package (storyline, solution diagram, and deck) aligned to a Kubernetes-led control plane (Project Apollo) and Polaris-managed operations. @TBD 📅 2025-10-31 ⏫ #task #proposed #auto

- [?] Meet with Microsoft MAI PM lead Kushal Datta to align on requirements and next steps for the MAI opportunity. @Myself 📅 2025-10-31 ⏫ #task #proposed #auto

- [?] Reconnect Product Marketing with Jason Vallery and Jonsi Stephenson and include Polaris and marketplace content requirements in the collateral plan. @Lior Genzel 📅 2025-10-29 ⏫ #task #proposed #auto

- [?] Implement the GCP MVP deployment flow using routable IPs and require a customer-provided IP range as an input to deployment. @Eirikur Hrafnsson 📅 2025-10-28 ⏫ #task #proposed #auto

- [?] Kick off Salesforce integration for marketplace transaction flow and data synchronization for Cloud Marketplace operations. @TBD 📅 2025-10-29 #task #proposed #auto

- [?] Tune GCP Marketplace private offer components and pricing and confirm that no new approvals are required due to an existing blanket private offer. @TBD 📅 2025-11-01 #task #proposed #auto

- [?] Harden maintenance handling for GCP MVP (VM migration and serialization) and validate behavior across GCP failure domains to protect HA and performance. @Ronnie Lazar 📅 2025-10-28 ⏫ #task #proposed #auto

- [?] Ramp QA and support playbooks for the GCP MVP, including break-glass procedures for deployment and operational incidents. @TBD 📅 2025-10-28 ⏫ #task #proposed #auto

- [?] Produce an end-to-end GCP demo video showing deployment via Polaris CLI and Polaris UI and the final deployed state for Supercomputing and CSP booth demos. @TBD 📅 2025-10-28 ⏫ #task #proposed #auto

- [?] Clarify licensing and packaging for Polaris when offered as a managed service (VAST-as-a-Service) to neoclouds. @TBD 📅 2025-10-28 #task #proposed #auto

- [?] Ensure any Enscale or neocloud resale model preserves VAST feature and control exposure and avoids CoreWeave-style lock-in. @Myself 📅 2025-10-28 ⏫ #task #proposed #auto

- [?] Ask Google for guidance on whether scheduled maintenance can overlap across failure domains and document the recommended operational approach for the GCP MVP HA design. @Eirikur Hrafnsson 📅 2025-10-28 #task #proposed #auto

- [?] Report out from the Friday Microsoft MAI session and align next steps across Cloud BU leadership and engineering. @Asaf Levy 📅 2025-11-03 ⏫ #task #proposed #auto

- [?] Finalize two collateral tracks (enterprise and marketplace collateral, plus hyperscaler-scale collateral) and distribute to the field organization. @Brian Moore 📅 2025-11-04 ⏫ #task #proposed #auto

- [?] Confirm GCP Marketplace offer activation and readiness for private offers. @TBD 📅 2025-11-05 #task #proposed #auto

- [?] Revisit the Google SaaS Runtime option post-MVP to improve preflight checks and deployment testing for customer environment variability. @TBD 📅 2025-10-28 🔽 #task #proposed #auto




## Decisions


- Adopt a dual-track go-to-market strategy: ship the GCP Marketplace MVP for enterprise adoption while simultaneously pursuing hyperscaler-scale first-party opportunities such as Microsoft MAI with a hardware-optimized story and Polaris-managed operations.

- Use routable IPs for the GCP MVP and require customers to provide an IP range during deployment; defer alias IPs and any Google SaaS Runtime approach until after MVP launch.

- Adapt the Enscale solution deck and storyline for Microsoft MAI, emphasizing a Kubernetes-led control plane (Project Apollo) and Polaris for lifecycle management.

- Avoid CoreWeave-style lock-in in any Enscale or neocloud resale model by preserving VAST feature and control exposure.




## Key Information


- Cloud BU leadership agreed to a dual-track go-to-market: (1) ship the Google Cloud Platform (GCP) Marketplace MVP for enterprise and marketplace-driven adoption, and (2) pursue hyperscaler-scale first-party opportunities such as Microsoft AI Infrastructure (MAI) with a hardware-optimized story and Polaris-managed operations.

- The GCP Marketplace MVP is close to launch, but the team lacks field-ready collateral (customer deck, internal enablement deck, CSP seller deck, battlecards, datasheets). Product Marketing owner Brian Moore has produced an initial v1 deck and started battlecards, but progress is slow.

- Engineering confirmed the GCP MVP networking approach will use routable IPs, and the deployment flow must collect a customer-provided IP range.

- The team needs an end-to-end GCP demo video showing deployment via Polaris CLI and Polaris UI plus the final deployed state, for Supercomputing and for shared booth presentations with Google and Microsoft.

- Performance data exists for the GCP v1 implementation, approximately 90% of theoretical read performance and 50-60% write performance, but the team has not defined standardized KPIs for field messaging or cross-cloud comparisons.

- The MAI opportunity discussed is on the order of approximately 160,000 GPUs, and Microsoft is asking for VAST guidance; a Friday follow-up session was planned to advance the storyline and architecture.

- Supercomputing conference presence includes a VAST booth plus participation in Google and Microsoft booths, and the team expects about 10 end-user meetings focused on cloud.

- Maintenance and high availability planning for GCP MVP assumes Google scheduled maintenance only, with handling via VM migration and serialization; GCP has 8 failure domains while Azure typically has 3, which impacts redundancy and usable capacity planning.

- Marketplace activation is expected to leverage an existing blanket private offer to avoid new approvals, but pricing components still need tuning.

- Key dates referenced: Microsoft Ignite runs 2025-11-18 to 2025-11-21; AWS re:Invent runs 2025-12-01 to 2025-12-05; a planned Iceland trip was discussed for 2025-12-08.



---

*Source: [[2025-10-28 - Cloud BU leadership aligned on a dual-track strategy (1) ship GCP MVP via marke]]*