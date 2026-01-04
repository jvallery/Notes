#!/bin/bash
#===============================================================================
# VAST 5.4 Unified Installation Script for Proxmox
#===============================================================================
#
# This script automates VAST 5.4 loopback cluster deployment on Proxmox/KVM.
# It consolidates all lessons learned and workarounds from development.
#
# Usage:
#   sudo ./install.sh                    # Full installation
#   sudo ./install.sh --phase <phase>    # Run specific phase
#   sudo ./install.sh --verify           # Verify existing installation
#   sudo ./install.sh --dry-run          # Show what would be done
#
# Phases:
#   pre-bootstrap   - Prepare host (pip, FD limits, ipmitool, etc.)
#   bootstrap       - Run VAST bootstrap
#   post-start      - Apply container fixes
#   cluster         - Create and activate cluster
#   verify          - Verify cluster health
#
# Configuration:
#   Edit config.env or set environment variables
#
# Author: Generated from VAST Proxmox deployment project
# Date: December 30, 2025
#
#===============================================================================

# Strict mode: exit on error, undefined vars, pipe failures
set -o pipefail

# Error trap for debugging
trap 'echo "[ERROR] Command failed at line $LINENO: $BASH_COMMAND" >&2' ERR

# Script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

#-------------------------------------------------------------------------------
# Load Configuration
#-------------------------------------------------------------------------------

# Default configuration
CLUSTER_NAME="${CLUSTER_NAME:-lb-vast54}"
VAST_BUILD="${VAST_BUILD:-release-5-4-0-2043819}"
VAST_ADMIN_USER="${VAST_ADMIN_USER:-admin}"
VAST_ADMIN_PASS="${VAST_ADMIN_PASS:-123456}"
MANAGEMENT_IP="${MANAGEMENT_IP:-}"
MANAGEMENT_IFACE="${MANAGEMENT_IFACE:-eth0}"
VAST_MOUNT="${VAST_MOUNT:-/vast}"
VAST_DRIVES="${VAST_DRIVES:-/vast/drives}"
VAST_USER="${VAST_USER:-centos}"
MIN_RAM_GB="${MIN_RAM_GB:-110}"
MIN_DISK_GB="${MIN_DISK_GB:-100}"
MIN_CPU="${MIN_CPU:-10}"
BOOTSTRAP_TIMEOUT="${BOOTSTRAP_TIMEOUT:-1800}"
CLUSTER_TIMEOUT="${CLUSTER_TIMEOUT:-1200}"
ACTIVATION_TIMEOUT="${ACTIVATION_TIMEOUT:-900}"
CHECK_INTERVAL="${CHECK_INTERVAL:-10}"
LOG_DIR="${LOG_DIR:-/home/centos/docs/install_logs}"
VERBOSE="${VERBOSE:-1}"
APPLY_WORKAROUNDS="${APPLY_WORKAROUNDS:-1}"
PREINSTALL_MONITOR="${PREINSTALL_MONITOR:-1}"
COPY_RSYNC="${COPY_RSYNC:-1}"
MONITOR_DURING_INSTALL="${MONITOR_DURING_INSTALL:-1}"
ABORT_ON_ERROR="${ABORT_ON_ERROR:-1}"

# Load config file (priority: env vars > config.env > config.env.example)
CONFIG_FILE="${SCRIPT_DIR}/config.env"
CONFIG_EXAMPLE="${SCRIPT_DIR}/config.env.example"

if [ -f "$CONFIG_FILE" ]; then
    source "$CONFIG_FILE"
elif [ -f "$CONFIG_EXAMPLE" ]; then
    echo "[WARN] No config.env found, using config.env.example defaults"
    source "$CONFIG_EXAMPLE"
fi

#-------------------------------------------------------------------------------
# Colors and Logging
#-------------------------------------------------------------------------------

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m'

# Initialize logging
mkdir -p "$LOG_DIR"
LOG_FILE="${LOG_DIR}/install_$(date +%Y%m%d_%H%M%S).log"

