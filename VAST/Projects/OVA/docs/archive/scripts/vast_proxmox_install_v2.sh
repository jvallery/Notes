#!/bin/bash
#
# VAST Data 5.4 - Optimized Proxmox Installation Script (v2)
#
# This script automates VAST installation with dual-disk support:
#   - scsi0: OS disk (small, 50-100GB)
#   - scsi1: Data disk (large, XFS formatted, for /vast)
#
# Optimizations:
#   - Separate I/O paths for OS and VAST data
#   - XFS filesystem for better sparse file handling
#   - Auto-detection and formatting of data disk
#
# Usage: sudo ./vast_proxmox_install_v2.sh
#

set -o pipefail

# Configuration
MANAGEMENT_IP="${VAST_MGMT_IP:-$(hostname -I | awk '{print $1}')}"
MANAGEMENT_IFACE="${VAST_MGMT_IFACE:-eth0}"
VAST_USER="${VAST_USER:-centos}"
CLUSTER_NAME="${VAST_CLUSTER_NAME:-lb-vast54}"
VAST_ADMIN_PASS="${VAST_ADMIN_PASS:-123456}"

# Data disk configuration
DATA_DISK="${VAST_DATA_DISK:-/dev/sdb}"
VAST_MOUNT="${VAST_MOUNT:-/vast}"

# Minimum requirements
MIN_RAM_GB=110
MIN_DISK_GB=100
MIN_CPU=12

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

# Logging
LOG_DIR="/home/${VAST_USER}"
LOG_FILE="${LOG_DIR}/vast_install_$(date +%Y%m%d_%H%M%S).log"

log_info()  { echo -e "${GREEN}[INFO]${NC} $1" | tee -a "$LOG_FILE"; }
log_warn()  { echo -e "${YELLOW}[WARN]${NC} $1" | tee -a "$LOG_FILE"; }
log_error() { echo -e "${RED}[ERROR]${NC} $1" | tee -a "$LOG_FILE"; }
log_step()  { echo -e "\n${GREEN}==> $1${NC}" | tee -a "$LOG_FILE"; }

check_root() {
    if [[ $EUID -ne 0 ]]; then
        log_error "This script must be run as root (use sudo)"
        exit 1
    fi
}

print_banner() {
    cat << 'EOF'

==============================================
 VAST Data 5.4 - Optimized Installation v2
==============================================
 Dual-Disk Performance Configuration
==============================================

EOF
    echo "Log file: $LOG_FILE"
    echo ""
}

#
# Phase 0: Data Disk Setup
#
setup_data_disk() {
    log_step "Phase 0: Data Disk Setup"
    
    # Check if data disk exists
    if [[ ! -b "$DATA_DISK" ]]; then
        log_warn "Data disk $DATA_DISK not found"
        log_info "Available disks:"
        lsblk -d -o NAME,SIZE,TYPE | grep disk | tee -a "$LOG_FILE"
        echo ""
        
        # Check if /vast already exists on root
        if [[ -d "/vast" ]]; then
            log_warn "Using existing /vast on root filesystem"
            log_warn "For optimal performance, add a dedicated data disk"
            return 0
        fi
        
        log_error "No data disk and no /vast directory. Add a data disk or create /vast manually."
        exit 1
    fi
    
    log_info "Data disk found: $DATA_DISK"
    
    # Check if already mounted
    if mountpoint -q "$VAST_MOUNT" 2>/dev/null; then
        log_info "$VAST_MOUNT already mounted ✓"
        df -h "$VAST_MOUNT" | tee -a "$LOG_FILE"
        return 0
    fi
    
    # Check if already formatted
    PART="${DATA_DISK}1"
    if [[ ! -b "$PART" ]]; then
        log_info "Partitioning $DATA_DISK..."
        parted "$DATA_DISK" mklabel gpt -s
        parted "$DATA_DISK" mkpart primary xfs 0% 100% -s
        partprobe "$DATA_DISK"
        sleep 2
    fi
    
    # Check filesystem
    if ! blkid "$PART" | grep -q xfs; then
        log_info "Formatting $PART as XFS..."
        mkfs.xfs -f -n ftype=1 -i size=512 "$PART"
    fi
    
    # Mount
    log_info "Mounting $PART at $VAST_MOUNT..."
    mkdir -p "$VAST_MOUNT"
    mount -o noatime,nodiratime "$PART" "$VAST_MOUNT"
    
    # Add to fstab
    if ! grep -q "$VAST_MOUNT" /etc/fstab; then
        echo "$PART $VAST_MOUNT xfs defaults,noatime,nodiratime 0 0" >> /etc/fstab
        log_info "Added to /etc/fstab ✓"
    fi
    
    # Set ownership
    chown "${VAST_USER}:${VAST_USER}" "$VAST_MOUNT"
    
    # Verify
    df -h "$VAST_MOUNT" | tee -a "$LOG_FILE"
    log_info "Data disk setup complete ✓"
}

