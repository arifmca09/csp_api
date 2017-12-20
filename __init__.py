
from .token import APIToken
from .users_validation import UsersValidation


class CSPApi(APIToken, UsersValidation):
    def __init__(self, username, password):
        super().__init__(username, password)
