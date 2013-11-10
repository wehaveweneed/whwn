#! /bin/bash

# Preinstallation requirements:
# Python 2.7+ but not Python 3
# Pip (sudo apt-get install python-pip) 
# virtualenv (sudo pip install virtualenv)
# virtaulenvwrapper (sudo pip instasll virtualenvwrapper)
# postgresql (sudo apt-get install postgresql postgresql-contrib postgresql-client)
# libpq-dev and python-dev to get pycorpg2 working iwth virtualenv (sudo apt-get install libpq-dev python-dev)
# Usage: remember to do . ./instasll-ubuntu.sh to source in the current shell

# create a .virtualEnvConfig file to source later on.
touch ~/.virtualEnvConfig
echo "export WORKON_HOME=\$HOME/.virtualenvs" >> ~/.virtualEnvConfig
# Edit this line to be wherever pip install virtualenwrapper be
echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.virtualEnvConfig
echo "export PIP_VIRTUALENV_BASE=\$WORKON_HOME" >> ~/.virtualEnvConfig
echo "export PIP_RESPECT_VIRTUALENV=true" >> ~/.virtualEnvConfig
echo "source ~/.virtualEnvConfig" >> ~/.bashrc

source ~/.bashrc

mkvirtualenv --no-site-packages --distribute whwn_env

workon whwn_env

#INstall the requirements
pip install -q -r requirements.txt --use-mirrors

#create database with postgres
#make sure your config for postgres user is NOT peer but instead trust
#go to /etc/postgresql/VERSION/main/pg_hba.conf and replace it
#then reload psql, /etc/init.d/postgresql reload
psql -c "CREATE USER whwn WITH PASSWORD 'whwn'" -U postgres
psql -c "CREATE DATABASE wehaveweneed WITH OWNER whwn" -U postgres
psql -c "ALTER USER whwn CREATEDB" -U postgres

#sync and migrate
#python manage.py syncdb --noinput
#python manage.py migrate --noinput

#run the tests
#python manage.py test whwn
