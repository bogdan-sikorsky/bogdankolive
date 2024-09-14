#!/bin/bash

# Define variables
KEY_NAME="github_deploy_key"
SSH_DIR="/home/ubuntu/.ssh"
KEY_PATH="/home/ubuntu/.ssh/ga_key"

# Create the .ssh directory if it doesn't exist
mkdir -p $SSH_DIR
chmod 700 $SSH_DIR

# Generate SSH key without passphrase
if [ ! -f "$KEY_PATH" ]; then
    ssh-keygen -t rsa -b 4096 -f "$KEY_PATH" -N ""
    echo "SSH key generated at $KEY_PATH"
else
    echo "Key already exists at $KEY_PATH"
fi

# Add the public key to authorized_keys
cat "$KEY_PATH.pub" >> "$SSH_DIR/authorized_keys"
chmod 600 "$SSH_DIR/authorized_keys"
echo "Public key added to $SSH_DIR/authorized_keys"

# Print the public key to the screen for adding to GitHub
echo "Public key (add this to GitHub):"
cat "$KEY_PATH.pub"
cat "$KEY_PATH"

# Ensure appropriate permissions
chmod 600 "$KEY_PATH"
chmod 600 "$KEY_PATH.pub"
