# First Boot Configuration

**Document:** 04-First-Boot.md  
**Last Updated:** December 30, 2025  

---

## Overview

After creating the VM and booting from the imported VMDK (or fresh Rocky Linux install), this document covers the essential configuration steps:

1. Replace VMware tools with Proxmox guest agent
2. Install Docker CE
3. Configure VirtIO drivers and upgrade SCSI controller
4. Set up NVMe passthrough drives
5. Format and mount data storage

**Important Boot Sequence:**
The OVA was built for VMware ESXi and requires VMware-compatible SCSI controller (LSI 53C895A) for initial boot. After booting, we install VirtIO drivers, rebuild initramfs, shutdown, change to VirtIO SCSI controller in Proxmox, then boot again for optimal performance.

---

## Initial Access

### SSH into the VM

The VAST OVA ships with:
- **Username:** `centos`
- **Default Password:** `centos` (change this!)

```bash
ssh centos@<vm-ip>
```

If DHCP assigned an IP, find it in Proxmox GUI → VM → Summary → IPs (requires guest agent).

### First Steps

```bash
# Change default password
passwd

# Check system info (DO NOT run dnf update - it breaks VAST compatibility)
uname -a
cat /etc/redhat-release
```

> **⚠️ CRITICAL:** Do NOT run `dnf update` or `yum update`. The OVA contains specific kernel and driver versions required for VAST. Updating breaks compatibility.

---

## Step 1: Replace VMware Tools with Guest Agent

The OVA includes VMware tools which don't work on KVM.

### Remove VMware Tools

```bash
# Stop and disable vmtoolsd
sudo systemctl stop vmtoolsd 2>/dev/null
sudo systemctl disable vmtoolsd 2>/dev/null

# Remove if installed as package
sudo dnf remove -y open-vm-tools 2>/dev/null || true
```

### Install QEMU Guest Agent

```bash
# Install guest agent
sudo dnf install -y qemu-guest-agent

# Enable and start
sudo systemctl enable --now qemu-guest-agent

# Verify
sudo systemctl status qemu-guest-agent
```

The guest agent allows Proxmox to:
- Display VM IP addresses
- Execute commands via `qm guest exec`
- Graceful shutdown/freeze for snapshots

---

## Step 2: Install Docker CE

The OVA for VMware has Docker pre-installed, but the Proxmox import may not have it.

### Check if Docker is Installed

```bash
docker --version
```

If not installed:

### Install Docker CE

```bash
# Install prerequisites (required for config-manager)
sudo dnf install -y dnf-plugins-core

# Remove conflicting packages if present
sudo dnf remove -y podman buildah 2>/dev/null || true

# Add Docker repository (official RHEL/Rocky repo)
sudo dnf config-manager --add-repo https://download.docker.com/linux/rhel/docker-ce.repo

# Install Docker
sudo dnf install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin

# Enable and start Docker
sudo systemctl enable --now docker

# Add centos user to docker group
sudo usermod -aG docker centos

# Activate group membership (or log out and back in)
newgrp docker

# Verify
docker ps
docker info
```

> **Note:** We use the RHEL repo path. The CentOS repo also works on Rocky Linux.

### Configure Docker for VAST Registry

VAST uses an internal Docker registry. Configure Docker to trust it:

```bash
# Create daemon.json
sudo mkdir -p /etc/docker
cat << 'EOF' | sudo tee /etc/docker/daemon.json
{
  "insecure-registries": ["vastdata.registry.local:5000"],
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "100m",
    "max-file": "3"
  }
}
EOF

# Restart Docker
sudo systemctl restart docker
```

---

## Step 3: Configure VirtIO Drivers and Upgrade SCSI Controller

The VM initially boots with LSI SCSI controller (VMware compatible). We now install VirtIO drivers and switch to VirtIO SCSI for better performance.

### Install VirtIO Drivers

VirtIO drivers are built into the Linux kernel. We just need to ensure they're in the initramfs:

```bash
# Add drivers to initramfs
echo 'add_drivers+=" virtio_scsi virtio_blk virtio_pci virtio_net "' | \
  sudo tee /etc/dracut.conf.d/virtio.conf

# Rebuild initramfs with VirtIO drivers
sudo dracut -f

# Verify modules are included
lsinitrd | grep virtio
```

### ⚠️ CRITICAL: Verify Before Shutdown

**Do not proceed unless this command shows virtio drivers:**

```bash
sudo lsinitrd | grep -E 'virtio_scsi|virtio_blk|virtio_pci|virtio_net'
```

If this returns **nothing**, DO NOT REBOOT. The VM will fail to boot with VirtIO controller. Run `dracut -f` again and verify.

### Shutdown and Switch SCSI Controller

Only after verification passes, shutdown the VM:

```bash
sudo shutdown -h now
```

**On Proxmox host:**

```bash
# Change SCSI controller to VirtIO
qm set <VMID> --scsihw virtio-scsi-single

# Start the VM
qm start <VMID>
```

**Or via Proxmox GUI:**
1. VM → Hardware → SCSI Controller
2. Change from "LSI 53C895A" to "VirtIO SCSI single"
3. Start VM

### Recovery: If VM Won't Boot After Switch

If the VM fails to boot after switching to VirtIO:

1. **On Proxmox host:** Switch controller back to LSI
   ```bash
   qm set <VMID> --scsihw lsi
   qm start <VMID>
   ```
2. Inside VM: Re-run dracut and verify
3. Retry the switch

### Verify Drivers After Reboot

```bash
lsmod | grep virtio
```

Expected output:
```
virtio_scsi           ...
virtio_blk            ...
virtio_net            ...
virtio_pci            ...
virtio_ring           ...
virtio                ...
```

---

## Step 4: Set Up Passthrough NVMe Drives

If using PCIe passthrough, the NVMe drives should appear as `/dev/nvme0n1` and `/dev/nvme1n1`.

### Verify NVMe Detection

```bash
# Check for NVMe devices
lsblk | grep nvme
nvme list
```

Expected output:
```
nvme0n1     259:0    0   1T  0 disk
nvme1n1     259:1    0   1T  0 disk
```

If not detected, check:
1. PCIe passthrough is configured correctly in Proxmox
2. NVMe driver is loaded: `lsmod | grep nvme`

### Decide on Storage Strategy

The NVMe drives will hold VAST's virtual SSD files (cluster data). The OS disk holds VAST binaries, containers, and configuration.

**Storage Layout:**
- `/` (OS disk): VAST binaries, Docker images, container data, config
- `/vast/drives/` (NVMe): Virtual SSD files for cluster data only

#### Option A: Software RAID (mdadm) - Maximum Performance

Stripe both NVMe drives for maximum throughput:

```bash
# Install mdadm
sudo dnf install -y mdadm

# Create RAID0 stripe
sudo mdadm --create /dev/md0 --level=0 --raid-devices=2 /dev/nvme0n1 /dev/nvme1n1

# Verify
cat /proc/mdstat
```

#### Option B: One NVMe Per D-Box Container (Recommended for Isolation)

Align each NVMe drive to a DNode container for better failure isolation:

```bash
# nvme0n1 → /vast/drives/dbox1 (for DNode-1, port 4300)
# nvme1n1 → /vast/drives/dbox2 (for DNode-2, port 4400)

# We'll format and mount each separately
```

This mirrors how physical VAST deployments assign drives to D-Boxes.

---

## Step 5: Format and Mount Data Storage

VAST's virtual SSD files will live on the NVMe drive(s). The files go in `/vast/drives/`, not `/vast/` (which contains binaries and config on the OS disk).

### Create Partition

JV comments -- Let's implify and just include the md0 raid0 example.  Not options

```bash
# Partition the NVMe (or md0 if using RAID)
sudo parted /dev/md0 mklabel gpt
sudo parted /dev/md0 mkpart primary xfs 0% 100%

```

### Format as XFS

```bash
# For mdadm RAID
sudo mkfs.xfs -f -n ftype=1 -i size=512 /dev/md0
```

### Mount the Filesystem

```bash
# Create mount point for VAST drives (NOT /vast)
sudo mkdir -p /vast/drives

# Option A: Single mount (RAID or single drive)
sudo mount -o noatime,nodiratime /dev/md0 /vast/drives


# Verify
df -h /vast/drives
```

### Add to fstab for Persistence

JV Comment, update blkid discovery.  XFS device got created as /dev/sda3

```bash
# Get the UUID(s)
UUID1=$(blkid /dev/nvme0n1p1 -s UUID -o value)


# Option A: Single mount
echo "UUID=$UUID /vast/drives xfs defaults,noatime,nodiratime 0 0" | sudo tee -a /etc/fstab

# Option B: Separate mounts per D-Box
echo "UUID=$UUID1 /vast/drives/dbox1 xfs defaults,noatime,nodiratime 0 0" | sudo tee -a /etc/fstab
[ -n "$UUID2" ] && echo "UUID=$UUID2 /vast/drives/dbox2 xfs defaults,noatime,nodiratime 0 0" | sudo tee -a /etc/fstab

# Verify
sudo mount -a
df -h /vast/drives
```

### Set Ownership

```bash
# VAST runs as centos user
sudo chown -R centos:centos /vast
```

---

## Step 6: Create VAST Directory Structure

Create the directories VAST expects:

```bash
# Create required directories
sudo mkdir -p /vast/bundles
sudo mkdir -p /vast/deploy
sudo mkdir -p /vast/data
sudo mkdir -p /vast/vman
sudo mkdir -p /vast/drives

# Set ownership
sudo chown -R centos:centos /vast

# Create OS release marker (VAST checks this)
echo '1.1.1' | sudo tee /etc/vast-os-release
sudo chmod 644 /etc/vast-os-release
```

---

## Step 7: Configure Registry Hostname

VAST containers expect a local Docker registry:

```bash
# Add registry hostname to /etc/hosts
echo "11.0.0.1 vastdata.registry.local" | sudo tee -a /etc/hosts

# Create registry cache pointer
sudo mkdir -p /file_server
echo "vastdata.registry.local:5000" | sudo tee /file_server/DCACHE
```

---

## Step 8: Set Up SSH Keys

VAST containers SSH to the host for certain operations:

```bash
# Generate SSH key if not exists
[ ! -f ~/.ssh/id_rsa ] && ssh-keygen -f ~/.ssh/id_rsa -q -N ""

# Add to authorized_keys
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys

# Copy to VAST deploy location
sudo mkdir -p /vast/deploy
sudo cp ~/.ssh/id_rsa /vast/deploy/ssh_key.pem
sudo chown centos:centos /vast/deploy/ssh_key.pem
chmod 600 /vast/deploy/ssh_key.pem

# Test SSH to localhost (should work without password)
ssh -o StrictHostKeyChecking=no localhost "echo SSH works"
```

---

## Step 9: Disable Swap

VAST performs better without swap:

```bash
# Disable swap immediately
sudo swapoff -a

# Remove swap from fstab
sudo sed -i '/swap/d' /etc/fstab

# Verify
free -h
# Should show "Swap: 0B 0B 0B"
```

---

## Step 10: Disable SELinux

VAST requires SELinux disabled:

```bash
# Disable immediately
sudo setenforce 0

# Disable permanently
sudo sed -i 's/SELINUX=enforcing/SELINUX=disabled/' /etc/selinux/config

# Verify
getenforce
# Should show "Permissive" or "Disabled"
```

---

## Verification Checklist

Before proceeding to VAST installation, verify:

```bash
# Check guest agent
sudo systemctl is-active qemu-guest-agent

# Check Docker
docker ps

# Check NVMe/storage
df -h /vast/drives

# Check SSH key
ssh localhost "echo SSH OK"

# Check Docker registry config
cat /etc/docker/daemon.json

# Check VirtIO drivers
lsmod | grep virtio

# Check SELinux
getenforce

# Check swap
free -h | grep Swap
```

### Expected Results

| Check | Expected |
|-------|----------|
| Guest agent | active |
| Docker | Running |
| /vast/drives | Mounted (1-2 TB NVMe) |
| SSH | Works without password |
| VirtIO | Loaded |
| SELinux | Permissive/Disabled |
| Swap | 0B |

---

## Create Post-Config Snapshot

Create a snapshot of this working state:

```bash
# On Proxmox host
qm snapshot <VMID> post-config --description "Configured, ready for VAST"
```

---

## Quick Setup Script

For automation, here's a condensed script:

