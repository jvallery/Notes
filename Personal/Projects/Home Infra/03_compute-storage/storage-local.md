# Local Storage Architecture

← [Documentation Index](../index.md)

## Storage Design Philosophy

All hosts use local NVMe storage for maximum performance and simplicity. This eliminates shared storage dependencies while providing high-speed access for containers and data processing.

## Manager Node Storage (Mini PCs)

### home1 Configuration
- **Capacity**: 500 GB NVMe SSD
- **Model**: Samsung 990 EVO Plus (PCIe 3.0)
- **File System**: ext4 on LVM
- **Purpose**: OS + moderate container data

### home2 & home3 Configuration
- **Capacity**: 256 GB NVMe SSD per host
- **Model**: Kingston OM8PCP3 (PCIe 3.0)
- **File System**: ext4 on LVM
- **Purpose**: OS + lightweight container data

### Partition Layout (home1 - 500GB)
```
/dev/nvme0n1
├── /dev/nvme0n1p1  512 MB  /boot/efi (FAT32)
├── /dev/nvme0n1p2  1 GB    /boot (ext4)
└── /dev/nvme0n1p3  498 GB  LVM PV
    └── vg0
        ├── root    60 GB   / (ext4)
        ├── var     60 GB   /var (ext4)
        ├── data    370 GB  /data (ext4)
        └── swap    8 GB    swap
```

### Partition Layout (home2/home3 - 256GB)
```
/dev/nvme0n1
├── /dev/nvme0n1p1  512 MB  /boot/efi (FAT32)
├── /dev/nvme0n1p2  1 GB    /boot (ext4)
└── /dev/nvme0n1p3  254 GB  LVM PV
    └── vg0
        ├── root    60 GB   / (ext4)
        ├── var     40 GB   /var (ext4)
        ├── data    150 GB  /data (ext4)
        └── swap    4 GB    swap
```

### Usage Patterns
- **OS Base**: ~8 GB (minimal Ubuntu installation)
- **Docker System**: ~15 GB (images, containers, logs)
- **Service Data**: ~50 GB (lightweight persistent volumes)
- **Free Space**: ~180 GB for growth and snapshots

## GPU Worker Storage

### Hardware Configuration
- **OS Drive**: 1×1 TB Samsung 990 EVO Plus (PCIe 3.0)
- **Additional Storage**: 2×1 TB Samsung 990 EVO Plus (PCIe 3.0)
- **Total Raw**: 3 TB per worker, 9 TB cluster total
- **Configuration**: Individual drives (no RAID)

### RAID Configuration
The data drives use Linux software RAID (mdadm) for reliability:

```bash
# RAID1 array configuration
/dev/md0 (RAID1)
├── /dev/nvme1n1 (1 TB)
└── /dev/nvme2n1 (1 TB)
```

### Mount Structure
```
/                  # OS drive (nvme0n1)
├── /boot/efi      # 512 MB, FAT32
├── /boot          # 1 GB, ext4
├── /               # 60 GB, ext4 (root)
├── /var           # 60 GB, ext4 (Docker data)
├── /tmp           # 20 GB, ext4
└── /swap          # 32 GB, swap file

/data              # RAID1 array (md0)
└── /data          # 1 TB, ext4 (container volumes)
```

### Data Directory Structure
```
/data/
├── backup/        # Local backup snapshots
├── ai-models/     # Shared AI/ML model cache
├── datasets/      # Training and inference data
├── containers/    # Container persistent volumes
│   ├── stack1/
│   ├── stack2/
│   └── ...
└── scratch/       # Temporary high-speed workspace
```

## RAID Management

### Monitoring and Alerts
```bash
# Check RAID status
cat /proc/mdstat

# Detailed array information
mdadm --detail /dev/md0

# Monitor for degraded arrays
mdadm --monitor --scan --syslog
```

### RAID Failure Recovery
```bash
# Simulate failure (testing)
mdadm /dev/md0 --fail /dev/nvme2n1

# Remove failed drive
mdadm /dev/md0 --remove /dev/nvme2n1

# Add replacement drive
mdadm /dev/md0 --add /dev/nvme2n1p1

# Monitor rebuild progress
watch cat /proc/mdstat
```

### Performance Characteristics
- **Read Speed**: ~7,000 MB/s (single drive speed)
- **Write Speed**: ~3,500 MB/s (RAID1 penalty)
- **IOPS**: 1M+ random reads, 500K+ random writes
- **Latency**: <0.1ms average

