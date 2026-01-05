# VAST 5.4 Loopback - Monitor Package Installation & FD Exhaustion Analysis

**Date:** December 30, 2025  
**VAST Version:** 5.4.0 (release-5-4-0-2043819)  
**Environment:** Proxmox 8.3 / Rocky Linux 8 VM  
**Status:** ✅ Root Cause Identified

---

## Executive Summary

During VAST cluster operation, the system hit the kernel file descriptor limit (2,097,152 FDs), causing `btop` failures, shell pipe errors, and general system instability. This document provides a complete root cause analysis and remediation steps for future deployments.

**Key Finding:** The monitor_v2 package installation retry loop consumed excessive file descriptors due to pip installation failures on the host, creating ~205 orphaned directories and ~74 failed pip uninstall attempts.

---

## Root Cause Analysis

### The Monitor Package Installation Architecture

VAST platform containers communicate with the host via SSH to install a Python monitoring package:

```
┌─────────────────────────────────────────────────────────────────┐
│                         HOST (Rocky Linux VM)                    │
│                                                                  │
│  SSH Server ◄────────────────────────────────────────────────┐  │
│       │                                                       │  │
│       ▼                                                       │  │
│  pip3 install /tmp/xxxxxxxx  ──► FAILS ──► Retry Loop        │  │
│       │                                                       │  │
│       └── Creates orphaned dirs in /tmp                       │  │
│                                                                  │
├──────────────────────────────────────────────────────────────────┤
│                     VAST Platform Containers (x4)                │
│                                                                  │
│  monitor.py ─┬─► scp monitor_v2 to host:/tmp/xxxxxxxx           │
│              └─► ssh host "pip3 install /tmp/xxxxxxxx"          │
│                        │                                         │
│                        └── On failure: RETRY IMMEDIATELY         │
│                            (no backoff, no cleanup)              │
└──────────────────────────────────────────────────────────────────┘
```

### The Failure Chain

1. **Container starts monitor process**
2. Monitor SSHs to host and runs `pip3 install -U --no-deps /tmp/xxxxxxxx`
3. pip3 fails with one of:
   - `RECORD file not found` (corrupt previous install)
   - `AssertionError: os.path.exists(pyc_path)` (race condition)
   - `OSError: No such file or directory: .../__pycache__/`
4. **Monitor retries immediately with NO backoff**
5. Each retry:
   - Creates new random 8-char directory (`/tmp/xxxxxxxx`)
   - Opens SSH connections (2+ FDs)
   - Opens pipes for stdout/stderr (2+ FDs)
   - Creates pip temp directories
   - **Does NOT clean up on failure**

### Evidence from This Deployment

| Metric | Value | Impact |
|--------|-------|--------|
| Orphaned 8-char directories in /tmp | **205** | ~357 MB disk |
| Failed pip-uninstall directories | **74** | Partial cleanups |
| Kernel messages (file-max reached) | **20+** occurrences | System-wide FD exhaustion |
| Time to FD exhaustion | ~14 minutes after boot | During container activation |

### Monitor Log Evidence

From `/vast/data/11.0.0.1-4100/monitor.log`:
```
2025-12-30 02:15:42 ERROR Failed to get cmd command ssh centos@localhost ...
  'sudo pip3 install -U --no-deps --no-cache-dir /tmp/hevnojky'
  ERROR: Cannot uninstall monitor-v2 0.0.3, RECORD file not found.

2025-12-30 02:27:42 ERROR ... pip3 install ... /tmp/okshyyok
  ERROR: Exception: AssertionError: assert os.path.exists(pyc_path)

2025-12-30 02:39:41 ERROR ... pip3 install ... /tmp/tabvaxwo  
  ERROR: OSError: No such file or directory: '.../__pycache__/'
```

Each error is followed by `install_package(host_executor)` showing the recursive retry.

---

## Why This Happens in Loopback Mode

### Normal (Physical) VAST Deployment

- 4 separate physical servers
- Each has its own 2M FD limit
- Monitor runs locally on each server
- pip install happens on local filesystem

### Loopback Deployment

- **4 containers share ONE kernel's FD limit**
- All 4 containers try to install monitor_v2 on the SAME host
- Race conditions between containers
- FD exhaustion affects ALL containers simultaneously

---

## The pip Issues (Python 3.6 + pip 21.3.1)

### Issue 1: RECORD File Not Found

When pip partially installs a package and is interrupted, the RECORD file (package manifest) can be missing. Subsequent installs fail because pip can't uninstall the existing version.

### Issue 2: pyc Path Assertion

This is a **known pip bug** with Python 3.6:
```python
# pip/_internal/operations/install/wheel.py line 618
assert os.path.exists(pyc_path)  # Fails under race conditions
```

The assertion fails when:
- Multiple processes try to compile .pyc files simultaneously
- Filesystem has high latency (virtual disk)
- Previous partial install left stale .pyc references

### Issue 3: Missing __pycache__

When pip uninstalls and reinstalls rapidly, __pycache__ directories can be deleted mid-operation.

---

## Remediation Steps for Fresh Deployment

### Pre-Bootstrap Host Preparation

Run these commands on a fresh VM BEFORE running `vast_bootstrap.sh`:

