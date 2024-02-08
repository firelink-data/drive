"""
MIT License

Copyright (c) 2024 Firelink Data

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

File created: 2024-02-08
Last updated: 2024-02-08
"""

import logging
import os
from confluent_kafka import Consumer, Message, Producer
from confluent_kafka.admin import AdminClient
from typing import List

log = logging.getLogger(__name__)


class Agent(object):
    """ """

    def __init__(self,
        name: str,
        consumer_topics: List[str],
        producer_topics: List[str],
        **kwargs,
    ):
        """ """

        kafka_server_ip = kwargs.get(
            "kafka_server_ip",
            os.environ["KAFKA_SERVER_IP"],
        )
        kafka_server_port = kwargs.get(
            "kafka_server_port",
            os.environ["KAFKA_SERVER_PORT"],
        )
        bootstrap_server = f"{kafka_server_ip}:{kafka_server_port}"

        admin_client = AdminClient({
            "bootstrap.servers": bootstrap_server,
        })

        producer_client = Producer({
            "bootstrap.servers": bootstrap_server,
        })

        kafka_consumer_group_id = os.environ.get("KAFKA_CONSUMER_GROUP_ID", "1")
        kafka_auto_offset_reset = os.environ.get("KAFKA_AUTO_OFFSET_RESET", "earliest")
        consumer_client = Consumer({
            "bootstrap.servers": bootstrap_server,
            "group.id": kafka_consumer_group_id,
            "auto.offset.reset": kafka_auto_offset_reset,
        })

        consumer_client.subscribe(consumer_topics)

        config = {}
        config["kafka.server.ip"] = kafka_server_ip
        config["kafka.server.port"] = kafka_server_port
        config["bootstrap.server"] = bootstrap_server

        config["producer.topics"] = producer_topics
        config["consumer.topics"] = consumer_topics
        config["consumer.group.id"] = kafka_consumer_group_id
        config["consumer.auto.offset.reset"] = kafka_auto_offset_reset

        self._config = config
        self._admin_client = admin_client
        self._producer_client = producer_client
        self._consumer_client = consumer_client

    def handle_message(self, msg: Message):
        """Each created agent has to implement logic to handle messages here."""
        raise NotImplementedError

    def run(self) -> int:
        """ """

        while True:
            try:
                msg = self.poll()

                if msg is None:
                    continue

                if msg.error():
                    log.error(f" ⚠️  Consumer error: {msg.error()}")
                    continue

                self.handle_message(msg)
            except:  # noqa
                log.error("Something bad happened, terminating...")
                return 1
            finally:
                log.info("Shutting down agent! Bye.")
                return 0