```bash
#!/bin/bash
# post-boot-config.sh - Run after first boot

set -e

echo "=== Post-Boot Configuration ==="

# VMware tools → Guest agent
sudo systemctl disable vmtoolsd 2>/dev/null || true
sudo dnf install -y qemu-guest-agent
sudo systemctl enable --now qemu-guest-agent

# Docker
if ! command -v docker &>/dev/null; then
    sudo dnf config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
    sudo dnf install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin
fi
sudo systemctl enable --now docker
sudo usermod -aG docker centos

# Docker registry config
sudo mkdir -p /etc/docker
cat << 'EOF' | sudo tee /etc/docker/daemon.json
{"insecure-registries": ["vastdata.registry.local:5000"]}
EOF
sudo systemctl restart docker

# VirtIO drivers
echo 'add_drivers+=" virtio_scsi virtio_blk virtio_pci "' | sudo tee /etc/dracut.conf.d/virtio.conf
sudo dracut -f

# SELinux
sudo setenforce 0
sudo sed -i 's/SELINUX=enforcing/SELINUX=disabled/' /etc/selinux/config

# Swap
sudo swapoff -a
sudo sed -i '/swap/d' /etc/fstab

echo "=== Configuration Complete ==="
echo "Next: Format NVMe drives and mount /vast/drives"
echo "Then: Proceed to 06-Pre-Install-Tweaks.md"
```

---

## Next Steps

1. **Topology Planning:** [05-Topology-Planning.md](05-Topology-Planning.md) - Decide cluster size
2. **Pre-Install Tweaks:** [06-Pre-Install-Tweaks.md](06-Pre-Install-Tweaks.md) - Apply critical workarounds
3. **Installation:** [07-Install-Script-Reference.md](07-Install-Script-Reference.md) - Run the install

---

*Previous: [03-VM-Setup.md](03-VM-Setup.md) | Next: [05-Topology-Planning.md](05-Topology-Planning.md)*



Notes and Gemini conversation --
I'm setting up a drive as raid0 but I can't find the blkid. Help!

  

The blkid starting 9914 is my OS disk I think. I don't see /dev/md0. How do I add it to fstab?

  

  

centos@localhost.localdomain:/home/centos $ sudo parted /dev/md0 mklabel gpt

Warning: The existing disk label on /dev/md0 will be destroyed and all data on

this disk will be lost. Do you want to continue?

Yes/No? yes

Information: You may need to update /etc/fstab.

  

centos@localhost.localdomain:/home/centos $ sudo parted /dev/md0 mkpart primary xfs 0% 100%

Information: You may need to update /etc/fstab.

  

centos@localhost.localdomain:/home/centos $ sudo mkfs.xfs -f -n ftype=1 -i size=512 /dev/md0

centos@localhost.localdomain:/home/centos $ clear

centos@localhost.localdomain:/home/centos $ sudo mkfs.xfs -f -n ftype=1 -i size=512 /dev/md0

log stripe unit (524288 bytes) is too large (maximum is 256KiB)

log stripe unit adjusted to 32KiB

meta-data=/dev/md0               isize=512    agcount=32, agsize=15259776 blks

         =                       sectsz=512   attr=2, projid32bit=1

         =                       crc=1        finobt=1, sparse=1, rmapbt=0

         =                       reflink=1    bigtime=0 inobtcount=0

data     =                       bsize=4096   blocks=488312832, imaxpct=5

         =                       sunit=128    swidth=256 blks

naming   =version 2              bsize=4096   ascii-ci=0, ftype=1

log      =internal log           bsize=4096   blocks=238440, version=2

         =                       sectsz=512   sunit=8 blks, lazy-count=1

realtime =none                   extsz=4096   blocks=0, rtextents=0

Discarding blocks...Done.

centos@localhost.localdomain:/home/centos $ sudo mkdir -p /vast/drives

centos@localhost.localdomain:/home/centos $ sudo mount -o noatime,nodiratime /dev/md0 /vast/drives

centos@localhost.localdomain:/home/centos $ UUID1=$(blkid /dev/md0 -s UUID -o value)

centos@localhost.localdomain:/home/centos $ $UUID1

centos@localhost.localdomain:/home/centos $ blkid /dev/md0

centos@localhost.localdomain:/home/centos $ blkid

/dev/sda3: UUID="9914d65e-64ef-46a7-9c3c-94e2d76279a3" BLOCK_SIZE="512" TYPE="xfs" PARTUUID="74fd0506-03"

centos@localhost.localdomain:/home/centos $ df

Filesystem      1K-blocks     Used  Available Use% Mounted on

devtmpfs         57466024        0   57466024   0% /dev

tmpfs            57482244        0   57482244   0% /dev/shm

tmpfs            57482244     9004   57473240   1% /run

tmpfs            57482244        0   57482244   0% /sys/fs/cgroup

/dev/sda3      1071842284 31812688 1040029596   3% /

/dev/sda1         1038336   252880     785456  25% /boot

tmpfs            11496448        0   11496448   0% /run/user/1000

/dev/md0       1952297568 13646504 1938651064   1% /vast/drives

You successfully formatted and mounted the drive, but `blkid` is likely returning nothing because of a **stale cache** or a conflict between the partition table you created and the filesystem you wrote on top of it.

