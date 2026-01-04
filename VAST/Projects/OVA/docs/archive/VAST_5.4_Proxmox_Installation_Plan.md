# VAST 5.4 Loopback v2 - Installation Plan

**Version:** 2.0  
**Date:** December 30, 2025  
**Status:** Planned - Pending Cluster Rebuild

---

## Overview

This document outlines the installation plan for VAST 5.4 loopback mode, incorporating all lessons learned and bug workarounds from the initial deployment.

**Changes from v1:**
- Pre-install rsync and create fake ipmitool BEFORE VAST installation
- Increased resource allocation
- Added post-container-start fix script
- Added comprehensive health checks

---

## Prerequisites

### Hardware Requirements (MINIMUM)

| Resource | v1 (Failed) | v2 (Planned) | Notes |
|----------|-------------|--------------|-------|
| vCPUs | 12 | **16-24** | Loopback idle load is 20+ |
| RAM | 117GB | 128GB | Keep as-is |
| Disk | 1TB | 1.5TB | More room for drives |
| Swap | 0 | **4GB** | Safety buffer |

### Software Prerequisites

- Proxmox VE 8.x
- Rocky Linux 8 guest VM
- SSH access as `centos` user with sudo

---

## Phase 1: VM Creation

### Proxmox Settings

```bash
# Create VM with these settings
CPU: 16-24 cores, host passthrough
RAM: 128GB
Disk: 1.5TB virtio-scsi
Network: vmbr0 (bridge to physical)
```

### Post-Install VM Configuration

```bash
# 1. Configure swap
sudo fallocate -l 4G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab

# 2. Set kernel parameters for VAST
cat << 'EOF' | sudo tee /etc/sysctl.d/99-vast.conf
vm.swappiness = 10
vm.dirty_ratio = 10
vm.dirty_background_ratio = 5
net.core.somaxconn = 65535
net.core.netdev_max_backlog = 65535
EOF
sudo sysctl -p /etc/sysctl.d/99-vast.conf
```

---

## Phase 2: Pre-Installation Fixes (NEW)

**⚠️ CRITICAL: Do these BEFORE running VAST installation**

### 2.1 Install Required Packages

```bash
# Install packages that VAST containers need
sudo dnf install -y rsync ipmitool python3-pip
```

### 2.2 Create Fake ipmitool

```bash
# VAST runs hardware validation that fails on VMs
# This creates a wrapper that returns fake hardware info

sudo mv /usr/bin/ipmitool /usr/bin/ipmitool.real 2>/dev/null || true

sudo cat > /usr/bin/ipmitool << 'EOF'
#!/bin/bash
# Fake ipmitool for VAST loopback mode
# VAST runs "ipmitool fru print 0" which fails on VMs without IPMI

if [[ "$*" == *"fru print"* ]]; then
    echo "Board Mfg Date        : Mon Jan 01 00:00:00 2024"
    echo "Board Mfg             : VAST Data Loopback"
    echo "Board Product         : Virtual Node"
    echo "Board Serial          : LOOPBACK-001"
    echo "Board Part Number     : VDL-VM-001"
    exit 0
fi

# Fall back to real ipmitool for other commands (if it exists)
if [[ -x /usr/bin/ipmitool.real ]]; then
    /usr/bin/ipmitool.real "$@" 2>/dev/null
fi
exit 0
EOF

sudo chmod +x /usr/bin/ipmitool

# Verify
ipmitool fru print 0
# Should output: Board Mfg : VAST Data Loopback
```

### 2.3 Clean Python Environment

```bash
# Remove any corrupted pip packages from previous attempts
sudo rm -rf /usr/local/lib/python3.6/site-packages/-* 2>/dev/null
sudo rm -rf /usr/local/lib/python3.6/site-packages/~* 2>/dev/null
```

---

## Phase 3: VAST Installation

### 3.1 Prepare Host

```bash
# From install-shell
cd /home/centos
./prepare_vm_for_vast.sh
```

### 3.2 Upload and Extract VAST Package

```bash
# Assumes vast-5.4.0-2043819.tar.zst is uploaded
cd /vast
tar -I zstd -xvf /tmp/vast-5.4.0-2043819.tar.zst
```

### 3.3 Run Main Installation

```bash
# From vast-install-shell
./install.sh
# Follow prompts for loopback configuration
```

---

## Phase 4: Post-Installation Fixes (NEW)

**⚠️ CRITICAL: Do these immediately after containers start**

### 4.1 Copy rsync to Containers

```bash
# The VAST containers are missing rsync
# This must be done EVERY time containers restart

cat > /home/centos/fix_vast_containers.sh << 'EOF'
#!/bin/bash
# Fix VAST container bugs

echo "=== Copying rsync to VAST containers ==="
for c in vast_platform_11.0.0.1-4100 vast_platform_11.0.0.1-4200 \
         vast_platform_11.0.0.1-4300 vast_platform_11.0.0.1-4400; do
    if docker ps --format '{{.Names}}' | grep -q "$c"; then
        echo "Fixing $c..."
        sudo docker cp /usr/bin/rsync $c:/usr/bin/rsync
    else
        echo "WARNING: $c is not running"
    fi
done

echo ""
echo "=== Done ==="
echo "Check cluster health with:"
echo "  curl -sk -u admin:123456 'https://192.168.30.109/api/cnodes/' | python3 -c \"import sys,json; [print(f'{c[\\\"name\\\"]}: {c[\\\"state\\\"]}') for c in json.load(sys.stdin)]\""
EOF

chmod +x /home/centos/fix_vast_containers.sh
```

