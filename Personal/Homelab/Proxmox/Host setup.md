Here is the consolidated runbook of everything we have done so far. You can copy this directly into your Obsidian note.

## **Proxmox Cluster Setup Runbook**

Target Nodes: Opal, Oro (and future: Onyx, Olivine)

Network Subnet: 192.168.30.0/24

Goal: Identical Networking, ZFS storage, NTP sync, and Package Repositories.

### **Phase 1: SSH Access & Keys**

1. **Clean Client Known Hosts:** Remove old fingerprints on the management machine (MacBook).
    
    Bash
    
    ```
    ssh-keygen -R [IP_ADDRESS]
    ssh-keygen -R [HOSTNAME]
    ```
    
2. **Install Public Key:** Push SSH key to all nodes for passwordless root access.
    
    Bash
    
    ```
    ssh-copy-id root@[HOSTNAME]
    ```
    

### **Phase 2: ZFS Storage Configuration**

**Goal:** Create a standardized storage pool named `tank` mirrored across identical NVMe drives.

1. **Identify Disk IDs:** List physical disk info to ensure we select the correct NVMe drives by ID (avoiding `/dev/nvme0n1` drift).
    
    Bash
    
    ```
    lsblk -o NAME,SIZE,MODEL,SERIAL,TYPE
    ls -l /dev/disk/by-id/
    ```
    
2. **Create Pool (Example):**
    
    Bash
    
    ```
    zpool create -f -o ashift=12 tank mirror \
      /dev/disk/by-id/[DISK_ID_1] \
      /dev/disk/by-id/[DISK_ID_2]
    ```
    

### **Phase 3: Repository & Update Management**

**Goal:** Remove Enterprise repos (unless licensed), enable Community repos, and automate security patches.

3.1 Clean Enterprise Repos

Remove the default enterprise sources that cause 401 Unauthorized errors.

Bash

```
# Remove main enterprise list if present
rm -f /etc/apt/sources.list.d/pve-enterprise.list

# Remove new deb822 source files (Proxmox 8.x+)
rm -f /etc/apt/sources.list.d/pve-enterprise.sources
rm -f /etc/apt/sources.list.d/ceph.sources

# Comment out any stragglers in the main list
sed -i "s|^deb https://enterprise.proxmox.com|#deb https://enterprise.proxmox.com|g" /etc/apt/sources.list
```

3.2 Add Community Repos

Add the "No-Subscription" repository.

Bash

```
# Note: Ensure distribution matches (e.g., bookworm vs trixie)
echo "deb http://download.proxmox.com/debian/pve trixie pve-no-subscription" > /etc/apt/sources.list.d/pve-no-subscription.list
```

3.3 Update & Install Utilities

Update the system and install time sync (Chrony) and update helpers.

Bash

```
apt update && apt dist-upgrade -y
apt install chrony unattended-upgrades apt-listchanges -y
```

3.4 Configure Unattended Upgrades

Enable automatic security updates but disable automatic reboots to protect cluster stability.

Bash

```
echo 'Unattended-Upgrade::Allowed-Origins {
    "${distro_id}:${distro_codename}-security";
    "Proxmox:${distro_codename}";
};
Unattended-Upgrade::Package-Blacklist {
};
Unattended-Upgrade::Automatic-Reboot "false";' > /etc/apt/apt.conf.d/51unattended-upgrades-local
```

### **Phase 4: Networking (In Progress)**

**Goal:** Configure `vmbr0` to be VLAN-aware and ensure consistent naming logic.

4.1 Identify Physical Interface

Find the active physical port (e.g., eno1, enp3s0).

Bash

```
ip link show
```

4.2 Edit Interface Config

File: /etc/network/interfaces

- **Standard:** `vmbr0` should have `bridge-vlan-aware yes`.
    
- **Alignment:** Ensure `bridge-ports` points to the correct physical interface for that specific hardware.
    

**4.3 Apply Networking**

Bash

```
ifreload -a
# OR
systemctl reload networking
```

---

Ready for the next step?

We need to capture the network config details for Phase 4 to finish aligning opal. Please paste:

1. **Oro:** `cat /etc/network/interfaces`
    
2. **Opal:** `ip link show`
   
   
