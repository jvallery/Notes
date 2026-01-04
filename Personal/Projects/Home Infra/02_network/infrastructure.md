# Network Infrastructure

← [Documentation Index](../index.md)

## Unifi Network Overview

The network infrastructure consists of a UDM Pro Max as the core gateway with a hierarchical switch topology providing connectivity across the 17,000 sq ft estate and 1.5 acre lot. All devices are managed through the integrated Unifi Controller.

### Core Gateway
- **UDM Pro Max**: Primary gateway, firewall, and network controller
- **Management IP**: 192.168.1.1
- **Uplink**: 2.5 GbE to Longmont Power & Communications (ISP)
- **Model**: UDM Pro Max
- **Firmware**: 4.3.6

## Switch Infrastructure

**tood**: Document actual switch configuration and locations

### Unifi Managed Switches
Based on Unifi controller data:

| Device Name | Model | Location | IP Address | Purpose |
|-------------|-------|----------|------------|---------|
| Server Closet - ROOT | US 24 | Server Closet | 192.168.1.200 | Primary distribution |
| Server Closet - Enterprise 24 Port | USW Enterprise 24 PoE | Server Closet | 192.168.1.42 | PoE distribution |
| Server Closet - PoE 16 Port | USW 24 PoE | Server Closet | 192.168.1.249 | Additional PoE |
| Studio Bottom | USW 24 PoE | Studio/Suite | 192.168.1.137 | Studio distribution |
| Studio Top | USW 24 PoE | Studio/Suite | 192.168.1.169 | Extended studio |

### Non-Unifi Switches (10 GbE)
| Location | Model | Purpose | Management |
|----------|-------|---------|------------|
| Server Closet | Netgear (tood: model) | 10 GbE backbone | Unmanaged |
| Basement Compute Rack | Netgear (tood: model) | 10 GbE worker connections | Unmanaged |

**tood**: Document exact switch models, port assignments, and physical connections

## Access Point Deployment

**tood**: Document actual access point locations and configurations

Based on Unifi controller data, the following APs are deployed:

### WiFi 6E Access Points
| Device Name | Model | Location | IP Address | Notes |
|-------------|-------|----------|------------|-------|
| Suite Office | U7 Pro Wall | Suite Office | 192.168.1.223 | Latest technology |

### WiFi 6 Access Points
| Device Name | Model | Location | IP Address | Notes |
|-------------|-------|----------|------------|-------|
| Basement | U6 LR | Basement | 192.168.1.62 | Compute rack area |
| Master Suite | U6 LR | Master Suite | 192.168.1.96 | Primary bedroom |
| Server Closet | U6 LR | Server Closet | 192.168.1.49 | Infrastructure area |
| Workshop | U6 LR | Workshop | 192.168.1.110 | Workshop area |
| Girl's Room | U6 LR | Girl's Room | 192.168.1.114 | Bedroom coverage |
| Garage | U6 LR | Garage | 192.168.1.213 | Garage area |

### Legacy Access Points (AC Mesh)
| Device Name | Model | Location | IP Address | Notes |
|-------------|-------|----------|------------|-------|
| AC Mesh | AC Mesh | tood: location | 192.168.1.38 | Extended coverage |
| AC Mesh | AC Mesh | tood: location | 192.168.1.81 | Extended coverage |
| Patio | AC Mesh | Patio | 192.168.1.227 | Outdoor coverage |
| Driveway | AC Mesh | Driveway | 192.168.1.147 | Driveway coverage |

**tood**:
- Verify exact physical locations for all APs
- Document channel assignments and power levels
- Map actual coverage areas
- Document cable runs and uplink connections

## Network Topology

**tood**: Document actual network topology and connections

### Physical Hierarchy (Known)
```
ISP (Longmont Power & Com)
    ↓ 2.5 GbE
UDM Pro Max (192.168.1.1)
    ↓ tood: verify connection
Server Closet - ROOT (192.168.1.200)
    ├── tood: verify port assignments to other switches
    └── tood: document 10 GbE Netgear switch connections
```

### Additional Infrastructure
- **10 GbE Network**: Separate Netgear switches in server closet and basement
- **Cross-Connect**: 10 GbE + 1 GbE redundant paths between locations
- **Worker Connections**: 10 GbE to oro, opal, onyx via Netgear switches
- **NAS Connection**: 10 GbE to Synology obsidian

**tood**:
- Map exact physical connections
- Document port assignments on all switches
- Verify 10 GbE network topology
- Document cable management and labeling

## Channel Planning

**tood**: Document actual WiFi channel assignments

Based on Unifi controller data, but needs verification:

### 2.4 GHz Band Distribution
**tood**: Verify these channel assignments in practice

### 5 GHz Band Distribution
**tood**: Document actual 5 GHz channel plan

### 6 GHz Band (WiFi 6E)
**tood**: Verify 6 GHz configuration on U7 Pro Wall

**Note**: Channel information above was extracted from controller but should be verified and optimized based on actual RF environment and interference patterns.

## Management & Monitoring

### Device Status
- **All Devices**: Up to date firmware
- **Management**: Centralized through UDM Pro Max controller
- **Monitoring**: Real-time performance and client tracking
- **Updates**: Automatic firmware updates enabled

### MAC Address Reference
| Device | MAC Address | Model |
|--------|-------------|-------|
| UDM Pro Max | 0c:ea:14:c7:8c:29 | UDM Pro Max |
| Server Closet - ROOT | 18:eb:29:b6:27:16 | US 24 |
| Server Closet - Enterprise | 68:d7:9a:68:23:53 | USW Enterprise 24 PoE |
| Studio Bottom | 70:a7:41:98:7b:0d | USW 24 PoE |
| Studio Top | d0:21:f9:48:6c:93 | USW 24 PoE |
| Server Closet - PoE 16 | d0:21:f9:41:19:32 | USW 24 PoE |

## Network Performance

### Bandwidth Allocation
- **ISP Connection**: 2.5 Gb symmetrical fiber (Nextlight primary)
- **Backup Internet**: Starlink (secondary via UDM Pro Max)
- **Tertiary Option**: Xfinity available in server closet (unused, can be patched)
- **Server Closet ↔ Basement**: 10 GbE (Netgear switches) + 1 GbE backup (Unifi)
- **Server Closet ↔ Studio**: 1 GbE (Unifi managed)
- **WiFi 6E**: Up to 2.4 Gbps (6 GHz band)
- **WiFi 6**: Up to 1.2 Gbps (5 GHz band)
- **Legacy AC**: Up to 866 Mbps (5 GHz band)

### Additional 10GbE Infrastructure
- **Server Closet**: Netgear 10GbE switch (unmanaged by Unifi)
- **Basement Compute Rack**: Netgear 10GbE switch (unmanaged by Unifi)
- **Synology NAS**: 10 GbE connection (not 1 GbE)
- **Cross-Connect**: 10 GbE link between server closet and basement rack

### Coverage Areas
- **Total Coverage**: ~17,000 sq ft and 1.5 acres
- **Indoor APs**: 8 devices
- **Outdoor APs**: 4 devices
- **Redundancy**: Overlapping coverage in critical areas

---

**Next**: [VLANs & DNS](vlan-dns.md) | **Related**: [WiFi Networks](wifi.md)
