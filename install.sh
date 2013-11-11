#! /usr/bin/env bash

# Text color variables.
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

function echobr {
  echo "${bldred}$1${txtrst}"
}
function echobg { 
  echo "${bldgrn}$1${txtrst}"
}
function echobb {
  echo "${bldblu}$1${txtrst}"
}
function echoby {
  echo "${bldylw}$1${txtrst}"
}
function echobw {
  echo "${bldwht}$1${txtrst}"
}

########################
# DETECT WHAT PLATFORM #
########################
if [[ $OSTYPE =~ darwin ]] ; then
  PLATFORM="osx"
elif [[ $OSTYPE =~ linux-gnu ]] ; then
  if [[ `cat /proc/version` =~ .*Ubuntu.* ]] ; then
    PLATFORM="ubuntu"
  else
    PLATFORM="unknown"
  fi
fi


# We want to make sure this script runs in the same environment
# that the user has so we wanna source the files
if [ -f $HOME/.bashrc ] ; then . $HOME/.bashrc; fi
if [ -f $HOME/.zshrc ] ; then . $HOME/.zshrc; fi
if [ -f $HOME/.profile ] ; then . $HOME/.profile; fi

echo ""

# Step 1: Check for the correct Python version.
# TODO: Platform specific installation instructions.

echobw "You're going to need Python 2.7 to run this baby... "
PYTHON_VERSION=`python -c "import sys; sys.stdout.write(sys.version)" | head -n1 | grep -oe "\d\.\d\.\d"`

if [[ $PYTHON_VERSION =~ ^[[:digit:]].[[:digit:]].[[:digit:]]$ ]] ; then
  if [[ $PYTHON_VERSION =~ ^2.7.[[:digit:]]$ ]] ; then
    echobg "    Version $PYTHON_VERSION found. Nice."
  elif [[ $PYTHON_VERSION =~ ^2.[[:digit:]].[[:digit:]]$ ]] ; then
    echobr "    You need to upgrade to version 2.7 of Python."
  fi
else
  echobr "    No python found :( you need to install Python version 2.7.*"
  exit 1
fi

echo ""

# Step 2: Check for a correct PostgreSQL installation.
# TODO: Platform specific installation instructions.

echobw "We use PostgreSQL as our main data store. Let's see if you have it... "
POSTGRESQL_VERSION=`psql --version | cut -d" " -f3`
if [[ $POSTGRESQL_VERSION =~ ^[[:digit:]].[[:digit:]].[[:digit:]]$ ]] ; then
  echobg "    Version $POSTGRESQL_VERSION found. Hot stuff."
else
  echobr "    You will need to have PostgreSQL installed and running to continue."
  exit 1
fi

echo ""

# Step 3: Check for a global installation of pip.
# TODO: Platform specific installation instructions.
echobw "You're going to need pip to install virtualenv to keep your Python workspace clean..."
PIP_VERSION=`pip -V | cut -d" " -f2`
if [[ $PIP_VERSION =~ ^[[:digit:]].[[:digit:]].[[:digit:]]$ ]] ; then
  echobg "    Version $PIP_VERSION found. Sweet."
else
  echobr "    You will need to install pip to continue."
  exit 1
fi

echo ""

# Step 4: Check for an insatllation of virtualenv and virtualenvwrapper
echobw "Now that you have pip, you're going to need virtualenv and virtualenvwrapper!"
if [[ -n $(pip list | grep -oe "^virtualenv\s") ]] ; then
  echobg "    Perfect, you have virtualenv."
else
  echobr "    Looks like you have some work to do. "
  echoby "    Please install virtualenv and virtualenvwrapper using:"
  echoby "        sudo pip install virtualenv virtualenvwrapper"
  exit 1
fi

echo ""

# Step 5: Set up the guys virtualenv/virtualenvwrapper .dotfiles if they
# don't exist already.
touch ~/.profile
echobw "Checking to see if virtualenvwrapper is set up properly."
if [[ -z $(echo $WORKON_HOME) ]] ; then
  echo "    Setting it up for you for you. Running: "
  echo "        echo \"export WORKON_HOME=\$HOME/.virtualenvs\" >> ~/.profile"
  # Doing the line add
  echo "export WORKON_HOME=\$HOME/.virtualenvs" >> ~/.profile
fi
if [[ $(cat ~/.profile | grep -c "virtualenvwrapper.sh") -eq 0 ]] ; then
  echo "        echo \"source /usr/local/bin/virtualenvwrapper.sh\" >> ~/.profile"
  # Doing the line add
  echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.profile