log() {
    local level="$1"
    shift
    local msg="$*"
    local timestamp=$(date '+%Y-%m-%d %H:%M:%S')
    echo "[$timestamp] [$level] $msg" >> "$LOG_FILE"
    
    case "$level" in
        INFO)  [ "$VERBOSE" -ge 1 ] && echo -e "${GREEN}[INFO]${NC} $msg" ;;
        WARN)  echo -e "${YELLOW}[WARN]${NC} $msg" ;;
        ERROR) echo -e "${RED}[ERROR]${NC} $msg" ;;
        DEBUG) [ "$VERBOSE" -ge 2 ] && echo -e "${CYAN}[DEBUG]${NC} $msg" ;;
        STEP)  echo -e "${BLUE}==>${NC} ${GREEN}$msg${NC}" ;;
    esac
}

log_info()  { log INFO "$@"; }
log_warn()  { log WARN "$@"; }
log_error() { log ERROR "$@"; }
log_debug() { log DEBUG "$@"; }
log_step()  { log STEP "$@"; }

die() {
    log_error "$@"
    exit 1
}

#-------------------------------------------------------------------------------
# Utility Functions
#-------------------------------------------------------------------------------

check_root() {
    if [ "$EUID" -ne 0 ]; then
        die "This script must be run as root (sudo $0)"
    fi
}

# P0.1: Safe Python/pip handling for Rocky 8 (Python 3.6)
check_python_environment() {
    log_info "Checking Python environment..."
    
    local py_version=$(python3 --version 2>&1 | awk '{print $2}')
    local py_major=$(echo "$py_version" | cut -d. -f1)
    local py_minor=$(echo "$py_version" | cut -d. -f2)
    
    log_info "Python version: $py_version"
    log_info "Python path: $(which python3)"
    
    # Python 3.6 requires pinned pip (pip 22+ dropped 3.6 support)
    if [ "$py_major" -eq 3 ] && [ "$py_minor" -eq 6 ]; then
        log_warn "Python 3.6 detected - using pinned pip/setuptools versions"
        PYTHON_36_MODE=1
    else
        log_info "Python ${py_major}.${py_minor} detected - modern pip OK"
        PYTHON_36_MODE=0
    fi
}

install_safe_pip() {
    if [ "${PYTHON_36_MODE:-0}" -eq 1 ]; then
        # Python 3.6: pip 22+ dropped support, pin to last compatible
        log_info "Installing pip==21.3.1 (last Python 3.6 compatible version)..."
        python3 -m pip install --quiet "pip==21.3.1" 2>/dev/null || \
            python3 -m pip install "pip==21.3.1"
        python3 -m pip install --quiet "setuptools<=59.6.0" "wheel<=0.37.1" 2>/dev/null || true
        
        # Verify
        local pip_ver=$(pip3 --version 2>/dev/null | awk '{print $2}')
        if [[ "$pip_ver" != "21.3.1" ]]; then
            log_warn "pip version is $pip_ver (expected 21.3.1) - may cause issues"
        else
            log_info "✓ pip $pip_ver installed (Python 3.6 safe)"
        fi
    else
        # Modern Python: upgrade pip normally
        log_info "Upgrading pip (modern Python)..."
        python3 -m pip install --upgrade pip >/dev/null 2>&1
        log_info "✓ pip version: $(pip3 --version | awk '{print $2}')"
    fi
}

auto_detect_ip() {
    if [ -z "$MANAGEMENT_IP" ]; then
        MANAGEMENT_IP=$(hostname -I | awk '{print $1}')
        log_debug "Auto-detected management IP: $MANAGEMENT_IP"
    fi
    
    # Auto-detect interface if not set or eth0 doesn't exist
    if [ -z "$MANAGEMENT_IFACE" ] || ! ip link show "$MANAGEMENT_IFACE" &>/dev/null; then
        MANAGEMENT_IFACE=$(ip route get 1.1.1.1 2>/dev/null | awk '{print $5; exit}')
        [ -z "$MANAGEMENT_IFACE" ] && MANAGEMENT_IFACE=$(ip -o link show up | awk -F': ' 'NR==2{print $2}')
        log_debug "Auto-detected management interface: $MANAGEMENT_IFACE"
    fi
}

