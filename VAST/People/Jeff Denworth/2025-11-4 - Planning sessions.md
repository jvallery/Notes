

### Session 1 — **

- Northstar & vision
- Program charter & decision rights (get you the “pen” and the authority)**


1. **North Star & scope of ambition** - Agree the 1/3/5 year product vision and what _not_ to build in the next 12 months.
    
2. **Cloud‑first strategy & sequencing** - Confirm we are not “lift & shift”; Discuss the crawl‑walk‑run approach and backlog.
    
3. **MAI/Apollo  & Azure path** - Decide the single‑threaded owner(s), success criteria, and the attack plan for the next 90 days.
    
4. **SaaS/tenancy, pricing & obligations** - Align on data custodian responsibilities, SLO/SLAs, and legal/compliance work which need to be considered.
    
5. **Org model, decision rights & ROB** - Given above, confirm my scope, team shape, decision matrix, and the cadence I’ll own. 
    
6. **Resourcing & goals** - Secure headcount/budget; commit to 30/60/90 outcomes.
    
7. **Risk review & objection handling** (15–20m) → Agree mitigations and communication plan.
    

---

## 2) Session detail pages (for your notes)

### Session A — North Star & scope of ambition

**Points to land**

- _“Neocloud‑in‑a‑box”_ = repeatable foundation for GPU‑dense, single‑tenant sites and select non‑Azure DCs; **software‑first, hardware‑flexible**, liquid‑cooling‑friendly.
    
- Prioritize **core layers** over **opinionated higher‑layer services** (Insight/Agent engines) until base is proven at scale; avoid “taste” lock‑in and fractured value props.
    
- Set time horizons: **0–12 months** (wedge wins + reliability), **12–36** (Azure hardware & control‑plane integrations, multi‑site repeatability), **36–60** (operational automation; AI‑operated fleet).
    

**Discuss**

