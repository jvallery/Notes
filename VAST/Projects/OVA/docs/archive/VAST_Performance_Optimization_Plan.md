# VAST Data 5.4 Performance Optimization Plan

**Date:** December 29, 2025  
**Status:** Planning Phase  
**Goal:** Maximize performance and usable capacity for VAST loopback cluster  

---

## Current State Analysis

### Storage Topology (Inefficient)

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         CURRENT ARCHITECTURE                            │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│   Proxmox Host                                                          │
│   ├── 2x 1TB NVMe (ZFS Mirror)                                          │
│   │   └── 1 TB usable (50% overhead for redundancy)                     │
│   │       └── 1 TB Virtual Disk (qcow2/raw)                             │
│   │           └── Rocky Linux ext4 filesystem                           │
│   │               └── /vast/drives/                                     │
│   │                   ├── 20x 40GB Virtual SSDs (800GB total)           │
│   │                   └── 4x 27GB Virtual NVRAM (108GB total)           │
│   │                       └── VAST Erasure Coding (n+4 parity)          │
│   │                           └── 422 GiB usable capacity               │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘

Capacity Loss Breakdown:
  Raw NVMe:           2.0 TB
  After ZFS Mirror:   1.0 TB  (-50% for RAID1)
  After VM overhead:  ~990 GB (-1% for partition tables)
  VAST virtual SSDs:  908 GB  (20x40GB + 4x27GB allocated)
  After Erasure Code: 422 GB  (-53% for n+4 parity across 20 drives)
  
  TOTAL EFFICIENCY:   21% of raw capacity
```

### Current Virtual Drive Configuration

From `/vast/data/loopback_topology.json`:
```json
{
  "ssd": {
    "size": "42949672960B",    // 40 GB per drive
    "drives_per_carrier": 1,
    "num_drives": 20           // 20 virtual SSDs
  },
  "nvram": {
    "size": "28GB",
    "num_drives": 4
  }
}
```

**Files in `/vast/drives/`:**
- 20 × dbox1_drive{1-20} @ 40GB each = 800GB allocated
- 4 × dbox1_nvram_{1-4} @ 27GB each = 108GB allocated
- Total: 908GB allocated, 17GB actual usage (sparse files)

---

## Proposed Architecture

### Option A: Separate Data Disk (Recommended)

```
┌─────────────────────────────────────────────────────────────────────────┐
│                      OPTIMIZED ARCHITECTURE                             │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│   Proxmox Host                                                          │
│   ├── Pool: vmtank (existing, any storage)                              │
│   │   └── 50 GB OS Disk (scsi0)                                         │
│   │       └── Rocky Linux / (root, boot, swap)                          │
│   │                                                                     │
│   └── Pool: vastdata (NEW - 2x NVMe RAID0)                              │
│       ├── sync=disabled (VAST handles its own consistency)              │
│       ├── compression=off (VAST compresses internally)                  │
│       ├── recordsize=128K (matches VAST chunk size)                     │
│       └── 1.8 TB Data Disk (scsi1)                                      │
│           ├── VirtIO SCSI single + IO Thread                            │
│           ├── cache=none, aio=native                                    │
│           └── XFS filesystem mounted at /vast                           │
│               └── VAST virtual drives                                   │
│                   └── ~900 GiB usable after EC                          │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘

Expected Capacity:
  Raw NVMe:           2.0 TB
  After ZFS Stripe:   1.9 TB  (-5% for ZFS overhead)
  VM Data Disk:       1.8 TB
  After Erasure Code: ~900 GB (53% of 1.8TB for EC)
  
  TOTAL EFFICIENCY:   45% of raw capacity (2x improvement)
```

### Option B: PCI Passthrough (Maximum Performance)

For absolute maximum performance, pass the NVMe devices directly to the VM:
- Bypasses ZFS, QEMU, VirtIO entirely
- VM sees raw NVMe devices
- Near-native performance (>95% of bare metal)
- Requires separate boot device for Proxmox

**Tradeoff:** More complex setup, requires additional boot device.

---

## Implementation Plan

### Phase 1: Proxmox Host Preparation

#### Step 1.1: Create High-Performance ZFS Pool

**On Proxmox host (via SSH or console):**

```bash
# CAUTION: This destroys all data on the NVMe drives!
# Ensure you have backups and Proxmox OS is on separate storage

# Identify NVMe devices
lsblk | grep nvme

# Destroy existing pool (if migrating from mirror)
# zpool destroy <existing-pool-name>