wait_for_condition() {
    local description="$1"
    local check_cmd="$2"
    local timeout="${3:-300}"
    local interval="${4:-$CHECK_INTERVAL}"
    
    local elapsed=0
    log_info "Waiting for: $description (timeout: ${timeout}s)"
    
    while [ $elapsed -lt $timeout ]; do
        if eval "$check_cmd" >/dev/null 2>&1; then
            log_info "✓ $description"
            return 0
        fi
        sleep "$interval"
        elapsed=$((elapsed + interval))
        [ "$VERBOSE" -ge 2 ] && echo -n "."
    done
    
    log_error "Timeout waiting for: $description"
    return 1
}

get_cluster_state() {
    curl -sk -u "${VAST_ADMIN_USER}:${VAST_ADMIN_PASS}" \
        "https://${MANAGEMENT_IP}/api/clusters/" 2>/dev/null | \
        python3 -c "import sys,json; d=json.load(sys.stdin); print(d[0]['state'] if d else 'NONE')" 2>/dev/null || echo "UNKNOWN"
}

#-------------------------------------------------------------------------------
# Phase 1: Pre-Bootstrap
#-------------------------------------------------------------------------------

phase_pre_bootstrap() {
    log_step "Phase 1: Pre-Bootstrap Host Preparation"
    
    # Validate requirements
    log_info "Validating system requirements..."
    
    local ram_gb=$(free -g | awk '/^Mem:/{print $2}')
    local disk_gb=$(df -BG "$VAST_MOUNT" 2>/dev/null | awk 'NR==2{print int($4)}' || df -BG / | awk 'NR==2{print int($4)}')
    local cpu_count=$(nproc)
    
    log_debug "RAM: ${ram_gb}GB, Disk: ${disk_gb}GB, CPUs: ${cpu_count}"
    
    [ "$ram_gb" -lt "$MIN_RAM_GB" ] && die "Insufficient RAM: ${ram_gb}GB < ${MIN_RAM_GB}GB required"
    [ "$disk_gb" -lt "$MIN_DISK_GB" ] && die "Insufficient disk: ${disk_gb}GB < ${MIN_DISK_GB}GB required"
    [ "$cpu_count" -lt "$MIN_CPU" ] && die "Insufficient CPUs: ${cpu_count} < ${MIN_CPU} required"
    
    log_info "✓ System requirements met (RAM: ${ram_gb}GB, Disk: ${disk_gb}GB, CPUs: ${cpu_count})"
    
    if [ "$APPLY_WORKAROUNDS" -eq 1 ]; then
        # Check Python environment first
        check_python_environment
        
        # Install pip safely (version-aware for Python 3.6)
        install_safe_pip
        
        # Install packages (dnf-plugins-core first for Docker repo)
        log_info "Installing required packages..."
        dnf install -y dnf-plugins-core >/dev/null 2>&1
        dnf install -y python3-devel python3-wheel python3-setuptools gcc rsync pv jq >/dev/null 2>&1
        
        # File descriptor limits (process)
        log_info "Configuring file descriptor limits..."
        cat << 'EOF' > /etc/security/limits.d/99-vast.conf
* soft nofile 1048576
* hard nofile 1048576
root soft nofile 1048576
root hard nofile 1048576
* soft nproc 65535
* hard nproc 65535
EOF
        
        # File descriptor limits (kernel)
        cat << 'EOF' > /etc/sysctl.d/99-vast-fd.conf
fs.file-max = 8388608
fs.nr_open = 2097152
fs.inotify.max_user_watches = 524288
fs.inotify.max_user_instances = 512
EOF
        sysctl -p /etc/sysctl.d/99-vast-fd.conf >/dev/null 2>&1
        log_info "✓ FD limits configured (kernel max: $(cat /proc/sys/fs/file-max))"
        
        # Performance tuning
        log_info "Applying kernel performance tuning..."
        cat << 'EOF' > /etc/sysctl.d/99-vast-perf.conf
vm.swappiness = 1
vm.dirty_ratio = 10
vm.dirty_background_ratio = 5
kernel.sched_migration_cost_ns = 5000000
kernel.sched_autogroup_enabled = 0
net.core.somaxconn = 65535
net.core.netdev_max_backlog = 65535
EOF
        sysctl -p /etc/sysctl.d/99-vast-perf.conf >/dev/null 2>&1
        
        # Disable THP
        echo never > /sys/kernel/mm/transparent_hugepage/enabled 2>/dev/null
        echo never > /sys/kernel/mm/transparent_hugepage/defrag 2>/dev/null
        log_info "✓ Transparent Huge Pages disabled"
        
        # Create fake ipmitool
        log_info "Creating fake ipmitool..."
        [ -f /usr/bin/ipmitool ] && [ ! -f /usr/bin/ipmitool.real ] && \
            mv /usr/bin/ipmitool /usr/bin/ipmitool.real 2>/dev/null
        
        cat << 'IPMITOOL' > /usr/bin/ipmitool
#!/bin/bash
if [[ "$*" == *"fru print"* ]]; then
    echo "Board Mfg             : VAST Data Loopback"
    exit 0
fi
[ -x /usr/bin/ipmitool.real ] && exec /usr/bin/ipmitool.real "$@"
exit 0
IPMITOOL
        chmod +x /usr/bin/ipmitool
        log_info "✓ ipmitool configured for VM environment"
        
        # Clean temp directories (SAFE: only pip-related, age-limited)
        log_info "Cleaning orphaned pip temp directories..."
        find /tmp -maxdepth 1 -type d -name 'pip-*' -mmin +60 -exec rm -rf {} + 2>/dev/null || true
        find /tmp -maxdepth 1 -type d -name 'pip-uninstall-*' -exec rm -rf {} + 2>/dev/null || true
        find /tmp -maxdepth 1 -type d -name 'pip-ephem-wheel-cache-*' -exec rm -rf {} + 2>/dev/null || true
        
        # Clean corrupted packages (specific patterns only)
        rm -rf /usr/local/lib/python3.6/site-packages/-* 2>/dev/null
        rm -rf /usr/local/lib/python3.6/site-packages/~* 2>/dev/null
        rm -rf /usr/local/lib/python3.6/site-packages/monitor_v2* 2>/dev/null
    fi
    
    log_step "Phase 1 Complete"
}

