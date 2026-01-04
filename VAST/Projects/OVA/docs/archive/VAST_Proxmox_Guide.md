# VAST Data 5.4 on Proxmox - Complete Installation Guide

**Version:** 1.0  
**Date:** December 29, 2025  
**Platform:** Proxmox VE 9.1 / KVM  
**VAST Build:** release-5-4-0-2043819

---

## Table of Contents

1. [Overview](#overview)
2. [Prerequisites](#prerequisites)
3. [Quick Start](#quick-start)
4. [Understanding the Architecture](#understanding-the-architecture)
5. [Manual Installation Steps](#manual-installation-steps)
6. [Loopback Networking](#loopback-networking)
7. [Post-Installation](#post-installation)
8. [Troubleshooting](#troubleshooting)
9. [Reference](#reference)

---

## Overview

The VAST Data 5.4 virtual appliance is distributed as an OVA designed for VMware ESXi. 
This guide documents how to run it on Proxmox VE (KVM) with a loopback network configuration.

### What This Guide Covers

- Installing VAST Data 5.4 from OVA on Proxmox/KVM
- Resolving compatibility issues between VMware OVA and KVM
- Configuring loopback networking for single-VM deployment
- Automating the entire installation process

### Key Differences from VMware Deployment

| Aspect | VMware ESXi | Proxmox/KVM | Solution |
|--------|-------------|-------------|----------|
| Guest Tools | open-vm-tools | qemu-guest-agent | Install qemu-guest-agent |
| Docker | Pre-installed | NOT installed | Install Docker CE first |
| NIC Driver | VMXNET3 | VirtIO | Already handled by import |
| Disk Controller | PVSCSI | VirtIO-SCSI | Works as-is |

---

## Prerequisites

### Hardware Requirements

| Resource | Minimum | Recommended | Notes |
|----------|---------|-------------|-------|
| vCPUs | 24 cores | 32 cores | |
| Memory | **128 GB** | 128 GB+ | **97GB is NOT sufficient - causes OOM** |
| Storage | 1 TB | 1.5 TB+ | |
| Network | 1 NIC | 2 NICs | |

> ⚠️ **WARNING:** 97GB RAM is insufficient for the full loopback cluster. The 4 platform 
> containers (2 cnodes + 2 dnodes) consume ~75GB+ during initialization. With insufficient 
> memory, the OOM killer will terminate processes causing `system_format` failures and 
> leaving the cluster in an unrecoverable INIT state.

### Proxmox VM Configuration

When importing the OVA to Proxmox, use these settings:

| Setting | Recommended Value |
|---------|-------------------|
| CPU Type | host |
| Machine | q35 |
| BIOS | SeaBIOS |
| Network | VirtIO |
| Nested Virtualization | **Enabled** (required) |

### Enabling Nested Virtualization

On the Proxmox host:

```bash
# For Intel CPUs
echo "options kvm_intel nested=1" > /etc/modprobe.d/kvm-intel.conf

# For AMD CPUs  
echo "options kvm_amd nested=1" > /etc/modprobe.d/kvm-amd.conf

# Reload module
modprobe -r kvm_intel && modprobe kvm_intel  # or kvm_amd
```

Verify in the guest:
```bash
cat /sys/module/kvm_amd/parameters/nested  # Should show: 1
```

### Pre-Import Checklist

Before running the installation:

- [ ] OVA imported to Proxmox and VM created
- [ ] VM has 24+ vCPUs, 96+ GB RAM, 1+ TB disk
- [ ] Nested virtualization enabled
- [ ] Network connectivity to internet (for yum repos)
- [ ] SSH access as user `centos` (default password: `centos`)

---

## Quick Start

### Automated Installation

The entire installation is automated by a single script:

```bash
# SSH to the VM as centos
ssh centos@<vm-ip>

# Run the installer
chmod +x vast_proxmox_install.sh
./vast_proxmox_install.sh
```

The script handles:
1. Docker installation and group membership
2. qemu-guest-agent installation
3. VMware tools removal
4. Registry and network configuration
5. VAST bootstrap execution
6. Loopback cluster creation
7. Waiting for cluster to come online

**Estimated time:** 20-40 minutes

### After Installation

Access the VMS Web UI:
- **URL:** `https://<vm-ip>`
- **Credentials:** admin / 123456

Access vCLI:
```bash
/vast/data/11.0.0.1-4100/vms.sh vcli
```

---

## Understanding the Architecture

### Loopback Topology

In loopback mode, VAST runs a complete cluster inside a single VM:

```
┌─────────────────────────────────────────────────────────────┐
│                    Proxmox VM (Rocky Linux)                  │
│                                                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐       │
│  │   CNode 1    │  │   CNode 2    │  │   Registry   │       │
│  │ 11.0.0.1-4100│  │ 11.0.0.1-4200│  │  (Docker)    │       │
│  └──────────────┘  └──────────────┘  └──────────────┘       │
│                                                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐       │
│  │   DNode 1    │  │   DNode 2    │  │  VMS/MCVMS   │       │
│  │ 11.0.0.1-4300│  │ 11.0.0.1-4400│  │  (Docker)    │       │
│  └──────────────┘  └──────────────┘  └──────────────┘       │
│                                                              │
│  Network Interfaces:                                         │
│  ├── eth0: 192.168.x.x (external management)                │
│  ├── dummy0: 11.0.0.1, 15.0.0.100 (internal loopback)       │
│  └── dummy1: 12.0.0.1 (secondary loopback)                  │
└─────────────────────────────────────────────────────────────┘
```

### Docker Containers

| Container | Purpose | Port |
|-----------|---------|------|
| registry | Local Docker registry | 5000 |
| vast_vms | VMS management service | 443 |
| mcvms | Multi-cluster VMS | - |
| vast_platform_11.0.0.1-4100 | CNode 1 | - |
| vast_platform_11.0.0.1-4200 | CNode 2 | - |
| vast_platform_11.0.0.1-4300 | DNode 1 | - |
| vast_platform_11.0.0.1-4400 | DNode 2 | - |

### Network Configuration

The loopback configuration creates internal-only VIP pools:

| Pool | IP Range | Subnet | Purpose |
|------|----------|--------|---------|
| vippool-1 | 15.0.0.1 - 15.0.0.8 | /24 | Data access (NFS/SMB) |
| gateway-1 | 18.18.0.1 - 18.18.0.2 | /24 | Replication |

**Important:** These VIPs are only accessible from within the VM itself.

---

## Manual Installation Steps

If you prefer to run steps manually (or the automated script fails), follow these steps:

### Step 1: Install Docker

```bash
# Install Docker CE
sudo yum install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin

# Enable and start
sudo systemctl enable docker
sudo systemctl start docker

# Add user to docker group
sudo usermod -aG docker centos

# Activate group membership (choose one):
newgrp docker          # Creates subshell with docker group
# OR
exit                   # Logout and SSH back in
```

**Verify docker works without sudo:**
```bash
docker ps
docker images
```

### Step 2: Install Proxmox Guest Agent

```bash
# Install qemu-guest-agent
sudo yum install -y qemu-guest-agent
sudo systemctl enable qemu-guest-agent
sudo systemctl start qemu-guest-agent

# Disable VMware tools (not needed)
sudo systemctl disable vmtoolsd
```

### Step 3: Configure Local Registry

```bash
# Set up registry cache pointer
sudo mkdir -p /file_server
sudo chown centos /file_server
echo "vastdata.registry.local:5000" > /file_server/DCACHE

# Add registry hostname to /etc/hosts
echo "11.0.0.1 vastdata.registry.local" | sudo tee -a /etc/hosts

# Configure Docker for insecure registry
echo '{ "insecure-registries": ["vastdata.registry.local:5000"] }' | sudo tee /etc/docker/daemon.json
sudo systemctl restart docker
```

### Step 4: Prepare Directories

```bash
# Create required directories
sudo mkdir -p /vast/bundles /vast/deploy /vast/data /vast/vman/vms/log
sudo chown -R centos:centos /vast

# Set OS release marker
echo '1.1.1' | sudo tee /etc/vast-os-release
sudo chmod 644 /etc/vast-os-release
```

### Step 5: Set Up SSH Keys

```bash
# Generate SSH key if needed
[ ! -f ~/.ssh/id_rsa ] && ssh-keygen -f ~/.ssh/id_rsa -q -N ""

# Add to authorized_keys
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys

# Copy to VAST deploy location
sudo cp ~/.ssh/id_rsa /vast/deploy/ssh_key.pem
sudo chown centos:centos /vast/deploy/ssh_key.pem
chmod 600 /vast/deploy/ssh_key.pem
```

### Step 6: Run VAST Bootstrap

```bash
# Set environment
export BUILD=release-5-4-0-2043819
export MGMT_IP=$(hostname -I | awk '{print $1}')

# Disable IPv6 on management interface
IFACE=$(ip -o -4 addr show | grep "$MGMT_IP" | awk '{print $2}')
echo 1 | sudo tee /proc/sys/net/ipv6/conf/$IFACE/disable_ipv6

# Clear hugepages
echo 0 | sudo tee /proc/sys/vm/nr_hugepages

# Run bootstrap
cd /vast/bundles
./vast_bootstrap.sh --interface ${MGMT_IP} --skip-prompt
```

### Step 7: Create Loopback Cluster

```bash
# Create loopback configuration
cat << 'EOF' > /vast/deploy/loopback_conf.yml
name: loopA
loopback: true
vip_pools:
   vippool-1:
     start_ip: '15.0.0.1'
     end_ip: '15.0.0.8'
     subnet_bits: 24
   gateway-1:
     role: 'replication'
     start_ip: '18.18.0.1'
     end_ip: '18.18.0.2'
     subnet_bits: 24
vms_ipv6: '1001::1'
vip_pool_segments:
  ipv4:
    protocols:
    - start_ip: '15.0.0.1'
      end_ip: '15.0.0.8'
      subnet_bits: 24
    replication: []
  ipv6:
  - end_ip: 1000::10
    start_ip: 1000::1
    subnet_bits: 120
EOF

# Create cluster
export BUILD=release-5-4-0-2043819
export VAST_INSTALL_ARGS='--vsettings CAS_OVER_RPC=true,IN_CLUSTER_COMMUNICATION_TCP=true'
export pem_file=/vast/deploy/ssh_key.pem

cd /vast/deploy
./vman.sh $BUILD $pem_file vcli -u admin -p 123456 -c cluster create \
    --build ${BUILD} ${VAST_INSTALL_ARGS} --name lb-vast54 --loopback
```

### Step 8: Monitor Progress

```bash
# Watch containers
watch -n5 'docker ps --format "table {{.Names}}\t{{.Status}}"'

# Check cluster state
curl -k -s https://$(hostname -I | awk '{print $1}')/api/clusters/1/ -u admin:123456 | python3 -m json.tool

# Check hosts
curl -k -s https://$(hostname -I | awk '{print $1}')/api/hosts/ -u admin:123456 | python3 -m json.tool
```

---

## Loopback Networking

### Default Configuration

The loopback topology uses internal dummy interfaces for all VAST traffic:

| Interface | IP Addresses | Purpose |
|-----------|--------------|---------|
| eth0 | DHCP (e.g., 192.168.30.109) | External management |
| dummy0 | 11.0.0.1/24, 15.0.0.100/24 | Node communication, VIPs |
| dummy1 | 12.0.0.1/24 | Secondary network |
| virbr0 | 192.168.122.1/24 | libvirt (unused) |

### Accessing VAST from Within the VM

The VIP pool (15.0.0.0/24) is only accessible from within the VM:

```bash
# Mount NFS export from within the VM
sudo mount -t nfs 15.0.0.1:/data /mnt/vast

# Test SMB
smbclient -L //15.0.0.1 -U admin
```

### External Access (Optional)

To access VAST from external clients, you have two options:

#### Option A: Create External VIP Pool

Create a VIP pool using real IPs from your network:

```bash
# In vCLI:
vippool create --ip-ranges 192.168.30.201,192.168.30.202 --subnet-cidr 30 --name external
```

Then add a route on your router:
```bash
ip route add 192.168.30.200/30 via 192.168.30.109
```

#### Option B: NAT/Port Forwarding

Use iptables to forward traffic:
```bash
# Forward NFS port
sudo iptables -t nat -A PREROUTING -p tcp --dport 2049 -j DNAT --to-destination 15.0.0.1:2049
sudo iptables -t nat -A POSTROUTING -j MASQUERADE
```

---

## Post-Installation

### Verify Cluster Health

```bash
# Access vCLI
/vast/data/11.0.0.1-4100/vms.sh vcli

# Check components
cluster show
cnode show
dnode show
vippool show
```

### Create a Test Export

```bash
# In vCLI:
view create --name testshare --path /testshare --protocols NFS
```

### After VM Reboot

VAST containers do not auto-start. Run:

```bash
cd /home/centos
./start_vms.sh
```

Or manually:
```bash
docker start registry vast_vms mcvms
# Wait for VMS to start platform containers
```

### Default Credentials

| Service | Username | Password |
|---------|----------|----------|
| VMS Web UI | admin | 123456 |
| vCLI | admin | 123456 |
| VM SSH | centos | centos |

---

## Troubleshooting

### Docker Permission Denied

**Symptom:**
```
permission denied while trying to connect to the Docker daemon socket
```

**Solution:**
```bash
# Verify user is in docker group
cat /etc/group | grep docker

# Activate group membership
newgrp docker
# OR logout and login again
```

### Bootstrap Failed

**Symptom:** Errors in `/vast/bundles/bootstrap.log`

**Solution:**
1. Check docker access: `docker ps`
2. Check disk space: `df -h`
3. Clean up and retry:
   ```bash
   docker stop $(docker ps -aq) 2>/dev/null
   docker rm $(docker ps -aq) 2>/dev/null
   sudo rm -rf /vast/data/* /vast/vman/*
   # Run installer again
   ```

### Cluster Stuck in INSTALLING

**Symptom:** `state: INSTALLING` for >30 minutes

**Diagnosis:**
```bash
# Check containers
docker ps -a

# Check VMS logs
docker logs vast_vms 2>&1 | tail -100

# Check host states
curl -k -s https://$(hostname -I | awk '{print $1}')/api/hosts/ -u admin:123456 | python3 -m json.tool
```

**Common causes:**
- Docker permission issues during bootstrap
- Insufficient memory
- Previous failed install leaving stale state

### Cluster Stuck in INIT State (OOM Failure)

**Symptom:** 
- Cluster state shows `INIT` and never progresses
- Hosts show state `INSTALLED` but cluster won't activate
- VMS logs show `system_format` PANIC or completion failures

**Diagnosis:**
```bash
# Check dmesg for OOM killer activity
dmesg | grep -i "out of memory"
dmesg | grep -i "killed process"

# Check container memory usage
docker stats --no-stream

# Check host states
curl -k -s https://$(hostname -I | awk '{print $1}')/api/hosts/ -u admin:123456 | \
  python3 -c "import sys,json; [print(h['name'],h['state']) for h in json.load(sys.stdin)]"
```

**Root Cause:**
The 4 platform containers (2 cnodes + 2 dnodes) consume ~75GB RAM at steady state, 
but peak higher during initialization. With insufficient RAM (e.g., 97GB), the Linux 
OOM killer terminates processes during `system_format`, corrupting the initialization.

**Solution:**
This is **unrecoverable** - you must:
1. Stop all containers: `docker stop $(docker ps -aq)`
2. Clean up: `sudo rm -rf /vast/data/* /vast/vman/*`
3. **Increase VM RAM to 112GB+** (128GB recommended)
4. Re-run the installation from scratch

**Prevention:**
Allocate at least 112GB RAM to the VM. The install script will warn if memory is insufficient.

### Registry Connection Failed

**Symptom:**
```
dial tcp: lookup vastdata.registry.local: no such host
```

**Solution:**
```bash
# Verify /etc/hosts entry
grep vastdata.registry.local /etc/hosts

# Add if missing
echo "11.0.0.1 vastdata.registry.local" | sudo tee -a /etc/hosts

# Verify docker config
cat /etc/docker/daemon.json
# Should contain: "insecure-registries": ["vastdata.registry.local:5000"]

# Restart docker
sudo systemctl restart docker
```

### Containers Won't Start

**Diagnosis:**
```bash
# Check docker daemon
sudo systemctl status docker
sudo journalctl -u docker -n 50

# Check disk space
df -h

# Check memory
free -h
```

---

## Reference

### Key File Locations

| Path | Purpose |
|------|---------|
| `/vast/bundles/` | Installation bundles, bootstrap script |
| `/vast/bundles/vast_bootstrap.sh` | Bootstrap script |
| `/vast/deploy/` | Deployment configs (vman.sh, loopback_conf.yml) |
| `/vast/deploy/vman.sh` | VMS management script |
| `/vast/deploy/ssh_key.pem` | SSH key for node communication |
| `/vast/data/` | Per-node container data |
| `/vast/data/11.0.0.1-4100/` | CNode 1 data and scripts |
| `/vast/vman/` | VMS runtime data |
| `/vast/vman/mgmt-vip` | Management VIP file |
| `/file_server/DCACHE` | Local registry cache config |
| `/etc/vast-os-release` | VAST OS version marker |

### Useful Scripts

| Script | Purpose |
|--------|---------|
| `~/vast_proxmox_install.sh` | Complete automated installation |
| `~/start_vms.sh` | Start VMS after reboot |
| `~/clean_traces.sh` | Clean up trace files |
| `/vast/data/11.0.0.1-4100/vms.sh vcli` | Access vCLI |
| `/vast/data/11.0.0.1-4100/attachdocker.sh` | CNode bash shell |

### API Endpoints

| Endpoint | Description |
|----------|-------------|
| `GET /api/clusters/` | List clusters |
| `GET /api/clusters/1/` | Cluster details |
| `GET /api/hosts/` | List hosts (cnodes/dnodes) |
| `GET /api/cnodes/` | List cnodes |
| `GET /api/dnodes/` | List dnodes |
| `GET /api/vippools/` | List VIP pools |
| `GET /api/views/` | List NFS/SMB exports |

**Usage:**
```bash
curl -k https://<ip>/api/clusters/1/ -u admin:123456
```

### vCLI Commands

```
cluster show              # Show cluster status
cnode show                # Show cnodes
dnode show                # Show dnodes
vippool show              # Show VIP pools
view show                 # Show exports
view create --name <n> --path <p> --protocols NFS  # Create export
help                      # Full help
```

---

## Summary

1. **Import OVA** to Proxmox with nested virtualization enabled
2. **Run installer:** `./vast_proxmox_install.sh`
3. **Wait** for cluster to come online (20-40 minutes)
4. **Access VMS:** `https://<ip>` with admin/123456
5. **After reboot:** Run `./start_vms.sh`

---

*Document generated from installation experience on December 29, 2025*
