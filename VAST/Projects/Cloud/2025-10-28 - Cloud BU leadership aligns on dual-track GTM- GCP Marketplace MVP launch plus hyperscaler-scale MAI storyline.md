---
type: "projects"
title: "Cloud BU leadership aligns on dual-track GTM: GCP Marketplace MVP launch plus hyperscaler-scale MAI storyline"
date: "2025-10-28"
project: ""
participants: ["Jason Vallery", "Asaf Levy", "Eirikur Hrafnsson", "Jonsi Stephenson", "Kirstin Bordner", "Lior Genzel", "Ronnie Lazar", "Brian Moore", "Shachar", "Sahar", "Jeff Denworth", "Tiffany", "Olivia", "Ronald Cohen", "Kushal Datta", "John Downey"]
source: "transcript"
source_ref: "/Users/jason.vallery/Documents/Notes/Sources/Transcripts/2026/2025-10-28 - Cloud BU leadership aligned on a dual-track strategy (1) ship GCP MVP via marke.md"
tags:
  - "type/projects"
  - "project/"
  - "generated"

---

# Cloud BU leadership aligns on dual-track GTM: GCP Marketplace MVP launch plus hyperscaler-scale MAI storyline

**Date**: 2025-10-28
**Project**: [[]]
**Attendees**: Jason Vallery, Asaf Levy, Eirikur Hrafnsson, Jonsi Stephenson, Kirstin Bordner, Lior Genzel, Ronnie Lazar, Brian Moore, Shachar, Sahar, Jeff Denworth, Tiffany, Olivia, Ronald Cohen, Kushal Datta, John Downey

## Summary

Cloud BU leadership aligned on a dual-track strategy: ship the GCP MVP via marketplace with strong collateral and demos, while simultaneously pursuing hyperscaler-scale opportunities (notably Microsoft MAI) with a hardware-optimized story and Polaris-managed operations. The team flagged urgent gaps in product marketing collateral, demo readiness for Supercomputing, and operational readiness (QA, support, maintenance handling) as the top launch risks.


## Action Items


- [?] Share the GCP performance Excel and introduce Jason Vallery to the GCP performance lead and the product marketing owner for the field performance calculator. @Lior Genzel 📅 2025-10-29 ⏫ #task #proposed #auto

- [?] Push Product Marketing to deliver GCP MVP collateral (customer deck, internal training deck, CSP seller deck, battlecards, datasheets) and share the latest deck draft with Cloud BU leadership. @Brian Moore 📅 2025-10-31 ⏫ #task #proposed #auto

- [?] Review GCP MVP and MAI decks and positioning, and propose a standardized performance and TCO benchmark framework for apples-to-apples comparisons across clouds and instance types. @Myself 📅 2025-10-31 ⏫ #task #proposed #auto

- [?] Schedule and run an internal working session with the Enscale technical team to refine the Microsoft MAI storyline and architecture. @Asaf Levy 📅 2025-10-29 ⏫ #task #proposed #auto

- [?] Deliver a Microsoft MAI presentation package (storyline, solution diagram, deck) aligned to a Kubernetes-led control plane (Project Apollo) and Polaris-managed operations. @TBD 📅 2025-10-31 ⏫ #task #proposed #auto

- [?] Meet with Microsoft MAI contact Kushal Datta to align on requirements and next steps for the MAI opportunity. @Myself 📅 2025-10-31 ⏫ #task #proposed #auto

- [?] Reconnect Product Marketing with Jason Vallery and Jonsi Stephenson and include Polaris and marketplace content requirements in the collateral plan. @Lior Genzel 📅 2025-10-29 ⏫ #task #proposed #auto

- [?] Implement the GCP MVP deployment flow using routable IPs and require a customer-provided IP range as an input to deployment. @Eirikur Hrafnsson 📅 2025-10-28 ⏫ #task #proposed #auto

- [?] Kick off Salesforce integration for marketplace transaction flow and data synchronization for the GCP marketplace offer. @TBD 📅 2025-10-29 #task #proposed #auto

