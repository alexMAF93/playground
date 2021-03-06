#!/bin/bash


usage() {
cat<<EOF
    $0 [OPTION] [USERNAME]

    OPTION:
        -h, shows this message
    
    USERNAME:
        - you can specify an user that will be added in the docker group


EOF
}


display_message() {
    decoration=$(printf "%-${1}s" "=")
    printf "${decoration// /=}"
    shift
    printf "> $* ...\n\n"
}


if [[ $(command -v docker) ]]
then
    display_message 5 Docker is already installed
    exit 0
fi


if [[ "$1" == "-h" ]]
then
    usage
    exit 0
elif [[ "$1" ]]
then
    USERNAME_TO_ADD=$1
fi


display_message 5 Checking the OS version
OS_VERS=$(cat /etc/redhat-release)
if [[ ! "$OS_VERS" =~ "CentOS Linux release 8" ]]
then
    printf "This script works only for CentOS 8\n\n"
    exit 27
else
    printf "${OS_VERS}\n"
fi


display_message 5 Adding the docker CE repo
dnf config-manager --add-repo=https://download.docker.com/linux/centos/docker-ce.repo


display_message 5 Installing the latest version of docker
dnf install docker-ce --nobest -y


display_message 5 Starting and enabling docker
systemctl start docker
systemctl enable docker


if [[ "$USERNAME_TO_ADD" ]]
then
    display_message 5 Adding the current user
    usermod -a -G docker $USERNAME_TO_ADD
fi


display_message 5 Done. Checking docker version
docker --version


display_message 5 You can try to run docker run hello-world
