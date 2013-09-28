#!/usr/bin/env bash

echo "==========================================================="
echo "[vagrant-vm-setup.sh] Setting up vagrant VM, please wait..."
echo "==========================================================="

sudo apt-get -y update
sudo apt-get -y install nginx
sudo apt-get -y install python-dev
sudo apt-get -y install python
sudo apt-get -y install python-pip
sudo apt-get -y install git
sudo apt-get -y install tmux


