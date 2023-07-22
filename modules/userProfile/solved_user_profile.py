import aiohttp


class SolvedUserProfile:
    def __init__(self) -> None:
        pass
    
    async def loadSolvedUserData(self, user : str) -> int:
        solved_url = "https://solved.ac/api/v3/user/problem_stats"
        
        async with aiohttp.ClientSession() as session:
            param = {"handle" : user}
            async with session.get(solved_url, params=param) as response:
                result = await response.json()
        
        return result