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

File created: 2024-01-26
Last updated: 2024-01-26
"""

import logging
from confluent_kafka import Message
from typing import Collection

log = logging.getLogger(__name__)


class Agent(object):
    """ """

    def __init__(self, topics: Collection[str]):
        """ """

        pass
    
    def handle_message(self, msg: Message) -> None:
        """Here the developer has to specify what to do on a new Kafka message."""
        raise NotImplementedError

    def run(self, *args, **kwargs) -> None:
        """This is the main execution loop of an Agent."""

        while True:
            msg = self._consumer.poll(self._poll_timeout)

            if msg is None:
                continue

            if msg.error():
                log.error(f"consumer error: {msg.error()}")

            self.handle_message(msg)