- What does “win” look like in 12 months (# of Apollo‑style sites, GPU utilization, $ ARR tied to VAST as storage standard)?
    
- What we will _not_ do this year (avoid building fully opinionated app layers too early).
    

**Decisions to make**

- Approve the vision statement + scope boundaries.
    
- Endorse **core‑first** prioritization for FY26.
    
- Name the top 3 proof‑points we must hit this year.
    

**Receipts / quotes to use from your convos**

- Vipin values **global namespace, quotas, capacity estimation, QoS**; “**Blob can’t match VAST performance**.”
    
- Marketplace VMs (Lsv4/v5) are **not** price/perf competitive at scale; **software‑first + ODM liquid‑cooled options**are attractive.
    
- “Use **MAI success as the wedge**; treat Blob compatibility as exploratory; focus on **GPU‑utilizing performance wins now**.”
    

**Notes:** ___

---

### Session B — Cloud‑first strategy & sequencing (not lift‑and‑shift)

**Points to land**

- Current cloud plan risks being a **lift‑and‑shift** of the box product. We need **cloud primitives** and a new control‑plane stance (AKS/Apollo‑aligned) with clear **tenancy, operability, and SLOs**.
    
- Adopt **Working Backwards** artifacts (PR/FAQ + 6‑pager) for “VAST Cloud” and “VAST in Apollo”. (PR/FAQ is a proven Amazon mechanism to force clarity before build. )
    

**Discuss**

- Crawl → Walk → Run:
    
    - **Crawl:** Private offer / single‑tenant deployments; thin control plane; basic tenancy; perf & reliability SLOs; observability
        
    - **Walk:** Public offer (customer‑tenant); hardened ops, cost telemetry, upgrade path; limited first‑party integrations
        
    - **Run:** Public SaaS (VAST‑tenant); billing, quotas, audit/forensics, D/R plans, compliance baselines
        
- Gating: do not advance stages without meeting **error‑budget‑backed SLOs** and runbooks (per Google SRE best practice on SLIs/SLOs/error budgets).
    

**Decisions to make**

- Approve the **staged plan** and SLO gates.
    
- Green‑light PR/FAQ drafts and the initial 6‑pager owners.
    

**Receipts / quotes to use**

- “Azure Storage lacks a deployable solution for Apollo‑like sites today; AKS exploring a **thin VAST control plane/topology**.”
    
- “MAI Falcon first tranche came online with **~3 EB Blob** but is struggling due to **control‑plane fragility & GPU issues**.”
    
- “**Marketplace** offers won’t be the win path at scale.”
    

**Notes:** ___

---

### Session C — MAI/Apollo wedge & Azure strategy

**Points to land**

- Treat MAI success as the **lighthouse**; use Apollo to standardize VAST as storage for single‑tenant GPU sites.
    
- Long‑game: Azure hardware qualification via **Ronnie Borker** path; align with **liquid‑cooled storage SKUs** for DC fungibility.
    

**Discuss**

- Single‑threaded owners across **MAI (Kushal/Vipin)**, **AKS/Apollo (Anson/Keek)**, **Azure Hardware**.
    
- Multi‑protocol head (S3 + Blob) as **exploratory**; near‑term center of gravity remains **perf** and GPU utilization.
    
- Success metrics: time‑to‑first‑IO, sustained read/write throughput, **GPU idle time reduction**, cutover time, site recovery time.
    

**Decisions to make**

- Name the **VAST single‑threaded owner** for MAI & Apollo motions (I can be that owner on product/alliances side).
    
- Commit to the 30/60/90 below and define the exec sponsor on Microsoft side.
    

**30/60/90 (proposal)**

- **30 days:** Joint success criteria + test plan; thin control‑plane topology proposal; perf targets; executive alignment.
    
- **60 days:** Site POC live with measurable perf; decision on liquid‑cooled storage SKU exploration with ODM.
    
- **90 days:** Written **scale plan** for first production site; Go/No‑Go on expanding to 2–3 additional sites.
    

**Notes:** ___

---

### Session D — SaaS/tenancy, pricing & obligations

**Points to land**

- Moving to VAST‑operated deployments changes us into **data custodian** for some tenants: we need clear **shared‑responsibility**, **SLO vs SLA** definitions, runbooks, and pricing that covers ops burden (see AWS/Azure shared‑responsibility models for reference framing).
    
- Build once: tenancy model, incident/severity model, on‑call, audit, and cost telemetry apply across offers.
    

**Discuss**

- **SLOs/SLAs:** user‑visible SLIs, error budgets, escalation policies; **pricing** aligned to the ops cost curve.
    
- **Compliance baselines:** logging, IAM, key mgmt, audit trail; legal/EULA/DPAs; support contract shape.
    
- **Operational tooling:** cost/usage metering, ticketing hooks, observability, incident review template.
    

**Decisions to make**

- Minimum SLO set & error budgets; agree we will gate GA on SLO conformance.
    
- Staff a **Product Ops/Readiness** function to own runbooks, gates, and quality bars.
    

**Notes:** ___

---

### Session E — Org model, decision rights & ROB

**Points to land**

- Product must become the connective tissue: **Tel Aviv ↔ Iceland ↔ Field/Alliances**. Clear decision rights and a cadence that shortens the insight→delivery loop.
    
- Architects continue to own FRDs; **Product** owns the **why/priority**, **backlog**, **PR/FAQ**, **RICE scoring**, and **release gates**.
    
- Use **RAPID** to speed decisions and avoid churn; log every big call.
    

**Discuss**

- **RAPID** decision roles for major bets (Deciders, Recommenders, Input, etc.).
    
- **ROB I will run** (see section below) with quality gates (Design, Readiness, Release, Postmortem).
    

**Decisions to make**

- Approve my **areas of ownership** and the **ROB**.
    
- Approve **hiring plan** (TPMs/PMs, Product Ops, Tech Writer, Enablement).
    

**Notes:** ___

---

### Session F — Resourcing & first 100 days

**Points to land**

- The current PM:Dev ratio is unsustainably low; product lacks end‑to‑end ownership and technical depth in the middle of the lifecycle.
    
- My time will split between **customer/alliances** and **running the cadence**; team fills the backbone (backlog, artifacts, analytics).
    

**Discuss**

- **Team ask** (min viable): (a) 1–2 **Principal PMs** (Cloud Platform; Azure/MSFT), (b) 1 **TPM** (release/readiness), (c) 1 **Product Ops** lead, (d) 1 **Tech Writer**, (e) 1 **Sales/SE Enablement PM**.
    
- **First‑100‑day outcomes:** ROB live; PR/FAQ drafts; unified backlog with RICE; MSFT wedge 30/60/90 in motion; SLOs and runbooks baselined; first Decision Log complete.
    

**Decisions to make**

- Headcount/budget; recruiting lanes; what I should **stop** doing to create focus.
    

**Notes:** ___

---

### Session G — Risks & objections

**Known risks**

- Azure internal P&L politics (Compute vs Storage); long hardware‑qualification timelines.
    
- MAI control‑plane fragility could slow proof; timeline optimism in cloud work.
    
- Fragmentation risk if we over‑invest in opinionated higher‑layer services too early.
    

**Default responses**

- We are **core‑first**; use MAI/Apollo as the **lighthouse**. Decision rights + SLO gates prevent timeline drift.
    
- Azure long‑game: work the **hardware path** and “thin control plane” with AKS; stage proof with measurable GPU‑utilization gains.
    
- Product Ops and the ROB keep us predictable without killing throughput.
    

**Notes:** ___

---

## 3) Rhythm of Business (ROB) I will run

|Cadence|Purpose|Attendees|Content owner|Inputs|Key decisions|
|---|---|---|---|---|---|
|**Mon – WBR (45m)**|Product & Eng weekly business review|Jeff, Shachar, Alon, Yancey, Field/Alliances rep|**Product Ops**|KPI deck (perf, reliability SLOs, GPU util), top risks/blockers|Priority changes, unblockers, escalation|
|**Tue – RFE Triage (60m)**|Normalize/score inbound RFEs|PM leads + Architects + Support|**PM (Backlog)**|RICE worksheet, revenue signals, tech effort ranges|Accept/merge/park; owner & milestone|
|**Wed – Design Review (60m)**|Review FRDs/PRFAQs; enforce quality|Architects + PM + Security/Compliance|**Architects**(FRD), **PM**(PR/FAQ)|Draft FRD, PR/FAQ, threat model|Design sign‑off or re‑work|
|**Thu – Release Readiness (45m)**|Gate releases on SLO, docs, support|Eng leads + PM + Support + Docs|**TPM/PM**|SLO/error‑budget report; docs; support plan|Ship/No‑ship; mitigation|
|**Fri – Decision Council (30m)**|Rapid, documented calls on big bets|Jeff (D), Recommenders, Input roles|**Product Ops**|1‑pager, options, tradeoffs|Decision logged; owners; next steps|
|**Monthly – MBR (90m)**|Strategy/roadmap check & budget|ELT|**Head of Product**|KPI trends; roadmap burn‑down; hiring plan|Reallocation; re‑sequencing; funding|
|**Quarterly – PI/OKR Planning (½–1 day)**|Align cross‑teams; commit objectives|All leads|**Head of Product**|OKR draft; roadmap; capacity|Committed OKRs; capacity plan|

> **Quality gates** I will enforce: (1) **Design** (FRD/PRFAQ reviewed), (2) **Readiness** (SLO/runbooks, Docs, Support), (3) **Release** (error budget healthy), (4) **Postmortem** (blameless retro). (SLO/error‑budget practices from Google SRE.)

---

## 4) My scope & ownership (proposal)

- **Cloud Product & Platform Strategy** — North Star, staged plan, PR/FAQ, roadmap.
    
- **Microsoft/MAI/Apollo Product leadership** — single‑threaded product owner; coordinate AKS/Hardware path.
    
- **Product Operations & ROB** — cadence, artifacts, quality gates, **Decision Log** (using RAPID).
    
- **Backlog & Prioritization** — RICE scoring, epic formation, customer insight synthesis (RICE reference model).
    
- **SLOs & Readiness** — define SLIs/SLOs; ensure runbooks, pricing/ops alignment; ship/no‑ship governance.
    
- **Field/Alliances interface** — message discipline; enablement; bring voice of customer into prioritization.
    

---

## 5) Quotes & data points (for color in the room)

- “**Use MAI success as the wedge**; position VAST as **software‑first**; be open to **ODM hardware and liquid‑cooled**options.”
    
- “MAI Falcon plan: Phoenix, Dallas, Richmond; ~**40k GPUs per site**; first tranche with **~3 EB Blob**.”
    
- “MAI is **struggling to use Falcon** capacity due to control‑plane fragility and GPU issues.”
    
- Vipin: “**Global namespace, quotas, capacity estimation, QoS**,” and “**Blob can’t match VAST performance**.”
    
- “**Marketplace** VM offers (e.g., Lsv4/v5) are **not price‑performance competitive** at scale.”
    
- “Azure Storage lacks a deployable solution for **Apollo‑like** sites today; **AKS** exploring a **thin VAST control plane/topology**.”
    
- Shachar: Architects write **FRDs**; wants **stronger technical depth** + **end‑to‑end** product involvement; optimizes for **throughput over predictability**; three buckets: **tactical deals, strategic innovation, technical debt**.
    

---

## 6) First‑100‑days scorecard (fill in as we go)

- **Week 2:** ROB running; Decision Log created; PR/FAQ owners assigned.
    
- **Day 30:** Unified backlog w/ RICE; baseline SLOs + runbooks; MSFT wedge success criteria signed.
    
- **Day 60:** First Apollo/MAI POC live; first release gated on SLOs; enablement pack v1.
    
- **Day 90:** 2–3 lighthouse sites planned; postmortem discipline visible; hiring plan executing.
    

**KPIs:** GPU idle % ↓, sustained throughput ↑, time‑to‑first‑IO ↓, error‑budget burn rate, time‑to‑detect/restore, RICE throughput (# scored / month), decision latency.

---

## 7) Parking lot / notes

- …
    

---

## 8) References you can cite in the room

- **Working Backwards (PR/FAQ, 6‑pager)** — Amazon’s approach to force clarity before build; adapt it for “VAST Cloud” + “VAST in Apollo”.
    
- **RAPID** — decision role clarity to move fast with accountability; log big calls.
    
- **SLOs & error budgets** — reliability gating for ship/no‑ship; protect user experience.
    
- **Shared responsibility models** — articulate data custodian obligations as we operate services.
    

---

## 9) Open decisions I want from Jeff

1. Approve my **scope** (Section 4) and the **ROB** (Section 3).
    
2. Name the **single‑threaded owner** (product) for MAI/Apollo (I propose: me).
    
3. Green‑light **headcount** for PMs/TPM/Product Ops/Tech Writing/Enablement.
    
4. Endorse **core‑first** prioritization and staged cloud plan with SLO gates.
    
5. Agree to run **Working‑Backwards** artifacts for VAST Cloud + Apollo.
    

---

### Quick talk‑track reminders (for influence & scope)

- Anchor on outcomes: **GPU utilization, perf SLOs, time‑to‑first‑IO**—then show how the **ROB** + **decision rights**make that repeatable.
    
- Tie your scope to relieving Jeff’s load: single‑threaded owner for MAI/Apollo + run the cadence so he can focus on top deals and exec alignment.
    
- Use MAI/Apollo **as the wedge**, not the end state—keep the **hardware SKU** and **thin control plane** narrative visible as the long‑game.
    
- Keep “**core‑first**; defer ‘taste‑layer’ services” visible to avoid effort dilution and stakeholder fragmentation.
    

If you want, I can also drop a compact **1‑pager PR/FAQ skeleton** into the guide that you can fill live with Jeff.
- Scale demands **clear decision rights**. Propose **RAPID** for must‑move decisions (you = _Recommend/Drive_, Jeff = _Decide/Approve_), and **DACI** for product specs (you = _Driver_, Alon/Shachar = _Contributors_, Jeff = _Approver_). This reduces loop time and ambiguity. ([Harvard Business Review](https://hbr.org/podcast/2021/03/building-influence-without-authority?utm_source=chatgpt.com "Building Influence Without Authority"))
    
- Establish a lightweight **operating mechanism**: monthly “Cloud Business Review,” weekly 30‑min “Issue‑drilldown,” and a **one‑page decision memo** format (see Session 3).
    
- Map 5–7 recurring decision types (e.g., roadmap tradeoffs, release gates, interrupt policy, external commitments, Azure/Apollo moves).
    
- Define who **Decides** vs **Inputs** for each, using RAPID/DACI.
    

**Receipts**

- _Tomer:_ “We’re ~4 PMs for ~400 engineers; Cloud Design Qualifiers needed.”
    
- _Liraz:_ “I think it’s tribal knowledge; I didn’t write anything.” (Need explicit decision rights/process.)
    

### Session 3 — **Scope, themes, and 12‑month roadmap (PR‑FAQ + RICE)**

- Use a short **PR‑FAQ** to “work backwards” from the customer (MAI/Apollo + top cloud customers): 1‑page press release + FAQ makes the end‑state vivid, then we derive milestones. ([Mindtools](https://www.mindtools.com/an30xh5/robert-cialdini-six-principles-of-persuasion?utm_source=chatgpt.com "Robert Cialdini: Six Principles of Persuasion"))
    
- Prioritize with **RICE** (Reach, Impact, Confidence, Effort) so deal‑driven asks roll up to coherent epics, not one‑offs. ([Harvard Business Review](https://hbr.org/archive-toc/BR0109?utm_source=chatgpt.com "From the Magazine (October 2001)"))
    

- **P0 themes** you’ve heard repeatedly:
    
    1. **True multi‑tenancy** (tenant‑scoped config, quotas/QoS, data spaces aligned to tenants, per‑tenant auth beyond current limits).
        
    2. **Global namespace performance** (e.g., write leases) visible to GPU workloads.
        
    3. **Cloud design qualifiers**: the minimum set to declare “Cloud‑ready” for 5.6.
        
    4. **Observability & live site** (see Session 5).
        
- When 5.6 GA (“around July” per Eyal), what fits P0 vs P1 without slipping GA?
    

**Decisions**

- Approve **3–4 named epics** and **Cloud Design Qualifiers** that _must_ be in 5.6 (and what can wait).
    
- Bless the **PR‑FAQ** as the canonical pre‑read for execs and field.
    

**Receipts**

- _Eyal:_ “5.6 GA is around July … 5.5 didn’t include cloud‑critical items.”
    
- _Tomer:_ “Global namespace write leases preview in 5.5; multi‑tenancy is not yet thematic.”
    
- _Eyal:_ “Auth providers limited (8); configs not tenant‑scoped.”
    

---

### Session 4 — **Release discipline, support policy, & interrupt guardrails**

**Attendees:** Jeff; bring Eyal (release), Liraz (program), Shachar (as needed).  
**Points to land**

- Create simple **stage gates** with explicit **exit criteria** and agree to a **support/EOL policy** (e.g., “N & N–1 minors” or similar), to reduce chaos and prevent 5.4‑style instability.
    
- Adopt a “**two‑way door** vs **one‑way door**” lens for interrupts: most are Type‑2 (reversible)—bias to ship and iterate; reserve interrupts for Type‑1 (irreversible). ([SEC](https://www.sec.gov/Archives/edgar/data/1018724/000119312517120198/d373368dex991.htm?utm_source=chatgpt.com "EX-99.1"))
    

**Topics**

- **Code freeze vs Golden Run**—synchronize dates; define “red list” changes allowed during freeze.
    
- **Minor‑release churn**—cap concurrent trains; create a _deal‑override_ policy (what qualifies, who approves).
    
- **Support policy messaging** to field (and how we’ll say “no” with alternatives).
    

**Decisions**

- Approve **support/EOL policy** and publish date.
    
- Approve **release policy** (freeze, gates, interrupt rules) and the _deal‑override_ RAPID (who decides).
    

**Receipts**

- _Eyal:_ “Minor releases killed us … constant urgent requests.”
    
- _Liraz:_ “Golden Run/Code freeze misaligned.”
    

---

### Session 5 — **SaaS operations: SLOs, error budgets, live‑site, telemetry**

**Attendees:** Jeff (Approver), you (Driver), Ops/QA reps.  
**Points to land**

- Define **SLOs/SLIs** and **error budgets**; use them to gate feature velocity vs reliability—industry‑standard SRE practice. ([DevOps.com](https://devops.com/measuring-github-copilots-impact-on-engineering-productivity/?utm_source=chatgpt.com "Best of 2023: Measuring GitHub Copilot's Impact on ..."))
    
- Instrument the **four golden signals** (latency, traffic, errors, saturation) and basic call‑home telemetry for fleet health. ([DevOps.com](https://devops.com/measuring-github-copilots-impact-on-engineering-productivity/?utm_source=chatgpt.com "Best of 2023: Measuring GitHub Copilot's Impact on ..."))
    

**Topics**

- Which SLOs matter for GPU‑bound workloads (e.g., namespace throughput percentile, metadata latency, job‑blocking errors)?
    
- On‑call ownership, runbooks, and a weekly **Live‑Site Review**.
    

**Decisions**

- Approve **initial SLOs**, error budgets, and on‑call RACI (who pages whom).
    
- Approve a minimal **observability plan** for 5.6; phase 2 post‑GA.
    

---

### Session 6 — **AI‑accelerated engineering: deliver more with the same team**

**Attendees:** Jeff; invite Shachar to align on “how,” not “whether.”  
**Points to land**

- You’re not pushing a heavy COE; you’re proposing a **lightweight guild + quarterly enablement** to scale what’s already working (Cursor, log analysis, CI triage), focusing on **measured outcomes** (cycle time, bug aging), not vanity metrics.
    
- Cite credible data: GitHub observed **55% faster** task completion and 88% felt more productive with Copilot‑class tools. Use this to justify small process tweaks and enablement time. ([GitHub Blog](https://github.blog/ai-and-ml/generative-ai/how-generative-ai-is-changing-the-way-developers-work/?utm_source=chatgpt.com "How generative AI is changing the way developers work"))
    

**Topics**

- Agree where AI helps now: **analysis/triage**, **test authoring**, **doc/PR‑FAQ drafting**, **safe scaffolding**—and where we’ll _not_ use it (complex kernel/FS algorithms without deep review).
    
- How to measure impact (DORA metrics) across releases. ([GitLab Docs](https://docs.gitlab.com/user/analytics/dora_metrics/?utm_source=chatgpt.com "DevOps Research and Assessment (DORA) metrics"))
    

**Decisions**

- Approve **1 day / sprint** sandbox time for devs to productionize AI wins (aligned to Shachar’s “organic innovation” preference).
    
- Approve **shared prompts/playbooks** in repo; rotate demo in monthly all‑hands to spread wins.
    

**Receipts**

- _Shachar:_ “Almost all devs use Cursor; focus AI on analysis/CI/bug triage; organize organically, not heavy COE.”
    

---

### Session 7 — **Microsoft/Apollo execution plan (3‑track)**

**Attendees:** Jeff (Approver), you (Driver), Alon (Contributor).  
**Points to land**

- **Track A (MAI deployment outside Azure DCs):** exploit success as the immediate wedge.
    
- **Track B (Apollo integration):** thin VAST control plane in **AKS‑led Project Apollo** as standard storage for single‑tenant GPU sites.
    
- **Track C (Azure hardware/first‑party path):** start the long road with Azure Hardware (Ronnie Borker), keep **liquid‑cooled SKU** conversations alive as DC cooling fungibility lever.
    

**Topics**

- Blob vs S3 vs multi‑protocol head: near‑term focus on **performance** for GPU utilization; explore Blob compatibility only as a leverage point into first‑party services—not as a distraction now.
    
- Partner map & exec coverage (Vipin, Kushal, AKS/Anson/Keek, Azure Hardware).
    

**Decisions**

- Approve **3‑track plan**, name DRIs per track, and what “proofs” we need by specific dates (pilot perf, Apollo POC, hardware meeting).
    

**Receipts**

- _Alon:_ “Marketplace SKUs aren’t price‑performance competitive for VAST at scale.”
    
- _Alon:_ “Liquid‑cooled storage SKUs help DC fungibility and late‑binding storage vs GPU rack decisions.”
    

---

### Session 8 — **Product operating model: PRD↔FRD, ownership, and PM depth**

**Attendees:** Jeff; invite Shachar + architects to co‑author the solution.  
**Points to land**

- Keep architects authoring **FRDs** for deep technical detail; have **PMs own PRDs/PR‑FAQs** and end‑to‑end validation with customers. Use **DACI** so PMs _drive_ multi‑team work, architects _contribute_, and Jeff _approves_. ([Mindtools](https://www.mindtools.com/an30xh5/robert-cialdini-six-principles-of-persuasion?utm_source=chatgpt.com "Robert Cialdini: Six Principles of Persuasion"))
    
- Recruit 1–2 **developer‑to‑PM** profiles to raise technical bench.
    

**Topics**

- Where to embed PMs with pods; how PMs will “play with the product” before GA (Shachar’s ask).
    
- Define **Cloud Design Qualifiers** as the binding contract between PRD and FRD.
    

**Decisions**

- Approve the **ownership model** (who writes PRD/FRD; who signs each gate).
    
- Approve **two reqs** for technical PM hires.
    

**Receipts**

- _Shachar:_ “Product should do more end‑to‑end and be more technical; architects write FRDs today.”
    
- _You to Shachar:_ “We’ll upskill and recruit dev‑to‑PM to close the gap.”
    

---

### Session 9 — **Field, RFEs, and deal‑override policy (clean pipeline, faster yes/no)**

**Attendees:** Jeff; include Tomer (PM), Sales/SE rep.  
**Points to land**

- Roll up RFEs into **thematic epics** scored by **RICE**; don’t let one‑offs fragment the product. ([Harvard Business Review](https://hbr.org/archive-toc/BR0109?utm_source=chatgpt.com "From the Magazine (October 2001)"))
    
- Create a **Deal‑Override Policy**: objective criteria + RAPID table; if we say “no,” provide **Option B** (workaround, timeline, or partner).
    
- Start a **“Design Partner” program** for 2–3 anchor customers to de‑risk 5.6.
    

**Topics**

- How to keep Slack support high‑touch without letting it become the backlog funnel.
    
- Beta acceptance criteria and how we’ll publicize wins (Kotter’s “short‑term wins”). ([Harvard Projects](https://projects.iq.harvard.edu/files/sdpfellowship/files/day3_2_choosing_strategies_for_change.pdf?utm_source=chatgpt.com "Choosing Strategies for Change"))
    

**Decisions**

- Approve **RFE triage rubric**, **deal‑override policy**, and **Design Partner** charter.
    

**Receipts**

- _Tomer:_ “Slack support is great; we need structured RFE ↔ features roll‑up.”
    
- _Shachar:_ “Three buckets: tactical deal features, strategic innovation, and technical debt. Optimize for throughput.”
    

---

### Session 10 — **Resourcing & guardrails (protect the bet without starving Insight Engine)**

**Attendees:** Jeff (Approver), you (Driver), Shachar.  
**Points to land**

- Set a **capacity reservation** for Cloud P0s (e.g., 20–30% of relevant teams’ time) so interrupts don’t cannibalize 5.6.
    
- Use **DORA metrics** to track whether we’re actually getting faster (lead time, deploy frequency, change fail rate, MTTR). ([GitLab Docs](https://docs.gitlab.com/user/analytics/dora_metrics/?utm_source=chatgpt.com "DevOps Research and Assessment (DORA) metrics"))
    

**Topics**

- What to slow/stop in Insight Engine to fund Cloud P0s (time‑boxed, not indefinite).
    
- A clear **“stop starting, start finishing”** list for 5.6.
    

**Decisions**

- Approve **capacity guardrails** (percentages by team).
    
- Approve the **focus list** and what slips post‑5.6.
    

**Receipts**

- _Shachar:_ “We prioritized Insight Engine this year; we can’t do everything. Optimize for throughput over predictability.”
    

---

### Session 11 — **Tel Aviv visit (Nov 23–26): outcomes, rooms, and agenda**

**Attendees:** Jeff; coordinate with Shachar.  
**Points to land**

- Your visit isn’t a tour; it’s **two outcomes**: (1) lock the 5.6 Cloud Design Qualifiers + P0s, (2) leave a live **Apollo/MAI execution plan** with named owners and dates.
    

**Topics**

- **Big Room Planning** half‑day with Ronnie/Max (cloud teams), architects, QA, program: confirm scope, dependencies, and gates.
    
- **Knowledge share**: Azure/MAI/Apollo context, GPU‑bound design considerations; capture unknowns to answer fast.
    

**Decisions**

- Approve agenda, rooms, and attendees; align a short **all‑hands cameo** for you to reinforce the why.
    

**Receipts**

- _Shachar:_ “May move monthly all‑hands to that week so you can do it in person.”
    

---

## Your influence playbook (sound bites Jeff will respect)

**1) “Give me a RAPID/DACI guardrail so we move fast and don’t revisit decisions.”**  
RAPID clarifies who **Recommends**, **Agrees/Approves**, **Performs**, **Inputs**, **Decides**; DACI makes **Driver** and **Approver**explicit on specs. This reduces cycle time and stakeholder thrash. ([Harvard Business Review](https://hbr.org/podcast/2021/03/building-influence-without-authority?utm_source=chatgpt.com "Building Influence Without Authority"))

**2) “We’ll use a PR‑FAQ so every bet starts with the customer’s press release.”**  
Amazon’s “working backwards” PR‑FAQ forces clarity before coding; it’s battle‑tested for big, ambiguous bets. ([Mindtools](https://www.mindtools.com/an30xh5/robert-cialdini-six-principles-of-persuasion?utm_source=chatgpt.com "Robert Cialdini: Six Principles of Persuasion"))

**3) “Type‑1 vs Type‑2: Let’s stop treating every interrupt like an irrevocable decision.”**  
Bezos’s two‑way door framing increases **decision velocity**—most interrupts are Type‑2; ship and iterate. ([SEC](https://www.sec.gov/Archives/edgar/data/1018724/000119312517120198/d373368dex991.htm?utm_source=chatgpt.com "EX-99.1"))

**4) “Reliability is a product feature—SLOs and error budgets will decide pace.”**  
Google SRE practice: define SLOs/SLIs; spend error budgets wisely between feature velocity and reliability. ([DevOps.com](https://devops.com/measuring-github-copilots-impact-on-engineering-productivity/?utm_source=chatgpt.com "Best of 2023: Measuring GitHub Copilot's Impact on ..."))

**5) “We’ll track DORA—not vanity metrics—to prove we’re shipping faster and safer.”**  
Deployment frequency, lead time, change‑fail rate, and MTTR are the industry standard performance indicators. ([GitLab Docs](https://docs.gitlab.com/user/analytics/dora_metrics/?utm_source=chatgpt.com "DevOps Research and Assessment (DORA) metrics"))

**6) “AI will compound throughput if we aim it at the right steps and measure it.”**  
Research shows Copilot‑class tooling improves speed and perceived productivity; we’ll focus on analysis, test authoring, and docs, with rigorous review for deep systems work. ([GitHub Blog](https://github.blog/ai-and-ml/generative-ai/how-generative-ai-is-changing-the-way-developers-work/?utm_source=chatgpt.com "How generative AI is changing the way developers work"))

**7) “RICE keeps us honest when deal asks pile up.”**  
Score reach/impact/confidence/effort so RFEs roll up into thematic epics vs. fragmented one‑offs. ([Harvard Business Review](https://hbr.org/archive-toc/BR0109?utm_source=chatgpt.com "From the Magazine (October 2001)"))

**8) “Short‑term wins create momentum for change.”**  
Lock in early customer‑visible wins (e.g., MAI perf proof) to accelerate adoption and org support. ([Harvard Projects](https://projects.iq.harvard.edu/files/sdpfellowship/files/day3_2_choosing_strategies_for_change.pdf?utm_source=chatgpt.com "Choosing Strategies for Change"))

---

## Quick artifacts to prepare (one‑pagers Jeff can skim)

- **Cloud Program Charter** (one page): mission, scope, RAPID/DACI table, cadences.
    
- **MAI/Apollo PR‑FAQ**: press release + 10 FAQs + 3 milestones. ([Mindtools](https://www.mindtools.com/an30xh5/robert-cialdini-six-principles-of-persuasion?utm_source=chatgpt.com "Robert Cialdini: Six Principles of Persuasion"))
    
- **5.6 Cloud Design Qualifiers**: the non‑negotiables to call 5.6 “Cloud‑ready.”
    
- **Release & Support Policy**: freeze windows, gates, _deal‑override_ rules, EOL/SLA.
    
- **SLOs v1 + Live‑Site RACI**: who owns what, paging tree, weekly review template. ([DevOps.com](https://devops.com/measuring-github-copilots-impact-on-engineering-productivity/?utm_source=chatgpt.com "Best of 2023: Measuring GitHub Copilot's Impact on ..."))
    
- **RICE Scoring Sheet** for RFEs (with examples). ([Harvard Business Review](https://hbr.org/archive-toc/BR0109?utm_source=chatgpt.com "From the Magazine (October 2001)"))
    

---

## Appendix: quotes & data points you can drop into the sessions

**From Alon (Chief Architect, 2025‑10‑28)**

- “Use **MAI success** as the wedge … **VAST as software‑first**, open to ODM and liquid‑cooled options.”
    
- “Blob can’t match VAST performance.”
    
- “AKS‑led **Project Apollo** aims for a slim control plane … storage isn’t solved; **VAST can be the standard**.”
    
- “Marketplace VM offers (e.g., Lsv4/v5) aren’t **price‑perf competitive** at scale.”
    
- “Liquid‑cooled storage SKUs could help DC cooling fungibility and **late‑binding** storage vs GPU racks.”
    

**From Shachar (Head of Dev, 2025‑10‑28)**

- Weekly 1:1 agreed; Tel Aviv visit welcomed (Nov 23–26).
    
- “Almost all devs use **Cursor**; focus AI on **analysis/CI/bug triage** … prefer **organic** innovation over a heavy COE.”
    
- “Product needs more **technical depth** and **end‑to‑end** involvement; architects write FRDs.”
    
- “We bucket work into **tactical deal features**, **strategic innovation**, and **technical debt**; I optimize for **throughput**.”
    

**From Eyal (Release Planning)**

- “Minor releases **killed us** … constant urgent requests … very challenging.”
    
- “5.6 GA around **July**; some cloud‑critical items absent in 5.5.”
    
- “**Auth providers** limited (≈8); **config** isn’t tenant‑scoped.”
    

**From Liraz (Program/Quality)**

- “**Golden Run** and **Code Freeze** out of sync.”
    
- “A lot is **tribal knowledge**; not written down.”
    
- “Target QA success ≈**96–97%**.”
    

**From Tomer (PM)**

- “We’re ~**4 PMs** for ~**400 engineers**; need **Cloud Design Qualifiers** and thematic multi‑tenancy.”
    
- “**Slack support** is great but mustn’t become the backlog funnel.”
    
- “Global namespace **write leases** in 5.5 preview.”
    

---

## What success looks like after these sessions

- You are named **DRI** for the Cloud Program; Jeff publicly backs the charter and cadence. (Scope ↑)
    
- **5.6** has approved **Cloud Design Qualifiers** and a clear, resourced P0 list. (Execution ↑)
    
- A published **Release & Support policy** reduces churn and sets expectations. (Predictability ↑)
    
- **SLOs + Live‑Site** rituals exist; observability is on the 5.6 plan. (Reliability ↑)
    
- The **MAI/Apollo plan** is three‑tracked, staffed, and time‑boxed; the field knows what to say. (Wedge ↑)
    
- **AI‑accelerated** practices are sanctioned and measured, aligned to Shachar’s style. (Throughput ↑)
    

If you want, I can turn this into a set of ready‑to‑use one‑page templates (charter, PR‑FAQ, gate checklist, SLO dashboard skeleton, RICE sheet) so you can drop them into the first pre‑read.