import logging
import sys
from src import Agent

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


if __name__ == "__main__":
    """The main Kafka polling loop is implemented in the `Agent.run()` method."""

    agent = Agent(topics=["agent-query"])
    sys.exit(agent.run())

