# Topology Planning

**Document:** 05-Topology-Planning.md  
**Last Updated:** December 30, 2025  

---

## Overview

VAST loopback mode creates a miniature cluster within a single VM. This document covers:

- Understanding CNodes and DNodes
- Default topology configuration
- Virtual SSD and NVRAM sizing
- Tunable parameters
- Capacity planning

---

## VAST Architecture Basics

### CNodes (Compute Nodes)

CNodes handle:
- Client I/O (NFS, SMB, S3)
- Data plane processing
- Caching
- Protocol translation

In loopback mode, these run as Docker containers.

### DNodes (Data Nodes)

DNodes handle:
- Persistent storage
- Erasure coding
- Similarity reduction (deduplication)
- Background data operations

In loopback mode, these also run as containers with virtual "drives".

### VMS (VAST Management Service)

VMS provides:
- Web UI
- REST API
- Cluster management
- Task orchestration

---

## Default Loopback Topology

The standard loopback configuration:

```
┌─────────────────────────────────────────────────────────────┐
│                     VAST Loopback Cluster                    │
│                                                              │
│  ┌──────────────┐  ┌──────────────┐                         │
│  │   CNode-1    │  │   CNode-2    │   ← 2 Compute Nodes     │
│  │ 11.0.0.1-4100│  │ 11.0.0.1-4200│                         │
│  └──────────────┘  └──────────────┘                         │
│                                                              │
│  ┌──────────────┐  ┌──────────────┐                         │
│  │   DNode-1    │  │   DNode-2    │   ← 2 Data Nodes        │
│  │ 11.0.0.1-4300│  │ 11.0.0.1-4400│                         │
│  └──────────────┘  └──────────────┘                         │
│                                                              │
│  Storage:                                                    │
│  ├── 40 × Virtual SSDs (40 GB each)  = 1.6 TB raw            │
│  └── 4 × Virtual NVRAM (27 GB each)  = 108 GB               │
│                                                              │
│  After Erasure Coding (N+4 parity):                         │
│  └── ~850 GB usable capacity                               │
└─────────────────────────────────────────────────────────────┘
```

### Container Port Assignments

| Container | Base IP | Port Offset | Full Address |
|-----------|---------|-------------|--------------|
| CNode-1 | 11.0.0.1 | 4100 | 11.0.0.1-4100 |
| CNode-2 | 11.0.0.1 | 4200 | 11.0.0.1-4200 |
| DNode-1 | 11.0.0.1 | 4300 | 11.0.0.1-4300 |
| DNode-2 | 11.0.0.1 | 4400 | 11.0.0.1-4400 |

---

## Virtual Drive Configuration

### Default Values

From the VAST bootstrap, the default topology creates:

```json
{
  "dboxes": [{
    "ssd": {
      "size": "42949672960B",    // 40 GiB per drive (42,949,672,960 bytes)
      "drives_per_carrier": 1,
      "num_drives": 40           // 40 virtual SSDs (20 per D-Box)
    },
    "nvram": {
      "size": "28991029248B",    // ~27 GiB per drive
      "drives_per_carrier": 1,
      "num_drives": 4            // 4 virtual NVRAM (2 per D-Box)
    }
  }]
}
```

> **Note:** `42949672960B` = 40 GiB (not GB). VAST uses binary units internally.

### Drive Files

VAST creates sparse files in `/vast/drives/`:

```
/vast/drives/
├── dbox1_drive1   (40 GiB sparse, SSD)
├── dbox1_drive2   (40 GiB sparse, SSD)
├── ... (drives 3-20 for D-Box 1)
├── dbox1_drive20  (40 GB sparse, SSD)
├── dbox2_drive1   (40 GB sparse, SSD)
├── ... (drives 2-20 for D-Box 2)
├── dbox2_drive20  (40 GB sparse, SSD)
├── dbox1_nvram_1  (27 GB sparse, NVRAM)
├── dbox1_nvram_2  (27 GB sparse, NVRAM)
├── dbox2_nvram_1  (27 GiB sparse, NVRAM)
└── dbox2_nvram_2  (27 GiB sparse, NVRAM)
```

