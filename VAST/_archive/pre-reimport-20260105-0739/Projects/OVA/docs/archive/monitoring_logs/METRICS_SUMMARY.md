# Performance Metrics Summary - VAST 5.4 Installation

**Monitoring Period:** 2025-12-29 18:28:56 to 19:14:31 (45 minutes 35 seconds)

---

## CPU Metrics

### CPU Steal (Hypervisor Contention)
- **Maximum:** 0.33%
- **Average:** < 0.1%
- **Assessment:** ✅ No significant hypervisor contention

### CPU Usage During Peak Load
- **Max %user:** 79%
- **Max %sys:** 25%
- **Max %iowait:** 1%

---

## Memory Metrics

### Memory Usage Timeline
| Time | Used | Free | Available |
|------|------|------|-----------|
| Start (18:28) | 1.0 GB | 116 GB | 114 GB |
| Peak (18:55) | 105 GB | 2.3 GB | 4.9 GB |
| Steady (19:14) | 108 GB | 3 GB | 2-4 GB |

### Container Memory (Final)
| Container | Memory |
|-----------|--------|
| cnode-2 (4200) | 49.0 GB |
| cnode-1 (4100) | 38.3 GB |
| dnode-2 (4400) | 8.0 GB |
| dnode-1 (4300) | 8.0 GB |
| vast_vms | 7.2 GB |
| mcvms | 0.9 GB |

---

## I/O Metrics

### Disk Latency
- **Max r_await:** 21.65 ms
- **Max w_await:** 36.02 ms
- **Assessment:** ✅ Acceptable for virtualized storage

---

## Load Average

| Time | 1-min | 5-min | 15-min |
|------|-------|-------|--------|
| Start | 0.02 | 0.02 | 0.00 |
| Peak | 40.0 | 35.0 | 27.0 |
| Steady | 32.0 | 32.0 | 27.0 |

---

## Scheduling Gap Analysis

- **Heartbeat interval:** 1 second
- **Gaps > 2 seconds detected:** 0
- **Assessment:** ✅ No scheduling stalls

---

## Key Timestamps

| Event | Time | Duration from Start |
|-------|------|---------------------|
| Script started | 18:32:13 | 0:00 |
| Bootstrap started | 18:32:13 | 0:00 |
| VMS up | 18:42:xx | ~10 min |
| Cluster create | 18:47:00 | ~15 min |
| State: ACTIVATING | 18:48:39 | ~16 min |
| State: ONLINE | 18:59:20 | ~27 min |
| Installation complete | 19:04:48 | ~32 min |

---

*Generated from monitoring logs in this directory*
