#!/bin/bash


DATE=`date +%m_%d_%Y`
ARC_DIR=/var/tmp/ARCHIVED_LOGS/

if [[ ! -d $ARC_DIR ]]
then
    mkdir $ARC_DIR
fi


cd /var/tmp
tar -cvzf old_logs_${DATE}.tar.gz *.log
mv old_logs_${DATE}.tar.gz $ARC_DIR
rm *.log
