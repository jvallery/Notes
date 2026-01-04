Here’s a structured analysis you can lift directly into a status email or slide for VAST leadership. I’ll first extract all the key info (competitive intel, requirements, next steps, timelines), then give you a draft email at the end.

---

Project Snapshot (for context)

- **Customer:** MAI, Nebius-based NeoCloud deployment in Dallas
- Scale: 120K GPUs (GB300 today, future generations expected)
    - **Current Plan-of-Record (POR):**
    - **Storage:** ~1.6 exabytes **all-flash** Blob storage
    - **Throughput:** ~192 Tbps total (≈1.6 Gbps per GPU)
    - **Hardware:** ~400 **Gen10.3** Azure SSD storage racks, ~15 kW/rack, CX7 NICs, delivering 1.6 EiB of usable capacity when configured as LRS Blob (14+4 EC with operational buffers/holdbacks)
    - **Architecture:**
        - Storage is **Azure Blob** (object) sitting behind **Sirius overlay** to reach the GPUs
        - Storage RDMA bandwidth **not currently accounted for** in the GPU front-end design
	- VAST being considered as either a **full pivot** from Blob or an **incremental supplement** to the Blob POR.
		- Path 1:  VAST ODM hadware to fully replace Azure Storage hardware
		- Path 2: Pave Gen10.3 with VAST
		
    Timeline -
    
    - The timeline is fast with first racks will need to be delpoyed by end of Jan. Early December site survey at **Nebius (Dallas)**
    - First ~9K GPUs live by **Jan 15–Feb 1, 2026** (storage needs to be ready by then).
        - Second tranche to support **18K GPUs** by around **June 1, 2026**.
        - Additional tranches in **July and September 2026** (dates & GPU counts to be confirmed; Bilal cites ~9.2K or 9.6K GPUs per tranche).
            - Up front (first half of 2026), Bilal **cannot guarantee** adjacent rows due to space constraints across 14 halls
    - VAST may need to:
        - Support **incremental row-by-row deployment**, or
        - Start as a **supplement** with more consolidated placement later.
        
     
    Network Requirements:
    
    - GPUs sit behind a **front-end network** that is treated as an external entity from Azure’s perspective.        
    - Azure connects via **border switches** and **Sirius appliances** providing overlay (physical virtual network).
    - All storage traffic to GPUs is currently expected to traverse **Sirius overlay**, sized for **192 Tbps**. If we can keep VAST + GPUs outside of the Azure network, this is a massive cost savings for Microsoft as the networking racks are not needed.
    - There are **14 data halls**, highly dense (“townhouses/row houses”).
    - Bilal believes front-end may be non-blocking, but **needs to confirm** especially for storage traffic.
        

 Next Steps & Owners (Consolidated)

- **Debrief & align requirements**
    
    - **Microsoft:** Bilal to **debrief MAI today** on the VAST option and get **per‑GPU throughput (read/write)** and **capacity** requirements by tranche.            
    - Clarify whether VAST is a **pivot** from Blob or **supplement** to Blob.    
    - **Microsoft:** Bilal to **align with Kanchan** on the VAST discussion and Microsoft’s internal requirements, then **circle back to VAST** on next steps.
-       - **Microsoft:** Suresh/Bilal to **schedule a three-way technical workshop** (Microsoft, MAI, VAST) to:    
        - Capture **detailed requirements**.
        - Draft the **site design** (topology, C/D ratios, capacity vs performance).
        - Discuss integration, security and operations.    
        - Confirm **Nebius front-end/back-end network topology**.
        - Determine if the **GPU front-end network is non-blocking** for storage traffic between all 14 halls.
        - Evaluate whether storage can **attach to the physical GPU network** **without** Sirius overlay and document required **security/compliance controls**.
            
- **POR details**
    
    - *Bilal to provide **detailed Gen10.3 POR specs**:
    -Bilal to confirm **exact site survey date/location** (Nebius / NIS facility, likely Dallas; early December) and agenda.
        
    - **Microsoft:** Bilal to **request VAST inclusion** in the site survey or schedule a **separate site visit** if agenda is too full.
        
    - **VAST:** Prepare a **site-survey checklist** (power, cooling, rack adjacency, network drops, management plane access, security requirements).
        
