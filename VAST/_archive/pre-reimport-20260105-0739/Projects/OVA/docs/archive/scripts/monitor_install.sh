#!/bin/bash
# =============================================================================
# VAST Installation Monitoring Script - Enhanced Edition
# =============================================================================
# Based on ChatGPT's "Test 0" instrumentation recommendations
# Run this BEFORE starting cluster create to capture evidence of stalls
#
# Usage: ./monitor_install.sh [start|stop|status]
# =============================================================================

LOG_DIR="/home/centos/install_monitoring_$(date +%Y%m%d_%H%M%S)"
PID_FILE="/tmp/vast_monitor_pids.txt"

start_monitoring() {
    mkdir -p "$LOG_DIR"
    
    echo "=============================================="
    echo " VAST Installation Monitoring - Starting"
    echo " Log directory: $LOG_DIR"
    echo "=============================================="
    echo ""

    # Check for required tools
    for tool in vmstat iostat mpstat pidstat tcpdump ss; do
        if ! command -v $tool &> /dev/null; then
            echo "WARNING: $tool not found. Some metrics will be missing."
        fi
    done

    # ==========================================================================
    # CPU Monitoring (detect scheduling stalls / steal time)
    # ==========================================================================
    
    # vmstat - overall system (1 second interval for fine-grained detection)
    echo "Starting vmstat (1s interval)..."
    vmstat -t 1 > "$LOG_DIR/vmstat.log" 2>&1 &
    echo "vmstat:$!" >> "$PID_FILE"

    # mpstat - per-CPU stats (shows %steal which indicates hypervisor stealing CPU)
    echo "Starting mpstat (1s interval, all CPUs)..."
    mpstat -P ALL 1 > "$LOG_DIR/mpstat.log" 2>&1 &
    echo "mpstat:$!" >> "$PID_FILE"

    # pidstat - per-process CPU/memory/IO (helps identify which process is suffering)
    echo "Starting pidstat (1s interval)..."
    pidstat -urd 1 > "$LOG_DIR/pidstat.log" 2>&1 &
    echo "pidstat:$!" >> "$PID_FILE"

    # ==========================================================================
    # I/O Monitoring (detect storage latency spikes)
    # ==========================================================================
    
    # iostat - disk I/O with extended stats (await is key metric)
    echo "Starting iostat (1s interval, extended stats)..."
    iostat -xzt 1 > "$LOG_DIR/iostat.log" 2>&1 &
    echo "iostat:$!" >> "$PID_FILE"

    # ==========================================================================
    # Memory Monitoring (detect swapping / memory pressure)
    # ==========================================================================
    
    echo "Starting memory monitor (5s interval)..."
    ( while true; do
        echo "=== $(date '+%Y-%m-%d %H:%M:%S.%3N') ===" >> "$LOG_DIR/memory.log"
        free -h >> "$LOG_DIR/memory.log"
        grep -E "MemTotal|MemFree|MemAvailable|Buffers|Cached|SwapTotal|SwapFree|Dirty|Writeback|AnonPages" /proc/meminfo >> "$LOG_DIR/memory.log"
        echo "" >> "$LOG_DIR/memory.log"
        sleep 5
    done ) &
    echo "memory:$!" >> "$PID_FILE"

    # ==========================================================================
    # Network Monitoring (detect leader connection failures)
    # ==========================================================================
    
    # Port 6001 connection state (ChatGPT's recommendation)
    echo "Starting port 6001 connection monitor (1s interval)..."
    ( while true; do
        echo "=== $(date '+%Y-%m-%d %H:%M:%S.%3N') ===" >> "$LOG_DIR/ss_6001.log"
        ss -tn 'sport = :6001 or dport = :6001' >> "$LOG_DIR/ss_6001.log" 2>/dev/null
        echo "" >> "$LOG_DIR/ss_6001.log"
        sleep 1
    done ) &
    echo "ss_6001:$!" >> "$PID_FILE"

    # tcpdump capture for post-mortem analysis
    echo "Starting tcpdump on port 6001..."
    tcpdump -i any port 6001 -w "$LOG_DIR/port_6001.pcap" 2>"$LOG_DIR/tcpdump.err" &
    echo "tcpdump:$!" >> "$PID_FILE"

    # ==========================================================================
    # Docker Container Monitoring
    # ==========================================================================
    
    echo "Starting docker stats (5s interval)..."
    ( while true; do
        echo "=== $(date '+%Y-%m-%d %H:%M:%S.%3N') ===" >> "$LOG_DIR/docker_stats.log"
        docker stats --no-stream --format "table {{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}\t{{.MemPerc}}\t{{.NetIO}}\t{{.BlockIO}}\t{{.PIDs}}" >> "$LOG_DIR/docker_stats.log" 2>/dev/null || echo "Docker not running" >> "$LOG_DIR/docker_stats.log"
        echo "" >> "$LOG_DIR/docker_stats.log"
        sleep 5
    done ) &
    echo "docker:$!" >> "$PID_FILE"

    # ==========================================================================
    # Kernel / System Events
    # ==========================================================================
    
    # dmesg watcher (catches OOM, hardware errors, etc.)
    echo "Starting dmesg watcher..."
    dmesg -wT > "$LOG_DIR/dmesg_live.log" 2>&1 &
    echo "dmesg:$!" >> "$PID_FILE"

    # Load average with timestamps
    echo "Starting load average monitor (1s interval)..."
    ( while true; do
        echo "$(date '+%Y-%m-%d %H:%M:%S.%3N') $(cat /proc/loadavg)" >> "$LOG_DIR/loadavg.log"
        sleep 1
    done ) &
    echo "loadavg:$!" >> "$PID_FILE"

    # ==========================================================================
    # Gap Detection (detect multi-second stalls)
    # ==========================================================================
    
    # Heartbeat - writes timestamp every second. Gaps indicate VM pauses.
    echo "Starting heartbeat (gap detector)..."
    ( while true; do
        echo "$(date '+%Y-%m-%d %H:%M:%S.%3N')" >> "$LOG_DIR/heartbeat.log"
        sleep 1
    done ) &
    echo "heartbeat:$!" >> "$PID_FILE"

    # Save log directory path
    echo "$LOG_DIR" > /tmp/vast_monitor_logdir.txt

    echo ""
    echo "=============================================="
    echo " Monitoring started successfully!"
    echo "=============================================="
    echo ""
    echo "Logs being collected:"
    echo "  CPU:"
    echo "    - vmstat.log      : System-wide CPU, memory, swap (1s)"
    echo "    - mpstat.log      : Per-CPU stats including %steal (1s)"
    echo "    - pidstat.log     : Per-process CPU/mem/IO (1s)"
    echo ""
    echo "  Storage:"
    echo "    - iostat.log      : Disk I/O latency (await) (1s)"
    echo ""
    echo "  Memory:"
    echo "    - memory.log      : Detailed memory stats (5s)"
    echo ""
    echo "  Network:"
    echo "    - ss_6001.log     : Port 6001 connection states (1s)"
    echo "    - port_6001.pcap  : Full packet capture"
    echo ""
    echo "  System:"
    echo "    - dmesg_live.log  : Kernel messages"
    echo "    - loadavg.log     : System load (1s)"
    echo "    - heartbeat.log   : Gap detector (1s)"
    echo "    - docker_stats.log: Container resources (5s)"
    echo ""
    echo "To stop: $0 stop"
    echo ""
    echo "=============================================="
    echo " KEY METRICS TO WATCH FOR STALLS:"
    echo "=============================================="
    echo "  %st (steal) in mpstat    → Hypervisor stealing CPU"
    echo "  await in iostat          → Disk latency (ms)"
    echo "  si/so in vmstat          → Swap in/out"
    echo "  Gaps in heartbeat.log    → VM pauses"
    echo "=============================================="
}

