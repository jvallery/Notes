# Host Mapping

← [Documentation Index](../index.md)

## Host-to-Location Matrix

| Host | Room | UPS | Swarm Role | GPU | Power Source |
|------|------|-----|------------|-----|--------------|
| home1 | Server Closet - Main House | CyberPower OR500LCDRM1U | manager | AMD Vega 8 | Main House (backed) |
| home2 | Compute Rack - Basement | CyberPower OR2200LCDRT2U | manager | Intel UHD 605 | Main House (backed) |
| home3 | Studio - Suite Side | CyberPower OR500LCDRM1U | manager | Intel UHD 600 | Suite (backed) |
| oro | Compute Rack - Basement | CyberPower OR2200LCDRT2U | worker | RTX 3060 | Pool/GPU (non-backed) |
| opal | Compute Rack - Basement | CyberPower OR2200LCDRT2U | worker | RTX 4070 Ti SUPER | Pool/GPU (non-backed) |
| onyx | Compute Rack - Basement | CyberPower OR2200LCDRT2U | worker | RTX 4070 Ti SUPER | Pool/GPU (non-backed) |
| obsidian | Compute Rack - Basement | CyberPower OR2200LCDRT2U | storage | no | Suite (backed) |

## Manager Node Distribution

The 3-node manager quorum is distributed across physical locations for high availability:

- **home1**: Server Closet (primary networking location)
- **home2**: Compute Rack (co-located with storage and workers)
- **home3**: Studio (geographically separated backup location)

This ensures the Docker Swarm cluster can survive:
- Loss of any single room/location
- Power outage to any single electrical circuit
- UPS failure in any single location

## GPU Worker Configuration

All GPU workers are co-located in the Compute Rack for:
- **Thermal Management**: Basement location provides cooling
- **Power Efficiency**: Shared high-capacity UPS
- **Storage Access**: Direct connection to NAS and local NVMe
- **Maintenance**: Centralized physical access

## Storage Architecture

### Local Storage (per host)
- **home1**: 500 GiB NVMe (Samsung 990 EVO Plus) for OS + container data
- **home2**: 256 GiB NVMe (Kingston OM8PCP3) for OS + container data
- **home3**: 256 GiB NVMe (Kingston OM8PCP3) for OS + container data
- **Workers**: 3×1 TiB NVMe (Samsung 990 EVO Plus) for OS + storage

### Shared Storage (NAS)
- **obsidian**: Synology NAS providing NFS exports
- **Location**: Compute Rack for direct worker access
- **Backup**: PowerWall+ backed power for data protection

## Power Distribution Strategy

| Circuit Type | Hosts | Rationale |
|--------------|-------|-----------|
| **PowerWall+ Backed** | home1, home2, home3, obsidian | Critical management and storage nodes |
| **Non-Backed** | oro, opal, onyx | GPU workers can restart after power restoration |

This design ensures:
- Management plane survives extended outages
- Storage remains available during outages
- Compute workloads resume automatically when power returns
- Cost optimization (UPS sizing vs. PowerWall+ capacity)

## Network Addressing

Each host receives a static IP on VLAN 30 (servers):

| Host | IP Address | MAC Address | Notes |
|------|------------|-------------|-------|
| home1 | 192.168.30.10 | TBD | Primary DNS, NGINX |
| home2 | 192.168.30.11 | TBD | Backup management |
| home3 | 192.168.30.12 | TBD | Studio management |
| oro | 192.168.30.20 | TBD | GPU worker 1 |
| opal | 192.168.30.21 | TBD | GPU worker 2 |
| onyx | 192.168.30.22 | TBD | GPU worker 3 |
| obsidian | 192.168.30.30 | TBD | NAS storage |

---

**Next**: [VLANs & DNS](../02_network/vlan-dns.md) | **Related**: [Room Layout](rooms.md)
