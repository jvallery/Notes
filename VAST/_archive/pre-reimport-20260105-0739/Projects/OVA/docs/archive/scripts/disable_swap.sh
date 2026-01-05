#!/bin/bash
echo "Current swap: $(swapon --show 2>/dev/null | tail -1 || echo 'none')"
echo "Disabling swap..."
sudo swapoff -a
sudo sed -i '/swap/s/^/#/' /etc/fstab
echo "Done. Swap disabled."
swapon --show 2>/dev/null || echo "No swap active"
