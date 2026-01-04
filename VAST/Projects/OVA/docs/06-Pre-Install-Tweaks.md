# Pre-Installation Tweaks and Workarounds

**Document:** 06-Pre-Install-Tweaks.md  
**Last Updated:** December 30, 2025  

---

## Overview

Through multiple deployment attempts, we discovered several bugs and issues in VAST 5.4 loopback mode that require workarounds. This document covers **all pre-installation fixes** that must be applied before running the VAST bootstrap.

> **🚨 CRITICAL:** Apply these fixes in order before running `vast_bootstrap.sh`.

### Step Labels

| Label | Meaning |
|-------|---------|
| **🚨 REQUIRED** | Must do or install will fail |
| **⚠️ WORKAROUND** | Fixes a known bug |
| **⚙️ OPTIONAL** | Performance tuning, not required |
| **🚧 DANGEROUS** | May cause data loss or instability |

---

## Summary of Issues and Fixes

| Issue | Root Cause | Fix | Label |
|-------|------------|-----|-------|
| File descriptor exhaustion | Monitor retry loop creates orphaned directories | Increase FD limits | **🚨 REQUIRED** |
| pip installation failures | Python 3.6 + old pip has bugs | Pin pip to 21.3.1 | **⚠️ WORKAROUND** |
| ipmitool errors | VAST runs hardware checks on VMs | Create fake ipmitool | **⚠️ WORKAROUND** |
| Monitor package race | 4 containers fight to install monitor_v2 | Pre-install before bootstrap | **⚠️ WORKAROUND** |
| Container missing rsync | Container image doesn't include rsync | Copy from host after start | **⚠️ WORKAROUND** |

---

## Fix 1: Pin pip Version [⚠️ WORKAROUND]

### Problem

Rocky Linux 8 uses **Python 3.6**, but pip 22.0+ **dropped Python 3.6 support**. 

- Do NOT "upgrade pip to latest" - this installs pip 24.x which is incompatible
- pip 21.3.1 is the **last version supporting Python 3.6**
- VAST 5.4 internally uses Python 3.6 paths

### Evidence

From `/vast/data/11.0.0.1-4100/monitor.log`:
```
ERROR: Exception: AssertionError: assert os.path.exists(pyc_path)
ERROR: Cannot uninstall monitor-v2 0.0.3, RECORD file not found.
```

### Solution (Python 3.6 Safe)

```bash
# Verify Python version
python3 --version  # Should show 3.6.x

# Pin pip to last Python 3.6 compatible version
sudo python3 -m pip install "pip==21.3.1"
sudo python3 -m pip install "setuptools<=59.6.0" "wheel<=0.37.1"

# Verify
pip3 --version
# Should show pip 21.3.1
```

> **⚠️ DO NOT run `pip install --upgrade pip`** - this breaks Python 3.6 environments.

---

## Fix 2: Increase File Descriptor Limits [🚨 REQUIRED]

### Problem

VAST loopback runs 4 containers that all share the host's file descriptor limit. When the monitor process fails and retries, it leaks FDs until the system hits `file-max`.

### Evidence

```bash
$ dmesg | grep file-max
VFS: file-max limit 2097152 reached
```

### Solution

#### Process Limits

```bash
cat << 'EOF' | sudo tee /etc/security/limits.d/99-vast.conf
# VAST Data file descriptor limits
* soft nofile 1048576
* hard nofile 1048576
root soft nofile 1048576
root hard nofile 1048576
* soft nproc 65535
* hard nproc 65535
EOF
```

#### Kernel Limits

```bash
cat << 'EOF' | sudo tee /etc/sysctl.d/99-vast-fd.conf
# Increase maximum file descriptors
fs.file-max = 8388608
fs.nr_open = 2097152

# Increase inotify limits for Docker
fs.inotify.max_user_watches = 524288
fs.inotify.max_user_instances = 512
EOF

# Apply immediately
sudo sysctl -p /etc/sysctl.d/99-vast-fd.conf
```

#### Verify

```bash
# Log out and back in for process limits
logout

# Then verify
ulimit -n
# Should show 1048576

cat /proc/sys/fs/file-max
# Should show 8388608
```

---

## Fix 3: Create Fake ipmitool [⚠️ WORKAROUND]

### Problem

VAST runs hardware validation commands like `ipmitool fru print 0` which fail on VMs without IPMI hardware.

