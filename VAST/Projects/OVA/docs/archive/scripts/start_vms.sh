#!/bin/bash

export MGMT_IFACE=$(hostname -I | awk '{print $1}')
export MGMT_IFACE_NAME=$(netstat -ie | grep -B1 "${MGMT_IFACE}" | head -n1 | awk '{print $1}' | sed 's/.$//')
echo 1 | sudo tee /proc/sys/net/ipv6/conf/$MGMT_IFACE_NAME/disable_ipv6
rm -f /vast/vman/mgmt-vip-ivp6
hostname -I | awk '{print $1}' > /vast/vman/mgmt-vip
CONTAINER_NAME="vast_platform_11.0.0.1-4100"

docker cp /vast/data/vms_image $CONTAINER_NAME:/vast/data/vms_image
docker exec -e DISABLE_IPV6_FOR_LOOPBACK=yes $CONTAINER_NAME bash -c 'sudo DISABLE_IPV6_FOR_LOOPBACK=yes /vast/bin/vms-bringup start'