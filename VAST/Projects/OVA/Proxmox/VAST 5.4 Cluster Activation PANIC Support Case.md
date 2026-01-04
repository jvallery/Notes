# VAST Data 5.4 Support Case - Cluster Activation PANIC

  

**Date:** December 29, 2025

**VAST Build:** release-5-4-0-2043819

**Cluster Name:** lb-vast54

**Configuration:** Loopback topology on Proxmox/KVM

  

---

  

## Summary

  

Cluster activation fails with PANIC on dnode-2 during initial cluster creation. The cluster transitions from ACTIVATING → UNKNOWN → INIT and becomes unrecoverable. Two separate installation attempts have failed with similar symptoms.

  

---

  

## Environment

  

### Hypervisor

- **Platform:** Proxmox VE 9.1 (KVM)

- **Host CPU:** AMD Ryzen Threadripper 2920X 12-Core Processor

- **Nested Virtualization:** Enabled

  

### Guest VM

- **OS:** Rocky Linux 8.10 (kernel 4.18.0-553.56.1.el8_10.x86_64)

- **vCPUs:** 24

- **RAM:** 109 GB (first attempt was 97GB)

- **Disk:** 1 TB

- **Network:** VirtIO (eth0: 192.168.30.109)

  

### VAST Configuration

- **Build:** release-5-4-0-2043819

- **Topology:** Loopback (2 cnodes + 2 dnodes in containers)

- **Docker:** Docker CE 26.1.3

  

---

  

## Timeline of Events

  

### First Attempt (97GB RAM) - Failed with OOM

- Bootstrap completed successfully

- Cluster creation initiated, containers started

- During cluster activation, OOM killer terminated processes

- `system_format` PANIC observed

- Cluster stuck in INIT state

- dmesg showed: OOM killer killing `.env` process

  

### Second Attempt (109GB RAM) - Failed with PANIC (NO OOM)

  

| Time (UTC) | Event |

|------------|-------|

| 10:23:16 | Installation script started |

| 10:34:18 | Bootstrap completed |

| 10:38:22 | Cluster create initiated |

| 10:38:37 | Installing build on all 4 hosts |

| 10:39:12 | Finished install containers |

| 10:39:40 | State: INSTALLING → INIT |

| 10:39:49 | Cluster formatting started |

| 10:39:56 | State: INIT → ACTIVATING |

| 10:41:53 | State: ACTIVATING → UNKNOWN |

| 10:42:50 | State: UNKNOWN → INIT |

| 10:57:34 | **PANIC on dnode-2 (11.0.0.1-4400)** |

| 10:57:38 | cluster_deploy state: RUNNING → FAILED |

| 10:57:43 | Leader reconnected, state: UNKNOWN → INIT |

| 10:57:43+ | Cluster remains stuck in INIT |

  

---

  

## PANIC Details

  

### Error Code

```

PANIC[P653:E9:S255:F28d time="2025-12-29 10:57:34.832443472"]

```

  

### Affected Component

- **Node:** dnode-2 (11.0.0.1) - Container: vast_platform_11.0.0.1-4400

  

### Stack Trace

```

===FIBER=0x7fcb99c3ddd0 group=E_VMSG_POLLING_VMSG_KEEP_ALIVE (365) module=E (0)

fiber_id=P00013:E008:S000:F00000019 parent_job_id=F9 state=2 daemon=1 join_count=0

anchor=(nil) gtsk_id=0xffffffffffffffff locker_index=22 is_suspended=0

time_in_suspend=0us (~0.00s) time_since_started=245385178us (~245.39s)

data_bytes_allocated=0

  

===BEGIN TRACEBACK===

0x0000000007ce83b4 P::error_handler at src/plasma/execution/env.cpp:3428

0x0000000007d6ae4e P::Trace::Buffer::write at src/plasma/trace/dbuffer.cpp:38

0x0000000007d6ae4e P::Trace::DBuffer::write at src/plasma/trace/dbuffer.cpp:120

0x0000000007d6ae4e P::Trace::Emitter::record_finish at src/plasma/trace/emitter.cpp:353

0x000000000948d1a5 P::Trace::Emitter::trace_after at src/plasma/trace/emitter.cpp:0

0x000000000948d1a5 void P::Trace::Emitter::trace<> at src/plasma/trace/emitter.hpp:863

0x000000000948d1a5 P::VMsg::VMsg::add_piggyback_acks at src/plasma/vmsg/vmsg.cpp:1455

0x000000000948b924 P::VMsg::VMsg::send_async at src/plasma/vmsg/vmsg.cpp:2072

0x0000000009487aeb P::VMsg::VMsg::send_keepalive at src/plasma/vmsg/vmsg.cpp:376

0x0000000009498840 P::VMsg::VMsg::send_single at src/plasma/vmsg/vmsg.cpp:426

0x0000000009498840 P::VMsg::VMsg::send_keepalives_to_env at src/plasma/vmsg/vmsg.cpp:445

0x0000000009498840 P::VMsg::VMsg::send_all_keepalive at src/plasma/vmsg/vmsg.cpp:484

0x0000000009498840 P::VMsg::vmsg_keepalive_fiber at src/plasma/vmsg/vmsg.cpp:512

0x0000000007cfe7de P::Fiber::main at src/plasma/fiber/fiber.cpp:268

===FINISH TRACEBACK=== (11 hidden frames)

```

  

