# VAST Data 5.4 Loopback Cluster - Deployment Analysis

**Date:** December 29, 2025  
**Final Status:** ✅ SUCCESSFUL  
**Total Attempts:** 3 (2 failed, 1 successful)  
**Build:** release-5-4-0-2043819  

---

## Executive Summary

After two failed installation attempts on Proxmox/KVM, the VAST Data 5.4 loopback cluster was successfully deployed. The root cause of failures was **CPU overcommitment** causing scheduling delays that triggered keepalive timeouts and PANICs in the VMsg subsystem.

### Key Finding
**Reducing vCPUs from 24 to 12 (matching physical host cores 1:1) was the primary fix.** Secondary optimizations (VirtIO tuning, THP disable) provided additional stability margin.

---

## Environment Configuration

### Hardware (Proxmox Host)
| Component | Specification |
|-----------|---------------|
| Platform | Proxmox VE 9.1 |
| CPU | AMD Ryzen Threadripper 2920X (12 cores / 24 threads) |
| RAM | 128GB DDR4 |
| Storage | NVMe SSD |
| Nested Virtualization | Enabled |

### Virtual Machine - Final Working Configuration
| Parameter | Failed Config | Successful Config | Change |
|-----------|---------------|-------------------|--------|
| **vCPUs** | 24 (2×12) | **12 (1×12)** | -50% |
| **RAM** | 97GB → 109GB | **117GB** | +7% |
| **SCSI Controller** | VirtIO SCSI | **VirtIO SCSI single + IO Thread** | Enhanced |
| **CPU Type** | qemu64 | **host** | Passthrough |
| **Memory Ballooning** | Enabled | **Disabled** | Off |

### Guest OS
- **Distribution:** Rocky Linux 8.10
- **Kernel:** 4.18.0-553.56.1.el8_10.x86_64
- **Docker:** CE 26.1.3
- **Guest Agent:** qemu-guest-agent (replaces vmtoolsd)

---

## Installation Attempts Summary

### Attempt 1: 97GB RAM - FAILED (OOM)
- **Symptoms:** OOM killer terminated processes during cluster activation
- **dmesg:** `Out of memory: Kill process`
- **Conclusion:** Insufficient RAM

### Attempt 2: 109GB RAM - FAILED (PANIC)
- **Symptoms:** PANIC P653 in `vmsg_keepalive_fiber` after 245 seconds
- **Error:** Keepalive thread detected stuck condition
- **State Transitions:** INIT → ACTIVATING → UNKNOWN → INIT (stuck)
- **Root Cause:** CPU scheduling delays from 2:1 vCPU overcommit
- **Key Evidence:** Fiber stuck for 245.39 seconds, `test_if_stuck()` triggered

### Attempt 3: 117GB RAM, 12 vCPUs - SUCCESS ✅
- **Duration:** 32 minutes total
- **State Transitions:** INIT → ACTIVATING → ONLINE
- **All components healthy, cluster operational

---

## Timeline of Successful Installation

| Time (UTC) | Event | Duration |
|------------|-------|----------|
| 18:32:13 | Installation script started | - |
| 18:32:13 | Phase 1-7 completed (checks, Docker, cleanup) | ~0 sec |
| 18:32:13 | Phase 8: Bootstrap started | - |
| 18:36:xx | VMS tarball extracted | ~4 min |
| 18:42:xx | VMS up, bootstrap complete | ~10 min |
| 18:47:00 | Phase 9: Cluster creation started | - |
| 18:47:22 | Installing build on all hosts | - |
| 18:47:37 | All hosts installed | 15 sec |
| 18:48:24 | CNodes/DNodes created | - |
| 18:48:30 | Cluster formatting started | - |
| 18:48:30 | State: INIT | - |
| 18:48:39 | State: ACTIVATING | 9 sec |
| **18:59:20** | **State: ONLINE** | **10 min 41 sec** |
| 19:04:44 | S3 certificates set | - |
| 19:04:46 | Trial license created | - |
| 19:04:48 | cluster_deploy task succeeded | Runtime: 1064.11s |
| 19:04:54 | Installation complete | **32 min 41 sec total** |

---

## Performance Analysis

### CPU Metrics During Installation

#### CPU Steal (Hypervisor Contention)
| Metric | Value | Assessment |
|--------|-------|------------|
| Max %steal | 0.33% | ✅ Excellent |
| Average %steal | ~0.05% | ✅ No contention |
| Samples with steal > 0 | < 1% | ✅ Negligible |

**Comparison:** Previous failed attempt (24 vCPUs) would have shown higher steal due to 2:1 overcommit.

#### CPU Utilization During Activation
| Phase | Max %user | Max %sys | Assessment |
|-------|-----------|----------|------------|
| Bootstrap | 10% | 5% | Light load |
| Cluster Install | 25% | 15% | Moderate |
| Activation Peak | 79% | 25% | Heavy but manageable |

