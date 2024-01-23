#!/bin/bash

sudo adduser kafka
sudo usermod -aG sudo kafka

su - kafka bash -c 'mkdir ~/Downloads; curl "https://downloads.apache.org/kafka/3.6.1/kafka_2.13-3.6.1.tgz" -o ~/Downloads/kafka.tgz; mkdir ~/kafka && cd ~/kafka; tar -xvzf ~/Downloads/kafka.tgz --strip 1'

