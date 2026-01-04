# Installation Script Reference

**Document:** 07-Install-Script-Reference.md  
**Last Updated:** December 30, 2025  

---

## Overview

This document describes the unified installation script that automates VAST 5.4 deployment on Proxmox. The script handles:

1. Pre-bootstrap host preparation
2. VAST bootstrap execution
3. Post-container fixes
4. Cluster creation
5. Health verification

---

## Why We Need an Install Script

### Problems We Solved

Through multiple deployment attempts, we encountered issues that require specific workarounds:

| Problem | Impact | Script Fix |
|---------|--------|------------|
| pip assertion errors | Monitor install fails | Pin pip to 21.3.1 (Python 3.6) |
| FD exhaustion | System crashes | Increase limits proactively |
| Missing ipmitool | CNode activation fails | Create fake ipmitool |
| Missing rsync in containers | Monitor can't copy files | Copy after container start |
| Monitor race condition | FD leak, CPU spike | Pre-install monitor_v2 |
| CPU overcommit | PANIC during activation | Validate before install |

### Manual vs Automated

| Step | Manual Time | Automated |
|------|-------------|-----------|
| Pre-bootstrap prep | 15-20 min | 1 min |
| Bootstrap | 10 min | 10 min (same) |
| Post-container fixes | 5-10 min | 30 sec |
| Cluster creation | 5 min | 2 min |
| Monitoring setup | 10 min | Automatic |
| **Total** | **45-55 min** | **~15 min** |

---

## Script Architecture

### Modular Design

```
docs/scripts/
├── config.env.example   # Configuration template
├── config.env           # Your local config (copy from example)
├── install.sh           # Main entry point
├── lib/
│   ├── pre-bootstrap.sh # Host preparation
│   ├── bootstrap.sh     # VAST bootstrap wrapper
│   ├── post-start.sh    # Container fixes
│   ├── cluster.sh       # Cluster creation
│   └── verify.sh        # Health checks
└── logs/                # Installation logs
```

### Execution Flow

```
┌─────────────────────────────────────────────────────────────┐
│                       install.sh                             │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Phase 1: Pre-Bootstrap                                      │
│  ├── Validate requirements (RAM, CPU, disk)                 │
│  ├── Pin pip to 21.3.1 (Python 3.6 safe)                    │
│  ├── Configure FD limits                                     │
│  ├── Create fake ipmitool                                    │
│  ├── Apply kernel tuning                                     │
│  └── Clean previous attempts                                 │
│                                                              │
│  Phase 2: Bootstrap                                          │
│  ├── Extract VAST tarball                                    │
│  ├── Start registry container                                │
│  ├── Load VAST images                                        │
│  ├── Start VMS container                                     │
│  └── Wait for VMS ready                                      │
│                                                              │
│  Phase 3: Post-Container                                     │
│  ├── Pre-install monitor_v2                                  │
│  ├── Copy rsync to containers                                │
│  └── Verify container health                                 │
│                                                              │
│  Phase 4: Cluster Creation                                   │
│  ├── Create loopback cluster                                 │
│  ├── Wait for ACTIVATING → ONLINE                           │
│  └── Configure S3/licenses                                   │
│                                                              │
│  Phase 5: Verification                                       │
│  ├── Check cluster state                                     │
│  ├── Check node states                                       │
│  ├── Verify VIP connectivity                                 │
│  └── Create success snapshot (optional)                      │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## Configuration File

### config.env.example

Copy to `config.env` and customize:

```bash
#===============================================================================
# VAST 5.4 Installation Configuration
#===============================================================================

# Cluster Settings
CLUSTER_NAME="lb-vast54"
VAST_BUILD="release-5-4-0-2043819"
VAST_ADMIN_USER="admin"
VAST_ADMIN_PASS="123456"

# Network Settings
MANAGEMENT_IP=""                 # Auto-detect if empty
MANAGEMENT_IFACE="eth0"

# Storage Settings
VAST_MOUNT="/vast"               # Where VAST data lives
DATA_DISK="/dev/nvme0n1p1"       # Data disk partition (optional)

