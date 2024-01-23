"""

File created: 2024-01-23
Last updated: 2024-01-23
"""

import logging
import os


log = logging.getLogger(__name__)
log.setLevel(os.getenv("LOGLEVEL", logging.INFO))


def set_log_level(level: int) -> None:
    """ Set the desired level of the global logging module. """
    log.setLevel(level)

