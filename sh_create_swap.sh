#!/bin/bash

# Define the swap size (change this value as needed)
SWAP_SIZE=2G
SWAP_FILE="/swapfile"
SWAP_CONF="/etc/fstab"

# Function to check if swap already exists
check_swap() {
    if swapon --show; then
        echo "Swap space already exists."
        exit 1
    fi
}

# Function to check available disk space
check_disk_space() {
    local available=$(df -h | grep '^/dev' | awk '{print $4}' | sed 's/[GMB]//g' | sort -n | tail -n 1)
    local required=$(echo $SWAP_SIZE | sed 's/G//;s/M//')

    if (( available < required )); then
        echo "Not enough disk space available for a $SWAP_SIZE swap file."
        exit 1
    fi
}

# Function to create swap file
create_swap_file() {
    echo "Creating swap file of size $SWAP_SIZE..."
    sudo fallocate -l $SWAP_SIZE $SWAP_FILE || {
        echo "Failed to create swap file with fallocate. Trying dd..."
        sudo dd if=/dev/zero of=$SWAP_FILE bs=1M count=$(echo $SWAP_SIZE | sed 's/G/2048/;s/M/1024/') || exit 1
    }
    sudo chmod 600 $SWAP_FILE
    sudo mkswap $SWAP_FILE
}

# Function to enable swap file
enable_swap_file() {
    echo "Enabling swap file..."
    sudo swapon $SWAP_FILE
    echo "$SWAP_FILE none swap sw 0 0" | sudo tee -a $SWAP_CONF
}

# Function to adjust swappiness
adjust_swappiness() {
    local new_swappiness=10
    echo "Setting swappiness to $new_swappiness..."
    sudo sysctl vm.swappiness=$new_swappiness
    echo "vm.swappiness=$new_swappiness" | sudo tee -a /etc/sysctl.conf
}

# Main script execution
check_swap
check_disk_space
create_swap_file
enable_swap_file
adjust_swappiness

# Show the final status of memory and swap
free -h
echo "Swap setup complete."
