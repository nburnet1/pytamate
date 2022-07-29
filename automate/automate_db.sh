#!/bin/bash
cd /home/$(whoami)/pytamate/automate
dir_length=$(ls uncommitted |wc -l)

if [[ $dir_length == 0 ]]
then
	exit
fi
dir=$(ls -d $PWD/uncommitted/*)

python3 sql_insert.py $dir

cd uncommitted
mv * ../committed
