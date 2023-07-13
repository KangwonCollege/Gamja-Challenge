import asyncio

from .access_token import AccessToken
from .scope import Scope
from .user import User

from modules.requests import Requests
from utils.pointerQueue import PointerQueue


class GithubOAuth2(PointerQueue):
    def __init__(self, client_id: str, client_secret: str, loop: asyncio.AbstractEventLoop = None):
        super().__init__()
        self.client_id = client_id
        self.client_secret = client_secret

        self.BASE = "https://github.com"
        self.API_BASE = "https://api.github.com"
        self.requests = Requests(loop=loop)

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
            redirect_uri: str = None,
            login: str = None,
            state: str = None,
            allow_signup: bool = True
    ):
        path = "/login/oauth/authorize"
        url = self.BASE + path

        _scope = [v.value for v in scope]

        position_value = self._add_pointer(f"{url}?")
        self.add_parameter(position_value, "client_id", self.client_id)
        if redirect_uri is not None:
            self.add_parameter(position_value, "redirect_uri", redirect_uri)
        if login is not None:
            self.add_parameter(position_value, "login", login)
        if state is not None:
            self.add_parameter(position_value, "state", state)
        if allow_signup is not None:
            self.add_parameter(position_value, "allow_signup", str(allow_signup))
        self.add_parameter(position_value, "scope", "%20".join(_scope), ended=True)
        return self._get_pointer(position_value)

    async def token(
            self,
            code: str,
            redirect_uri: str = None
    ):
        data = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "code": code
        }
        headers = {
            "Accept": "application/json"
        }
        if redirect_uri is not None:
            data["redirect_uri"] = redirect_uri
        response = await self.requests.post(
            "https://github.com/login/oauth/access_token",
            data=data,
            headers=headers,
            raise_on=True
        )
        return AccessToken.from_payload(response.data)

    async def user(self, access_token: AccessToken, login: str = None):
        url = self.API_BASE + "/user"
        if login is not None:
            url += "s/{}".format(login)

        headers = {
            "Authorization": f"{access_token.token_type} {access_token.access_token}"
        }
        response = await self.requests.get(
            url,
            headers=headers,
            raise_on=True
        )
        return User(response.data)