## File System Optimization

### ext4 Configuration
```bash
# Mount options for performance
/dev/md0 /data ext4 defaults,noatime,nodiratime,data=writeback 0 2
```

### Key Optimizations
- **noatime**: Disable access time updates for performance
- **nodiratime**: Disable directory access time updates
- **data=writeback**: Async data writes for speed
- **Reserved blocks**: 1% reserved for root (default 5% reduced)

## Snapshot Strategy

### LVM Snapshots (Managers)
```bash
# Create snapshot before major changes
lvcreate -L 10G -s -n data-snapshot /dev/vg0/data

# Mount snapshot for backup
mount /dev/vg0/data-snapshot /mnt/snapshot

# Remove after backup
umount /mnt/snapshot
lvremove /dev/vg0/data-snapshot
```

### Filesystem Snapshots (Workers)
Using filesystem-level tools for RAID arrays:

```bash
# Create filesystem snapshot
fsfreeze -f /data
rsync -aH /data/ /backup/snapshots/$(date +%Y%m%d)/
fsfreeze -u /data
```

## Performance Monitoring

### Storage Metrics
Key metrics tracked via Prometheus node_exporter:

| Metric | Normal | Warning | Critical |
|--------|--------|---------|----------|
| Disk Usage | <70% | 80% | 90% |
| IOPS | Baseline | +200% | +500% |
| Latency | <1ms | 5ms | 10ms |
| Queue Depth | <5 | 15 | 30 |

### SMART Monitoring
```bash
# Check drive health
smartctl -a /dev/nvme0n1

# Key SMART attributes to monitor
- Temperature
- Power_On_Hours
- Wear_Leveling_Count
- Reallocated_Sector_Ct
```

## Capacity Planning

### Current Utilization (per worker)
- **OS Partition**: ~25% (250 GB used of 1 TB)
- **Data Partition**: ~40% (400 GB used of 1 TB)
- **Growth Rate**: ~5 GB/month per worker

### Expansion Triggers
- **Storage**: Add drives when reaching 80% capacity
- **Performance**: Scale out when IOPS consistently >500K
- **Reliability**: Replace drives after 3 years or SMART warnings

## Backup Integration

### Local Backup Strategy
Each worker maintains local snapshots:

```bash
# Daily snapshot rotation
#!/bin/bash
DATE=$(date +%Y%m%d)
rsync -aH --delete /data/ /backup/daily/$DATE/
find /backup/daily/ -type d -mtime +7 -exec rm -rf {} \;
```

### NAS Integration
Critical data replicated to NAS for redundancy:

```bash
# Sync important data to NAS
rsync -avz /data/ai-models/ obsidian:/volume1/ai-models/
rsync -avz /data/datasets/ obsidian:/volume1/datasets/
```

## Disaster Recovery

### Recovery Procedures

#### Manager Node Recovery
1. Boot from Ubuntu USB installer
2. Restore partition layout and LVM
3. Restore data from latest NAS backup
4. Rejoin Docker Swarm cluster

#### Worker Node Recovery
1. Rebuild RAID array with replacement drives
2. Restore filesystem structure
3. Restore container volumes from local snapshots
4. Rejoin Swarm as worker node

### Recovery Time Objectives
- **Manager Node**: 2 hours (limited by data restore)
- **Worker Node**: 4 hours (includes RAID rebuild)
- **Full Cluster**: 8 hours (worst-case scenario)

## Performance Tuning

### Kernel Parameters
```bash
# /etc/sysctl.d/99-storage.conf
# Increase read-ahead for sequential workloads
vm.swappiness=10
vm.vfs_cache_pressure=50
vm.dirty_background_ratio=5
vm.dirty_ratio=10
```

### I/O Scheduler
```bash
# Set optimal scheduler for NVMe
echo mq-deadline > /sys/block/nvme0n1/queue/scheduler
echo mq-deadline > /sys/block/nvme1n1/queue/scheduler
echo mq-deadline > /sys/block/nvme2n1/queue/scheduler
```

### Container Storage Driver
Docker configured with optimal storage driver:

```json
{
  "storage-driver": "overlay2",
  "storage-opts": [
    "overlay2.override_kernel_check=true"
  ]
}
```

---

**Next**: [NAS & NFS](nas-nfs.md) | **Related**: [Host Configuration](hosts.md)
