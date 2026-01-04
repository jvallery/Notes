Subject: Cloud Pricing Direction — Principles, Decisions Needed, and Option Set for Leadership Alignment

Hi Pricing v‑team,

Thank you all for a productive conversation this morning on the pricing for Cloud. The recent discussions have uncovered the core tension we need to resolve: cloud economics are fundamentally different from on‑prem, yet our current posture assumes they’re the same. 

This note sets what I would like to see as guiding principles, the **specific decisions we need from leadership**, and a concise **menu of pricing options with pros/cons**, so we can converge quickly and avoid one‑way doors.

## Why we can’t copy/paste on‑prem pricing into cloud

- **Cloud topology variance**: instance families, generations, and per‑cloud networking create different CPU:capacity ratios and performance ceilings; not all shapes make sense for storage‑led use cases.
    
- **Provider metering already exists**: customers already pay the cloud for capacity, requests/IO, and egress. If we layer the wrong software meter on top, we blow up TCO at PiB/EiB scale.
    
- We need a **pricing roadmap that can evolve** (private offers -> public reservations -> public PAYG -> SaaS) **without re-contracting customers** or creating irreconcilable exceptions.
    
## Principles:

1. **Simplicity first**: easy to quote, easy to forecast, minimal knobs.
    
2. **Value alignment**: revenue recovery must correlate to **customer value** (hot working sets and compute‑heavy services carry more value than cold archives).
    
3. **Normalization across deployments**: pricing should normalize value across clouds, VM SKUs, and generations (e.g., ACU/vCPU differences) so customers aren’t penalized (or we leave money on the table) purely due to instance shape quirks.
    
4. **Separate storage from compute‑intensive services**: storage capacity and advanced/CPU‑heavy features should have distinct meters so we can scale revenue with usage without confusing the storage bill.
    
5. **Simple, consistent discounts**: the same discounting on‑prem and in cloud (term, volume, reserved packs), aligned with cloud commitment constructs (e.g., Reserved Capacity/Commitments).
    
6. PAYG & Reserved Models **:
    
    - **Reserved for predictable estates and ELAs.
        
    - **PAYG/burst for spin‑up/spin‑down use; necessary even before SaaS if we want marketplace velocity.
        
7. **No one‑way doors**: never require throttling/disabled cores or per‑API/IOPS charges. Keep the model evolvable toward SaaS.
    
## My view on end‑state and near‑term posture

- **End‑state direction**: a **two‑meter model** based on **synthetic normalization**
    
    - **VAST Data Unit (VDU)**: a capacity‑weighted unit that charges full weight for **hot working set on NVMe**, and a **light, capped weight** for warm/cold tiers (block/object offload).
        
    - **VAST Compute Unit (VCU)**: a normalized **compute meter** (vCPU‑hours; GPU later) for **compute‑heavy services** (indexing/catalog, protection jobs, scans, analytics), with a **baseline included** and **reserved packs**for predictability.  
        This captures value, stays simple, and works on‑prem, in customer tenants, and as SaaS.
        
- **Near‑term posture (to ship quickly and cleanly)**: **capacity‑only, tier‑weighted** pricing via **private offers**. Publish a shape‑to‑tier map per cloud. Add **VCUs** for a few clearly compute‑heavy features once public offer is live.

## Decisions we need from leadership (with my recommendation)

1. **Adopt two‑meter end‑state (VDU + VCU)?**  
    **Recommend: Yes.** This is the only model that cleanly separates storage from compute services and scales with customer received value.
    
2. **Posture for private offers (now): capacity‑only or capacity+fixed cores?**  
    **Recommend: Capacity‑only given timeline.  Risk needs to be quantified against future business with the private offer customers and their specific scenarios/use cases. 
    
3. **Public PAYG timing and scope:**  
    **Recommend:** Introduce PAYG alongside reservations in the public offer with **VCUs for a limited set of compute‑heavy features**(baseline included), while keeping the tier‑weighted capacity meter.
    
