"""
Template file for an autonomous LLM agent.

File created: 2024-01-24
Last updated: 2024-01-27
"""

import logging
import os
import langchain  # noqa
from confluent_kafka import Consumer, Message, Producer
from confluent_kafka.admin import AdminClient
from typing import List

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


class Agent(object):
    """ """

    def __init__(self, topics: List[str]):
        """ """

        kafka_server_ip = os.environ["KAFKA_SERVER_IP"]
        kafka_server_port = os.environ["KAFKA_SERVER_PORT"]
        bootstrap_server = f"{kafka_server_ip}:{kafka_server_port}"

        client = AdminClient({
            "bootstrap.servers": bootstrap_server,
        })

        metadata = client.list_topics(timeout=10)
        log.info(f" ✅ connected to bootstrap server {bootstrap_server}")
        log.info(f"got this broker metadata from AdminClient: {metadata.brokers}")

        producer = Producer({
            "bootstrap.servers": bootstrap_server,
        })

        consumer = Consumer({
            "bootstrap.servers": bootstrap_server,
            "group.id": "agent",
            "auto.offset.reset": "earliest",
        })

        consumer.subscribe(topics)

        self._client = client
        self._producer = producer
        self._consumer = consumer

        self._topics = topics
        self._bootstrap_server = bootstrap_server
        self._kafka_server_ip = kafka_server_ip
        self._kafka_server_port = kafka_server_port

    def handle_message(self, msg: Message):
        """This is were you would implement your agent logic."""
        log.info(f" 💌 got this message from Kafka: {msg.value().decode('utf-8')}")

    def run(self, *args, **kwargs):
        """ """

        while True:
            msg = self._consumer.poll(1.0)

            if msg is None:
                continue

            if msg.error():
                log.error(f" ⛔ consumer error: {msg.error()}")
                continue

            self.handle_message(msg)

