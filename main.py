import datetime
import asyncio

from discord import Intents

from modules.gitUserData import GitUserData
from modules.gitUserProfile import GitUserProfile

async def main():
    git_user_data = GitUserData(name="Mule129")
    
    git_user_data.date = datetime.datetime.utcnow().isoformat()
    git_user_profile = GitUserProfile()
    git_user_data = await git_user_profile.loadGitUserData(git_user_data.name, git_user_data.date)
    print(git_user_data)
    print(datetime.datetime.utcnow().isoformat())
    date_ = datetime.timedelta(days=30)
    date_ = datetime.datetime.now() - date_
    print(date_.isoformat())

loop = asyncio.get_event_loop()
loop.run_until_complete(main())