- [?] Tune GCP marketplace private offer components and pricing, and confirm that an existing blanket private offer can be used without new approval cycles. @John Downey 📅 2025-11-01 #task #proposed #auto

- [?] Harden maintenance handling for GCP MVP (for example VM migration and serialization) and validate behavior across GCP failure domains for HA. @Ronnie Lazar 📅 2025-10-28 ⏫ #task #proposed #auto

- [?] Ramp QA and support playbooks for GCP MVP, including break-glass procedures for deployment and operations. @Shachar 📅 2025-10-28 ⏫ #task #proposed #auto

- [?] Produce an end-to-end GCP demo video showing deployment via Polaris CLI and Polaris UI and the final deployed state for Supercomputing and CSP booth demos. @TBD 📅 2025-10-28 ⏫ #task #proposed #auto

- [?] Clarify licensing and packaging for Polaris when offered as a managed service (VAST-as-a-Service) to neoclouds. @TBD 📅 2025-10-28 #task #proposed #auto

- [?] Ensure any Enscale or Nscale resale preserves VAST feature and control exposure and avoids CoreWeave-style lock-in. @Myself 📅 2025-10-28 ⏫ #task #proposed #auto

- [?] Ask Google for guidance on maintenance overlap guarantees across failure domains and document the recommended operational approach for HA. @Eirikur Hrafnsson 📅 2025-10-28 #task #proposed #auto

- [?] Report out from the Friday Microsoft MAI session and align next steps across Cloud BU leadership. @Asaf Levy 📅 2025-11-03 ⏫ #task #proposed #auto

- [?] Finalize two collateral tracks (enterprise and marketplace, plus hyperscaler-scale) and distribute to the field organization. @Brian Moore 📅 2025-11-04 ⏫ #task #proposed #auto

- [?] Confirm GCP marketplace offer activation and readiness for private offers. @John Downey 📅 2025-11-05 #task #proposed #auto

- [?] Revisit the Google SaaS Runtime option for improved preflight checks and testing after the GCP MVP launch. @TBD 📅 2025-10-28 🔽 #task #proposed #auto




## Decisions


- Pursue a dual-track go-to-market strategy: ship the GCP MVP via marketplace for enterprise adoption while also pursuing hyperscaler-scale first-party engagements (for example Microsoft MAI) with a hardware-optimized story and Polaris-managed operations.

- Use routable IPs for the GCP MVP deployment model, and defer alias IPs and a Google SaaS Runtime approach until after MVP launch.

- Adapt the Enscale solution deck for Microsoft MAI positioning, emphasizing a Kubernetes-led control plane (Project Apollo) and Polaris for lifecycle management.

- Avoid CoreWeave-style lock-in in any Enscale or Nscale resale arrangement by retaining VAST feature and control exposure contractually and technically.




## Key Information


- Cloud BU leadership agreed to a dual-track go-to-market strategy: (1) ship the GCP MVP via cloud marketplace for enterprise burst use cases, and (2) pursue hyperscaler-scale first-party engagements such as Microsoft MAI with a hardware-optimized story and Polaris-managed operations.

- The GCP MVP networking approach will use routable IPs, and the deployment flow must collect a customer-provided IP range.

- Product Marketing assigned a person named Brian to create GCP MVP collateral (customer deck, internal training deck, CSP seller deck, battlecards, datasheets), but progress has been slow and collateral quality is currently not acceptable for field use.

- Supercomputing conference requires an end-to-end demo video showing GCP deployment via Polaris CLI and Polaris UI, including the final deployed state, for VAST's booth and shared Google and Microsoft booth presentations.

- Jonsi Stephenson stated he would be in Orlando and is handing over for November 17, then attending Microsoft Ignite from 2025-11-18 to 2025-11-21, then AWS re:Invent from 2025-12-01 to 2025-12-05, and expects Jason Vallery and Jeff Denworth to visit Iceland on 2025-12-08.



---

*Source: [[2025-10-28 - Cloud BU leadership aligned on a dual-track strategy (1) ship GCP MVP via marke]]*