#
# Phase 1: System Checks
#
system_checks() {
    log_step "Phase 1: System checks"
    
    log_info "Management IP: $MANAGEMENT_IP"
    log_info "Management Interface: $MANAGEMENT_IFACE"
    
    # CPU check
    CPU_CORES=$(nproc)
    if [[ $CPU_CORES -lt $MIN_CPU ]]; then
        log_warn "Only $CPU_CORES CPU cores available ($MIN_CPU minimum)"
    else
        log_info "CPU cores: $CPU_CORES ✓"
    fi
    
    # Memory check
    RAM_GB=$(free -g | awk '/Mem:/{print $2}')
    if [[ $RAM_GB -lt $MIN_RAM_GB ]]; then
        log_warn "${RAM_GB}GB RAM available (${MIN_RAM_GB}GB minimum)"
    else
        log_info "RAM: ${RAM_GB}GB ✓"
    fi
    
    # Data disk space check
    DISK_GB=$(df -BG "$VAST_MOUNT" 2>/dev/null | awk 'NR==2{gsub("G",""); print $4}')
    if [[ -z "$DISK_GB" ]]; then
        DISK_GB=$(df -BG / | awk 'NR==2{gsub("G",""); print $4}')
    fi
    log_info "Disk space available: ${DISK_GB}GB"
    
    # Virtualization check
    if grep -qE 'hypervisor|KVM|QEMU' /proc/cpuinfo 2>/dev/null || \
       systemd-detect-virt 2>/dev/null | grep -qiE 'kvm|qemu'; then
        log_info "Virtualization: KVM/Proxmox ✓"
    fi
    
    # VAST bundle check
    if [[ -f "./vastdata_release_2043819.vast.tar.gz" ]]; then
        log_info "VAST bundle found ✓"
    elif [[ -f "/home/${VAST_USER}/vastdata_release_2043819.vast.tar.gz" ]]; then
        log_info "VAST bundle found ✓"
        cd "/home/${VAST_USER}"
    else
        log_error "VAST bundle not found"
        exit 1
    fi
    
    # Bootstrap script check
    if [[ -f "./vast_bootstrap.sh" ]]; then
        log_info "Bootstrap script found ✓"
    else
        log_error "vast_bootstrap.sh not found"
        exit 1
    fi
}

#
# Phase 2: Docker Installation
#
install_docker() {
    log_step "Phase 2: Docker installation"
    
    if command -v docker &>/dev/null && docker ps &>/dev/null; then
        log_info "Docker already installed and accessible ✓"
        return 0
    fi
    
    if ! command -v docker &>/dev/null; then
        log_info "Installing Docker CE..."
        dnf config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
        dnf install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin
    fi
    
    systemctl enable docker
    systemctl start docker
    
    # Add user to docker group
    usermod -aG docker "$VAST_USER"
    
    # Verify
    if docker ps &>/dev/null; then
        log_info "Docker is accessible ✓"
    else
        log_warn "Docker requires group refresh - using sudo for this session"
    fi
}

#
# Phase 3: Proxmox Integration
#
proxmox_integration() {
    log_step "Phase 3: Proxmox integration"
    
    # Install qemu-guest-agent
    if ! rpm -q qemu-guest-agent &>/dev/null; then
        dnf install -y qemu-guest-agent
        systemctl enable qemu-guest-agent
        systemctl start qemu-guest-agent
    fi
    log_info "qemu-guest-agent installed ✓"
    
    # Disable vmtoolsd if present
    if systemctl is-active vmtoolsd &>/dev/null; then
        systemctl stop vmtoolsd
        systemctl disable vmtoolsd
        log_info "vmtoolsd disabled ✓"
    fi
}

#
# Phase 4: Network Configuration
#
configure_network() {
    log_step "Phase 4: Network configuration"
    
    # Disable IPv6 on management interface
    if [[ -f "/proc/sys/net/ipv6/conf/${MANAGEMENT_IFACE}/disable_ipv6" ]]; then
        echo 1 > "/proc/sys/net/ipv6/conf/${MANAGEMENT_IFACE}/disable_ipv6"
        log_info "IPv6 disabled on $MANAGEMENT_IFACE ✓"
    fi
    
    # Check firewall
    if systemctl is-active firewalld &>/dev/null; then
        log_info "Opening firewall ports..."
        firewall-cmd --permanent --add-port=443/tcp
        firewall-cmd --permanent --add-port=6001/tcp
        firewall-cmd --permanent --add-port=6001/udp
        firewall-cmd --reload
        log_info "Firewall configured ✓"
    else
        log_info "Firewall not active, skipping ✓"
    fi
}

