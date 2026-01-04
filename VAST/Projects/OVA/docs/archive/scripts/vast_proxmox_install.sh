#!/bin/bash
#
# VAST Data 5.4 - Proxmox Complete Installation Script
# 
# This script handles the complete installation of VAST Data virtual appliance
# on Proxmox/KVM environment. It automatically handles all prerequisites including
# Docker installation and group membership.
#
# Usage:
#   chmod +x vast_proxmox_install.sh
#   ./vast_proxmox_install.sh
#
# After successful installation:
#   - VMS Web UI: https://<mgmt_ip>
#   - Credentials: admin / 123456
#   - vCLI: /vast/data/11.0.0.1-4100/vms.sh vcli
#
# Version: 1.0
# Date: December 29, 2025
#

set -e

# ============================================================================
# CONFIGURATION
# ============================================================================
export BUILD=release-5-4-0-2043819
export PIPE=$(echo $BUILD | awk -F'-' '{print $NF}')
export DISABLE_IPV6_FOR_LOOPBACK=yes
export VAST_INSTALL_ARGS='--vsettings CAS_OVER_RPC=true,IN_CLUSTER_COMMUNICATION_TCP=true'
export VMAN_USER_PASSWORD='-u admin -p 123456'
export pem_file=/vast/deploy/ssh_key.pem
export EXTRA_VOLUME_MOUNTS="-v /file_server:/file_server"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Log file
LOGFILE="/home/centos/vast_install_$(date +%Y%m%d_%H%M%S).log"

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

log() {
    local level=$1
    shift
    local message="$@"
    local timestamp=$(date '+%Y-%m-%d %H:%M:%S')
    
    case $level in
        INFO)  echo -e "${GREEN}[INFO]${NC} $message" ;;
        WARN)  echo -e "${YELLOW}[WARN]${NC} $message" ;;
        ERROR) echo -e "${RED}[ERROR]${NC} $message" ;;
        STEP)  echo -e "\n${BLUE}==>${NC} ${BLUE}$message${NC}" ;;
    esac
    
    echo "[$timestamp] [$level] $message" >> "$LOGFILE"
}

check_root() {
    if [ "$EUID" -eq 0 ]; then
        log ERROR "Do not run this script as root. Run as 'centos' user."
        exit 1
    fi
}

check_docker_access() {
    # Returns 0 if docker is accessible without sudo
    docker ps &>/dev/null
    return $?
}

wait_for_cluster_state() {
    local target_state=$1
    local timeout=$2
    local elapsed=0
    local interval=30
    
    log INFO "Waiting for cluster to reach state: $target_state (timeout: ${timeout}s)"
    
    while [ $elapsed -lt $timeout ]; do
        local state=$(curl -k -s "https://$MGMT_IP/api/clusters/1/" -u admin:123456 2>/dev/null | \
            python3 -c "import sys,json; print(json.load(sys.stdin).get('state','UNKNOWN'))" 2>/dev/null || echo "UNKNOWN")
        
        log INFO "Cluster state: $state (elapsed: ${elapsed}s)"
        
        if [ "$state" == "$target_state" ]; then
            return 0
        fi
        
        sleep $interval
        elapsed=$((elapsed + interval))
    done
    
    return 1
}

# ============================================================================
# DOCKER GROUP HANDLING
# ============================================================================

# Check if we need to re-exec with docker group
handle_docker_group() {
    # If docker command works, we're good
    if check_docker_access; then
        log INFO "Docker access confirmed ✓"
        return 0
    fi
    
    # Check if docker is even installed
    if ! command -v docker &>/dev/null; then
        # Docker not installed yet, will be handled later
        return 0
    fi
    
    # Docker is installed but we can't access it
    # Check if user is in docker group in /etc/group
    if grep -q "^docker:.*:$(whoami)" /etc/group 2>/dev/null || \
       grep -q "^docker:.*:.*$(whoami)" /etc/group 2>/dev/null; then
        # User is in docker group but session doesn't have it
        # Re-exec this script with sg to get group membership
        log INFO "Re-executing script with docker group membership..."
        exec sg docker -c "$0 --docker-group-active"
    else
        log ERROR "User is not in docker group. This should not happen."
        exit 1
    fi
}

# Check for re-exec flag
if [ "$1" == "--docker-group-active" ]; then
    log INFO "Running with docker group active"
    shift
fi

# ============================================================================
# MAIN INSTALLATION
# ============================================================================

echo ""
echo "=============================================="
echo "VAST Data 5.4 - Proxmox Installation Script"
echo "=============================================="
echo ""
echo "Log file: $LOGFILE"
echo ""

# Ensure we're not root
check_root

# ============================================================================
# PHASE 1: SYSTEM CHECKS
# ============================================================================

log STEP "Phase 1: System checks"

