#!/bin/bash

KAFKA_CLUSTER_IP="$(/sbin/ip a | awk '/inet 192/ { print $2 }')"
KAFKA_CLUSTER_IP=(${KAFKA_CLUSTER_IP//// })

KAFKA_LIB_PATH="/var/lib/kafka"
KAFKA_COMBINED_LOG_PATH="$KAFKA_LIB_PATH/kraft-combined-logs"
KAFKA_METADATA_LOG_PATH="$KAFKA_LIB_PATH/metadata-logs"

function query_user()
{
    printf "$1\n"
    while true; do
        read -p "Proceed with doing this? [y\\n] " yn
        case $yn in
            [Yy]* ) printf "$2\n"; break;;
            [Nn]* ) printf " ❌ You chose 'no', exiting..."; exit;;
            * ) printf " 🚨 Please answer either yes or no.\n";;
        esac
    done
}

if id "kafka" >/dev/null 2>&1; then
    query_user " ❓ You already have a 'kafka' user on your system!\n    If you don't have anything important already on that user, we would recommend\n    to remove it and let this script set the user up again. Do you want to use\n    the existing 'kafka' user for installing a fresh Kafka version 3.6.1?" \
        " ❗ Will use your existing user, this is not the standard procedure, might lead to unexpected behaviour..."
else
    query_user " ✅ Setting up a user 'kafka' with sudo privileges." " ✅ Please follow the on-screen prompts."
    sudo adduser kafka
    sudo usermod -aG sudo kafka
fi

query_user " ✅ Downloading Apache Kafka version 3.6.1 for Scala 2.13." " ✅ Sit back and relax."
su - kafka bash -c 'mkdir ~/Downloads; curl "https://downloads.apache.org/kafka/3.6.1/kafka_2.13-3.6.1.tgz" -o ~/Downloads/kafka.tgz; mkdir ~/kafka && cd ~/kafka; tar -xvzf ~/Downloads/kafka.tgz --strip 1'

query_user " ✅ Setting up Kafka directory and KRaft log paths." " ✅ Cool!"
sudo su -c 'mkdir -p $KAFKA_LIB_PATH; mkdir -p $KAFKA_COMBINED_LOG_PATH; mkdir -p /var/lib/kafka/metadata-logs; chown -R kafka:kafka /var/lib/kafka'

query_user " ✅ Setting up your Kafka configuration for localhost and Docker compatibility." " ✅ Thanks! Soon done..."
env KAFKA_CLUSTER_IP=$KAFKA_CLUSTER_IP su kafka bash -c 'cd ~/kafka/config/kraft; echo "process.roles=broker,controller" > server.properties; echo "node.id=1" >> server.properties; echo "controller.quorum.voters=1@localhost:9093" >> server.properties; echo "listeners=PLAINTEXT://:9092,CONTROLLER://:9093,DOCKER_CLIENT://$KAFKA_CLUSTER_IP:19092" >> server.properties; echo "inter.broker.listener.name=PLAINTEXT" >> server.properties; echo "advertised.listeners=PLAINTEXT://localhost:9092,DOCKER_CLIENT://$KAFKA_CLUSTER_IP:19092" >> server.properties; echo "controller.listener.names=CONTROLLER" >> server.properties; echo "listener.security.protocol.map=CONTROLLER:PLAINTEXT,PLAINTEXT:PLAINTEXT,SSL:SSL,SASL_PLAINTEXT:SASL_PLAINTEXT,SASL_SSL:SASL_SSL,DOCKER_CLIENT:PLAINTEXT" >> server.properties; echo "num.network.threads=3" >> server.properties; echo "num.io.threads=8" >> server.properties; echo "socket.send.buffer.bytes=102400" >> server.properties; echo "socket.receive.buffer.bytes=102400" >> server.properties; echo "socket.request.max.bytes=104857600" >> server.properties; echo "log.dirs=/var/lib/kafka/kraft-combined-logs" >> server.properties; echo "num.partitions=1" >> server.properties; echo "num.recovery.threads.per.data.dir=1" >> server.properties; echo "offsets.topic.replication.factor=1" >> server.properties; echo "transaction.state.log.replication.factor=1" >> server.properties; echo "transaction.state.log.min.isr=1" >> server.properties; echo "log.retention.hours=-1" >> server.properties; echo "log.segment.bytes=1073741824" >> server.properties; echo "log.retention.check.interval.ms=300000" >> server.properties'

query_user " ✅ Generating a Kafka cluster UUID and formatting log storage with your config." " ✅ Last step!"
su kafka bash -c 'cd ~/kafka; export KAFKA_CLUSTER_ID="$(./bin/kafka-storage.sh random-uuid)"; ./bin/kafka-storage.sh format -t $KAFKA_CLUSTER_ID -c config/kraft/server.properties'

printf "\n\n 🚀 Great! Kafka 3.6.1 is now installed on your system for the 'kafka' user.\n\n" 
printf " Log path:  $KAFKA_LOG_PATH\n"
printf " KRaft combined logs path:  $KAFKA_COMBINED_LOG_PATH\n"
printf " KRaft metadata logs path:  $KAFKA_METADATA_LOG_PATH\n"
printf " KAFKA_CLUSTER_IP (your host ip): $KAFKA_CLUSTER_IP\n"