# Resource Validation
MIN_RAM_GB=110                   # Minimum RAM required
MIN_DISK_GB=100                  # Minimum disk space
MIN_CPU=12                       # Minimum CPU cores
MAX_VCPU_RATIO=1                 # vCPUs per physical core (1 = no overcommit)

# Timeouts (seconds)
BOOTSTRAP_TIMEOUT=1800           # 30 minutes
CLUSTER_TIMEOUT=1200             # 20 minutes
ACTIVATION_TIMEOUT=900           # 15 minutes

# Logging
LOG_DIR="/home/centos/docs/install_logs"
VERBOSE=1                        # 0=quiet, 1=normal, 2=debug

# Features
APPLY_WORKAROUNDS=1              # Apply all known workarounds
CREATE_SNAPSHOT=0                # Create Proxmox snapshot on success
MONITOR_DURING_INSTALL=1         # Run monitoring during install
```

### Environment Variable Override

```bash
# Override any config via environment
CLUSTER_NAME="my-cluster" VERBOSE=2 ./install.sh
```

---

## Script Usage

### Basic Usage

```bash
# Navigate to scripts directory
cd /home/centos/docs/scripts

# Make executable
chmod +x install.sh

# Run with defaults
sudo ./install.sh
```

### With Custom Config

```bash
# Copy template and edit
cp config.env.example config.env
vim config.env