# Determine management interface
export MGMT_IP=$(hostname -I | awk '{print $1}')
export MGMT_IFACE_NAME=$(ip -o -4 addr show | grep "$MGMT_IP" | awk '{print $2}')

log INFO "Management IP: $MGMT_IP"
log INFO "Management Interface: $MGMT_IFACE_NAME"

# Check CPU cores
CORES=$(nproc)
if [ $CORES -lt 24 ]; then
    log WARN "Only $CORES CPU cores available (24 minimum, 32 recommended)"
else
    log INFO "CPU cores: $CORES ✓"
fi

# Check memory - CRITICAL: 112GB+ required to avoid OOM during cluster activation
TOTAL_MEM_GB=$(free -g | awk '/^Mem:/{print $2}')
if [ "$TOTAL_MEM_GB" -lt 112 ]; then
    log ERROR "CRITICAL: Only ${TOTAL_MEM_GB}GB RAM available!"
    log ERROR "The loopback cluster requires 112GB+ RAM during initialization."
    log ERROR "With less memory, the OOM killer will terminate processes during"
    log ERROR "system_format, leaving the cluster in an unrecoverable INIT state."
    log ERROR ""
    log ERROR "Please allocate at least 112GB RAM to this VM before proceeding."
    echo ""
    read -p "Continue anyway? (y/N): " confirm
    if [[ ! "$confirm" =~ ^[Yy]$ ]]; then
        log INFO "Aborting. Increase VM memory and try again."
        exit 1
    fi
    log WARN "Proceeding despite insufficient memory - cluster may fail!"
elif [ "$TOTAL_MEM_GB" -lt 128 ]; then
    log WARN "${TOTAL_MEM_GB}GB RAM available (128GB recommended for safety margin)"
else
    log INFO "Memory: ${TOTAL_MEM_GB}GB ✓"
fi

# Check disk space
AVAIL_DISK_GB=$(df -BG / | awk 'NR==2 {print $4}' | tr -d 'G')
if [ "$AVAIL_DISK_GB" -lt 500 ]; then
    log WARN "Only ${AVAIL_DISK_GB}GB disk space available (1TB recommended)"
else
    log INFO "Disk space: ${AVAIL_DISK_GB}GB ✓"
fi

# Check virtualization
VIRT_TYPE=$(systemd-detect-virt 2>/dev/null || echo "unknown")
if [ "$VIRT_TYPE" != "kvm" ]; then
    log WARN "Detected virtualization: $VIRT_TYPE (expected: kvm)"
else
    log INFO "Virtualization: KVM/Proxmox ✓"
fi

# Check VAST bundle
if [ ! -f /vast/bundles/vastdata_release_*.vast.tar.gz ]; then
    log ERROR "VAST bundle not found in /vast/bundles/"
    log ERROR "Expected: /vast/bundles/vastdata_release_*.vast.tar.gz"
    exit 1
fi
log INFO "VAST bundle found ✓"

if [ ! -f /vast/bundles/vast_bootstrap.sh ]; then
    log ERROR "Bootstrap script not found: /vast/bundles/vast_bootstrap.sh"
    exit 1
fi
log INFO "Bootstrap script found ✓"

# ============================================================================
# PHASE 2: INSTALL DOCKER
# ============================================================================

log STEP "Phase 2: Docker installation"

if ! command -v docker &>/dev/null; then
    log INFO "Installing Docker CE..."
    sudo yum install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin 2>&1 | tee -a "$LOGFILE"
    
    log INFO "Enabling and starting Docker..."
    sudo systemctl enable docker
    sudo systemctl start docker
    
    log INFO "Adding user to docker group..."
    sudo usermod -aG docker centos
    
    log INFO "Docker installed ✓"
    
    # Re-exec with docker group
    log INFO "Re-executing script with docker group membership..."
    exec sg docker -c "$0 --docker-group-active"
else
    log INFO "Docker already installed ✓"
fi

# Ensure docker is running
if ! systemctl is-active --quiet docker; then
    log INFO "Starting Docker service..."
    sudo systemctl start docker
fi

# Handle docker group if needed
handle_docker_group

# Verify docker access
if ! check_docker_access; then
    log ERROR "Cannot access Docker. Please logout and login, then run this script again."
    exit 1
fi

log INFO "Docker is accessible ✓"

# ============================================================================
# PHASE 3: INSTALL QEMU GUEST AGENT
# ============================================================================

log STEP "Phase 3: Proxmox integration"

# Install qemu-guest-agent for Proxmox integration
if ! rpm -q qemu-guest-agent &>/dev/null; then
    log INFO "Installing qemu-guest-agent..."
    sudo yum install -y qemu-guest-agent 2>&1 | tee -a "$LOGFILE"
    sudo systemctl enable qemu-guest-agent
    sudo systemctl start qemu-guest-agent
    log INFO "qemu-guest-agent installed ✓"
