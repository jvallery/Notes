#!/bin/bash
# =============================================================================
# VAST 5.4 Proxmox Pre-Installation Preparation Script
# =============================================================================
# Run this script on a CLEAN VM before attempting VAST installation
# This script prepares the VM for VirtIO SCSI conversion and optimizes settings
#
# After running this script:
#   1. Shut down the VM
#   2. In Proxmox: Change SCSI controller to "VirtIO SCSI single"
#   3. In Proxmox: Enable "IO thread" on the disk
#   4. In Proxmox: Increase RAM to 128GB+, disable ballooning
#   5. In Proxmox: Set CPU type to "host"
#   6. Boot the VM
#   7. Snapshot as new baseline
#   8. Proceed with VAST installation
# =============================================================================

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

log_info() { echo -e "${GREEN}[INFO]${NC} $1"; }
log_warn() { echo -e "${YELLOW}[WARN]${NC} $1"; }
log_error() { echo -e "${RED}[ERROR]${NC} $1"; }

# Check if running as root
if [ "$EUID" -ne 0 ]; then
    log_error "Please run as root: sudo $0"
    exit 1
fi

echo "=============================================="
echo " VAST 5.4 Proxmox VM Preparation"
echo " $(date)"
echo "=============================================="
echo ""

# =============================================================================
# PHASE 1: Add VirtIO Drivers to Initramfs
# =============================================================================
log_info "PHASE 1: Adding VirtIO drivers to initramfs..."

# Check if VirtIO modules exist
if [ ! -f "/lib/modules/$(uname -r)/kernel/drivers/scsi/virtio_scsi.ko.xz" ]; then
    log_error "VirtIO SCSI module not found! Cannot proceed."
    exit 1
fi

# Create dracut configuration
cat > /etc/dracut.conf.d/virtio.conf << 'EOF'
# Add VirtIO drivers for Proxmox/KVM boot disk
add_drivers+=" virtio_scsi virtio_blk "
EOF
log_info "Created /etc/dracut.conf.d/virtio.conf"

# Backup current initramfs
KERNEL=$(uname -r)
if [ ! -f "/boot/initramfs-${KERNEL}.img.pre-virtio" ]; then
    cp /boot/initramfs-${KERNEL}.img /boot/initramfs-${KERNEL}.img.pre-virtio
    log_info "Backed up initramfs to /boot/initramfs-${KERNEL}.img.pre-virtio"
else
    log_warn "Backup already exists, skipping"
fi

# Rebuild initramfs
log_info "Rebuilding initramfs (this takes a minute)..."
dracut -f /boot/initramfs-${KERNEL}.img ${KERNEL}

# Verify
if lsinitrd /boot/initramfs-${KERNEL}.img | grep -q virtio_scsi; then
    log_info "✓ VirtIO SCSI driver successfully added to initramfs"
else
    log_error "VirtIO SCSI driver NOT found in initramfs!"
    exit 1
fi

echo ""

# =============================================================================
# PHASE 2: Install Required Packages
# =============================================================================
log_info "PHASE 2: Installing required packages..."

# Install monitoring tools
yum install -y sysstat tcpdump qemu-guest-agent 2>/dev/null || dnf install -y sysstat tcpdump qemu-guest-agent

# Enable qemu-guest-agent
systemctl enable --now qemu-guest-agent

# Disable vmtoolsd if present (VMware artifact)
if systemctl is-enabled vmtoolsd 2>/dev/null; then
    systemctl disable --now vmtoolsd 2>/dev/null || true
    log_info "Disabled vmtoolsd (VMware guest tools)"
fi

log_info "✓ Packages installed"
echo ""

# =============================================================================
# PHASE 3: System Tuning (sysctl)
# =============================================================================
log_info "PHASE 3: Applying system tuning..."

cat > /etc/sysctl.d/99-vast-tuning.conf << 'EOF'
# ===========================================
# VAST Data Cluster Optimization
# ===========================================

# --- Memory Management ---
vm.swappiness = 10
vm.overcommit_memory = 0
vm.dirty_ratio = 40
vm.dirty_background_ratio = 10
vm.zone_reclaim_mode = 0

# --- File System ---
fs.file-max = 2097152
fs.inotify.max_user_watches = 524288
fs.inotify.max_user_instances = 512
fs.aio-max-nr = 1048576

# --- Network: Core ---
net.core.rmem_max = 134217728
net.core.wmem_max = 134217728
net.core.rmem_default = 16777216
net.core.wmem_default = 16777216
net.core.somaxconn = 65535
net.core.netdev_max_backlog = 65535

# --- Network: TCP ---
net.ipv4.tcp_rmem = 4096 87380 134217728
net.ipv4.tcp_wmem = 4096 65536 134217728
net.ipv4.tcp_window_scaling = 1
net.ipv4.tcp_keepalive_time = 60
net.ipv4.tcp_keepalive_intvl = 10
net.ipv4.tcp_keepalive_probes = 6
net.ipv4.tcp_fin_timeout = 15
net.ipv4.tcp_fastopen = 3
net.ipv4.tcp_max_orphans = 65535
net.ipv4.tcp_max_syn_backlog = 65535

