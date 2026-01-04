---
type: people
title: Vipin Sachdeva
created: '2026-01-03'
last_contact: '2025-10-31'
auto_created: true
tags:
- type/people
- needs-review
- company/microsoft
---

# Vipin Sachdeva

## Profile

**Role**: Microsoft
**Relationship**: Partner/customer-side contact (MAI within Microsoft ecosystem)

**Background**:
- MAI (ex-Inflection) contact; described as a strong VAST proponent; Koncha previously worked with him during Inflection.
- MAI-aligned; described as a strong VAST proponent; to be re-engaged to reopen MAI conversation and align with Kushal.

## Open Tasks

```dataview
TASK
FROM ""
WHERE !completed AND contains(text, "Vipin Sachdeva")
SORT due ASC
```

## Recent Context

- 2025-10-31: [[2025-10-31 - Jason (now at VAST) and Kushal discussed deploying VAST for Apollo’s training wo]] - 1:1 between Jason Vallery (VAST Data) and Kushal Datta (Microsoft Apollo) to evaluate deploying VAST... (via Kushal Datta)
- 2025-10-29: [[2025-10-29 - Jason introduced his cloud-first vision for VAST (VAST-as-a-Service, multi-cloud]] - 1:1 between Jason Vallery and Rick Haselton covering Jason’s cloud-first VAST-as-a-Service vision an... (via Rick Haselton)
- 2025-10-28: [[2025-10-28 - Discussed Microsoft AI (MAI) landscape, Falcon capacity rollout, and Azure dynam]] - Weekly 1:1 between Jason Vallery and Alon Horev aligning on Microsoft AI (MAI) dynamics, Falcon capa... (via Alon Horev)
- 2025-10-28: [[2025-10-28 - Jason and Koncha aligned on using MAI and UK Met Office as marquee wins to push]] - Weekly 1:1 between Jason Vallery and Kanchan Mehrotra ("Koncha") aligning on using MAI and UK Met Of... (via Kanchan Mehrotra)
- 2025-10-28: [[2025-10-28 - Jason and Kanchan aligned to pursue MAI and UK Met Office as flagship wins to un]] - Weekly 1:1 between Jason Vallery (VAST) and Kanchan Mehrotra (Microsoft) aligning on a dual-track pl... (via Kanchan Mehrotra)
- 2025-10-27: [[2025-10-27 - Jason and Kurt aligned on a go-to-market path to bring VAST’s high-density, lowe]] - Weekly 1:1 where Jason Vallery and Kurt Niebuhr aligned on a Microsoft Azure go-to-market path for V... (via Kurt Niebuhr)

## Key Facts

- MAI Falcon plan includes Phoenix, Dallas, and Richmond sites (~40k GPUs per site) connected by an AI WAN; initial tranche includes ~3 EB of Blob.
- MAI struggles to use Falcon capacity due to control plane fragility and GPU issues.
- OpenAI GPT-4.5 training reportedly took ~9 months across multi-islands and up to ~100k H100s; outcome described as disappointing, shifting away from ever-bigger clusters.
- MAI is exploring online RL continuous learning loops with ~60s feedback cycles (trainers in Phoenix, generators elsewhere).
- Vipin values VAST features (global namespace, quotas, capacity estimation, QoS) and acknowledges Blob cannot match VAST performance.
- Marketplace VM offers (Lsv4/v5) are not price-performance competitive for VAST at scale; hardware qualification is viewed as the long-term path.
- Azure Hardware qualification for first-party SKUs is a multi-year effort; liquid-cooled storage SKUs could help with data center cooling fungibility and late-binding storage vs GPU rack decisions.
- Blob API is largely Microsoft-specific; S3 compatibility is broadly attractive; multi-protocol (Blob + S3) could broaden appeal but faces Azure control plane integration hurdles.
- Azure LSV4 is a poor fit for VAST (too many cores, weak networking, low NVMe density) leading to poor cost/perf and sticker shock.
- LSV5 is committed by Egal’s team but roughly a year+ out; networking plans may still be insufficient for UK Met Office economics.

## Background

Vipin has over 23 years of experience in high-performance computing and AI. He joined Microsoft AI in March 2024. Prior to that, he served as a Member of Technical Staff at Inflection AI from September 2022 to March 2024, and as Head of HPC at Roivant Sciences from May 2021 to September 2022. His earlier roles include positions at IBM and academic research.

## Key Decisions

- ✅ Wait until Friday’s Kushal meeting before Alon follows up with Vipin.
- ✅ Prioritize Project Apollo as the first entry path over Azure marketplace SKUs.
- ✅ Use MAI success as the wedge to influence broader Azure storage strategy and hardware qualification.
- ✅ Treat Blob compatibility as exploratory; near-term emphasis remains on performance to keep GPUs utilized.
- ✅ Focus first on MAI and UK Met Office to create executive pull for a VAST-suitable Azure hardware shape.
- ✅ Pursue a dual track: ship marketplace offers while driving a leadership-backed hardware path.
- ✅ Defer broad sales pushes until a credible Azure product/SKU path exists.
- ✅ Near-term focus on MAI and UK Met Office over broad sales motion.
- ✅ Pursue a dual-track: marketplace listing plus flagship customer escalations.
- ✅ Use Nidhi to re-energize internal advocacy once the story and offer are ready.

## Related Customers

- [[Microsoft]]

## Related Projects

- [[VAST on Azure Integration]]
- [[Cloud]]

## Related

---
*Last updated: *