# Create striped pool optimized for performance
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
zfs list
```

**ZFS Settings Explained:**

| Setting | Value | Rationale |
|---------|-------|-----------|
| `sync=disabled` | Async writes | VAST handles its own write barriers. ZFS sync causes double-commit latency. |
| `compression=off` | No compression | VAST uses Similarity Reduction (already compressed). Re-compression wastes CPU. |
| `atime=off` | No access time | Reduces metadata writes |
| `recordsize=128K` | 128KB blocks | Matches VAST's internal chunk sizes for alignment |
| `primarycache=metadata` | Metadata-only ARC | VAST caches data in VM RAM. ARC for data = double caching. |

**Memory Consideration:**
- With `primarycache=metadata`, ZFS ARC will use minimal RAM (~1-2GB)
- This leaves more RAM for the VAST VM
- VAST's internal caching (in VM) is more efficient for its workload

#### Step 1.2: Create Data Disk for VM

```bash
# Create zvol for VAST data disk (90% of pool for headroom)
zfs create -V 1800G vastdata/vast-data-disk

# Or use thin provisioning
zfs create -V 1800G -s vastdata/vast-data-disk

# Verify
ls -la /dev/zvol/vastdata/
```

### Phase 2: VM Configuration

#### Step 2.1: Add Data Disk to VM

**Via Proxmox CLI:**

```bash
# Get VM ID
VMID=<your-vm-id>

# Add new data disk with optimized settings
qm set $VMID -scsi1 vastdata:vm-${VMID}-disk-1,size=1800G,iothread=1,cache=none,aio=native,discard=on

# Or if using zvol directly
qm set $VMID -scsi1 /dev/zvol/vastdata/vast-data-disk,iothread=1,cache=none,aio=native
```

**Via Proxmox GUI:**
1. VM → Hardware → Add → Hard Disk
2. Bus: SCSI (1)
3. Storage: vastdata
4. Size: 1800 GiB
5. Cache: none
6. Discard: checked
7. IO Thread: checked
8. Advanced:
   - Async IO: native

#### Step 2.2: Reduce OS Disk Size (New Installation)

For a fresh install, use a minimal OS disk:

```bash
# Create small OS disk on existing storage
qm set $VMID -scsi0 vmtank:50,iothread=1
```

### Phase 3: Guest OS Configuration

#### Step 3.1: Partition and Format Data Disk

**Inside the VM:**

```bash
# Identify new disk
lsblk

# Should show new disk (e.g., /dev/sdb with 1.8T)
# Partition the entire disk
parted /dev/sdb mklabel gpt
parted /dev/sdb mkpart primary xfs 0% 100%

# Format as XFS (better for large sparse files)
mkfs.xfs -f -n ftype=1 -i size=512 /dev/sdb1

# Create mount point
mkdir -p /vast_data

# Mount
mount /dev/sdb1 /vast_data

# Add to fstab
echo '/dev/sdb1 /vast_data xfs defaults,noatime,nodiratime 0 0' >> /etc/fstab

# Set ownership
chown centos:centos /vast_data
```

#### Step 3.2: Migrate VAST Data Location

**Before VAST installation (new cluster):**

```bash
# Create symlink for VAST to use the fast disk
mkdir -p /vast_data/vast
ln -s /vast_data/vast /vast

# Or configure VAST to use /vast_data directly during bootstrap
```

**For existing cluster (requires cluster recreation):**

```bash
# Stop VAST
cd /vast/bundles/upgrades/2043819
sudo ./vman.sh release-5-4-0-2043819 /vast/deploy/ssh_key.pem cluster stop

# Stop containers
sudo docker stop $(docker ps -q)

# Move data (preserves sparse files)
rsync -aHAXxSP /vast/ /vast_data/

# Replace original with symlink
sudo rm -rf /vast
sudo ln -s /vast_data /vast

