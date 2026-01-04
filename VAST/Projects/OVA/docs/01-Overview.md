# VAST Data 5.4 Loopback on Proxmox — Unofficial Lab Runbook

**Project:** VAST Data 5.4 Loopback Cluster on Proxmox (Homelab)  
**Version:** 1.1  
**Last Updated:** December 30, 2025  

---

## ⚠️ Important Disclaimers

> **NOT FOR PRODUCTION USE**
>
> - This is an **unofficial, unsupported** deployment guide
> - VAST loopback mode is for **development/testing only**
> - Workarounds documented here may break with VAST updates
> - VAST Data has not endorsed or validated this approach
> - **You accept all risk** of data loss and system instability

---

## Project Goals

This project documents the complete process of deploying VAST Data 5.4 storage software in a **homelab environment** using Proxmox VE as the hypervisor. The goal is educational: understanding how enterprise-grade storage systems work by running them on commodity hardware.

### Why This Project?

- **Learning:** Hands-on experience with a production-quality distributed storage system
- **Experimentation:** Safe environment to test VAST features without production impact
- **Documentation:** Create a repeatable process for homelab enthusiasts

### What is VAST Data?

VAST Data is an enterprise storage platform that provides:
- **Universal storage:** NFS, SMB, S3 object storage from a single namespace
- **Flash-native architecture:** Designed for NVMe SSDs
- **Similarity reduction:** Inline deduplication and compression
- **Scale-out design:** CNodes (compute) + DNodes (data) architecture

### Loopback Mode

VAST provides a "loopback" mode that runs a complete cluster within a single VM:
- 2 CNodes (Compute Nodes) - handle client I/O
- 2 DNodes (Data Nodes) - manage storage
- VMS (VAST Management Service) - cluster management
- All running as Docker containers

**Important:** Loopback mode is for development/testing only, not production use.

---

## Hardware Environment

### Proxmox Host

| Component | Specification |
|-----------|---------------|
| **CPU** | AMD Ryzen Threadripper 2920X (12 cores / 24 threads) |
| **RAM** | 128 GB DDR4 |
| **NVMe** | 2× 1 TB NVMe SSDs (for VAST data) |
| **Boot** | Separate SATA SSD (for Proxmox OS) |
| **Network** | 1 GbE (management) |

### Why This Hardware?

- **12 physical cores:** VAST is latency-sensitive; we allocate 1:1 vCPU to physical cores
- **128 GB RAM:** VAST containers consume ~110 GB at steady state
- **2× NVMe:** Provide fast storage backend for VAST's virtual drives
- **Separate boot drive:** Allows dedicated NVMe pool for VAST data

---

## Deployment Topology

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          PROXMOX HOST (Bare Metal)                          │
│                      AMD Threadripper 2920X | 128GB RAM                      │
│                                                                              │
│  ┌────────────────────────────────────────────────────────────────────────┐ │
│  │                         VAST VM (Rocky Linux 8)                        │ │
│  │                        12 vCPUs | 120 GB RAM                           │ │
│  │                                                                        │ │
│  │  ┌──────────────────────────────────────────────────────────────────┐ │ │
│  │  │                    Docker Containers                              │ │ │
│  │  │                                                                   │ │ │
│  │  │  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌──────────┐   │ │ │
│  │  │  │ CNode-1 │ │ CNode-2 │ │ DNode-1 │ │ DNode-2 │ │   VMS    │   │ │ │
│  │  │  │  4100   │ │  4200   │ │  4300   │ │  4400   │ │ +MCVMS   │   │ │ │
│  │  │  └─────────┘ └─────────┘ └─────────┘ └─────────┘ └──────────┘   │ │ │
│  │  │                                                                   │ │ │
│  │  └──────────────────────────────────────────────────────────────────┘ │ │
│  │                                                                        │ │
│  │  Storage:                                                              │ │
│  │  ├── /dev/sda (50 GB) - OS disk (from converted VMDK)                 │ │
│  │  └── /dev/nvme0n1, /dev/nvme1n1 - PCIe passthrough NVMe (2 TB total)  │ │
│  │                                                                        │ │
│  │  Networking:                                                           │ │
│  │  ├── eth0: 192.168.x.x (external management)                          │ │
│  │  ├── dummy0: 11.0.0.1 (loopback cluster)                              │ │
│  │  └── VIPs: 15.0.0.x (data access, internal only)                      │ │
│  │                                                                        │ │
│  └────────────────────────────────────────────────────────────────────────┘ │
│                                                                              │
│  Storage Backend:                                                            │
│  ├── local (SATA SSD) - Proxmox OS                                          │
│  └── nvme-passthrough - 2× NVMe passed directly to VAST VM                  │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Source Material: VMware ESXi OVA

VAST distributes their loopback image as a **VMware ESXi OVA**. This project converts it to run on Proxmox/KVM:

### What's in the OVA?

- **Rocky Linux 8** base OS
- **Pre-configured directories** at `/vast/`
- **Bootstrap scripts** for cluster deployment
- **Python environment** for VAST tools

### What's NOT in the OVA (for KVM)?

- **Docker:** Must be installed manually (VMware OVA has it pre-installed)
- **Guest Agent:** VMware Tools → must replace with `qemu-guest-agent`
- **VirtIO drivers:** May need to rebuild initramfs