- **Deployment model decision space**
    
    - **Microsoft + VAST:** Suresh and Jason/Lior to outline options & tradeoffs:
        
        - **Azure storage hardware (Gen10.3)** vs **VAST ODM hardware**.
            
        - Pros/cons on:
            
            - Cost
                
            - Performance
                
            - Time-to-deploy
                
            - Operational model.
                
    - No final decision yet, but we need a **proposal ready** for the workshop.
        
- **Supply chain & ramp**
    
    - **VAST:** Jason (with suppliers) to:
        
        - Validate **flash and node availability** for the 2026 ramp.
            
        - Propose a **tranche-based build plan** aligned to:
            
            - First ~9K GPUs (Feb 2026).
                
            - 18K GPUs (June 2026).
                
            - Subsequent tranches (July/September).
                
        - Confirm **lead times** and whether a **single 1.6 EB “drop”** is possible vs incremental.
            
- **Rack & hall planning**
    
    - **Microsoft:** Suresh to draft a **rack adjacency / row allocation plan** for VAST:
        
        - What’s feasible in early 2026 vs later.
            
        - How to minimize scattering across the 14 data halls.
            
    - **VAST:** Provide guidance on **minimum cluster contiguity** needed to meet performance and failure-domain requirements.
        
- **Dedup & capacity assumptions**
    
    - **VAST:** Lior to propose **dedupe planning assumptions** (e.g., 1.5–1.7× effective capacity) based on MAI dataset patterns.
        
    - **Joint:** Align these assumptions so MAI understands **physical vs effective capacity**.
        

### 4.3 Medium-Term (Post-Workshop / Through 2026)

- **Engineering roadmap alignment**
    
    - **VAST:**
        
        - Prioritize **Blob tiering support** (VAST → object) and **Blob API over VAST** to allow:
            
            - Transparent tiering to Blob.
                
            - Use of existing Blob-based tooling.
                
        - Provide **rough timeline ranges** once requirements and opportunity size are locked.
            
    - **Microsoft/MAI:**
        
        - Validate how important Blob API compatibility is vs pure file/NFS usage, and when.
            
- **Finalize site design & war room**
    
    - **Joint:** Run a **war-room style design session**:
        
        - Lock **C/D node ratios**, rack counts, network architecture.
            
        - Confirm **attach model**: direct to GPU network vs via Sirius.
            
        - Align on **operational model** (monitoring, SLAs, on-call, upgrades).
            
- **Execute ramp**
    
    - **VAST:** Airlift engineers and **execute deployments on each tranche**, adhering to agreed **work-back schedules** from the MAI go-live dates.
        
    - **Microsoft:** Ensure **GPU availability, power, and network** are ready for each tranche and coordinate with Nebius.
        

---

## 5. Timelines & Key Dates

Here’s a clean timeline you can reuse:

### 2025

- **Nov 20, 2025** – Alignment call (this meeting).
    
- **Late Nov 2025**
    
    - Nidi leaving Microsoft; ownership shifts to **Bilal + Kanchan + Suresh**.
        
    - Bilal to **debrief MAI** and **Kanchan** on VAST option and requirements.
        
- **Early December 2025**
    
    - **Nebius/MAI site survey** at NIS facility (likely Dallas).
        
    - VAST **requested** to attend; agenda already crowded.
        
    - Separate site visit can be arranged if needed.
        
- **Dec 3–16, 2025 (approx.)**
    
    - Bilal **OOO in the Middle East**.
        
    - **Suresh is DRI** during this time.
        

### 2026 (Nebius ramp – dates approximate from transcript)

- **Jan 15 – Feb 1, 2026**
    
    - First storage capacity must be **live** to support **~9K GPUs**.
        
    - VAST (if selected) must work back from this to:
        
        - Land initial racks.
            
        - Complete installation, configuration, and validation.
            
- **June 1, 2026**
    
    - Enough storage must be live to support **~18K GPUs** (GB300).
        
- **July & September 2026**
    
    - Additional GPU tranches (~9.2K–9.6K GPUs each) with corresponding storage needs.
        
    - Exact dates and GPU counts TBD.
        
- **End 2026 / early 2027 (implied)**
    
    - Reach full POR of **~1.6 EB all-flash** and **192 Tbps+** to support **100K–120K GPUs**.
        

