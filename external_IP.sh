#!/bin/bash


DIR=/var/www/html/owncloud/config


OLD_IP=`cat $DIR/config.php | grep '1 =>' | awk '{print $3}' | sed s/\'//g | sed s/,//`
NEW_IP=`curl -s http://whatismyip.akamai.com`


if [[ ! "$OLD_IP" == "$NEW_IP" ]]
then
	cat $DIR/config_file | sed "s/IP_TO_BE_REPLACED/${NEW_IP}/" > $DIR/config.php
	chown apache:apache $DIR/config.php
	ssmtp mitroi.alex93@gmail.com <<-EOF
	To: Alex Mitroi
	From: Alex Mitroi
	Subject: External IP for $HOSTNAME

	The new external IP: $NEW_IP
	
	OwnCloud: https://${NEW_IP}:19443/owncloud
	Webmin  : https://${NEW_IP}:19999/
	

	EOF

fi
