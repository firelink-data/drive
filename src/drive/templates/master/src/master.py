from confluent_kafka import Message
from drive.agent import Agent


class MasterAgent(Agent):
    """ """

    def __init__(self, *args, **kwargs):
        super(MasterAgent, self).__init__("Master", *args, **kwargs)

    def handle_message(self, msg: Message):
        """ """
        pass

