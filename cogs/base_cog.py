import discord
from discord.ext import interaction
from sqlalchemy import Result
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import select
from sqlalchemy.sql import exists
from typing import Callable, Coroutine, Any, TypeVar

from models import database

T = TypeVar('T')


class BaseCog:
    def __init__(self, client: interaction.Client, factory: async_sessionmaker):
        self.client = client
        self.factory = factory

    def session(self):
        return self.factory()

    @staticmethod
    def _get_user_id(argument: discord.User | discord.Member | int) -> int:
        if not isinstance(argument, int) and hasattr(argument, 'id'):
            argument = argument.id
        return argument

    async def _session_execute(
            self,
            query: Callable[[AsyncSession, ...], Coroutine[Any, Any, T]],
            commit_able: bool = False,
            session: AsyncSession = None,
            *args,
            **kwargs
    ) -> T:
        single_session = False
        if session is None:
            single_session = True
            session = self.session()

        result = await query(session, *args, **kwargs)

        if single_session:
            if commit_able:
                await session.commit()
            await session.close()
        return result

    @staticmethod
    async def _is_exist_participant_command(session: AsyncSession, author: int) -> bool:
        query = select(exists(database.UserInfo).where(database.UserInfo.id == author))
        data: Result = await session.execute(query)
        result = data.scalar_one_or_none()
        return bool(result)

    async def is_exist_participant(
            self,
            author: discord.User | discord.Member | int,
            session: AsyncSession = None
    ) -> bool:
        author = self._get_user_id(author)
        result = await self._session_execute(self._is_exist_participant_command, False, session, author=author)
        return bool(result)

    @staticmethod
    async def _get_participant_command(session: AsyncSession, author: int):
        query = select(database.UserInfo).where(database.UserInfo.id == author)
        data: Result = await session.execute(query)
        result = data.scalar_one_or_none()
        return result

    async def get_participant(
            self,
            author: discord.User | discord.Member | int,
            session: AsyncSession = None
    ) -> database.UserInfo:
        author = self._get_user_id(author)
        result = await self._session_execute(self._get_participant_command, False, session, author=author)
        return result

    @property
    def embed_init(self) -> discord.Embed:
        return discord.Embed(title="감자 챌린지(Gamja Challenge)")

    @property
    def indicator_animated_emoji(self) -> discord.PartialEmoji:
        return discord.PartialEmoji(name="wait", id=1129377087430606927, animated=True)

    @property
    def success_animated_emoji(self) -> discord.PartialEmoji:
        return discord.PartialEmoji(name="\U00002705")

    @property
    def failed_animated_emoji(self) -> discord.PartialEmoji:
        return discord.PartialEmoji(name="\U0000274C")


def setup(client: interaction.Client, factory: async_sessionmaker):
    return
