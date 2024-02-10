from .agent import Agent  # noqa


def create_custom_agent(name: str):
    raise NotImplementedError


def create_template_agent(name: str):
    """
    Available templates:
        - Mathematician
        - Master
        - Searcher

    """

    pass
