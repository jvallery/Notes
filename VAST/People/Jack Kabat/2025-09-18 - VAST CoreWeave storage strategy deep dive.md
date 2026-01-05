---
type: people
title: VAST/CoreWeave storage strategy deep dive
date: '2025-09-18'
person: Jack Kabat
participants:
- Jack Kabat
- Jason Vallery
source: transcript
source_ref: Inbox/_archive/2026-01-04/2025-09-18 - Jason outlined his new architect
  remit to assess VAST and CoreWeave strategies,.md
tags:
- type/customer
- account/jack-kabat
- generated
---

# VAST/CoreWeave storage strategy deep dive

**Date**: 2025-09-18
**Account**: [[Jack Kabat]]
**Attendees**: Jack Kabat, Jason Vallery

## Summary

Jason described his new architect remit (carved out by Manish) to assess VAST and CoreWeave strategies, NVIDIA DGX-driven direction, and gaps in Azure’s storage stack, with Project Apollo likely in scope. They compared VAST’s global namespace/strong consistency (DataSpaces) and GPU-adjacent flash approach versus OpenAI’s local NVMe-on-GPU-hosts plus blob pattern (e.g., Fairwater), and agreed Azure needs a layered, OpenAI-independent capability set.
## Action Items
- [ ] Conduct deep dive on VAST and CoreWeave strategies/capabilities, NVIDIA alignment, and Azure storage gaps; propose a direction. @Myself 📅 2025-10-26 ⏫ #task #proposed
- [ ] Evaluate storage architecture options (VAST-style GPU-adjacent flash/global namespace vs OpenAI local NVMe + blob) and recommend a layered approach for Azure scale, including global namespace/consistency needs beyond OpenAI IP. @Myself 📅 2025-10-26 ⏫ #task #proposed
- [ ] Identify and engage internal VAST SMEs (including the contact referred to as "Khan Channel") and gather insights/materials. @Myself 📅 2025-10-27 ⏫ #task #proposed
- [ ] Assess Project Apollo implications and integration points with the proposed storage strategy. @Myself 📅 2025-10-26 ⏫ #task #proposed
- [ ] Schedule a follow-up with Jack to review findings and recommendations. @Myself 📅 2025-10-26 ⏫ #task #proposed
- [ ] Share correct contact details for the internal VAST SME ("Khan Channel") and any relevant offsite notes. @Jack 📅 2025-10-26 🔽 #task #proposed
- [ ] Provide context on UK Met Office Gen 2 and its relation to VAST engagements. @Jack 📅 2025-10-27 🔽 #task #proposed
- [ ] Check with NVIDIA contact Vlad for current DGX Cloud storage deployment patterns relevant to Azure strategy. @Jack 📅 2025-10-27 🔽 #task #proposed

## Decisions
- Jason will proceed with a VAST/CoreWeave strategy deep dive as his first task in the new architect role.
- Azure should pursue a layered storage approach and develop global namespace/consistency capabilities that are independent of OpenAI’s proprietary sync IP.

## Key Information
- Jason returned from a 3-month sabbatical and moved into an architect role carved out by Manish.
- CoreWeave positions VAST as preferred storage but built its own object storage to avoid full vertical coupling.
- NVIDIA is pushing DGX architecture and hardware-level optimizations and relies on storage partners (not a storage company).
- OpenAI’s pattern uses local NVMe on GPU hosts with lazy movement to/from blob; Fairwater is an example.
- OpenAI’s global/regional synchronization is proprietary IP built atop Azure data movement; Azure lacks this as a native storage primitive.
- VAST DataSpaces provides a global namespace with cross-region data locking and strong consistency; VAST focuses on high-performance flash rather than cheap-and-deep HDD storage.
- Azure’s 70+ regions and convergence of training and inference increase the need for distributed consistency and layered storage design.
- There is concern Microsoft’s storage maturity and execution speed may leave it vulnerable to commoditization by NVIDIA’s roadmap.
- Project Apollo introduces uncertainty (potential innovation path vs duplicative effort).

---

*Source: [[Inbox/_archive/2025-09-18/2025-09-18 - Jason outlined his new architect remit to assess VAST and CoreWeave strategies,.md|2025-09-18 - Jason outlined his new architect remit to assess VAST and CoreWeave strategies,]]*

## Related

- [[Jason Vallery]]
- [[CoreWeave]]
- [[Microsoft]]
- [[Oracle]]
- [[NVIDIA]]
- [[Fairwater]]
- [[Project Apollo]]