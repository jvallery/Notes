# VM Setup and VMDK Import

**Document:** 03-VM-Setup.md  
**Last Updated:** December 30, 2025  

---

## Overview

This document covers creating the VAST VM in Proxmox, including:
- Extracting the VMDK from the ESXi OVA
- Importing and converting the disk image
- Configuring VM settings for optimal performance
- Setting up PCIe passthrough for NVMe drives
- Resizing the OS disk (the OVA's 600GB disk is unnecessary with passthrough)

---

## Prerequisites

Before starting:

- [ ] Proxmox VE installed and accessible
- [ ] VAST 5.4 OVA file obtained (e.g., `vast-5.4.0-loopback.ova`)
- [ ] PCIe passthrough configured (see [02-Hardware-Performance.md](02-Hardware-Performance.md))
- [ ] Sufficient storage for disk conversion (~50GB for OS disk)

---

## Step 1: Extract VMDK from OVA

The OVA is a tar archive containing the VMDK disk image.

### On Your Workstation or Proxmox Host

```bash
# Create working directory
mkdir -p /tmp/vast-ova
cd /tmp/vast-ova

# Extract OVA (it's just a tar file)
tar -xvf /path/to/vast-5.4.0-loopback.ova

# List contents - should see .vmdk files
ls -la *.vmdk
```

You should see something like:
```
-rw-r--r-- 1 root root 30000000000 Dec 29 12:00 vast-loopback-disk1.vmdk
```

The VMDK may be split into multiple files (e.g., `*-s001.vmdk`, `*-s002.vmdk`).

---

## Step 2: Create the VM

### Via Proxmox GUI

1. **Create VM** (don't add disk yet):
   - Datacenter → your node → Create VM
   - General: VM ID (e.g., 100), Name: `vast-loopback`
   - OS: Do not use any media (we'll import disk)
   - System: 
     - Machine: `q35`
     - SCSI Controller: `LSI 53C895A` (VMware compatible - required for initial boot)
       
       **JV Comment: Why not the VMWare PVSCSI -- this is what I used before?  Confirm SeaBIOS? 
       
     - Qemu Agent: ✓ Checked
       
       
   - Disks: **Delete the default disk** (we'll import)
   - CPU:
     - Sockets: 1
     - Cores: 12 (match your physical cores) 
       
       **JV Comment: (starting with 16 here)**
       
     - Type: `host`
     - Enable NUMA: ✓
   - Memory: 
     - Memory: 122880 MB (120 GB)
     - Ballooning: ✗ Unchecked
   - Network:
     - Model: VirtIO
     - Bridge: vmbr0

2. **Don't start the VM yet** - we need to import the disk first.

**Important:** The SCSI controller must be **LSI 53C895A** (VMware compatible) for the initial boot. The OVA was built for VMware and won't boot with VirtIO until we install VirtIO drivers inside the guest.

### Via CLI

```bash
VMID=100
qm create $VMID \
  --name vast-loopback \
  --machine q35 \
  --ostype l26 \
  --scsihw lsi \
  --agent 1 \
  --cpu host \
  --sockets 1 \
  --cores 12 \
  --numa 1 \
  --memory 122880 \
  --balloon 0 \
  --net0 virtio,bridge=vmbr0
```

**Note:** We'll switch to VirtIO SCSI after installing VirtIO drivers. See [04-First-Boot.md](04-First-Boot.md).

---

## Step 3: Import the VMDK

> **⚠️ DO NOT RESIZE THE OS DISK SMALLER THAN 200GB**  
> The OVA's `/vast` directory contains bundles (~20GB), Docker images (~15GB), container data, and logs. Shrinking to 50GB will cause failures.

### Option A: Keep Original Size (Recommended)

The OVA comes with a ~600GB disk. Keep this or resize to 200GB minimum:

```bash
cd /tmp/vast-ova

# Check VMDK info
qemu-img info vast-loopback-disk1.vmdk

# Import to Proxmox storage (e.g., local-lvm)
qm disk import $VMID vast-loopback-disk1.vmdk local-lvm --format qcow2
```

### Option B: Full Size Import

If you prefer to keep the full disk:

```bash
qm disk import $VMID vast-loopback-disk1.vmdk local-lvm
```

### Attach the Disk

After import, the disk is unused. Attach it:

```bash
# Attach as scsi0 with IO thread enabled
qm set $VMID --scsi0 local-lvm:vm-$VMID-disk-0,iothread=1,discard=on
```

Or in GUI: Hardware → Unused Disk → Edit → Add

---

## Step 4: Add PCIe Passthrough NVMe Devices

If using NVMe passthrough (recommended):

### Find Device IDs

```bash
lspci -nn | grep -i nvme
```

Example output:
```
01:00.0 Non-Volatile memory controller [0108]: Samsung Electronics Co Ltd NVMe SSD Controller SM981/PM981 [144d:a808]
02:00.0 Non-Volatile memory controller [0108]: Samsung Electronics Co Ltd NVMe SSD Controller SM981/PM981 [144d:a808]
```

### Add to VM

```bash
# Add first NVMe
qm set $VMID --hostpci0 01:00.0,pcie=1

# Add second NVMe
qm set $VMID --hostpci1 02:00.0,pcie=1
```

Or in GUI: Hardware → Add → PCI Device

**JV Comment/Gemini notes:**
Which of these do I need to map to the PCIe pass through?

  

root@onyx:~# lspci -nn | grep -i nvme

09:00.0 Non-Volatile memory controller [0108]: Samsung Electronics Co Ltd NVMe SSD Controller SM981/PM981/PM983 [144d:a808]

0a:00.0 Non-Volatile memory controller [0108]: Samsung Electronics Co Ltd NVMe SSD Controller PM9C1a (DRAM-less) [144d:a80d]

0b:00.0 Non-Volatile memory controller [0108]: Samsung Electronics Co Ltd NVMe SSD Controller PM9C1a (DRAM-less) [144d:a80d]

41:00.0 Non-Volatile memory controller [0108]: Samsung Electronics Co Ltd NVMe SSD Controller PM9A1/PM9A3/980PRO [144d:a80a]

42:00.0 Non-Volatile memory controller [0108]: Samsung Electronics Co Ltd NVMe SSD Controller SM981/PM981/PM983 [144d:a808]

Based on the device IDs, here are the two you need to pass through.

You are looking for the **Samsung 990 EVO Plus** drives. These use the newer "PM9C1a" controller (Device ID `a80d`).

### The Targets (Pass These Through)

- **`0a:00.0`** (Samsung 990 EVO Plus)
    
- **`0b:00.0`** (Samsung 990 EVO Plus)
    

---

### The Full Decoder Ring

Here is what every device in that list corresponds to, so you don't accidentally pass through your OS drive.

|Bus ID|Controller Name|Device ID|Real Drive Model|Role|
|---|---|---|---|---|
|**`0a:00.0`**|**PM9C1a (DRAM-less)**|`[144d:a80d]`|**Samsung 990 EVO Plus**|**VAST Passthrough (Target)**|
|**`0b:00.0`**|**PM9C1a (DRAM-less)**|`[144d:a80d]`|**Samsung 990 EVO Plus**|**VAST Passthrough (Target)**|
|`41:00.0`|PM9A1/980PRO|`[144d:a80a]`|Samsung 980 PRO|`temp-tank` (Backup)|
|`09:00.0`|SM981/Phoenix|`[144d:a808]`|Samsung 970 EVO Plus|`tank` (New VM Data)|
|`42:00.0`|SM981/Phoenix|`[144d:a808]`|Samsung 970 PRO|`rpool` (OS Drive)|

_(Note: The 970 PRO and 970 EVO Plus share the same controller ID `a808`, so distinguishing them relies on the slot, but `0a` and `0b` are definitely the 990s)._

### Command to Attach

Assuming your VM ID is **105**, you can run this command to attach both PCI devices directly:

Bash

```
qm set 105 -hostpci0 0000:0a:00.0 -hostpci1 0000:0b:00.0
```

Or, if doing this in the Proxmox GUI:

1. Go to **VM 105** > **Hardware**.
    
2. **Add** > **PCI Device**.
    
3. Select `0000:0a:00.0`.
    
4. Repeat for `0000:0b:00.0`.
    
5. Check **"All Functions"** (optional but good practice) and ensure **"PCI-Express"** is checked.
    

On PCI express devices, Proxmox 9.1 has checkmarks for "ROM-Bar" and "PCI-EXpress". Do I check these?

For NVMe storage drives that are being passed through as secondary data disks (which is exactly what you are doing for VAST), here are the correct settings:

- **PCI-Express:** **CHECK ✅**
    
- **ROM-Bar:** **UNCHECK ⬜**
    

### The "Why"

1. **PCI-Express (Check it):**
    
    - This tells the VM, "This is a modern, high-speed PCIe device, not an old-school legacy PCI card."
        
    - It is critical for performance and ensures the guest OS (Rocky Linux) negotiates the link speed correctly.
        
2. **ROM-Bar (Uncheck it):**
    
    - The "ROM Bar" makes the device's firmware (Option ROM) visible to the VM's BIOS at boot time.
        
    - **Why uncheck?** You are booting the VM from the virtual disk (`scsi0`), not from these NVMe drives. If you enable the ROM-Bar, the VM's BIOS might try to initialize these drives during startup, which can cause boot delays or conflicts. You want the OS to load, and _then_ the Linux kernel to discover the drives.
        

### Summary Checklist for your GUI

When adding the device, your window should look like this:

- **Device:** `0000:0a:00.0` (and `0b` for the second one)
    
- **All Functions:** **Checked** (Good practice, though NVMe usually only has function 0)
    
- **ROM-Bar:** **Unchecked**
    
- **PCI-Express:** **Checked**
    

Once you click "Add," you don't need to reboot the host, but you will need to **Stop** and **Start** the VM (not just reboot) for the changes to take effect.

---

## Step 5: Resize OS Disk (Optional)

If you imported the full 600GB disk but want to shrink it:

**Warning:** This is irreversible. Create a backup first.

### Shrink qcow2 Disk

1. Boot VM and shrink filesystem inside (dangerous, not recommended)
2. Or start fresh with a smaller disk and migrate data

**Recommendation:** For fresh deployments, use a minimal OS disk (50GB) and put all VAST data on passthrough NVMe.

### Alternative: Create New Small Disk

```bash
# Remove the large disk
qm set $VMID --delete scsi0

# Create a new small OS disk
qm set $VMID --scsi0 local-lvm:50,iothread=1,discard=on
```

**Note:** We always use the VAST OVA/VMDK - fresh Rocky Linux installs are not supported because the OVA contains VAST-specific pre-configuration.

---

## Step 6: Configure Boot Order

Ensure the VM boots from the correct device:

```bash
# Set boot order (scsi0 = OS disk)
qm set $VMID --boot order=scsi0
```

Or if installing from ISO:
```bash
# NOTE: We do NOT install from ISO - always use the VAST OVA/VMDK
```

---

## Step 7: Final VM Configuration Review

Verify the VM configuration:

```bash
qm config $VMID
```

Expected output (key settings):

```
cores: 12
memory: 122880
balloon: 0
cpu: host
scsihw: lsi
numa: 1
hostpci0: 01:00.0,pcie=1
hostpci1: 02:00.0,pcie=1
scsi0: local-lvm:vm-100-disk-0,iothread=1,discard=on
net0: virtio=...,bridge=vmbr0
agent: 1
```

**Note:** After installing VirtIO drivers (see [04-First-Boot.md](04-First-Boot.md)), you'll change `scsihw: lsi` to `scsihw: virtio-scsi-single` for better performance.

---

## VM Configuration Summary

### Final Configuration

| Setting | Value |
|---------|-------|
| Machine | q35 |
| BIOS | SeaBIOS (or OVMF for UEFI) |
| CPU Type | host |
| Sockets | 1 |
| Cores | 12 |
| RAM | 120 GB |
| Ballooning | Disabled |
| NUMA | Enabled |
| SCSI Controller | LSI 53C895A (initial boot) → VirtIO SCSI single (after driver install) |
| OS Disk | 200 GB (local-lvm, VirtIO, IO Thread) |
| NVMe | PCIe passthrough (2 devices) |
| Network | VirtIO on vmbr0 |
| Guest Agent | Enabled |

### GUI Quick Reference

In Proxmox GUI → VM → Hardware:

| Component | Initial Boot Setting | After VirtIO Install |
|-----------|---------------------|----------------------|
| SCSI Controller | LSI 53C895A | VirtIO SCSI single |
| Processors | 1 socket, 12 cores, host type, NUMA enabled | (unchanged) |
| Memory | 122880 MB, no ballooning | (unchanged) |
| Hard Disk (scsi0) | 50GB, IO Thread, Cache: none, Discard | (unchanged) |
| PCI Device 0 | NVMe (01:00.0) | (unchanged) |
| PCI Device 1 | NVMe (02:00.0) | (unchanged) |
| Network Device | VirtIO, vmbr0 | (unchanged) |

---

## Verify Before First Boot

Before starting the VM:

- [ ] CPU cores ≤ physical cores
- [ ] Memory ballooning disabled
- [ ] SCSI controller is LSI 53C895A (for initial boot from OVA)
- [ ] IO Thread enabled on disks
- [ ] Guest agent enabled
- [ ] NVMe devices attached (if using passthrough)

---

## Create Pre-Boot Snapshot

Create a snapshot before first boot to enable easy rollback:

```bash
qm snapshot $VMID pre-boot --description "Before first boot"
```

---

## Troubleshooting

### VMDK Import Fails

**Error:** `qemu-img: Could not open 'disk.vmdk': Could not open backing file`

**Solution:** Ensure all VMDK segments are in the same directory:
```bash
ls -la *.vmdk  # Should show all segments
```

### VM Won't Boot After Import

**Symptoms:** Kernel panic, no root filesystem, blank screen

**Cause:** Wrong SCSI controller - OVA was built for VMware SCSI (LSI), not VirtIO

**Solution:** 
1. Ensure SCSI controller is set to "LSI 53C895A" (not VirtIO)
2. Boot should succeed with LSI controller
3. Install VirtIO drivers inside guest (see [04-First-Boot.md](04-First-Boot.md))
4. Only then switch to VirtIO SCSI controller

### PCIe Passthrough Device Not Visible

**Symptoms:** VM boots but NVMe not detected

**Solutions:**
1. Verify IOMMU is enabled: `dmesg | grep -i iommu`
2. Check device is isolated: `lspci -s 01:00.0 -v | grep -i driver`
3. Device should show `Kernel driver in use: vfio-pci`

### VM Uses Wrong Disk

**Symptoms:** Boots from ISO instead of disk

**Solution:** 
```bash
qm set $VMID --boot order=scsi0
```

---

## Next Steps

After VM creation:

1. **First Boot:** [04-First-Boot.md](04-First-Boot.md) - Install guest agent, Docker, configure NVMe
2. **Topology Planning:** [05-Topology-Planning.md](05-Topology-Planning.md) - Plan your cluster size
3. **Pre-Install Tweaks:** [06-Pre-Install-Tweaks.md](06-Pre-Install-Tweaks.md) - Apply workarounds

---

*Previous: [02-Hardware-Performance.md](02-Hardware-Performance.md) | Next: [04-First-Boot.md](04-First-Boot.md)*