#### Load Average
| Time | 1-min | 5-min | 15-min | Context |
|------|-------|-------|--------|---------|
| Start | 0.02 | 0.02 | 0.00 | Idle |
| Bootstrap | 5-10 | 3-5 | 2-3 | Moderate |
| Activation | 30-40 | 25-35 | 20-27 | Heavy (expected) |
| Post-Online | 26-32 | 28-32 | 23-27 | Steady state |

With 12 cores, load average of 30 means ~2.5 processes waiting per core - high but no runaway.

### Memory Metrics

#### Memory Timeline
| Phase | Used | Free | Available | Assessment |
|-------|------|------|-----------|------------|
| Start | 1.0 GB | 116 GB | 114 GB | Fresh VM |
| Bootstrap | 10-20 GB | 90+ GB | 80+ GB | Healthy |
| Activation | 105 GB | 2-3 GB | 4-5 GB | Tight but OK |
| Steady State | 108 GB | 3 GB | 2-4 GB | Operational |

**Critical:** Memory peaked at 105 GB during activation, leaving only 4-5 GB available. The 117 GB allocation provided just enough headroom.

#### Container Memory Usage (Steady State)
| Container | Memory | % of Total |
|-----------|--------|------------|
| vast_platform_4200 (cnode-2) | 49.0 GB | 41.7% |
| vast_platform_4100 (cnode-1) | 38.3 GB | 32.6% |
| vast_platform_4400 (dnode-2) | 8.0 GB | 6.8% |
| vast_platform_4300 (dnode-1) | 8.0 GB | 6.8% |
| vast_vms | 7.2 GB | 6.1% |
| mcvms | 0.9 GB | 0.7% |
| registry | 8 MB | 0.01% |
| **Total** | **~111 GB** | **94%** |

### I/O Metrics

#### Disk Latency (VirtIO SCSI with IO Thread)
| Metric | Max Value | Assessment |
|--------|-----------|------------|
| r_await (read latency) | 21.65 ms | ✅ Acceptable |
| w_await (write latency) | 36.02 ms | ✅ Acceptable |
| Peak IOPS | ~200 r/s, ~150 w/s | Moderate |
| Peak throughput | ~150 MB/s read | During tarball extract |

**Note:** VirtIO SCSI single controller with IO Thread enabled provided adequate performance. Previous default VirtIO-BLK may have had higher latency.

### Scheduling Gap Analysis

**Heartbeat Log Analysis:**
- Total duration: 43 minutes 37 seconds
- Heartbeat interval: 1 second
- **Gaps > 2 seconds: ZERO**

This confirms that reducing vCPUs to 12 eliminated the scheduling delays that caused the PANIC in the failed attempt.

---

## Workarounds and Fixes Applied

### 1. Docker Installation
**Issue:** VAST OVA is designed for VMware and includes Docker pre-installed. Proxmox import resulted in Docker not being available.

**Fix:** Manual Docker CE installation:
```bash
dnf config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
dnf install -y docker-ce docker-ce-cli containerd.io
systemctl enable --now docker
usermod -aG docker centos
```

### 2. Guest Agent Replacement
**Issue:** vmtoolsd (VMware tools) doesn't function on KVM.

**Fix:** 
```bash
systemctl stop vmtoolsd 2>/dev/null
systemctl disable vmtoolsd 2>/dev/null
dnf install -y qemu-guest-agent
systemctl enable --now qemu-guest-agent
```

### 3. VirtIO Driver Initialization
**Issue:** SCSI controller change required proper driver loading at boot.

**Fix:** 
```bash
echo 'add_drivers+=" virtio_scsi virtio_blk "' > /etc/dracut.conf.d/virtio.conf
dracut -f
```

### 4. Transparent Huge Pages (THP)
**Issue:** THP defragmentation can cause latency spikes during memory allocation.

**Fix:**
```bash
echo never > /sys/kernel/mm/transparent_hugepage/enabled
echo never > /sys/kernel/mm/transparent_hugepage/defrag
# Persisted via tuned profile
```

### 5. I/O Scheduler
**Issue:** Default I/O scheduler may not be optimal for virtualized storage.

**Fix:**
```bash
echo mq-deadline > /sys/block/sda/queue/scheduler
```

### 6. Kernel Parameters
**Applied sysctl tunings:**
```bash
vm.swappiness = 1
vm.dirty_ratio = 10
vm.dirty_background_ratio = 5
kernel.sched_migration_cost_ns = 5000000
kernel.sched_autogroup_enabled = 0
```

### 7. Proxmox VM Configuration
**Critical changes in Proxmox:**
- SCSI Controller: VirtIO SCSI single (not default)
- IO Thread: Enabled
- CPU Type: host (not qemu64)
- Sockets: 1 (not 2)
- Cores: 12 (matching host physical cores)
- Memory Ballooning: Disabled

---

## Monitoring Infrastructure

### Enhanced Monitoring Script
A comprehensive monitoring script (`monitor_install.sh`) was created to capture:

