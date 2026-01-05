# VAST 5.4 Loopback Pre-Deployment Checklist

**Version:** 2.0  
**Last Updated:** December 30, 2025  
**Target:** Fresh Rocky Linux 8 VM on Proxmox

---

## Overview

This checklist incorporates all lessons learned from the December 2025 deployment attempts. Follow this checklist **in order** before running `vast_bootstrap.sh`.

---

## Phase 1: Proxmox VM Configuration

### Hardware Settings

| Setting | Required Value | Reason |
|---------|---------------|--------|
| **vCPUs** | 12 (match physical cores 1:1) | Prevents CPU overcommit causing keepalive timeouts |
| **RAM** | 120+ GB | VAST needs ~110GB at steady state |
| **Disk** | 500+ GB (VirtIO SCSI) | Storage for loopback drives |
| **CPU Type** | `host` | Full CPU feature passthrough |
| **SCSI Controller** | VirtIO SCSI single + IO Thread | Better disk latency |
| **Memory Ballooning** | ❌ Disabled | Prevents memory reclaim under load |
| **Network** | VirtIO | Best performance |

### BIOS/UEFI Settings

- [ ] Nested virtualization enabled on Proxmox host
- [ ] VM uses OVMF (UEFI) if required by VAST

---

## Phase 2: Fresh VM Setup

### After First Boot

```bash
# Update system
sudo dnf update -y

# Install required packages
sudo dnf install -y \
    python3-devel \
    python3-wheel \
    python3-setuptools \
    gcc \
    rsync \
    pv \
    jq \
    tmux \
    htop

# Reboot if kernel was updated
sudo reboot
```

### Verify System State

```bash
# Check kernel version (should be 4.18.0-553+ for Rocky 8)
uname -r

# Check memory (should show ~120GB)
free -h

# Check CPU count (should be 12)
nproc

# Check disk space
df -h /
```

---

## Phase 3: Pre-Bootstrap Host Preparation

### Run the Preparation Script

```bash
# Copy script to VM (or create from docs)
cd /home/centos/docs/scripts
sudo ./pre_bootstrap_host_prep.sh
```

### Manual Verification

After running the script, verify:

```bash
# 1. pip version (should be 23.x or higher)
pip3 --version

# 2. File descriptor limits
ulimit -n  # Should show 1048576 after re-login
cat /proc/sys/fs/file-max  # Should show 8388608

# 3. ipmitool returns fake data
ipmitool fru print 0  # Should show "VAST Data Loopback"

# 4. No orphaned temp directories
ls /tmp/???????? 2>/dev/null | wc -l  # Should be 0

# 5. monitor_v2 is not installed (clean state)
pip3 show monitor-v2  # Should say "not found"
```

---

## Phase 4: VAST Bundle Extraction

### Upload and Extract

```bash
cd /vast/bundles

# Upload the .vast.tar.gz file to this directory
ls -la *release*.vast.tar.gz

# Extract (takes ~5 minutes)
BUNDLE=$(ls *release*.vast.tar.gz | head -1)
mkdir -p upgrades
pv $BUNDLE | tar xzf - -C upgrades/
```

### Verify Extraction

```bash
# Check extracted files
ls -la /vast/bundles/upgrades/*/

# Should see vman.sh, metadata.txt, etc.
```

---

## Phase 5: Bootstrap

### Start Bootstrap

```bash
cd /vast/bundles
./vast_bootstrap.sh --interface $(hostname -I | awk '{print $1}') --skip-prompt
```

### Monitor Bootstrap

In a separate terminal:

```bash
# Watch the bootstrap log
tail -f /vast/bundles/bootstrap.log

# Monitor system resources
htop

# Monitor file descriptors
watch -n 5 'cat /proc/sys/fs/file-nr'
```

### Expected Timeline

