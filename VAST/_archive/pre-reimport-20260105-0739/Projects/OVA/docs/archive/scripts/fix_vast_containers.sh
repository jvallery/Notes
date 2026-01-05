#!/bin/bash
#
# fix_vast_containers.sh - Fix VAST loopback container bugs
#
# This script must be run EVERY TIME after VAST containers start.
# It fixes bugs in the VAST container images that prevent proper operation.
#
# Bugs fixed:
# 1. Missing rsync - Required for monitor package installation
#
# Usage:
#   ./fix_vast_containers.sh
#
# Created: December 30, 2025
#

set -e

CONTAINERS=(
    "vast_platform_11.0.0.1-4100"
    "vast_platform_11.0.0.1-4200"
    "vast_platform_11.0.0.1-4300"
    "vast_platform_11.0.0.1-4400"
)

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo "========================================"
echo "VAST Loopback Container Fix Script"
echo "========================================"
echo ""

# Check rsync exists on host
if [[ ! -f /usr/bin/rsync ]]; then
    echo -e "${RED}ERROR: rsync not found on host. Install with:${NC}"
    echo "  sudo dnf install -y rsync"
    exit 1
fi

# Copy rsync to all running containers
echo "Copying rsync to VAST platform containers..."
echo ""

for container in "${CONTAINERS[@]}"; do
    if docker ps --format '{{.Names}}' | grep -q "^${container}$"; then
        echo -n "  $container: "
        if sudo docker cp /usr/bin/rsync "$container:/usr/bin/rsync" 2>/dev/null; then
            echo -e "${GREEN}OK${NC}"
        else
            echo -e "${RED}FAILED${NC}"
        fi
    else
        echo -e "  $container: ${YELLOW}NOT RUNNING (skipped)${NC}"
    fi
done

echo ""
echo "========================================"
echo "Container fix complete"
echo "========================================"
echo ""

# Check cluster health
VAST_IP="${VAST_IP:-192.168.30.109}"
VAST_USER="${VAST_USER:-admin}"
VAST_PASS="${VAST_PASS:-123456}"

echo "Checking cluster health..."
echo ""

# Check if API is responding
if curl -sk -u "${VAST_USER}:${VAST_PASS}" "https://${VAST_IP}/api/clusters/" >/dev/null 2>&1; then
    echo "CNodes:"
    curl -sk -u "${VAST_USER}:${VAST_PASS}" "https://${VAST_IP}/api/cnodes/" 2>/dev/null | \
        python3 -c "import sys,json; [print(f'  {c[\"name\"]}: {c[\"state\"]}') for c in json.load(sys.stdin)]" 2>/dev/null || echo "  (unable to parse)"
    
    echo ""
    echo "DNodes:"
    curl -sk -u "${VAST_USER}:${VAST_PASS}" "https://${VAST_IP}/api/dnodes/" 2>/dev/null | \
        python3 -c "import sys,json; [print(f'  {d[\"name\"]}: {d[\"state\"]}') for d in json.load(sys.stdin)]" 2>/dev/null || echo "  (unable to parse)"
else
    echo -e "${YELLOW}VMS API not responding. Cluster may still be starting.${NC}"
    echo "Wait 2-3 minutes and check manually:"
    echo "  curl -sk -u admin:123456 'https://${VAST_IP}/api/cnodes/'"
fi

echo ""
echo "Done."
