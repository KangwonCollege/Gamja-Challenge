import os.path

import discord
from discord.ext import interaction
from sqlalchemy.ext.asyncio import async_sessionmaker
from datetime import datetime

from cogs.base_cog import BaseCog
from modules.userProfile.drawProfile import DrawProfile
from utils.directory import directory


class LoadProfile(BaseCog):
    def __init__(self, bot: interaction.Client, factory: async_sessionmaker) -> None:
        super().__init__(bot, factory)
        self.bot = bot

        self.embed_color = discord.Color.og_blurple()

    @interaction.command(name="유저정보", description="유저 정보를 확인할 수 있습니다")
    async def load_profile(self, ctx: interaction.ApplicationContext):
        path = os.path.join(directory, "assets", "tier_img", "bronze_1.png")
        file = discord.File(filename="tier.png", fp=path)

        embed = discord.Embed(title="유저정보", timestamp=datetime.today(), color=self.embed_color)
        embed.description = (
                "**user id : **" + str(ctx.author.id)
        )
        embed.set_thumbnail(url="attachment://tier.png")
        embed.add_field(name=":outbox_tray: **깃허브 기여도**", value="50 Commit")
        embed.add_field(name=":military_medal: **백준 푼 문제수**", value="30 Solved")
        embed.add_field(name=":trophy: **랭킹**", value="32위")
        embed.set_author(icon_url=ctx.author.avatar, name=ctx.author.name)

        embed.set_footer(text="확인 시각")

        return await ctx.send(embed=embed, file=file)

    @interaction.command(name="랭킹확인", description="이번 시즌 자신의 랭킹을 확인할 수 있습니다")
    async def check_rank(self, ctx: interaction.ApplicationContext):
        embed = discord.Embed(color=self.embed_color)
        embed.add_field(name="아직 개발중인 기능입니다", value="차후 업데이트를 기다려 주세요!")

        return await ctx.send(embed=embed)

    @interaction.command(name="프로필", description="이번 시즌 자신의 프로필 이미지를 로드합니다.")
    async def load_profile_img(self, ctx):
        path = os.path.join(directory, "assets", "dumpfile_profile.png")  # 이미지 중복 로드, 저장 공간 문제 발생 가능
        img = DrawProfile()
        new_img = img.user_profile(
            profile_image_url=ctx.author.avatar,
            user_name=ctx.author.name,
            user_id=ctx.author.id,
            # add userInfo DB data
        )
        new_img.save(path)

        return await ctx.send(file=discord.File(path))

    @interaction.command(name="캘린더", description="이번 시즌 자신의 캘린더 이미지를 로드합니다")
    async def load_calender_img(self, ctx):
        path = os.path.join(directory, "assets", "dumpfile_calender.png")
        img = DrawProfile()
        new_img = img.user_calender()
        new_img.save(path)

        return await ctx.send(file=discord.File(path))


def setup(client: interaction.Client, factory: async_sessionmaker):
    return client.add_interaction_cog(LoadProfile(bot=client, factory=factory))