#-------------------------------------------------------------------------------
# Phase 2: Bootstrap
#-------------------------------------------------------------------------------

phase_bootstrap() {
    log_step "Phase 2: VAST Bootstrap"
    
    auto_detect_ip
    
    # Find bootstrap script
    local bootstrap_script=""
    if [ -f "$VAST_MOUNT/bundles/vast_bootstrap.sh" ]; then
        bootstrap_script="$VAST_MOUNT/bundles/vast_bootstrap.sh"
    else
        # Look for extracted bundle
        local bundle_dir=$(ls -d $VAST_MOUNT/bundles/upgrades/*/ 2>/dev/null | head -1)
        if [ -n "$bundle_dir" ] && [ -f "${bundle_dir}/vast_bootstrap.sh" ]; then
            bootstrap_script="${bundle_dir}/vast_bootstrap.sh"
        fi
    fi
    
    [ -z "$bootstrap_script" ] && die "Cannot find vast_bootstrap.sh in $VAST_MOUNT/bundles/"
    log_info "Using bootstrap script: $bootstrap_script"
    
    # Check if already bootstrapped
    if docker ps --format '{{.Names}}' 2>/dev/null | grep -q "vast_vms"; then
        log_info "VMS container already running - skipping bootstrap"
        return 0
    fi
    
    # Disable IPv6 on management interface
    log_info "Disabling IPv6 on $MANAGEMENT_IFACE..."
    echo 1 > /proc/sys/net/ipv6/conf/${MANAGEMENT_IFACE}/disable_ipv6 2>/dev/null || true

    # Run bootstrap
    log_info "Running VAST bootstrap (this takes ~10 minutes)..."
    cd "$(dirname "$bootstrap_script")"
    
    timeout "$BOOTSTRAP_TIMEOUT" ./vast_bootstrap.sh --interface "$MANAGEMENT_IP" --skip-prompt 2>&1 | \
        tee -a "$LOG_FILE" | \
        while read line; do
            log_debug "$line"
            # Show progress indicators
            echo "$line" | grep -qE "(extracting|starting|done|Done)" && log_info "$line"
        done
    
    local exit_code=${PIPESTATUS[0]}
    [ $exit_code -ne 0 ] && die "Bootstrap failed with exit code $exit_code"
    
    # Wait for VMS
    wait_for_condition "VMS container healthy" \
        "curl -sk https://${MANAGEMENT_IP}/api/version/" \
        300 10 || die "VMS did not become healthy"
    
    log_step "Phase 2 Complete - VMS is up"
}

#-------------------------------------------------------------------------------
# Phase 3: Post-Container Fixes
#-------------------------------------------------------------------------------

phase_post_start() {
    log_step "Phase 3: Post-Container Fixes"
    
    # Wait for containers to be running
    sleep 5
    
    # Pre-install monitor_v2
    if [ "$PREINSTALL_MONITOR" -eq 1 ]; then
        log_info "Pre-installing monitor_v2 package..."
        
        local vast_image="vastdata.registry.local:5000/dev/orion:${VAST_BUILD}"
        
        docker rm -f temp_monitor_extract 2>/dev/null || true
        if docker create --name temp_monitor_extract "$vast_image" >/dev/null 2>&1; then
            local temp_dir=$(mktemp -d)
            docker cp temp_monitor_extract:/vast/install/pysrc/monitor_v2 "$temp_dir/monitor_v2" 2>/dev/null
            docker rm temp_monitor_extract >/dev/null 2>&1
            
            if [ -d "$temp_dir/monitor_v2" ]; then
                pip3 install --force-reinstall --no-deps "$temp_dir/monitor_v2" >/dev/null 2>&1
                rm -rf "$temp_dir"
                log_info "✓ monitor_v2 pre-installed"
            else
                log_warn "Could not extract monitor_v2"
            fi
        else
            log_warn "Could not create temp container for monitor extraction"
        fi
    fi
    
    # Copy rsync to containers (idempotent - tracks completion per container)
    if [ "$COPY_RSYNC" -eq 1 ]; then
        log_info "Copying rsync to VAST containers..."
        local rsync_state_dir="/vast/deploy/.rsync_state"
        mkdir -p "$rsync_state_dir"
        
        for port in 4100 4200 4300 4400; do
            local container="vast_platform_11.0.0.1-${port}"
            local state_file="${rsync_state_dir}/${container}.done"
            
            # Skip if already copied (survives reboots)
            if [ -f "$state_file" ]; then
                log_debug "  ✓ $container (already done)"
                continue
            fi
            
            if docker ps --format '{{.Names}}' | grep -q "$container"; then
                # Check if rsync already exists in container
                if docker exec "$container" which rsync >/dev/null 2>&1; then
                    log_debug "  ✓ $container (rsync already present)"
                    touch "$state_file"
                elif docker cp /usr/bin/rsync "$container:/usr/bin/rsync" 2>/dev/null; then
                    log_debug "  ✓ $container (copied)"
                    touch "$state_file"
                else
                    log_warn "  ✗ Could not copy to $container"
                fi
            fi
        done
    fi
    
    # Check container health
    log_info "Container status:"
    docker ps --filter "name=vast" --format "  {{.Names}}: {{.Status}}" | head -10
    
    log_step "Phase 3 Complete"
}

#-------------------------------------------------------------------------------
# Phase 4: Cluster Creation
#-------------------------------------------------------------------------------

check_cluster_prerequisites() {
    local errors=0
    
    log_info "Checking cluster creation prerequisites..."
    
    # Check Docker is running
    if ! docker info >/dev/null 2>&1; then
        log_error "Docker is not running"
        ((errors++))
    fi
    
    # Check at least one VAST container is running
    local container_count=$(docker ps --filter "name=vast_platform" --format '{{.Names}}' 2>/dev/null | wc -l)
    if [ "$container_count" -lt 1 ]; then
        log_error "No VAST containers running (need bootstrap first)"
        ((errors++))
    else
        log_debug "Found $container_count VAST containers"
    fi
    
    # Check /vast/deploy directory exists
    if [ ! -d "/vast/deploy" ]; then
        log_error "/vast/deploy directory missing (need bootstrap first)"
        ((errors++))
    fi
    
    # Check vman.sh exists
    local vman_dir=$(ls -d $VAST_MOUNT/bundles/upgrades/*/ 2>/dev/null | head -1)
    if [ -z "$vman_dir" ] || [ ! -f "${vman_dir}/vman.sh" ]; then
        log_error "vman.sh not found in $VAST_MOUNT/bundles/upgrades/"
        ((errors++))
    fi
    
    # Check SSH key exists
    if [ ! -f "/vast/deploy/ssh_key.pem" ]; then
        log_error "/vast/deploy/ssh_key.pem missing"
        ((errors++))
    fi
    
    # Check FD limits are set
    local file_max=$(sysctl -n fs.file-max 2>/dev/null || echo 0)
    if [ "$file_max" -lt 1000000 ]; then
        log_warn "fs.file-max is only $file_max (recommend 8M+)"
    fi
    
    if [ $errors -gt 0 ]; then
        die "Cluster prerequisites not met ($errors errors). Run phases 1-3 first."
    fi
    
    log_info "✓ All cluster prerequisites met"
}

