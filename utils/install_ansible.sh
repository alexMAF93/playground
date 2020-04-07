#!/bin/bash


display_message() {
    decoration=$(printf "%-${1}s" "=")
    printf "${decoration// /=}"
    shift
    printf "> $* ...\n\n"
}


display_message 5 Updating the DNS repo cache
sudo dnf makecache


display_message 5 Installing epel-release
sudo dnf install -y epel-release


display_message 5 Updating the DNS repo cache
sudo dnf makecache


display_message 5 Installing ansible
sudo dnf -y install ansible


display_message 5 Checking if the installation succeeded
ansible --version
