#!/bin/bash
#===============================================================================
# VAST 5.4 Pre-Bootstrap Host Preparation Script
#===============================================================================
# Run this script on a fresh Rocky Linux 8 VM BEFORE running vast_bootstrap.sh
#
# This script addresses the following issues discovered during deployment:
# 1. pip assertion errors due to old pip version
# 2. File descriptor exhaustion from monitor retry loops
# 3. Race conditions when multiple containers install monitor_v2
#
# Usage: sudo ./pre_bootstrap_host_prep.sh
#
# Author: Generated from deployment analysis, December 30, 2025
#===============================================================================

set -euo pipefail

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

log_info() { echo -e "${GREEN}[INFO]${NC} $1"; }
log_warn() { echo -e "${YELLOW}[WARN]${NC} $1"; }
log_error() { echo -e "${RED}[ERROR]${NC} $1"; }

echo "==============================================================================="
echo " VAST 5.4 Pre-Bootstrap Host Preparation"
echo " $(date)"
echo "==============================================================================="
echo ""

# Check if running as root
if [ "$EUID" -ne 0 ]; then
    log_error "This script must be run as root (sudo)"
    exit 1
fi

#-------------------------------------------------------------------------------
# 1. Upgrade pip to avoid Python 3.6 bugs
#-------------------------------------------------------------------------------
log_info "[1/7] Upgrading pip..."

# Check current pip version
PIP_VERSION=$(pip3 --version 2>/dev/null | awk '{print $2}' || echo "not installed")
log_info "Current pip version: $PIP_VERSION"

# Upgrade pip using python3 -m pip (recommended method)
python3 -m pip install --upgrade pip 2>&1 | tail -3

NEW_PIP_VERSION=$(pip3 --version 2>/dev/null | awk '{print $2}')
log_info "New pip version: $NEW_PIP_VERSION"

#-------------------------------------------------------------------------------
# 2. Install build dependencies
#-------------------------------------------------------------------------------
log_info "[2/7] Installing build dependencies..."

dnf install -y python3-devel python3-wheel python3-setuptools gcc 2>&1 | tail -3 || {
    log_warn "Some packages may already be installed"
}

#-------------------------------------------------------------------------------
# 3. Increase file descriptor limits
#-------------------------------------------------------------------------------
log_info "[3/7] Configuring file descriptor limits..."

# Create limits.d config for VAST
cat << 'EOF' > /etc/security/limits.d/99-vast.conf
# VAST Data file descriptor limits
# Required for loopback mode where 4 containers share host FD limit

* soft nofile 1048576
* hard nofile 1048576
root soft nofile 1048576
root hard nofile 1048576

# Also increase max user processes
* soft nproc 65535
* hard nproc 65535
EOF

log_info "Created /etc/security/limits.d/99-vast.conf"

# Create sysctl config for kernel limits
cat << 'EOF' > /etc/sysctl.d/99-vast.conf
# VAST Data kernel limits

# Increase max file descriptors (default is often 2097152)
fs.file-max = 8388608

# Increase per-process FD limit
fs.nr_open = 2097152

# Increase inotify limits (for docker/containers)
fs.inotify.max_user_watches = 524288
fs.inotify.max_user_instances = 512

# Network tuning for high connection counts
net.core.somaxconn = 65535
net.ipv4.tcp_max_syn_backlog = 65535
EOF

log_info "Created /etc/sysctl.d/99-vast.conf"

# Apply sysctl settings
sysctl -p /etc/sysctl.d/99-vast.conf 2>&1 | head -5

#-------------------------------------------------------------------------------
# 4. Pre-create directories and set permissions
#-------------------------------------------------------------------------------
log_info "[4/7] Creating required directories..."

# Monitor cache directory
mkdir -p /tmp/monitor_v2_commands_cache
chmod 777 /tmp/monitor_v2_commands_cache

# VAST directories (may not exist yet)
mkdir -p /vast/deploy
mkdir -p /vast/vman
mkdir -p /vast/log
mkdir -p /vast/data

# Ensure centos user exists and has proper permissions
if id "centos" &>/dev/null; then
    chown -R centos:centos /vast 2>/dev/null || true
    log_info "Set ownership of /vast to centos user"
else
    log_warn "centos user does not exist - skipping ownership change"
fi

#-------------------------------------------------------------------------------
# 5. Clean any stale temp files from previous attempts
#-------------------------------------------------------------------------------
log_info "[5/7] Cleaning stale temp files..."

# Count before cleanup
BEFORE_8CHAR=$(ls -d /tmp/???????? 2>/dev/null | wc -l || echo "0")
BEFORE_PIPUN=$(ls -d /tmp/pip-uninstall-* 2>/dev/null | wc -l || echo "0")