### 4.2 Run the Fix Script

```bash
/home/centos/fix_vast_containers.sh
```

### 4.3 Verify Cluster Health

```bash
# Check all nodes are ACTIVE
curl -sk -u admin:123456 'https://192.168.30.109/api/cnodes/' | \
  python3 -c "import sys,json; [print(f'{c[\"name\"]}: {c[\"state\"]}') for c in json.load(sys.stdin)]"

curl -sk -u admin:123456 'https://192.168.30.109/api/dnodes/' | \
  python3 -c "import sys,json; [print(f'{c[\"name\"]}: {c[\"state\"]}') for c in json.load(sys.stdin)]"

# Expected output:
# cnode-1: ACTIVE
# cnode-2: ACTIVE  
# dnode-1: ACTIVE
# dnode-2: ACTIVE
```

---

## Phase 5: Validation

### 5.1 Create Test View

```bash
curl -sk -u admin:123456 -X POST 'https://192.168.30.109/api/views/' \
  -H 'Content-Type: application/json' \
  -d '{"name": "test-view", "path": "/test", "policy_id": 1}'
```

### 5.2 Create NFS Export

```bash
curl -sk -u admin:123456 -X POST 'https://192.168.30.109/api/nfsexports/' \
  -H 'Content-Type: application/json' \
  -d '{"name": "test-export", "path": "/test", "root_squash": false}'
```

### 5.3 Mount and Test

```bash
# Get CNode VIP
VIP=$(curl -sk -u admin:123456 'https://192.168.30.109/api/cnodes/1/' | \
  python3 -c "import sys,json; print(json.load(sys.stdin)['vips'][0])")

# Mount
sudo mkdir -p /mnt/vast
sudo mount -t nfs $VIP:/test /mnt/vast

# Write test file
echo "Hello VAST" | sudo tee /mnt/vast/test.txt

# Verify
cat /mnt/vast/test.txt
```

---

## Phase 6: Operational Procedures

### Starting the Cluster

```bash
# 1. Start containers
sudo docker start registry
sudo docker start vast_platform_11.0.0.1-{4100,4200,4300,4400}
sudo /vast/deploy/vman.sh release-5-4-0-2043819 UNKNOWN start

# 2. Fix containers (REQUIRED after every restart)
/home/centos/fix_vast_containers.sh

# 3. Wait for cluster to stabilize (2-3 minutes)
sleep 180

# 4. Verify health
curl -sk -u admin:123456 'https://192.168.30.109/api/cnodes/' | python3 -c "import sys,json; print('\\n'.join([f'{c[\"name\"]}: {c[\"state\"]}' for c in json.load(sys.stdin)]))"
```

### Stopping the Cluster

```bash
# 1. Unmount any NFS mounts
sudo umount /mnt/vast 2>/dev/null || true

# 2. Stop platform containers (allow graceful shutdown)
sudo docker stop vast_platform_11.0.0.1-{4100,4200,4300,4400}

# 3. Stop VMS (this removes the container!)
sudo docker stop vast_vms

# 4. Stop registry last
sudo docker stop registry
```

### Monitoring

```bash
# Watch load average (normal is 20+ for loopback)
watch -n5 'uptime; echo "---"; docker ps --format "table {{.Names}}\t{{.Status}}"'

# Check for monitor retry loops (bad if count is high)
docker logs vast_platform_11.0.0.1-4100 2>&1 | tail -100 | grep -c "ExecError"

# Check VMS workers
docker logs vast_vms 2>&1 | tail -50
```

---

## Troubleshooting Quick Reference

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| `pip3 install` failures in logs | Missing rsync | Run fix_vast_containers.sh |
| `ipmitool: No such file` | Missing fake ipmitool | Create wrapper script |
| VMS not responding | vast_vms container stopped | `vman.sh ... start` |
| Load average > 100 | Cascade failure | Stop all containers, wait, restart |
| Node stuck in FAILED | Multiple possible | Check logs, may need full restart |

---

## Success Criteria

The installation is complete when:

- [ ] All 4 platform containers running
- [ ] All CNodes show ACTIVE state
- [ ] All DNodes show ACTIVE state
- [ ] VMS UI accessible at https://192.168.30.109
- [ ] Test NFS mount works
- [ ] Data persists after graceful restart

---

## Related Documents

- [VAST_Loopback_Bugs_and_Workarounds.md](VAST_Loopback_Bugs_and_Workarounds.md) - Detailed bug descriptions
- [VAST_Lessons_Learned.md](VAST_Lessons_Learned.md) - Key lessons from v1
- [VAST_5.4_Proxmox_Complete_Guide.md](VAST_5.4_Proxmox_Complete_Guide.md) - Original installation guide

---

*Plan v2 - Incorporating all workarounds learned from failed v1 deployment.*
