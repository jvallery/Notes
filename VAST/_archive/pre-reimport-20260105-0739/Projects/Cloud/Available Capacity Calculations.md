
Hi All --

Is the intent to have a uniform fixed overhead percent across all deployments and cloud providers?

I agree with the spirit of keeping a single overhead number simple for customers, but a fixed % (e.g., ~35%) will be wrong often enough to create surprises in both pricing and delivery. Two reasons:

1. **The number of _guaranteed_ sub‑zonal failure domains (FDs) isn’t uniform across clouds/regions.**
    
    - **GCP** exposes up to **8 sub‑zonal “availability domains”** per zone via _Spread Placement Policy_ (these are distinct hardware groups within a zone). That materially enables wider, more efficient EC stripes inside a single zone.
        
    - **AWS** can guarantee **7 distinct racks per AZ** with _Spread_ or **7 partitions per AZ** with _Partition_ placement groups (non‑overlapping sets of racks).
        
    - **Azure** offers **5 fault domains per zone** when we choose _static fixed_ spreading in VM Scale Sets; Availability Sets (no AZs) expose **3 FDs** and **20 UDs** (only one UD updated at a time).
        
    - **OCI** has **exactly 3 FDs per Availability Domain** (datacenter).
        
    
    Wider FDs ⇒ wider **intra‑zone** EC stripes ⇒ lower parity overhead for the same failure tolerance. A uniform 35% doesn’t reflect those structural differences.
    
2. **Storage‑optimized VM capacity is uneven across zones—and sometimes within the sub‑zonal FDs.**  
    Example: Azure’s Ls‑series (NVMe local) SKUs aren’t uniformly available across all zones in a region; Microsoft explicitly guides you to query _zone support by SKU_ in the target region (`az vm list-skus`). If a zone or FD can’t supply enough of the chosen SKU, our effective stripe width and capacity drop to the _least_ populated domain.
    

There are also **operational levers that change “overhead” in practice**:

- **Provider maintenance/update behavior**: only one _Update Domain_ at a time on Azure (AvSets/Uniform VMSS), vs. “budgeted rolling updates” we set ourselves on GCP (MIG `maxUnavailable`/`maxSurge`) and AWS (ASG Instance Refresh min‑healthy). Our chosen budget must be ≤ parity or we temporarily reduce usable capacity.
    
- **Ephemeral storage traits**: local NVMe is _ephemeral_ across providers (e.g., EC2 instance store is lost on stop/terminate; Azure temporary disk can be lost on host moves; GCP Local SSD is ephemeral though designed to survive live‑migrate events). This drives **rebuild headroom** we need to reserve, which is not a fixed %, and it varies with failure/maintenance patterns in each cloud.
    
- **Capacity guarantees**: we can (and should) use **capacity reservations** where available—AWS _On‑Demand Capacity Reservations_, Azure _Capacity Reservation_, GCP _Reservations_, and OCI _Compute Capacity Reservations_—but these are scoped per AZ/region and don’t ensure equal capacity per FD. We still have to model skew.
    

---

## A simple model the team can implement now (“Available Capacity” as a pricing unit)

Instead of a single fixed %, let’s calculate “available capacity” from first principles given the **actual** region, zone(s), FD spreading, and SKU counts we can provision.

**Inputs per deployment plan**

- **Topology**: chosen cloud, region, zones in scope, **FD count per zone** (from table below), and the **EC scheme**inside a zone (k data + m parity, width W=k+m).
    
- **Inventory**: for each zone and FD, **instance count of the chosen SKU** and **ephemeral TiB per instance** (SKU spec).
    
- **Operational budgets**: non‑EC overheads (FS/metadata/SCM), **rebuild headroom** (to absorb a node/FD loss), and **rolling‑update budget** (max concurrent unavailability).
    

**Computation**

1. **Raw capacity per FD** = instances_FD × ephemeral_TiB.
    
