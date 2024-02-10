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
Last updated: 2024-02-08
"""

import click
import os
import subprocess
import logging
from drive.agent import (
    create_custom_agent,
    create_template_agent,
)

__all__ = ("agent_group",)

log = logging.getLogger(__name__)


@click.group(name="agent")
def agent():
    """🤖 Tools to manage your LLM agents."""
    pass


@agent.command(name="create")
@click.argument(
    "name", nargs=1, required=True,
)
@click.option(
    "-c",
    "--custom",
    "custom",
    is_flag=True,
    show_default=True,
    default=False,
)
def create(
    name: str,
    custom: bool,
):
    """📝 Create a new agent container, either custom or from templates."""

    create_fn = create_custom_agent if custom else create_template_agent
    create_fn(name)


@agent.command("build")
def build():
    """👷 Build the docker container for the agent."""

    os.system("sudo docker build -t agent-bond ~/.drive/agents/Bond")


@agent.command(name="start")
def start():
    """🟢 Start an existing agent."""

    kafka_server_ip = subprocess.getoutput(
        "/sbin/ip a | awk '/inet 192/ { print $2 }'",
    ).split("/")[0]

    print(kafka_server_ip)

    os.system(
        f"sudo docker run --env KAFKA_SERVER_IP={kafka_server_ip} --env KAFKA_SERVER_PORT=19092 agent-bond"
    )


@agent.command(name="stop")
def stop():
    """🔴 Stop an existing agent that is alive."""
    pass


agent_group = agent
