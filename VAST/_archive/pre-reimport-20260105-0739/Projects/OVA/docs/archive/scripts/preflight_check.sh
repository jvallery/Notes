#!/bin/bash
# =============================================================================
# VAST Pre-Flight Check
# =============================================================================
# Run this before VAST installation to verify system is properly configured
# =============================================================================

echo "=============================================="
echo " VAST Pre-Flight System Check"
echo " $(date)"
echo "=============================================="
echo ""

PASS=0
WARN=0
FAIL=0

check_pass() { echo "  ✓ $1"; ((PASS++)); }
check_warn() { echo "  ⚠ $1"; ((WARN++)); }
check_fail() { echo "  ✗ $1"; ((FAIL++)); }

# ==========================================================================
# CPU Checks
# ==========================================================================
echo "=== CPU ==="
VCPUS=$(nproc)
if [ "$VCPUS" -le 16 ]; then
    check_pass "vCPUs: $VCPUS (good - not over-subscribed)"
else
    check_warn "vCPUs: $VCPUS (consider reducing to 12-16 to avoid scheduling stalls)"
fi

CPU_TYPE=$(grep "model name" /proc/cpuinfo | head -1 | cut -d: -f2 | xargs)
if echo "$CPU_TYPE" | grep -qiE "QEMU|kvm64"; then
    check_warn "CPU type: $CPU_TYPE (consider 'host' passthrough for better perf)"
else
    check_pass "CPU type: $CPU_TYPE"
fi

# Check for nested virt
if [ -f /sys/module/kvm_amd/parameters/nested ]; then
    NESTED=$(cat /sys/module/kvm_amd/parameters/nested)
elif [ -f /sys/module/kvm_intel/parameters/nested ]; then
    NESTED=$(cat /sys/module/kvm_intel/parameters/nested)
else
    NESTED="unknown"
fi
if [ "$NESTED" = "1" ] || [ "$NESTED" = "Y" ]; then
    check_pass "Nested virtualization: enabled"
else
    check_fail "Nested virtualization: NOT enabled (required for VAST)"
fi

echo ""

# ==========================================================================
# Memory Checks
# ==========================================================================
echo "=== Memory ==="
TOTAL_MEM_GB=$(free -g | awk '/Mem:/{print $2}')
if [ "$TOTAL_MEM_GB" -ge 120 ]; then
    check_pass "Total RAM: ${TOTAL_MEM_GB}GB (good)"
elif [ "$TOTAL_MEM_GB" -ge 100 ]; then
    check_warn "Total RAM: ${TOTAL_MEM_GB}GB (borderline - 128GB recommended)"
else
    check_fail "Total RAM: ${TOTAL_MEM_GB}GB (too low - need 112GB+)"
fi

SWAP_USED=$(free -m | awk '/Swap:/{print $3}')
if [ "$SWAP_USED" -eq 0 ]; then
    check_pass "Swap usage: 0 (good)"
else
    check_warn "Swap usage: ${SWAP_USED}MB (consider disabling swap)"
fi

SWAPPINESS=$(sysctl -n vm.swappiness)
if [ "$SWAPPINESS" -le 10 ]; then
    check_pass "Swappiness: $SWAPPINESS (good)"
else
    check_warn "Swappiness: $SWAPPINESS (should be 10 or lower)"
fi

THP=$(cat /sys/kernel/mm/transparent_hugepage/enabled | grep -o '\[.*\]' | tr -d '[]')
if [ "$THP" = "never" ]; then
    check_pass "Transparent Huge Pages: disabled (good)"
else
    check_warn "Transparent Huge Pages: $THP (should be 'never' to avoid latency)"
fi

echo ""

# ==========================================================================
# Storage Checks
# ==========================================================================
echo "=== Storage ==="

# Check disk controller
if lsmod | grep -q virtio_scsi; then
    check_pass "Disk controller: VirtIO SCSI (good)"
elif lsmod | grep -q vmw_pvscsi; then
    check_warn "Disk controller: VMware PVSCSI (consider VirtIO for Proxmox)"
else
    DISK_MOD=$(lsmod | grep -E "scsi|ata" | head -1 | awk '{print $1}')
    check_warn "Disk controller: $DISK_MOD"
fi

# Check I/O scheduler
SCHED=$(cat /sys/block/sda/queue/scheduler 2>/dev/null | grep -o '\[.*\]' | tr -d '[]')
if [ "$SCHED" = "mq-deadline" ] || [ "$SCHED" = "none" ]; then
    check_pass "I/O scheduler: $SCHED (good for low latency)"
else
    check_warn "I/O scheduler: $SCHED (consider mq-deadline)"
fi

# Check disk space
DISK_FREE=$(df -BG / | awk 'NR==2{print $4}' | tr -d 'G')
if [ "$DISK_FREE" -ge 500 ]; then
    check_pass "Free disk space: ${DISK_FREE}GB"
elif [ "$DISK_FREE" -ge 200 ]; then
    check_warn "Free disk space: ${DISK_FREE}GB (may be tight)"
else
    check_fail "Free disk space: ${DISK_FREE}GB (need more space)"
fi

echo ""

# ==========================================================================
# Network Checks
# ==========================================================================
echo "=== Network ==="

# Check guest agent
if systemctl is-active qemu-guest-agent &>/dev/null; then
    check_pass "qemu-guest-agent: running"
else
    check_warn "qemu-guest-agent: not running"
fi

if systemctl is-enabled vmtoolsd &>/dev/null 2>&1; then
    check_warn "vmtoolsd: still enabled (should be disabled for Proxmox)"
else
    check_pass "vmtoolsd: disabled/not present"
fi

# Check network buffers
RMEM_MAX=$(sysctl -n net.core.rmem_max 2>/dev/null)
if [ "$RMEM_MAX" -ge 100000000 ]; then
    check_pass "Network buffers: tuned (rmem_max=${RMEM_MAX})"
else
    check_warn "Network buffers: default (consider tuning)"
fi

echo ""

# ==========================================================================
# Docker Check
# ==========================================================================
echo "=== Docker ==="

if command -v docker &>/dev/null; then
    DOCKER_VERSION=$(docker --version 2>/dev/null | awk '{print $3}' | tr -d ',')
    check_pass "Docker installed: $DOCKER_VERSION"
    
    if systemctl is-active docker &>/dev/null; then
        check_pass "Docker service: running"
    else
        check_warn "Docker service: not running"
    fi
else
    check_warn "Docker: not installed (will be installed during VAST setup)"
fi

echo ""

# ==========================================================================
# Scripts Check
# ==========================================================================
echo "=== Scripts ==="

for script in vast_proxmox_install.sh monitor_install.sh; do
    if [ -x "/home/centos/$script" ]; then
        check_pass "$script: present and executable"
    elif [ -f "/home/centos/$script" ]; then
        check_warn "$script: present but not executable"
    else
        check_fail "$script: MISSING"
    fi
done

echo ""

# ==========================================================================
# Summary
# ==========================================================================
echo "=============================================="
echo " Summary: $PASS passed, $WARN warnings, $FAIL failed"
echo "=============================================="

if [ "$FAIL" -gt 0 ]; then
    echo ""
    echo " ⚠ Address failed items before proceeding!"
    exit 1
elif [ "$WARN" -gt 0 ]; then
    echo ""
    echo " Consider addressing warnings for best results."
    exit 0
else
    echo ""
    echo " ✓ System is ready for VAST installation!"
    exit 0
fi
