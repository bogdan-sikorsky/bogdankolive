#!/bin/bash


# Prevents interactions
export DEBIAN_FRONTEND=noninteractive


# Update and upgrade the system
sudo apt update
sudo apt -y upgrade


# Install git
sudo apt install -y git
git --version


# Install docker
sudo apt-get remove docker docker-engine docker.io containerd runc
sudo apt-get install -y \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io


# Install docker-compose
#sudo apt install -y python3-pip
#sudo pip install -y docker-compose
sudo curl -L "https://github.com/docker/compose/releases/download/$(curl -s https://api.github.com/repos/docker/compose/releases/latest | grep tag_name | cut -d '"' -f 4)/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
docker-compose --version


# Add user to docker group
sudo gpasswd -a $USER docker
newgrp docker


# Install make for makefile
sudo apt install make
