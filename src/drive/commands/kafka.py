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

File created: 2024-01-23
Last updated: 2024-01-23
"""

import logging
import os
import click

__all__ = ("kafka_group",)

log = logging.getLogger(__name__)


@click.group()
def kafka():
    """🔗 Tools to manage your Kafka cluster."""
    pass


@kafka.command()
def start():
    """🟢 Start the Kafka cluster."""

    log.info("starting the Kafka server...")
    os.system(
        'su - kafka -c "kafka/bin/kafka-server-start.sh kafka/config/kraft/server.properties &"'
    )
    log.info("OK!")


@kafka.command()
def stop():
    """🔴 Stop the Kafka cluster."""

    log.info("stopping the Kafka server...")
    os.system(
        'su - kafka -c "kafka/bin/kafka-server-stop.sh kafka/config/kraft/server.properties &"'
    )
    log.info("OK!")


kafka_group = kafka
