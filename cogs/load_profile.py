import discord
from discord.ext import interaction
from sqlalchemy.ext.asyncio import async_sessionmaker
from datetime import datetime

from cogs.base_cog import BaseCog


class LoadProfile:
    def __init__(self, bot: interaction.Client, factory: async_sessionmaker) -> None:
        # super().__init__(bot, factory)
        self.bot = bot

    @interaction.command(name="티어확인", description="이번 시즌 티어를 확인할 수 있습니다")
    async def check_tier(self, ctx: interaction.ApplicationContext):
        embed = discord.Embed(title="티어확인 Title", timestamp=datetime.today())  # self.embed_init
        embed.description = (
            "description"
        )
        print(ctx.author.avatar, type(ctx.author))
        embed.set_author(name=ctx.name, url=ctx.author.avatar, icon_url=ctx.author.avatar)
        # embed.set_image(url=ctx.author.avatar)  # url only
        embed.set_footer(text=f"갱신시각")  # datetime.timestamp()

        return await ctx.send(embed=embed, content="<t:111>")

    @interaction.command(name="랭킹확인", description="이번 시즌 서버 내 자신의 랭킹을 확인할 수 있습니다")
    async def check_rank(self, ctx: interaction.ApplicationContext):
        embed = discord.Embed()
        embed.set_image(url="")  # url only

        return ctx.send("test")


def setup(client: interaction.Client, factory: async_sessionmaker):
    return client.add_interaction_cog(LoadProfile(client, factory))