2. **Stripe limiter** = min(raw_capacity per FD) across the W FDs used by the stripe.
    
    - If we place **one fragment per FD** (our default), total _user_ capacity **inside the zone** ≈  
        [  
        \text{Usable_zone} \approx \left(\sum_{\text{FD}} \text{raw_capacity_FD}\right)\times \frac{k}{W} ;-; \text{headroom}_{\text{rebuild}} ;-; \text{headroom}_{\text{rolling updates}}  
        ]  
        The **min‑FD** bound matters because stripes are limited by the most capacity‑constrained FD.
        
3. Apply **non‑EC overheads** (filesystem/metadata/SCM). Karl’s sheet has ~8% FS + ~3% SCM; let’s keep these explicit knobs in the calculator rather than baking them into one % everywhere.
    
4. If we’re doing **zone‑level HADR** (e.g., 2+1 across three AZs), multiply by the outer‑code factor and include any cross‑zone reserve.
    

**Why this is better than a fixed number**: it keeps the customer‑facing “available capacity” predictable while letting engineering choose the best EC width that the **real** FD/zone/SKU landscape supports in that region.

---

## What changes with “8 failure domains”?

We can absolutely run **wide intra‑zone codes** where the cloud allows it:

|Cloud|Provider‑promised _sub‑zonal_FD knobs we can rely on|**Max EC width (single zone)** you can safely assume|Example (f=1)|Overhead|Example (f=2)|Overhead|
|---|---|--:|--:|--:|--:|--:|
|**GCP**|Spread Placement Policy across **up to 8 availability domains** per zone.|**8**|**7+1**|**14.3%**|**6+2**|**33.3%**|
|**AWS**|**7** distinct racks per AZ (Spread) **or 7 partitions per AZ**(Partition).|**7**|**6+1**|**16.7%**|**5+2**|**40.0%**|
|**Azure (VMSS zonal, static‑fixed)**|Exactly **5 FDs** per zone; AvSet (no AZs) = **3 FDs**, **20 UDs**.|**5**|**4+1**|**25.0%**|**3+2**|**66.7%**|
|**OCI**|**3 FDs per Availability Domain**.|**3**|**2+1**|**50.0%**|_(not practical)_|—|

> Notes (for planning):  
> • AZ counts and support vary by region (AWS regions have multiple AZs; AZs are physically separate DCs). Use zone‑level codes **only** when you intend to pay cross‑AZ latency/egress; otherwise stay intra‑zone and wide.  
> • Azure zone/SKU support is region‑specific—**check actual zone coverage by SKU** (`az vm list-skus`). This is the common source of “we planned 5 FDs but got 3 FDs worth of Ls‑capacity in one zone.”  
> • On GCP and AWS, there’s no “UD” abstraction; we control maintenance blast radius with **MIG rolling updates** and **ASG Instance Refresh**. Keep max unavailable ≤ **m**.

---

## Why a **fixed % overhead** is risky (and what to do instead)

**Constraints & gotchas with a single percentage**

- **FD count drives parity math**: 7+1 on GCP is great _where we truly get 8 FDs_; in Azure Ls regions where we can only fix 5 FDs, the same failure tolerance forces **4+1** (25%), not 14–17%.
    
- **SKU availability by zone/FD**: storage‑optimized shapes (e.g., Azure Ls‑series) can be **zone‑limited** and sometimes temporarily constrained within a zone. Our effective stripe count becomes bound by the **least‑capable FD**.
    
- **Maintenance semantics**: Azure updates **one UD at a time**; if we also roll platform/driver updates on our side, we must ensure concurrency ≤ parity or we’re over‑committing capacity. On AWS/GCP, _we_ set those budgets via ASG/MIG; budgets vary by cluster size.
    
- **Ephemeral storage behavior**: EC2 instance store/ Azure temporary disk can be lost on certain events; GCP Local SSD is still ephemeral. The **rebuild headroom** we reserve will differ by provider and by how aggressively we roll updates.
    
- **Quotas & guarantees**: we can mitigate with **capacity reservations**—but they’re per‑AZ/region and don’t balance capacity across FDs automatically.
    

**Recommendation**