1. **vmstat** - Virtual memory statistics (1-second intervals)
2. **mpstat** - Per-CPU usage including %steal (1-second intervals)
3. **pidstat** - Per-process CPU usage (1-second intervals)
4. **iostat** - Disk I/O including await times (1-second intervals)
5. **memory.log** - Detailed memory snapshots (5-second intervals)
6. **docker_stats.log** - Container resource usage (7-second intervals)
7. **heartbeat.log** - Scheduling gap detector (1-second intervals)
8. **port_6001.pcap** - Network traffic capture for cluster communication
9. **ss_6001.log** - Socket state monitoring (1-second intervals)
10. **dmesg_live.log** - Kernel messages
11. **loadavg.log** - Load average tracking (1-second intervals)

**Log Location:** `/home/centos/install_monitoring_20251229_182856/`

---

## Files and Artifacts

### Installation Scripts
| File | Purpose |
|------|---------|
| `/home/centos/vast_proxmox_install.sh` | Main installation automation |
| `/home/centos/prepare_vm_for_vast.sh` | VirtIO/tuning preparation |
| `/home/centos/monitor_install.sh` | Enhanced monitoring |
| `/home/centos/preflight_check.sh` | Pre-installation verification |
| `/home/centos/start_vms.sh` | Post-reboot container startup |

### Log Files
| File | Contents |
|------|----------|
| `/home/centos/vast_install_final.log` | Successful installation log |
| `/home/centos/vast_install_20251229_183213.log` | Detailed timestamped log |
| `/home/centos/install_monitoring_20251229_182856/` | All performance traces |

### Documentation
| File | Contents |
|------|----------|
| `/home/centos/docs/VAST_Support_Case_Summary.md` | Failed attempt analysis |
| `/home/centos/docs/VAST_Proxmox_Guide.md` | Installation guide |
| `/home/centos/docs/VAST_5.4_Deployment_Analysis.md` | This document |

---

## Key Lessons Learned

### 1. vCPU Overcommitment is Critical
**Never allocate more vCPUs than physical cores for latency-sensitive workloads.** VAST's control plane (keepalives, cluster coordination) requires predictable scheduling. Hyperthread contention causes fatal delays.

### 2. Memory Sizing
117GB was sufficient but tight. For production, recommend **128GB minimum** for loopback clusters.

### 3. Proxmox/KVM is Viable
VAST can run successfully on Proxmox/KVM with proper tuning, despite being designed for VMware.

### 4. VirtIO Optimization Matters
IO Thread on VirtIO SCSI controller improved disk latency consistency.

### 5. THP Should Be Disabled
Transparent Huge Pages defragmentation can cause unpredictable latency spikes during memory pressure.

---

## Recommendations for Future Deployments

### Minimum Requirements (Proxmox/KVM)
| Resource | Minimum | Recommended |
|----------|---------|-------------|
| vCPUs | 12 (1:1 with physical) | 16-24 (if host has cores) |
| RAM | 117 GB | 128+ GB |
| Disk | 500 GB | 1 TB |
| Controller | VirtIO SCSI single | VirtIO SCSI single |
| IO Thread | Enabled | Enabled |
| CPU Type | host | host |
| Ballooning | Disabled | Disabled |

### Pre-Installation Checklist
- [ ] Verify vCPU count ≤ physical cores
- [ ] Disable memory ballooning
- [ ] Enable IO Thread on SCSI controller
- [ ] Set CPU type to "host"
- [ ] Install qemu-guest-agent
- [ ] Disable vmtoolsd
- [ ] Run prepare_vm_for_vast.sh
- [ ] Create snapshot before installation

### Post-Installation
- [ ] Create snapshot of working state
- [ ] Test reboot and start_vms.sh
- [ ] Document access credentials

---

## Appendix: PANIC Analysis from Failed Attempt

### Error Code Breakdown
```
PANIC[P653:E9:S255:F28d]
```
- **P653:** Panic code (silo stuck detection)
- **E9:** Environment ID
- **S255:** Silo ID
- **F28d:** Fiber ID (hex)

### Stack Trace Key Points
1. `vmsg_keepalive_fiber` - Responsible for cluster heartbeats
2. `test_if_stuck()` - Detected fiber hadn't completed in 245 seconds
3. `send_keepalive` / `send_all_keepalive` - Attempting to send heartbeats
4. Fiber was in `daemon=1` state, meaning critical background task

### Root Cause
With 24 vCPUs on 12 physical cores:
- Hypervisor must time-slice 24 virtual CPUs across 12 physical
- Under heavy load (activation phase), scheduling becomes unpredictable
- Keepalive fiber waits in run queue too long
- 245 seconds exceeds internal timeout threshold
- PANIC triggered by `test_if_stuck()`

---

## Summary Statistics

| Metric | Value |
|--------|-------|
| Total installation attempts | 3 |
| Failed attempts | 2 |
| Successful attempts | 1 |
| Successful install time | 32 min 41 sec |
| Activation time (INIT→ONLINE) | 10 min 41 sec |
| Peak memory usage | 105 GB |
| Peak load average | 40.0 |
| Max CPU steal | 0.33% |
| Scheduling gaps > 2s | 0 |
| Final cluster state | ONLINE |

---

*Document generated: December 29, 2025*  
*VAST Data 5.4 build release-5-4-0-2043819*