# --- Kernel ---
kernel.pid_max = 4194304
kernel.hung_task_timeout_secs = 120
kernel.msgmax = 65536
kernel.msgmnb = 65536
EOF

sysctl -p /etc/sysctl.d/99-vast-tuning.conf 2>&1 | grep -v "No such file" || true
log_info "✓ Sysctl settings applied"

# =============================================================================
# PHASE 4: Ulimits
# =============================================================================
log_info "PHASE 4: Configuring ulimits..."

cat > /etc/security/limits.d/99-vast.conf << 'EOF'
# VAST Data ulimits
*               soft    nofile          1048576
*               hard    nofile          1048576
*               soft    nproc           unlimited
*               hard    nproc           unlimited
*               soft    memlock         unlimited
*               hard    memlock         unlimited
*               soft    core            unlimited
*               hard    core            unlimited
root            soft    nofile          1048576
root            hard    nofile          1048576
EOF

log_info "✓ Ulimits configured"
echo ""

# =============================================================================
# PHASE 5: Disable Unnecessary Services
# =============================================================================
log_info "PHASE 5: Disabling unnecessary services..."

for svc in tuned kdump rhsmcertd insights-client mdmonitor; do
    if systemctl is-enabled "$svc" 2>/dev/null | grep -q enabled; then
        systemctl disable --now "$svc" 2>/dev/null || true
        log_info "  Disabled: $svc"
    fi
done
echo ""

# =============================================================================
# PHASE 6: I/O Scheduler & THP
# =============================================================================
log_info "PHASE 6: Optimizing I/O scheduler and memory..."

# Set I/O scheduler
for dev in /sys/block/sd*/queue/scheduler; do
    if [ -f "$dev" ]; then
        echo mq-deadline > "$dev" 2>/dev/null || true
    fi
done
log_info "✓ I/O scheduler set to mq-deadline"

# Disable transparent hugepages
if [ -f /sys/kernel/mm/transparent_hugepage/enabled ]; then
    echo never > /sys/kernel/mm/transparent_hugepage/enabled
fi
if [ -f /sys/kernel/mm/transparent_hugepage/defrag ]; then
    echo never > /sys/kernel/mm/transparent_hugepage/defrag
fi
log_info "✓ Transparent hugepages disabled"

# Create systemd service to persist on reboot
cat > /etc/systemd/system/vast-tuning.service << 'EOF'
[Unit]
Description=VAST System Tuning
After=local-fs.target

[Service]
Type=oneshot
ExecStart=/bin/bash -c 'for dev in /sys/block/sd*/queue/scheduler; do echo mq-deadline > "$dev" 2>/dev/null || true; done'
ExecStart=/bin/bash -c 'echo never > /sys/kernel/mm/transparent_hugepage/enabled 2>/dev/null || true'
ExecStart=/bin/bash -c 'echo never > /sys/kernel/mm/transparent_hugepage/defrag 2>/dev/null || true'
RemainAfterExit=yes

[Install]
WantedBy=multi-user.target
EOF

systemctl daemon-reload
systemctl enable vast-tuning.service
log_info "✓ Tuning service enabled for persistence"
echo ""

# =============================================================================
# PHASE 7: Create Monitoring Script
# =============================================================================
log_info "PHASE 7: Creating monitoring script..."

cat > /home/centos/monitor_install.sh << 'MONITOR_SCRIPT'
#!/bin/bash
# VAST Installation Monitoring Script
# Usage: ./monitor_install.sh [start|stop|status]

LOG_DIR="/home/centos/install_monitoring_$(date +%Y%m%d_%H%M%S)"
PID_FILE="/tmp/vast_monitor_pids.txt"

start_monitoring() {
    mkdir -p "$LOG_DIR"
    echo "Starting monitoring in $LOG_DIR"

    # System resources (every 5 seconds)
    vmstat -t 5 > "$LOG_DIR/vmstat.log" 2>&1 &
    echo "vmstat:$!" >> "$PID_FILE"

    # I/O stats
    iostat -xzt 5 > "$LOG_DIR/iostat.log" 2>&1 &
    echo "iostat:$!" >> "$PID_FILE"

    # Memory details
    ( while true; do
        echo "=== $(date '+%Y-%m-%d %H:%M:%S') ===" >> "$LOG_DIR/memory.log"
        free -h >> "$LOG_DIR/memory.log"
        grep -E "MemTotal|MemFree|MemAvailable|SwapFree|Dirty|Writeback" /proc/meminfo >> "$LOG_DIR/memory.log"
        sleep 10
    done ) &
    echo "memory:$!" >> "$PID_FILE"

    # Docker stats
    ( while true; do
        echo "=== $(date '+%Y-%m-%d %H:%M:%S') ===" >> "$LOG_DIR/docker_stats.log"
        docker stats --no-stream --format "table {{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}\t{{.NetIO}}\t{{.BlockIO}}" >> "$LOG_DIR/docker_stats.log" 2>/dev/null || true
        sleep 10
    done ) &
    echo "docker:$!" >> "$PID_FILE"

    # Network capture on port 6001 (leader communication)
    tcpdump -i any port 6001 -w "$LOG_DIR/port_6001.pcap" 2>/dev/null &
    echo "tcpdump:$!" >> "$PID_FILE"

    # dmesg watcher
    dmesg -wT > "$LOG_DIR/dmesg_live.log" 2>&1 &
    echo "dmesg:$!" >> "$PID_FILE"

    # Load average
    ( while true; do
        echo "$(date '+%Y-%m-%d %H:%M:%S') $(cat /proc/loadavg)" >> "$LOG_DIR/loadavg.log"
        sleep 5
    done ) &
    echo "loadavg:$!" >> "$PID_FILE"

    echo "$LOG_DIR" > /tmp/vast_monitor_logdir.txt
    echo ""
    echo "Monitoring started. Logs: $LOG_DIR"
    echo "To stop: $0 stop"
}

