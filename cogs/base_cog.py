import discord
from discord.ext import interaction
from sqlalchemy import Result
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import select
from sqlalchemy.sql import exists

from models import database


class BaseCog:
    def __init__(self, client: interaction.Client, factory: async_sessionmaker):
        self.clinet = client
        self.factory = factory

    def session(self):
        return self.factory()

    async def is_exist_participant(self, author: discord.User | discord.Member | int, session: AsyncSession = None) -> bool:
        if not isinstance(author, int) and hasattr(author, 'id'):
            author = author.id

        single_session = False
        if session is None:
            single_session = True
            session = self.session()

        query = select(exists(database.UserInfo).where(database.UserInfo.id == author))
        data: Result = await session.execute(query)
        result = data.scalar_one_or_none()

        if single_session:
            await session.close()
        return bool(result)


def setup(client: interaction.Client, factory: async_sessionmaker):
    return
