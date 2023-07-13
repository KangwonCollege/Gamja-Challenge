from .scope import Scope


class AccessToken:
    def __init__(
            self,
            access_token: str,
            token_type: str,
            scope: list[Scope]
    ):
        self.access_token = access_token
        self.scope = scope
        self.token_type = token_type

    @classmethod
    def from_payload(cls, payload: dict[str]):
        scope = payload['scope'].split(',')
        _scope = []
        for s in scope:
            for v in list(Scope):
                if v.value == s:
                    _scope.append(v)
                    break
        return cls(
            access_token=payload['access_token'],
            token_type=payload['token_type'],
            scope=_scope
        )
