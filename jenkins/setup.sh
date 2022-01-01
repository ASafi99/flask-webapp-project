#!/bin/bash

echo "Setup stage"

install apt dependencies
sudo apt update 
sudo apt install python3 python3-venv python3-pip -y

#create and activate venv
python3 -m venv venv
source venv/bin/activate

# install pip requirements
pip3 install -r requirements.txt

# apt dependencies
sudo apt-get update
sudo apt install -y curl jq

# install docker
curl https://get.docker.com | sudo bash
sudo usermod -aG docker jenkins
newgrp docker

# install docker compose
version=$(curl -s https://api.github.com/repos/docker/compose/releases/latest | jq -r '.tag_name')
sudo curl -L "https://github.com/docker/compose/releases/download/${version}/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# docker login
docker login --username $DOCKER_HUB_CREDS_USR --password $DOCKER_HUB_CREDS_PSW