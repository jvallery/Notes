# VAST Data 5.4 Proxmox Deployment - Next Steps Guide

**Version:** 2.0  
**Date:** December 29, 2025  
**Status:** Ready for Next Deployment  

---

## Executive Summary

This guide consolidates all lessons learned from three deployment attempts and provides a complete, optimized path for the next VAST Data 5.4 loopback cluster deployment on Proxmox.

### Key Changes from v1

| Aspect | v1 (Current) | v2 (Next Deployment) |
|--------|--------------|----------------------|
| ZFS Topology | Mirror (RAID1) | **Stripe (RAID0)** |
| Usable Capacity | 422 GB | **~900 GB** |
| VM Disks | 1 (combined) | **2 (OS + Data)** |
| Data Filesystem | ext4 | **XFS** |
| ZFS Sync | Default | **Disabled** |
| vCPU Count | 12 | 12 (unchanged) |

---

## Hardware Requirements

### Proxmox Host

| Component | Minimum | Recommended | Notes |
|-----------|---------|-------------|-------|
| CPU | 12 cores | 16+ cores | Physical cores, not threads |
| RAM | 128 GB | 160+ GB | VAST VM needs 117GB+ |
| NVMe | 2× 1TB | 2× 2TB | For ZFS stripe |
| Boot Device | 50GB SSD | 100GB SSD | Separate from NVMe data pool |

### Memory Allocation Strategy

```
Total Host RAM:     128 GB
├── Proxmox OS:       2 GB
├── ZFS ARC:          2 GB  (metadata only with primarycache=metadata)
├── VM Overhead:      4 GB  (QEMU/KVM)
└── VAST VM:        120 GB  (allocate 117-120GB to VM)
```

---

## Pre-Deployment Checklist

### Hardware Preparation

- [ ] **Separate Boot Device:** Proxmox OS must NOT be on the NVMe drives
  - Use any SATA SSD (128GB+) or USB drive for Proxmox OS
  - This allows both NVMe drives to be dedicated to VAST data

- [ ] **BIOS Settings:**
  - Enable AMD-Vi / Intel VT-d (for future passthrough option)
  - Enable nested virtualization (for VAST containers)
  - Disable power saving features (for consistent latency)

### Proxmox Configuration

- [ ] **ZFS Pool Creation:**
  ```bash
  # On Proxmox host console/SSH
  
  # Identify NVMe devices
  lsblk | grep nvme
  # Example: nvme0n1 (1TB), nvme1n1 (1TB)
  
  # Create optimized stripe pool
  zpool create -o ashift=12 \
    -O compression=off \
    -O atime=off \
    -O xattr=sa \
    -O sync=disabled \
    -O recordsize=128K \
    -O primarycache=metadata \
    vastdata /dev/nvme0n1 /dev/nvme1n1
  
  # Verify
  zpool status vastdata
  # Expected: RAID0 stripe across both NVMe, ~1.9TB usable
  ```

- [ ] **Storage Configuration in Proxmox GUI:**
  - Datacenter → Storage → Add → ZFS
  - ID: `vastdata`
  - ZFS Pool: `vastdata`
  - Content: Disk image, Container
  - Thin provision: Yes

---

## VM Creation

### Create New VM (Recommended Fresh Start)

**Option A: GUI Method**

1. **General:**
   - VM ID: Choose (e.g., 100)
   - Name: `vast-loopback`

2. **OS:**
   - ISO: Rocky Linux 8.10 minimal
   - Type: Linux, Version: 8.x

3. **System:**
   - Machine: q35
   - BIOS: OVMF (UEFI)
   - SCSI Controller: **VirtIO SCSI single**
   - Qemu Agent: ✓ Checked

4. **Disks (Add Two):**

   | Disk | Storage | Size | Settings |
   |------|---------|------|----------|
   | scsi0 (OS) | local-lvm or vmtank | 50 GB | IO Thread ✓ |
   | scsi1 (Data) | vastdata | 1800 GB | IO Thread ✓, Cache: none, Discard ✓, AIO: native |

5. **CPU:**
   - Sockets: 1
   - Cores: 12 (match host physical cores)
   - Type: host
   - Enable NUMA: ✓

6. **Memory:**
   - Memory: 120000 MB (117 GB)
   - Ballooning: ✗ Unchecked

7. **Network:**
   - Model: VirtIO
   - Bridge: vmbr0 (your management network)

**Option B: CLI Method**

```bash
# Create VM with optimal settings
qm create 100 \
  --name vast-loopback \
  --machine q35 \
  --bios ovmf \
  --scsihw virtio-scsi-single \
  --agent 1 \
  --ostype l26 \
  --cpu host \
  --sockets 1 \
  --cores 12 \
  --numa 1 \
  --memory 120000 \
  --balloon 0 \
  --net0 virtio,bridge=vmbr0 \
  --scsi0 local-lvm:50,iothread=1 \
  --scsi1 vastdata:1800,iothread=1,cache=none,discard=on,aio=native \
  --ide2 local:iso/Rocky-8.10-x86_64-minimal.iso,media=cdrom \
  --boot order=ide2
```