fi
if [[ -z $(echo $PIP_VIRTUALENV_BASE) ]] ; then
  echo '        echo "export PIP_VIRTUALENV_BASE=\$WORKON_HOME" >> ~/.profile'
  # Doing the line add
  echo "export PIP_VIRTUALENV_BASE=\$WORKON_HOME" >> ~/.profile
fi
if [[ -z $(echo $PIP_RESPECT_VIRTUALENV) ]] ; then
  echo '        echo "export PIP_RESPECT_VIRTUALENV=true" >> ~/.profile'
  # Doing the line add
  echo "export PIP_RESPECT_VIRTUALENV=true" >> ~/.profile
fi
if [[ -z $(echo $VIRTUALENVWRAPPER_PYTHON) ]] ; then
  echo "        echo \"export VIRTUALENVWRAPPER_PYTHON=`which python`\" >> ~/.profile"
  # Doing the line add
  echo "export VIRTUALENVWRAPPER_PYTHON=`which python`" >> ~/.profile
fi
echobg "    Virtualenvwrapper is now setup properly. Yes!"
. ~/.profile

echo ""

# Step 6: Check for an installation of NodeJS and NPM
echobw "We use NodeJS and npm to bootstrap our javascript packages."
if [ -n $(which npm) ] ; then
  echobg "    Npm installation found, moving on!"
else
  echobr "    Install version 0.10.* of Node to get npm."
  echoby "    The suggested method is via Node Version Manager(NVM) which you can find here: "
  echoby "    https://github.com/creationix/nvm "
  echoby "    Installation instructions are in the README."
  exit 1
fi

echo ""

# Step 7: If virtualenv is properly installed, we automatically do everything else
# for them.
if [[ `echo $VIRTUAL_ENV` =~ whwn ]] ; then
  echobw "Cool, we'll do the rest from here in this order:"
  echobb "    1. Use pip to install our Django project requirements"
  echobb "    2. Setup our PostgreSQL database to properly work"
  echobb "    3. Sync and Migrate our Django project with our PostgreSQL Database"
  echobb "    4. Install the requisite javascript packages using npm and bower."
else
  # Instruct to create a virtualenv
  echobr "You're going to need a virtualenv so that you don't crowd your default 
  system packages."

  echobw "Please run the following to create a whwn environment and: "
  echoby "    source ~/.profile    # Reload your ~./profile settings we just added."
  echoby "    mkvirtualenv --no-site-packages --distribute whwn"
  echoby "    workon whwn"
  echo ""
  echobw "Then rerun ${bldblu}install.sh${bldwht} to continue."
  exit 1
fi

sleep 3
echo ""

# Step 8: We're going to install our python packages using pip.
echoby "Running:${bldwht} pip install -r requirements.txt"
workon whwn # load our virtualenv so pip installs into it.
pip install -r requirements.txt
echo ""

# Step 9: We're going to use our npm setup script to install our npm/bower packages.
echoby "Running:${bldwht} npm run-script setup"
npm run-script setup
echo ""

# We're going to setup postgres for them.

echoby "Running:${bldwht} psql -c \"CREATE USER whwn WITH PASSWORD 'whwn'\" -U postgres"
echobw "         psql -c \"CREATE DATABASE wehaveweneed WITH OWNER whwn\" -U postgres"
echobw "         psql -c \"ALTER USER whwn CREATEDB\" -U postgres"

echo ""
if [[ $PLATFORM == "osx" ]] ; then
   echoby "Seems like your platform is osx, which doesn't have a 'postgres' user on most"
   echoby "default installations. Going to try to create the 'postgres' user for you."
   echoby "Running: ${bldwht}createdb"
   echobw "         psql -c \"CREATE USER postgres SUPERUSER CREATEROLE CREATEDB\""

   createdb
   psql -c "CREATE USER postgres SUPERUSER CREATEROLE CREATEDB"
fi

psql -c "CREATE USER whwn WITH PASSWORD 'whwn'" -U postgres
psql -c "CREATE DATABASE wehaveweneed WITH OWNER whwn" -U postgres
psql -c "ALTER USER whwn CREATEDB" -U postgres

echo ""
echoby "Running:${bldwht} python manage.py syncdb --noinput"
python manage.py syncdb --noinput

echo ""
echoby "Running:${bldwht} python manage.py migrate --noinput"
python manage.py migrate --noinput

echo ""
echobg "Congratulations! Everything is setup! Please peruse the output of this script to 
understand exactly what was run."
exit 0

# DONE! YIPEE!