> Key uncertainty: final deployment **location(s)** – there is a tension between references to **New Jersey datacenter** (Blob POR) and **Nebius Dallas**. This must be clarified, as it affects shipping, logistics and network topology.

---

## 6. Draft Status Email to VAST Leadership

You can paste and tweak this as needed.

---

**Subject:** Status – Microsoft MAI / Nebius Storage Opportunity (Nov 20, 2025)

Hi all,

Here’s a status update on the Microsoft MAI / Nebius storage engagement following today’s call with **Bilal Abdullah**(Master Principal Cloud Architect, Microsoft) and **Lior/Jason** from VAST.

---

### 1. Opportunity Overview

- Microsoft MAI is building a **Nebius-based NeoCloud deployment** of roughly **100K–120K GPUs** over the next several years.
    
- The current **plan-of-record (POR)** is an **Azure Blob**-based SSD storage solution:
    
    - ~**1.6 exabytes all-flash**.
        
    - ~**192 Tbps** total throughput (~1.6 Gbps per GPU).
        
    - ~**400 Gen10.3** storage racks at ~15 kW each with CX7 NICs.
        
- MAI strongly prefers **file-based storage (NFS)** with **NFS/RDMA and GPU Direct Storage**, which Blob cannot provide. They have had to refactor tooling around Blob and view that as a long-term constraint, especially as NVIDIA raises the **per‑GPU throughput** bar with each generation.
    

This opens a path for **VAST** either as:

- a **full pivot** from Blob, or
    
- an **incremental supplement** to the existing Blob POR.
    

---

### 2. Competitive Intelligence

- MAI has a long, positive track record running on **VAST at CoreWeave** (e.g., Condor cluster, where we see ~**1.7×**effective capacity from dedupe).
    
- Microsoft is already running a separate **bake-off** on future Azure hardware where **VAST and Lustre** are being compared head‑to‑head for MAI use cases; Blob is **not** part of that POC.
    
- VAST advantages vs Blob in this context:
    
    - **File + Object** (NFS over RDMA, GPU Direct Storage, S3 over RDMA).
        
    - **Modern ODM hardware** with tunable compute/data node ratios, better NICs and NVMe density.
        
    - **Data reduction** that can materially increase effective capacity vs physical flash.
        
- Today, VAST is **not yet an Azure hardware provider** (unlike NetApp) and Marketplace deployment on Lsv4 is not viable at this scale (would require tens of MW of compute).
    
- Multiple **NeoClouds** (CoreWeave, Crusoe, Vinescale, etc.) already standardize on VAST. Bilal is aware that a Nebius win should ideally align with a **consistent storage story** across the NeoCloud ecosystem.
    

On networking:

- The Nebius design uses **Sirius appliances** to bridge between Azure and the GPU front-end network for Blob. Sirius is currently sized to deliver ~192 Tbps.
    
- VAST **can attach directly to the physical GPU network**, bypassing Sirius, if Microsoft security/compliance approves:
    
    - This could remove a significant amount of **Sirius networking cost and complexity**.
        
    - Bilal explicitly called this out as a potential major **savings** vs the Blob-only architecture.
        

---

### 3. Requirements Snapshot

From today’s discussion, the requirements break down as:

**Scale & performance**

- ~**100K–120K GPUs** over the life of the cluster.
    
- Initial target throughput ~**192 Tbps** (≈1.6 Gbps per GPU); likely to increase with future GPU generations.
    
- **Capacity:** ~**1.6 EB all-flash** at full ramp, with interest in leveraging VAST **dedupe** to increase effective capacity.
    

**Storage characteristics**

- **File-first**: NFS, NFS over RDMA, GPU Direct Storage.
    
- Optional object/S3 over RDMA.
    
- Roadmap asks:
    
    - **Tiering** from VAST to object (including Blob).
        
    - Potential **Blob API compatibility over VAST** to preserve existing tooling.
        

**Network & data center layout**

- Preferred: VAST sits on the **physical GPU front-end RDMA network**, not behind Sirius, assuming security sign-off.
    
- Need confirmation that the **front-end network** (spanning **14 data halls**) is **non-blocking** at required throughput for storage.
    
- VAST would ideally occupy **3–4 contiguous rows** of racks on a single T0 network. Space constraints in the first half of 2026 may force more distributed placements initially.
    