**Note:** These are sparse files - they start small and grow as data is written. With 2 D-Boxes, drives are distributed evenly (20 SSDs + 2 NVRAM per D-Box).

---

## Capacity Calculations

### Observed Topology Profiles

| Profile | Backing Storage | SSDs | Raw Capacity | Usable (observed) |
|---------|-----------------|------|--------------|-------------------|
| **1 TiB Backing** | 1× 1TB NVMe | 20 × 40 GiB | 800 GiB | ~422 GiB |
| **2 TiB Backing** | 2× 1TB NVMe | 40 × 40 GiB | 1.6 TiB | ~850 GiB |

> **Verify via API:**
> ```bash
> curl -sk -u admin:123456 https://localhost/api/capacity/ | jq
> ```

### Understanding Efficiency

```
Raw Drive Capacity:     40 × 40 GiB = 1.6 TiB
Erasure Coding:         N+4 parity (~10% overhead for 40 drives)
Metadata/Reserved:      ~20-25% additional
Similarity Tables:      Variable

Total Efficiency:       ~50-53%
Actual Usable:          ~850 GiB
```

### Factors Affecting Usable Capacity

1. **Erasure Coding:** N+4 parity uses ~20% for redundancy
2. **Metadata:** VAST stores file system metadata
3. **Similarity Tables:** Deduplication hash tables
4. **NVRAM Overhead:** Write logs and staging

---

## Customizing Topology

### When to Customize

- **More capacity:** Increase SSD count or size
- **Less resources:** Reduce CNode/DNode count
- **Testing specific scenarios:** Different protection levels

### Topology Configuration Options

The topology is defined at cluster creation time. Key parameters:

| Parameter | Default | Range | Notes |
|-----------|---------|-------|-------|
| CNode count | 2 | 1-4 | More = more client throughput |
| DNode count | 2 | 2-4 | Minimum 2 for redundancy |
| SSD count | 40 | 8-80+ | Split evenly across D-Boxes |
| SSD size | 40 GiB | 20-100 GiB | Larger = more capacity |
| NVRAM count | 4 | 2-8 | More = better write handling |
| NVRAM size | 27 GiB | 10-50 GiB | Larger = more write buffer |

> **⚠️ Note:** Topology is defined at cluster creation time and cannot be changed without destroying the cluster. Defaults shown are from build `release-5-4-0-2043819`.

### Capacity Planning Table

| SSD Config | Raw Capacity | Usable (est.) | Required NVMe Space |
|------------|--------------|---------------|---------------------|
| 20 × 40 GB | 800 GB | ~420 GB | 1 TB |
| 40 × 40 GB | 1.6 TB | ~850 GB | 2 TB |
| 40 × 80 GB | 3.2 TB | ~1.7 TB | 4 TB |
| 60 × 40 GB | 2.4 TB | ~1.3 TB | 3 TB |

**Note:** With 2 D-Boxes, SSDs are split evenly between them. For example, 40 total SSDs = 20 per D-Box.

**Rule of Thumb:** Provision ~2× the usable capacity you want as raw NVMe space.

---

## Resource Requirements by Topology

### CPU and Memory Scaling

| Topology | Min vCPUs | Min RAM | Notes |
|----------|-----------|---------|-------|
| 2C + 2D (default) | 12 | 117 GB | Standard loopback |
| 1C + 2D | 10 | 100 GB | Minimal viable |
| 2C + 4D | 16 | 140 GB | More storage capacity |
| 4C + 4D | 24 | 180 GB | Maximum for homelab |

### Container Memory Usage

Approximate memory per container type:

| Container Type | Typical Memory |
|----------------|----------------|
| CNode | 35-50 GB each |
| DNode | 6-10 GB each |
| VMS | 6-8 GB |
| MCVMS | 1 GB |
| Registry | < 100 MB |

