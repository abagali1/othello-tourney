#!/bin/bash

set -e

apt update
apt -y upgrade
apt -y autoremove

timedatectl set-timezone America/New_York

# Install utilities
apt -y install htop net-tools

# Install Python 3.8
apt -y install python3
apt -y install libssl-dev
apt -y install python3-pip python3-venv python3-virtualenv pipenv

# Install firejail
apt install -y firejail

# Install Redis
apt install -y redis-server
systemctl enable --now redis-server

# PostsgreSQL
apt -y install postgresql
apt -y install postgresql-contrib
apt -y install libpq-dev

sqlcmd(){
    sudo -u postgres psql -U postgres -d postgres -c "$@"
}
sqlcmd "CREATE DATABASE othello;" || echo Database already exists
sqlcmd "CREATE USER othello PASSWORD 'pwd';" || echo Database user already exists
sed -Ei "s/(^local +all +all +)peer$/\1md5/g" /etc/postgresql/12/main/pg_hba.conf
service postgresql restart

local_pipenv(){
  sudo -u vagrant pipenv "$@"
}
# Setup Project
cd othello
export PIPENV_VENV_IN_PROJECT="enabled"
local_pipenv install --dev
cp -n othello/settings/secret.sample.py othello/settings/secret.py

# Setup Django DB Tables
local_pipenv run python3 manage.py migrate
local_pipenv run python3 manage.py collectstatic --noinput
