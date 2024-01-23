"""

File created: 2024-01-23
Last updated: 2024-01-23
"""

import logging
import os
import click
from drive import commands


log = logging.getLogger(__name__)
log.setLevel(os.getenv("LOGLEVEL", logging.INFO))


def set_log_level(level: int) -> None:
    """ Set the desired level of the global logging module. """
    log.setLevel(level)



@click.group()
def cli():
    """ 🚀 DRIVE, managing autonomous LLM agents made easy! """
    pass


# Register the grouped `click` commands to the `cli` entry point.
for group in commands.groups:
    cli.add_command(group)