# Restart
./start_vms.sh
```

### Phase 4: VAST Cluster Recreation (If Needed)

Since loopback topology is fixed at cluster creation, to get larger virtual drives:

#### Step 4.1: Clean Existing Installation

```bash
# Inside VM
sudo docker stop $(docker ps -q)
sudo docker rm $(docker ps -aq)
sudo rm -rf /vast/*
```

#### Step 4.2: Modify Loopback Topology (Advanced)

The loopback topology is generated by the bootstrap script. To customize:

```bash
# Create custom topology file
cat > /tmp/custom_topology.json << 'EOF'
{
  "user": "centos",
  "ip": "11.0.0.1",
  "cboxes": {
    "count": 1,
    "cnodes_per_cbox": 2
  },
  "dboxes": [
    {
      "dbox_type": "sanmina-active-passive",
      "nvram": {
        "size": "56GB",
        "drives_per_carrier": 1,
        "num_drives": 4
      },
      "ssd": {
        "size": "85899345920B",
        "drives_per_carrier": 1,
        "num_drives": 20
      }
    }
  ]
}
EOF
```

**Note:** Modifying the topology may not be supported. The bootstrap script generates this automatically based on available resources. You may need to:
1. Increase the VM disk size first
2. Re-run bootstrap with `--skip-prompt`
3. VAST will auto-detect available space

---

## Updated Installation Script

### Modified `vast_proxmox_install.sh` for Dual-Disk Setup

Key changes needed:

```bash
# Add to Phase 5: Preparing VAST directories
prepare_vast_data_disk() {
    log_step "Preparing VAST data disk"
    
    # Check for secondary disk
    if [[ -b /dev/sdb ]]; then
        if ! mountpoint -q /vast; then
            log_info "Formatting and mounting data disk..."
            
            # Only format if not already formatted
            if ! blkid /dev/sdb1 &>/dev/null; then
                parted /dev/sdb mklabel gpt -s
                parted /dev/sdb mkpart primary xfs 0% 100% -s
                mkfs.xfs -f -n ftype=1 -i size=512 /dev/sdb1
            fi
            
            # Mount
            mkdir -p /vast
            mount /dev/sdb1 /vast
            
            # Add to fstab if not present
            grep -q '/vast' /etc/fstab || \
                echo '/dev/sdb1 /vast xfs defaults,noatime,nodiratime 0 0' >> /etc/fstab
            
            chown centos:centos /vast
            log_info "Data disk mounted at /vast ✓"
        else
            log_info "Data disk already mounted at /vast ✓"
        fi
    else
        log_warn "No secondary disk found. Using root filesystem for /vast"
    fi
}
```

---

## Performance Comparison

### Expected Performance Gains

| Metric | Current Setup | Optimized Setup | Improvement |
|--------|---------------|-----------------|-------------|
| **Usable Capacity** | 422 GB | ~900 GB | **2.1x** |
| **Sequential Write** | ~500 MB/s | ~2 GB/s | **4x** |
| **Sequential Read** | ~800 MB/s | ~3 GB/s | **3.7x** |
| **Random 4K IOPS** | ~50K | ~200K | **4x** |
| **Write Latency** | 2-5ms | <1ms | **2-5x** |

### Why These Gains?

1. **ZFS Stripe vs Mirror**: 2x raw throughput (both NVMe working in parallel)
2. **sync=disabled**: Removes ZFS write barrier latency (~10ms → 0ms)
3. **Separate Data Disk**: No I/O contention with OS operations
4. **IO Thread**: Dedicated thread for disk I/O, no QEMU bottleneck
5. **XFS vs ext4**: Better sparse file handling for virtual SSDs

---

## Risk Assessment

| Risk | Mitigation |
|------|------------|
| **NVMe failure = data loss** | Acceptable for test environment. Production would use physical VAST cluster. |
| **sync=disabled = data loss on host crash** | VAST maintains internal consistency. Host crash during write → worst case lose last few seconds of writes. Acceptable for testing. |
| **Performance testing only** | This config is NOT for production data. Document clearly. |

---

## Pre-Deployment Checklist

### Proxmox Host

- [ ] Identify NVMe devices: `lsblk | grep nvme`
- [ ] Backup any data on existing ZFS pool
- [ ] Verify Proxmox OS is NOT on the NVMe drives
- [ ] Create ZFS stripe pool with optimized settings
- [ ] Create zvol or dataset for VAST data disk
- [ ] Add disk to VM with optimized settings

### VM Preparation

- [ ] Boot VM with new data disk attached
- [ ] Verify disk visible: `lsblk`
- [ ] Format with XFS
- [ ] Mount at /vast or /vast_data
- [ ] Update fstab for persistence
- [ ] Create snapshot before VAST installation

### VAST Installation

- [ ] Run prepare_vm_for_vast.sh
- [ ] Run preflight_check.sh
- [ ] Start monitoring: `monitor_install.sh start`
- [ ] Run vast_proxmox_install.sh
- [ ] Verify cluster online
- [ ] Check usable capacity in VAST UI

---

## Quick Reference Commands

### Proxmox Host

```bash
# Check pool status
zpool status vastdata
zfs list

# Monitor I/O
zpool iostat -v 1

# Check ARC usage (should be low with metadata-only caching)
arc_summary | head -50
```

### VM Guest

```bash
# Check disk performance
fio --name=test --rw=randread --bs=4k --iodepth=32 --numjobs=4 \
    --size=1G --runtime=60 --filename=/vast/testfile

# Monitor I/O
iostat -xz 1

# Check VAST capacity
/vast/data/11.0.0.1-4100/vms.sh vcli -c "show cluster"
```

---

## Summary

### Key Changes from Current Setup

| Component | Current | Optimized |
|-----------|---------|-----------|
| ZFS Topology | Mirror (RAID1) | Stripe (RAID0) |
| ZFS Sync | Default (enabled) | Disabled |
| ZFS Compression | Default | Disabled |
| ZFS Caching | All data | Metadata only |
| VM Disks | 1 (OS + data) | 2 (separate) |
| Data Disk FS | ext4 | XFS |
| Capacity | 422 GB | ~900 GB |

### Implementation Order

1. **Proxmox:** Create new ZFS stripe pool
2. **Proxmox:** Create and attach data disk to VM
3. **VM:** Format and mount data disk
4. **VM:** Run VAST installation on new disk
5. **Verify:** Check capacity and performance

---

*Document created: December 29, 2025*  
*For VAST Data 5.4 on Proxmox/KVM*
