Here’s a forwardable write‑up you can send to the Performance team. It distills what Google is asking for, how they want it measured, and how to fill the spreadsheet so we don’t miss any “gotchas.”

---

## Email draft to Performance team

**Subject:** Action required: Populate Google “VAST Data – GDC Storage RFP” performance + price/perf spreadsheet (NVMe/TCP, NFSv4, S3)

Team,  
Google’s GDC Storage group sent us an Excel template (“**19Dec2025 VAST Data - GDC Storage RFP V1.xlsx**”) that we must populate with **normalized performance + pricing data** for VAST. They will compare vendors primarily on **IOPS per GiB** and **price per GiB**, with throughput as a secondary dimension. We reviewed the format with them on a call today; the spreadsheet is now the official deliverable format.

### 1) What we must deliver back to Google

Please complete **both tabs** in the attached workbook:

1. **Tab: “PricePerformance Analysis”**  
    Populate all requested rows/columns for:
    

- **BLOCK (NVMe/TCP)**: **2 IOPS/GiB**, **5 IOPS/GiB**, **10 IOPS/GiB** sections (each has S/M/L/XL rows)
    
- **FILE (NFSv4)**: **2 IOPS/GiB** section (S/M/L/XL rows)
    
- **OBJECT (S3)**: **Standard class** + **Archive class** (each has S/M/L/XL rows)
    

2. **Tab: “Performance Profile”**  
    Provide **fio-based latency curves (Mean + P95) vs IOPS** for specific NVMe/TCP workloads (details below). Fill in the columns with the “model/specs,” config details for S/M/L/XL, and any notes.
    

Also: Google explicitly asked us to **disclose the benchmarking tool(s) and methodology** we used (fio etc.) along with results.

---

## 2) Global test assumptions Google expects (must follow)

These are listed at the top of the “PricePerformance Analysis” tab and were emphasized during the call:

### Block/File IOPS normalization requirements

- **Read/Write ratio:** **80/20**, **uniform random**
    
- **IO size for IOPS:** **4 KiB**
    
- **Latency target:** keep **Mean Latency < 2 ms**  
    _Interpretation:_ push performance but do **not** report IOPS that require mean latency >2ms. They want IOPS “under 2ms” for apples-to-apples.
    
- **Protocols:**
    
    - Block: **NVMe over TCP**
        
    - File: **NFSv4**
        
    - Object: **S3**
        

### Encryption requirements (must be enabled during benchmarks)

- **Encryption in transit:** **Enabled**  
    Google called out: **IPsec for file+block, TLS for S3**. They explicitly want benchmarks with encryption enabled because it impacts IOPS.
    
- **Encryption at rest:** **Enabled** (and they want a “2nd at-rest layer at tenant granularity or finer”)
    

### Data reduction settings

- **Dedupe + compression:** **Disabled for performance tests**
    
    - Use **random data** so results aren’t inflated by dedupe/compression.
        

### Object test realism constraint

- **Working set ≥ 20% of usable capacity**  
    This is to avoid measuring only cache behavior.
    

### Units (important)

- They standardize on **TiB/GiB**, not TB/GB.  
    Make sure we report capacities and any derived “per GiB” values consistently.
    

---

## 3) Specific spreadsheet sections and exactly what to fill

### A) “PricePerformance Analysis” tab

#### BLOCK sections (NVMe/TCP) — 2 / 5 / 10 IOPS per GiB

Each of the 3 block sections has **Small (~112TiB usable), Med (~256TiB), Large (~512TiB), X‑Large (~1PiB)**.

For each row, please fill:

- **Usable capacity w/o dedupe/compression** (TiB)
    
- **Usable capacity with dedupe/compression** (TiB)  
    (This can be an **estimated “typical mixed private cloud”** number; see notes below.)
    
- **Raw capacity (TiB)**
    
- **All-in price** (must include **HW + SW + Support**) using Google’s requested commercial terms:  
    **60 months | 4‑hour support | Commercial**
    
- **Total IOPS** (for the 4KiB, 80/20 random workload under mean latency <2ms)
    
- **Max total read throughput** + **max total write throughput**
    
    - Also fill **“Throughput IO Size”** (e.g., 256KiB, 1MiB, etc.) and disclose the access pattern used for throughput (seq vs random) either in the notes column or the throughput fields.
        
- **Mean latency (ms)**
    
- **kW** and **Rack Units**
    
- **Configuration notes/details** (controller model/qty, drive model/type/qty/capacity; any key architecture notes)
    

And in the normalized columns, please compute + fill:

- **IOPS/GiB**
    
- **Read Throughput/GiB**
    
- **Write Throughput/GiB**
    
- **Price/GiB**
    

> Tip: For “per GiB” normalization, use the same baseline they are using to compare vendors (the sheet note says capacities are without dedupe/compression and assuming host-encrypted data). Practically, that means normalize using **usable capacity w/o dedupe/compression** unless Google later instructs otherwise.

#### FILE section (NFSv4) — 2 IOPS per GiB

Same structure as block (S/M/L/XL). Fill the same columns, but for **NFSv4**.

#### OBJECT sections (S3) — Standard + Archive classes

