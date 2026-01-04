# Host Configuration

← [Documentation Index](../index.md)

## Hardware Overview

The infrastructure consists of 7 hosts distributed across 3 physical locations, providing high availability and performance scaling for different workload types.

### Host Summary

| Host | Type | CPU | RAM | Storage | GPU | Role | Location |
|------|------|-----|-----|---------|-----|------|----------|
| home1 | BESSTAR UM250 | AMD Ryzen 5 PRO 2500U | 16 GB | 500 GB NVMe | AMD Vega 8 | manager | Server Closet |
| home2 | NEO J50C-4 Max | Intel Pentium Silver J5005 | 8 GB | 256 GB NVMe | Intel UHD 605 | manager | Compute Rack |
| home3 | NEO J50C-8SE | Intel Celeron J4125 | 8 GB | 256 GB NVMe | Intel UHD 600 | manager | Studio |
| oro | Gigabyte X399 | AMD Threadripper 2950X | 128 GB | 3×1 TB NVMe | 2xRTX 4070 | worker | Compute Rack |
| opal | Gigabyte X399 | AMD Threadripper 2950X | 128 GB | 3×1 TB NVMe | 2xRTX 4070 | worker | Compute Rack |
| onyx | Gigabyte X399 | AMD Threadripper 2920X | 128 GB | 3×1 TB NVMe | 2xRTX 3060 | worker | Compute Rack |
| obsidian | Synology | Celeron J4125 | 8 GB | 4×8 TB HDD | none | storage | Compute Rack |

## Manager Nodes (Mini PC Class)

### home1 - BESSTAR UM250
- **Model**: BESSTAR UM250 Mini PC
- **CPU**: AMD Ryzen 5 PRO 2500U (4C/8T, up to 3.6 GHz)
- **RAM**: 16 GB DDR4-2400 SO-DIMM
- **Storage**: 500 GB NVMe SSD (Samsung 990 EVO Plus)
- **GPU**: AMD Radeon Vega 8 (integrated)
- **Network**: Gigabit Ethernet + Wi-Fi 5
- **Power**: 65W TDP, external power adapter

### home2 - NEO J50C-4 Max
- **Model**: NEO J50C-4 Max Mini PC
- **CPU**: Intel Pentium Silver J5005 (4C/4T, up to 2.8 GHz)
- **RAM**: 8 GB DDR4-2400 SO-DIMM
- **Storage**: 256 GB NVMe SSD (Kingston OM8PCP3)
- **GPU**: Intel UHD Graphics 605 (integrated)
- **Network**: Gigabit Ethernet + Wi-Fi 5
- **Power**: 10W TDP, external power adapter

### home3 - NEO J50C-8SE
- **Model**: NEO J50C-8SE Mini PC
- **CPU**: Intel Celeron J4125 (4C/4T, up to 2.7 GHz)
- **RAM**: 8 GB DDR4-2400 SO-DIMM
- **Storage**: 256 GB NVMe SSD (Kingston OM8PCP3)
- **GPU**: Intel UHD Graphics 600 (integrated)
- **Network**: Gigabit Ethernet + Wi-Fi 5
- **Power**: 10W TDP, external power adapter

### Role Distribution
- **home1**: Primary networking services (NGINX, DNS, DDNS)
- **home2**: Backup management and monitoring coordination
- **home3**: Geographic redundancy and IoT hub backup

### Manager Quorum Benefits
- **3-node HA**: Survives loss of any single node
- **Split-brain Protection**: Odd number prevents ties
- **Load Distribution**: Management tasks spread across nodes
- **Geographic Separation**: Distributed across physical locations

## GPU Worker Nodes

### oro - Gigabyte X399 AORUS XTREME
- **Motherboard**: Gigabyte X399 AORUS XTREME
- **CPU**: AMD Ryzen Threadripper 2950X (16C/32T, up to 4.4 GHz)
- **RAM**: 128 GB DDR4-3600 (tood: verify module configuration)
- **Storage**:
  - 3×1 TB NVMe: Samsung 990 EVO Plus
- **GPU**: 2x NVIDIA RTX 4070 (tood: verify exact model)
- **Network**: 10 GbE (Netgear switch) + 1 GbE (Unifi)
- **Power**: tood: measure actual consumption

### opal - Gigabyte X399 AORUS XTREME
- **Motherboard**: Gigabyte X399 AORUS XTREME
- **CPU**: AMD Ryzen Threadripper 2950X (16C/32T, up to 4.4 GHz)
- **RAM**: 128 GB DDR4-3600 (tood: verify module configuration)
- **Storage**:
  - 3×1 TB NVMe: Samsung 990 EVO Plus
- **GPU**: 2x NVIDIA RTX 4070 (tood: verify exact model)
- **Network**: 10 GbE (Netgear switch) + 1 GbE (Unifi)
- **Power**: tood: measure actual consumption

### onyx - Gigabyte X399 AORUS XTREME
- **Motherboard**: Gigabyte X399 AORUS XTREME
- **CPU**: AMD Ryzen Threadripper 2920X (12C/24T, up to 4.3 GHz)
- **RAM**: 128 GB DDR4-3200 (tood: verify module configuration)
- **Storage**:
  - 3×1 TB NVMe: Samsung 990 EVO Plus
- **GPU**: 2x NVIDIA RTX 3060 (tood: verify exact model)
- **Network**: 10 GbE (Netgear switch) + 1 GbE (Unifi)
- **Power**: tood: measure actual consumption

### Performance Characteristics
- **AI/ML Workloads**: tood: calculate total VRAM (2x4070 + 2x4070 + 2x3060)
- **Compute**: 44 cores, 88 threads total across cluster
- **Memory**: 384 GB total system RAM (128 + 128 + 128 GB)
- **Storage**: 9 TB local NVMe across workers
- **Network**: 10 GbE backbone + 1 GbE backup

