import logging
import langchain  # noqa
from .tools import *  # noqa
from confluent_kafka import Consumer

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


class Agent(object):
    """ """

    def __init__(self, topics):
        """ """

        consumer = Consumer({
            "bootstrap.servers": "localhost:9093",
            "group.id": "agent",
            "auto.offset.reset": "earliest",
        })

        consumer.subscribe(topics)

        self._consumer = consumer
        self._topics = topics

    def handle_message(self, msg: str):
        """ This is were you would implement your agent logic. """

        log.info(f"got this message from Kafka: {msg}")


    def run(self, *args, **kwargs):
        """ """

        while True:
            msg = self._consumer.poll(1.0)

            if msg is None:
                continue

            if msg.error():
                log.error(f"consumer error: {msg.error()}")

            self.handle_message(msg)

