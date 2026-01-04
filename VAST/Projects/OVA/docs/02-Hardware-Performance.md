# Hardware and Performance Considerations

**Document:** 02-Hardware-Performance.md  
**Last Updated:** December 30, 2025  

---

## Overview

VAST Data is enterprise storage software designed for high-performance hardware. Running it in a homelab requires careful attention to resource allocation and performance tuning. This document covers hardware requirements, storage configuration, and performance optimization.

---

## Minimum Requirements

### Proxmox Host

| Resource | Minimum | Recommended | Notes |
|----------|---------|-------------|-------|
| **CPU** | 12 physical cores | 16+ cores | VAST needs dedicated cores |
| **RAM** | 128 GB | 160+ GB | VM needs 120GB, host needs overhead |
| **NVMe** | 1× 1 TB | 2× 1 TB+ | Dedicated to VAST, not shared |
| **Boot Drive** | 50 GB | 100 GB | Separate from NVMe data pool |
| **Network** | 1 GbE | 10 GbE | 1 GbE sufficient for loopback testing |

### VAST VM

| Resource | Minimum | Recommended | Notes |
|----------|---------|-------------|-------|
| **vCPUs** | 12 | 12 | **Never exceed physical core count** |
| **RAM** | 117 GB | 120 GB | Hard minimum - OOM below this |
| **OS Disk** | 200 GB | 200 GB | Holds `/vast` (bundles, containers, logs) |
| **Data Disk** | 1 TB | 2 TB | NVMe for `/vast/drives/` (virtual SSDs) |

> **⚠️ Storage Layout:** The OS disk must be **200 GB+** because `/vast/bundles/` (~20GB), Docker images (~15GB), and logs live on it. Only the virtual SSD files go on NVMe at `/vast/drives/`.

---

## CPU Allocation Considerations

### Observed Behavior

During deployment, we observed stability issues that *may* be related to CPU overcommitment. VAST uses tight timing constraints for cluster heartbeats, and when vCPUs compete for physical cores, processes can be delayed by hypervisor scheduling.

**However:** We did not definitively root-cause whether the observed PANIC events were caused by:
1. CPU overcommitment and hypervisor scheduling delays
2. FD exhaustion from the pip/monitor bug causing infinite retry loops
3. A combination of both factors

### Our Configuration

| Configuration | Physical Cores | vCPUs | Result |
|---------------|----------------|-------|--------|
| Initial | 12 | 24 | PANIC after 245 seconds |
| Final | 12 | 12 | Stable (after also fixing FD bugs) |

**Note:** The 1:1 mapping was applied *alongside* the FD limit and pip version fixes. Both may have contributed to stability.

### Recommendation

As a conservative approach, allocate vCPUs ≤ physical cores:

```
vCPUs ≤ Physical Cores (not threads!)
```

For a 12-core CPU (24 threads), allocate **maximum 12 vCPUs** to the VAST VM. This eliminates CPU overcommitment as a potential variable.

---

## Storage Architecture

### Option A: NVMe Passthrough (Recommended)

Pass NVMe devices directly to the VM for best performance:

```
┌─────────────────────────────────────────────────────────────┐
│                      Proxmox Host                           │
│                                                              │
│  ┌─────────────┐                                            │
│  │ Proxmox OS  │  (SATA SSD)                                │
│  └─────────────┘                                            │
│                                                              │
│  ┌─────────────────────────────────────────────────────────┐ │
│  │                      VAST VM                            │ │
│  │                                                         │ │
│  │  /dev/sda (50GB)     - OS disk (VirtIO, from VMDK)     │ │
│  │      └─ /vast/ (VAST binaries, config, containers)    │ │
│  │  /dev/nvme0n1 (1TB)  - PCIe passthrough NVMe #1        │ │
│  │  /dev/nvme1n1 (1TB)  - PCIe passthrough NVMe #2        │ │
│  │      └─ /vast/drives/ (virtual SSD files only)        │ │
│  │                                                         │ │
│  └─────────────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────────┘
```

**Advantages:**
- Near-native NVMe performance
- No hypervisor I/O overhead
- VM sees raw NVMe devices
- ~95% of bare metal performance

**Disadvantages:**
- More complex setup (IOMMU, device isolation)
- Devices exclusively owned by VM
- Can't snapshot device state easily

### Option B: ZFS Pool with Virtual Disk

If passthrough isn't possible, use a ZFS pool on the host:

```
┌─────────────────────────────────────────────────────────────┐
│                      Proxmox Host                           │
│                                                              │
│  ┌─────────────────────────────────────────────────────────┐ │
│  │                    ZFS Pool "vastdata"                  │ │
│  │              nvme0n1 + nvme1n1 (stripe/mirror)          │ │
│  │                                                         │ │
│  │  ┌─────────────────────────────────────────────────────┐│ │
│  │  │  VAST VM                                            ││ │
│  │  │                                                     ││ │
│  │  │  /dev/sda (50GB)  - OS disk                        ││ │
│  │  │  /dev/sdb (1.8TB) - zvol from vastdata pool        ││ │
│  │  │                                                     ││ │
│  │  └─────────────────────────────────────────────────────┘│ │
│  └─────────────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────────┘
```

