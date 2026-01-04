# VAST 5.4 Loopback Mode - Bugs, Defects & Workarounds

**Date:** December 30, 2025  
**VAST Version:** 5.4.0 (release-5-4-0-2043819)  
**Environment:** Proxmox 8.3 / Rocky Linux 8 VM  
**Status:** 🔴 Cluster Crashed During Troubleshooting

---

## Executive Summary

After successfully deploying a VAST 5.4 loopback cluster, we encountered a series of bugs and defects during routine troubleshooting that ultimately caused a complete cluster failure. This document catalogs all issues discovered and proposes workarounds for the next deployment.

**Key Finding:** VAST loopback mode appears to be under-tested and contains several bugs that require manual intervention to work around. The mode is clearly intended for internal VAST development/testing, not production use.

---

## 🐛 Critical Bugs Discovered

### Bug #1: Missing `rsync` in Container Images

**Severity:** 🔴 Critical - Prevents node recovery  
**Component:** Container image `release-5-4-0-2043819-x86_64`

**Description:**  
The VAST platform containers do not include `rsync`, which is required by the monitor process to copy packages to the host for installation.

**Symptoms:**
```
monitor_v2.commands.exceptions.ExecError: ssh centos@localhost ... 
'sudo pip3 install -U --no-deps --no-cache-dir /tmp/wlkexvqj'
```
The temp directory doesn't exist because rsync failed silently.

**Root Cause:**  
The monitor's `install_package()` function in `/vast/pysrc/monitor_v2/monitor_v2/_setup.py` uses rsync to copy files:
```python
host_executor.rsync("/vast/install/pysrc/monitor_v2", source_dir)
```
But rsync is not installed in the container.

**Workaround:**
```bash
# Copy rsync from host to all containers BEFORE cluster issues occur
for c in vast_platform_11.0.0.1-4100 vast_platform_11.0.0.1-4200 \
         vast_platform_11.0.0.1-4300 vast_platform_11.0.0.1-4400; do
    sudo docker cp /usr/bin/rsync $c:/usr/bin/rsync
done
```

**Note:** Container restarts will lose rsync! Must re-copy after any restart.

---

### Bug #2: Hardware Management Commands in Loopback Mode

**Severity:** 🔴 Critical - Blocks node activation  
**Component:** VMS node activation task

**Description:**  
When activating a CNode, VMS runs `ipmitool fru print 0` to check hardware - but this is meaningless in a VM and causes activation to fail.

**Symptoms:**
```
Command failed with 1: ssh ... sudo ipmitool fru print 0 | grep "Board Mfg"
Error: Could not open device at /dev/ipmi0 or /dev/ipmi/0
```

**Root Cause:**  
The `modify_cnode` task doesn't check if the cluster is in loopback mode before running hardware validation commands.

**Workaround:**
```bash
# Create a fake ipmitool that returns valid output
sudo cat > /usr/bin/ipmitool << 'EOF'
#!/bin/bash
if [[ "$*" == *"fru print"* ]]; then
    echo "Board Mfg Date        : Mon Jan 01 00:00:00 2024"
    echo "Board Mfg             : VAST Data Loopback"
    echo "Board Product         : Virtual CNode"
    echo "Board Serial          : LOOPBACK-001"
    exit 0
fi
/usr/bin/ipmitool.real "$@" 2>/dev/null || exit 0
EOF
chmod +x /usr/bin/ipmitool
```

---

### Bug #3: Container Package Repositories Unreachable

**Severity:** 🟡 Medium - Prevents package installation  
**Component:** Container DNF/YUM configuration

**Description:**  
All package repositories in the containers point to internal VAST artifactory servers that are unreachable from customer environments.

**Symptoms:**
```
Errors during downloading metadata for repository 'build-external':
  - Curl error (28): Timeout was reached for https://artifactory.vastdata.com/...
```

**Impact:**  
Cannot install any additional packages (like rsync) via normal package manager.

**Workaround:**  
Must copy binaries directly from host system.

---

### Bug #4: Corrupted pip Packages on Host

**Severity:** 🟡 Medium - Causes warnings  
**Component:** Host Python environment

**Description:**  
VAST installation leaves corrupted pip package metadata in site-packages.

**Symptoms:**
```
WARNING: Ignoring invalid distribution -nitor-v2 (/usr/local/lib/python3.6/site-packages)
WARNING: Ignoring invalid distribution - (/usr/local/lib/python3.6/site-packages)
```

**Workaround:**
```bash
sudo rm -rf /usr/local/lib/python3.6/site-packages/-*
sudo rm -rf /usr/local/lib/python3.6/site-packages/~*
```

---

## ⚠️ Design Issues (Not Bugs)

### Issue #1: Extreme Idle CPU/IO Consumption

**Observed Behavior:**  
- Load average: 20-26 on 12 vCPUs with ZERO user data
- Disk I/O: 13,000-40,000 read IOPS on empty cluster
- CPU: ~75% user + ~20% system = 95%+ utilization

**Explanation:**  
In loopback mode, the CPU must emulate all storage operations that would normally be handled by NVMe SSDs. The VAST data plane uses busy-polling and constant background operations:
- VL1 cache management
- Similarity detection scanning
- Metadata housekeeping
- Inter-node heartbeats
- NVRAM emulation

**This is expected behavior for loopback mode, not a bug.** Real VAST clusters offload this to dedicated hardware.

**Recommendation:**  
- Allocate 16+ vCPUs minimum for loopback
- Accept that idle load will be high
- Stop containers when not actively testing

---

### Issue #2: VMS Container Naming Confusion

