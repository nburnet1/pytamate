#!/bin/bash

read -n 1 -sp "Have you configured all yaml files and read the README? [y/N]" yon
clear
if [ $yon != "y" ]; then
    echo "Please edit yaml files before continuing with the installation."
	echo "Exiting..."
	exit
fi

pip install pyinstaller
pip install mysql-connector-python
pip install pyyaml

echo "Reading automate_config.yml..."

arr=($(cat automate/automate_config.yml | grep "freq:"))
freq=${arr[1]}

echo "Setting up cron job..."
cronjob="*/$freq * * * * $PWD/automate/automate_db.sh"

(crontab -u $USER -l; echo "$cronjob") | crontab -u $USER -
echo "Cron job has been setup under" $USER


