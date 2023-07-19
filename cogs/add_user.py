import random
import string

import discord
from discord.ext import interaction
from sqlalchemy.ext.asyncio import async_sessionmaker
from typing import Optional

from cogs.base_cog import BaseCog
from modules import githubOauth2
from modules import errors
from repository.user_repository import UserRepository
from utils.getConfig import get_config

parser = get_config()


class AddUser(BaseCog, UserRepository):
    def __init__(self, bot: interaction.Client, factory: async_sessionmaker) -> None:
        super().__init__(bot, factory)
        self.bot = bot
        self.generated_state_key = []
        self.client = githubOauth2.GithubOAuth2(
            client_id=parser.get('Github', 'client_id'),
            client_secret=parser.get('Github', 'client_secret')
        )

        self.bot.add_setup_hook(self.setup_hook)

    async def setup_hook(self):
        # Circuital Issue: Session and connector has to use same event loop
        self.client.requests.loop = self.bot.loop

    def generate_state_key(self) -> str:
        state_key = ""
        for _ in range(8):
            state_key += random.choice(string.ascii_lowercase)

        if state_key in self.generated_state_key:
            return self.generate_state_key()
        self.generated_state_key.append(state_key)
        return state_key

    @interaction.command(name="시즌등록")
    async def add_user(self, ctx: interaction.ApplicationContext, account_type: str):
        pass

    @add_user.subcommand(name="깃허브", description="깃허브 계정으로 시즌에 참가하려면 시즌등록 명령어를 이용해주세요.")
    async def github_add_user(self, ctx: interaction.ApplicationContext):
        await ctx.defer(hidden=True)
        if not await self.is_exist_participant(ctx.author):
            user_info = await self.github_register_user(ctx)
        else:
            user_info = await self.get_participant(ctx.author)

    async def github_register_user(self, ctx: interaction.ApplicationContext) -> Optional[githubOauth2.User]:
        embed = self.embed_init
        state = self.generate_state_key()
        embed.description = (
            "감자 챌린지의 `깃허브` 부분을 참가하기 위해서는 깃허브 로그인이 필요합니다.\n"
            "아래의 로그인 버튼을 눌러 깃허브 로그인을 진행해주세요."
        )
        embed.add_field(
            name="로그인 상태",
            value="{} 대기 중".format(self.indicator_animated_emoji.__str__()),
            inline=True
        )
        components = interaction.ActionRow(components=[
            interaction.Button(
                style=discord.ButtonStyle.link,
                url=self.client.authorize(
                    redirect_uri="http://localhost:8080/login/callback",
                    scope=[githubOauth2.Scope.user],
                    state=state,
                ),
                label="로그인"
            )
        ])
        await ctx.edit(embed=embed, components=[components])
        _, access_token = await self.bot.wait_for(
            "login_success",
            check=lambda process_state, _: process_state == state
        )
        access_token: githubOauth2.AccessToken

        components.components[0].disabled = True
        embed.set_field_at(
            index=0,
            name=embed.fields[0].name,
            value="{} 사용자 정보 확인 중".format(self.indicator_animated_emoji.__str__()),
            inline=embed.fields[0].inline
        )
        await ctx.edit(embed=embed, components=[components])
        try:
            user_info = await self.client.user(access_token=access_token)
        except errors.HttpException:
            embed.description += (
                "\n\n 사용자 정보를 불러오는 과정에서 오류가 발생하였습니다. \n"
                "다시 시도해주시기 바랍니다."
            )
            embed.set_field_at(
                index=0,
                name=embed.fields[0].name,
                value="{} 실패".format(self.failed_animated_emoji.__str__()),
                inline=embed.fields[0].inline
            )
            await ctx.edit(embed=embed, components=[components])
            return

        embed.set_field_at(
            index=0,
            name=embed.fields[0].name,
            value="{} 성공".format(self.success_animated_emoji.__str__()),
            inline=embed.fields[0].inline
        )
        await ctx.edit(embed=embed, components=[components])
        print(user_info.name)
        return user_info

    @add_user.subcommand(name="백준", description="백준 계정으로 시즌에 참가하려면 시즌등록 명령어를 이용해주세요.")
    async def baekjoon_add_user(self, ctx: interaction.ApplicationContext):
        if await self.is_exist_participant(ctx.author):
            embed = discord.Embed(title="감자 챌린지(Gamja Challenge)", description="이미 등록된 계정입니다.")
            await ctx.send(embed=embed)
            return

    async def baekjoon_register_user(self, ctx: interaction.ApplicationContext):
        embed = self.embed_init
        embed.description = (
            "감자 챌린지의 `백준` 부분을 참가하기 위해서는 사용자 등록 과정이 필요합니다.\n"
            "아래의 등록 버튼을 눌러서 등록해주세요."
        )
        components = interaction.ActionRow(components=[
            interaction.Button(
                style=discord.ButtonStyle.primary,
                custom_id="baekjoon_sumbit_id",
                label="등록"
            )
        ])
        await ctx.send(embed=embed, components=[components])
        return


def setup(client: interaction.Client, factory: async_sessionmaker):
    return client.add_interaction_cog(AddUser(client, factory))