4. **Normalization approach:**  
    **Recommend:** Do **not** meter actual vCPU count in cloud. Normalize via **VDU weights** (for capacity tiers) and **VCUs** (for optional compute). Publish a **shape‑to‑tier** guide; never throttle cores.
    
5. **Discounts (on‑prem & cloud):**  
    **Recommend:** 1‑ and 3‑year **term bands** + **volume tiers** + **reserved VCU packs**. Use marketplace **private offers** and align to cloud commitments. Keep cloud discounts tighter than historic on‑prem.
    
6. **Hybrid ELA conversion rights (on‑prem <-> cloud):**  
    **Recommend:** Yes - explicitly support deploy‑anywhere entitlements; track usage in Polaris; transact via marketplace where needed to burn down commits.
    
7. **What we will not do:**  
    **Recommend:** No per‑API/IOPS software charges; no core throttling; no enforcement tricks that turn pricing into an engineering feature.
    


## Option set (concise pros/cons)

**A) Capacity‑only (flat or tier‑weighted)**

- **Pros:** Easiest to sell; clean parity across clouds; aligns with storage buyer expectations.
    
- **Cons:** Doesn’t monetize compute‑heavy services; flat variant risks double‑charging perception on object.
    
- **Use:** MVP/private offers; choose **tier‑weighted** to keep PB‑scale TCO sane.
    

**B) Capacity + fixed core entitlement (normalized cores per PiB; no throttling)**

- **Pros:** Cross‑cloud price parity; preserves “capacity + compute” narrative.
    
- **Cons:** Leaves upside for compute‑intensive adopters; core≠core across generations; adds explanation burden.
    
- **Use:** Transitional only if we must anchor to “cores.”
    

**C) Capacity + **measured compute units** (VCUs)**

- **Pros:** Captures value from advanced services; natural for PAYG; prepares for SaaS.
    
- **Cons:** Requires usage pipeline and clear visualizations; avoid credit opacity by including a baseline and labeling per‑feature usage.
    
- **Use:** Add with public PAYG; start with 2–3 features.
    

**D) Synthetic “single VAST unit” (bundling capacity+compute+perf)**

- **Pros:** Full normalization in one SKU.
    
- **Cons:** Hardest to understand/forecast; highest change‑management burden internally and with customers.
    
- **Use:** Not recommended now; revisit for first‑party SaaS packaging later.
    

**E) Performance classes overlay (Standard/Performance/Extreme SLOs)**

- **Pros:** Customer‑friendly; lets us pre‑qualify shapes and acknowledge network limits.
    
- **Cons:** Still need a compute revenue path (pair with C).
    
- **Use:** Optional façade once we support multiple instance families per cloud.
    

---

## Immediate follow‑ups (owners & artifacts)

- **Price card & policy (Pricing Ops):** publish tier weights, resiliency uplift, and discount bands (1/3‑yr, volume).
    
- **Shape‑to‑tier maps (PM/Eng):** by cloud, with networking assumptions; kept evergreen.
    
- **Usage & billing (Eng/Finance):** VCU metering for the first 2–3 compute‑heavy features; monthly export + “cost cockpit” in Polaris.
    
- **Marketplace motion (BizOps/Alliances):** private‑offer templating; public PAYG SKU plan; ELA conversion mechanics.
    
- **Field enablement (Sales/SE):** one‑pager: “How to position VDU/VCU and tier weights; what we don’t charge for; discount guardrails.”
    

---

## Ask