| Phase | Duration | Indicator |
|-------|----------|-----------|
| Tarball extraction | ~5 min | VMS tarball extracting |
| VMS startup | ~5 min | "starting VMS ---- 60% done" |
| VMS ready | ~2 min | "Done, VMS is up" |
| Host discovery | ~30 sec | "discovering hosts.." |

---

## Phase 6: Post-Bootstrap, Pre-Cluster

### Run Post-Container Script

After VMS is up but BEFORE creating the cluster:

```bash
cd /home/centos/docs/scripts
./post_container_start.sh
```

### Verify VMS Access

```bash
# Check VMS is responding
curl -sk https://$(hostname -I | awk '{print $1}')/api/version/ | jq .

# Check VMS container is running
docker ps | grep vast_vms
```

---

## Phase 7: Cluster Creation

### Via Web UI

1. Open `https://<VM_IP>` in browser
2. Login: admin / 123456
3. Navigate to Cluster → Create Cluster
4. Configure:
   - Cluster Name: `lb-vast54`
   - Topology: Loopback
   - CNodes: 2
   - DNodes: 2

### Via CLI (Alternative)

```bash
# Use vman CLI
cd /vast/bundles/upgrades/*/
./vman.sh release-5-4-0-2043819 UNKNOWN vcli

# In vman CLI:
cluster create --name lb-vast54 --loopback
```

### Monitor Cluster Creation

```bash
# Watch FD usage (critical during activation)
watch -n 2 'echo "FDs: $(cat /proc/sys/fs/file-nr)"; echo ""; docker stats --no-stream --format "{{.Name}}: {{.CPUPerc}} {{.MemUsage}}"'

# Watch container logs for errors
docker logs -f vast_platform_11.0.0.1-4100 2>&1 | grep -iE "error|exception|panic"
```

---

## Phase 8: Post-Cluster Verification

### Cluster Health Check

```bash
# API health check
curl -sk -u admin:123456 'https://localhost/api/clusters/' | jq '.[0].state'
# Should return "ONLINE"

# Node status
curl -sk -u admin:123456 'https://localhost/api/cnodes/' | jq '.[] | {name, state}'
curl -sk -u admin:123456 'https://localhost/api/dnodes/' | jq '.[] | {name, state}'
# All should be "ACTIVE"
```

### System Health Check

```bash
# Load average (should be 20-30 with 12 cores)
uptime

# Memory usage (should be ~95% used)
free -h

# File descriptors (should be stable, not climbing)
cat /proc/sys/fs/file-nr
```

---

## Troubleshooting Quick Reference

### If FDs are climbing rapidly

```bash
# Identify the consumer
lsof -n 2>/dev/null | awk '{print $1}' | sort | uniq -c | sort -nr | head -10

# If it's monitor-related, pre-install monitor_v2
./post_container_start.sh
```

### If cluster stuck in ACTIVATING

```bash
# Check for PANICs
docker logs vast_platform_11.0.0.1-4100 2>&1 | grep -i panic

# Check container health
docker stats --no-stream
```

### If OOM kills occur

```bash
# Check dmesg
dmesg | grep -i "out of memory\|oom"

# Increase VM memory or reduce container count
```

---

## Files Created by This Process

| File | Purpose |
|------|---------|
| `/home/centos/docs/scripts/pre_bootstrap_host_prep.sh` | Host preparation |
| `/home/centos/docs/scripts/post_container_start.sh` | Post-container fixes |
| `/etc/security/limits.d/99-vast.conf` | FD limits |
| `/etc/sysctl.d/99-vast.conf` | Kernel tuning |
| `/usr/bin/ipmitool` | Fake ipmitool for VMs |

---

## Success Criteria

- [ ] Cluster state is `ONLINE`
- [ ] All 2 CNodes are `ACTIVE`
- [ ] All 2 DNodes are `ACTIVE`
- [ ] File descriptors stable (not climbing)
- [ ] Load average 20-30 (with 12 cores)
- [ ] No PANICs in container logs
- [ ] Web UI accessible and responsive

---

*Document created from lessons learned during December 2025 deployment attempts.*