### OVA-to-Proxmox Conversion Process

1. Extract VMDK from OVA tarball
2. Convert VMDK to qcow2 (or import directly)
3. Create VM with VirtIO devices
4. Boot and install KVM-specific components
5. Run VAST bootstrap

See [03-VM-Setup.md](03-VM-Setup.md) for detailed steps.

---

## Proxmox Host Setup (Brief)

### Proxmox Version

- **Proxmox VE 9.1** (latest stable as of December 2025)
- Kernel with KVM/nested virtualization enabled

### Key Host Configuration

```bash
# Enable nested virtualization (AMD)
echo "options kvm_amd nested=1" > /etc/modprobe.d/kvm-amd.conf
modprobe -r kvm_amd && modprobe kvm_amd

# Verify
cat /sys/module/kvm_amd/parameters/nested  # Should show: 1
```

### IOMMU for PCIe Passthrough

If using NVMe passthrough (recommended):

```bash
# /etc/default/grub - add to GRUB_CMDLINE_LINUX_DEFAULT
amd_iommu=on iommu=pt

# Regenerate grub
update-grub

# Reboot
```

### Host Resources

| Allocated | Purpose |
|-----------|---------|
| ~4 GB RAM | Proxmox host OS + ZFS ARC (if using ZFS) |
| ~120 GB RAM | VAST VM |
| 1× SSD | Proxmox OS |
| 2× NVMe | VAST data (passthrough to VM) |

---

## Networking

### External Access

| Address | Purpose |
|---------|---------|
| 192.168.30.109 | VM management IP (example) |
| 192.168.30.109:443 | VMS Web UI (HTTPS) |
| 192.168.30.109:22 | SSH access |

### Internal Loopback

| Address | Purpose |
|---------|---------|
| 11.0.0.1 | Loopback node base IP |
| 15.0.0.1-8 | Data VIPs (NFS/SMB) - internal only |
| 18.18.0.1-2 | Replication gateway - internal only |

**Note:** The 15.0.0.x VIPs are only accessible from within the VM. For external access, either:
- SSH into VM and mount from there
- Set up NAT/port forwarding (advanced)

---

## Key Lessons Learned

Through multiple deployment attempts, we discovered:

### 1. CPU Allocation (Possibly Critical)

- Consider limiting vCPUs to physical core count
- 24 vCPUs on 12 cores → PANIC (correlation, not proven causation)
- 12 vCPUs on 12 cores → Success (also had FD bug fixes)
- Root cause may have been FD exhaustion, CPU overcommit, or both

### 2. Memory Requirements

- **Minimum 117 GB RAM** for loopback cluster
- 97 GB → OOM during activation
- 109 GB → Worked but tight
- 120 GB → Comfortable margin

### 3. Known Bugs and Workarounds

- Missing `rsync` in container images → Copy from host
- Missing `pip` on host → Pre-install before bootstrap
- `ipmitool` hardware checks → Create fake ipmitool script
- Monitor retry loops → Pre-install monitor_v2 package

See [06-Pre-Install-Tweaks.md](06-Pre-Install-Tweaks.md) for complete workaround details.

---

## Document Index

| Document | Description |
|----------|-------------|
| [01-Overview.md](01-Overview.md) | This document - project goals and context |
| [02-Hardware-Performance.md](02-Hardware-Performance.md) | Hardware requirements and tuning |
| [03-VM-Setup.md](03-VM-Setup.md) | VM creation and VMDK import |
| [04-First-Boot.md](04-First-Boot.md) | Post-boot configuration |
| [05-Topology-Planning.md](05-Topology-Planning.md) | Loopback topology options |
| [06-Pre-Install-Tweaks.md](06-Pre-Install-Tweaks.md) | Host preparation and workarounds |
| [07-Install-Script-Reference.md](07-Install-Script-Reference.md) | Installation automation |
| [scripts/install.sh](scripts/install.sh) | Main installation script |
| [scripts/config.env.example](scripts/config.env.example) | Configuration template (copy to config.env) |

---

## Quick Reference

### Default Credentials

| Service | Username | Password |
|---------|----------|----------|
| VMS Web UI | admin | 123456 |
| VM SSH | centos | (your password) |

### Key Paths

| Path | Purpose |
|------|---------|
| `/vast/bundles/` | VAST installation packages |
| `/vast/deploy/` | Deployment configuration |
| `/vast/data/` | Container data directories |
| `/vast/drives/` | Virtual SSD/NVRAM files (on NVMe, not OS disk) |

### Essential Commands

```bash
# Check cluster status
curl -sk -u admin:123456 'https://localhost/api/clusters/' | jq '.[0].state'

# Access vCLI
/vast/data/11.0.0.1-4100/vms.sh vcli

# Start containers after reboot
./scripts/start_vms.sh

# Check container health
docker ps --format "table {{.Names}}\t{{.Status}}"
```

---

## Archive

Previous documentation and scripts from iterative development are preserved in [archive/](archive/). These contain detailed debugging information and lessons learned from failed attempts.

---

*Next: [02-Hardware-Performance.md](02-Hardware-Performance.md) - Hardware requirements and performance tuning*