### Thermal Design
**tood**: Document actual thermal management strategy

- **Case**: tood: verify case models and cooling setup
- **CPU Cooling**: tood: document actual cooling solutions
- **Case Fans**: tood: document fan configuration
- **GPU**: tood: document GPU cooling approach
- **Basement Location**: Natural cooling advantage

## Storage Node (NAS)

### Synology DS920+ Specifications
- **CPU**: Intel Celeron J4125 (4C/4T, up to 2.7 GHz)
- **RAM**: 8 GB DDR4 (4 GB base + 4 GB upgrade)
- **Storage**: 4×8 TB WD Red Plus (WD80EFBX)
- **RAID**: SHR-1 (Synology Hybrid RAID with 1-disk redundancy)
- **Network**: 2×1 Gb Ethernet (bonded)
- **Expansion**: 2×M.2 NVMe cache slots (unused)

### Storage Configuration
- **Usable Capacity**: ~22 TB after RAID overhead
- **File Systems**: Btrfs with snapshots
- **Backup Strategy**: Local snapshots + offsite replication
- **Performance**: ~220 MB/s sequential via NFS

## Network Configuration

### Static IP Assignments

| Host | Primary IP | Management IP | MAC Address | Notes |
|------|------------|---------------|-------------|-------|
| home1 | 192.168.30.10 | 192.168.1.10 | 00:1e:c9:xx:xx:10 | Primary DNS/NGINX |
| home2 | 192.168.30.11 | 192.168.1.11 | 00:1e:c9:xx:xx:11 | Backup management |
| home3 | 192.168.30.12 | 192.168.1.12 | 00:1e:c9:xx:xx:12 | Studio management |
| oro | 192.168.30.20 | 192.168.1.20 | 90:2b:34:xx:xx:20 | GPU worker 1 |
| opal | 192.168.30.21 | 192.168.1.21 | 90:2b:34:xx:xx:21 | GPU worker 2 |
| onyx | 192.168.30.22 | 192.168.1.22 | 90:2b:34:xx:xx:22 | GPU worker 3 |
| obsidian | 192.168.30.30 | 192.168.1.30 | 00:11:32:xx:xx:30 | NAS storage |

### Network Performance
- **Manager Nodes**: 1 Gb Ethernet connections (home1, home2, home3)
- **Worker Nodes**: 10 GbE primary + 1 GbE backup (oro, opal, onyx)
- **Storage Node**: 10 GbE connection (obsidian/Synology)
- **ISP Connection**: 2.5 Gb symmetrical fiber (Nextlight)
- **Backup Internet**: Starlink (via UDM Pro Max secondary)
- **Cross-Connect**: 10 GbE + 1 GbE between server closet and basement

## Power and Cooling

### Power Consumption
**tood**: Measure actual power consumption for all hosts. Current data is placeholders.

| Host | Idle | Normal | Peak | Notes |
|------|------|--------|------|-------|
| home1 | tood | tood | tood | Mini PC, low power |
| home2 | tood | tood | tood | Mini PC, very low power |
| home3 | tood | tood | tood | Mini PC, very low power |
| oro | tood | tood | tood | Dual GPU workstation |
| opal | tood | tood | tood | Dual GPU workstation |
| onyx | tood | tood | tood | Dual GPU workstation |
| obsidian | tood | tood | tood | NAS, always-on storage |

### Thermal Management
- **Basement Advantage**: ~5°C cooler than main floors (estimated)
- **Rack Ventilation**: tood: document actual thermal design
- **Monitoring**: tood: implement temperature sensors
- **Alerts**: tood: configure thermal alerts

## Expansion Planning

### Short-term Capacity (6 months)
- **Current Utilization**:
  - CPU: ~30% average across workers
  - Memory: ~40% average across workers
  - Storage: ~60% of NAS capacity
- **Growth Headroom**: Can handle 2x current workload

### Medium-term Expansion (1-2 years)
- **Additional Workers**: Space and power for 2 more GPU nodes
- **Storage Expansion**: Synology DX517 5-bay expansion unit
- **Network Upgrade**: 25 Gb backbone when needed

### Long-term Architecture (3+ years)
- **Kubernetes Migration**: If workload complexity requires it
- **Edge Computing**: Additional NUC-class nodes for branch locations
- **Specialized Hardware**: Potential FPGA or ARM nodes for specific workloads

## Performance Baselines

**tood**: Establish actual performance baselines through testing

### Compute Benchmarks
- **Threadripper 2950X**: tood: run Cinebench R23 (oro, opal)
- **Threadripper 2920X**: tood: run Cinebench R23 (onyx)
- **GPU Performance**: tood: benchmark actual GPU configurations
  - oro: 2x RTX 4070 (tood: verify model and test)
  - opal: 2x RTX 4070 (tood: verify model and test)
  - onyx: 2x RTX 3060 (tood: verify model and test)

### Storage Performance
- **Local NVMe**: tood: benchmark Samsung 990 EVO Plus performance
- **NAS over NFS**: tood: test 10 GbE NAS performance
- **Network**: tood: validate 10 GbE throughput

### Availability Metrics
**tood**: Establish actual availability targets and measurements

- **Target Uptime**: tood: define SLA based on workload requirements
- **Planned Maintenance**: tood: establish maintenance windows
- **MTTR**: tood: measure mean time to recovery
- **MTBF**: tood: track hardware failure rates

---

**Next**: [Local Storage](storage-local.md) | **Related**: [Host Mapping](../01_physical/host-map.md)
