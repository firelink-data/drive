#!/bin/bash

sudo apt-get update
sudo apt-get install docker.io docker-compose containerd

sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker
