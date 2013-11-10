#! /bin/bash

# install.sh - helping people bootstrap their environments for whwn dev

# Text color variables
txtund=$(tput sgr 0 1)          # Underline
txtbld=$(tput bold)             # Bold
bldred=${txtbld}$(tput setaf 1) #  red
bldgrn=${txtbld}$(tput setaf 2) #  green
bldylw=${txtbld}$(tput setaf 3) #  yellow
bldblu=${txtbld}$(tput setaf 4) #  blue
bldwht=${txtbld}$(tput setaf 7) #  white
txtrst=$(tput sgr0)             # Reset
info=${bldwht}*${txtrst}        # Feedback
pass=${bldblu}*${txtrst}
warn=${bldred}*${txtrst}
ques=${bldblu}?${txtrst}

# setup by checking which platform we are running.
if [[ $OSTYPE =~ darwin.* ]] ; then
  PLATFORM="osx"
elif [[ $OSTYPE =~ linux-gnu ]] ; then
  if [[ `cat /proc/version` =~ .*Ubuntu.* ]] ; then
    PLATFORM="ubuntu"
  else
    PLATFORM="unknown"
  fi
fi

echo ""

echo "${bldwht}You're going to need Python 2.7 to run this baby... ${txtrst}"
PYTHON_VERSION=`python -c "import sys; sys.stdout.write(sys.version)" | head -n1 | grep -oe "\d\.\d\.\d"`
sleep 1
if [[ $PYTHON_VERSION =~ ^[[:digit:]].[[:digit:]].[[:digit:]]$ ]] ; then
  echo "    ${bldgrn}Version $PYTHON_VERSION found. Nice.${txtrst}"
else
  echo "    ${bldred}No python found :( you need to install Python version 2.7.*${txtrst}"
  exit 1
fi

echo ""

echo "${bldwht}We use PostgreSQL as our main data store. Let's see if you have it... ${txtrst}"
POSTGRESQL_VERSION=`psql --version | cut -d" " -f3`
sleep 1
if [[ $POSTGRESQL_VERSION =~  ^[[:digit:]].[[:digit:]].[[:digit:]]$ ]] ; then
  echo "    ${bldgrn}Version $POSTGRESQL_VERSION found. Hot stuff.${txtrst}"
else
  echo "    ${bldred}You will need to have PostgreSQL installed and running to continue.${txtrst}"
  exit 1
fi

echo ""

echo "${bldwht}You're going to need pip to install virtualenv to keep your Python workspace clean...${txtrst}"
PIP_VERSION=`pip -V | cut -d" " -f2`
sleep 1
if [[ $PIP_VERSION =~ ^[[:digit:]].[[:digit:]].[[:digit:]]$ ]] ; then
  echo "    ${bldgrn}Version $PIP_VERSION found. Sweet.${txtrst}"
else
  echo "    ${bldred}You will need to install pip to continue.${txtrst}"
  exit 1
fi

echo ""

echo "${bldwht}Now that you have pip, you're going to need virtualenv and virtualenvwrapper!${txtrst}"
sleep 1
if [[ `pip list | grep -oe "^virtualenv\s"`  -eq "virtualenv" ]] ; then
  echo "    ${bldgrn}Perfect, you've installed virtualenv.${txtrst}"
  if [[ `pip list | grep -oe '^virtualenvwrapper\s'` -eq "virtualenvwrapper" ]] ; then
    echo "    ${bldgrn}You've got virtualenvwrapper too. Awesome.${txtrst}"
  fi
else
  echo "    ${bldred}Looks like you have some work to do. ${txtrst} "
  echo "    Please install virtualenv and virtualenvwrapper using:"
  echo "        pip install virtualenv virtualenvwrapper"
  exit 1
fi

echo ""

echo "${bldwht}Checking to see if virtualenvwrapper is set up properly.${txtrst}"
sleep 1
if [[ ! -n $(echo $WORKON_HOME) ]] ; then
  echo "    Setting it up for you for you. Running: "
  echo '        echo "export WORKON_HOME=\$HOME/.virtualenvs" >> ~/.profile'
  # Doing the line add
  echo "export WORKON_HOME=\$HOME/.virtualenvs" >> ~/.profile
  if [[ ! -n $(which virtualenvwrapper.sh) ]] ; then
    echo '        echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.profile'
    # Doing the line add
    echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.profile
  fi
  if [[ ! -n $(echo $PIP_VIRTUALENV_BASE) ]] ; then
    echo '        echo "export PIP_VIRTUALENV_BASE=\$WORKON_HOME" >> ~/.profile'
    # Doing the line add
    echo "export PIP_VIRTUALENV_BASE=\$WORKON_HOME" >> ~/.profile
  fi
  if [[ ! -n $(echo $PIP_RESPECT_VIRTUALENV) ]] ; then
    echo '        echo "export PIP_RESPECT_VIRTUALENV=true" >> ~/.profile'
    # Doing the line add
    echo "export PIP_RESPECT_VIRTUALENV=true" >> ~/.profile
  fi
fi
source ~/.profile
echo "    ${bldgrn}Virtualenvwrapper is now setup properly. Yes!${txtrst}"

echo ""

echo "${bldwht}We use NodeJS and npm to bootstrap our javascript packages.${txtrst}"
sleep 1
if [[ -n $(which npm) ]] ; then
  echo "    ${bldgrn}Npm installation found, moving on!.${txtrst}"
else
  echo "${bldred}Install version 0.10.* of Node to get npm${txtrst}"
  exit 1
fi

echo ""

sleep 1
if [[ ! `echo $VIRTUAL_ENV` =~ whwn ]] ; then
  # Instruct to create a virtualenv
  echo "${bldrd}You're going to need a virtualenv so that you don't crowd your default 
  system packages.${txtrst}"

  echo "${bldwht}Please run the following to create a whwn environment and: ${txtrst}"
  echo "    ${bldylw}mkvirtualenv --no-site-packages --distribute whwn"
  echo "    workon whwn${txtrst}"
  exit 1
else
  echo "${bldwht}Cool, we'll do the rest from here in this order: ${txtrst}"
  echo "    ${bldblu}1. Use pip to install our Django project requirements"
  echo "    2. Setup our PostgreSQL database to properly work"
  echo "    3. Sync and Migrate our Django project with our PostgreSQL Database"
  echo "    4. Install the requisite javascript packages using npm and bower.${txtrst}"
fi

sleep 3

echo "${bldylw}Running:${bldwht} pip install -q -r requirements.txt --use-mirrors${txtrst}"
pip install -q -r requirements.txt --use-mirrors
echo "${bldylw}Running:${bldwht} npm run-script setup${txtrst}"
npm run-script setup
echo "${bldylw}Running:${bldwht} psql -c \"CREATE USER whwn WITH PASSWORD 'whwn'\" -U postgres
               psql -c \"CREATE DATABASE wehaveweneed WITH OWNER whwn\" -U postgres
               psql -c \"ALTER USER whwn CREATEDB\" -U postgres${txtrst}"
psql -c "CREATE USER whwn WITH PASSWORD 'whwn'" -U postgres
psql -c "CREATE DATABASE wehaveweneed WITH OWNER whwn" -U postgres
psql -c "ALTER USER whwn CREATEDB" -U postgres
echo "${bldylw}Running:${bldwht} python manage.py syncdb --noinput${txtrst}"
python manage.py syncdb --noinput
echo "${bldylw}Running:${bldwht} python manage.py migrate --noinput${txtrst}"
python manage.py migrate --noinput

echo "${bldgrn}Congratulations! Everything is setup! Please peruse the output of this script to know exactly
what was run.${txtrst}"
exit 0
  

# mkvirtualenv --no-site-packages --distribute whwn_env
# 
# workon whwn_env
# 
# #INstall the requirements
# pip install -q -r requirements.txt --use-mirrors
# 
# #create database with postgres
# #make sure your config for postgres user is NOT peer but instead trust
# #go to /etc/postgresql/VERSION/main/pg_hba.conf and replace it
# #then reload psql, /etc/init.d/postgresql reload

#sync and migrate
#python manage.py syncdb --noinput
#python manage.py migrate --noinput

#run the tests
#python manage.py test whwn
