#!/usr/bin/env python
import requests


class UsersValidation(object):
    """
    Module for CSP UserValidation API
    """
    def __init__(self, measurement):
        """
        Initialization for Users Validation

        :param measurement: Provide Influx DB measurement name
        """
        self.measurement = measurement

    def validate_customer(self, url):
        """
        Validate Customer API URL

        :param url: Provide validate customer URL API
        :return: Returns validate customer in dictionary
        :rtype: dict
        """

        method = requests.get(url=url, headers={"cn": "5043451834", "Authorization": "Bearer %s" %self.app_token.json()['access_token']})
        # print self.app_token.json()
        return method