Object has different fields (and they left some per‑GiB columns intentionally blank). There are **two classes**:

- **OBJECT – Standard Storage Class**
    
    - Workload: **50/50 GET/PUT**, “new object PUTs,” uniform random GET access
        
    - Working set ≥ 20% usable capacity
        
    - Sizes: **Small (~300TiB usable), Med (~900TiB), Large (~1.5PiB), X‑Large (~5PiB)**
        
- **OBJECT – Archive Storage Class**
    
    - Workload: **10/90 GET/PUT**, “new object PUTs,” uniform random GET access
        
    - Same sizing rows as above
        

For each object row, fill:

- **Usable capacity with dedupe/compression** and **w/o dedupe/compression**
    
- **Raw capacity (TiB)**
    
- **All-in 60‑month price** (HW/SW/Support)
    
- **QPS @ 256KiB objects** (**include P95 latency disclosure**)
    
- **QPS @ 256MiB objects** (**include P95 latency disclosure**)
    
- **Max read throughput supported** (disclose **object size** and **# of buckets**)
    
- **Max write throughput supported** (same disclosure)
    
- **kW**, **rack units**
    
- **Config notes** (incl. erasure coding, layout assumptions)
    

---

## 4) “Performance Profile” tab — additional latency-vs-IOPS curves

This tab asks for:

**fio-based latency (Mean and P95) vs IOPS curves** for **NVMe/TCP** workloads, using:

- **Uniform random I/O distribution**
    
- **Sufficiently large disk volumes so peak IOPS density < 5 IOPS/GiB**
    

Workloads listed:

- 100/0 **8KiB** random read
    
- 50/50 **8KiB** random read/write
    
- 0/100 **8KiB** random write
    
- (Sheet shows “0/100 64KiB random read” — likely a typo)
    
- 50/50 **64KiB** random read/write
    
- (Sheet shows “100/0 64KiB random write” — likely a typo)
    

**Guidance:** Assume the intent is:

- **64KiB 100/0 random read**, and **64KiB 0/100 random write**  
    …but please **call out the assumption** in the “Comments” column (or email thread) so Google doesn’t interpret it as us ignoring the template.
    

What to put in the columns:

- **Storage Model & Specs:** testbed description (VAST SW version, controller model, drive type, network, encryption settings, client count)
    
- **Config Details (S/M/L/XL):** link each curve set to the same S/M/L/XL configs used in Tab 1
    
- **Comments:** any extrapolation, bottlenecks, deviations, or notes on how curves were generated
    

---

## 5) Important call outcomes / constraints to incorporate

These are things Google explicitly discussed with us:

### Self‑Encrypting Drives (SEDs)

- The template mentions **“Self encrypting drives with FIPS 140-2 or -3 certification.”**
    
- We stated on the call: **VAST does NOT support SEDs** (due to HA/dual-controller key mgmt complexity). We meet FIPS requirements via **dual software-layer encryption**.
    

**Action:** Do **not** spend time trying to test SED modes. Instead:

- Add an explicit note in **Configuration Notes/Details** that **SEDs are not used/supported**, and encryption is done in software layers.
    
- Coordinate with Security/Compliance to provide the standard positioning / any “one‑pager” language if needed for the final submission.
    

### “Nearest SKU” is acceptable (add rows for clarity)

Google understands vendors may not have an exact “112TiB usable” system. They explicitly suggested:

- If our smallest deliverable config is bigger (example discussed: 150TiB/223TiB vs requested 112TiB), **still fill the 112TiB line**, but **add an extra line** underneath explaining:
    
    - “To sell/support 112TiB, we must deploy X TiB hardware; here’s the actual price/perf,” and
        
    - optionally, “at X TiB you get more capacity/perf.”
        

### Data reduction numbers are estimates, performance tests should not benefit from them

- For performance testing, use random data so dedupe doesn’t inflate results.
    
- For capacity w/ dedupe/compression column: provide a **reasonable “mixed private cloud” estimate** (and state it’s an estimate).
    

---

## 6) What we need back from you (so we can reply to Google)

1. Completed workbook with both tabs filled.
    
2. A short methodology blurb we can paste into the email thread (tools used per protocol, client setup, fio parameters at a high level, encryption enabled confirmation).
    
3. Your estimated completion date so we can tell Google when we plan to submit.
    

---

## Quick checklist (sanity before sending)

-  Block/File IOPS numbers are **4KiB**, **80/20**, **uniform random**, **mean latency <2ms**
    
-  **Encryption in transit enabled** during tests; **encryption at rest enabled**
    
-  **Dedupe/compression disabled** for performance runs; random data
    
-  Object results include **QPS @ 256KiB + 256MiB** with **P95 latency disclosed**
    
-  Working set constraints observed (≥20% for object; and <5 IOPS/GiB density for the latency-curve tab)
    
-  All-in **60‑month, 4hr support, commercial** pricing populated (HW+SW+Support)
    
-  kW, rack units, and hardware/config notes filled
    
-  Note included: **SEDs not supported; software-based dual encryption**
    

---

If you want, I can also convert the above into a shorter “Slack-ready” version, but this email format is usually the easiest to forward and track as action items.