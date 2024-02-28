import discord
from discord.ext import interaction

from sqlalchemy.ext.asyncio import async_sessionmaker

from cogs.base_cog import BaseCog
from repository.user_repository import UserRepository


class Profile(BaseCog, UserRepository):
    def __init__(self, bot: interaction.Client, factory: async_sessionmaker) -> None:
        super().__init__(bot, factory)
        self.bot = bot
        self.factory = factory

    @interaction.command(name="프로필", description="이번 시즌 프로필을 불러옵니다")
    async def profile(self, ctx: interaction.ApplicationContext) -> None:
        await ctx.defer()

        user = ctx.author
        data = await UserRepository(self.factory).get_participant(author=user)

        embed = self.embed_init
        embed.add_field(name=ctx.author.name, value=data)

        await ctx.edit(embed=embed)


def setup(client: interaction.Client, factory: async_sessionmaker):
    client.add_interaction_cog(Profile(client, factory))
