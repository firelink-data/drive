#!/bin/bash

sudo adduser kafka
sudo usermod -aG sudo kafka

su - kafka bash -c 'mkdir ~/Downloads; curl "https://downloads.apache.org/kafka/3.6.1/kafka_2.13-3.6.1.tgz" -o ~/Downloads/kafka.tgz; mkdir ~/kafka && cd ~/kafka; tar -xvzf ~/Downloads/kafka.tgz --strip 1'

su - kafka bash -c 'sudo mkdir -p /var/lib/kafka; sudo mkdir -p /var/lib/kafka/kraft-combined-logs; sudo mkdir -p /var/lib/kafka/metadata-logs; sudo chown -R kafka:kafka /var/lib/kafka'

sudo mkdir -p /var/lib/kafka
sudo mkdir -p /var/lib/kafka/kraft-combined-logs
sudo mkdir -p /var/lib/kafka/metadata-logs
sudo chown -R kafka:kafka /var/lib/kafka

cd ~/kafka

export KAFKA_CLUSTER_ID="$(./bin/kafka-storage.sh random-uuid)"
./bin/kafka-storage.sh format -t $KAFKA_CLUSTER_ID -c config/kraft/server.properties