stop_monitoring() {
    echo "Stopping monitoring..."
    if [ -f "$PID_FILE" ]; then
        while IFS=: read -r name pid; do
            kill "$pid" 2>/dev/null && echo "Stopped $name"
        done < "$PID_FILE"
        rm -f "$PID_FILE"
    fi
    [ -f /tmp/vast_monitor_logdir.txt ] && echo "Logs saved to: $(cat /tmp/vast_monitor_logdir.txt)"
}

case "${1:-start}" in
    start) [ -f "$PID_FILE" ] && { echo "Already running. Stop first."; exit 1; }; start_monitoring ;;
    stop) stop_monitoring ;;
    status) [ -f "$PID_FILE" ] && cat "$PID_FILE" || echo "Not running" ;;
    *) echo "Usage: $0 [start|stop|status]" ;;
esac
MONITOR_SCRIPT

chmod +x /home/centos/monitor_install.sh
chown centos:centos /home/centos/monitor_install.sh
log_info "✓ Monitoring script created at /home/centos/monitor_install.sh"
echo ""

# =============================================================================
# SUMMARY
# =============================================================================
echo ""
echo "=============================================="
echo " PREPARATION COMPLETE"
echo "=============================================="
echo ""
echo "VirtIO Driver Status:"
lsinitrd /boot/initramfs-$(uname -r).img 2>/dev/null | grep -E "virtio_scsi|virtio_blk" | head -2
echo ""
echo "Current Memory:"
free -h | head -2
# =============================================================================
# PHASE 8: CPU Count Recommendation (IMPORTANT)
# =============================================================================
echo ""
log_warn "PHASE 8: CPU Configuration Recommendation"
echo ""
echo "  Your Proxmox host has a Threadripper 2920X (12 cores, 24 threads)."
echo "  Currently the VM may be assigned 24 vCPUs."
echo ""
echo "  RECOMMENDATION: Reduce vCPUs to 16 (or even 12)"
echo ""
echo "  WHY: VAST spawns polling threads per vCPU. With 24 vCPUs competing"
echo "  for 12 physical cores, you get heavy context switching. This can"
echo "  cause the 'stuck fiber' behavior we observed (keepalive timeouts)."
echo ""
echo "  Fewer vCPUs = fewer polling threads = less CPU contention = lower latency"
echo ""

# =============================================================================
# PHASE 9: Hugepages (OPTIONAL - Disabled by default)
# =============================================================================
log_info "PHASE 9: Hugepages configuration (informational only)"
echo ""
echo "  Current hugepages status:"
grep -E "HugePages_Total|Hugepagesize" /proc/meminfo | sed 's/^/    /'
echo ""
echo "  Static hugepages are NOT enabled by default."
echo "  VAST does not appear to require them, and pre-allocating them"
echo "  would lock memory away from normal use."
echo ""
echo "  THP (Transparent Huge Pages) has been DISABLED to prevent"
echo "  defragmentation-related latency spikes."
echo ""
# Uncomment below to experiment with static hugepages (40GB):
# echo "  Allocating 40GB of static hugepages..."
# sysctl -w vm.nr_hugepages=20480  # 40GB / 2MB = 20480 pages
# grep HugePages /proc/meminfo

echo ""
echo "=============================================="
echo " NEXT STEPS (on Proxmox host):"
echo "=============================================="
echo ""
echo "1. Shut down this VM:"
echo "   sudo shutdown -h now"
echo ""
echo "2. In Proxmox GUI, modify VM settings:"
echo "   • Hardware → SCSI Controller → VirtIO SCSI single"
echo "   • Hardware → Hard Disk → Edit → Check 'IO thread'"
echo "   • Hardware → Memory → 131072 MB (128GB)"
echo "   • Hardware → Memory → UNCHECK 'Ballooning Device'"
echo "   • Hardware → Processor → Type: 'host'"
echo "   • Hardware → Processor → Cores: 16 (reduce from 24)"
echo ""
echo "3. Boot the VM and verify it comes up"
echo ""
echo "4. Create a snapshot as new baseline"
echo ""
echo "5. Proceed with VAST installation"
echo ""
echo "=============================================="
