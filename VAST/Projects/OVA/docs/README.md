# VAST 5.4 Loopback on Proxmox — Unofficial Lab Runbook

> **⚠️ NOT FOR PRODUCTION USE**  
> This is an **unofficial, unsupported** homelab runbook. VAST loopback mode is for development/testing only. Workarounds documented here may break with VAST updates.

---

## 📋 Tested Configuration

| Component | Version/Spec |
|-----------|-------------|
| **Proxmox VE** | 9.1 |
| **VAST Build** | release-5-4-0-2043819 |
| **Guest OS** | Rocky Linux 8 (Python 3.6) |
| **Host CPU** | AMD Threadripper 2920X (12 cores) |
| **Host RAM** | 128 GB |
| **Storage** | 2× 1TB NVMe (PCIe passthrough) |
| **VM Config** | 12 vCPUs, 120 GB RAM |
| **Last Validated** | December 2025 |

---

## 📚 Documentation

| # | Document | Description |
|---|----------|-------------|
| 1 | [Overview](01-Overview.md) | Project goals, hardware environment, topology, networking |
| 2 | [Hardware & Performance](02-Hardware-Performance.md) | Host requirements, PCIe passthrough, ZFS, kernel tuning |
| 3 | [VM Setup](03-VM-Setup.md) | VMDK extraction from OVA, Proxmox VM creation, disk import |
| 4 | [First Boot](04-First-Boot.md) | Guest agent, Docker CE, VirtIO drivers, NVMe, XFS |
| 5 | [Topology Planning](05-Topology-Planning.md) | CNodes, DNodes, virtual drives, capacity calculations |
| 6 | [Pre-Install Tweaks](06-Pre-Install-Tweaks.md) | All workarounds: pip, FD limits, ipmitool, THP, etc. |
| 7 | [Install Script Reference](07-Install-Script-Reference.md) | Script architecture, phases, configuration, usage |

---

## 🚀 Quick Start

### Prerequisites

- Proxmox VE 8.x or 9.x
- VAST 5.4 OVA file (`vast_5.4.ova`)
- AMD/Intel CPU with 12+ cores
- 128GB+ RAM
- 2× NVMe SSDs (1TB+ each)

### Installation

```bash
# 1. Clone or copy docs to your VM
cd /home/centos/docs/scripts

# 2. Create and edit configuration
cp config.env.example config.env
vi config.env

# 3. Run installation
sudo ./install.sh
```

### Phased Installation

```bash
# Run individual phases
sudo ./install.sh --phase pre-bootstrap
sudo ./install.sh --phase bootstrap
sudo ./install.sh --phase post-start
sudo ./install.sh --phase cluster
sudo ./install.sh --phase verify
```

---

## 📁 Files

```
docs/
├── README.md                    # This file
├── 01-Overview.md               # Project scope and disclaimers
├── 02-Hardware-Performance.md   # Hardware requirements
├── 03-VM-Setup.md               # VM creation from OVA
├── 04-First-Boot.md             # Guest OS preparation
├── 05-Topology-Planning.md      # Cluster topology
├── 06-Pre-Install-Tweaks.md     # Workarounds (being merged)
├── 07-Install-Script-Reference.md # Script documentation
├── scripts/
│   ├── install.sh               # Unified install script
│   └── config.env.example       # Configuration template
└── archive/                     # Historical docs and scripts
```

---

## 🔑 Default Credentials

| Component | Username | Password |
|-----------|----------|----------|
| VAST Web UI | `admin` | `123456` |
| VAST vCLI | `admin` | `123456` |
| VM (Rocky Linux) | `centos` | (SSH key) |

> **⚠️ CHANGE DEFAULT PASSWORD IMMEDIATELY AFTER INSTALL**

---

## ⚠️ Critical Warnings

| Warning | Details |
|---------|--------|
| **DO NOT run `dnf update`** | Preserve OVA kernel/drivers for VAST compatibility |
| **PCIe passthrough = no snapshots** | Proxmox cannot snapshot VMs with passthrough devices |
| **Python 3.6 constraints** | Do not upgrade pip beyond 21.3.1 (breaks VAST) |
| **12 vCPUs maximum** | On 12-core host; do not overcommit |