stop_monitoring() {
    echo "Stopping monitoring..."
    
    if [ -f "$PID_FILE" ]; then
        while IFS=: read -r name pid; do
            if kill -0 "$pid" 2>/dev/null; then
                kill "$pid" 2>/dev/null && echo "  Stopped: $name (PID $pid)"
            fi
        done < "$PID_FILE"
        rm -f "$PID_FILE"
    else
        echo "No PID file found."
    fi

    if [ -f /tmp/vast_monitor_logdir.txt ]; then
        LOG_DIR=$(cat /tmp/vast_monitor_logdir.txt)
        echo ""
        echo "Logs saved to: $LOG_DIR"
        echo ""
        echo "Log file sizes:"
        du -sh "$LOG_DIR"/* 2>/dev/null | sort -h
        echo ""
        echo "Quick analysis commands:"
        echo "  # Check for CPU steal:"
        echo "  grep -E 'Average|%steal' $LOG_DIR/mpstat.log | tail -20"
        echo ""
        echo "  # Check for I/O latency spikes (await > 100ms is concerning):"
        echo "  awk '\$10 > 100 {print}' $LOG_DIR/iostat.log | head -20"
        echo ""
        echo "  # Check for gaps (VM pauses) - look for time jumps > 2s:"
        echo "  awk 'NR>1 {split(\$2,a,\":\"); cur=a[1]*3600+a[2]*60+a[3]; if(prev && cur-prev>2) print \"GAP:\",prev_line,\"->\",\$0; prev=cur; prev_line=\$0}' $LOG_DIR/heartbeat.log"
        echo ""
        echo "  # Check for swap activity:"
        echo "  awk '\$7>0 || \$8>0 {print}' $LOG_DIR/vmstat.log"
    fi
    
    echo "Monitoring stopped."
}

status_monitoring() {
    if [ -f "$PID_FILE" ]; then
        echo "Monitoring processes:"
        while IFS=: read -r name pid; do
            if kill -0 "$pid" 2>/dev/null; then
                echo "  ✓ $name (PID $pid) - running"
            else
                echo "  ✗ $name (PID $pid) - stopped"
            fi
        done < "$PID_FILE"
        
        if [ -f /tmp/vast_monitor_logdir.txt ]; then
            LOG_DIR=$(cat /tmp/vast_monitor_logdir.txt)
            echo ""
            echo "Log directory: $LOG_DIR"
            echo "Current sizes:"
            du -sh "$LOG_DIR" 2>/dev/null
        fi
    else
        echo "No monitoring session active."
    fi
}

case "${1:-}" in
    start)
        if [ -f "$PID_FILE" ]; then
            echo "Monitoring already running. Stop first with: $0 stop"
            exit 1
        fi
        start_monitoring
        ;;
    stop)
        stop_monitoring
        ;;
    status)
        status_monitoring
        ;;
    *)
        echo "Usage: $0 {start|stop|status}"
        echo ""
        echo "  start  - Start all monitoring processes"
        echo "  stop   - Stop monitoring and show analysis hints"
        echo "  status - Show running monitors"
        exit 1
        ;;
esac
