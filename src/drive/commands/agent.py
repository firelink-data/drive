import click


@click.group()
def agent():
    """ """
    pass


@agent.command()
def create():
    """ """
    pass


@agent.command()
def start():
    """ """
    pass

@agent.command()
def stop():
    """ """
    pass


agent_group = agent