### Evidence

```
Command failed with 1: ssh ... sudo ipmitool fru print 0 | grep "Board Mfg"
Error: Could not open device at /dev/ipmi0 or /dev/ipmi/0
```

### Solution

```bash
# Backup real ipmitool if it exists
sudo mv /usr/bin/ipmitool /usr/bin/ipmitool.real 2>/dev/null || true

# Create fake ipmitool
cat << 'IPMITOOL' | sudo tee /usr/bin/ipmitool
#!/bin/bash
# Fake ipmitool for VAST loopback mode on VMs

if [[ "$*" == *"fru print"* ]]; then
    echo "Board Mfg Date        : Mon Jan 01 00:00:00 2024"
    echo "Board Mfg             : VAST Data Loopback"
    echo "Board Product         : Virtual Platform"
    echo "Board Serial          : LOOPBACK-$(hostname | md5sum | cut -c1-8)"
    exit 0
fi

if [[ "$*" == *"mc info"* ]]; then
    echo "Device ID             : 32"
    echo "Firmware Revision     : 1.00"
    echo "IPMI Version          : 2.0"
    exit 0
fi

if [[ "$*" == *"sensor"* ]]; then
    echo "CPU Temp         | 45.000     | degrees C  | ok"
    exit 0
fi

# Fall back to real ipmitool for other commands
[ -x /usr/bin/ipmitool.real ] && exec /usr/bin/ipmitool.real "$@"
exit 0
IPMITOOL

sudo chmod +x /usr/bin/ipmitool

# Verify
ipmitool fru print 0
# Should show "Board Mfg : VAST Data Loopback"
```

---

## Fix 4: Install Required Packages [🚨 REQUIRED]

### Problem

The host needs certain packages that VAST containers expect to be available.

### Solution

```bash
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
```

---

## Fix 5: Clean Orphaned Temporary Directories [⚙️ OPTIONAL]

### Problem

Failed monitor installations leave orphaned directories in `/tmp`:
- 8-character random directories (e.g., `/tmp/hevnojky`)
- pip-uninstall directories
- pip cache directories

These consume disk space and may cause issues on reinstall.

### Solution

```bash
# Clean up orphaned directories
sudo rm -rf /tmp/???????? 2>/dev/null
sudo rm -rf /tmp/pip-uninstall-* 2>/dev/null
sudo rm -rf /tmp/pip-ephem-wheel-cache-* 2>/dev/null

# Verify
ls /tmp/ | wc -l
# Should be minimal
```

---

## Fix 6: Remove Corrupted pip Packages [⚙️ OPTIONAL]

### Problem

Previous failed installations may leave corrupted package metadata.

### Evidence

```
WARNING: Ignoring invalid distribution -nitor-v2 (/usr/local/lib/python3.6/site-packages)
```

### Solution

```bash
# Remove corrupted package entries
sudo rm -rf /usr/local/lib/python3.6/site-packages/-* 2>/dev/null
sudo rm -rf /usr/local/lib/python3.6/site-packages/~* 2>/dev/null

# Remove old monitor packages
sudo rm -rf /usr/local/lib/python3.6/site-packages/monitor_v2* 2>/dev/null
sudo rm -rf /usr/local/lib/python3.6/site-packages/monitor_bundle* 2>/dev/null
sudo rm -rf /usr/local/lib/python3.6/site-packages/monitor-v2* 2>/dev/null
```

---

## Fix 7: Kernel Performance Parameters [⚙️ OPTIONAL]

### Problem

Default kernel settings aren't optimal for VAST's high-throughput, low-latency requirements.

### Solution

```bash
cat << 'EOF' | sudo tee /etc/sysctl.d/99-vast-perf.conf
# Virtual memory
vm.swappiness = 1
vm.dirty_ratio = 10
vm.dirty_background_ratio = 5
vm.dirty_expire_centisecs = 500
vm.dirty_writeback_centisecs = 100

# Scheduler (reduce migration overhead)
kernel.sched_migration_cost_ns = 5000000
kernel.sched_autogroup_enabled = 0

# Network tuning
net.core.somaxconn = 65535
net.core.netdev_max_backlog = 65535
net.ipv4.tcp_max_syn_backlog = 65535
net.ipv4.tcp_fin_timeout = 30
net.ipv4.tcp_keepalive_time = 300
EOF

sudo sysctl -p /etc/sysctl.d/99-vast-perf.conf
```