```bash
#!/bin/bash
# /home/centos/pre_bootstrap_host_prep.sh

echo "=== VAST 5.4 Pre-Bootstrap Host Preparation ==="

# 1. Upgrade pip to avoid Python 3.6 bugs
echo "[1/5] Upgrading pip..."
sudo python3 -m pip install --upgrade pip

# 2. Install monitor_v2 dependencies (prevents build-time issues)
echo "[2/5] Installing build dependencies..."
sudo dnf install -y python3-devel python3-wheel python3-setuptools

# 3. Increase file descriptor limits (safety margin)
echo "[3/5] Increasing file descriptor limits..."
cat << 'EOF' | sudo tee /etc/security/limits.d/99-vast.conf
* soft nofile 1048576
* hard nofile 1048576
root soft nofile 1048576
root hard nofile 1048576
EOF

# Increase kernel limits
echo 'fs.file-max = 8388608' | sudo tee -a /etc/sysctl.d/99-vast.conf
echo 'fs.nr_open = 2097152' | sudo tee -a /etc/sysctl.d/99-vast.conf
sudo sysctl -p /etc/sysctl.d/99-vast.conf

# 4. Pre-create monitor_v2 installation directory structure
echo "[4/5] Pre-creating monitor directories..."
sudo mkdir -p /usr/local/lib/python3.6/site-packages/monitor_v2
sudo mkdir -p /tmp/monitor_v2_commands_cache
sudo chmod 777 /tmp/monitor_v2_commands_cache

# 5. Clean any stale temp files
echo "[5/5] Cleaning temp files..."
sudo rm -rf /tmp/???????? /tmp/pip-uninstall-* /tmp/pip-ephem-wheel-cache-*

echo "=== Host preparation complete ==="
echo "You can now run: ./vast_bootstrap.sh"
```

### Post-Container-Start Script

After containers start, run this to ensure monitor_v2 installs cleanly:

```bash
#!/bin/bash
# /home/centos/post_container_start.sh

echo "=== Post-Container Start Fixes ==="

# Wait for containers to be running
sleep 10

# 1. Extract and pre-install monitor_v2 from container
echo "[1/3] Pre-installing monitor_v2..."
docker create --name temp_extract vastdata.registry.local:5000/dev/orion:release-5-4-0-2043819
docker cp temp_extract:/vast/install/pysrc/monitor_v2 /tmp/monitor_v2_preinstall
docker rm temp_extract

# Install with force-reinstall to avoid RECORD issues
sudo python3 -m pip install --force-reinstall --no-deps /tmp/monitor_v2_preinstall
rm -rf /tmp/monitor_v2_preinstall

# 2. Verify installation
echo "[2/3] Verifying installation..."
pip3 show monitor-v2 || echo "WARNING: monitor-v2 not installed!"

# 3. Monitor FD usage
echo "[3/3] Current FD usage:"
cat /proc/sys/fs/file-nr

echo "=== Post-start fixes complete ==="
```

---

## Monitoring for FD Leaks

### Real-Time FD Monitor

```bash
#!/bin/bash
# Monitor FD usage in real-time
watch -n 5 '
echo "=== File Descriptor Status ==="
echo "System: $(cat /proc/sys/fs/file-nr)"
echo ""
echo "=== Top FD Consumers ==="
for pid in $(ls /proc | grep -E "^[0-9]+$" | head -20); do
    count=$(ls /proc/$pid/fd 2>/dev/null | wc -l)
    if [ $count -gt 100 ]; then
        name=$(cat /proc/$pid/comm 2>/dev/null)
        echo "$name (PID $pid): $count FDs"
    fi
done | sort -t: -k2 -nr | head -10
'
```

### Alarm Script

```bash
#!/bin/bash
# Alert if FD usage exceeds threshold
THRESHOLD=1000000
CURRENT=$(cat /proc/sys/fs/file-nr | awk '{print $1}')
MAX=$(cat /proc/sys/fs/file-nr | awk '{print $3}')

if [ $CURRENT -gt $THRESHOLD ]; then
    echo "ALERT: FD usage $CURRENT exceeds threshold $THRESHOLD (max: $MAX)"
    echo "Top consumers:"
    lsof -n 2>/dev/null | awk '{print $1}' | sort | uniq -c | sort -nr | head -5
fi
```

---

## Lessons Learned

### 1. Pre-install Host Dependencies

The monitor_v2 package should be pre-installed on the host BEFORE containers start. This avoids:
- Race conditions between containers
- pip retry loops
- FD exhaustion

### 2. Upgrade pip on Rocky Linux 8

The default pip version (21.3.1) has bugs with Python 3.6. Upgrading pip before VAST bootstrap prevents assertion errors.

### 3. Increase FD Limits Proactively

Even though the default limit is 2M, loopback mode can exhaust this. Setting higher limits provides safety margin.

### 4. Monitor Retry Bug

The VAST monitor's retry logic has no backoff and doesn't clean up temp directories. This is a VAST bug that should be reported.

---

## Summary Table

| Issue | Root Cause | Prevention |
|-------|------------|------------|
| FD exhaustion | Monitor retry loop | Pre-install monitor_v2, upgrade pip |
| pip RECORD error | Corrupt previous install | Use `--force-reinstall` |
| pip assertion error | Python 3.6 + old pip | Upgrade pip to latest |
| Orphaned /tmp dirs | No cleanup on failure | Pre-bootstrap cleanup script |
| 4 containers race | Shared host resources | Pre-install before container start |

---

## Files Referenced

- Monitor code: `/vast/pysrc/monitor_v2/monitor_v2/_setup.py`
- SSH executor: `/vast/pysrc/monitor_v2/monitor_v2/commands/simple.py`
- Container logs: `/vast/data/11.0.0.1-*/monitor.log`
- vman.sh: `/vast/deploy/vman.sh`

---

*This analysis was performed during Christmas break 2025 to understand VAST loopback deployment issues and prepare for the next installation attempt.*
