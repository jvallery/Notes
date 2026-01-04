# WiFi Networks

← [Documentation Index](../index.md)

## SSID Configuration

| SSID | VLAN | Security | Band | Purpose |
|------|------|----------|------|---------|
| home | 40 | WPA3-Personal | 2.4/5/6 GHz | Family devices |
| devices | 10 | WPA2-Personal | 2.4/5 GHz | IoT devices |
| guest | 50 | Open + Captive Portal | 2.4/5 GHz | Visitor access |

## Network Details

### Home Network (Primary)
- **SSID**: `home`
- **VLAN**: 40 (Personal devices)
- **Security**: WPA3-Personal with 802.11w (PMF)
- **Bands**: 2.4 GHz, 5 GHz, 6 GHz (WiFi 6E)
- **Devices**: Family phones, laptops, tablets, smart TVs
- **Internet**: Full access
- **Local Access**: Can reach container services (VLAN 60)

### IoT Device Network
- **SSID**: `devices`
- **VLAN**: 10 (IoT & sensors)
- **Security**: WPA2-Personal (legacy device compatibility)
- **Bands**: 2.4 GHz, 5 GHz
- **Devices**: Smart thermostats, ESP32 modules, sensors
- **Internet**: Blocked (local communication only)
- **Isolation**: Cannot reach other VLANs except servers for telemetry

### Guest Network
- **SSID**: `guest`
- **VLAN**: 50 (Guest isolation)
- **Security**: Open with captive portal
- **Bands**: 2.4 GHz, 5 GHz
- **Access**: Internet only, no local network access
- **Bandwidth**: Limited to 100 Mbps total
- **Time Limit**: 24-hour access tokens

## Access Point Deployment

### WiFi 6E Coverage (Latest Technology)
- **Suite Office**: U7 Pro Wall (192.168.1.223)
  - Coverage: Office workspace with highest performance
  - 6 GHz band: 160 MHz channel width for maximum throughput

### WiFi 6 Coverage (Primary Network)
- **Master Suite**: U6 LR (192.168.1.96) - Primary bedroom coverage
- **Basement**: U6 LR (192.168.1.62) - Compute rack and basement areas
- **Server Closet**: U6 LR (192.168.1.49) - Infrastructure monitoring
- **Workshop**: U6 LR (192.168.1.110) - Workshop and utility areas
- **Girl's Room**: U6 LR (192.168.1.114) - Bedroom coverage
- **Garage**: U6 LR (192.168.1.213) - Garage and outdoor extension

### Legacy Coverage (AC Mesh)
- **AC Mesh Units**: 4 outdoor/extended range units
  - **Patio**: 192.168.1.227 - Outdoor entertainment area
  - **Driveway**: 192.168.1.147 - Vehicle and entrance coverage
  - **AC Mesh**: 192.168.1.38, 192.168.1.81 - Additional coverage zones

### Coverage Strategy
```
Main House:
├── Master Suite: Primary bedroom (U6 LR)
├── Girl's Room: Secondary bedroom (U6 LR)
├── Server Closet: Infrastructure area (U6 LR)
└── Basement: Compute rack area (U6 LR)

Studio/Suite:
├── Suite Office: High-performance workspace (U7 Pro Wall)
└── Workshop: Utility and project area (U6 LR)

Outdoor:
├── Garage: Vehicle connectivity (U6 LR)
├── Patio: Entertainment area (AC Mesh)
├── Driveway: Entrance coverage (AC Mesh)
└── Extended Areas: Additional AC Mesh units
```

## Client Device Management

### Device Categories
- **Personal**: Phones, laptops, tablets → `home` SSID
- **IoT**: Sensors, switches, hubs → `devices` SSID
- **Cameras**: PoE wired (no WiFi)
- **Guests**: Temporary devices → `guest` SSID

### Connection Optimization
- **Band Steering**: Prefer 5/6 GHz for capable devices
- **Load Balancing**: Distribute clients across APs
- **Fast Roaming**: 802.11r for seamless handoffs
- **Beam Forming**: Directional signal optimization

## Guest Access Portal

### Captive Portal Features
- **Authentication**: Self-service access codes
- **Time Limits**: 24-hour default, custom durations available
- **Bandwidth**: Per-device and total limits
- **Content Filtering**: Basic malware/phishing protection
- **Usage Tracking**: Anonymous bandwidth monitoring

### Guest Management
- **Access Codes**: Generated via UniFi controller or mobile app
- **Scheduling**: Time-based access (e.g., during events)
- **Revocation**: Immediate access termination capability
- **Audit Trail**: Connection logs for security purposes

## Performance & Optimization

### Channel Planning
- **2.4 GHz**: Channels 1, 6, 11 (non-overlapping)
- **5 GHz**: DFS channels enabled for additional spectrum
- **6 GHz**: All available channels (WiFi 6E)
- **Power**: Optimized for coverage without interference

### Quality of Service (QoS)
1. **Priority 1**: Voice/video calls, real-time communication
2. **Priority 2**: Interactive applications, web browsing
3. **Priority 3**: Streaming media, large downloads
4. **Priority 4**: Bulk transfers, backups

### Monitoring Metrics
- **Signal Strength**: Target -65 dBm or better
- **Channel Utilization**: Keep below 60%
- **Client Count**: Max 25 devices per AP
- **Throughput**: Monitor for degradation

---

**Next**: [Host Configuration](../03_compute-storage/hosts.md) | **Related**: [VLANs & DNS](vlan-dns.md)
