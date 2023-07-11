from datetime import datetime
from typing import Any, Optional


class User:
    def __init__(self, payload: dict[str, Any]):
        self.id: int = payload['id']
        self.login: str = payload.get('login')
        self.node_id: str = payload.get('node_id')
        self.avatar_url: str = payload.get('avatar_url')
        self.gravatar_id: str = payload.get('gravatar_id')
        self.type: str = payload.get('type')
        self.site_admin: bool = payload.get('site_admin')
        self.name: bool = payload.get('name')
        self.company: str = payload.get('company')
        self.blog: str = payload.get('blog')
        self.location: str = payload.get('location')
        self.email: str = payload.get('email')
        self.hireable: Optional[str] = payload.get('hireable')
        self.bio: Optional[str] = payload.get('bio')
        self.twitter_username: Optional[str] = payload.get('twitter_username')
        self.public_repos: int = payload.get('public_repos')
        self.public_gists: int = payload.get('public_gists')
        self.followers: int = payload.get('followers')
        self.following: int = payload.get('following')
        self._created_at: str = payload.get('created_at')
        self._updated_at: str = payload.get('updated_at')
        self.private_gists: int = payload.get('private_gists')
        self.total_private_repos: int = payload.get('total_private_repos')
        self.owned_private_repos: int = payload.get('owned_private_repos')
        self.disk_usage: int = payload.get('disk_usage')
        self.collaborators: int = payload.get('collaborators')
        self.two_factor_authentication: bool = payload.get('two_factor_authentication')
        self.plan: dict[str, Any] = payload.get('plan')

    @property
    def created_at(self) -> datetime:
        return datetime.fromisoformat(self._created_at)

    @property
    def updated_at(self) -> datetime:
        return datetime.fromisoformat(self._updated_at)
