#!/bin/bash

export BUILD=release-5-4-0-2043819

export PIPE=$(echo $BUILD | awk -F'-' '{print $NF}')
export DISABLE_IPV6_FOR_LOOPBACK=yes
export MGMT_IFACE=$(hostname -I | awk '{print $1}')
export MGMT_IFACE_NAME=$(netstat -ie | grep -B1 "${MGMT_IFACE}" | head -n1 | awk '{print $1}' | sed 's/.$//')
export VAST_INSTALL_ARGS='--vsettings CAS_OVER_RPC=true,IN_CLUSTER_COMMUNICATION_TCP=true'

export VMAN_USER_PASSWORD='-u admin -p 123456'
export pem_file=/vast/deploy/ssh_key.pem
export EXTRA_VOLUME_MOUNTS="-v /file_server:/file_server"


#ipv6 is disabled for management interface
echo 1 | sudo tee /proc/sys/net/ipv6/conf/$MGMT_IFACE_NAME/disable_ipv6

# setup hack to avoid trying to access the image registry on AWS
sudo mkdir -p /file_server
sudo chown centos /file_server
echo "vastdata.registry.local:5000" > /file_server/DCACHE

# stop running containers (besides the local_registry)
echo "$(date --rfc-3339=seconds) - Stopping vast containers"
docker ps -aq --format "{{.ID}} {{.Names}}" | grep -v " registry" | cut -d' ' -f 1 | xargs --no-run-if-empty docker stop | xargs --no-run-if-empty docker rm

# clean hugepages
echo "$(date --rfc-3339=seconds) - Clearing hugepages"
echo 0 | sudo tee /proc/sys/vm/nr_hugepages

echo '1.1.1' | sudo tee /etc/vast-os-release && sudo chmod 644 /etc/vast-os-release
mkdir -p /vast/bundles/  /vast/deploy/

# setup SSH key
if [ ! -f "$pem_file" ]; then
  echo "$(date --rfc-3339=seconds) - Setting up ssh key"
  rsa_file=~/.ssh/id_rsa
  [ ! -f "$rsa_file" ] && ssh-keygen -f $rsa_file -q -N ""
  cat $rsa_file.pub >> ~/.ssh/authorized_keys
  # copying this so that vast_bootsrap does not erase the ~/.ssh dir!!
  cp $rsa_file $pem_file
fi  

# start VMS
echo "$(date --rfc-3339=seconds) - Starting vast_bootstrap"
/vast/bundles/vast_bootstrap.sh --interface ${MGMT_IFACE} --skip-prompt #--use-existing-bundle
echo "$(date --rfc-3339=seconds) - Finished vast_bootstrap"


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

# cluster create
echo "$(date --rfc-3339=seconds) - creating cluster"
cd /vast/deploy/
./vman.sh $BUILD $pem_file vcli $VMAN_USER_PASSWORD -c cluster create --build ${BUILD} ${VAST_INSTALL_ARGS} --name lb-${BUILD} --loopback
echo "$(date --rfc-3339=seconds) - finished cluster creation"
