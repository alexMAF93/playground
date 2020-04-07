#!/bin/bash


display_message() {
    decoration=$(printf "%-${1}s" "=")
    printf "${decoration// /=}"
    shift
    printf "> $* ...\n\n"
}



# install celery using pip
display_message 5 Installing celery through pip
if [[ $(command -v pip) ]]
then
    pip install Celery
else
    pip3 install Celery
fi


# Installing RabbitMQ
display_message 5 Installing RabbitMQ

display_message 3 Adding the epel repo
dnf -y install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm


display_message 3 Installing Erlang
dnf -y install wget
wget https://github.com/rabbitmq/erlang-rpm/releases/download/v21.3.8.6/erlang-21.3.8.6-1.el7.x86_64.rpm
dnf install -y erlang-21.3.8.6-1.el7.x86_64.rpm


display_message 3 Checking if erlang was installed
erl # check the Erlang installation


display_message 3 Adding the RabbitMQ repo
cat <<EOF >> /etc/yum.repos.d/rabbitmq-server.repo
[rabbitmq-server]
name=rabbitmq-server
baseurl=https://packagecloud.io/rabbitmq/rabbitmq-server/el/7/$basearch
repo_gpgcheck=1
gpgcheck=0
enabled=1
gpgkey=https://packagecloud.io/rabbitmq/rabbitmq-server/gpgkey
sslverify=1
sslcacert=/etc/pki/tls/certs/ca-bundle.crt
metadata_expire=300
EOF


display_message 3 Installing RabbitMQ with Yum
dnf makecache -y --disablerepo='*' --enablerepo='rabbitmq-server'
dnf install -y rabbitmq-server


display_message 5 Configuring the firewall
firewall-cmd --zone=public --permanent --add-port={4369,25672,5671,5672,15672,61613,61614,1883,8883}/tcp
firewall-cmd --reload


display_message 5 Start and enable RabbitMQ
systemctl start rabbitmq-server.service
systemctl enable rabbitmq-server.service
