from .scope import Scope
from utils.pointerQueue import PointerQueue


class GithubOAuth2(PointerQueue):
    def __init__(
            self,
            client_id: str,
            client_secret: str
    ):
        self.client_id = client_id
        self.client_secret = client_secret

        self.BASE = "https://github.com"

    def add_parameter(
            self,
            position: int,
            key: str,
            value: str,
            ended: bool = False
    ) -> None:
        self._pointer_value[position] += f"{key}={value}"
        if not ended:
            self._pointer_value[position] += "&"

    def authorize(
            self,
            scope: list[Scope],
            redirect_url: str = None,
            login: str = None,
            state: str = None,
            allow_signup: bool = True
    ):
        path = "/login/oauth/authorize"
        url = self.BASE + path

