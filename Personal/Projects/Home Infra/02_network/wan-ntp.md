# WAN & NTP Configuration

← [Documentation Index](../index.md)

## Dual-WAN Setup

### Primary: Nextlight Fiber
- **Speed**: 2.5 Gbps symmetrical
- **Reliability**: Primary connection for all traffic
- **Latency**: ~5ms to Denver
- **Provider**: Nextlight (Longmont municipal fiber)

### Secondary: Starlink
- **Speed**: Variable (50-200 Mbps down, 10-40 Mbps up)
- **Reliability**: Backup connection for failover
- **Latency**: ~25-60ms (satellite)
- **Provider**: Starlink (SpaceX)

### Tertiary Option: Xfinity (Available)
- **Status**: Wired to server closet but currently unused
- **Speed**: tood: verify available speeds
- **Note**: Can be patched in if needed for additional redundancy
- **Provider**: Comcast Xfinity

### Failover Configuration
- **UDM Pro Max**: Supports primary and secondary WAN only
- **Primary**: Nextlight fiber (2.5 GbE)
- **Secondary**: Starlink via ethernet adapter
- **Detection**: tood: document actual failover settings
- **Recovery**: tood: document failback behavior

## Network Time Protocol (NTP)

### Authoritative Time Source
**tood**: Document actual NTP configuration

- **Primary**: tood: identify actual NTP source
- **Backup Sources**: tood: verify backup NTP servers
- **Configuration**: tood: document NTP setup
- **Precision**: tood: measure actual time accuracy

### NTP Configuration
```
Primary: 192.168.1.100 (Dishy via DNAT)
Backup: pool.ntp.org
Fallback: time.cloudflare.com
```

### Why Starlink for NTP?
1. **GPS-based**: Direct satellite time reference
2. **Always Available**: Independent of internet connectivity
3. **Local Network**: No external dependency for time sync
4. **High Precision**: Better than most internet NTP sources

## Internet Failover Strategy

### Traffic Routing
- **Normal Operation**: All traffic via Nextlight fiber
- **Degraded Service**: Critical services only via Xfinity
- **Full Failover**: All traffic via Xfinity when fiber is down

### Service Prioritization During Failover
1. **Critical**: DNS, NTP, monitoring, alerts
2. **Important**: VPN, SSH, container services
3. **Normal**: Web browsing, streaming
4. **Deferred**: Backups, large downloads, updates

### Monitoring & Alerting
- **Connection Health**: Continuous ping monitoring
- **Bandwidth Usage**: Track utilization on each WAN
- **Failover Events**: Alerts when switching connections
- **Recovery Notification**: Confirm when primary is restored

## External DNS & Dynamic DNS

### Public DNS Records
- **Provider**: Cloudflare DNS
- **Domain**: vallery.net
- **TTL**: 300 seconds for dynamic updates

### Dynamic DNS Updates
- **Service**: Cloudflare API via UDM-Pro
- **Update Frequency**: Every 5 minutes or on IP change
- **Records Updated**:
  - `home.vallery.net` → Current public IP
  - `vpn.vallery.net` → WireGuard endpoint

### External Services
- **VPN Access**: WireGuard on UDM-Pro
- **Remote Management**: SSH via VPN only
- **Monitoring**: External healthcheck endpoints

## WAN Security

### Firewall Rules
- **Default**: Block all inbound traffic
- **VPN Only**: WireGuard port 51820 allowed
- **No Port Forwarding**: All services behind VPN
- **DDoS Protection**: Rate limiting on WAN interfaces

### Intrusion Detection
- **IDS/IPS**: UniFi Threat Management enabled
- **Geo-blocking**: Block traffic from high-risk countries
- **Malware Filtering**: DNS-based blocking of known bad domains

---

**Next**: [WiFi Networks](wifi.md) | **Related**: [VLANs & DNS](vlan-dns.md)
