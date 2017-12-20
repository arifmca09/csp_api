#!/usr/bin/env python

import sys
import requests
from types import SimpleNamespace


class APIToken(object):
    """
    CSP API Token Generation
    """
    def __init__(self, username, password):
        """
        Initialization to have username and password

        :param username: Provide api username
        :param password: Provide api password
        """

        self.username = username
        self.password = password
        self.app_token = None
        self.cus_token = None

    def application_token(self, url):
        """
        Application Token generation

        :param url: Provide application token url
        :return: return token in dictionary
        :rtype: dict
        """
        try:
            method = requests.post(url=url, timeout=10, auth=(self.username, self.password))
            self.app_token = SimpleNamespace(**method.json())
            return self.app_token
        except Exception as e:
            print(e)
            sys.exit(2)

    def customer_token(self, url, username, password):
        """
        Customer Token generation

        :param url: Provide customer token url
        :param username: Provide customer username used in payload
        :param password: Provide customer password used in payload
        :return: return token in dictionary
        :rtype: dict
        """
        try:
            method = requests.post(url=url, timeout=10, auth=(self.username, self.password),
                                   data="username=%s&password=%s" % (username, password),
                                   headers={"Content-Type": "text/plain"},
                                   )
            self.cus_token = SimpleNamespace(**method.json())
            return self.cus_token
        except Exception as e:
            print(e)
            sys.exit(2)