**Observed Behavior:**  
There are two VMS-related containers:
- `vast_vms` - Full VMS with nginx, HTTPS (5.3GB image)
- `mcvms` - Multi-cluster VMS API only (978MB image)

The `vast_vms` container uses `--rm` flag, so stopping it removes it entirely.

**Impact:**  
After stopping vast_vms, must use `vman.sh` to recreate it:
```bash
/vast/deploy/vman.sh release-5-4-0-2043819 UNKNOWN start
```

---

### Issue #3: Monitor Retry Loop Consumes Resources

**Observed Behavior:**  
When the monitor fails (due to missing rsync), it retries indefinitely with no backoff, consuming CPU and generating massive logs.

**Log Evidence:**
```
ExecError: ssh centos@localhost ... 'sudo pip3 install ...'
[repeats 70+ times]
```

**Impact:**  
Wastes resources and makes logs difficult to parse.

---

## 🔴 Cascade Failure Event (December 30, 2025)

### What Happened

1. Discovered CNode-1 was in FAILED state after 5 hours away
2. Identified missing rsync as root cause
3. Copied rsync to containers
4. Installed fake ipmitool
5. Attempted `cnode activate --name cnode-1`
6. Activation ran for ~8 minutes then failed
7. **Cascade failure began:**
   - DNode-1 entered PANIC state
   - CNode-2 went FAILING
   - Load average spiked to **3762.90**
   - All nodes failed

### Load Average Timeline
| Time | Load Average | Notes |
|------|-------------|-------|
| 02:29 | 22.59 | Normal for loopback |
| 02:41 | 35.10 | After restart |
| 02:53 | 3762.90 | Complete meltdown |
| 02:55 | 431.05 | After emergency stop |
| 02:58 | 21.39 | Recovering |

### Probable Cause

The activation attempt may have triggered data plane reconfiguration that exposed timing bugs or resource exhaustion. The PANIC log shows:
```
PANIC: killing pid=13 at time="2025-12-30 02:52:48": silo=0 is stuck for 2630 ms
```

This suggests the data plane couldn't keep up with cluster state changes.

---

## 📋 Complete Workaround Checklist for v2

### Before Cluster Creation

```bash
# 1. Allocate sufficient resources
# - Minimum: 16 vCPUs, 64GB RAM, 1TB+ disk
# - Recommended: 24 vCPUs for comfortable operation

# 2. Install required packages on host
sudo dnf install -y rsync ipmitool

# 3. Create fake ipmitool BEFORE deployment
sudo mv /usr/bin/ipmitool /usr/bin/ipmitool.real
sudo cat > /usr/bin/ipmitool << 'EOF'
#!/bin/bash
if [[ "$*" == *"fru print"* ]]; then
    echo "Board Mfg Date        : Mon Jan 01 00:00:00 2024"
    echo "Board Mfg             : VAST Data Loopback"
    echo "Board Product         : Virtual Node"
    echo "Board Serial          : LOOPBACK-001"
    exit 0
fi
/usr/bin/ipmitool.real "$@" 2>/dev/null || exit 0
EOF
sudo chmod +x /usr/bin/ipmitool
```

### After Container Start (EVERY TIME)

```bash
# Copy rsync to all platform containers
for c in vast_platform_11.0.0.1-4100 vast_platform_11.0.0.1-4200 \
         vast_platform_11.0.0.1-4300 vast_platform_11.0.0.1-4400; do
    sudo docker cp /usr/bin/rsync $c:/usr/bin/rsync
done
```

### Monitoring Best Practices

```bash
# Check for monitor retry loops
docker logs vast_platform_11.0.0.1-4100 2>&1 | grep -c ExecError

# Check cluster health before doing anything
curl -sk -u admin:123456 'https://192.168.30.109/api/cnodes/' | \
  python3 -c "import sys,json; [print(f'{c[\"name\"]}: {c[\"state\"]}') for c in json.load(sys.stdin)]"

# Monitor load average
uptime
```

---

## 🗺️ v2 Deployment Plan

### Phase 1: Clean Environment

1. Destroy existing VM completely
2. Create fresh Rocky Linux 8 VM with:
   - 16-24 vCPUs
   - 128GB RAM (if available)
   - 1.5TB+ disk

### Phase 2: Pre-Installation Fixes

1. Install rsync and ipmitool on host
2. Create fake ipmitool script
3. Set up swap (4GB recommended)
4. Configure kernel parameters for VAST

### Phase 3: Modified Installation

1. Run prepare_vm_for_vast.sh
2. Run vast_proxmox_install.sh with modifications:
   - Add rsync copy step after container creation
   - Add health check before cluster create
3. Document any new issues

### Phase 4: Validation

1. Verify all nodes ACTIVE
2. Create test view
3. Mount and write test data
4. Graceful shutdown test
5. Restart and verify data persistence

---

## 🤔 Questions for VAST Support

1. Why doesn't the loopback container image include rsync?
2. Why does node activation run ipmitool in loopback mode?
3. Is there a way to disable hardware validation for loopback clusters?
4. What is the expected idle resource consumption for loopback?
5. Are there undocumented flags to reduce background activity?

---

## Appendix: Files Modified During Troubleshooting

| File/Location | Modification | Reason |
|---------------|--------------|--------|
| `/usr/bin/ipmitool` | Replaced with wrapper | Hardware validation bypass |
| `/usr/bin/rsync` in containers | Copied from host | Missing in image |
| `/usr/local/lib/python3.6/site-packages/` | Cleaned corrupted packages | pip warnings |

---

*Document created after cluster failure during recovery attempt. All findings based on VAST 5.4.0 loopback mode on Proxmox/KVM.*