You ran `mkfs.xfs` directly on `/dev/md0` _after_ creating a partition table. This effectively overwrote the partition table, meaning `/dev/md0` is now a "raw" filesystem (which is fine, but it explains why you don't see partitions).

Here is how to get the UUID and set up your `fstab`.

### 1. Find the UUID (The reliable way)

Since standard `blkid` is failing, use `lsblk` with the filesystem flag. It reads the disk structure live and usually bypasses the stale cache causing your issue.

Run this command:

Bash

```
lsblk -f
```

Look for the row named `md0`. Copy the alphanumeric string under the `UUID` column.

**Alternative (Force `blkid` to probe):** If `lsblk` doesn't show it, force a low-level probe that ignores the cache:

Bash

```
sudo blkid -p /dev/md0
```

### 2. Update `/etc/fstab`

Once you have the UUID (let's assume it is `1234-5678` for this example), you need to add it to your fstab file so it mounts on reboot.

1. Open fstab:
    
    Bash
    
    ```
    sudo nano /etc/fstab
    ```
    
2. Add this line at the bottom (replace `YOUR-UUID-HERE` with the actual ID you copied):
    
    Plaintext
    
    ```
    UUID=YOUR-UUID-HERE  /vast/drives  xfs  noatime,nodiratime  0 0
    ```
    
3. **Critical Step:** Verify your work **before** rebooting. If the fstab is wrong, the server will fail to boot.
    
    Bash
    
    ```
    sudo mount -a
    ```
    
    - If this returns **no output**, you are safe to reboot.
        
    - If it returns an error, check your UUID and syntax immediately.
        

### Why `blkid` failed (Explanation)

In your logs, you ran:

1. `parted /dev/md0 ...` (Created a Partition Table)
    
2. `mkfs.xfs ... /dev/md0` (Created a Filesystem)
    

By running `mkfs` on `/dev/md0` (instead of `/dev/md0p1`), you overwrote the Partition Table headers you just created with XFS headers. `blkid` likely saw "ghost" signatures of the deleted partition table and got confused, refusing to print output to avoid giving you wrong data. The `lsblk -f` or `blkid -p` commands bypass this confusion.

Help! The drive still didn't mount. How do I get these online before I reboot? Give me the step-by-step

  

centos@localhost.localdomain:/home/centos $ lsblkid

zsh: command not found: lsblkid

centos@localhost.localdomain:/home/centos $ clear

centos@localhost.localdomain:/home/centos $ lsblk -f

NAME FSTYPE LABEL              UUID                                 MOUNTPOINT

sda

├─sda1

│    xfs                       6542bc40-c6ae-41b1-85b3-3abb5d48bfe1 /boot

├─sda2

│    swap                      f6fa6613-1edf-462a-9066-33b21e40d246 [SWAP]

└─sda3

     xfs                       9914d65e-64ef-46a7-9c3c-94e2d76279a3 /vast/driv

sr0

nvme1n1

│    linux_ localhost.localdomain:0

│                              a0ceec2a-c724-05f5-a618-27e46f42adc5

└─md0

     xfs                       edd7c7a2-d6e9-4530-aa70-51be9e5282bb /vast/driv

nvme0n1

│    linux_ localhost.localdomain:0

│                              a0ceec2a-c724-05f5-a618-27e46f42adc5

└─md0

     xfs                       edd7c7a2-d6e9-4530-aa70-51be9e5282bb /vast/driv

centos@localhost.localdomain:/home/centos $ sudo blkid -p /dev/md0

/dev/md0: UUID="edd7c7a2-d6e9-4530-aa70-51be9e5282bb" BLOCK_SIZE="512" TYPE="xfs" USAGE="filesystem"

centos@localhost.localdomain:/home/centos $ sudo nano /etc/fstab

centos@localhost.localdomain:/home/centos $ sudo mount -a

centos@localhost.localdomain:/home/centos $ df

Filesystem      1K-blocks     Used  Available Use% Mounted on

devtmpfs         57466024        0   57466024   0% /dev

tmpfs            57482244        0   57482244   0% /dev/shm

tmpfs            57482244     9008   57473236   1% /run

tmpfs            57482244        0   57482244   0% /sys/fs/cgroup

/dev/sda3      1071842284 31812720 1040029564   3% /

/dev/sda1         1038336   252880     785456  25% /boot

tmpfs            11496448        0   11496448   0% /run/user/1000

centos@localhost.localdomain:/home/centos $

centos@localhost.localdomain:/home/centos $

centos@localhost.localdomain:/home/centos $ mount -a

mount: only root can use "--all" option

centos@localhost.localdomain:/home/centos $ sudo mount -a

centos@localhost.localdomain:/home/centos $ cat /etc/fstab

  

#

# /etc/fstab

# Created by anaconda on Tue Jun 24 10:43:16 2025

#

# Accessible filesystems, by reference, are maintained under '/dev/disk/'.

# See man pages fstab(5), findfs(8), mount(8) and/or blkid(8) for more info.

#

# After editing this file, run 'systemctl daemon-reload' to update systemd

# units generated from this file.

#

UUID=9914d65e-64ef-46a7-9c3c-94e2d76279a3 /                       xfs     defaults        0 0

UUID=6542bc40-c6ae-41b1-85b3-3abb5d48bfe1 /boot                   xfs     defaults        0 0

UUID=f6fa6613-1edf-462a-9066-33b21e40d246 none                    swap    defaults        0 0

UUID=edd7c7a2-d6e9-4530-aa70-51be9e5282bb /vast/drives  xfs  noatime,nodiratime  0 0

centos@localhost.localdomain:/home/centos $

The drive is likely not mounting because `systemd` (which manages mounts on CentOS) hasn't been notified of your changes to `/etc/fstab`.

You edited the file, but as the comment inside `fstab` warns: **"After editing this file, run 'systemctl daemon-reload' to update systemd units."**

Here are the commands to fix this immediately and verify it is online.

### Step-by-Step Fix

**1. Refresh the system configuration** Tell systemd to read your new `fstab` entry.

Bash

```
sudo systemctl daemon-reload
```

**2. Mount the specific drive** Instead of `mount -a` (which sometimes skips things it thinks are already handled), tell it to mount this specific mount point using the config you just wrote.

Bash

```
sudo mount /vast/drives
```

**3. Verify it is online** Check specifically for the mount point.

Bash

```
df -h /vast/drives
```

_(You should see `/dev/md0` listed with roughly 1.8TB or 1.9TB of space)._

### Troubleshooting

If the mount command in Step 2 fails:

- **"Mount point does not exist":** Run `sudo mkdir -p /vast/drives` and try mounting again.
    
- **"Wrong fs type, bad option...":** Run `dmesg | tail` to see the specific error log from the kernel.
    

Woo.. that worked. Now give me some good FIO tests to verify the performance of /vast/drives across various VAST centric scenarios

Since VAST Data architecture (Universal Storage) is designed to serve massive throughput for AI/HPC workloads (GPU feeding) and high IOPS for metadata, we need to test both extremes. We want to prove that your local NVMe RAID0 can mimic the "Tier 1 performance" that VAST promises.

First, ensure `fio` is installed on your Rocky Linux VM:

Bash

```
sudo dnf install -y fio
```

Here are the four key scenarios to run.

### 1. The "Firehose" Ingest (Sequential Write)

**Scenario:** Simulates high-speed data ingest or writing AI checkpoints. VAST systems ingest data into a write buffer (Storage Class Memory) before moving it to flash. We want to see if your RAID0 can swallow data as fast as the network would theoretically send it.

- **Metric to watch:** BW (Bandwidth) - You want to see GB/s here.
    

Bash

```
fio --name=vast_ingest \
    --directory=/vast/drives \
    --ioengine=libaio \
    --direct=1 \
    --rw=write \
    --bs=1M \
    --size=4G \
    --numjobs=4 \
    --iodepth=32 \
    --group_reporting \
    --runtime=60 \
    --time_based
```

- `--direct=1`: Bypasses the OS RAM cache to test the raw metal.
    
- `--bs=1M`: Large block size mimics the large stripes VAST uses for data.
    

### 2. The "GPU Feeder" (Sequential Read)

**Scenario:** Simulates training a model where GPUs are hungry for massive datasets. This is the "hero number" for VAST deployments feeding NVIDIA SuperPODs.

- **Metric to watch:** BW (Bandwidth). With 2x Gen4/5 drives in RAID0, this should be huge.
    

Bash

```
fio --name=vast_training \
    --directory=/vast/drives \
    --ioengine=libaio \
    --direct=1 \
    --rw=read \
    --bs=1M \
    --size=4G \
    --numjobs=4 \
    --iodepth=32 \
    --group_reporting \
    --runtime=60 \
    --time_based
```

### 3. The "Metadata Storm" (4K Random Read)

**Scenario:** VAST disaggregates metadata from data. While metadata usually lives on 3D XPoint/SCM in real VAST clusters, your RAID0 needs to handle the "file walk" or "ls -R" on millions of files.

- **Metric to watch:** IOPS (Input/Output Operations Per Second) and Latency (lat).
    

Bash

```
fio --name=vast_metadata \
    --directory=/vast/drives \
    --ioengine=libaio \
    --direct=1 \
    --rw=randread \
    --bs=4k \
    --size=1G \
    --numjobs=8 \
    --iodepth=64 \
    --group_reporting \
    --runtime=60 \
    --time_based
```

- _Note:_ We increased `numjobs` and `iodepth` here because NVMe drives thrive on parallelism for small blocks.
    

### 4. The "Real World" (70/30 Mixed)

**Scenario:** A general purpose workload. While VAST handles read/write distinctively, this validates the controller's ability to context switch between reading and writing without choking.

Bash

```
fio --name=vast_mixed \
    --directory=/vast/drives \
    --ioengine=libaio \
    --direct=1 \
    --rw=randrw \
    --rwmixread=70 \
    --bs=128k \
    --size=4G \
    --numjobs=4 \
    --iodepth=32 \
    --group_reporting \
    --runtime=60 \
    --time_based
```

### 🧹 Cleanup

When you are done, FIO usually cleans up, but if you interrupted the tests, you might have large files left over. Run this to reclaim space:

Bash

```
rm /vast/drives/vast_*
```

What should we set the default owner and permissions to be for the /vast/drives folder?

  

centos@localhost.localdomain:/home/centos $ fio --name=vast_ingest \

    --directory=/vast/drives \

    --ioengine=libaio \

    --direct=1 \

    --rw=write \

    --bs=1M \

    --size=4G \

    --numjobs=4 \

    --iodepth=32 \

    --group_reporting \

    --runtime=60 \

    --time_based

vast_ingest: (g=0): rw=write, bs=(R) 1024KiB-1024KiB, (W) 1024KiB-1024KiB, (T) 1024KiB-1024KiB, ioengine=libaio, iodepth=32

...

fio-3.19

Starting 4 processes

vast_ingest: Laying out IO file (1 file / 4096MiB)

fio: pid=0, err=13/file:filesetup.c:174, func=open, error=Permission denied

vast_ingest: Laying out IO file (1 file / 4096MiB)

fio: pid=0, err=13/file:filesetup.c:174, func=open, error=Permission denied

vast_ingest: Laying out IO file (1 file / 4096MiB)

fio: pid=0, err=13/file:filesetup.c:174, func=open, error=Permission denied

vast_ingest: Laying out IO file (1 file / 4096MiB)

fio: pid=0, err=13/file:filesetup.c:174, func=open, error=Permission denied

  

  

Run status group 0 (all jobs):

To fix the `Permission denied` error, you need to grant your current user (`centos`) ownership of the new mount point. By default, `mount` sets the owner to `root`, so your user cannot write the test files.

### The Fix

Run these two commands to transfer ownership to the `centos` user and ensure the permissions are correct for a data drive:

Bash

```
# 1. Give the 'centos' user ownership of the directory
sudo chown -R centos:centos /vast/drives

# 2. Set permissions (Owner=Read/Write/Exec, Others=Read/Exec)
sudo chmod 755 /vast/drives
```

### Why these settings?

- **Owner (`centos:centos`):** Since you are running the FIO tests and managing the VM as the `centos` user, this gives you full control without needing `sudo` for every file operation.
    
- **Permissions (`755`):** This is the standard setting for data directories. It allows you (the owner) to do anything, while allowing others to read the data (useful if you later share this via NFS to other VMs).
    

Once you run those commands, **re-run your FIO command immediately.** It should work perfectly.

Here is the raw dump of all the tests. Review the results in context and characterize the findings against workload expectations and the hardware (dual samsung 990 plus 1TiB drives in RAID0).

  

centos@localhost.localdomain:/home/centos $ fio --name=vast_ingest \

    --directory=/vast/drives \

    --ioengine=libaio \

    --direct=1 \

    --rw=write \

    --bs=1M \

    --size=4G \

    --numjobs=4 \

    --iodepth=32 \

    --group_reporting \

    --runtime=60 \

    --time_based

vast_ingest: (g=0): rw=write, bs=(R) 1024KiB-1024KiB, (W) 1024KiB-1024KiB, (T) 1024KiB-1024KiB, ioengine=libaio, iodepth=32

...

fio-3.19

Starting 4 processes

vast_ingest: Laying out IO file (1 file / 4096MiB)

fio: pid=0, err=13/file:filesetup.c:174, func=open, error=Permission denied

vast_ingest: Laying out IO file (1 file / 4096MiB)

fio: pid=0, err=13/file:filesetup.c:174, func=open, error=Permission denied

vast_ingest: Laying out IO file (1 file / 4096MiB)

fio: pid=0, err=13/file:filesetup.c:174, func=open, error=Permission denied

vast_ingest: Laying out IO file (1 file / 4096MiB)

fio: pid=0, err=13/file:filesetup.c:174, func=open, error=Permission denied

  

  

Run status group 0 (all jobs):

centos@localhost.localdomain:/home/centos $

centos@localhost.localdomain:/home/centos $

centos@localhost.localdomain:/home/centos $ # 1. Give the 'centos' user ownership of the directory

sudo chown -R centos:centos /vast/drives

  

# 2. Set permissions (Owner=Read/Write/Exec, Others=Read/Exec)

sudo chmod 755 /vast/drives

centos@localhost.localdomain:/home/centos $ fio --name=vast_ingest \

    --directory=/vast/drives \

    --ioengine=libaio \

    --direct=1 \

    --rw=write \

    --bs=1M \

    --size=4G \

    --numjobs=4 \

    --iodepth=32 \

    --group_reporting \

    --runtime=60 \

    --time_based

vast_ingest: (g=0): rw=write, bs=(R) 1024KiB-1024KiB, (W) 1024KiB-1024KiB, (T) 1024KiB-1024KiB, ioengine=libaio, iodepth=32

...

fio-3.19

Starting 4 processes

vast_ingest: Laying out IO file (1 file / 4096MiB)

vast_ingest: Laying out IO file (1 file / 4096MiB)

vast_ingest: Laying out IO file (1 file / 4096MiB)

vast_ingest: Laying out IO file (1 file / 4096MiB)

Jobs: 4 (f=4): [W(4)][100.0%][w=5653MiB/s][w=5653 IOPS][eta 00m:00s]

vast_ingest: (groupid=0, jobs=4): err= 0: pid=7269: Thu Jan  1 18:26:41 2026

  write: IOPS=5636, BW=5636MiB/s (5910MB/s)(330GiB/60022msec); 0 zone resets

    slat (usec): min=24, max=466, avg=46.19, stdev= 9.21

    clat (usec): min=8238, max=51069, avg=22661.35, stdev=3624.76

     lat (usec): min=8291, max=51111, avg=22707.70, stdev=3624.95

    clat percentiles (usec):

     |  1.00th=[21365],  5.00th=[21365], 10.00th=[21365], 20.00th=[21365],

     | 30.00th=[21365], 40.00th=[21365], 50.00th=[21365], 60.00th=[21365],

     | 70.00th=[21365], 80.00th=[21365], 90.00th=[29492], 95.00th=[33424],

     | 99.00th=[33424], 99.50th=[33424], 99.90th=[40633], 99.95th=[42730],

     | 99.99th=[45351]

   bw (  MiB/s): min= 5440, max= 5744, per=100.00%, avg=5645.73, stdev=14.54, samples=476

   iops        : min= 5439, max= 5744, avg=5645.72, stdev=14.55, samples=476

  lat (msec)   : 10=0.01%, 20=0.06%, 50=99.92%, 100=0.01%

  cpu          : usr=4.06%, sys=2.91%, ctx=338286, majf=0, minf=45

  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=100.0%, >=64=0.0%

     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%

     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.1%, 64=0.0%, >=64=0.0%

     issued rwts: total=0,338293,0,0 short=0,0,0,0 dropped=0,0,0,0

     latency   : target=0, window=0, percentile=100.00%, depth=32

  

Run status group 0 (all jobs):

  WRITE: bw=5636MiB/s (5910MB/s), 5636MiB/s-5636MiB/s (5910MB/s-5910MB/s), io=330GiB (355GB), run=60022-60022msec

  

Disk stats (read/write):

    md0: ios=0/675889, merge=0/0, ticks=0/9713647, in_queue=9713647, util=99.94%, aggrios=0/338301, aggrmerge=0/1, aggrticks=0/4866605, aggrin_queue=4866606, aggrutil=99.90%

  nvme0n1: ios=0/338304, merge=0/3, ticks=0/2069914, in_queue=2069914, util=98.94%

  nvme1n1: ios=0/338298, merge=0/0, ticks=0/7663297, in_queue=7663298, util=99.90%

centos@localhost.localdomain:/home/centos $ fio --name=vast_training \

    --directory=/vast/drives \

    --ioengine=libaio \

    --direct=1 \

    --rw=read \

    --bs=1M \

    --size=4G \

    --numjobs=4 \

    --iodepth=32 \

    --group_reporting \

    --runtime=60 \

    --time_based

vast_training: (g=0): rw=read, bs=(R) 1024KiB-1024KiB, (W) 1024KiB-1024KiB, (T) 1024KiB-1024KiB, ioengine=libaio, iodepth=32

...

fio-3.19

Starting 4 processes

vast_training: Laying out IO file (1 file / 4096MiB)

vast_training: Laying out IO file (1 file / 4096MiB)

vast_training: Laying out IO file (1 file / 4096MiB)

vast_training: Laying out IO file (1 file / 4096MiB)

Jobs: 4 (f=0): [f(4)][100.0%][r=6937MiB/s][r=6937 IOPS][eta 00m:00s]

vast_training: (groupid=0, jobs=4): err= 0: pid=7284: Thu Jan  1 18:27:55 2026

  read: IOPS=7007, BW=7008MiB/s (7348MB/s)(411GiB/60019msec)

    slat (usec): min=12, max=1370, avg=16.35, stdev= 8.36

    clat (usec): min=7289, max=35646, avg=18245.21, stdev=272.58

     lat (usec): min=7774, max=35662, avg=18261.68, stdev=269.87

    clat percentiles (usec):

     |  1.00th=[18220],  5.00th=[18220], 10.00th=[18220], 20.00th=[18220],

     | 30.00th=[18220], 40.00th=[18220], 50.00th=[18220], 60.00th=[18220],

     | 70.00th=[18220], 80.00th=[18220], 90.00th=[18220], 95.00th=[18220],

     | 99.00th=[18220], 99.50th=[18220], 99.90th=[18220], 99.95th=[18482],

     | 99.99th=[29492]

   bw (  MiB/s): min= 6937, max= 7088, per=100.00%, avg=7018.42, stdev= 9.69, samples=476

   iops        : min= 6936, max= 7088, avg=7018.40, stdev= 9.71, samples=476

  lat (msec)   : 10=0.03%, 20=99.93%, 50=0.04%

  cpu          : usr=0.94%, sys=3.68%, ctx=420580, majf=0, minf=129

  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=100.0%, >=64=0.0%

     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%

     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.1%, 64=0.0%, >=64=0.0%

     issued rwts: total=420609,0,0,0 short=0,0,0,0 dropped=0,0,0,0

     latency   : target=0, window=0, percentile=100.00%, depth=32

  

Run status group 0 (all jobs):

   READ: bw=7008MiB/s (7348MB/s), 7008MiB/s-7008MiB/s (7348MB/s-7348MB/s), io=411GiB (441GB), run=60019-60019msec

  

Disk stats (read/write):

    md0: ios=838114/9, merge=0/0, ticks=10279537/2, in_queue=10279539, util=99.97%, aggrios=420609/4, aggrmerge=0/1, aggrticks=5157620/12, aggrin_queue=5157631, aggrutil=100.00%

  nvme0n1: ios=420609/6, merge=0/3, ticks=2642891/4, in_queue=2642894, util=100.00%

  nvme1n1: ios=420609/2, merge=0/0, ticks=7672350/20, in_queue=7672369, util=99.93%

centos@localhost.localdomain:/home/centos $ fio --name=vast_metadata \

>     --directory=/vast/drives \

>     --ioengine=libaio \

>     --direct=1 \

>     --rw=randread \

>     --bs=4k \

>     --size=1G \

>     --numjobs=8 \

>     --iodepth=64 \

>     --group_reporting \

>     --runtime=60 \

>     --time_based

vast_metadata: (g=0): rw=randread, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=64

...

fio-3.19

Starting 8 processes

vast_metadata: Laying out IO file (1 file / 1024MiB)

vast_metadata: Laying out IO file (1 file / 1024MiB)

vast_metadata: Laying out IO file (1 file / 1024MiB)

vast_metadata: Laying out IO file (1 file / 1024MiB)

vast_metadata: Laying out IO file (1 file / 1024MiB)

vast_metadata: Laying out IO file (1 file / 1024MiB)

vast_metadata: Laying out IO file (1 file / 1024MiB)

vast_metadata: Laying out IO file (1 file / 1024MiB)

Jobs: 8 (f=8): [r(8)][100.0%][r=3923MiB/s][r=1004k IOPS][eta 00m:00s]

vast_metadata: (groupid=0, jobs=8): err= 0: pid=7327: Thu Jan  1 18:46:17 2026

  read: IOPS=979k, BW=3826MiB/s (4012MB/s)(224GiB/60002msec)

    slat (nsec): min=1903, max=1147.6k, avg=6039.40, stdev=7726.58

    clat (usec): min=58, max=4914, avg=515.47, stdev=120.52

     lat (usec): min=66, max=4919, avg=521.69, stdev=121.92

    clat percentiles (usec):

     |  1.00th=[  388],  5.00th=[  408], 10.00th=[  416], 20.00th=[  433],

     | 30.00th=[  445], 40.00th=[  457], 50.00th=[  469], 60.00th=[  502],

     | 70.00th=[  537], 80.00th=[  578], 90.00th=[  660], 95.00th=[  816],

     | 99.00th=[  938], 99.50th=[  971], 99.90th=[ 1037], 99.95th=[ 1106],

     | 99.99th=[ 1336]

   bw (  MiB/s): min= 3274, max= 4465, per=100.00%, avg=3831.15, stdev=40.36, samples=952

   iops        : min=838208, max=1143262, avg=980773.46, stdev=10333.36, samples=952

  lat (usec)   : 100=0.01%, 250=0.01%, 500=60.05%, 750=33.47%, 1000=6.26%

  lat (msec)   : 2=0.21%, 4=0.01%, 10=0.01%

  cpu          : usr=24.36%, sys=75.60%, ctx=3304, majf=2, minf=621

  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=100.0%

     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%

     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.1%, >=64=0.0%

     issued rwts: total=58766651,0,0,0 short=0,0,0,0 dropped=0,0,0,0

     latency   : target=0, window=0, percentile=100.00%, depth=64

  

Run status group 0 (all jobs):

   READ: bw=3826MiB/s (4012MB/s), 3826MiB/s-3826MiB/s (4012MB/s-4012MB/s), io=224GiB (241GB), run=60002-60002msec

  

Disk stats (read/write):

    md0: ios=58649626/10, merge=0/0, ticks=3683662/2, in_queue=3683664, util=99.98%, aggrios=29383325/4, aggrmerge=0/1, aggrticks=1927212/3, aggrin_queue=1927215, aggrutil=99.92%

  nvme0n1: ios=29383028/6, merge=0/3, ticks=1960425/2, in_queue=1960427, util=99.92%

  nvme1n1: ios=29383623/3, merge=0/0, ticks=1894000/4, in_queue=1894003, util=99.92%

centos@localhost.localdomain:/home/centos $ fio --name=vast_mixed \

    --directory=/vast/drives \

    --ioengine=libaio \

    --direct=1 \

    --rw=randrw \

    --rwmixread=70 \

    --bs=128k \

    --size=4G \

    --numjobs=4 \

    --iodepth=32 \

    --group_reporting \

    --runtime=60 \

    --time_based

vast_mixed: (g=0): rw=randrw, bs=(R) 128KiB-128KiB, (W) 128KiB-128KiB, (T) 128KiB-128KiB, ioengine=libaio, iodepth=32

...

fio-3.19

Starting 4 processes

vast_mixed: Laying out IO file (1 file / 4096MiB)

vast_mixed: Laying out IO file (1 file / 4096MiB)

vast_mixed: Laying out IO file (1 file / 4096MiB)

vast_mixed: Laying out IO file (1 file / 4096MiB)

Jobs: 4 (f=4): [m(4)][4.9%][r=4636MiB/s,w=1987MiB/s][r=37.1k,w=15.9k IOPS][etaJobs: 4 (f=4): [m(4)][6.6%][r=4741MiB/s,w=2042MiB/s][r=37.9k,w=16.3k IOPS][etaJobs: 4 (f=4): [m(4)][8.2%][r=4678MiB/s,w=2014MiB/s][r=37.4k,w=16.1k IOPS][etaJobs: 4 (f=4): [m(4)][9.8%][r=4712MiB/s,w=2006MiB/s][r=37.7k,w=16.0k IOPS][etaJobs: 4 (f=4): [m(4)][11.5%][r=4802MiB/s,w=2038MiB/s][r=38.4k,w=16.3k IOPS][etJobs: 4 (f=4): [m(4)][13.1%][r=4723MiB/s,w=2016MiB/s][r=37.8k,w=16.1k IOPS][etJobs: 4 (f=4): [m(4)][14.8%][r=4751MiB/s,w=2072MiB/s][r=38.0k,w=16.6k IOPS][etJobs: 4 (f=4): [m(4)][16.4%][r=4597MiB/s,w=1992MiB/s][r=36.8k,w=15.9k IOPS][etJobs: 4 (f=4): [m(4)][18.0%][r=4885MiB/s,w=2088MiB/s][r=39.1k,w=16.7k IOPS][etJobs: 4 (f=4): [m(4)][19.7%][r=4810MiB/s,w=2048MiB/s][r=38.5k,w=16.4k IOPS][etJobs: 4 (f=4): [m(4)][21.3%][r=4777MiB/s,w=2076MiB/s][r=38.2k,w=16.6k IOPS][etJobs: 4 (f=4): [m(4)][23.3%][r=4845MiB/s,w=2065MiB/s][r=38.8k,w=16.5k IOPS][etJobs: 4 (f=4): [m(4)][25.0%][r=4696MiB/s,w=1993MiB/s][r=37.6k,w=15.9k IOPS][etJobs: 4 (f=4): [m(4)][26.7%][r=4927MiB/s,w=2134MiB/s][r=39.4k,w=17.1k IOPS][etJobs: 4 (f=4): [m(4)][28.3%][r=4754MiB/s,w=2040MiB/s][r=38.0k,w=16.3k IOPS][etJobs: 4 (f=4): [m(4)][30.0%][r=4834MiB/s,w=2110MiB/s][r=38.7k,w=16.9k IOPS][etJobs: 4 (f=4): [m(4)][31.7%][r=4733MiB/s,w=2035MiB/s][r=37.9k,w=16.3k IOPS][etJobs: 4 (f=4): [m(4)][33.3%][r=4765MiB/s,w=2060MiB/s][r=38.1k,w=16.5k IOPS][etJobs: 4 (f=4): [m(4)][35.0%][r=4869MiB/s,w=2072MiB/s][r=38.0k,w=16.6k IOPS][etJobs: 4 (f=4): [m(4)][36.7%][r=4752MiB/s,w=2046MiB/s][r=38.0k,w=16.4k IOPS][etJobs: 4 (f=4): [m(4)][38.3%][r=4778MiB/s,w=2081MiB/s][r=38.2k,w=16.6k IOPS][etJobs: 4 (f=4): [m(4)][40.0%][r=4843MiB/s,w=2100MiB/s][r=38.7k,w=16.8k IOPS][etJobs: 4 (f=4): [m(4)][41.7%][r=4789MiB/s,w=2048MiB/s][r=38.3k,w=16.4k IOPS][etJobs: 4 (f=4): [m(4)][44.1%][r=4767MiB/s,w=2057MiB/s][r=38.1k,w=16.5k IOPS][etJobs: 4 (f=4): [m(4)][45.0%][r=4828MiB/s,w=2081MiB/s][r=38.6k,w=16.6k IOPS][etJobs: 4 (f=4): [m(4)][46.7%][r=4725MiB/s,w=2043MiB/s][r=37.8k,w=16.3k IOPS][etJobs: 4 (f=4): [m(4)][48.3%][r=4891MiB/s,w=2107MiB/s][r=39.1k,w=16.9k IOPS][etJobs: 4 (f=4): [m(4)][50.0%][r=4652MiB/s,w=2007MiB/s][r=37.2k,w=16.1k IOPS][etJobs: 4 (f=4): [m(4)][52.5%][r=4911MiB/s,w=2105MiB/s][r=39.3k,w=16.8k IOPS][etJobs: 4 (f=4): [m(4)][53.3%][r=4687MiB/s,w=2016MiB/s][r=37.5k,w=16.1k IOPS][etJobs: 4 (f=4): [m(4)][55.0%][r=4848MiB/s,w=2072MiB/s][r=38.8k,w=16.6k IOPS][etJobs: 4 (f=4): [m(4)][56.7%][r=4753MiB/s,w=2045MiB/s][r=38.0k,w=16.4k IOPS][etJobs: 4 (f=4): [m(4)][58.3%][r=4705MiB/s,w=2019MiB/s][r=37.6k,w=16.1k IOPS][etJobs: 4 (f=4): [m(4)][60.0%][r=4854MiB/s,w=2087MiB/s][r=38.8k,w=16.7k IOPS][etJobs: 4 (f=4): [m(4)][62.7%][r=4704MiB/s,w=2044MiB/s][r=37.6k,w=16.4k IOPS][etJobs: 4 (f=4): [m(4)][63.3%][r=4890MiB/s,w=2073MiB/s][r=39.1k,w=16.6k IOPS][etJobs: 4 (f=4): [m(4)][66.1%][r=4680MiB/s,w=2021MiB/s][r=37.4k,w=16.2k IOPS][etJobs: 4 (f=4): [m(4)][66.7%][r=4639MiB/s,w=2003MiB/s][r=37.1k,w=16.0k IOPS][etJobs: 4 (f=4): [m(4)][68.3%][r=4782MiB/s,w=2042MiB/s][r=38.3k,w=16.3k IOPS][etJobs: 4 (f=4): [m(4)][70.0%][r=4732MiB/s,w=2028MiB/s][r=37.9k,w=16.2k IOPS][etJobs: 4 (f=4): [m(4)][71.7%][r=4759MiB/s,w=2026MiB/s][r=38.1k,w=16.2k IOPS][etJobs: 4 (f=4): [m(4)][73.3%][r=4716MiB/s,w=2020MiB/s][r=37.7k,w=16.2k IOPS][etJobs: 4 (f=4): [m(4)][75.0%][r=4685MiB/s,w=2018MiB/s][r=37.5k,w=16.1k IOPS][etJobs: 4 (f=4): [m(4)][76.7%][r=4812MiB/s,w=2041MiB/s][r=38.5k,w=16.3k IOPS][etJobs: 4 (f=4): [m(4)][78.3%][r=4758MiB/s,w=2039MiB/s][r=38.1k,w=16.3k IOPS][etJobs: 4 (f=4): [m(4)][80.0%][r=4714MiB/s,w=2032MiB/s][r=37.7k,w=16.3k IOPS][etJobs: 4 (f=4): [m(4)][81.7%][r=4727MiB/s,w=2041MiB/s][r=37.8k,w=16.3k IOPS][etJobs: 4 (f=4): [m(4)][83.3%][r=4612MiB/s,w=1982MiB/s][r=36.9k,w=15.9k IOPS][etJobs: 4 (f=4): [m(4)][85.0%][r=4822MiB/s,w=2027MiB/s][r=38.6k,w=16.2k IOPS][etJobs: 4 (f=4): [m(4)][88.1%][r=4759MiB/s,w=2010MiB/s][r=38.1k,w=16.1k IOPS][etJobs: 4 (f=4): [m(4)][88.3%][r=4759MiB/s,w=2056MiB/s][r=38.1k,w=16.4k IOPS][etJobs: 4 (f=4): [m(4)][90.0%][r=4639MiB/s,w=2012MiB/s][r=37.1k,w=16.1k IOPS][etJobs: 4 (f=4): [m(4)][91.7%][r=4750MiB/s,w=2033MiB/s][r=38.0k,w=16.3k IOPS][etJobs: 4 (f=4): [m(4)][93.3%][r=4748MiB/s,w=2016MiB/s][r=37.0k,w=16.1k IOPS][etJobs: 4 (f=4): [m(4)][95.0%][r=4681MiB/s,w=2005MiB/s][r=37.5k,w=16.0k IOPS][etJobs: 4 (f=4): [m(4)][96.7%][r=4737MiB/s,w=2032MiB/s][r=37.9k,w=16.3k IOPS][etJobs: 4 (f=4): [m(4)][98.3%][r=4657MiB/s,w=2015MiB/s][r=37.3k,w=16.1k IOPS][etJobs: 4 (f=4): [m(4)][100.0%][r=4806MiB/s,w=2057MiB/s][r=38.4k,w=16.5k IOPS][eta 00m:00s]

vast_mixed: (groupid=0, jobs=4): err= 0: pid=7347: Thu Jan  1 18:47:49 2026

  read: IOPS=38.0k, BW=4751MiB/s (4982MB/s)(278GiB/60005msec)

    slat (usec): min=3, max=249, avg= 7.00, stdev= 2.76

    clat (usec): min=90, max=27061, avg=3263.53, stdev=2840.17

     lat (usec): min=95, max=27068, avg=3270.64, stdev=2840.24

    clat percentiles (usec):

     |  1.00th=[  120],  5.00th=[  176], 10.00th=[  229], 20.00th=[  367],

     | 30.00th=[  906], 40.00th=[ 1942], 50.00th=[ 3064], 60.00th=[ 4146],

     | 70.00th=[ 5014], 80.00th=[ 5538], 90.00th=[ 5997], 95.00th=[ 6587],

     | 99.00th=[13304], 99.50th=[15533], 99.90th=[20579], 99.95th=[21890],

     | 99.99th=[24249]

   bw (  MiB/s): min= 4445, max= 5144, per=100.00%, avg=4760.49, stdev=33.01, samples=476

   iops        : min=35560, max=41156, avg=38083.92, stdev=264.04, samples=476

  write: IOPS=16.3k, BW=2041MiB/s (2141MB/s)(120GiB/60005msec); 0 zone resets

    slat (usec): min=3, max=886, avg=10.69, stdev= 3.99

    clat (usec): min=39, max=16254, avg=211.06, stdev=653.16

     lat (usec): min=60, max=16264, avg=221.87, stdev=653.17

    clat percentiles (usec):

     |  1.00th=[   62],  5.00th=[   65], 10.00th=[   68], 20.00th=[   71],

     | 30.00th=[   74], 40.00th=[   79], 50.00th=[   88], 60.00th=[  100],

     | 70.00th=[  116], 80.00th=[  149], 90.00th=[  253], 95.00th=[  416],

     | 99.00th=[ 3589], 99.50th=[ 5080], 99.90th=[ 8848], 99.95th=[ 9765],

     | 99.99th=[11731]

   bw (  MiB/s): min= 1868, max= 2254, per=100.00%, avg=2045.12, stdev=18.03, samples=476

   iops        : min=14950, max=18036, avg=16360.91, stdev=144.23, samples=476

  lat (usec)   : 50=0.01%, 100=18.03%, 250=17.42%, 500=10.38%, 750=2.95%

  lat (usec)   : 1000=2.14%

  lat (msec)   : 2=7.00%, 4=12.84%, 10=27.66%, 20=1.48%, 50=0.10%

  cpu          : usr=5.80%, sys=11.99%, ctx=2463298, majf=0, minf=71

  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=100.0%, >=64=0.0%

     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%

     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.1%, 64=0.0%, >=64=0.0%

     issued rwts: total=2280781,979937,0,0 short=0,0,0,0 dropped=0,0,0,0

     latency   : target=0, window=0, percentile=100.00%, depth=32

  

Run status group 0 (all jobs):

   READ: bw=4751MiB/s (4982MB/s), 4751MiB/s-4751MiB/s (4982MB/s-4982MB/s), io=278GiB (299GB), run=60005-60005msec

  WRITE: bw=2041MiB/s (2141MB/s), 2041MiB/s-2041MiB/s (2141MB/s-2141MB/s), io=120GiB (128GB), run=60005-60005msec

  

Disk stats (read/write):

    md0: ios=2274487/977196, merge=0/0, ticks=7390217/192571, in_queue=7582788, util=99.98%, aggrios=1140390/489977, aggrmerge=0/1, aggrticks=3713412/98502, aggrin_queue=3811914, aggrutil=97.33%

  nvme0n1: ios=1141223/489259, merge=0/3, ticks=3475885/104059, in_queue=3579944, util=96.67%

  nvme1n1: ios=1139558/490695, merge=0/0, ticks=3950939/92946, in_queue=4043884, util=97.33%

These results are fascinating. You have successfully achieved "Enterprise Class" IOPS, but we have uncovered a massive **architectural bottleneck** in the bandwidth.

Here is the executive summary of your RAID0 performance against the hardware capabilities of dual Samsung 990 EVO Plus drives.

### 📊 Executive Summary

- **IOPS (Metadata):** 🚀 **Hero Status.** You hit **980,000 IOPS**. This is effectively 1 Million IOPS, saturating the rated spec of the drives. Your metadata performance is Tier-1 capable.
    
- **Throughput (Bandwidth):** 🚧 **Capped.** You are hitting a hard "Invisible Wall" at roughly **7.3 GB/s** (Read) and **5.9 GB/s** (Write).
    
    - _Theoretical Max:_ ~14 GB/s (Read) / ~12 GB/s (Write).
        
    - _Actual Max:_ ~7.3 GB/s.
        
- **Verdict:** Your storage is **CPU/Bus Bound**, not Disk Bound. You are getting the speed of exactly _one_ Gen4 NVMe drive, despite having two in RAID0.
    

---

### 1. The "Firehose" Ingest (Sequential Write)

- **Result:** `5.9 GB/s` (5,636 MiB/s)
    
- **Latency:** ~22ms (High)
    
- **Hardware Expectation:** ~12 GB/s
    
- **Analysis:** You are achieving ~6 GB/s, which is enough to saturate a **40GbE or 50GbE network link**. While this is impressively fast for a home lab, it is only about 50% of what these two drives can theoretically do in RAID0.
    
    - _Note:_ The high latency (22ms) and 99.9% utilization suggest the drives are queuing hard, likely waiting on the system bus to accept the data.
        

### 2. The "GPU Feeder" (Sequential Read)

- **Result:** `7.3 GB/s` (7,008 MiB/s)
    
- **Hardware Expectation:** ~14.5 GB/s
    
- **Analysis:** This result is the "Smoking Gun." The number **7.3 GB/s** is suspiciously close to the practical limit of a **single PCIe Gen4 x4 link** (which tops out around 7.5 GB/s real-world).
    
    - **The Diagnosis:** It is highly likely that your two NVMe drives are sharing a single upstream bottleneck. This commonly happens if:
        
        - Both M.2 slots share a DMI link to the CPU (Chipset bottleneck).
            
        - The PCIe slot they are in (if using an adapter) is bifurcated but limited to x4 total or Gen3 x8 bandwidth.
            
        - The VM's vCPU cannot process interrupts fast enough to drive more than 7GB/s.
            

### 3. The "Metadata Storm" (4K Random Read)

- **Result:** `980k IOPS` (3.8 GB/s)
    
- **Hardware Expectation:** ~1M IOPS
    
- **Analysis:** This is a perfect score. You have successfully simulated a high-performance metadata server.
    
    - **Bottleneck Found:** Look at your CPU usage: `sys=75.60%`.
        
    - **Meaning:** Your CPU is screaming. It is spending 75% of its time just handling the interrupts from the NVMe drives. You have reached the limit of what the kernel can process, but 1 Million IOPS is massive. For comparison, a standard SATA SSD does ~80k IOPS. You are **12x faster**.
        

### 4. The "Real World" (Mixed 70/30)

- **Result:** `7.1 GB/s Total` (4.9 GB/s Read + 2.1 GB/s Write)
    
- **Analysis:** This confirms the bottleneck. Even when mixing reads and writes, the total aggregate throughput sums up to **~7.1 GB/s**. Your system simply cannot move more than ~7.3 GB of data per second across the bus.
    

### Conclusion for VAST Simulation

Despite the bandwidth cap, this configuration is **excellent** for your simulation.

1. **Metadata:** You have authentic, blistering fast metadata performance (1M IOPS). This will make VAST operations feel instantaneous.
    
2. **Throughput:** Even "capped" at 7.3 GB/s, you can simulate feeding a GPU cluster at speeds faster than most enterprise 100GbE SANs (which usually practically net ~8-9 GB/s).
    
3. **Next Step:** Unless you plan to upgrade to 100GbE networking, **do not worry about the 7.3 GB/s cap.** You have more local disk speed than your network card can likely handle anyway.
    

**You are green-lit for VAST deployment.**

These NVMe drives are in a PCI x16 slot on a Gen3 bus (Threadripper 2920x, x399 motherboard) set to bifurcation x4, x4, x4, x4. I assume this means we're getting the full capabilities of the bus?

Yes, your assumption is exactly right. You are getting **100% of the capabilities of the PCIe Gen 3.0 bus.**

The "bottleneck" we saw at 7.3 GB/s wasn't a configuration error—it was simply the **physics of the Threadripper 2920X.**

Here is the math that confirms your setup is running perfectly.

### The Physics of Your Threadripper 2920X

Your CPU is a 2nd Gen Threadripper (Zen+ architecture), which supports **PCIe Gen 3.0**. It does not support Gen 4.0 or 5.0.

- **Bus Speed:** PCIe Gen 3.0
    
- **Lane Bandwidth (x1):** ~985 MB/s
    
- **Drive Bandwidth (x4):** ~3,940 MB/s (3.94 GB/s) theoretical max per drive.
    
- **Total Bandwidth (2 Drives / x8 total):** ~7,880 MB/s (7.88 GB/s) theoretical max.
    

### Your Result vs. Theoretical Max

You achieved **7,348 MB/s** (Read).

7,880 MB/s (Theoretical)7,348 MB/s (Actual)​≈93.2% Efficiency

Getting 93% of the theoretical wire speed after overhead (filesystem, RAID calculation, virtualization) is **spectacular**. You are squeezing every last drop of performance out of that Gen 3.0 bus.

### Summary

1. **Bifurcation is working:** The fact that you got ~7.3 GB/s proves bifurcation works. If it wasn't working, you would have only seen one drive (~3.5 GB/s) or no drives.
    
2. **No "Shared Link" issue:** My previous suspicion about a DMI bottleneck was incorrect; you are simply hitting the speed limit of the Gen 3 interface.
    
3. **Future Proofing:** If you ever upgrade that CPU/Motherboard to a Threadripper 3000 (Gen 4) or newer, those same drives will instantly double in speed to ~14 GB/s without you changing a single config file.
    

**You are fully validated. The hardware is performing perfectly. Would you like to proceed with the VAST cluster installation now?**

UUID=9914d65e-64ef-46a7-9c3c-94e2d76279a3 /vast/drives xfs defaults,noatime,nodiratime 0 0
centos@localhost.localdomain:/home/centos $ cat /etc/fstab

#
# /etc/fstab
# Created by anaconda on Tue Jun 24 10:43:16 2025
#
# Accessible filesystems, by reference, are maintained under '/dev/disk/'.
# See man pages fstab(5), findfs(8), mount(8) and/or blkid(8) for more info.
#
# After editing this file, run 'systemctl daemon-reload' to update systemd
# units generated from this file.
#
UUID=9914d65e-64ef-46a7-9c3c-94e2d76279a3 /                       xfs     defaults        0 0
UUID=6542bc40-c6ae-41b1-85b3-3abb5d48bfe1 /boot                   xfs     defaults        0 0
UUID=f6fa6613-1edf-462a-9066-33b21e40d246 none                    swap    defaults        0 0
UUID=9914d65e-64ef-46a7-9c3c-94e2d76279a3 /vast/drives xfs defaults,noatime,nodiratime 0 0
centos@localhost.localdomain:/home/centos $ sudo mount -a
mount: (hint) your fstab has been modified, but systemd still uses
       the old version; use 'systemctl daemon-reload' to reload.
centos@localhost.localdomain:/home/centos $ sudo systemctl daemon-reload
centos@localhost.localdomain:/home/centos $ df -h
Filesystem      Size  Used Avail Use% Mounted on
devtmpfs         55G     0   55G   0% /dev
tmpfs            55G     0   55G   0% /dev/shm
tmpfs            55G  8.8M   55G   1% /run
tmpfs            55G     0   55G   0% /sys/fs/cgroup
/dev/sda3      1023G   31G  992G   3% /
/dev/sda1      1014M  247M  768M  25% /boot
tmpfs            11G     0   11G   0% /run/user/1000
centos@localhost.localdomain:/home/centos $ sudo mount -0a
mount: invalid option -- '0'
Try 'mount --help' for more information.
centos@localhost.localdomain:/home/centos $ sudo mount -a
centos@localhost.localdomain:/home/centos $ df
Filesystem      1K-blocks     Used  Available Use% Mounted on
devtmpfs         57466024        0   57466024   0% /dev
tmpfs            57482244        0   57482244   0% /dev/shm
tmpfs            57482244     9008   57473236   1% /run
tmpfs            57482244        0   57482244   0% /sys/fs/cgroup
/dev/sda3      1071842284 31812696 1040029588   3% /
/dev/sda1         1038336   252880     785456  25% /boot
tmpfs            11496448        0   11496448   0% /run/user/1000
centos@localhost.localdomain:/home/centos $ pwd
/home/centos
centos@localhost.localdomain:/home/centos $ nano /etc/fstab
centos@localhost.localdomain:/home/centos $ sudo nano /etc/fstab
centos@localhost.localdomain:/home/centos $ blkid
/dev/sda3: UUID="9914d65e-64ef-46a7-9c3c-94e2d76279a3" BLOCK_SIZE="512" TYPE="xfs" PARTUUID="74fd0506-03"
centos@localhost.localdomain:/home/centos $ lsblkid
zsh: command not found: lsblkid
centos@localhost.localdomain:/home/centos $ clear
centos@localhost.localdomain:/home/centos $ lsblk -f
NAME FSTYPE LABEL              UUID                                 MOUNTPOINT
sda
├─sda1
│    xfs                       6542bc40-c6ae-41b1-85b3-3abb5d48bfe1 /boot
├─sda2
│    swap                      f6fa6613-1edf-462a-9066-33b21e40d246 [SWAP]
└─sda3
     xfs                       9914d65e-64ef-46a7-9c3c-94e2d76279a3 /vast/driv
sr0
nvme1n1
│    linux_ localhost.localdomain:0
│                              a0ceec2a-c724-05f5-a618-27e46f42adc5
└─md0
     xfs                       edd7c7a2-d6e9-4530-aa70-51be9e5282bb /vast/driv
nvme0n1
│    linux_ localhost.localdomain:0
│                              a0ceec2a-c724-05f5-a618-27e46f42adc5
└─md0
     xfs                       edd7c7a2-d6e9-4530-aa70-51be9e5282bb /vast/driv
centos@localhost.localdomain:/home/centos $ sudo blkid -p /dev/md0
/dev/md0: UUID="edd7c7a2-d6e9-4530-aa70-51be9e5282bb" BLOCK_SIZE="512" TYPE="xfs" USAGE="filesystem"
centos@localhost.localdomain:/home/centos $ sudo nano /etc/fstab
centos@localhost.localdomain:/home/centos $ sudo mount -a
centos@localhost.localdomain:/home/centos $ df
Filesystem      1K-blocks     Used  Available Use% Mounted on
devtmpfs         57466024        0   57466024   0% /dev
tmpfs            57482244        0   57482244   0% /dev/shm
tmpfs            57482244     9008   57473236   1% /run
tmpfs            57482244        0   57482244   0% /sys/fs/cgroup
/dev/sda3      1071842284 31812720 1040029564   3% /
/dev/sda1         1038336   252880     785456  25% /boot
tmpfs            11496448        0   11496448   0% /run/user/1000
centos@localhost.localdomain:/home/centos $
centos@localhost.localdomain:/home/centos $
centos@localhost.localdomain:/home/centos $ mount -a
mount: only root can use "--all" option
centos@localhost.localdomain:/home/centos $ sudo mount -a
centos@localhost.localdomain:/home/centos $ cat /etc/fstab

#
# /etc/fstab
# Created by anaconda on Tue Jun 24 10:43:16 2025
#
# Accessible filesystems, by reference, are maintained under '/dev/disk/'.
# See man pages fstab(5), findfs(8), mount(8) and/or blkid(8) for more info.
#
# After editing this file, run 'systemctl daemon-reload' to update systemd
# units generated from this file.
#
UUID=9914d65e-64ef-46a7-9c3c-94e2d76279a3 /                       xfs     defaults        0 0
UUID=6542bc40-c6ae-41b1-85b3-3abb5d48bfe1 /boot                   xfs     defaults        0 0
UUID=f6fa6613-1edf-462a-9066-33b21e40d246 none                    swap    defaults        0 0
UUID=edd7c7a2-d6e9-4530-aa70-51be9e5282bb /vast/drives  xfs  noatime,nodiratime  0 0
centos@localhost.localdomain:/home/centos $
centos@localhost.localdomain:/home/centos $ sudo systemctl daemon-reload
centos@localhost.localdomain:/home/centos $ sudo mount /vast/drives
centos@localhost.localdomain:/home/centos $ sudo mount /vast/drives
mount: /vast/drives: /dev/md0 already mounted on /vast/drives.
centos@localhost.localdomain:/home/centos $ df -h /vast/drives
Filesystem      Size  Used Avail Use% Mounted on
/dev/md0        1.9T   14G  1.9T   1% /vast/drives
centos@localhost.localdomain:/home/centos $ sudo dnf install -y fio
Last metadata expiration check: 0:18:02 ago on Thu 01 Jan 2026 06:06:37 PM UTC.
Dependencies resolved.
==============================================================================
 Package            Architecture  Version              Repository        Size
==============================================================================
Installing:
 fio                x86_64        3.19-4.el8           appstream        537 k
Installing dependencies:
 daxctl-libs        x86_64        71.1-7.el8           baseos            41 k
 libpmem            x86_64        1.6.1-1.el8          appstream         78 k
 libpmemblk         x86_64        1.6.1-1.el8          appstream         91 k
 ndctl-libs         x86_64        71.1-7.el8           baseos            79 k

Transaction Summary
==============================================================================
Install  5 Packages

Total download size: 825 k
Installed size: 2.8 M
Downloading Packages:
(1/5): libpmemblk-1.6.1-1.el8.x86_64.rpm      612 kB/s |  91 kB     00:00
(2/5): libpmem-1.6.1-1.el8.x86_64.rpm         511 kB/s |  78 kB     00:00
(3/5): fio-3.19-4.el8.x86_64.rpm              2.3 MB/s | 537 kB     00:00
(4/5): daxctl-libs-71.1-7.el8.x86_64.rpm      391 kB/s |  41 kB     00:00
(5/5): ndctl-libs-71.1-7.el8.x86_64.rpm       657 kB/s |  79 kB     00:00
------------------------------------------------------------------------------
Total                                         2.0 MB/s | 825 kB     00:00
Running transaction check
Transaction check succeeded.
Running transaction test
Transaction test succeeded.
Running transaction
  Preparing        :                                                      1/1
  Installing       : daxctl-libs-71.1-7.el8.x86_64                        1/5
  Running scriptlet: daxctl-libs-71.1-7.el8.x86_64                        1/5
  Installing       : libpmem-1.6.1-1.el8.x86_64                           2/5
  Running scriptlet: libpmem-1.6.1-1.el8.x86_64                           2/5
  Installing       : ndctl-libs-71.1-7.el8.x86_64                         3/5
  Running scriptlet: ndctl-libs-71.1-7.el8.x86_64                         3/5
  Installing       : libpmemblk-1.6.1-1.el8.x86_64                        4/5
  Running scriptlet: libpmemblk-1.6.1-1.el8.x86_64                        4/5
  Installing       : fio-3.19-4.el8.x86_64                                5/5
  Running scriptlet: fio-3.19-4.el8.x86_64                                5/5
  Verifying        : fio-3.19-4.el8.x86_64                                1/5
  Verifying        : libpmem-1.6.1-1.el8.x86_64                           2/5
  Verifying        : libpmemblk-1.6.1-1.el8.x86_64                        3/5
  Verifying        : daxctl-libs-71.1-7.el8.x86_64                        4/5
  Verifying        : ndctl-libs-71.1-7.el8.x86_64                         5/5

Installed:
  daxctl-libs-71.1-7.el8.x86_64         fio-3.19-4.el8.x86_64
  libpmem-1.6.1-1.el8.x86_64            libpmemblk-1.6.1-1.el8.x86_64
  ndctl-libs-71.1-7.el8.x86_64

Complete!
centos@localhost.localdomain:/home/centos $ fio --name=vast_ingest \
    --directory=/vast/drives \
    --ioengine=libaio \
    --direct=1 \
    --rw=write \
    --bs=1M \
    --size=4G \
    --numjobs=4 \
    --iodepth=32 \
    --group_reporting \
    --runtime=60 \
    --time_based
vast_ingest: (g=0): rw=write, bs=(R) 1024KiB-1024KiB, (W) 1024KiB-1024KiB, (T) 1024KiB-1024KiB, ioengine=libaio, iodepth=32
...
fio-3.19
Starting 4 processes
vast_ingest: Laying out IO file (1 file / 4096MiB)
fio: pid=0, err=13/file:filesetup.c:174, func=open, error=Permission denied
vast_ingest: Laying out IO file (1 file / 4096MiB)
fio: pid=0, err=13/file:filesetup.c:174, func=open, error=Permission denied
vast_ingest: Laying out IO file (1 file / 4096MiB)
fio: pid=0, err=13/file:filesetup.c:174, func=open, error=Permission denied
vast_ingest: Laying out IO file (1 file / 4096MiB)
fio: pid=0, err=13/file:filesetup.c:174, func=open, error=Permission denied


Run status group 0 (all jobs):
centos@localhost.localdomain:/home/centos $
centos@localhost.localdomain:/home/centos $
centos@localhost.localdomain:/home/centos $ # 1. Give the 'centos' user ownership of the directory
sudo chown -R centos:centos /vast/drives

# 2. Set permissions (Owner=Read/Write/Exec, Others=Read/Exec)
sudo chmod 755 /vast/drives
centos@localhost.localdomain:/home/centos $ fio --name=vast_ingest \
    --directory=/vast/drives \
    --ioengine=libaio \
    --direct=1 \
    --rw=write \
    --bs=1M \
    --size=4G \
    --numjobs=4 \
    --iodepth=32 \
    --group_reporting \
    --runtime=60 \
    --time_based
vast_ingest: (g=0): rw=write, bs=(R) 1024KiB-1024KiB, (W) 1024KiB-1024KiB, (T) 1024KiB-1024KiB, ioengine=libaio, iodepth=32
...
fio-3.19
Starting 4 processes
vast_ingest: Laying out IO file (1 file / 4096MiB)
vast_ingest: Laying out IO file (1 file / 4096MiB)
vast_ingest: Laying out IO file (1 file / 4096MiB)
vast_ingest: Laying out IO file (1 file / 4096MiB)
Jobs: 4 (f=4): [W(4)][100.0%][w=5653MiB/s][w=5653 IOPS][eta 00m:00s]
vast_ingest: (groupid=0, jobs=4): err= 0: pid=7269: Thu Jan  1 18:26:41 2026
  write: IOPS=5636, BW=5636MiB/s (5910MB/s)(330GiB/60022msec); 0 zone resets
    slat (usec): min=24, max=466, avg=46.19, stdev= 9.21
    clat (usec): min=8238, max=51069, avg=22661.35, stdev=3624.76
     lat (usec): min=8291, max=51111, avg=22707.70, stdev=3624.95
    clat percentiles (usec):
     |  1.00th=[21365],  5.00th=[21365], 10.00th=[21365], 20.00th=[21365],
     | 30.00th=[21365], 40.00th=[21365], 50.00th=[21365], 60.00th=[21365],
     | 70.00th=[21365], 80.00th=[21365], 90.00th=[29492], 95.00th=[33424],
     | 99.00th=[33424], 99.50th=[33424], 99.90th=[40633], 99.95th=[42730],
     | 99.99th=[45351]
   bw (  MiB/s): min= 5440, max= 5744, per=100.00%, avg=5645.73, stdev=14.54, samples=476
   iops        : min= 5439, max= 5744, avg=5645.72, stdev=14.55, samples=476
  lat (msec)   : 10=0.01%, 20=0.06%, 50=99.92%, 100=0.01%
  cpu          : usr=4.06%, sys=2.91%, ctx=338286, majf=0, minf=45
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=100.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.1%, 64=0.0%, >=64=0.0%
     issued rwts: total=0,338293,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=32

Run status group 0 (all jobs):
  WRITE: bw=5636MiB/s (5910MB/s), 5636MiB/s-5636MiB/s (5910MB/s-5910MB/s), io=330GiB (355GB), run=60022-60022msec

Disk stats (read/write):
    md0: ios=0/675889, merge=0/0, ticks=0/9713647, in_queue=9713647, util=99.94%, aggrios=0/338301, aggrmerge=0/1, aggrticks=0/4866605, aggrin_queue=4866606, aggrutil=99.90%
  nvme0n1: ios=0/338304, merge=0/3, ticks=0/2069914, in_queue=2069914, util=98.94%
  nvme1n1: ios=0/338298, merge=0/0, ticks=0/7663297, in_queue=7663298, util=99.90%
centos@localhost.localdomain:/home/centos $ fio --name=vast_training \
    --directory=/vast/drives \
    --ioengine=libaio \
    --direct=1 \
    --rw=read \
    --bs=1M \
    --size=4G \
    --numjobs=4 \
    --iodepth=32 \
    --group_reporting \
    --runtime=60 \
    --time_based
vast_training: (g=0): rw=read, bs=(R) 1024KiB-1024KiB, (W) 1024KiB-1024KiB, (T) 1024KiB-1024KiB, ioengine=libaio, iodepth=32
...
fio-3.19
Starting 4 processes
vast_training: Laying out IO file (1 file / 4096MiB)
vast_training: Laying out IO file (1 file / 4096MiB)
vast_training: Laying out IO file (1 file / 4096MiB)
vast_training: Laying out IO file (1 file / 4096MiB)
Jobs: 4 (f=0): [f(4)][100.0%][r=6937MiB/s][r=6937 IOPS][eta 00m:00s]
vast_training: (groupid=0, jobs=4): err= 0: pid=7284: Thu Jan  1 18:27:55 2026
  read: IOPS=7007, BW=7008MiB/s (7348MB/s)(411GiB/60019msec)
    slat (usec): min=12, max=1370, avg=16.35, stdev= 8.36
    clat (usec): min=7289, max=35646, avg=18245.21, stdev=272.58
     lat (usec): min=7774, max=35662, avg=18261.68, stdev=269.87
    clat percentiles (usec):
     |  1.00th=[18220],  5.00th=[18220], 10.00th=[18220], 20.00th=[18220],
     | 30.00th=[18220], 40.00th=[18220], 50.00th=[18220], 60.00th=[18220],
     | 70.00th=[18220], 80.00th=[18220], 90.00th=[18220], 95.00th=[18220],
     | 99.00th=[18220], 99.50th=[18220], 99.90th=[18220], 99.95th=[18482],
     | 99.99th=[29492]
   bw (  MiB/s): min= 6937, max= 7088, per=100.00%, avg=7018.42, stdev= 9.69, samples=476
   iops        : min= 6936, max= 7088, avg=7018.40, stdev= 9.71, samples=476
  lat (msec)   : 10=0.03%, 20=99.93%, 50=0.04%
  cpu          : usr=0.94%, sys=3.68%, ctx=420580, majf=0, minf=129
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=100.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.1%, 64=0.0%, >=64=0.0%
     issued rwts: total=420609,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=32

Run status group 0 (all jobs):
   READ: bw=7008MiB/s (7348MB/s), 7008MiB/s-7008MiB/s (7348MB/s-7348MB/s), io=411GiB (441GB), run=60019-60019msec

Disk stats (read/write):
    md0: ios=838114/9, merge=0/0, ticks=10279537/2, in_queue=10279539, util=99.97%, aggrios=420609/4, aggrmerge=0/1, aggrticks=5157620/12, aggrin_queue=5157631, aggrutil=100.00%
  nvme0n1: ios=420609/6, merge=0/3, ticks=2642891/4, in_queue=2642894, util=100.00%
  nvme1n1: ios=420609/2, merge=0/0, ticks=7672350/20, in_queue=7672369, util=99.93%
centos@localhost.localdomain:/home/centos $ fio --name=vast_metadata \
>     --directory=/vast/drives \
>     --ioengine=libaio \
>     --direct=1 \
>     --rw=randread \
>     --bs=4k \
>     --size=1G \
>     --numjobs=8 \
>     --iodepth=64 \
>     --group_reporting \
>     --runtime=60 \
>     --time_based
vast_metadata: (g=0): rw=randread, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=64
...
fio-3.19
Starting 8 processes
vast_metadata: Laying out IO file (1 file / 1024MiB)
vast_metadata: Laying out IO file (1 file / 1024MiB)
vast_metadata: Laying out IO file (1 file / 1024MiB)
vast_metadata: Laying out IO file (1 file / 1024MiB)
vast_metadata: Laying out IO file (1 file / 1024MiB)
vast_metadata: Laying out IO file (1 file / 1024MiB)
vast_metadata: Laying out IO file (1 file / 1024MiB)
vast_metadata: Laying out IO file (1 file / 1024MiB)
Jobs: 8 (f=8): [r(8)][100.0%][r=3923MiB/s][r=1004k IOPS][eta 00m:00s]
vast_metadata: (groupid=0, jobs=8): err= 0: pid=7327: Thu Jan  1 18:46:17 2026
  read: IOPS=979k, BW=3826MiB/s (4012MB/s)(224GiB/60002msec)
    slat (nsec): min=1903, max=1147.6k, avg=6039.40, stdev=7726.58
    clat (usec): min=58, max=4914, avg=515.47, stdev=120.52
     lat (usec): min=66, max=4919, avg=521.69, stdev=121.92
    clat percentiles (usec):
     |  1.00th=[  388],  5.00th=[  408], 10.00th=[  416], 20.00th=[  433],
     | 30.00th=[  445], 40.00th=[  457], 50.00th=[  469], 60.00th=[  502],
     | 70.00th=[  537], 80.00th=[  578], 90.00th=[  660], 95.00th=[  816],
     | 99.00th=[  938], 99.50th=[  971], 99.90th=[ 1037], 99.95th=[ 1106],
     | 99.99th=[ 1336]
   bw (  MiB/s): min= 3274, max= 4465, per=100.00%, avg=3831.15, stdev=40.36, samples=952
   iops        : min=838208, max=1143262, avg=980773.46, stdev=10333.36, samples=952
  lat (usec)   : 100=0.01%, 250=0.01%, 500=60.05%, 750=33.47%, 1000=6.26%
  lat (msec)   : 2=0.21%, 4=0.01%, 10=0.01%
  cpu          : usr=24.36%, sys=75.60%, ctx=3304, majf=2, minf=621
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=100.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.1%, >=64=0.0%
     issued rwts: total=58766651,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=64

Run status group 0 (all jobs):
   READ: bw=3826MiB/s (4012MB/s), 3826MiB/s-3826MiB/s (4012MB/s-4012MB/s), io=224GiB (241GB), run=60002-60002msec

Disk stats (read/write):
    md0: ios=58649626/10, merge=0/0, ticks=3683662/2, in_queue=3683664, util=99.98%, aggrios=29383325/4, aggrmerge=0/1, aggrticks=1927212/3, aggrin_queue=1927215, aggrutil=99.92%
  nvme0n1: ios=29383028/6, merge=0/3, ticks=1960425/2, in_queue=1960427, util=99.92%
  nvme1n1: ios=29383623/3, merge=0/0, ticks=1894000/4, in_queue=1894003, util=99.92%
centos@localhost.localdomain:/home/centos $ fio --name=vast_mixed \
    --directory=/vast/drives \
    --ioengine=libaio \
    --direct=1 \
    --rw=randrw \
    --rwmixread=70 \
    --bs=128k \
    --size=4G \
    --numjobs=4 \
    --iodepth=32 \
    --group_reporting \
    --runtime=60 \
    --time_based
vast_mixed: (g=0): rw=randrw, bs=(R) 128KiB-128KiB, (W) 128KiB-128KiB, (T) 128KiB-128KiB, ioengine=libaio, iodepth=32
...
fio-3.19
Starting 4 processes
vast_mixed: Laying out IO file (1 file / 4096MiB)
vast_mixed: Laying out IO file (1 file / 4096MiB)
vast_mixed: Laying out IO file (1 file / 4096MiB)
vast_mixed: Laying out IO file (1 file / 4096MiB)
Jobs: 4 (f=4): [m(4)][4.9%][r=4636MiB/s,w=1987MiB/s][r=37.1k,w=15.9k IOPS][etaJobs: 4 (f=4): [m(4)][6.6%][r=4741MiB/s,w=2042MiB/s][r=37.9k,w=16.3k IOPS][etaJobs: 4 (f=4): [m(4)][8.2%][r=4678MiB/s,w=2014MiB/s][r=37.4k,w=16.1k IOPS][etaJobs: 4 (f=4): [m(4)][9.8%][r=4712MiB/s,w=2006MiB/s][r=37.7k,w=16.0k IOPS][etaJobs: 4 (f=4): [m(4)][11.5%][r=4802MiB/s,w=2038MiB/s][r=38.4k,w=16.3k IOPS][etJobs: 4 (f=4): [m(4)][13.1%][r=4723MiB/s,w=2016MiB/s][r=37.8k,w=16.1k IOPS][etJobs: 4 (f=4): [m(4)][14.8%][r=4751MiB/s,w=2072MiB/s][r=38.0k,w=16.6k IOPS][etJobs: 4 (f=4): [m(4)][16.4%][r=4597MiB/s,w=1992MiB/s][r=36.8k,w=15.9k IOPS][etJobs: 4 (f=4): [m(4)][18.0%][r=4885MiB/s,w=2088MiB/s][r=39.1k,w=16.7k IOPS][etJobs: 4 (f=4): [m(4)][19.7%][r=4810MiB/s,w=2048MiB/s][r=38.5k,w=16.4k IOPS][etJobs: 4 (f=4): [m(4)][21.3%][r=4777MiB/s,w=2076MiB/s][r=38.2k,w=16.6k IOPS][etJobs: 4 (f=4): [m(4)][23.3%][r=4845MiB/s,w=2065MiB/s][r=38.8k,w=16.5k IOPS][etJobs: 4 (f=4): [m(4)][25.0%][r=4696MiB/s,w=1993MiB/s][r=37.6k,w=15.9k IOPS][etJobs: 4 (f=4): [m(4)][26.7%][r=4927MiB/s,w=2134MiB/s][r=39.4k,w=17.1k IOPS][etJobs: 4 (f=4): [m(4)][28.3%][r=4754MiB/s,w=2040MiB/s][r=38.0k,w=16.3k IOPS][etJobs: 4 (f=4): [m(4)][30.0%][r=4834MiB/s,w=2110MiB/s][r=38.7k,w=16.9k IOPS][etJobs: 4 (f=4): [m(4)][31.7%][r=4733MiB/s,w=2035MiB/s][r=37.9k,w=16.3k IOPS][etJobs: 4 (f=4): [m(4)][33.3%][r=4765MiB/s,w=2060MiB/s][r=38.1k,w=16.5k IOPS][etJobs: 4 (f=4): [m(4)][35.0%][r=4869MiB/s,w=2072MiB/s][r=38.0k,w=16.6k IOPS][etJobs: 4 (f=4): [m(4)][36.7%][r=4752MiB/s,w=2046MiB/s][r=38.0k,w=16.4k IOPS][etJobs: 4 (f=4): [m(4)][38.3%][r=4778MiB/s,w=2081MiB/s][r=38.2k,w=16.6k IOPS][etJobs: 4 (f=4): [m(4)][40.0%][r=4843MiB/s,w=2100MiB/s][r=38.7k,w=16.8k IOPS][etJobs: 4 (f=4): [m(4)][41.7%][r=4789MiB/s,w=2048MiB/s][r=38.3k,w=16.4k IOPS][etJobs: 4 (f=4): [m(4)][44.1%][r=4767MiB/s,w=2057MiB/s][r=38.1k,w=16.5k IOPS][etJobs: 4 (f=4): [m(4)][45.0%][r=4828MiB/s,w=2081MiB/s][r=38.6k,w=16.6k IOPS][etJobs: 4 (f=4): [m(4)][46.7%][r=4725MiB/s,w=2043MiB/s][r=37.8k,w=16.3k IOPS][etJobs: 4 (f=4): [m(4)][48.3%][r=4891MiB/s,w=2107MiB/s][r=39.1k,w=16.9k IOPS][etJobs: 4 (f=4): [m(4)][50.0%][r=4652MiB/s,w=2007MiB/s][r=37.2k,w=16.1k IOPS][etJobs: 4 (f=4): [m(4)][52.5%][r=4911MiB/s,w=2105MiB/s][r=39.3k,w=16.8k IOPS][etJobs: 4 (f=4): [m(4)][53.3%][r=4687MiB/s,w=2016MiB/s][r=37.5k,w=16.1k IOPS][etJobs: 4 (f=4): [m(4)][55.0%][r=4848MiB/s,w=2072MiB/s][r=38.8k,w=16.6k IOPS][etJobs: 4 (f=4): [m(4)][56.7%][r=4753MiB/s,w=2045MiB/s][r=38.0k,w=16.4k IOPS][etJobs: 4 (f=4): [m(4)][58.3%][r=4705MiB/s,w=2019MiB/s][r=37.6k,w=16.1k IOPS][etJobs: 4 (f=4): [m(4)][60.0%][r=4854MiB/s,w=2087MiB/s][r=38.8k,w=16.7k IOPS][etJobs: 4 (f=4): [m(4)][62.7%][r=4704MiB/s,w=2044MiB/s][r=37.6k,w=16.4k IOPS][etJobs: 4 (f=4): [m(4)][63.3%][r=4890MiB/s,w=2073MiB/s][r=39.1k,w=16.6k IOPS][etJobs: 4 (f=4): [m(4)][66.1%][r=4680MiB/s,w=2021MiB/s][r=37.4k,w=16.2k IOPS][etJobs: 4 (f=4): [m(4)][66.7%][r=4639MiB/s,w=2003MiB/s][r=37.1k,w=16.0k IOPS][etJobs: 4 (f=4): [m(4)][68.3%][r=4782MiB/s,w=2042MiB/s][r=38.3k,w=16.3k IOPS][etJobs: 4 (f=4): [m(4)][70.0%][r=4732MiB/s,w=2028MiB/s][r=37.9k,w=16.2k IOPS][etJobs: 4 (f=4): [m(4)][71.7%][r=4759MiB/s,w=2026MiB/s][r=38.1k,w=16.2k IOPS][etJobs: 4 (f=4): [m(4)][73.3%][r=4716MiB/s,w=2020MiB/s][r=37.7k,w=16.2k IOPS][etJobs: 4 (f=4): [m(4)][75.0%][r=4685MiB/s,w=2018MiB/s][r=37.5k,w=16.1k IOPS][etJobs: 4 (f=4): [m(4)][76.7%][r=4812MiB/s,w=2041MiB/s][r=38.5k,w=16.3k IOPS][etJobs: 4 (f=4): [m(4)][78.3%][r=4758MiB/s,w=2039MiB/s][r=38.1k,w=16.3k IOPS][etJobs: 4 (f=4): [m(4)][80.0%][r=4714MiB/s,w=2032MiB/s][r=37.7k,w=16.3k IOPS][etJobs: 4 (f=4): [m(4)][81.7%][r=4727MiB/s,w=2041MiB/s][r=37.8k,w=16.3k IOPS][etJobs: 4 (f=4): [m(4)][83.3%][r=4612MiB/s,w=1982MiB/s][r=36.9k,w=15.9k IOPS][etJobs: 4 (f=4): [m(4)][85.0%][r=4822MiB/s,w=2027MiB/s][r=38.6k,w=16.2k IOPS][etJobs: 4 (f=4): [m(4)][88.1%][r=4759MiB/s,w=2010MiB/s][r=38.1k,w=16.1k IOPS][etJobs: 4 (f=4): [m(4)][88.3%][r=4759MiB/s,w=2056MiB/s][r=38.1k,w=16.4k IOPS][etJobs: 4 (f=4): [m(4)][90.0%][r=4639MiB/s,w=2012MiB/s][r=37.1k,w=16.1k IOPS][etJobs: 4 (f=4): [m(4)][91.7%][r=4750MiB/s,w=2033MiB/s][r=38.0k,w=16.3k IOPS][etJobs: 4 (f=4): [m(4)][93.3%][r=4748MiB/s,w=2016MiB/s][r=37.0k,w=16.1k IOPS][etJobs: 4 (f=4): [m(4)][95.0%][r=4681MiB/s,w=2005MiB/s][r=37.5k,w=16.0k IOPS][etJobs: 4 (f=4): [m(4)][96.7%][r=4737MiB/s,w=2032MiB/s][r=37.9k,w=16.3k IOPS][etJobs: 4 (f=4): [m(4)][98.3%][r=4657MiB/s,w=2015MiB/s][r=37.3k,w=16.1k IOPS][etJobs: 4 (f=4): [m(4)][100.0%][r=4806MiB/s,w=2057MiB/s][r=38.4k,w=16.5k IOPS][eta 00m:00s]
vast_mixed: (groupid=0, jobs=4): err= 0: pid=7347: Thu Jan  1 18:47:49 2026
  read: IOPS=38.0k, BW=4751MiB/s (4982MB/s)(278GiB/60005msec)
    slat (usec): min=3, max=249, avg= 7.00, stdev= 2.76
    clat (usec): min=90, max=27061, avg=3263.53, stdev=2840.17
     lat (usec): min=95, max=27068, avg=3270.64, stdev=2840.24
    clat percentiles (usec):
     |  1.00th=[  120],  5.00th=[  176], 10.00th=[  229], 20.00th=[  367],
     | 30.00th=[  906], 40.00th=[ 1942], 50.00th=[ 3064], 60.00th=[ 4146],
     | 70.00th=[ 5014], 80.00th=[ 5538], 90.00th=[ 5997], 95.00th=[ 6587],
     | 99.00th=[13304], 99.50th=[15533], 99.90th=[20579], 99.95th=[21890],
     | 99.99th=[24249]
   bw (  MiB/s): min= 4445, max= 5144, per=100.00%, avg=4760.49, stdev=33.01, samples=476
   iops        : min=35560, max=41156, avg=38083.92, stdev=264.04, samples=476
  write: IOPS=16.3k, BW=2041MiB/s (2141MB/s)(120GiB/60005msec); 0 zone resets
    slat (usec): min=3, max=886, avg=10.69, stdev= 3.99
    clat (usec): min=39, max=16254, avg=211.06, stdev=653.16
     lat (usec): min=60, max=16264, avg=221.87, stdev=653.17
    clat percentiles (usec):
     |  1.00th=[   62],  5.00th=[   65], 10.00th=[   68], 20.00th=[   71],
     | 30.00th=[   74], 40.00th=[   79], 50.00th=[   88], 60.00th=[  100],
     | 70.00th=[  116], 80.00th=[  149], 90.00th=[  253], 95.00th=[  416],
     | 99.00th=[ 3589], 99.50th=[ 5080], 99.90th=[ 8848], 99.95th=[ 9765],
     | 99.99th=[11731]
   bw (  MiB/s): min= 1868, max= 2254, per=100.00%, avg=2045.12, stdev=18.03, samples=476
   iops        : min=14950, max=18036, avg=16360.91, stdev=144.23, samples=476
  lat (usec)   : 50=0.01%, 100=18.03%, 250=17.42%, 500=10.38%, 750=2.95%
  lat (usec)   : 1000=2.14%
  lat (msec)   : 2=7.00%, 4=12.84%, 10=27.66%, 20=1.48%, 50=0.10%
  cpu          : usr=5.80%, sys=11.99%, ctx=2463298, majf=0, minf=71
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=100.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.1%, 64=0.0%, >=64=0.0%
     issued rwts: total=2280781,979937,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=32

Run status group 0 (all jobs):
   READ: bw=4751MiB/s (4982MB/s), 4751MiB/s-4751MiB/s (4982MB/s-4982MB/s), io=278GiB (299GB), run=60005-60005msec
  WRITE: bw=2041MiB/s (2141MB/s), 2041MiB/s-2041MiB/s (2141MB/s-2141MB/s), io=120GiB (128GB), run=60005-60005msec

Disk stats (read/write):
    md0: ios=2274487/977196, merge=0/0, ticks=7390217/192571, in_queue=7582788, util=99.98%, aggrios=1140390/489977, aggrmerge=0/1, aggrticks=3713412/98502, aggrin_queue=3811914, aggrutil=97.33%
  nvme0n1: ios=1141223/489259, merge=0/3, ticks=3475885/104059, in_queue=3579944, util=96.67%
  nvme1n1: ios=1139558/490695, merge=0/0, ticks=3950939/92946, in_queue=4043884, util=97.33%
centos@localhost.localdomain:/home/centos $
centos@localhost.localdomain:/home/centos $ rm /vast/drives/vast_*
centos@localhost.localdomain:/home/centos $ sudo mkdir -p /vast/bundles
sudo mkdir -p /vast/deploy
sudo mkdir -p /vast/data
sudo mkdir -p /vast/vman
sudo mkdir -p /vast/drives

# Set ownership
sudo chown -R centos:centos /vast

# Create OS release marker (VAST checks this)
echo '1.1.1' | sudo tee /etc/vast-os-release
sudo chmod 644 /etc/vast-os-release
1.1.1
centos@localhost.localdomain:/home/centos $ echo "11.0.0.1 vastdata.registry.local" | sudo tee -a /etc/hosts

# Create registry cache pointer
sudo mkdir -p /file_server
echo "vastdata.registry.local:5000" | sudo tee /file_server/DCACHE

11.0.0.1 vastdata.registry.local
vastdata.registry.local:5000
centos@localhost.localdomain:/home/centos $ [ ! -f ~/.ssh/id_rsa ] && ssh-keygen -f ~/.ssh/id_rsa -q -N ""

# Add to authorized_keys
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys

# Copy to VAST deploy location
sudo mkdir -p /vast/deploy
sudo cp ~/.ssh/id_rsa /vast/deploy/ssh_key.pem
sudo chown centos:centos /vast/deploy/ssh_key.pem
chmod 600 /vast/deploy/ssh_key.pem

# Test SSH to localhost (should work without password)
ssh -o StrictHostKeyChecking=no localhost "echo SSH works"
SSH works
centos@localhost.localdomain:/home/centos $ sudo swapoff -a

# Remove swap from fstab
sudo sed -i '/swap/d' /etc/fstab

# Verify
free -h
# Should show "Swap: 0B 0B 0B"

              total        used        free      shared  buff/cache   available
Mem:          109Gi       567Mi       108Gi       8.0Mi       720Mi       106Gi
Swap:            0B          0B          0B
centos@localhost.localdomain:/home/centos $ # Disable immediately
sudo setenforce 0

# Disable permanently
sudo sed -i 's/SELINUX=enforcing/SELINUX=disabled/' /etc/selinux/config

# Verify
getenforce
# Should show "Permissive" or "Disabled"
setenforce: SELinux is disabled
Disabled
centos@localhost.localdomain:/home/centos $ ```bash
# Check guest agent
sudo systemctl is-active qemu-guest-agent

# Check Docker
docker ps

# Check NVMe/storage
df -h /vast/drives

# Check SSH key
ssh localhost "echo SSH OK"

# Check Docker registry config
cat /etc/docker/daemon.json

# Check VirtIO drivers
lsmod | grep virtio

# Check SELinux
getenforce

# Check swap
free -h | grep Swap
bquote>
centos@localhost.localdomain:/home/centos $

