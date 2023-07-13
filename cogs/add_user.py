import random
import string

import discord
from discord.ext import interaction
from sqlalchemy.ext.asyncio import async_sessionmaker

from cogs.base_cog import BaseCog
from modules import githubOauth2
from utils.getConfig import get_config

parser = get_config()


class AddUser(BaseCog):
    def __init__(self, bot: interaction.client, factory: async_sessionmaker) -> None:
        super().__init__(bot, factory)
        self.generated_state_key = []
        self.client = githubOauth2.GithubOAuth2(
            client_id=parser.get('Github', 'client_id'),
            client_secret=parser.get('Github', 'client_secret')
        )

    def generate_state_key(self) -> str:
        state_key = ""
        for _ in range(8):
            state_key += random.choice(string.ascii_lowercase)

        if state_key in self.generated_state_key:
            return self.generate_state_key()
        self.generated_state_key.append(state_key)
        return state_key

    @interaction.command(name="시즌등록", description="이번 시즌에 참가하기 위하여 정보를 입력해주세요")
    @interaction.option(
        name="type",
        choices=[
            interaction.CommandOptionChoice(name="백준", value="beakjoon"),
            interaction.CommandOptionChoice(name="깃허브", value="github")
        ],
        description="등록할 계정의 유형을 선택해주세요."
    )
    async def add_user(self, ctx: interaction.ApplicationContext, account_type: str):
        state = self.generate_state_key()
        if await self.is_exist_participant(ctx.author):
            embed = discord.Embed(title="감자 챌린지(Gamja Challenge)", description="이미 등록된 계정입니다.")
            await ctx.send(embed=embed)
            return
        embed = discord.Embed(title="감자 챌린지(Gamja Challenge)")
        if account_type == "github":
            embed.description = (
                "감자 챌린지의 `깃허브` 부분을 참가하기 위해서는 깃허브 로그인이 필요합니다.\n"
                "아래의 로그인 버튼을 눌러 깃허브 로그인을 진행해주세요."
            )
            components = interaction.ActionRow(components=[
                interaction.Button(
                    style=discord.ButtonStyle.link,
                    url=self.client.authorize(
                        redirect_uri="https://localhost:8080/session/callback",
                        scope=[githubOauth2.Scope.user],
                        state=state,
                    ),
                    label="로그인"
                )
            ])
        elif account_type == "beakjoon":
            embed.description = (
                "감자 챌린지의 `백준` 부분을 참가하기 위해서는 사용자 등록 과정이 필요합니다.\n"
                "아래의 등록 버튼을 눌러서 등록해주세요."
            )
            components = interaction.ActionRow(components=[
                interaction.Button(
                    style=discord.ButtonStyle.link,
                    url=self.client.authorize(
                        redirect_uri="https://localhost:8080/session/callback",
                        scope=[githubOauth2.Scope.user],
                        state=state,
                    ),
                    label="로그인"
                )
            ])
        await ctx.send(embed=embed, components=[components])

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


def setup(client: interaction.Client, factory: async_sessionmaker):
    return client.add_interaction_cog(AddUser(client, factory))
