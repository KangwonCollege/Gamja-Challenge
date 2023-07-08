import aiohttp
import asyncio
import datetime


from utils.fileOpen import read_file
from utils.getConfig import get_config
from utils.directory import directory

class GitUserProfile():
    def __init__(self) -> None:
        pass
    
    async def loadGitUserData(self, user, date) -> int:
        git_url = "https://api.github.com/graphql"
        
        async with aiohttp.ClientSession() as session:

            token = get_config()["git_token"]
            with open(directory+"gitQuery.graphql", "r") as f:
                query = f.read()

            header = { "Authorization" : f"Bearer {token}"}
            variable = {
                "login" : f"{user}",
                "from" : "2023-05-02T16:59:24Z", # iso 8601(2023-05-02T16:59:24Z)
                "to" : f"{date}"
            }

            async with session.post(git_url, headers=header , json = {"query" : query, "variables" : variable}) as response:
                result = await response.json()

        return result