### Key Observations from Traceback

1. PANIC occurred in **VMsg keepalive fiber** (`vmsg_keepalive_fiber`)

2. Fiber had been running for **245.39 seconds** (~4 minutes) - `time_since_started`

3. Failure in `P::Silo::test_if_stuck()` at `src/plasma/execution/silo.cpp:959`

4. The keepalive mechanism detected a stuck condition

  

---

  

## Pre-PANIC Symptoms

  

### Leader Connection Failures

Starting around 10:42, repeated failures to connect to cluster leader:

```

Cluster Leader connection end-point ('11.0.0.1', 6001, 1) error

Failed to connect to address=11.0.0.1:6001 after 3 attempts.

```

  

### State Oscillations

```

10:39:56 - INIT → ACTIVATING

10:41:53 - ACTIVATING → UNKNOWN (after ~2 min)

10:42:50 - UNKNOWN → INIT

10:42:56 - INIT → UNKNOWN

10:57:43 - UNKNOWN → INIT (after PANIC)

```

  

The cluster never successfully transitioned to ONLINE state.

  

---

  

## Resource State at Time of Failure

  

### Memory (No OOM in second attempt)

```

total used free

Mem: 109Gi 69Gi 35Gi (at steady state after containers started)

Mem: 109Gi 83Gi 16Gi (current state)

```

  

### Container Memory Usage (Post-Failure)

| Container | Memory Used |

|-----------|-------------|

| vast_platform_11.0.0.1-4100 (cnode-1) | 47.28 GB |

| vast_platform_11.0.0.1-4200 (cnode-2) | 3.08 GB |

| vast_platform_11.0.0.1-4300 (dnode-1) | 8.05 GB |

| vast_platform_11.0.0.1-4400 (dnode-2) | 3.91 GB |

| vast_vms | 6.44 GB |

| mcvms | 0.97 GB |

| registry | 17 MB |

| **Total** | **~69 GB** |

  

### No OOM Events

```bash

$ dmesg | grep -i "out of memory"

# No results

```

  

---

  

## Differences from ESXi/VMware

  

This is running on Proxmox/KVM, not VMware ESXi:

1. Docker was NOT pre-installed in the OVA (had to install Docker CE)

2. Using qemu-guest-agent instead of vmtoolsd

3. NIC driver is VirtIO instead of VMXNET3

4. Disk controller is VirtIO-SCSI instead of PVSCSI

  

---

  

## Current State

  

### Cluster

```json

{

"state": "INIT",

"leader_state": "UP",

"enabled": true,

"loopback": true

}

```

  

### Hosts

| Host | Type | State |

|------|------|-------|

| 11.0.0.1-4100 | CNODE | INSTALLED |

| 11.0.0.1-4200 | CNODE | INSTALLED |

| 11.0.0.1-4300 | DNODE | INSTALLED |

| 11.0.0.1-4400 | DNODE | INSTALLED |

  

All hosts are INSTALLED but cluster cannot activate.

  

---

  

## Commands That Failed

  

```bash

# Tried to manually activate

cluster activate --id 1

# Error: system_modify returned an error: SystemModifyResultCode.ILLEGAL_TRANSITION

  

# Tried to deactivate first

cluster deactivate

# Error: Task enable_disable_cluster failed: ILLEGAL_TRANSITION

  

# Tried to format

cluster format --id 1 --psnt lb-vast54 --guid 54539e1c-000d-58a5-97bc-d9733daffa58

# Error: Can run cluster format only on a stopped cluster

```

  

---

  

## Questions for Support

  

1. **Is 109GB RAM sufficient for loopback cluster activation?** First attempt with 97GB failed with OOM, second with 109GB failed without OOM but with same PANIC.

  

2. **What does PANIC code P653:E9:S255:F28d indicate?** The traceback shows `test_if_stuck()` in silo.cpp - what condition causes this?

  

3. **Is there a way to recover from INIT state?** All transition commands fail with ILLEGAL_TRANSITION.

  

4. **Is the loopback configuration supported on KVM/Proxmox?** Or only on VMware ESXi?

  

5. **What is the minimum recommended RAM for loopback cluster on virtual platforms?** We've tried 97GB (OOM) and 109GB (PANIC without OOM).

  

---

  

## Log Files Available

  

- `/vast/vman/vms/log/vms.log` - VMS main log

- `/vast/vman/vms/log/workers.log` - Celery workers log (contains PANIC details)

- `/vast/data/11.0.0.1-4400/traces/env/` - Platform trace files (zstd compressed)

- `/home/centos/vast_install_20251229_102316.log` - Installation script log

  

---

  

## Steps to Reproduce

  

1. Import VAST 5.4 OVA to Proxmox (convert VMDK to qcow2)

2. Configure VM: 24 vCPUs, 109GB RAM, 1TB disk, nested virtualization enabled

3. Install Docker CE (not pre-installed like on ESXi)

4. Install qemu-guest-agent, disable vmtoolsd

5. Run bootstrap: `./vast_bootstrap.sh --interface 192.168.30.109 --skip-prompt`

6. Create loopback cluster: `cluster create --build release-5-4-0-2043819 --name lb-vast54 --loopback`

7. Observe: Cluster goes ACTIVATING → UNKNOWN → INIT, PANIC on dnode-2

  

---

  

*Generated: December 29, 2025*