---

## Fix 8: Disable Transparent Huge Pages [⚙️ OPTIONAL]

### Problem

THP defragmentation *may* cause latency spikes during memory allocation. This is a common recommendation for database and latency-sensitive workloads, though we did not definitively prove it caused issues in our deployment.

### Solution (Conservative)

```bash
# Disable immediately
echo never | sudo tee /sys/kernel/mm/transparent_hugepage/enabled
echo never | sudo tee /sys/kernel/mm/transparent_hugepage/defrag

# Create systemd service for persistence
cat << 'EOF' | sudo tee /etc/systemd/system/disable-thp.service
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

sudo systemctl daemon-reload
sudo systemctl enable disable-thp

# Verify
cat /sys/kernel/mm/transparent_hugepage/enabled
# Should show: always madvise [never]
```

---

## Fix 9: Configure I/O Scheduler [⚙️ OPTIONAL]

### Solution

```bash
# Set for VirtIO disks
echo mq-deadline | sudo tee /sys/block/sda/queue/scheduler

# For NVMe (if passthrough)
echo none | sudo tee /sys/block/nvme0n1/queue/scheduler 2>/dev/null

# Persist via udev
cat << 'EOF' | sudo tee /etc/udev/rules.d/60-io-scheduler.rules
ACTION=="add|change", KERNEL=="sd[a-z]", ATTR{queue/scheduler}="mq-deadline"
ACTION=="add|change", KERNEL=="nvme[0-9]*", ATTR{queue/scheduler}="none"
EOF

sudo udevadm control --reload-rules
```

---

## Complete Pre-Bootstrap Script

All fixes combined into a single script:

```bash
#!/bin/bash
#===============================================================================
# VAST 5.4 Pre-Bootstrap Host Preparation
# Run this BEFORE vast_bootstrap.sh
#===============================================================================

set -euo pipefail

echo "=== VAST 5.4 Pre-Bootstrap Preparation ==="
echo ""

# Check root
if [ "$EUID" -ne 0 ]; then
    echo "ERROR: Run as root (sudo ./pre-bootstrap.sh)"
    exit 1
fi

# 1. Pin pip to safe version for Python 3.6
echo "[1/9] Installing pip==21.3.1 (Python 3.6 safe)..."
python3 -m pip install pip==21.3.1 setuptools==59.6.0 wheel==0.37.1

# 2. Install packages
echo "[2/9] Installing packages..."
dnf install -y python3-devel python3-wheel python3-setuptools gcc rsync pv jq

# 3. File descriptor limits (process)
echo "[3/9] Configuring FD limits (process)..."
cat << 'EOF' > /etc/security/limits.d/99-vast.conf
* soft nofile 1048576
* hard nofile 1048576
root soft nofile 1048576
root hard nofile 1048576
* soft nproc 65535
* hard nproc 65535
EOF

# 4. File descriptor limits (kernel)
echo "[4/9] Configuring FD limits (kernel)..."
cat << 'EOF' > /etc/sysctl.d/99-vast-fd.conf
fs.file-max = 8388608
fs.nr_open = 2097152
fs.inotify.max_user_watches = 524288
fs.inotify.max_user_instances = 512
EOF
sysctl -p /etc/sysctl.d/99-vast-fd.conf

# 5. Performance tuning
echo "[5/9] Applying kernel performance settings..."
cat << 'EOF' > /etc/sysctl.d/99-vast-perf.conf
vm.swappiness = 1
vm.dirty_ratio = 10
vm.dirty_background_ratio = 5
kernel.sched_migration_cost_ns = 5000000
kernel.sched_autogroup_enabled = 0
net.core.somaxconn = 65535
net.core.netdev_max_backlog = 65535
EOF
sysctl -p /etc/sysctl.d/99-vast-perf.conf

# 6. Disable THP
echo "[6/9] Disabling Transparent Huge Pages..."
echo never > /sys/kernel/mm/transparent_hugepage/enabled
echo never > /sys/kernel/mm/transparent_hugepage/defrag

# 7. Create fake ipmitool
echo "[7/9] Creating fake ipmitool..."
[ -f /usr/bin/ipmitool ] && mv /usr/bin/ipmitool /usr/bin/ipmitool.real 2>/dev/null || true
cat << 'IPMITOOL' > /usr/bin/ipmitool
#!/bin/bash
if [[ "$*" == *"fru print"* ]]; then
    echo "Board Mfg             : VAST Data Loopback"
    exit 0
fi
[ -x /usr/bin/ipmitool.real ] && exec /usr/bin/ipmitool.real "$@"
exit 0
IPMITOOL
chmod +x /usr/bin/ipmitool

# 8. Clean temp directories
echo "[8/9] Cleaning temp directories..."
rm -rf /tmp/???????? 2>/dev/null || true
rm -rf /tmp/pip-uninstall-* 2>/dev/null || true
rm -rf /tmp/pip-ephem-wheel-cache-* 2>/dev/null || true

# 9. Clean corrupted packages
echo "[9/9] Cleaning corrupted pip packages..."
rm -rf /usr/local/lib/python3.6/site-packages/-* 2>/dev/null || true
rm -rf /usr/local/lib/python3.6/site-packages/~* 2>/dev/null || true
rm -rf /usr/local/lib/python3.6/site-packages/monitor_v2* 2>/dev/null || true

echo ""
echo "=== Pre-Bootstrap Complete ==="
echo ""
echo "pip version: $(pip3 --version | awk '{print $2}')"
echo "FD limit: $(cat /proc/sys/fs/file-max)"
echo ""
echo "IMPORTANT: Log out and back in for ulimit changes to take effect!"
echo ""
echo "Next steps:"
echo "  1. Log out: exit"
echo "  2. Log back in: ssh centos@<vm-ip>"
echo "  3. Verify: ulimit -n (should show 1048576)"
echo "  4. Run: ./vast_bootstrap.sh"
echo ""
```

