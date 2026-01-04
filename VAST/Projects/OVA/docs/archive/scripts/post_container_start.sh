#!/bin/bash
#===============================================================================
# VAST 5.4 Post-Container-Start Script
#===============================================================================
# Run this script AFTER containers start but BEFORE cluster activation
#
# This script:
# 1. Pre-installs monitor_v2 on host to prevent container race conditions
# 2. Monitors file descriptor usage
# 3. Provides early warning of issues
#
# Usage: ./post_container_start.sh
#
# Author: Generated from deployment analysis, December 30, 2025
#===============================================================================

set -euo pipefail

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

log_info() { echo -e "${GREEN}[INFO]${NC} $1"; }
log_warn() { echo -e "${YELLOW}[WARN]${NC} $1"; }
log_error() { echo -e "${RED}[ERROR]${NC} $1"; }
log_step() { echo -e "${BLUE}[STEP]${NC} $1"; }

echo "==============================================================================="
echo " VAST 5.4 Post-Container-Start Fixes"
echo " $(date)"
echo "==============================================================================="
echo ""

#-------------------------------------------------------------------------------
# Check prerequisites
#-------------------------------------------------------------------------------
log_step "[1/5] Checking prerequisites..."

# Check if docker is available
if ! command -v docker &>/dev/null; then
    log_error "Docker is not installed or not in PATH"
    exit 1
fi

# Check if containers are running
RUNNING_CONTAINERS=$(docker ps --filter "name=vast_platform" -q | wc -l)
if [ "$RUNNING_CONTAINERS" -eq 0 ]; then
    log_warn "No VAST platform containers are currently running"
    log_info "This script should be run after containers start"
    log_info "Proceeding anyway to pre-install monitor_v2..."
fi

log_info "Found $RUNNING_CONTAINERS running VAST platform containers"

#-------------------------------------------------------------------------------
# Extract and pre-install monitor_v2
#-------------------------------------------------------------------------------
log_step "[2/5] Pre-installing monitor_v2 on host..."

# Find the VAST image
VAST_IMAGE=$(docker images --format "{{.Repository}}:{{.Tag}}" | grep "release-5-4-0" | head -1)
if [ -z "$VAST_IMAGE" ]; then
    VAST_IMAGE="vastdata.registry.local:5000/dev/orion:release-5-4-0-2043819"
    log_warn "Could not find VAST image, using default: $VAST_IMAGE"
fi
log_info "Using image: $VAST_IMAGE"

# Create temporary container to extract files
log_info "Extracting monitor_v2 from container image..."
docker rm -f temp_monitor_extract 2>/dev/null || true
docker create --name temp_monitor_extract "$VAST_IMAGE" >/dev/null 2>&1

# Copy monitor_v2 source
TEMP_DIR=$(mktemp -d)
docker cp temp_monitor_extract:/vast/install/pysrc/monitor_v2 "$TEMP_DIR/monitor_v2"
docker rm temp_monitor_extract >/dev/null 2>&1

# Install with force-reinstall to avoid any RECORD issues
log_info "Installing monitor_v2 package..."
sudo python3 -m pip install --force-reinstall --no-deps "$TEMP_DIR/monitor_v2" 2>&1 | tail -5

# Cleanup
rm -rf "$TEMP_DIR"

# Verify installation
if pip3 show monitor-v2 &>/dev/null; then
    VERSION=$(pip3 show monitor-v2 | grep Version | awk '{print $2}')
    log_info "monitor-v2 version $VERSION installed successfully"
else
    log_error "monitor-v2 installation failed!"
    exit 1
fi

#-------------------------------------------------------------------------------
# Clean orphaned temp directories
#-------------------------------------------------------------------------------
log_step "[3/5] Cleaning orphaned temp directories..."

ORPHAN_COUNT=$(ls -d /tmp/???????? 2>/dev/null | wc -l || echo "0")
if [ "$ORPHAN_COUNT" -gt 0 ]; then
    log_warn "Found $ORPHAN_COUNT orphaned monitor install directories"
    sudo rm -rf /tmp/????????
    log_info "Cleaned up orphaned directories"
else
    log_info "No orphaned directories found"
fi

# Clean pip temp directories
sudo rm -rf /tmp/pip-uninstall-* 2>/dev/null || true
sudo rm -rf /tmp/pip-ephem-wheel-cache-* 2>/dev/null || true

#-------------------------------------------------------------------------------
# Check file descriptor status
#-------------------------------------------------------------------------------
log_step "[4/5] Checking file descriptor status..."

FD_INFO=$(cat /proc/sys/fs/file-nr)
FD_USED=$(echo "$FD_INFO" | awk '{print $1}')
FD_MAX=$(echo "$FD_INFO" | awk '{print $3}')
FD_PERCENT=$((FD_USED * 100 / FD_MAX))

log_info "File descriptors: $FD_USED used / $FD_MAX max ($FD_PERCENT%)"

if [ "$FD_PERCENT" -gt 50 ]; then
    log_warn "FD usage is high ($FD_PERCENT%) - monitor closely"
elif [ "$FD_PERCENT" -gt 80 ]; then
    log_error "FD usage is critical ($FD_PERCENT%) - investigate immediately"
fi

# Check for any recent FD exhaustion in dmesg
if dmesg | grep -q "file-max limit.*reached" 2>/dev/null; then
    log_warn "Kernel has previously hit file-max limit - check dmesg for details"
fi

#-------------------------------------------------------------------------------
# Container health check
#-------------------------------------------------------------------------------
log_step "[5/5] Checking container health..."

if [ "$RUNNING_CONTAINERS" -gt 0 ]; then
    echo ""
    echo "Container Status:"
    echo "----------------"
    docker ps --filter "name=vast" --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}" | head -10
    
    echo ""
    echo "Container Resource Usage:"
    echo "------------------------"
    docker stats --no-stream --format "table {{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}\t{{.PIDs}}" | grep -E "vast|NAME"
fi

#-------------------------------------------------------------------------------
# Summary
#-------------------------------------------------------------------------------
echo ""
echo "==============================================================================="
echo " Post-Start Fixes Complete"
echo "==============================================================================="
echo ""
echo "Status:"
echo "  ✓ monitor-v2 pre-installed (version $(pip3 show monitor-v2 | grep Version | awk '{print $2}'))"
echo "  ✓ Orphaned temp directories cleaned"
echo "  ✓ File descriptors: $FD_USED / $FD_MAX ($FD_PERCENT%)"
echo "  ✓ Running containers: $RUNNING_CONTAINERS"
echo ""
echo "Recommendation:"
echo "  Monitor FD usage during cluster activation with:"
echo "    watch -n 5 'cat /proc/sys/fs/file-nr'"
echo ""
echo "==============================================================================="