else
    log INFO "qemu-guest-agent already installed ✓"
fi

# Disable VMware tools (not needed on Proxmox)
if systemctl is-enabled --quiet vmtoolsd 2>/dev/null; then
    log INFO "Disabling VMware tools (not needed on Proxmox)..."
    sudo systemctl disable vmtoolsd
    sudo systemctl stop vmtoolsd 2>/dev/null || true
    log INFO "VMware tools disabled ✓"
fi

# ============================================================================
# PHASE 4: CONFIGURE NETWORKING
# ============================================================================

log STEP "Phase 4: Network configuration"

# Disable IPv6 on management interface
echo 1 | sudo tee /proc/sys/net/ipv6/conf/$MGMT_IFACE_NAME/disable_ipv6 >/dev/null
log INFO "IPv6 disabled on $MGMT_IFACE_NAME ✓"

# Configure firewall if active
if command -v firewall-cmd &>/dev/null && systemctl is-active --quiet firewalld; then
    log INFO "Configuring firewall..."
    sudo firewall-cmd --permanent --add-port=443/tcp 2>/dev/null || true
    sudo firewall-cmd --permanent --add-port=80/tcp 2>/dev/null || true
    sudo firewall-cmd --permanent --add-port=5000/tcp 2>/dev/null || true
    sudo firewall-cmd --permanent --add-port=2049/tcp 2>/dev/null || true
    sudo firewall-cmd --permanent --add-port=111/tcp 2>/dev/null || true
    sudo firewall-cmd --permanent --add-port=111/udp 2>/dev/null || true
    sudo firewall-cmd --reload 2>/dev/null || true
    log INFO "Firewall configured ✓"
else
    log INFO "Firewall not active, skipping ✓"
fi

# ============================================================================
# PHASE 5: PREPARE VAST DIRECTORIES
# ============================================================================

log STEP "Phase 5: Preparing VAST directories"

