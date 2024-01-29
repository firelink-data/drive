#!/bin/bash
#
# MIT License
#
# Copyright (c) 2024 Firelink Data
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
#
# Install Kafka (KRaft mode) version 3.6.1 on your system under a dedicated 'kafka' user.
# Will download the Kafka binaries from the apache archives, set up KRaft logging and
# metadata configuration, create advertised listener on port 19092 dedicated for 
# Docker containers, and set your (current) localhost ip on the Docker listener.
#
# File created: 2024-01-24
# Last updated: 2024-01-29
#

if [[ $EUID -ne 0 ]]; then
    printf " 🔒 THIS SCRIPT MUST BE RUN AS ROOT! Please use 'sudo $0' instead.\n" 1>&2
    exit 1
fi

KAFKA_CLUSTER_IP="$(/sbin/ip a | awk '/inet 192/ { print $2 }')"
KAFKA_CLUSTER_IP=(${KAFKA_CLUSTER_IP//// })

KAFKA_LIB_PATH="/var/lib/kafka"
KAFKA_COMBINED_LOG_PATH="$KAFKA_LIB_PATH/kraft-combined-logs"
KAFKA_METADATA_LOG_PATH="$KAFKA_LIB_PATH/metadata-logs"

function query_user()
{
    printf "$1\n"
    while true; do
        read -p " Proceed with doing this? [y\\n] " yn
        case $yn in
            [Yy]* ) printf "$2\n"; break;;
            [Nn]* ) printf " ❌ You chose 'no', exiting...\n"; exit;;
            * ) printf " 🚨 Please answer either yes or no.\n";;
        esac
    done
}

if id "kafka" >/dev/null 2>&1; then
    query_user " ❓ You already have a 'kafka' user on your system!\n    If you don't have anything important already on that user, we would recommend\n    to remove it and let this script set the user up again. Do you want to use\n    the existing 'kafka' user for installing a fresh Kafka 3.6.1 version?" \
        " ❗ Will use your existing user, this is not the standard procedure, might lead to unexpected behaviour..."
else
    query_user "\n ✅ Setting up a user 'kafka' with sudo privileges." " Please follow the on-screen prompts."
    sudo adduser kafka
    sudo usermod -aG sudo kafka
fi

query_user "\n ✅ Downloading Apache Kafka version 3.6.1 for Scala 2.13." " Sit back and relax."
su - kafka bash -c 'mkdir -p ~/Downloads; curl "https://downloads.apache.org/kafka/3.6.1/kafka_2.13-3.6.1.tgz" -o ~/Downloads/kafka.tgz; mkdir ~/kafka && cd ~/kafka; tar -xvzf ~/Downloads/kafka.tgz --strip 1'

query_user "\n ✅ Setting up Kafka directory and KRaft log paths." " Cool!"
env KAFKA_LIB_PATH=$KAFKA_LIB_PATH KAFKA_COMBINED_LOG_PATH=$KAFKA_COMBINED_LOG_PATH KAFKA_METADATA_LOG_PATH=$KAFKA_METADATA_LOG_PATH sudo -E su -c 'mkdir -p $KAFKA_LIB_PATH; mkdir -p $KAFKA_COMBINED_LOG_PATH; mkdir -p $KAFKA_METADATA_LOG_PATH; chown -R kafka:kafka $KAFKA_LIB_PATH'

query_user "\n ✅ Setting up your Kafka configuration for localhost and Docker compatibility." " Thanks! Soon done..."
env KAFKA_CLUSTER_IP=$KAFKA_CLUSTER_IP su kafka bash -c 'cd ~/kafka/config/kraft; echo "process.roles=broker,controller" > server.properties; echo "node.id=1" >> server.properties; echo "controller.quorum.voters=1@localhost:9093" >> server.properties; echo "listeners=PLAINTEXT://:9092,CONTROLLER://:9093,DOCKER_CLIENT://$KAFKA_CLUSTER_IP:19092" >> server.properties; echo "inter.broker.listener.name=PLAINTEXT" >> server.properties; echo "advertised.listeners=PLAINTEXT://localhost:9092,DOCKER_CLIENT://$KAFKA_CLUSTER_IP:19092" >> server.properties; echo "controller.listener.names=CONTROLLER" >> server.properties; echo "listener.security.protocol.map=CONTROLLER:PLAINTEXT,PLAINTEXT:PLAINTEXT,SSL:SSL,SASL_PLAINTEXT:SASL_PLAINTEXT,SASL_SSL:SASL_SSL,DOCKER_CLIENT:PLAINTEXT" >> server.properties; echo "num.network.threads=3" >> server.properties; echo "num.io.threads=8" >> server.properties; echo "socket.send.buffer.bytes=102400" >> server.properties; echo "socket.receive.buffer.bytes=102400" >> server.properties; echo "socket.request.max.bytes=104857600" >> server.properties; echo "log.dirs=/var/lib/kafka/kraft-combined-logs" >> server.properties; echo "num.partitions=1" >> server.properties; echo "num.recovery.threads.per.data.dir=1" >> server.properties; echo "offsets.topic.replication.factor=1" >> server.properties; echo "transaction.state.log.replication.factor=1" >> server.properties; echo "transaction.state.log.min.isr=1" >> server.properties; echo "log.retention.hours=-1" >> server.properties; echo "log.segment.bytes=1073741824" >> server.properties; echo "log.retention.check.interval.ms=300000" >> server.properties'

query_user "\n ✅ Generating a Kafka cluster UUID and formatting log storage with your config." " Last step!"
su kafka bash -c 'cd ~/kafka; export KAFKA_CLUSTER_ID="$(./bin/kafka-storage.sh random-uuid)"; ./bin/kafka-storage.sh format -t $KAFKA_CLUSTER_ID -c config/kraft/server.properties'

printf "\n\n 🚀✨ Success! Kafka 3.6.1 (KRaft mode) is now installed on your system.\n\n" 
printf " Kafka log path:\t\t\t$KAFKA_LIB_PATH\n"
printf " KRaft combined logs path:\t\t$KAFKA_COMBINED_LOG_PATH\n"
printf " KRaft metadata logs path:\t\t$KAFKA_METADATA_LOG_PATH\n"
printf " Advertised listeners:\t\t\tPLAINTEXT:9092,DOCKER_CLIENT:19092\n"
printf " Num network threads:\t\t\t3\n"
printf " Num IO threads:\t\t\t8\n"
printf " Num partitions:\t\t\t1\n"
printf " KAFKA_CLUSTER_IP (your localhost ip):\t$KAFKA_CLUSTER_IP\n"

