import requests

from users_validation import UsersValidation


class APIToken(UsersValidation):
    """
    CSP api Token Generation
    """
    def __init__(self, username, password, measurement):
        """
        Initialization to have username and password

        :param username: Provide api username
        :param password: Provide api password
        """
        self.username = username
        self.password = password
        self.measurement = measurement
        self.app_token = None

    def application_token(self, url):
        """
        Application Token generation

        :param url: Provide application token url
        :return: return token in dictionary
        :rtype: dict
        """

        self.app_token = requests.post(url=url, timeout=10, auth=(self.username, self.password))
        return self.app_token.json()

    def customer_token(self, url, username, password):
        """
        Customer Token generation

        :param url: Provide customer token url
        :param username: Provide customer username used in payload
        :param password: Provide customer password used in payload
        :return: return token in dictionary
        :rtype: dict
        """

        method = requests.post(url=url, timeout=10, auth=(self.username, self.password),
                               data="username=%s&password=%s" % (username, password),
                               headers={"Content-Type": "text/plain"},
                               )
        return method