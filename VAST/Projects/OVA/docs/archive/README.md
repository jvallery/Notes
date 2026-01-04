# VAST Data 5.4 Proxmox Deployment - Documentation

**Project:** VAST Data 5.4 Loopback Cluster on Proxmox/KVM  
**Date:** December 29, 2025  
**Status:** ✅ Successfully Deployed (v1), Planning v2 Optimization  

---

## ⭐ START HERE

| If you want to... | Read this |
|-------------------|-----------|
| Deploy a new optimized cluster | [VAST_Next_Steps_Guide.md](VAST_Next_Steps_Guide.md) |
| Understand what we learned | [VAST_5.4_Deployment_Analysis.md](VAST_5.4_Deployment_Analysis.md) |
| Optimize storage performance | [VAST_Performance_Optimization_Plan.md](VAST_Performance_Optimization_Plan.md) |

---

## Quick Reference

### Access Points
| Service | URL/Path | Credentials |
|---------|----------|-------------|
| Web UI | https://192.168.30.109 | admin / 123456 |
| vCLI | `/vast/data/11.0.0.1-4100/vms.sh vcli` | - |
| CNode Shell | `/vast/data/11.0.0.1-4100/attachdocker.sh` | - |

### After Reboot
```bash
./start_vms.sh
```

---

## Documentation Index

### Main Documents

| File | Description |
|------|-------------|
| [VAST_Next_Steps_Guide.md](VAST_Next_Steps_Guide.md) | **START HERE** - Complete guide for next deployment |
| [VAST_Performance_Optimization_Plan.md](VAST_Performance_Optimization_Plan.md) | Dual-disk, ZFS stripe optimization plan |
| [VAST_5.4_Deployment_Analysis.md](VAST_5.4_Deployment_Analysis.md) | Post-mortem of successful v1 deployment |
| [VAST_Support_Case_Summary.md](VAST_Support_Case_Summary.md) | Failed attempt analysis (PANIC investigation) |
| [VAST_Proxmox_Guide.md](VAST_Proxmox_Guide.md) | Original step-by-step installation guide |

### Scripts

| File | Purpose |
|------|---------|
| [scripts/vast_proxmox_install_v2.sh](scripts/vast_proxmox_install_v2.sh) | **NEW** - Optimized installer with dual-disk support |
| [scripts/vast_proxmox_install.sh](scripts/vast_proxmox_install.sh) | Original installation automation |
| [scripts/prepare_vm_for_vast.sh](scripts/prepare_vm_for_vast.sh) | VirtIO/tuning preparation |
| [scripts/monitor_install.sh](scripts/monitor_install.sh) | Enhanced monitoring script |
| [scripts/preflight_check.sh](scripts/preflight_check.sh) | Pre-installation verification |
| [scripts/start_vms.sh](scripts/start_vms.sh) | Post-reboot container startup |

### Installation Logs

| File | Contents |
|------|----------|
| [install_logs/vast_install_final.log](install_logs/vast_install_final.log) | Successful installation log |
| [install_logs/vast_install_20251229_183213.log](install_logs/vast_install_20251229_183213.log) | Detailed timestamped log |

### Performance Traces

| File | Contents |
|------|----------|
| [monitoring_logs/METRICS_SUMMARY.md](monitoring_logs/METRICS_SUMMARY.md) | Key metrics summary |
| [monitoring_logs/mpstat.log](monitoring_logs/mpstat.log) | Per-CPU usage (1-sec intervals) |
| [monitoring_logs/vmstat.log](monitoring_logs/vmstat.log) | Virtual memory stats |
| [monitoring_logs/iostat.log](monitoring_logs/iostat.log) | Disk I/O latencies |
| [monitoring_logs/memory.log](monitoring_logs/memory.log) | Memory snapshots |
| [monitoring_logs/docker_stats.log](monitoring_logs/docker_stats.log) | Container resources |
| [monitoring_logs/heartbeat.log](monitoring_logs/heartbeat.log) | Scheduling gap detector |
| [monitoring_logs/pidstat.log](monitoring_logs/pidstat.log) | Per-process CPU |
| [monitoring_logs/loadavg.log](monitoring_logs/loadavg.log) | Load average tracking |
| [monitoring_logs/dmesg_live.log](monitoring_logs/dmesg_live.log) | Kernel messages |

---

## Key Findings Summary

### Root Cause of v1 Failures
**vCPU overcommitment (24 vCPUs on 12 physical cores)** caused scheduling delays that triggered PANIC in VAST's keepalive subsystem.

### v1 Solution (Current Deployment)
1. **Reduced vCPUs from 24 to 12** (1:1 with physical cores)
2. Enabled VirtIO SCSI with IO Thread
3. Set CPU type to "host"
4. Disabled memory ballooning
5. Disabled Transparent Huge Pages

### v2 Optimizations (Next Deployment)
1. **ZFS Stripe instead of Mirror** (2x capacity: 1TB → 2TB)
2. **Separate OS and Data disks** (no I/O contention)
3. **ZFS sync=disabled** (VAST handles consistency)
4. **XFS filesystem** (better sparse file handling)
5. **primarycache=metadata** (avoid double caching with VAST)

### Performance Results (v1)
| Metric | Value |
|--------|-------|
| CPU Steal (max) | 0.33% |
| Scheduling gaps > 2s | 0 |
| Install time | 32 min |
| Activation time | 10 min 41 sec |

### Expected Results (v2)
| Metric | v1 | v2 (Expected) |
|--------|-----|---------------|
| Usable Capacity | 422 GB | **~900 GB** |
| Sequential Write | ~500 MB/s | **~2 GB/s** |
| Random IOPS | ~50K | **~200K** |

---

## VM Configuration (Working)

```
CPU: 1 socket × 12 cores = 12 vCPUs
RAM: 117 GB (ballooning disabled)
Disk: 1 TB VirtIO SCSI single (IO Thread enabled)
CPU Type: host
Network: VirtIO
```

---

## Folder Structure

```
docs/
├── README.md                              # This file
├── VAST_Next_Steps_Guide.md               # ⭐ START HERE for next deployment
├── VAST_Performance_Optimization_Plan.md  # Detailed optimization analysis
├── VAST_5.4_Deployment_Analysis.md        # v1 deployment post-mortem
├── VAST_Support_Case_Summary.md           # Failed attempt analysis
├── VAST_Proxmox_Guide.md                  # Original installation guide
├── install_logs/                          # Installation output logs
│   ├── vast_install_final.log
│   ├── vast_install_20251229_*.log
│   └── nohup_install.log
├── monitoring_logs/                       # Performance traces
│   ├── METRICS_SUMMARY.md
│   ├── mpstat.log
│   ├── vmstat.log
│   ├── iostat.log
│   ├── memory.log
│   ├── docker_stats.log
│   ├── heartbeat.log
│   ├── pidstat.log
│   ├── loadavg.log
│   ├── dmesg_live.log
│   └── ss_6001.log
└── scripts/                               # All automation scripts
    ├── vast_proxmox_install_v2.sh         # ⭐ NEW optimized installer
    ├── vast_proxmox_install.sh            # Original installer
    ├── prepare_vm_for_vast.sh
    ├── monitor_install.sh
    ├── preflight_check.sh
    ├── start_vms.sh
    ├── disable_swap.sh
    └── clean_traces.sh
```

---

*Generated: December 29, 2025*
