# Comprehensive VLAN Networking Configuration

## Overview

This implementation provides comprehensive multi-VLAN networking support for the home infrastructure, addressing the critical netplan management issues and implementing all required VLAN networks.

## VLAN Architecture

The system supports four distinct VLAN networks:

### VLAN 10 - IoT Devices Network (192.168.10.0/24)
- **Purpose**: IoT device connectivity
- **Security**: Isolated from other networks with inbound traffic blocked
- **Configuration**: Only enabled on hosts with `base_os_iot_devices: true`
- **Gateway**: 192.168.10.1

### VLAN 30 - Server Management Network (192.168.30.0/24)
- **Purpose**: Server management and administration
- **Security**: SSH and HTTPS access allowed
- **Configuration**: Enabled on all hosts
- **Gateway**: 192.168.30.1

### VLAN 31 - Ceph Cluster Network (192.168.31.0/24)
- **Purpose**: Ceph-to-Ceph cluster communication
- **Security**: Cluster-only traffic, no gateway
- **Configuration**: Auto-enabled for hosts with `ceph_role` defined
- **Gateway**: None (cluster-only)

### VLAN 60 - Container Overlay Network (192.168.60.0/24)
- **Purpose**: Container-to-container communication
- **Security**: Container traffic allowed, limited server access
- **Configuration**: Enabled for hosts with `containers_ip` defined
- **Gateway**: 192.168.60.1

## File Structure

```
ansible/roles/base_os/
├── tasks/
│   ├── network.yml                     # Consolidated networking and firewall configuration
│   └── hardening.yml                   # OS security hardening (non-networking)
├── templates/
│   └── netplan.yaml.j2                 # Comprehensive netplan template
├── handlers/
│   └── main.yml                        # Enhanced netplan handlers
├── defaults/
│   └── main.yml                        # VLAN configuration defaults
├── examples/
│   └── host_vars_example.yml           # Example host configuration
└── files/
    └── validate_vlan_networking.sh     # Validation script
```

## Key Features

### 1. Intelligent Interface Detection
- Automatically detects primary network interface
- Falls back through multiple detection methods
- Handles various interface naming schemes (eth0, ens3, ens160, etc.)

### 2. Consolidated Netplan Management
- **Fixes B-1 Critical Issue**: Single netplan file approach
- Removes all existing netplan configurations before deployment
- Comprehensive error handling and validation

### 3. Flexible VLAN Assignment
- Host-specific IP assignment via inventory variables
- Automatic IP calculation for Ceph clusters
- Conditional VLAN enablement per host

### 4. Enhanced Security
- UFW firewall integration with VLAN-specific rules
- IoT network isolation
- Server management network access controls
- Cluster-only communication for Ceph

### 5. Performance Optimizations
- Jumbo frames support for Ceph networks
- Advanced TCP congestion control (BBR)
- Optimized kernel parameters for multi-VLAN setups

## Configuration Methods

### Method 1: Inventory Variables (Recommended)
Configure host-specific IPs in `inventories/prod/host_vars/hostname.yml`:

```yaml
# Server management network (required for all hosts)
servers_ip: "192.168.30.100"

# Ceph cluster network (for Ceph nodes)
ceph_cluster_ip: "192.168.31.100"

# Container network (for container hosts)
containers_ip: "192.168.60.100"

# IoT management (for gateway hosts)
base_os_iot_devices: true
iot_devices_ip: "192.168.10.1"
```

### Method 2: Automatic Assignment
For Ceph clusters, IPs can be auto-calculated:

```yaml
ceph_role: "storage"
ceph_host_id: 10  # Results in 192.168.31.10
```

## Firewall Rules

The implementation includes comprehensive UFW rules:

- **SSH Access**: Allowed from server management network (VLAN 30)
- **HTTPS Access**: Allowed from server management network
- **IoT Isolation**: IoT devices blocked from all other networks
- **Ceph Communication**: Full cluster communication on VLAN 31
- **Container Access**: Containers can reach server services on specific ports

## Critical Fixes Implemented

### B-1: Conflicting Netplan Management
- **Problem**: Multiple netplan files causing conflicts
- **Solution**: Remove all existing configs, deploy single comprehensive file
- **File**: `/etc/netplan/01-static.yaml` (single source of truth)

### Error Handling
- **Validation**: `netplan try` before applying changes
- **Connectivity**: Verify gateway reachability after changes
- **Rollback**: Automatic rollback on validation failure
- **VLAN Verification**: Check all VLAN interfaces are operational

### Performance
- **BBR Congestion Control**: For improved cluster performance
- **Kernel Optimizations**: Network buffer and queue optimizations
- **RPF Configuration**: Proper reverse path filtering for multi-VLAN

## Deployment

### Enable Comprehensive Networking
The role now uses the comprehensive networking by default. To deploy:

```bash
ansible-playbook -i inventories/prod site.yml --tags networking
```

### Validation Commands
After deployment, verify the configuration:

```bash
# Check netplan configuration
sudo netplan get

# Verify VLAN interfaces
ip link show | grep vlan

# Check firewall rules
sudo ufw status verbose

# Test connectivity
ping -c 3 192.168.30.1  # Server gateway
ping -c 3 192.168.10.1  # IoT gateway (if enabled)
```

## Migration from Legacy Configuration

The new implementation automatically:
1. Removes legacy `ifupdown` packages
2. Cleans up old netplan configurations
3. Deploys comprehensive configuration
4. Applies proper firewall rules

No manual intervention required for migration.

## Troubleshooting

### Common Issues

1. **Interface Detection Fails**
   - Check: `ip link show`
   - Solution: Set `primary_interface` variable manually

2. **VLAN Not Created**
   - Check: Host has appropriate `*_ip` variable set
   - Check: VLAN kernel module loaded (`lsmod | grep 8021q`)

3. **Connectivity Lost**
   - Check: Gateway configuration in infrastructure.yml
   - Check: Firewall rules with `sudo ufw status`

4. **Netplan Apply Fails**
   - Check: `/etc/netplan/01-static.yaml` syntax
   - Run: `sudo netplan try` for validation

### Debug Commands

```bash
# View current network configuration
ip addr show
ip route show

# Check netplan status
sudo netplan status

# Validate configuration
sudo netplan try --timeout=10

# Check firewall logs
sudo tail -f /var/log/ufw.log
```

## Future Enhancements

- Support for additional VLAN networks
- Dynamic VLAN assignment via DHCP reservations
- Integration with network monitoring
- Advanced QoS configuration per VLAN
- IPv6 support for all VLANs
