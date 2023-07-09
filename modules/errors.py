from typing import Any


class HttpException(Exception):
    def __init__(self, response_code: int, data: dict[str, Any]):
        self.response_code = response_code
        self.data = data
        super(HttpException, self).__init__("HTTP Response Error: {}".format(response_code))


class NotFound(HttpException):
    pass


class InternalServerError(HttpException):
    pass
