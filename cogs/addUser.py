import discord
from discord.ext import interaction
from sqlalchemy.orm import sessionmaker

from utils.directory import directory
from models.database.userInfo import UserInfo


class AddUser:
    def __init__(self, bot: interaction.client) -> None:
        self.client = bot

    @interaction.command(name="시즌등록", description="이번 시즌에 참가하기 위하여 정보를 입력해주세요")
    @interaction.option(
        name="type",
        choices=[
            interaction.CommandOptionChoice(name="백준", value="beakjoon"),
            interaction.CommandOptionChoice(name="깃허브", value="github")
        ],
        description="등록할 계정의 유형을 선택해주세요."
    )
    @interaction.option(name="id", description="시즌 등록을 위한 아이디를 입력해주세요")
    async def add_user(self, ctx: interaction.ApplicationContext, account_type: str):
        user_info = UserInfo()
        embed = discord.Embed()
        # if False:  # solved ac => Not Found // Git GraphQL => "data" : {"User" : null}s
        #     embed.add_field(
        #         name="ID 등록 실패 :(",
        #         value="없는 ID 입니다. ID를 다시 한번 확인해주세요"
        #     )
        #     await ctx.send(embad=embed)
        #     return

        # if type == "백준":
        #     embed.add_field(name="Git ID 등록 완료 :D", value="github user info load")
        #     user_info.github_id = user
        # else:
        #     user_info.beakjoon_id = user
        #     embed.add_field(name="Beakjoon ID 등록 완료 :D", value="beackjoon user info load")

        await ctx.send(embed=embed)


def setup(client: interaction.Client, factory: sessionmaker):
    return client.add_interaction_cog(AddUser(client))