# Create required directories
sudo mkdir -p /file_server /vast/bundles /vast/deploy /vast/data /vast/vman/vms/log
sudo chown -R centos:centos /file_server /vast
chmod 755 /vast /vast/*

log INFO "Directories created ✓"

# Set up local registry cache (prevents AWS ECR access attempts)
echo "vastdata.registry.local:5000" > /file_server/DCACHE
log INFO "Local registry cache configured ✓"

# Add registry to /etc/hosts proactively
# The registry runs on 11.0.0.1 (dummy0 interface)
if ! grep -q "vastdata.registry.local" /etc/hosts; then
    log INFO "Adding registry DNS entry to /etc/hosts..."
    echo "11.0.0.1 vastdata.registry.local" | sudo tee -a /etc/hosts >/dev/null
fi
log INFO "Registry DNS configured ✓"

# Configure Docker insecure registry
DOCKER_DAEMON_FILE="/etc/docker/daemon.json"
if [ ! -f "$DOCKER_DAEMON_FILE" ] || ! grep -q "vastdata.registry.local" "$DOCKER_DAEMON_FILE" 2>/dev/null; then
    log INFO "Configuring Docker for local registry..."
    echo '{ "insecure-registries": ["vastdata.registry.local:5000"] }' | sudo tee "$DOCKER_DAEMON_FILE" >/dev/null
    sudo systemctl restart docker
    sleep 3
fi
log INFO "Docker registry configuration ✓"

# Set up OS release file
echo '1.1.1' | sudo tee /etc/vast-os-release >/dev/null
sudo chmod 644 /etc/vast-os-release
log INFO "VAST OS release configured ✓"

# ============================================================================
# PHASE 6: SET UP SSH KEYS
# ============================================================================

log STEP "Phase 6: SSH key setup"

if [ ! -f "$pem_file" ]; then
    log INFO "Setting up SSH keys..."
    rsa_file=~/.ssh/id_rsa
    
    # Create .ssh directory if needed
    mkdir -p ~/.ssh
    chmod 700 ~/.ssh
    
    # Generate key if needed
    if [ ! -f "$rsa_file" ]; then
        ssh-keygen -f $rsa_file -q -N ""
    fi
    
    # Add to authorized_keys
    if ! grep -q "$(cat $rsa_file.pub)" ~/.ssh/authorized_keys 2>/dev/null; then
        cat $rsa_file.pub >> ~/.ssh/authorized_keys
    fi
    chmod 600 ~/.ssh/authorized_keys
    
    # Copy to pem file location
    sudo mkdir -p /vast/deploy
    sudo cp $rsa_file $pem_file
    sudo chown centos:centos $pem_file
    chmod 600 $pem_file
    
    log INFO "SSH keys configured ✓"
else
    log INFO "SSH keys already exist ✓"
fi

# ============================================================================
# PHASE 7: CLEAN UP PREVIOUS INSTALL (if any)
# ============================================================================

log STEP "Phase 7: Cleaning up any previous installation"

# Stop existing VAST containers (except registry)
log INFO "Stopping existing VAST containers..."
docker ps -aq --format "{{.ID}} {{.Names}}" 2>/dev/null | \
    grep -v " registry" | cut -d' ' -f 1 | \
    xargs --no-run-if-empty docker stop 2>/dev/null || true
docker ps -aq --format "{{.ID}} {{.Names}}" 2>/dev/null | \
    grep -v " registry" | cut -d' ' -f 1 | \
    xargs --no-run-if-empty docker rm 2>/dev/null || true

# Clear hugepages
echo 0 | sudo tee /proc/sys/vm/nr_hugepages >/dev/null
log INFO "Hugepages cleared ✓"

log INFO "Cleanup complete ✓"

# ============================================================================
# PHASE 8: RUN VAST BOOTSTRAP
# ============================================================================

log STEP "Phase 8: Running VAST bootstrap"
log INFO "This will take 10-20 minutes. Please wait..."

cd /vast/bundles/

# Run bootstrap
./vast_bootstrap.sh --interface ${MGMT_IP} --skip-prompt 2>&1 | tee -a "$LOGFILE"

log INFO "Bootstrap completed ✓"

# ============================================================================
# PHASE 9: CREATE LOOPBACK CLUSTER
# ============================================================================

log STEP "Phase 9: Creating loopback cluster"

# Create loopback configuration
cat << EOF > /vast/deploy/loopback_conf.yml
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

log INFO "Loopback configuration created ✓"

# Create cluster
cd /vast/deploy/
log INFO "Creating cluster (this takes several minutes)..."

./vman.sh $BUILD $pem_file vcli $VMAN_USER_PASSWORD -c cluster create \
    --build ${BUILD} ${VAST_INSTALL_ARGS} --name lb-vast54 --loopback 2>&1 | tee -a "$LOGFILE"

log INFO "Cluster creation initiated ✓"

# ============================================================================
# PHASE 10: WAIT FOR CLUSTER TO COME ONLINE
# ============================================================================

log STEP "Phase 10: Waiting for cluster to come online"

# Wait for cluster to be online (up to 30 minutes)
if wait_for_cluster_state "ONLINE" 1800; then
    log INFO "Cluster is ONLINE ✓"
else
    log WARN "Cluster did not reach ONLINE state within timeout"
    log INFO "Current cluster state:"
    curl -k -s "https://$MGMT_IP/api/clusters/1/" -u admin:123456 2>/dev/null | python3 -m json.tool || true
    log INFO "Installation will continue. Check status manually."
fi

# ============================================================================
# PHASE 11: VERIFY INSTALLATION
# ============================================================================

log STEP "Phase 11: Verifying installation"

# Check containers
log INFO "Running containers:"
docker ps --format "table {{.Names}}\t{{.Status}}" | tee -a "$LOGFILE"

# Check cluster status
log INFO "Cluster status:"
curl -k -s "https://$MGMT_IP/api/clusters/1/" -u admin:123456 2>/dev/null | \
    python3 -c "import sys,json; d=json.load(sys.stdin); print(f'  Name: {d[\"name\"]}'); print(f'  State: {d[\"state\"]}'); print(f'  Build: {d[\"build\"]}')" 2>/dev/null | tee -a "$LOGFILE" || log WARN "Could not retrieve cluster status"

# Check hosts
log INFO "Hosts status:"
curl -k -s "https://$MGMT_IP/api/hosts/?fields=host_label,node_type,install_state" -u admin:123456 2>/dev/null | \
    python3 -c "
import sys,json
for h in json.load(sys.stdin):
    print(f'  {h[\"host_label\"]}: {h[\"node_type\"]} - {h[\"install_state\"]}')
" 2>/dev/null | tee -a "$LOGFILE" || log WARN "Could not retrieve hosts status"

# ============================================================================
# COMPLETION
# ============================================================================

echo ""
echo "=============================================="
echo "VAST Installation Complete!"
echo "=============================================="
echo ""
echo "Access Points:"
echo "  Web UI: https://${MGMT_IP}"
echo "  Credentials: admin / 123456"
echo ""
echo "vCLI Access:"
echo "  /vast/data/11.0.0.1-4100/vms.sh vcli"
echo ""
echo "CNode Shell Access:"
echo "  /vast/data/11.0.0.1-4100/attachdocker.sh"
echo ""
echo "Loopback Network:"
echo "  VIP Pool: 15.0.0.1 - 15.0.0.8 /24"
echo "  Replication: 18.18.0.1 - 18.18.0.2 /24"
echo "  (Only accessible from within this VM)"
echo ""
echo "After Reboot:"
echo "  Run: ./start_vms.sh"
echo ""
echo "Log file: $LOGFILE"
echo ""