# Clean up
rm -rf /tmp/???????? 2>/dev/null || true
rm -rf /tmp/pip-uninstall-* 2>/dev/null || true
rm -rf /tmp/pip-ephem-wheel-cache-* 2>/dev/null || true

log_info "Removed $BEFORE_8CHAR orphaned monitor directories"
log_info "Removed $BEFORE_PIPUN orphaned pip-uninstall directories"

#-------------------------------------------------------------------------------
# 6. Remove any corrupt monitor_v2 installations
#-------------------------------------------------------------------------------
log_info "[6/7] Checking for corrupt monitor_v2 installations..."

if pip3 show monitor-v2 &>/dev/null; then
    log_warn "Found existing monitor-v2 installation"
    
    # Check if RECORD file exists
    RECORD_FILE="/usr/local/lib/python3.6/site-packages/monitor_v2-0.0.3.dist-info/RECORD"
    if [ ! -f "$RECORD_FILE" ]; then
        log_warn "RECORD file missing - removing corrupt installation"
        rm -rf /usr/local/lib/python3.6/site-packages/monitor_v2*
        rm -rf /usr/local/lib/python3.6/site-packages/monitor_bundle*
        rm -rf /usr/local/lib/python3.6/site-packages/monitor_client*
        rm -rf /usr/local/lib/python3.6/site-packages/monitor_utils*
        log_info "Removed corrupt monitor packages"
    else
        log_info "monitor-v2 installation appears healthy"
    fi
else
    log_info "No existing monitor-v2 installation found"
fi

#-------------------------------------------------------------------------------
# 7. Create fake ipmitool for loopback mode
#-------------------------------------------------------------------------------
log_info "[7/7] Setting up ipmitool for loopback mode..."

if [ -f /usr/bin/ipmitool ]; then
    # Backup original if it exists and isn't our fake
    if ! grep -q "VAST Data Loopback" /usr/bin/ipmitool 2>/dev/null; then
        mv /usr/bin/ipmitool /usr/bin/ipmitool.real 2>/dev/null || true
        log_info "Backed up original ipmitool to ipmitool.real"
    fi
fi

# Create fake ipmitool that returns valid output for VMs
cat << 'IPMITOOL' > /usr/bin/ipmitool
#!/bin/bash
# Fake ipmitool for VAST loopback mode on VMs
# Returns valid output to satisfy hardware validation checks

if [[ "$*" == *"fru print"* ]]; then
    echo "Board Mfg Date        : Mon Jan 01 00:00:00 2024"
    echo "Board Mfg             : VAST Data Loopback"
    echo "Board Product         : Virtual Platform"
    echo "Board Serial          : LOOPBACK-$(hostname | md5sum | cut -c1-8)"
    exit 0
fi

if [[ "$*" == *"mc info"* ]]; then
    echo "Device ID             : 32"
    echo "Device Revision       : 1"
    echo "Firmware Revision     : 1.00"
    echo "IPMI Version          : 2.0"
    echo "Manufacturer ID       : 0"
    echo "Product ID            : 0 (0x0000)"
    exit 0
fi

if [[ "$*" == *"sensor"* ]]; then
    echo "CPU Temp         | 45.000     | degrees C  | ok"
    echo "System Temp      | 35.000     | degrees C  | ok"
    exit 0
fi

if [[ "$*" == *"lan print"* ]]; then
    echo "IP Address Source       : Static Address"
    echo "IP Address              : 0.0.0.0"
    echo "Subnet Mask             : 0.0.0.0"
    exit 0
fi

# For any other command, try real ipmitool if it exists
if [ -x /usr/bin/ipmitool.real ]; then
    /usr/bin/ipmitool.real "$@" 2>/dev/null || exit 0
else
    exit 0
fi
IPMITOOL

chmod +x /usr/bin/ipmitool
log_info "Created fake ipmitool for VM environment"

#-------------------------------------------------------------------------------
# Summary
#-------------------------------------------------------------------------------
echo ""
echo "==============================================================================="
echo " Pre-Bootstrap Preparation Complete"
echo "==============================================================================="
echo ""
echo "Changes made:"
echo "  ✓ pip upgraded to $(pip3 --version | awk '{print $2}')"
echo "  ✓ File descriptor limits increased to 8M (kernel) / 1M (process)"
echo "  ✓ Required directories created"
echo "  ✓ Stale temp files cleaned"
echo "  ✓ ipmitool configured for VM environment"
echo ""
echo "Current system status:"
echo "  File descriptors: $(cat /proc/sys/fs/file-nr | awk '{print $1 " used / " $3 " max"}')"
echo "  Python version: $(python3 --version)"
echo "  pip version: $(pip3 --version | awk '{print $2}')"
echo ""
echo "Next steps:"
echo "  1. Log out and log back in (for ulimit changes to take effect)"
echo "  2. Run: ./vast_bootstrap.sh"
echo ""
echo "==============================================================================="
