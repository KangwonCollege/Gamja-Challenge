import aiohttp
import asyncio
import datetime


from utils.fileOpen import read_file

class GitUserProfile():
    def __init__(self) -> None:
        pass
    
    async def loadGitUserData(self, user, date) -> int:
        async with aiohttp.ClientSession() as session:
            # with open(r"config\token.txt", "r") as f:
            #     token = f.read()

            token = await read_file(r"config\token.txt")
            with open("assats\gitQuery.graphql", "r") as f:
                query = f.read()

            header = { "Authorization" : f"Bearer {token}"}
            variable = {
                "login" : f"{user}",
                "from" : "2023-05-02T16:59:24Z", #2023-05-02T16:59:24Z
                "to" : f"{date}"
            }

            async with session.post("https://api.github.com/graphql", headers=header , json = {"query" : query, "variables" : variable}) as response:
                result = await response.json()

        return result
