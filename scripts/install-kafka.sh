#!/bin/bash

KAFKA_CLUSTER_IP="$(/sbin/ip a | awk '/inet 192/ { print $2 }')"

sudo adduser kafka
sudo usermod -aG sudo kafka

printf " ✅ Downloading Apache Kafka\n"
su - kafka bash -c 'mkdir ~/Downloads; curl "https://downloads.apache.org/kafka/3.6.1/kafka_2.13-3.6.1.tgz" -o ~/Downloads/kafka.tgz; mkdir ~/kafka && cd ~/kafka; tar -xvzf ~/Downloads/kafka.tgz --strip 1'

printf " ✅ Setting up Kafka directory and log paths\n"
su - kafka bash -c 'sudo mkdir -p /var/lib/kafka; sudo mkdir -p /var/lib/kafka/kraft-combined-logs; sudo mkdir -p /var/lib/kafka/metadata-logs; sudo chown -R kafka:kafka /var/lib/kafka'

printf " ✅ Setting up your Kafka configuration\n"
su - kafka bash -c 'cd ~/kafka/config/kraft; echo "process.roles=broker,controll" > server.properties; echo "node.id=1" >> server.properties; echo "controller.quorum.voters=1@localhost:9093" >> server.properties; echo "listeners=PLAINTEXT://:9092,CONTROLLER://:9093,DOCKER_CLIENT://:19092" >> server.properties; echo "inter.broker.listener.name=PLAINTEXT" >> server.properties; echo "advertised.listeners=PLAINTEXT://localhost:9092,DOCKER_CLIENT://$KAFKA_CLUSTER_IP:19092" >> server.properties; echo "controller.listener.names=CONTROLLER" >> server.properties; echo "listener.security.protocol.map=CONTROLLER:PLAINTEXT,PLAINTEXT:PLAINTEXT,SSL:SSL,SASL_PLAINTEXT:SASL_PLAINTEXT,SASL_SASL:SASL_SASL,DOCKER_CLIENT:PLAINTEXT" >> server.properties; echo "num.network.threads=3" >> server.properties; echo "num.io.threads=8" >> server.properties; echo "socket.send.buffer.bytes=102400" >> server.properties; echo "socket.receive.buffer.bytes=102400" >> server.properties; echo "socket.request.max.bytes=104857600" >> server.properties; echo "log.dirs=/var/lib/kafka/kraft-combined-logs" >> server.properties; echo "num.partitions=1" >> server.properties; echo "num.recovery.threads.per.data.dir=1" >> server.properties; echo "offsets.topic.replication.factor=1" >> server.properties; echo "transaction.state.log.replication.factor=1" >> server.properties; echo "transaction.state.log.min.isr=1" >> server.properties; echo "log.retention.hours=-1" >> server.properties; echo "log.segment.bytes=1073741824" >> server.properties; echo "log.retention.check.interval.ms=300000" >> server.properties'

printf " ✅ Generating a Kafka cluster ID and formatting storage with your config\n"
su - kafka bash -c 'cd ~/kafka; export KAFKA_CLUSTER_ID="$(./bin/kafka-storage.sh random-uuid)"; ./bin/kafka-storage.sh format -t $KAFKA_CLUSTER_ID -c config/kraft/server.properties'