**Integration**

- VAST provides its own **management plane**, which MAI already knows from CoreWeave.
    
- Must integrate with **Azure Active Directory** for auth and potentially hook into Microsoft/Nebius control workflows.
    

**Ramp model (high level)**

- First storage tranche live by **Jan 15 – Feb 1, 2026** to support ~**9K GPUs**.
    
- Second tranche by **June 1, 2026** to support ~**18K GPUs**.
    
- Additional tranches (July and September 2026) with ~9K+ GPUs each.
    
- Final state: ~**1.6 EB** and ~**192 Tbps** or higher.
    

---

### 4. Key Risks

- **Blob POR momentum:** Blob-based storage and Sirius networking plans are already in motion; a pivot or supplement will need **program approvals**.
    
- **Network integration risk:** It is not yet confirmed that the GPU network is **non-blocking** for storage or that VAST can directly attach without Sirius.
    
- **Data hall constraints:** Early 2026 space constraints across **14 data halls** may prevent the ideal “contiguous rows” layout for VAST.
    
- **Supply chain:** Delivering up to **1.6 EB all-flash** in a 2026 ramp will require careful **flash and node availability planning**.
    
- **Owner availability:**
    
    - Nidi (prior POC owner) is leaving at the **end of the month**.
        
    - Bilal will be **OOO roughly Dec 3–16**, and his manager **Suresh** will act as DRI during that period.
        

---

### 5. Next Steps (VAST & Microsoft)

**Immediate (next 1–2 weeks)**

- **Bilal (Microsoft)**
    
    - Debrief **MAI** on the VAST option; confirm file-based preference, per‑GPU throughput (read/write) and capacity requirements by tranche.
        
    - Align with **Kanchan** on Microsoft’s requirements and whether VAST is a **pivot** vs a **supplement** to Blob.
        
- **Jason (VAST)**
    
    - Share **VAST sizing examples, deployment tables**, and management/API documentation with **Bilal and Suresh**.
        
- **Suresh (Microsoft)**
    
    - Schedule a **three-way technical workshop** with **Microsoft, MAI, and VAST** to pin down requirements and start the site design.
        
    - Work with networking to confirm **Nebius front-end/back-end topology**, whether storage can **attach to the physical GPU network** without Sirius, and what security controls are required.
        

**Before the early-December site survey**

- **Bilal (Microsoft)**
    
    - Confirm **site survey date/location** and determine if VAST can be included. If not, schedule a **separate Nebius site visit**.
        
    - Provide detailed **Gen10.3 POR specs** (rack, power, NIC, capacity, and Sirius overlay limits).
        
- **VAST**
    
    - Prepare for site survey: checklist for **power, cooling, rack adjacency, network connectivity, management plane access, security**.
        
    - Engage suppliers to validate **flash and node lead times** and propose a **tranche-based build plan** aligned to MAI’s 2026 GPU dates.
        
    - Draft **deduplication planning assumptions** (Lior) based on MAI-like datasets to set realistic **effective capacity targets**.
        

**Medium term (post-workshop / through 2026)**

- **Joint**
    
    - Finalize the **site design** (C/D node ratios, rack layout, network architecture) and **deployment model**(Azure storage hardware vs VAST ODM).
        
    - Establish a **work-back schedule** from MAI’s go-live dates for each GPU tranche and align on engineering resourcing.
        
- **VAST**
    
    - Prioritize engineering work for **Blob tiering** and **Blob API compatibility** based on the confirmed scope of the opportunity.
        

---

### 6. Asks from VAST Leadership

- **Endorse engineering investment** to:
    
    - Support **Blob tiering / Blob API over VAST** if MAI ranks that as critical.
        
    - Assign senior engineering resources for **network integration design** (direct GPU network attach) and **site survey**.
        
- **Support supply chain engagement**:
    
    - Authorize early conversations with **flash and ODM suppliers** for a multi‑EB, multi‑tranche 2026 ramp.
        
- **Executive cover**:
    
    - Be prepared to engage Microsoft at the **VP+ level** if/when a pivot from Blob to VAST is considered at the Nebius program steering group.
        

Happy to refine this further or turn it into a deck.

Best,  
[Your Name]

---

If you’d like, I can also break this into a one-page exec summary slide outline next.