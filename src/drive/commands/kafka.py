import click


@click.group()
def kafka():
    """ """
    pass


@kafka.command()
def start():
    """ """
    pass


@kafka.command()
def stop():
    """ """
    pass


kafka_group = kafka