---

## Rocky Linux Installation

### Minimal Installation

1. Boot from ISO
2. Select "Minimal Install" (no GUI needed)
3. **Disk Partitioning (CRITICAL):**
   - Select ONLY the 50GB disk (sda) for installation
   - Do NOT touch the 1.8TB disk (sdb) - it's for VAST data
   - Auto-partition is fine for OS disk:
     - /boot: 1GB
     - swap: 8GB (or minimal, VAST doesn't use it)
     - /: remainder (~40GB)

4. Set root password and create `centos` user with sudo
5. Complete installation and reboot

### Post-Installation Setup

```bash
# SSH into the new VM

# Update system
dnf update -y

# Install essential tools
dnf install -y \
  epel-release \
  vim wget curl \
  net-tools bind-utils \
  htop iotop \
  git \
  python3 python3-pip \
  parted xfsprogs

# Disable SELinux (VAST requirement)
setenforce 0
sed -i 's/SELINUX=enforcing/SELINUX=disabled/' /etc/selinux/config
```

---

## Data Disk Preparation

### Format and Mount the 1.8TB Data Disk

```bash
# Verify disk is visible
lsblk
# Should show sdb with 1.8T size

# Create partition
parted /dev/sdb mklabel gpt
parted /dev/sdb mkpart primary xfs 0% 100%

# Format as XFS (optimal for VAST's sparse files)
mkfs.xfs -f -n ftype=1 -i size=512 /dev/sdb1

# Create mount point
mkdir -p /vast

# Mount
mount -o noatime,nodiratime /dev/sdb1 /vast

# Add to fstab for persistence
echo '/dev/sdb1 /vast xfs defaults,noatime,nodiratime 0 0' >> /etc/fstab

# Set ownership
chown centos:centos /vast

# Verify
df -h /vast
# Should show ~1.8TB available
```

### Why XFS?

- Better handling of large sparse files (VAST virtual SSDs are 40GB sparse files)
- Better scalability for large directories
- Native support for direct I/O
- Lower fragmentation for large sequential writes

---

## VM Tuning

### Run the Preparation Script

```bash
# Copy preparation script to VM
scp prepare_vm_for_vast.sh centos@<vm-ip>:/home/centos/

# Run it
sudo /home/centos/prepare_vm_for_vast.sh
```

### Key Tuning Applied

| Setting | Value | Rationale |
|---------|-------|-----------|
| vm.swappiness | 1 | Minimize swap usage |
| THP | disabled | Prevent defrag latency spikes |
| I/O scheduler | mq-deadline | Optimal for VirtIO |
| ulimits | 1000000+ | VAST needs many file descriptors |
| VirtIO drivers | in initramfs | Ensure boot reliability |

---

## VAST Installation

### Transfer Installation Files

```bash
# On your workstation, copy files to VM
scp vastdata_release_2043819.vast.tar.gz centos@<vm-ip>:/home/centos/
scp vast_bootstrap.sh centos@<vm-ip>:/home/centos/
scp vast_proxmox_install_v2.sh centos@<vm-ip>:/home/centos/
```

### Create Snapshot Before Installation

```bash
# On Proxmox host
qm snapshot 100 pre-vast-install --description "Clean state before VAST installation"
```

### Run Installation

```bash
# On the VM
cd /home/centos

# Start monitoring in background
sudo ./monitor_install.sh start

# Run installation (as root or with sudo)
sudo ./vast_proxmox_install_v2.sh 2>&1 | tee vast_install.log

# After completion, stop monitoring
sudo ./monitor_install.sh stop
```

### Expected Timeline

| Phase | Duration | Description |
|-------|----------|-------------|
| Phase 0-7 | ~1 min | Data disk setup, system checks, Docker |
| Phase 8 | ~10 min | Bootstrap (tarball extraction, VMS startup) |
| Phase 9 | ~15 min | Cluster creation and activation |
| Phase 10-11 | ~5 min | Verification |
| **Total** | **~30-35 min** | Complete installation |

---

## Verification

### Check Cluster Status

```bash
# Web UI
curl -sk https://localhost/api/clusters/ | python3 -m json.tool

# CLI
/vast/data/11.0.0.1-4100/vms.sh vcli -c "show cluster"
```

### Check Usable Capacity

```bash
# In VAST CLI
/vast/data/11.0.0.1-4100/vms.sh vcli -c "show capacity"
```

**Expected Result:** ~900 GB usable (vs 422 GB before)

### Performance Test

```bash
# Test disk performance from VM
fio --name=vast-test --rw=randread --bs=4k --iodepth=32 \
    --numjobs=4 --size=1G --runtime=60 --filename=/vast/testfile

# Expected: >100K IOPS, <1ms latency
```

---

## Post-Installation

### Create Success Snapshot

```bash
# On Proxmox host
qm snapshot 100 vast-installed --description "VAST 5.4 successfully installed and online"
```

### Document Access Credentials

| Service | URL | Username | Password |
|---------|-----|----------|----------|
| Web UI | https://<vm-ip> | admin | 123456 |
| SSH | <vm-ip>:22 | centos | (your password) |

### Create start_vms.sh (if not exists)

```bash
cat > /home/centos/start_vms.sh << 'EOF'
#!/bin/bash
cd /vast/bundles/upgrades/*/
./vman.sh $(basename $(pwd)) /vast/deploy/ssh_key.pem start
EOF
chmod +x /home/centos/start_vms.sh
```

---

## Troubleshooting

### Common Issues

| Issue | Symptom | Solution |
|-------|---------|----------|
| PANIC during activation | Cluster goes ACTIVATING → UNKNOWN | Reduce vCPUs to match physical cores |
| OOM during activation | dmesg shows "Out of memory" | Increase VM RAM to 117GB+ |
| Bootstrap hangs | "starting VMS" for >20 min | Check Docker daemon, restart and retry |
| Low performance | IOPS << 50K | Verify IO Thread enabled, cache=none |

### Rollback Procedure

```bash
# On Proxmox host
qm rollback 100 pre-vast-install
```

---

## ZFS Monitoring (Host Side)

### Check Pool Health

```bash
# On Proxmox host
zpool status vastdata
zpool iostat -v vastdata 5
```

### Check ARC Usage

```bash
arc_summary | head -30
# ARC should be using minimal RAM with primarycache=metadata
```

### Check for Sync Writes

```bash
zpool iostat -v vastdata 1 | grep -v "^$"
# With sync=disabled, all writes should be async
```

---

## File Summary

All files are in `/home/centos/docs/`:

| File | Purpose |
|------|---------|
| `VAST_Next_Steps_Guide.md` | This document |
| `VAST_Performance_Optimization_Plan.md` | Detailed optimization analysis |
| `VAST_5.4_Deployment_Analysis.md` | Post-mortem of successful v1 install |
| `VAST_Support_Case_Summary.md` | Analysis of failed attempts |
| `scripts/vast_proxmox_install_v2.sh` | Updated installer with dual-disk support |
| `scripts/prepare_vm_for_vast.sh` | VM tuning script |
| `scripts/monitor_install.sh` | Performance monitoring |

---

## Capacity Calculation Reference

### Current (v1) - ZFS Mirror + Single Disk

```
Raw NVMe:            2.0 TB
ZFS Mirror (-50%):   1.0 TB
VM Disk:             1.0 TB
VAST EC (-53%):      0.42 TB (422 GB usable)
Efficiency:          21%
```

### Optimized (v2) - ZFS Stripe + Dual Disk

```
Raw NVMe:            2.0 TB
ZFS Stripe (-5%):    1.9 TB
VM Data Disk:        1.8 TB
VAST EC (-50%):      0.9 TB (900 GB usable)
Efficiency:          45%
```

### VAST Erasure Coding Overhead

VAST loopback uses a fixed configuration:
- 20 virtual SSDs
- n+4 parity (for 20 drives, that's ~20% parity overhead)
- Plus internal metadata, similarity reduction overhead
- **Effective usable: ~50% of raw virtual SSD capacity**

This is by design for data protection and cannot be disabled in loopback mode.

---

## Quick Reference Card

```
┌────────────────────────────────────────────────────────────┐
│                    VAST 5.4 QUICK REFERENCE                │
├────────────────────────────────────────────────────────────┤
│ Web UI:    https://<vm-ip>        admin / 123456           │
│ vCLI:      /vast/data/11.0.0.1-4100/vms.sh vcli            │
│ Shell:     /vast/data/11.0.0.1-4100/attachdocker.sh        │
│ Restart:   ./start_vms.sh                                   │
├────────────────────────────────────────────────────────────┤
│ Critical Settings (Proxmox VM):                             │
│   vCPUs:     ≤ Physical cores (12 for Threadripper 2920X)  │
│   RAM:       117 GB minimum, ballooning OFF                │
│   CPU Type:  host                                           │
│   Disk:      VirtIO SCSI single, IO Thread ON              │
├────────────────────────────────────────────────────────────┤
│ Critical Settings (ZFS Host):                               │
│   sync=disabled   compression=off   atime=off               │
│   recordsize=128K   primarycache=metadata                   │
└────────────────────────────────────────────────────────────┘
```

---

*Document Version: 2.0*  
*Last Updated: December 29, 2025*  
*For VAST Data build release-5-4-0-2043819*
