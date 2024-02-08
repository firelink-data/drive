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
import sys
from agent_src import MasterAgent

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


DEFAULT_CONSUME_TOPICS = [
    "drive.user.master.dispatch",
    "drive.master.searcher.dispatch",
    "drive.master.mathematician.dispatch",
]

DEFAULT_PRODUCE_TOPICS = [
    "drive.user.master.response",
    "drive.master.searcher.response",
    "drive.master.mathematician.dispatch",
]


if __name__ == "__main__":
    """The main Kafka polling loop is implemented in the `Agent.run()` method."""

    agent = MasterAgent(
        consume_topics=DEFAULT_CONSUME_TOPICS,
        produce_topics=DEFAULT_PRODUCE_TOPICS,
    )
    sys.exit(agent.run())