#
# Phase 5: VAST Directory Preparation
#
prepare_directories() {
    log_step "Phase 5: Preparing VAST directories"
    
    # Create directory structure
    mkdir -p "${VAST_MOUNT}/data"
    mkdir -p "${VAST_MOUNT}/deploy"
    mkdir -p "${VAST_MOUNT}/vman"
    mkdir -p "${VAST_MOUNT}/bundles"
    mkdir -p "${VAST_MOUNT}/log"
    mkdir -p "${VAST_MOUNT}/drives"
    chown -R "${VAST_USER}:${VAST_USER}" "${VAST_MOUNT}"
    log_info "Directories created ✓"
    
    # If using separate mount, ensure /vast symlink exists
    if [[ "$VAST_MOUNT" != "/vast" ]]; then
        if [[ -L /vast ]]; then
            log_info "Symlink /vast already exists ✓"
        elif [[ -d /vast ]]; then
            log_warn "/vast is a directory, not a symlink. Consider migrating to data disk."
        else
            ln -s "$VAST_MOUNT" /vast
            log_info "Created symlink /vast -> $VAST_MOUNT ✓"
        fi
    fi
    
    # Local registry cache
    if ! grep -q "vastdata.registry.local" /etc/hosts; then
        echo "127.0.0.1 vastdata.registry.local" >> /etc/hosts
        log_info "Local registry cache configured ✓"
    fi
    
    # Docker registry config
    mkdir -p /etc/docker
    cat > /etc/docker/daemon.json << 'EOF'
{
  "insecure-registries": ["vastdata.registry.local:5000"],
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "100m",
    "max-file": "3"
  }
}
EOF
    systemctl restart docker 2>/dev/null || true
    log_info "Docker registry configuration ✓"
    
    # VAST OS release
    if [[ ! -f /etc/vast-release ]]; then
        echo "VAST OS" > /etc/vast-release
        log_info "VAST OS release configured ✓"
    fi
}

#
# Phase 6: SSH Keys
#
setup_ssh() {
    log_step "Phase 6: SSH key setup"
    
    if [[ -f "/home/${VAST_USER}/.ssh/id_rsa" ]]; then
        log_info "SSH keys already exist ✓"
    else
        sudo -u "$VAST_USER" ssh-keygen -t rsa -b 4096 -N "" -f "/home/${VAST_USER}/.ssh/id_rsa"
        log_info "SSH keys generated ✓"
    fi
    
    # Authorize key for localhost
    AUTH_KEYS="/home/${VAST_USER}/.ssh/authorized_keys"
    PUB_KEY=$(cat "/home/${VAST_USER}/.ssh/id_rsa.pub")
    if ! grep -q "$PUB_KEY" "$AUTH_KEYS" 2>/dev/null; then
        echo "$PUB_KEY" >> "$AUTH_KEYS"
        chmod 600 "$AUTH_KEYS"
        chown "${VAST_USER}:${VAST_USER}" "$AUTH_KEYS"
    fi
}

#
# Phase 7: Cleanup Previous Installation
#
cleanup_previous() {
    log_step "Phase 7: Cleaning up any previous installation"
    
    log_info "Stopping existing VAST containers..."
    docker stop $(docker ps -q --filter "name=vast" --filter "name=registry" --filter "name=mcvms") 2>/dev/null || true
    docker rm $(docker ps -aq --filter "name=vast" --filter "name=registry" --filter "name=mcvms") 2>/dev/null || true
    
    # Clear hugepages
    echo 0 > /proc/sys/vm/nr_hugepages 2>/dev/null || true
    log_info "Hugepages cleared ✓"
    
    log_info "Cleanup complete ✓"
}

#
# Phase 8: Run Bootstrap
#
run_bootstrap() {
    log_step "Phase 8: Running VAST bootstrap"
    
    log_info "This will take 10-20 minutes. Please wait..."
    
    chmod +x ./vast_bootstrap.sh
    
    # Run bootstrap
    ./vast_bootstrap.sh --interface "$MANAGEMENT_IP" --skip-prompt 2>&1 | tee -a "$LOG_FILE"
    
    if [[ ${PIPESTATUS[0]} -eq 0 ]]; then
        log_info "Bootstrap completed ✓"
    else
        log_error "Bootstrap failed"
        exit 1
    fi
}

