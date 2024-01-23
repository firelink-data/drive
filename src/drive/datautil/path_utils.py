"""
"""

from pathlib import Path


def default_drive_path() -> Path:
    """ """

    return Path.home() / ".drive"
