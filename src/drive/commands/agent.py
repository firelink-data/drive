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
Last updated: 2024-01-24
"""

import click
import os


__all__ = ("agent_group",)


@click.group(name="agent")
def agent():
    """ 🤖 Tools to manage your LLM agents. """
    pass


@agent.command(name="create")
def create():
    """ 📝 Create a new agent container, either custom or from templates. """
    pass


@agent.command("build")
def build():
    """ 👷 Build the docker container for the agent. """

    os.system("sudo docker build -t agent-bond ~/.drive/agents/Bond")


@agent.command(name="start")
def start():
    """ 🟢 Start an existing agent."""

    os.system("sudo docker run agent-bond")


@agent.command(name="stop")
def stop():
    """ 🔴 Stop an existing agent that is alive. """
    pass


agent_group = agent