# Run with config
sudo ./install.sh
```

### Phases Only

```bash
# Run specific phases
sudo ./install.sh --phase pre-bootstrap
sudo ./install.sh --phase bootstrap
sudo ./install.sh --phase post-start
sudo ./install.sh --phase cluster
sudo ./install.sh --phase verify
```

### Dry Run

```bash
# Show what would be done without executing
sudo ./install.sh --dry-run
```

---

## Phase Details

### Phase 1: Pre-Bootstrap

**Purpose:** Prepare the host system for VAST installation.

**Actions:**
1. Validate system requirements (RAM, CPU, disk)
2. Pin pip to 21.3.1 (Python 3.6 compatible)
3. Configure file descriptor limits
4. Create fake ipmitool script
5. Apply kernel performance tuning
6. Disable Transparent Huge Pages
7. Clean orphaned temp directories
8. Remove corrupted pip packages

**Success Criteria:**
- pip version = 21.3.1 (not higher)
- ulimit -n ≥ 1048576
- ipmitool returns fake data
- THP disabled
- No orphaned /tmp directories

### Phase 2: Bootstrap

**Purpose:** Run VAST bootstrap to extract images and start VMS.

**Actions:**
1. Verify VAST tarball exists
2. Extract tarball if needed
3. Disable IPv6 on management interface
4. Run vast_bootstrap.sh
5. Wait for VMS container to be healthy

**Success Criteria:**
- VMS container running
- Registry container running
- VMS API responding on port 443

### Phase 3: Post-Container

**Purpose:** Apply fixes after containers start but before cluster creation.

**Actions:**
1. Pre-install monitor_v2 package on host
2. Copy rsync binary to all platform containers
3. Verify container health and connectivity

**Success Criteria:**
- monitor_v2 package installed
- rsync present in all containers
- All containers in healthy state

### Phase 4: Cluster Creation

**Purpose:** Create and activate the loopback cluster.

**Actions:**
1. Generate loopback configuration YAML
2. Call cluster create via vman CLI
3. Monitor state transitions: INIT → ACTIVATING → ONLINE
4. Configure S3 certificates
5. Create trial license

**Success Criteria:**
- Cluster state: ONLINE
- All CNodes: ACTIVE
- All DNodes: ACTIVE

### Phase 5: Verification

**Purpose:** Verify successful deployment.

**Actions:**
1. Query cluster API for health
2. Check all node states
3. Verify usable capacity
4. Test VIP connectivity
5. Create NFS test export
6. Generate summary report

**Success Criteria:**
- API returns valid cluster data
- All nodes report ACTIVE
- Capacity > 0

---

## Monitoring During Installation

The script optionally runs monitoring in the background:

### Captured Metrics

| Metric | Interval | File |
|--------|----------|------|
| vmstat | 1 sec | vmstat.log |
| mpstat | 1 sec | mpstat.log |
| iostat | 1 sec | iostat.log |
| Docker stats | 7 sec | docker_stats.log |
| FD usage | 5 sec | fd_monitor.log |
| Load average | 1 sec | loadavg.log |
| dmesg | live | dmesg_live.log |

### Log Location

```
/home/centos/docs/install_logs/
├── install_YYYYMMDD_HHMMSS.log    # Main install log
├── vmstat.log
├── mpstat.log
├── iostat.log
├── docker_stats.log
├── fd_monitor.log
├── loadavg.log
└── dmesg_live.log
```

---

## Error Handling

### Automatic Retry

The script retries certain operations:

| Operation | Retries | Delay |
|-----------|---------|-------|
| Docker commands | 3 | 5 sec |
| API calls | 5 | 10 sec |
| Container health | 30 | 10 sec |
| Cluster state | 60 | 15 sec |

### Rollback Points

The script creates checkpoints at each phase:

```bash
# If phase 3 fails, restart from phase 3
sudo ./install.sh --resume
```

### Common Errors and Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| "Insufficient RAM" | < 110 GB | Add more RAM to VM |
| "Docker not running" | Docker daemon down | `sudo systemctl start docker` |
| "Bootstrap timeout" | Network or disk issues | Check logs, retry |
| "Cluster stuck in ACTIVATING" | Resource constraints | Check FD usage, add resources |
| "PANIC detected" | CPU overcommit or OOM | Reduce vCPUs, add RAM |

---

## Post-Installation

### What the Script Creates

| Item | Location |
|------|----------|
| VAST data | `/vast/data/`, `/vast/drives/` |
| Container configs | `/vast/deploy/` |
| SSH key | `/vast/deploy/ssh_key.pem` |
| Logs | `/home/centos/docs/install_logs/` |
| Start script | `/home/centos/start_vms.sh` |

### After Reboot

Containers don't auto-start. Use:

```bash
/home/centos/start_vms.sh
```

Or manually:

```bash
cd /vast/bundles/upgrades/*/
./vman.sh $(basename $(pwd)) /vast/deploy/ssh_key.pem start
```

### Accessing VAST

| Service | URL/Command |
|---------|-------------|
| Web UI | `https://<vm-ip>` |
| vCLI | `/vast/data/11.0.0.1-4100/vms.sh vcli` |
| API | `curl -sk -u admin:123456 https://localhost/api/` |

---

## Troubleshooting

### View Install Logs

```bash
# Latest log
ls -lt /home/centos/docs/install_logs/*.log | head -1

# Tail live
tail -f /home/centos/docs/install_logs/install_*.log
```

### Check Container Status

```bash
docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"
```

### Check FD Usage

```bash
cat /proc/sys/fs/file-nr
# Format: allocated  free  max
```

### Check for PANICs

```bash
docker logs vast_platform_11.0.0.1-4100 2>&1 | grep -i panic
```

### Manual Recovery

If the script fails mid-installation:

```bash
# Clean up
docker stop $(docker ps -aq) 2>/dev/null
docker rm $(docker ps -aq) 2>/dev/null

# Clean VAST directories (preserves drives)
sudo rm -rf /vast/data/* /vast/vman/*

# Restart from beginning
sudo ./install.sh
```

---

## Script Verification Checklist

Before using the script:

- [ ] `config.env` copied from `config.env.example` and configured
- [ ] VAST tarball present in `/vast/bundles/`
- [ ] Pre-install tweaks from [06-Pre-Install-Tweaks.md](06-Pre-Install-Tweaks.md) applied
- [ ] Logged out and back in (for ulimit changes)
- [ ] Sufficient disk space (>200 GB free on OS disk)
- [ ] Docker running and accessible

---

## Success Criteria

Installation is complete when:

- [ ] Cluster state is `ONLINE`
- [ ] All CNodes are `ACTIVE`
- [ ] All DNodes are `ACTIVE`
- [ ] Web UI accessible at `https://<vm-ip>`
- [ ] No PANICs in container logs
- [ ] FD usage stable (not climbing)

---

*Previous: [06-Pre-Install-Tweaks.md](06-Pre-Install-Tweaks.md) | Next: [README.md](README.md) (Index)*
