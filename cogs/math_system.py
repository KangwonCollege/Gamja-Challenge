import discord
import sqlalchemy.ext.asyncio
from discord.ext import interaction
from sqlalchemy import select, Engine
from sqlalchemy.orm import Session, sessionmaker

from models.database.userInfo import UserInfo


class MathSystem:

    def __init__(self, bot: interaction.Client, factory: sessionmaker) -> None:
        self.client = bot
        self.factory = factory

    @interaction.command(name="랭크확인", description="자신의 랭크를 확인할 수 있습니다")
    async def check_lank(self, ctx: interaction.ApplicationContext,
                         engine: Engine) -> None:
        user_info = UserInfo()

        session = sessionmaker(bind=engine)
        stmt = select(UserInfo).where(UserInfo.id.in_([ctx.id]))
        for user in session.scalars(stmt):
            print(user)

        if ctx.id == user_info.id:
            embed = discord.Embed(title="랭크 확인",
                                  description=f"백준 ID : {user_info.beakjoon_id}\n 깃허브 ID : {user_info.github_id}")
            embed.add_field(name="랭크", value=user_info.tier)