---

## Modifying the Bootstrap

### Custom Topology File

The bootstrap reads topology from JSON. To customize:

1. Extract default topology from bootstrap
2. Modify parameters
3. Provide modified file to bootstrap

**Warning:** Custom topologies are not officially supported and may cause issues.

### Example: Larger SSDs

To use 80 GB SSDs instead of 40 GB:

```bash
# Modify after bootstrap but before cluster create
# The topology is in /vast/data/loopback_topology.json

# This is EXPERIMENTAL and may break things
```

---

## VIP Pool Configuration

### Default VIP Pools

| Pool | Range | Subnet | Purpose |
|------|-------|--------|---------|
| vippool-1 | 15.0.0.1 - 15.0.0.8 | /24 | NFS/SMB access |
| gateway-1 | 18.18.0.1 - 18.18.0.2 | /24 | Replication |

### Customizing VIP Pools

VIP pools are defined in the loopback configuration file:

```yaml
# /vast/deploy/loopback_conf.yml
name: lb-vast54
loopback: true
vip_pools:
   vippool-1:
     start_ip: '15.0.0.1'
     end_ip: '15.0.0.8'
     subnet_bits: 24
   gateway-1:
     role: 'replication'
     start_ip: '18.18.0.1'
     end_ip: '18.18.0.2'
     subnet_bits: 24
```

For external access (advanced), you could add real network IPs here.

---

## Configuration Variables for Install Script

Our install script supports topology customization via environment variables:

```bash
# config.env

# Cluster Configuration
CLUSTER_NAME="lb-vast54"
VAST_BUILD="release-5-4-0-2043819"

# Topology (for information - actual topology set by bootstrap)
CNODE_COUNT=2
DNODE_COUNT=2
SSD_COUNT=20
SSD_SIZE_GB=40
NVRAM_COUNT=4
NVRAM_SIZE_GB=27

# VIP Configuration
VIP_START="15.0.0.1"
VIP_END="15.0.0.8"
VIP_SUBNET=24
```

**Note:** Some parameters (like CNode/DNode count) are set by the bootstrap and can't be changed after cluster creation.

---

## Topology Best Practices

### For Homelab (Our Setup)

| Parameter | Recommendation |
|-----------|----------------|
| CNodes | 2 (default) |
| DNodes | 2 (default) |
| SSDs | 20-30 depending on space |
| SSD Size | 40-80 GB each |
| Total Raw | 1-2 TB |

### For Minimum Viable

If resources are tight:

| Parameter | Minimum |
|-----------|---------|
| CNodes | 1 |
| DNodes | 2 |
| SSDs | 8 |
| RAM | 100 GB |
| vCPUs | 10 |

### What NOT to Do

- ❌ Don't run with < 2 DNodes (no redundancy)
- ❌ Don't use < 8 SSDs (erasure coding needs minimum)
- ❌ Don't allocate > 12 vCPUs on 12-core host
- ❌ Don't use < 100 GB RAM (OOM risk)

---

## Viewing Current Topology

After cluster creation:

```bash
# Via Web UI
https://<vm-ip> → Cluster → Overview

# Via API
curl -sk -u admin:123456 'https://localhost/api/clusters/' | jq .

# Via vCLI
/vast/data/11.0.0.1-4100/vms.sh vcli -c "cluster show"

# Check virtual drives
ls -la /vast/drives/
du -sh /vast/drives/

# Check capacity
curl -sk -u admin:123456 'https://localhost/api/capacity/' | jq .
```

---

## Next Steps

1. **Pre-Install Tweaks:** [06-Pre-Install-Tweaks.md](06-Pre-Install-Tweaks.md) - Apply workarounds before installation
2. **Installation:** [07-Install-Script-Reference.md](07-Install-Script-Reference.md) - Run the automated installer

---

*Previous: [04-First-Boot.md](04-First-Boot.md) | Next: [06-Pre-Install-Tweaks.md](06-Pre-Install-Tweaks.md)*