Please confirm the **seven decisions** above (especially #1–#3) so we can lock the price card, prepare marketplace offers, and brief the field with a consistent story. I’ll draft the customer‑facing one‑pager once we agree on tier weights, resiliency uplift, and discount bands.

Thanks,  
[Your Name]  
[Title / Team]


Below is a **menu of pricing options** for VAST in public cloud, organized to reflect the arguments you raised on the call (capacity‑only vs. fixed cores vs. consumption), plus how major cloud services price similar value so you can anticipate customer expectations. For each option I list **what you’d charge**, **how to meter it**, **pros**, **cons**, and **where it fits**. I close with a **phase‑by‑phase recommendation** and a compact **discount/commit toolkit**.

> **Context from your call** (condensed)
> 
> - You want **simple, cross‑cloud‑consistent pricing** that won’t blow up TCO at large scale and can also map to on‑prem.
>     
> - Near term: **private offers** (term commits) running in customer tenants. Later: **public PAYG**; eventual **SaaS**.
>     
> - Cloud shapes vary (e.g., Azure Lsv3, AWS i4i/i3en, GCP Local SSD), often **over‑provisioned on vCPU** for storage‑heavy use cases; networking (often ~100 Gbps east/west) can bottleneck. ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/storage-optimized/lsv3-series "Lsv3 size series - Azure Virtual Machines"))
>     
> - You debated: **capacity‑only** vs. **fixed cores per PiB** vs. **usage credits**; **never throttle/disable cores**; want clear discount logic aligned with **cloud commitments** (Azure Reserved Capacity, ANF Reservations, GCP CUDs). ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blob-reserved-capacity "Optimize costs for Blob storage with reserved capacity"))
>     

---

## Option A — **Capacity‑only** (simple storage SKU)

**What you charge**

- A single $/TiB‑month software fee on **“data under VAST management”** (all tiers), optionally:
    
    - **A1:** one flat rate, or
        
    - **A2:** **tier‑weighted** rates (Hot NVMe > Warm block > Cold object).
        

**How to meter**

- Average **TiB‑hours** by tier (NVMe / block / object) summed monthly.
    

**Pros**

