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

if [ ! -f /home/vagrant/.vagrant_do_not_delete ]; then
    # Locale stuff (for PostgreSQL)
    # Source: http://www.softr.li/blog/2012/05/22/chef-recipe-to-install-a-postgresql-server-on-a-machine-configured-with-en_us-locales
    export LANGUAGE="en_US.UTF-8"
    export LANG="en_US.UTF-8"
    export LC_ALL="en_US.UTF-8"
    locale-gen en_US.UTF-8
    sudo dpkg-reconfigure locales
fi

sudo apt-get -y install postgresql-9.1 
sudo apt-get -y install postgresql
sudo apt-get -y install postgresql-client
sudo apt-get -y install python-psycopg2
