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

File created: 2024-02-10
Last updated: 2024-02-10
"""

from __future__ import annotations

import logging
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

log = logging.getLogger(__name__)


class Client(object):
    """ """

    def __new__(cls, *args, **kwargs) -> Client:
        """Setup for a singleton `Client` instance."""

        if not hasattr(cls, '_self'):
            cls._self = super().__new__(cls)

        return cls._self

    def __init__(
        self,
        llm_type: ChatOpenAI,
        emb_type: OpenAIEmbeddings,
        **kwargs,
    ):
        """ """

        pass

