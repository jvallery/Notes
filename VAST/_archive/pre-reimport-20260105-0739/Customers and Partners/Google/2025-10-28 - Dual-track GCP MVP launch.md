---
type: customer
title: Dual-track GCP MVP launch
date: '2025-10-28'
account: Google
participants:
- Jason Vallery
- Asaf Levy
- Eirikur Hrafnsson
- Jonsi Stefansson
- Kirstin Bordner
- Lior Genzel
- Ronnie Lazar
source: transcript
source_ref: Inbox/_archive/2026-01-04/2025-10-28 - Cloud BU leadership aligned on
  a dual-track strategy (1) ship GCP MVP via marke.md
tags:
- type/customer
- account/google
- generated
---

# Dual-track GCP MVP launch

**Date**: 2025-10-28
**Account**: [[Google]]
**Attendees**: Jason Vallery, Asaf Levy, Eirikur Hrafnsson, Jonsi Stefansson, Kirstin Bordner, Lior Genzel, Ronnie Lazar

## Summary

Cloud BU leadership aligned on a dual-track go-to-market: (1) ship the GCP MVP via marketplace with strong collateral and demos, and (2) pursue hyperscaler-scale opportunities (notably Microsoft/MAI) with a hardware-optimized story and Polaris-managed operations. Key blockers are collateral readiness, QA/support and break-glass procedures, deployment preflight variability, and maintenance/HA handling across failure domains. The team confirmed GCP MVP networking will use routable IPs (customer-provided range) and will proceed with marketplace activation while tuning private offer pricing components.
## Action Items
- [?] Share GCP performance Excel and introduce Jason to the performance lead and product marketing owner for the field sizing calculator @Lior Genzel Genzel 📅 2025-10-29 ⏫ #task #proposed
- [?] Push Product Marketing to deliver customer, internal, and CSP seller decks plus battlecards/datasheets; share latest deck @Brian Moore 📅 2025-10-31 ⏫ #task #proposed
- [?] Review decks/positioning and propose a standard performance/TCO benchmark frame across clouds @Myself 📅 2025-10-31 ⏫ #task #proposed
- [?] Schedule and run internal working session with Enscale technical team to refine the MAI storyline and architecture @Asaf Levy 📅 2025-10-29 ⏫ #task #proposed
- [?] Deliver MAI presentation (storyline, solution diagram, deck) aligned to Kubernetes-led control plane and Polaris @Cloud BU engineering 📅 2025-10-31 🔺 #task #proposed
- [?] Meet with MAI’s Kushal Datta to align on requirements and next steps @Myself 📅 2025-10-31 ⏫ #task #proposed
- [?] Reconnect Product Marketing with Jason/Jonsi and include Polaris/marketplace content requirements @Lior Genzel Genzel 📅 2025-10-29 ⏫ #task #proposed
- [?] Implement GCP MVP deployment flow using routable IPs and require customer-provided IP range @Eirikur Hrafnsson ⏫ #task #proposed
- [?] Kick off Salesforce integration for marketplace transaction flow and data sync @Cloud BU ops 📅 2025-10-29 ⏫ #task #proposed
- [?] Tune GCP marketplace private offer components and pricing; confirm no new approvals needed @John Downey 📅 2025-11-01 ⏫ #task #proposed
- [?] Report out from Friday’s Microsoft/MAI session and align next steps @Asaf Levy 📅 2025-11-03 ⏫ #task #proposed
- [?] Finalize two collateral tracks (enterprise/marketplace and hyperscaler-scale) and distribute to field @Brian Moore 📅 2025-11-04 ⏫ #task #proposed
- [?] Confirm GCP marketplace offer activation and readiness for private offers @John Downey 📅 2025-11-05 ⏫ #task #proposed

## Decisions
- Pursue a dual-track go-to-market: marketplace offer for enterprise bursts plus targeted hyperscaler-scale engagements (e.g., Microsoft/MAI).
- Use routable IPs for the GCP MVP; defer alias IPs/SaaS Runtime until post-launch.
- Adapt Enscale solution/deck for Microsoft/MAI with Kubernetes-led control plane and Polaris emphasis.
- Retain contractual control to avoid CoreWeave-style feature/control lock-out in any Nscale/Enscale resale.

## Key Information
- GCP MVP is close to launch; demos are needed for Supercomputing and CSP booths.
- Collateral gap persists: customer/internal/CSP decks, battlecards, and datasheets are not ready; Product Marketing owner is Brian.
- Performance data exists for GCP v1 (~90% theoretical read; ~50–60% write), but standardized KPIs are not defined.
- GCP MVP networking will use routable IPs; customer must provide an IP range.
- Marketplace plan: leverage an existing blanket private offer to avoid new approvals; pricing components still need tuning.
- Maintenance/HA approach in GCP relies on scheduled maintenance, VM migration/serialization; GCP has 8 failure domains; Azure typically 3.
- MAI opportunity discussed at ~160,000 GPUs; Microsoft team requested VAST guidance; follow-up planned for Friday.
- Polaris is required for lifecycle management in both tracks to avoid value abstraction by neocloud operators/resellers.
- Supercomputing presence includes VAST booth plus Google and Microsoft booths; ~10 end-user cloud meetings planned.
- Key event dates cited: Ignite 2025-11-18 to 2025-11-21; re:Invent 2025-12-01 to 2025-12-05; planned Iceland trip 2025-12-08.

---

*Source: [[Inbox/_archive/2025-10-28/2025-10-28 - Cloud BU leadership aligned on a dual-track strategy (1) ship GCP MVP via marke.md|2025-10-28 - Cloud BU leadership aligned on a dual-track strategy (1) ship GCP MVP via marke]]*

## Related

- [[Microsoft]]
- [[Amazon]]
- [[Oracle]]
- [[CoreWeave]]
- [[Jason Vallery]]
- [[Asaf Levy]]
- [[Eirikur Hrafnsson]]
- [[Jonsi Stephenson]]
- [[Kirstin Bordner]]
- [[Lior Genzel]]
- [[Ronnie Lazar]]
- [[John Downey]]
- [[Brian Moore]]
- [[Jeff Denworth]]
- [[Tiffany Stonehill]]
- [[Olivia Bouree]]
- [[Ronen Cohen]]
- [[Timo Pervane]]
- [[Frank Ray]]
- [[Kishore Inampudi]]
- [[Jan Niemus]]
- [[Qi Ke]]
- [[David Holz]]
- [[Rob Banga]]
- [[Enscale deck]]
- [[Cloud control plane]]
- [[OpenAI VAST POC - CoreWeave Cluster]]