- **Simplest** to sell and compare (matches how storage services are listed). Azure NetApp Files and Azure Blob Storage both support **term‑discounted, capacity‑based** reservations (100 TiB/1 PiB blocks, 1‑ and 3‑year), so procurement is familiar. ([Microsoft Azure](https://azure.microsoft.com/en-us/pricing/details/netapp/ "Azure NetApp Files – Pricing"))
    
- Predictable; **no surprise “IOPS/throughput” meters** (a complaint about some competitors). For example, FSx for ONTAP charges on **multiple components** (SSD storage, SSD IOPS, capacity pool, throughput capacity, backups); you avoid that complexity. ([Amazon Web Services, Inc.](https://aws.amazon.com/fsx/netapp-ontap/pricing/ "Amazon FSx for NetApp ONTAP Pricing"))
    
- Keeps field motion and quoting fast for **private offers**.
    

**Cons**

- Doesn’t monetize **compute‑heavy features** as they land (indexing, AI/analytics pipelines).
    
- Cross‑cloud **TCO still diverges** because the **cloud infra** costs vary by shape/region—even if VAST’s software line item is identical.
    
- If you do **A1 (flat)**, large cold/object estates can make the perceived “double billing” worse (provider already charges for object storage/requests).
    

**When it fits**

- **MVP / Private‑offer phase**; burst use cases; storage‑centric POCs.
    
- If you choose **A2 (tier‑weighted)**, keep cold/object weighted **lightly** so TCO stays acceptable at PB+ scale; S3/Blob/GCS already monetize those bytes & requests. ([Amazon Web Services, Inc.](https://aws.amazon.com/s3/pricing/ "S3 Pricing"))
    

---

## Option B — **Capacity + fixed core ratio** (normalized compute entitlement)

**What you charge**

- Capacity fee **plus** a **fixed, normalized vCPU entitlement** per PiB (e.g., “300 vCPU / PiB counted for pricing, regardless of actual VM cores”). No throttling; extra cores on some clouds are “free headroom.”
    

**How to meter**

- Capacity as in A; compute **doesn’t meter actual vCPU‑hours**—you price an **allowance** tied to capacity.
    

**Pros**

- **Cross‑cloud price parity**: customers see the same VAST software price even when Azure Lsv3 or AWS i4i expose very different vCPU counts. ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/storage-optimized/lsv3-series "Lsv3 size series - Azure Virtual Machines"))
    
- Keeps your **on‑prem “capacity + cores” narrative** consistent in concept while shielding cloud variability.
    
- Customers can realize **better performance** on shapes with more cores **without paying more**, reducing negotiation friction.
    

**Cons**

- **Leave money on the table** for compute‑intensive adopters (once higher‑level services/AI kick in).
    
- **Core != core** (generation, clock, ACU on Azure) so equivalence is imperfect; some buyers will question fairness. ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/virtual-machines/constrained-vcpu "Constrained vCPU sizes - Azure Virtual Machines"))
    
- If you later introduce usage‑based compute, this model may need to be **unwound**.
    

**When it fits**

- Bridge model until public PAYG; when you need **one price across clouds** today without growing the metering surface.
    

---

## Option C — **Capacity + measured compute (“credits”)**

**What you charge**

- Capacity (possibly tier‑weighted) **+** metered **vCPU‑hours** (and GPU‑hours later) for **compute‑heavy features**via **VAST Compute Credits (VCCs)**.
    
- Include a **baseline** compute allowance per TiB/PiB for routine ops; bill overage via credits.
    

**How to meter**

- Attribute **vCPU‑seconds** to features (indexing, global snapshots/replication orchestration, data‑reduction passes, scans, etc.).
    
- Show per‑feature usage for transparency.
    

**Pros**

- Scales revenue with **value delivered** (when customers run more data services, you earn more).
    
- Mirrors modern cloud data platforms: **Snowflake’s credits** (per‑second with 60‑second minimum) and **Databricks’ DBUs** (normalized compute unit) are well‑known constructs; buyers accept them, especially with **commit discounts**. ([Snowflake Documentation](https://docs.snowflake.com/en/user-guide/cost-understanding-overall "Understanding overall cost"))
    
- Readies you for a **future SaaS** offer where you’ll own infrastructure risk.
    

**Cons**

- Introduces a **second meter**; some customers perceive credit models as **opaque** if not visualized well. (Databricks DBU complexity is a common industry complaint.) ([CloudZero](https://www.cloudzero.com/blog/databricks-pricing/ "How Databricks Pricing Works: A 2025 Cost Breakdown"))
    
- Requires **usage pipeline** and a cost cockpit at GA.
    

**When it fits**

- Start with **just a few compute‑heavy features** on credits; keep core storage ops included. It’s an easy on‑ramp to the full SaaS model later.
    

---

## Option D — **Synthetic “VAST Unit” (bundle capacity + compute + perf)**

**What you charge**

- Price a single **synthetic unit** that bundles normalized vCPU, memory/throughput and TiB into one SKU.
    

**How to meter**

- Convert each deployment topology into **units** via a matrix (e.g., “N VMs of class X + Y TiB = Z units”).
    

**Pros**

- Full **cross‑cloud normalization**; one SKU to rule them all.
    

**Cons**

- **Customer confusion** and poor comparability in practice; similar unit models (e.g., DBUs) often require extra education and tooling to forecast. ([Microsoft Azure](https://azure.microsoft.com/en-us/pricing/details/databricks/ "Azure Databricks Pricing"))
    
- Hard to keep “unit math” in sync with rapidly changing instance generations and network caps.
    

**When it fits**

- Not ideal for the MVP. Consider only if you later run a **first‑party** SaaS and want a single line item.
    

---

## Option E — **Performance‑class (SLO) pricing**

**What you charge**

- Price by **throughput/SLO class per PiB** (e.g., Standard, Performance, Extreme), akin to how **Azure NetApp Files** sells **service levels** and how public‑cloud storage often tiers by service class. ([Microsoft Azure](https://azure.microsoft.com/en-us/pricing/details/netapp/ "Azure NetApp Files – Pricing"))
    

**How to meter**

- Tag deployments to a class. Back the class with **instance families** (e.g., i3en vs i4i, Azure Lsv3) and **network caps**; police only if telemetry shows chronic SLO miss. ([Amazon Web Services, Inc.](https://aws.amazon.com/ec2/instance-types/i4i/ "Amazon EC2 I4i Instances – Compute"))
    

**Pros**

- Lets you **pre‑qualify shapes** into classes; avoids penalizing customers for surplus cores when networking is the limiter.
    
- Easy narrative for storage buyers used to service levels.
    

**Cons**

- You still need a place to monetize **heavy compute services** (combine with **C** or include a “compute uplift” on higher classes).
    
- Requires careful SLO definition to avoid disputes.
    

**When it fits**

- As a **clear, customer‑friendly façade** over A/B/C; particularly good once you support multiple instance families per cloud.
    

---

## Option F — **Per‑node license + capacity** (classic appliance model)

**What you charge**

- License per **compute node** (or per cluster) + capacity.
    

**Pros**

- Simple for infra teams to count.
    

**Cons**

- **Cloud‑hostile** (shape churn, node size variation); can misalign with value and makes cross‑cloud parity hard.
    
- Customers associate this with legacy licensing.
    

**When it fits**

- I don’t recommend it for cloud; fine to keep **on‑prem** for continuity if needed.
    

---

## Option G — **“Unlock the extra cores” add‑on**

**What you charge**

- Base includes a **fixed compute entitlement** per PiB (Option B). Customers can buy an **add‑on** to “unlock” all cores on a VM family.
    

**Pros**

- Monetizes compute‑heavy adopters **without throttling** anyone by default.
    

**Cons**

- Messaging risk (“pay to unlock cores you already paid your cloud for”).
    
- If you ever **enforce limits**, that’s engineering work + customer friction (the team argued against throttling).
    

**When it fits**

- As a **niche add‑on** if customers explicitly ask; otherwise prefer **C (credits)**.
    

---

## Option H — **Hybrid ELA with conversion rights** (on‑prem + cloud)

**What you charge**

- A single enterprise commit (capacity and optional credits) with **deployment flexibility** across on‑prem and public cloud; transact via marketplace when needed to burn provider commits.
    

**Pros**

- Matches how large customers actually buy; simplifies multi‑cloud estates.
    
- Mirrors cloud commitment programs: **Azure Storage/ANF reserved capacity** (100 TiB/1 PiB; 1‑/3‑year), **GCP spend‑based CUDs** for NetApp Volumes, etc. ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blob-reserved-capacity "Optimize costs for Blob storage with reserved capacity"))
    

**Cons**

- Back‑office complexity (entitlement tracking across venues); discount leakage if not governed.
    

**When it fits**

- Big strategic accounts (your “ELA + marketplace” stories).
    

---

# Cross‑option levers & mechanics

### Simple **Resiliency Class** uplift

Apply a small factor on the **capacity** meter for multi‑AZ/dual‑region coordination overhead. Keep it transparent; customers already pay the cloud for extra **durability classes** (e.g., LRS/ZRS/GRS on Azure; S3 Standard vs. One Zone‑IA; GCS dual‑region). ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blob-reserved-capacity "Optimize costs for Blob storage with reserved capacity"))

### Align discounting with cloud programs

- **Term commits** (1‑/3‑year) on capacity and (if using credits) **reserved credit packs** — matches Azure **Storage/ANF Reserved Capacity** and GCP **CUDs** (spend‑based). ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blob-reserved-capacity "Optimize costs for Blob storage with reserved capacity"))
    
- **Volume tiers** (PB‑scale step‑downs).
    
- **Prepay wallet** (applied to capacity and credits).
    
- **Marketplace private offers** to count against cloud commits.
    

### What **not** to meter (customers dislike)

- **IOPS/throughput fees** (FSx for ONTAP has them; keep VAST simpler). ([Amazon Web Services, Inc.](https://aws.amazon.com/fsx/netapp-ontap/pricing/ "Amazon FSx for NetApp ONTAP Pricing"))
    
- **Per‑API‑call** software charges on object (S3/Blob/GCS already do this). ([Amazon Web Services, Inc.](https://aws.amazon.com/s3/pricing/ "S3 Pricing"))
    

### Metering blueprint (if you use C or A2)

- **Capacity by tier**: hourly **TiB** on NVMe (hot), block (warm), object (cold).
    
- **Compute (credits)**: **vCPU‑seconds** per feature; show feature tags on the bill (like Snowflake/Databricks do). ([Snowflake Documentation](https://docs.snowflake.com/en/user-guide/cost-understanding-overall "Understanding overall cost"))
    
- **Caps for cold**: optionally cap chargeable cold/object bytes at **β× hot** so PB‑scale lakes don’t dominate TCO (cloud already charges those bytes).
    

---

## Competitive reality to anchor your pros/cons

- **FSx for NetApp ONTAP** pricing involves **five components** (storage, IOPS, capacity pool, throughput, backups); great for fine‑tuning, but harder to forecast. Your **two meters** (capacity + optional credits) stay cleaner. ([Amazon Web Services, Inc.](https://aws.amazon.com/fsx/netapp-ontap/pricing/ "Amazon FSx for NetApp ONTAP Pricing"))
    
- **Azure NetApp Files** uses service levels and supports **100 TiB/1 PiB reservations** with 1‑/3‑year terms (familiar procurement motion). ([Microsoft Azure](https://azure.microsoft.com/en-us/pricing/details/netapp/ "Azure NetApp Files – Pricing"))
    
- **GCP NetApp Volumes** uses **spend‑based CUDs** (predictable discount mechanism). ([Google Cloud](https://cloud.google.com/netapp/volumes/docs/cuds "Committed use discounts | NetApp Volumes"))
    
- **Databricks** (DBUs) and **Snowflake** (credits) normalized compute consumption and sell **commit discounts**; good pattern for your higher‑level services later. ([Microsoft Azure](https://azure.microsoft.com/en-us/pricing/details/databricks/ "Azure Databricks Pricing"))
    

---

# Recommendation (phase‑by‑phase)

### **Phase 1 — Private offers in customer tenants (now)**

**Choose Option A2 (capacity‑only, tier‑weighted)** with a **tiny Resiliency Class uplift**.

- Why: maximum **simplicity**, clean **cross‑cloud** price list, and predictable TCO for buyers comparing against capacity‑priced services (ANF, etc.). ([Microsoft Azure](https://azure.microsoft.com/en-us/pricing/details/netapp/ "Azure NetApp Files – Pricing"))
    
- Implementation notes:
    
    - Weighting example: **Hot NVMe = 1.0×**, **Warm block = 0.25–0.35×**, **Cold object = 0.05–0.10×**, with **caps**on warm/cold vs hot to protect PB‑scale economics.
        
    - Publish a short **shape‑to‑tier map** (e.g., Azure Lsv3 = Hot; AWS i4i/i3en = Hot; object buckets = Cold) and acknowledge **network** as the typical limiter. ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/storage-optimized/lsv3-series "Lsv3 size series - Azure Virtual Machines"))
        
    - **Discount policy**: lower and tighter than on‑prem; mirror cloud programs: 1‑yr vs 3‑yr **Reserved Capacity/CUD** style bands for transparency. ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blob-reserved-capacity "Optimize costs for Blob storage with reserved capacity"))
        

### **Phase 2 — Public PAYG (≈ next wave)**

Layer in **Option C (credits)** **only** for **clearly compute‑heavy features** (index/catalog, global protection orchestration, policy scans), with:

- An **included baseline** per TiB so routine ops remain “free.”
    
- **Reserved credit packs** (1‑/3‑yr) for predictable jobs (nightly indexing, replication windows), mirroring **Databricks/Snowflake** commit patterns. ([Microsoft Azure](https://azure.microsoft.com/en-us/pricing/details/databricks/ "Azure Databricks Pricing"))
    
- Keep the **capacity tiering** as in Phase 1.
    

### **Phase 3 — Future SaaS**

Keep the **same two meters** (capacity + credits), but you roll cloud COGS into the price. Keep **term commits** and **prepay wallets**; optionally introduce **Performance classes (Option E)** as friendly bundles for the catalog.

---

## Quick decision matrix (pros/cons distilled)

|Option|Buyer Simplicity|Captures compute value|Cross‑cloud parity|TCO at PB scale|Risks|
|---|---|---|---|---|---|
|**A1** Flat capacity|**High**|Low|Medium|**Medium–Low**(depends on cold %)|Double‑charge perception on object|
|**A2** Tier‑weighted capacity|**High**|Low|Medium|**High** (with caps)|Slightly more SKU logic|
|**B** Fixed cores per PiB (no throttle)|**Med‑High**|Med (baseline only)|**High**|High|Leaves upside on the table; core quality varies (ACU, generations). ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/virtual-machines/constrained-vcpu "Constrained vCPU sizes - Azure Virtual Machines"))|
|**C** Credits for compute|Medium|**High**|High|**High**|Needs usage pipeline; credit models can feel opaque. ([CloudZero](https://www.cloudzero.com/blog/databricks-pricing/ "How Databricks Pricing Works: A 2025 Cost Breakdown"))|
|**D** Synthetic “VAST Unit”|Low|High|High|High|Most confusing in practice (sales friction).|
|**E** Performance classes|**High**|Med (if uplifted)|**High**|High|Requires careful SLOs and shape mapping.|

---

## Guardrails & FAQs you’ll face

- **“Why not charge IOPS/throughput?”** Because it complicates bills and customers already see that complexity elsewhere (e.g., FSx for ONTAP). We keep software billing to **capacity + (optional) compute credits**. ([Amazon Web Services, Inc.](https://aws.amazon.com/fsx/netapp-ontap/pricing/ "Amazon FSx for NetApp ONTAP Pricing"))
    
- **“Can you match my cloud commit structure?”** Yes. We mirror **Azure/ANF Reserved Capacity** and **GCP CUDs** with 1‑/3‑year commits (and private offers via marketplace). ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blob-reserved-capacity "Optimize costs for Blob storage with reserved capacity"))
    
- **“What about different VM generations/CPU speeds?”** We acknowledge variability (Azure **ACU** exists specifically to normalize performance across SKUs), so we don’t price **per actual vCPU** in cloud. We either normalize (Option B) or charge **compute by usage** (Option C). ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/virtual-machines/constrained-vcpu "Constrained vCPU sizes - Azure Virtual Machines"))
    
- **“Reserved capacity for S3?”** There’s no general S3 “reserved storage” construct; the exception is **provisioned capacity for Glacier expedited retrievals** (a different problem). ([AWS Documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/restoring-objects-retrieval-options.html "Understanding archive retrieval options"))
    

---

### Bottom line

- **Short term:** ship with **Capacity‑only, tier‑weighted (A2)** + **tight term discounts** aligned to Azure/ANF/GCP programs. This matches how storage is bought, is easy to compare, and protects PB‑scale TCO. ([Microsoft Azure](https://azure.microsoft.com/en-us/pricing/details/netapp/ "Azure NetApp Files – Pricing"))
    
- **Next:** add a **lightweight compute‑credits rail (C)** for the select services where you truly burn CPU; include a baseline so customers don’t feel nickel‑and‑dimed. Anchor discounting in **reserved credit packs** akin to DBU/credit commitments. ([Microsoft Azure](https://azure.microsoft.com/en-us/pricing/details/databricks/ "Azure Databricks Pricing"))
    
- **Always:** keep a **small resiliency uplift**, avoid IOPS/API fees, and publish a **clear shape‑to‑tier map** (Lsv3 / i4i / Local SSD as “Hot”). ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/storage-optimized/lsv3-series "Lsv3 size series - Azure Virtual Machines"))
    

If you want, I can convert this into a one‑page **decision playbook** (with example billing line items and a shape‑to‑tier appendix) so sales can choose among A2, B, and C with consistent language and discount bands.