import aiohttp

class SolvedUserProfile():
    def __init__(self) -> None:
        pass
    
    async def loadSolvedUserData(self, user : str) -> int:
        async with aiohttp.ClientSession() as session:
            header = {"handle" : user}
            async with session.get("https://solved.ac/api/v3/user/problem_stats", params=header) as response:
                result = await response.json()
        
        return result