---

## 🌐 Network Configuration

VAST loopback uses multiple IP ranges. Only the management IP must be routable from your network.

| Network | Range | Purpose | Routable? |
|---------|-------|---------|-----------|
| **Management** | Your LAN IP (e.g., 192.168.x.x) | Web UI, API, SSH | ✅ Yes |
| **Internal Loopback** | 11.0.0.1/24 | Container-to-container | ❌ Internal only |
| **VIP Pool** | 15.0.0.1-8/24 | Client mount points | ❌ Internal only |
| **Replication Gateway** | 18.18.0.1-2/24 | Inter-node replication | ❌ Internal only |

### Container Port Mapping

| Container | Purpose | Base Port |
|-----------|---------|-----------|
| `vast_platform_11.0.0.1-4100` | CNode 1 (primary) | 4100 |
| `vast_platform_11.0.0.1-4200` | CNode 2 | 4200 |
| `vast_platform_11.0.0.1-4300` | DNode 1 | 4300 |
| `vast_platform_11.0.0.1-4400` | DNode 2 | 4400 |

### IP Auto-Detection

If `MANAGEMENT_IP` is not set in config.env, the script auto-detects using:
```bash
ip route get 1.1.1.1 | awk '{print $7; exit}'
```

---

## 🌐 Access Points

After successful installation:

- **Web UI**: `https://<MANAGEMENT_IP>`
- **vCLI**: `/vast/data/11.0.0.1-4100/vms.sh vcli`

---

## 📋 Quick Reference Commands

### Check Cluster Status
```bash
# Via API
curl -sk -u admin:123456 https://$(hostname -I | awk '{print $1}')/api/clusters/

# Via vCLI
/vast/data/11.0.0.1-4100/vms.sh vcli cluster show
```

### Check Containers
```bash
docker ps --filter "name=vast"
```

### Check File Descriptor Usage
```bash
cat /proc/sys/fs/file-nr
```

### View Installation Logs
```bash
ls -la /home/centos/docs/install_logs/
tail -f /home/centos/docs/install_logs/install_*.log
```

### Restart Cluster
```bash
# Stop containers
docker stop $(docker ps -q --filter "name=vast")

# Start containers
docker start $(docker ps -aq --filter "name=vast")
```

---

## 🐛 Troubleshooting

| Symptom | Possible Cause | Solution |
|---------|----------------|----------|
| Bootstrap hangs | Missing pip packages | Run `pip3 install pip==21.3.1` (DO NOT use latest) |
| PANIC during boot | FD exhaustion or CPU overcommit | Fix FD limits, reduce vCPUs to ≤ physical cores |
| Monitor retry loop | FD exhaustion | Increase fs.file-max to 8M+ |
| Installation timeout | Slow disk | Use PCIe passthrough for NVMe |
| rsync not found | Missing in container | Copy from host: `docker cp /usr/bin/rsync vast_platform_*:/usr/bin/` |
| VM won't boot | Wrong SCSI controller | Use LSI 53C895A for OVA, then switch to VirtIO |

See [06-Pre-Install-Tweaks.md](06-Pre-Install-Tweaks.md) for complete workaround details.

---

## 📊 System Requirements Summary

| Resource | Minimum | Recommended |
|----------|---------|-------------|
| CPU | 10 cores | 12+ cores |
| RAM | 110 GB | 128 GB |
| Disk (OS) | 200 GB | 200 GB |
| Data Disk | 500 GB | 1+ TB NVMe |
| vCPUs | ≤ physical cores | 12 (on 12-core host) |

---

## 🔗 Related Resources

- [VAST Documentation](https://support.vastdata.com/)
- [Proxmox VE Wiki](https://pve.proxmox.com/wiki/)
- [Docker CE Documentation](https://docs.docker.com/)

---

## 📝 Version History

| Version | Date | Description |
|---------|------|-------------|
| 1.0 | Dec 2025 | Initial Lab Runbook release |

---

*This documentation represents consolidated lessons learned from VAST 5.4 deployment on Proxmox.*