- Keep Karl’s FS/SCM terms explicit.
    
- Replace the single “35%” with a **range published up‑front** (e.g., _“Overhead typically 20–50% depending on region/SKU and HADR settings”_) **and** compute the exact number at deploy time using the model above.
    
- Where we want to promise a specific capacity number pre‑contract, back it with **capacity reservations** in the selected AZ(s) and spot‑check SKU availability by zone (Azure: `az vm list-skus --location <region> --size <SKU> --zone`).
    

---

## Answering Jason’s concern about flexibility

> _“I do worry that we will have to support various EC schemes based on the cloud provider…and in the future, we are likely to need to support EC over availability zones to ensure HADR.”_

I agree. The model above accommodates this by **decoupling**:

- **Intra‑zone EC width** (map 1 fragment per FD; pick widest feasible width per cloud/region).
    
- **Zone‑level HADR** (small outer code such as 2+1 across 3 zones, or async replication where latency/egress are concerns).  
    On Azure and GCP we rely on our own rolling‑update budgets; on Azure AvSets we also inherit “one UD at a time” behavior. This keeps us flexible without baking in one overhead %.
    

---

## What I propose we do next (engineering + PM)

1. **Parameterize the calculator Karl shared** with: cloud/region, zones, _FD count_, SKU per‑zone counts, EC width, non‑EC overheads, rebuild/rolling‑update headroom. Output “available capacity” and the derived overhead %. (We’ll feed this value into pricing.)
    
2. **Per‑cloud deployment defaults** (can be overridden per region):
    
    - **GCP**: target **7+1** intra‑zone where 8 sub‑zonal ADs are supported; roll with MIG (`maxUnavailable` ≤ m).
        
    - **AWS**: target **6+1** in a Partition PG (7 partitions/AZ); use ASG Instance Refresh (min‑healthy ≥ k/(k+m)).
        
    - **Azure**: target **4+1** in zonal VMSS with **static fixed** FDs; confirm zone/SKU coverage (`az vm list-skus`).
        
    - **OCI**: target **2+1** per AD (3 FDs); add outer HADR across ADs where required.
        
3. **Operational guardrails**: require **capacity reservations** when we commit to a specific capacity by date (AWS/Azure/GCP/OCI each have native constructs).
    

If we’re aligned, I’ll work with Karl and the dev leads to wire these inputs into the deployment tooling so the “available capacity” number we show the customer is both **accurate for their region/SKU** and consistent with how we stripe for durability and availability.

—[Your Name]  
VP, Product Management

---

### Appendix – quick reference (promises and knobs)

|Cloud|Isolation building blocks (what we can rely on)|Capacity/maintenance notes|
|---|---|---|
|**GCP**|**Zone** + _Spread Placement Policy_ across sub‑zonal **availability domains (up to 8)**; rolling updates via **MIG**(`maxUnavailable`, `maxSurge`).|Local SSD is ephemeral (designed to survive live migration but not guaranteed across all events); reservations can **guarantee capacity** per zone.|
|**AWS**|**AZ** + _Spread_ (**7 distinct racks/AZ**) or _Partition_ (**7 partitions/AZ**) placement; rolling via **ASG Instance Refresh**.|EC2 instance store is ephemeral; use **On‑Demand Capacity Reservations** to pin capacity in an AZ.|
|**Azure**|**AZ** + **VMSS (static‑fixed 5 FDs/zone)** or **Availability Set (3 FDs, 20 UDs; one UD at a time)**; zone/SKU coverage varies by region and must be queried.|Temporary disk is ephemeral; **Capacity Reservations** available. Maintenance updates one UD at a time on AvSets/Uniform VMSS.|
|**OCI**|**Availability Domain** + **3 Fault Domains/AD**; planned maintenance supports live‑ or reboot‑migration; **Compute Capacity Reservations** available.|Dense NVMe shapes are local; plan for rebuild headroom and per‑FD balancing.|

_Happy to iterate with the dev leaders on the exact calculator knobs so what we show in pricing aligns 1:1 with what we deploy._