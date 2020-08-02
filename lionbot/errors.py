class DiscordError(Exception):
    """
    Exception raised when Discord rejects a message.
    """
    def __init__(self, response, body):
        self.body = body
        self.response = response


class ValidationException(Exception):
    def __init__(self, source, sha, body):
        self.source = source
        self.incoming_sha = sha
        self.body = body


class SubscriptionError(Exception):
    """
    Exception raised when a request to subscribe failed.
    """
    def __init__(self, source, response):
        self.source = source
        self.response = response


class AuthenticationError(Exception):
    """
    Exception raised when failing to authenticate.
    """

    def __init__(self, source, response):
        self.source = source
        self.response = response