#### ZFS Stripe vs Mirror

| Topology | Command | Usable Space | IOPS | Fault Tolerance |
|----------|---------|--------------|------|-----------------|
| **Stripe (RAID0)** | `zpool create vastdata nvme0n1 nvme1n1` | 2 TB | 2× single | None |
| **Mirror (RAID1)** | `zpool create vastdata mirror nvme0n1 nvme1n1` | 1 TB | 1× (2× read) | 1 drive |

**Recommendation:** Use **stripe** for homelab (2× capacity, 2× performance). Data loss on drive failure is acceptable for testing.

#### Optimized ZFS Pool Creation

> **⚠️ DATA LOSS RISK: BENCHMARK MODE ONLY**  
> The `sync=disabled` setting below **ignores fsync semantics** and will lose data on power loss. Only use for benchmarking or truly disposable data. For safer defaults, use `sync=standard`.

```bash
# Create high-performance stripe for VAST (BENCHMARK MODE)
zpool create -o ashift=12 \
  -O compression=off \
  -O atime=off \
  -O xattr=sa \
  -O sync=disabled \
  -O recordsize=128K \
  -O primarycache=metadata \
  vastdata /dev/nvme0n1 /dev/nvme1n1
```

**Settings Explained:**

| Setting | Value | Rationale |
|---------|-------|-----------|
| `ashift=12` | 4K sectors | Matches modern NVMe |
| `compression=off` | Disabled | VAST compresses internally |
| `atime=off` | No access time | Reduces metadata writes |
| `sync=disabled` | Async writes | VAST handles consistency |
| `recordsize=128K` | 128KB blocks | Matches VAST chunk size |
| `primarycache=metadata` | Metadata only | Avoid double-caching |

---

## PCIe Passthrough Setup

> **⚠️ SNAPSHOT WARNING**  
> Proxmox **cannot snapshot VMs with PCIe passthrough devices**. If you need snapshots:
> - Use ZFS zvol storage instead of passthrough, OR
> - Shutdown VM and use `vzdump` for offline backup, OR
> - Accept no snapshots and rely on VAST internal snapshots

### Step 1: Enable IOMMU

Edit `/etc/default/grub`:

```bash
# For AMD CPUs
GRUB_CMDLINE_LINUX_DEFAULT="quiet amd_iommu=on iommu=pt"

# For Intel CPUs
GRUB_CMDLINE_LINUX_DEFAULT="quiet intel_iommu=on iommu=pt"
```

Apply:
```bash
update-grub
reboot
```

### Step 2: Verify IOMMU Groups

```bash
# List IOMMU groups
for d in /sys/kernel/iommu_groups/*/devices/*; do
    n=${d#*/iommu_groups/*}; n=${n%%/*}
    printf 'IOMMU Group %s: ' "$n"
    lspci -nns "${d##*/}"
done | grep -i nvme
```

Ideal: Each NVMe in its own IOMMU group.

### Step 3: Blacklist NVMe from Host

Create `/etc/modprobe.d/vfio.conf`:

```bash
# Replace with your NVMe device IDs from lspci
options vfio-pci ids=144d:a808,144d:a808
```

Add VFIO modules to initramfs (`/etc/modules`):
```
vfio
vfio_iommu_type1
vfio_pci
vfio_virqfd
```

Update initramfs:
```bash
update-initramfs -u
reboot
```

### Step 4: Add to VM

In Proxmox GUI or CLI:

```bash
# Get device IDs
lspci -nn | grep -i nvme
# Example: 01:00.0 Non-Volatile memory controller [0108]: Samsung ...

# Add to VM
qm set <VMID> -hostpci0 01:00.0,pcie=1
qm set <VMID> -hostpci1 02:00.0,pcie=1
```

---

## VM Performance Tuning

### Proxmox VM Configuration

| Setting | Value | How to Set |
|---------|-------|------------|
| CPU Type | `host` | Hardware → CPU → Type |
| SCSI Controller | VirtIO SCSI single | Hardware → Add → Controller |
| IO Thread | Enabled | Each disk → Edit → IO Thread ✓ |
| Cache | None | Each disk → Edit → Cache: none |
| Discard | Enabled | Each disk → Edit → Discard ✓ |
| Ballooning | Disabled | Hardware → Memory → uncheck Ballooning |
| NUMA | Enabled | Hardware → Processors → Enable NUMA |

### Guest OS Tuning

#### Disable Transparent Huge Pages (Optional)

THP defragmentation may cause latency spikes. This is a common recommendation for latency-sensitive workloads, though we did not definitively prove it caused issues:

```bash
# Disable immediately
echo never > /sys/kernel/mm/transparent_hugepage/enabled
echo never > /sys/kernel/mm/transparent_hugepage/defrag

# Persist across reboots
cat << 'EOF' > /etc/systemd/system/disable-thp.service
[Unit]
Description=Disable Transparent Huge Pages
DefaultDependencies=no
After=sysinit.target local-fs.target
Before=basic.target

[Service]
Type=oneshot
ExecStart=/bin/sh -c 'echo never > /sys/kernel/mm/transparent_hugepage/enabled'
ExecStart=/bin/sh -c 'echo never > /sys/kernel/mm/transparent_hugepage/defrag'

[Install]
WantedBy=basic.target
EOF

systemctl daemon-reload
systemctl enable disable-thp
```

