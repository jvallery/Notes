# VAST 5.4 Loopback - Lessons Learned

**Last Updated:** December 30, 2025

This document captures key lessons learned from deploying and operating VAST 5.4 in loopback mode on Proxmox/KVM.

---

## Critical Lessons

### 1. Loopback Mode Is NOT Production-Ready

**Lesson:** VAST loopback mode is intended for VAST internal development and testing. It has numerous bugs and requires extensive workarounds.

**Evidence:**
- Missing rsync in containers
- Hardware validation (ipmitool) runs on VMs
- High idle resource consumption (20+ load on 12 CPUs)
- Cascade failures during normal operations

**Recommendation:** Use loopback only for demos, education, or development. Never for production workloads.

---

### 2. Container Fixes Are Non-Persistent

**Lesson:** Any binaries copied into VAST containers are lost on container restart.

**Impact:** After every container restart, you must:
```bash
for c in vast_platform_11.0.0.1-{4100,4200,4300,4400}; do
    sudo docker cp /usr/bin/rsync $c:/usr/bin/rsync
done
```

**Recommendation:** Create a post-start script and document this requirement prominently.

---

### 3. Don't Troubleshoot Under Load

**Lesson:** When the cluster is already under stress (high load, failing nodes), attempting recovery operations can trigger cascade failures.

**What Happened:** 
- Cluster was at 25 load average with CNode-1 failed
- Attempted `cnode activate --name cnode-1`
- Triggered cascade failure, load spiked to 3762
- All nodes failed

**Recommendation:** 
1. Check cluster health BEFORE any recovery action
2. If nodes are failing, stop all containers first
3. Let the system cool down before restarting
4. Start fresh rather than trying to recover a degraded cluster

---

### 4. The Monitor Retry Loop Is Dangerous

**Lesson:** When the monitor process fails (e.g., due to missing rsync), it retries indefinitely with no backoff, consuming resources.

**Symptoms:**
- Unexplained high CPU usage
- Thousands of SSH connections
- Massive log spam

**Detection:**
```bash
docker logs vast_platform_11.0.0.1-4100 2>&1 | grep -c "ExecError\|pip3 install"
```

**Recommendation:** Check logs for retry patterns before assuming the cluster is healthy.

---

### 5. VMS Container Is Ephemeral

**Lesson:** The `vast_vms` container runs with `--rm` flag. Stopping it deletes it.

**Recovery:**
```bash
/vast/deploy/vman.sh release-5-4-0-2043819 UNKNOWN start
```

**Recommendation:** Never stop vast_vms unless you intend to completely restart VMS.

---

### 6. Resource Requirements Are Higher Than Expected

**Lesson:** VAST loopback consumes extreme resources even when idle.

**Observed (empty cluster, no data):**
- Load average: 20-26 on 12 vCPUs
- Disk I/O: 13,000-40,000 read IOPS
- CPU: 75-95% utilization

**Why:**
- All storage operations run in software
- Busy-polling in data plane
- Background processes (VL1, similarity, metadata)

**Recommendation:** 
- Minimum: 16 vCPUs, 64GB RAM
- Recommended: 24 vCPUs, 128GB RAM
- Stop containers when not testing to reclaim resources

---

### 7. Package Managers Won't Work in Containers

**Lesson:** All DNF/YUM repos in VAST containers point to internal VAST servers.

**Impact:** Cannot install packages normally:
```
Curl error (28): Timeout was reached for https://artifactory.vastdata.com/...
```

**Workaround:** Copy binaries directly from host:
```bash
docker cp /usr/bin/rsync vast_platform_11.0.0.1-4100:/usr/bin/rsync
```

---

### 8. API Health Checks Are Essential

**Lesson:** Check cluster health via API BEFORE and AFTER any operation.

**Quick Health Check:**
```bash
# Check all node states
curl -sk -u admin:123456 'https://192.168.30.109/api/cnodes/' | \
  python3 -c "import sys,json; [print(f'{c[\"name\"]}: {c[\"state\"]}') for c in json.load(sys.stdin)]"

curl -sk -u admin:123456 'https://192.168.30.109/api/dnodes/' | \
  python3 -c "import sys,json; [print(f'{c[\"name\"]}: {c[\"state\"]}') for c in json.load(sys.stdin)]"
```

**Expected healthy state:** All nodes should be `ACTIVE`

---

### 9. Understand the Container Architecture

**Lesson:** VAST loopback uses multiple containers with different purposes:

| Container | Purpose | Size | Notes |
|-----------|---------|------|-------|
| `vast_platform_11.0.0.1-4100` | CNode 1 | - | Runs data plane |
| `vast_platform_11.0.0.1-4200` | CNode 2 | - | Runs data plane |
| `vast_platform_11.0.0.1-4300` | DNode 1 | - | Runs storage |
| `vast_platform_11.0.0.1-4400` | DNode 2 | - | Runs storage |
| `vast_vms` | VMS + Web UI | 5.3GB | API, nginx, HTTPS |
| `mcvms` | Multi-cluster VMS | 978MB | Lightweight API |
| `registry` | Container registry | - | Local image hosting |

---

### 10. graceful Shutdown Is Critical

**Lesson:** Always stop containers in the right order and allow graceful shutdown.

**Shutdown Order:**
1. Stop VAST services via VMS (if accessible)
2. Stop platform containers: `docker stop vast_platform_11.0.0.1-{4100..4400}`
3. Stop VMS: `docker stop vast_vms`
4. Stop registry last

**Never:** Use `docker kill` or forcefully terminate containers

---

## Summary of Required Pre-Work for v2

Before next deployment, complete these steps:

### 1. Host Preparation
```bash
sudo dnf install -y rsync ipmitool
```

### 2. Create Fake ipmitool
```bash
sudo mv /usr/bin/ipmitool /usr/bin/ipmitool.real
sudo cat > /usr/bin/ipmitool << 'EOF'
#!/bin/bash
if [[ "$*" == *"fru print"* ]]; then
    echo "Board Mfg             : VAST Data Loopback"
    exit 0
fi
/usr/bin/ipmitool.real "$@" 2>/dev/null || exit 0
EOF
sudo chmod +x /usr/bin/ipmitool
```

### 3. Post-Container-Start Script
```bash
#!/bin/bash
# /home/centos/fix_vast_containers.sh
# Run this AFTER containers start

for c in vast_platform_11.0.0.1-4100 vast_platform_11.0.0.1-4200 \
         vast_platform_11.0.0.1-4300 vast_platform_11.0.0.1-4400; do
    echo "Fixing $c..."
    sudo docker cp /usr/bin/rsync $c:/usr/bin/rsync
done
echo "Done. Check cluster health with:"
echo "  curl -sk -u admin:123456 'https://192.168.30.109/api/cnodes/'"
```

---

*These lessons were learned the hard way. Document everything. Test carefully. When in doubt, stop and think.*
