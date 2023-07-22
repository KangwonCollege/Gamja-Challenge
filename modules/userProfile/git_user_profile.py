import aiohttp
from PIL import Image
import discord

from utils.getConfig import get_config
from utils.directory import directory
from models.database.baekjoonUserInfo import BaekjoonUserInfo
from models.database.githubUserInfo import GithubUserInfo
from models.database.userInfo import UserInfo


class UserProfile(BaekjoonUserInfo, GithubUserInfo, UserInfo):
    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    async def _load_git_user_data(user, date) -> int:
        git_url = "https://api.github.com/graphql"

        async with aiohttp.ClientSession() as session:
            token = get_config()["git_token"]
            with open(directory + "gitQuery.graphql", "r") as f:
                query = f.read()

            header = {"Authorization": f"Bearer {token}"}
            variable = {
                "login": f"{user}",
                "from": "2023-05-02T16:59:24Z",  # iso 8601(2023-05-02T16:59:24Z)
                "to": f"{date}"
            }

            async with session.post(git_url, headers=header, json={"query": query, "variables": variable}) as response:
                result = await response.json()

        return result

        def make_rank_profile(self, discord_name: str, discord_profile_img: discord.User.banner, ) -> Image:
            BaekjoonUserInfo.baekjoon_id