Save as `/home/centos/docs/scripts/pre-bootstrap.sh`

---

## Post-Container Fixes

After containers start but before cluster activation, apply these fixes:

### Copy rsync to Containers

VAST containers need rsync but don't have it:

```bash
#!/bin/bash
# post-container-fixes.sh
# Run after "VMS is up" but before cluster creation

echo "Copying rsync to VAST containers..."

for c in vast_platform_11.0.0.1-{4100,4200,4300,4400}; do
    if docker ps --format '{{.Names}}' | grep -q "$c"; then
        docker cp /usr/bin/rsync $c:/usr/bin/rsync
        echo "  ✓ $c"
    fi
done

echo "Done"
```

### Pre-install monitor_v2

Prevent the race condition by pre-installing:

```bash
# Extract monitor_v2 from container image
docker create --name temp_extract vastdata.registry.local:5000/dev/orion:release-5-4-0-2043819
docker cp temp_extract:/vast/install/pysrc/monitor_v2 /tmp/monitor_v2
docker rm temp_extract

# Install on host
sudo pip3 install --force-reinstall --no-deps /tmp/monitor_v2
rm -rf /tmp/monitor_v2

# Verify
pip3 show monitor-v2
```

---

## Verification Checklist

Before running bootstrap, verify all fixes:

```bash
echo "=== Pre-Bootstrap Verification ==="

# pip version
echo -n "pip: "
pip3 --version | awk '{print $2}'

# FD limits
echo -n "FD limit (process): "
ulimit -n

echo -n "FD limit (kernel): "
cat /proc/sys/fs/file-max

# ipmitool
echo -n "ipmitool: "
ipmitool fru print 0 2>/dev/null | grep -q "VAST Data Loopback" && echo "OK (fake)" || echo "MISSING"

# THP
echo -n "THP: "
cat /sys/kernel/mm/transparent_hugepage/enabled | grep -q '\[never\]' && echo "disabled" || echo "ENABLED (bad)"

# Orphan directories
echo -n "Orphan dirs: "
ls -d /tmp/???????? 2>/dev/null | wc -l
```

### Expected Output

```
=== Pre-Bootstrap Verification ===
pip: 23.3.2
FD limit (process): 1048576
FD limit (kernel): 8388608
ipmitool: OK (fake)
THP: disabled
Orphan dirs: 0
```

---

## Next Steps

After applying all fixes:

1. **Log out and back in** (for ulimit changes)
2. **Run the installer:** [07-Install-Script-Reference.md](07-Install-Script-Reference.md)

---

*Previous: [05-Topology-Planning.md](05-Topology-Planning.md) | Next: [07-Install-Script-Reference.md](07-Install-Script-Reference.md)*
