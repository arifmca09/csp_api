#!/usr/bin/env python

import requests
from jsonmerge import merge as combine


class APIRequest(object):
    """
    Module for CSP API Validations
    """
    def __init__(self, timeout=10):
        """
        Initialization for Request Validation

        :param timeout: Provide timeout value for API call
        """
        self.timeout = timeout
        self.app_token = None

    def merge(self, headers):
        """
        Perform merge of headers with Authorization JSON

        :param headers: Provide headers in JSON
        :return: Returns merged headers
        :rtype: dict
        """
        authorization = {"Authorization": "Bearer %s" % self.app_token.access_token}
        merge = combine(headers, authorization)
        return merge

    def get(self, url, headers, proxies=None):
        """
        Perform GET request method

        :param url: Provide get request URL
        :param headers: Provide headers in JSON
        :param proxies: Provides proxy server in JSON format
        :return: Returns get request response in dictionary
        :rtype: dict
        """
        method = requests.get(url=url, headers=self.merge(headers=headers),
                              proxies=proxies, timeout=self.timeout
                              )
        return method

    def post(self, url, headers, data, proxies=None):
        """
        Perform POST request method

        :param url: Provide post request URL
        :param headers: Provide headers in JSON
        :param proxies: Provides proxy server in JSON format
        :param data: Provide payload data
        :return: returns response in dictionary
        :rtype: dict
        """
        method = requests.post(url=url, headers=self.merge(headers=headers),
                               data=data, proxies=proxies, timeout=self.timeout
                               )
        return method