#
# Phase 9: Create Loopback Cluster
#
create_cluster() {
    log_step "Phase 9: Creating loopback cluster"
    
    VAST_DIR=$(ls -d /vast/bundles/upgrades/*/ 2>/dev/null | head -1)
    if [[ -z "$VAST_DIR" ]]; then
        log_error "VAST installation directory not found"
        exit 1
    fi
    
    BUILD=$(basename "$VAST_DIR")
    log_info "Build: $BUILD"
    
    cd "$VAST_DIR"
    
    # Create loopback topology config
    cat > /vast/data/loopback_config.json << EOF
{
    "cluster_name": "${CLUSTER_NAME}",
    "admin_password": "${VAST_ADMIN_PASS}",
    "vsettings": {
        "CAS_OVER_RPC": "true",
        "IN_CLUSTER_COMMUNICATION_TCP": "true"
    }
}
EOF
    log_info "Loopback configuration created ✓"
    
    log_info "Creating cluster (this takes several minutes)..."
    
    ./vman.sh "$BUILD" /vast/deploy/ssh_key.pem \
        vcli -u admin -p "$VAST_ADMIN_PASS" -c \
        "cluster create --build $BUILD --vsettings CAS_OVER_RPC=true,IN_CLUSTER_COMMUNICATION_TCP=true --name $CLUSTER_NAME --loopback" \
        2>&1 | tee -a "$LOG_FILE"
    
    log_info "Cluster creation initiated ✓"
}

#
# Phase 10: Wait for Cluster Online
#
wait_for_online() {
    log_step "Phase 10: Waiting for cluster to come online"
    
    TIMEOUT=1800
    ELAPSED=0
    INTERVAL=30
    
    log_info "Waiting for cluster to reach state: ONLINE (timeout: ${TIMEOUT}s)"
    
    while [[ $ELAPSED -lt $TIMEOUT ]]; do
        # Try to get cluster state via web UI
        STATE=$(curl -sk "https://${MANAGEMENT_IP}/api/clusters/" 2>/dev/null | \
                python3 -c "import sys,json; d=json.load(sys.stdin); print(d[0]['state'] if d else 'UNKNOWN')" 2>/dev/null || echo "UNKNOWN")
        
        log_info "Cluster state: $STATE (elapsed: ${ELAPSED}s)"
        
        if [[ "$STATE" == "ONLINE" ]]; then
            log_info "Cluster is ONLINE ✓"
            return 0
        fi
        
        sleep $INTERVAL
        ELAPSED=$((ELAPSED + INTERVAL))
    done
    
    log_warn "Timeout waiting for ONLINE state"
    return 1
}

#
# Phase 11: Verify Installation
#
verify_installation() {
    log_step "Phase 11: Verifying installation"
    
    log_info "Running containers:"
    docker ps --format "table {{.Names}}\t{{.Status}}" | tee -a "$LOG_FILE"
    
    # Check disk usage
    log_info "VAST data usage:"
    du -sh "${VAST_MOUNT}/drives"/* 2>/dev/null | tee -a "$LOG_FILE"
    
    log_info "Cluster status:"
    curl -sk "https://${MANAGEMENT_IP}/api/clusters/" 2>/dev/null | \
        python3 -c "import sys,json; d=json.load(sys.stdin)[0]; print(f'  Name: {d[\"name\"]}'); print(f'  State: {d[\"state\"]}')" 2>/dev/null | \
        tee -a "$LOG_FILE"
}

#
# Print Final Summary
#
print_summary() {
    cat << EOF

==============================================
VAST Installation Complete!
==============================================

Access Points:
  Web UI: https://${MANAGEMENT_IP}
  Credentials: admin / ${VAST_ADMIN_PASS}

Data Location:
  Mount: ${VAST_MOUNT}
  Virtual SSDs: ${VAST_MOUNT}/drives/

vCLI Access:
  /vast/data/11.0.0.1-4100/vms.sh vcli

After Reboot:
  Run: ./start_vms.sh

Log file: ${LOG_FILE}
EOF
}

#
# Main
#
main() {
    check_root
    print_banner
    
    setup_data_disk
    system_checks
    install_docker
    proxmox_integration
    configure_network
    prepare_directories
    setup_ssh
    cleanup_previous
    run_bootstrap
    create_cluster
    wait_for_online
    verify_installation
    print_summary
}

# Run
main "$@"
