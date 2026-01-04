# VLANs & DNS Schema

← [Documentation Index](../index.md)

## VLAN Architecture

| VLAN ID | CIDR | Purpose | Wi‑Fi SSID | Sub‑domain |
|---------|------|---------|------------|------------|
| 1 | 192.168.1.0/24 | Unifi infrastructure | n/a | core.vallery.net |
| 10 | 192.168.10.0/24 | IoT & sensors | devices | devices.vallery.net |
| 20 | 192.168.20.0/24 | PoE Cameras | n/a | cameras.vallery.net |
| 30 | 192.168.30.0/24 | Servers & hosts | n/a | servers.vallery.net |
| 40 | 192.168.40.0/24 | Personal devices | home | home.vallery.net |
| 50 | 192.168.50.0/24 | Guest Wi‑Fi (captive) | guest | guest.vallery.net |
| 60 | 192.168.60.0/24 | Container macvlan | n/a | containers.vallery.net |

## VLAN Purpose & Isolation

### VLAN 1 - Core Infrastructure
- **Purpose**: UniFi controller, switches, and core network services
- **Access**: Management only, no user devices
- **Services**: UDM-Pro, switches, controller

### VLAN 10 - IoT & Sensors
- **Purpose**: Smart home devices, sensors, ESP32 modules
- **Isolation**: No internet access by default, local communication only
- **Devices**: Thermostats, door sensors, environmental monitors
- **Wi-Fi**: `devices` SSID with device-specific PSK

### VLAN 20 - Security Cameras
- **Purpose**: PoE cameras and NVR systems
- **Isolation**: No internet access, local recording only
- **Access**: Frigate NVR on servers VLAN can access
- **Storage**: Direct to NAS on server VLAN

### VLAN 30 - Servers & Infrastructure
- **Purpose**: Docker Swarm nodes, NAS, and infrastructure services
- **Access**: Full internet access for updates and external services
- **Security**: Firewalled, VPN access required for management

### VLAN 40 - Personal Devices
- **Purpose**: Family phones, laptops, tablets
- **Access**: Full internet access
- **Wi-Fi**: `home` SSID with WPA3 encryption
- **Inter-VLAN**: Can access containers VLAN for services

### VLAN 50 - Guest Network
- **Purpose**: Visitor device isolation
- **Access**: Internet only, no local network access
- **Wi-Fi**: `guest` SSID with captive portal
- **Bandwidth**: Limited to prevent abuse

### VLAN 60 - Container Services
- **Purpose**: Docker containers with macvlan networking
- **Access**: Accessible from personal devices VLAN
- **Services**: Home Assistant, Grafana, media servers
- **DNS**: Services advertised via mDNS and static DNS

## DNS Hierarchy

### Domain Structure
```
vallery.net (public domain)
├── core.vallery.net (VLAN 1)
├── devices.vallery.net (VLAN 10)
├── cameras.vallery.net (VLAN 20)
├── servers.vallery.net (VLAN 30)
├── home.vallery.net (VLAN 40)
├── guest.vallery.net (VLAN 50)
└── containers.vallery.net (VLAN 60)
```

### Internal DNS Services
- **Primary DNS**: home1.servers.vallery.net (192.168.30.10)
- **Secondary DNS**: home2.servers.vallery.net (192.168.30.11)
- **External Resolver**: Cloudflare (1.1.1.1, 1.0.0.1)
- **Local Override**: `.local` domains for service discovery

### Static DNS Entries

| FQDN | IP | Service |
|------|----|---------|
| gateway.core.vallery.net | 192.168.1.1 | UDM Pro Max |
| root-switch.core.vallery.net | 192.168.1.200 | Server Closet - ROOT |
| enterprise-switch.core.vallery.net | 192.168.1.42 | Server Closet - Enterprise 24 Port |
| poe-switch.core.vallery.net | 192.168.1.249 | Server Closet - PoE 16 Port |
| studio-bottom.core.vallery.net | 192.168.1.137 | Studio Bottom Switch |
| studio-top.core.vallery.net | 192.168.1.169 | Studio Top Switch |
| home1.servers.vallery.net | 192.168.30.10 | Primary manager |
| nas.servers.vallery.net | 192.168.30.30 | Synology NAS |
| homeassistant.containers.vallery.net | 192.168.60.10 | Home Assistant |
| grafana.containers.vallery.net | 192.168.60.20 | Monitoring |

## Inter-VLAN Routing Rules

### Allowed Traffic
- **Personal → Containers**: Full access to published services
- **Servers → All**: Management and monitoring access
- **Cameras → Servers**: Stream data to Frigate NVR
- **IoT → Servers**: Telemetry data to InfluxDB

### Blocked Traffic
- **Guest → Any Local**: Isolated to internet only
- **IoT → Internet**: Prevents data exfiltration
- **Cameras → Internet**: Local processing only
- **Containers → IoT**: Prevents service compromise from spreading

## Wi-Fi Network Configuration

| SSID | VLAN | Security | Purpose |
|------|------|----------|---------|
| home | 40 | WPA3-Personal | Family devices |
| devices | 10 | WPA2-Personal (device-specific PSK) | IoT devices |
| guest | 50 | Open with captive portal | Visitor access |

### Access Point Placement
- **Main House**: 3x APs covering all floors
- **Suite**: 1x AP for studio and living areas
- **Outdoor**: 2x outdoor APs for yard coverage
- **Garage**: 1x AP for vehicle connectivity

---

**Next**: [WAN & NTP](wan-ntp.md) | **Related**: [Host Mapping](../01_physical/host-map.md)