#### I/O Scheduler

For VirtIO disks, use `mq-deadline`:

```bash
# Set for current session
echo mq-deadline > /sys/block/sda/queue/scheduler

# Persist via udev rule
cat << 'EOF' > /etc/udev/rules.d/60-io-scheduler.rules
ACTION=="add|change", KERNEL=="sd[a-z]", ATTR{queue/scheduler}="mq-deadline"
ACTION=="add|change", KERNEL=="nvme[0-9]*", ATTR{queue/scheduler}="none"
EOF

udevadm control --reload-rules
```

#### Kernel Parameters

```bash
cat << 'EOF' > /etc/sysctl.d/99-vast-performance.conf
# Virtual memory
vm.swappiness = 1
vm.dirty_ratio = 10
vm.dirty_background_ratio = 5
vm.dirty_expire_centisecs = 500
vm.dirty_writeback_centisecs = 100

# Scheduler optimization for virtualization
kernel.sched_migration_cost_ns = 5000000
kernel.sched_autogroup_enabled = 0

# Network (for VAST cluster communication)
net.core.somaxconn = 65535
net.core.netdev_max_backlog = 65535
net.ipv4.tcp_max_syn_backlog = 65535

# File descriptors (critical for VAST)
fs.file-max = 8388608
fs.nr_open = 2097152
fs.inotify.max_user_watches = 524288
EOF

sysctl -p /etc/sysctl.d/99-vast-performance.conf
```

#### File Descriptor Limits

VAST loopback can exhaust default FD limits:

```bash
cat << 'EOF' > /etc/security/limits.d/99-vast.conf
* soft nofile 1048576
* hard nofile 1048576
root soft nofile 1048576
root hard nofile 1048576
* soft nproc 65535
* hard nproc 65535
EOF
```

**Important:** Log out and back in for limits to take effect.

---

## Performance Expectations

### Observed Metrics (Successful Deployment)

| Metric | Value | Notes |
|--------|-------|-------|
| **CPU steal** | 0.33% max | Excellent - no hypervisor contention |
| **Load average** | 20-26 (idle) | Normal for loopback mode |
| **Memory used** | 108 GB | Steady state with empty cluster |
| **Disk latency** | <40ms writes | Acceptable for VirtIO |
| **Install time** | ~32 minutes | Bootstrap + activation |

### Container Resource Usage

| Container | CPU | Memory | Purpose |
|-----------|-----|--------|---------|
| CNode-1 (4100) | 50-200% | 40 GB | Primary compute |
| CNode-2 (4200) | 50-150% | 40 GB | Secondary compute |
| DNode-1 (4300) | 50-100% | 8 GB | Data storage |
| DNode-2 (4400) | 50-100% | 8 GB | Data storage |
| VMS | 10-50% | 7 GB | Management |
| MCVMS | 5-20% | 1 GB | Multi-cluster API |

### Why Load Average is High

Even with an **empty cluster**, load average is 20-26 because:

1. **Busy-polling:** VAST data plane uses CPU polling, not interrupts
2. **Background processes:** Similarity detection, metadata maintenance
3. **Heartbeats:** Constant inter-node communication
4. **Software NVRAM:** CPU emulates hardware NVRAM

This is **expected behavior** for loopback mode. Physical VAST clusters offload this to dedicated hardware.

---

## Capacity Planning

### Virtual Drive Allocation

VAST creates sparse files in `/vast/drives/` (on NVMe, not OS disk):

| Drive Type | Default Size | Count | Total Allocation |
|------------|--------------|-------|------------------|
| SSD | 40 GB | 40 | 1.6 TB |
| NVRAM | 27 GB | 4 | 108 GB |
| **Total** | | | **~1.7 TB** |

After erasure coding (N+4 parity), usable capacity is ~**850 GB**.

### Increasing Capacity

With passthrough NVMe (2 TB total), potential usable capacity:
- 2 TB raw × ~45% efficiency = **~900 GB usable**

Capacity is configured at cluster creation time. See [05-Topology-Planning.md](05-Topology-Planning.md).

---

## Monitoring

### Real-Time Monitoring Commands

```bash
# File descriptor usage (critical)
watch -n 5 'cat /proc/sys/fs/file-nr'

# Container resources
docker stats --format "table {{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}"

# System load
htop

# Disk I/O
iostat -x 1

# CPU steal (for virtualization issues)
mpstat 1 | grep all
```

### Warning Signs

| Metric | Warning Level | Action |
|--------|--------------|--------|
| FD usage > 50% | Monitor closely | Check for retry loops |
| CPU steal > 5% | Reduce vCPUs | Hypervisor overloaded |
| Load > 50 (12 cores) | Investigate | Something is wrong |
| Memory > 115 GB | Danger zone | Risk of OOM |

---

*Previous: [01-Overview.md](01-Overview.md) | Next: [03-VM-Setup.md](03-VM-Setup.md)*
