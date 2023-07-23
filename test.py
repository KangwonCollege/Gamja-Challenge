import os

import discord
import sqlalchemy
from discord.ext import interaction
from sqlalchemy import NullPool
from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import AsyncConnection
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import create_engine
from sqlalchemy import select
import asyncio

from models import database as db_model
from utils.getConfig import get_config
from models.database.baekjoonUserInfo import BaekjoonUserInfo


async def run(async_session: async_sessionmaker[AsyncSession]) -> None:
    async with async_session() as session:
        stmt = select(BaekjoonUserInfo).where(BaekjoonUserInfo.baekjoon_id.in_(["test1"]))
        data = await session.scalars(stmt)
        for user in data:
            print(user)


async def main() -> None:
    directory = os.path.dirname(os.path.abspath(__file__))
    parser = get_config()

    # Database
    database_parser = get_config("database")
    database_section = database_parser.get("Default", "database_section")
    database = {
        "drivername": "mysql+aiomysql",
        "username": database_parser.get(database_section, "user"),
        "host": database_parser.get(database_section, "host"),
        "password": database_parser.get(database_section, "password"),
        "database": database_parser.get(database_section, "database"),
        "port": database_parser.getint(database_section, "port", fallback=3306),
    }
    database_url = sqlalchemy.engine.url.URL.create(
        **database
    )
    engine = create_async_engine(
        database_url,
        poolclass=NullPool,
    )
    # session = AsyncSession(engine)
    # stmt = select(BaekjoonUserInfo).where(BaekjoonUserInfo.baekjoon_id.in_(["test", "tt"]))
    #
    # result = await session.execute(stmt)

    sessionmaker = async_sessionmaker(engine)

    await run(sessionmaker)

    await engine.dispose()

    # async for user in result.scalars():
    #     print(user)

loop = asyncio.get_event_loop()
asyncio.run(main())
