<div align="center">
<br/>
<br/>

<a href="https://github.com/firelink-data/drive">
<img align="center" width=35% src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/57/Drive_2011_Film.svg/3000px-Drive_2011_Film.svg.png"></img>
</a>

<br/>
<br/>

[![PyPI - Version](https://img.shields.io/pypi/v/drivepy)](https://pypi.org/project/drivepy)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![codecov](https://codecov.io/gh/firelink-data/drive/graph/badge.svg?token=JTMK8O4CEO)](https://codecov.io/gh/firelink-data/drive)
[![CI](https://github.com/firelink-data/drive/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/firelink-data/drive/actions/workflows/ci.yml)
[![CD](https://github.com/firelink-data/drive/actions/workflows/cd.yml/badge.svg?branch=main)](https://github.com/firelink-data/drive/actions/workflows/cd.yml)
[![Tests](https://github.com/firelink-data/drive/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/firelink-data/drive/actions/workflows/tests.yml)
[![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)
[![Lint style: Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

*"I drive." - Gyan Rosling LLM agent 2024*

<br/>
</div>

## 🔎 Overview

*drive* enables you to create and manage a fully autonomous- and highly customizable LLM agent *farm*. It is built using Apache Kafka, Docker, and LangChain, which allows for extremely robust and scalable communication between agents.

The tool allows you you to either create and run agents from plug-n-play templates or create your completely custom agents with specialized personalities, tools, and logic. However, creating custom agents requires you to be rather familiar with the LangChain eco-system, LLM agents, prompting, and bindable tools for them. We recommend anyone that wants to create a custom agent to read up on custom agents in the LangChain documentation, e.g., [this link](https://python.langchain.com/docs/modules/agents/how_to/custom_agent).

## 📦 Installation

To install Apache Kafka, please use the installation scripts available at our [firelink]() repository.
If you want to install it manually yourself, make sure to follow the Docker with Kafka
setup documentation available under docs/.

```
python -m pip install drivepy
```

## 📋 License

All code is to be held under a general MIT license, please see [LICENSE](https://github.com/firelink-data/drive/blob/main/LICENSE) for specific information.

