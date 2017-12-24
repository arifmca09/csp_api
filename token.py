#!/usr/bin/env python

import requests
from types import SimpleNamespace


class APIToken(object):
    """
    CSP API Token Generation
    """
    def __init__(self, username, password, timeout):
        """
        Initialization to have username and password

        :param username: Provide api username
        :param password: Provide api password
        """

        self.username = username
        self.password = password
        self.app_token = None
        self.cus_token = None
        self.timeout = timeout

    def application_token(self, url):
        """
        Application Token generation

        :param url: Provide application token url
        :return: return token in dictionary
        :rtype: dict
        """
        try:
            method = requests.post(url=url, timeout=self.timeout, auth=(self.username, self.password))
            self.app_token = SimpleNamespace(**method.json())
            return self.merge_object(self.app_token, method)
        except Exception as e:
            return e

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
            method = requests.post(url=url, timeout=self.timeout, auth=(self.username, self.password),
                                   data="username=%s&password=%s" % (username, password),
                                   headers={"Content-Type": "text/plain"},
                                   )
            self.cus_token = SimpleNamespace(**method.json())
            return self.merge_object(self.cus_token, method)
        except Exception as e:
            return e

    @staticmethod
    def merge_object(from_object, to_object):
        """
        Used to copy properties from one object to another if there isn't a naming conflict;

        :param from_object: Provide object (from) to merge
        :param to_object: Provide object (to) to merge
        :return: combined object of two different objects
        :rtype: object
        """
        for i in from_object.__dict__:
            if not callable(from_object.__dict__[i]) and not hasattr(to_object, i):
                setattr(to_object, i, getattr(from_object, i))
        return to_object
