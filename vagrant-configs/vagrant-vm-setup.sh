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
# 'whois' is needed for 'mkpasswd'
sudo apt-get -y install whois

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

echo "Installing Django! Please wait..."
sudo pip install django
echo "Installing Gunicorn! Please wait..."
sudo pip install gunicorn
echo "Installing South! Please wait..."
sudo pip install South

if [ ! -f /home/vagrant/.vagrant_do_not_delete ]; then
    # Copy Ubuntu Upstart config
    sudo cp /vagrant/vagrant-configs/djangodash-server.conf /etc/init/djangodash-server.conf
    # Start Gunicorn server
    sudo service happyly-server start
    
    # Copy nginx config
    sudo mv /etc/nginx/sites-available/default /etc/nginx/sites-available/default.original.backup
    sudo cp /vagrant/vagrant-configs/nginx-config /etc/nginx/sites-available/default
    # Start nginx (only for current login)
    sudo /etc/init.d/nginx start
    # Start nginx when system boots
    sudo update-rc.d nginx defaults
    
    git clone https://gist.github.com/18b7598e67b6d5b57e18.git vagrant_django_settings.py
    cp vagrant_django_settings.py/vagrant_settings.py /vagrant/carpet/carpet/
    
    # Change password of 'postgres' user (New password: 'vagrant')
    sudo usermod -p `mkpasswd vagrant` postgres
    #sudo -u postgres createuser -d -R -S -P django_login
    sudo -u postgres psql -c "CREATE ROLE django_login PASSWORD 'vagrant' NOSUPERUSER CREATEDB NOCREATEROLE INHERIT LOGIN;"
    sudo -u postgres psql -c "CREATE DATABASE django_db OWNER django_login ENCODING 'UTF8';"
    echo "local      django_db   django_login   md5" | sudo tee -a /etc/postgresql/9.1/main/pg_hba.conf
    sudo /etc/init.d/postgresql restart
fi