phase_cluster() {
    log_step "Phase 4: Cluster Creation"
    
    # Verify prerequisites before proceeding
    check_cluster_prerequisites
    
    auto_detect_ip
    
    # Check if cluster already exists
    local current_state=$(get_cluster_state)
    if [ "$current_state" == "ONLINE" ]; then
        log_info "Cluster already ONLINE - skipping creation"
        return 0
    fi
    
    if [ "$current_state" != "NONE" ] && [ "$current_state" != "UNKNOWN" ]; then
        log_info "Cluster exists in state: $current_state"
        # Could add recovery logic here
    fi
    
    # Create loopback config
    log_info "Creating loopback configuration..."
    cat << EOF > /vast/deploy/loopback_conf.yml
name: ${CLUSTER_NAME}
loopback: true
vip_pools:
   vippool-1:
     start_ip: '${VIP_START:-15.0.0.1}'
     end_ip: '${VIP_END:-15.0.0.8}'
     subnet_bits: ${VIP_SUBNET:-24}
   gateway-1:
     role: 'replication'
     start_ip: '${GATEWAY_START:-18.18.0.1}'
     end_ip: '${GATEWAY_END:-18.18.0.2}'
     subnet_bits: ${GATEWAY_SUBNET:-24}
vms_ipv6: '1001::1'
vip_pool_segments:
  ipv4:
    protocols:
    - start_ip: '${VIP_START:-15.0.0.1}'
      end_ip: '${VIP_END:-15.0.0.8}'
      subnet_bits: ${VIP_SUBNET:-24}
    replication: []
  ipv6:
  - end_ip: 1000::10
    start_ip: 1000::1
    subnet_bits: 120
EOF
    
    # Find vman.sh
    local vman_dir=$(ls -d $VAST_MOUNT/bundles/upgrades/*/ 2>/dev/null | head -1)
    [ -z "$vman_dir" ] && die "Cannot find VAST installation directory"
    
    local vman_script="${vman_dir}/vman.sh"
    [ ! -f "$vman_script" ] && die "Cannot find vman.sh"
    
    # Create cluster
    log_info "Creating loopback cluster: $CLUSTER_NAME"
    log_info "This will take 10-20 minutes..."
    
    export VAST_INSTALL_ARGS='--vsettings CAS_OVER_RPC=true,IN_CLUSTER_COMMUNICATION_TCP=true'
    
    cd "$vman_dir"
    timeout "$CLUSTER_TIMEOUT" ./vman.sh "$VAST_BUILD" /vast/deploy/ssh_key.pem vcli \
        -u "$VAST_ADMIN_USER" -p "$VAST_ADMIN_PASS" \
        -c "cluster create --build ${VAST_BUILD} ${VAST_INSTALL_ARGS} --name ${CLUSTER_NAME} --loopback" \
        2>&1 | tee -a "$LOG_FILE" &
    
    local cluster_pid=$!
    
    # Monitor cluster state
    local start_time=$(date +%s)
    local last_state=""
    
    while kill -0 $cluster_pid 2>/dev/null; do
        sleep "$CHECK_INTERVAL"
        
        local current_state=$(get_cluster_state)
        local elapsed=$(($(date +%s) - start_time))
        
        if [ "$current_state" != "$last_state" ]; then
            log_info "Cluster state: $current_state (${elapsed}s elapsed)"
            last_state="$current_state"
        fi
        
        if [ "$current_state" == "ONLINE" ]; then
            log_info "✓ Cluster is ONLINE!"
            wait $cluster_pid 2>/dev/null
            break
        fi
        
        if [ $elapsed -gt "$ACTIVATION_TIMEOUT" ] && [ "$current_state" == "ACTIVATING" ]; then
            log_warn "Activation taking longer than expected..."
        fi
        
        # Check for FD issues
        local fd_used=$(cat /proc/sys/fs/file-nr | awk '{print $1}')
        local fd_max=$(cat /proc/sys/fs/file-nr | awk '{print $3}')
        local fd_pct=$((fd_used * 100 / fd_max))
        [ $fd_pct -gt 50 ] && log_warn "FD usage high: ${fd_pct}%"
    done
    
    wait $cluster_pid 2>/dev/null
    
    # Verify final state
    local final_state=$(get_cluster_state)
    [ "$final_state" != "ONLINE" ] && die "Cluster failed to come online. State: $final_state"
    
    log_step "Phase 4 Complete - Cluster is ONLINE"
}

#-------------------------------------------------------------------------------
# Phase 5: Verification
#-------------------------------------------------------------------------------

phase_verify() {
    log_step "Phase 5: Verification"
    
    auto_detect_ip
    
    # Check cluster
    log_info "Checking cluster health..."
    
    local cluster_state=$(get_cluster_state)
    log_info "Cluster state: $cluster_state"
    [ "$cluster_state" != "ONLINE" ] && log_error "Cluster is not ONLINE!"
    
    # Check CNodes
    log_info "CNode status:"
    curl -sk -u "${VAST_ADMIN_USER}:${VAST_ADMIN_PASS}" \
        "https://${MANAGEMENT_IP}/api/cnodes/" 2>/dev/null | \
        python3 -c "
import sys, json
for c in json.load(sys.stdin):
    print(f\"  {c['name']}: {c['state']}\")
" 2>/dev/null || log_warn "Could not fetch CNode status"
    
    # Check DNodes
    log_info "DNode status:"
    curl -sk -u "${VAST_ADMIN_USER}:${VAST_ADMIN_PASS}" \
        "https://${MANAGEMENT_IP}/api/dnodes/" 2>/dev/null | \
        python3 -c "
import sys, json
for d in json.load(sys.stdin):
    print(f\"  {d['name']}: {d['state']}\")
" 2>/dev/null || log_warn "Could not fetch DNode status"
    
    # Check capacity
    log_info "Capacity:"
    curl -sk -u "${VAST_ADMIN_USER}:${VAST_ADMIN_PASS}" \
        "https://${MANAGEMENT_IP}/api/capacity/" 2>/dev/null | \
        python3 -c "
import sys, json
c = json.load(sys.stdin)
print(f\"  Usable: {c.get('usable_capacity_bytes', 0) / 1e9:.1f} GB\")
print(f\"  Used: {c.get('used_capacity_bytes', 0) / 1e9:.1f} GB\")
" 2>/dev/null || log_warn "Could not fetch capacity"
    
    # System health
    log_info "System status:"
    log_info "  FD usage: $(cat /proc/sys/fs/file-nr | awk '{printf "%d / %d (%d%%)", $1, $3, $1*100/$3}')"
    log_info "  Load: $(uptime | awk -F'load average:' '{print $2}')"
    log_info "  Memory: $(free -h | awk '/^Mem:/{printf "%s used / %s total", $3, $2}')"
    
    # Generate summary
    echo ""
    echo "==============================================================================="
    echo " VAST Installation Summary"
    echo "==============================================================================="
    echo ""
    echo " Cluster: $CLUSTER_NAME"
    echo " State:   $cluster_state"
    echo ""
    echo " Access:"
    echo "   Web UI:  https://${MANAGEMENT_IP}"
    echo "   User:    ${VAST_ADMIN_USER}"
    echo "   Pass:    ${VAST_ADMIN_PASS}"
    echo ""
    echo " vCLI:    /vast/data/11.0.0.1-4100/vms.sh vcli"
    echo ""
    echo " Logs:    $LOG_FILE"
    echo ""
    echo "==============================================================================="
    
    log_step "Phase 5 Complete"
}

#-------------------------------------------------------------------------------
# Main Entry Point
#-------------------------------------------------------------------------------

usage() {
    echo "Usage: $0 [OPTIONS]"
    echo ""
    echo "Options:"
    echo "  --phase <phase>   Run specific phase (pre-bootstrap, bootstrap, post-start, cluster, verify)"
    echo "  --verify          Verify existing installation"
    echo "  --dry-run         Show what would be done"
    echo "  -v, --verbose     Increase verbosity"
    echo "  -h, --help        Show this help"
    echo ""
    echo "Examples:"
    echo "  sudo $0                      # Full installation"
    echo "  sudo $0 --phase bootstrap    # Run bootstrap only"
    echo "  sudo $0 --verify             # Check cluster health"
    exit 0
}

main() {
    local phase=""
    local dry_run=0
    
    # Parse arguments
    while [ $# -gt 0 ]; do
        case "$1" in
            --phase)
                phase="$2"
                shift 2
                ;;
            --verify)
                phase="verify"
                shift
                ;;
            --dry-run)
                dry_run=1
                shift
                ;;
            -v|--verbose)
                VERBOSE=$((VERBOSE + 1))
                shift
                ;;
            -h|--help)
                usage
                ;;
            *)
                die "Unknown option: $1"
                ;;
        esac
    done
    
    check_root
    
    echo ""
    echo "==============================================================================="
    echo " VAST 5.4 Installation for Proxmox"
    echo " $(date)"
    echo "==============================================================================="
    echo ""
    
    if [ $dry_run -eq 1 ]; then
        log_info "DRY RUN MODE - no changes will be made"
        echo ""
        echo "Would execute phases:"
        echo "  1. Pre-Bootstrap (pip, FD limits, ipmitool, etc.)"
        echo "  2. Bootstrap (extract, start VMS)"
        echo "  3. Post-Start (monitor_v2, rsync)"
        echo "  4. Cluster (create and activate)"
        echo "  5. Verify (health checks)"
        exit 0
    fi
    
    log_info "Log file: $LOG_FILE"
    log_info "Config: $CONFIG_FILE"
    echo ""
    
    # Run requested phase(s)
    case "$phase" in
        pre-bootstrap)
            phase_pre_bootstrap
            ;;
        bootstrap)
            phase_bootstrap
            ;;
        post-start)
            phase_post_start
            ;;
        cluster)
            phase_cluster
            ;;
        verify)
            phase_verify
            ;;
        "")
            # Full installation
            phase_pre_bootstrap
            phase_bootstrap
            phase_post_start
            phase_cluster
            phase_verify
            ;;
        *)
            die "Unknown phase: $phase"
            ;;
    esac
    
    echo ""
    log_info "Installation complete!"
}

# Run main
main "$@"
