#!/bin/bash

if [[ `nslookup slalexvr 2>&1 >/dev/null; echo $?` == "0" ]]
then
        printf "DNS is working properly ...\n"
        exit 0
else
        printf "DNS is not working, checking ...\n"
fi


if [ -s /etc/resolv.conf ]
then
        printf "/etc/resolv.conf exists\n"
else
        printf "/etc/resolv.conf does not exist\nCreating it now ...\n"
        printf "nameserver 192.168.100.1\n" > /etc/resolv.conf
        printf "Done!\n"
fi


if ` ! cat /etc/resolv.conf | grep -q "123"`
then
        printf "Problem with the resolv.conf file\n"
        cat /etc/resolv.conf
        printf "Overwritting it right now ...\n"
        printf "search salajan.ro\nnameserver 192.168.100.123\nnameserver 192.168.100.1\n" > /etc/resolv.conf
        printf "\nMaking sure it doesn't happen again ...\n"
        chattr +i /etc/resolv.conf
        for i in `lsattr /etc/resolv.conf | sed "s/-/ /g"`
        do
                if [[ "$i" == "i" ]]
                then
                        cnt=1
                        break
                fi
        done
else
        printf "The /etc/resolv.conf file contains the DNS server, moving on ...\n"
fi


if [ $cnt -eq 1 ]
then
        printf "The file /etc/resolv.conf is immutable now!\n"
else
        printf "The file /etc/resolv.conf is still not immutable, please try to do it manually\n"
fi


if `nc -z 192.168.100.123 53`
then
        printf "The port 53 is open on DNS server, moving on ...\n"
else
        printf "Port 53 is closed on DNS server, checking the firewall ... \n"
fi


LOADED=`ssh 192.168.100.123 "systemctl status firewalld" | tr -s ' ' | sed "s/\ //g" | sed "s/(/:/g" | grep "^Loaded:" | cut -d: -f2`
ACTIVE=`ssh 192.168.100.123 "systemctl status firewalld" | tr -s ' ' | sed "s/\ //g" | sed "s/(/:/g" | grep "^Active:" | cut -d: -f2`


if [[ `printf "$LOADED"` != "masked" || `printf "$ACTIVE"` != "inactive" ]]
then
        printf "The firewall is active on the DNS server\n"
        printf "Turning it off right now ...\n"
        ssh 192.168.100.123 "systemctl stop firewalld"
        printf "The firewall will be masked, so that this won't happen again soon ...\n"
        ssh 192.168.100.123 "systemctl mask firewalld"
        printf "\nLet's see if it worked\n"
        ssh 192.168.100.123 "systemctl status firewalld" | tr -s ' ' | sed "s/\ //g" | egrep "^Loaded:"\|"^Active:"
        printf "\n"
else
        printf "The firewall is disabled on the DNS server, moving on ...\n"
fi


printf "Checking if the problem was fixed ...\n"

if [[ `nslookup slalexvr 2>&1 >/dev/null; echo $?` == "0" ]]
then
        nslookup slalexvr
        printf "\nNow it's working\n"
else
        nslookup slalexvr
        printf "\nIt's still not working\nOut of ideas...\n"
fi
