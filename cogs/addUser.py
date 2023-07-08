from discord.ext import interaction
import discord

from utils.directory import directory
from models.database.userInfo import UserInfo

class AddUser():
    def __init__(self, bot: interaction.client) -> None:
        self.client = bot
        

    @interaction.command(name="시즌등록", description="이번 시즌에 참가하기 위하여 정보를 입력해주세요")
    @interaction.option(name="type", 
                        choices=[interaction.CommandOptionChoice("백준", "깃허브"),
                                 interaction.CommandOptionChoice("깃허브", "백준")],
                        description="ID 유형을 입력해주세요")
    @interaction.option(name="id", description="시즌 등록을 위한 아이디를 입력해주세요")
    async def addGitUser(self, ctx: interaction.ApplicationContext, type : str, user : str):
        user_info = UserInfo()
        embad = discord.Embed()
        if False: # solved ac => Not Found // Git GraphQL => "data" : {"User" : null}s
            embad.add_field(name="ID 등록 실패 :(", 
                            value="없는 ID 입니다. ID를 다시 한번 확인해주세요")
            await ctx.send(embad=embad)
            return

        if type == "백준":
            embad.add_field(name="Git ID 등록 완료 :D", value="github user info load")
            user_info.github_id = user
        else:
            user_info.beakjoon_id = user
            embad.add_field(name="Beakjoon ID 등록 완료 :D", value="beackjoon user info load")
        
        await ctx.send(embed=embad) # type이 반대로 뜨는 문제가 있어요

    

def setup(client: interaction.Client):
    return client.add_interaction_cog(AddUser(client))