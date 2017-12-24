#!/usr/bin/env python

from .token import APIToken
from .request import APIRequest


class CSPApi(APIToken, APIRequest):
    def __init__(self, username, password):
        super().__init__(username, password)

