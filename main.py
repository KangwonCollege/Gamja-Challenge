import os

import discord
from discord.ext import interaction
from sqlalchemy import NullPool
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncSession

from utils.getConfig import get_config

if __name__ == "__main__":
    directory = os.path.dirname(os.path.abspath(__file__))
    parser = get_config()

    bot = interaction.Client(
        intents=discord.Intents.default(),
        enable_debug_events=True,
        global_sync_command=False
    )

    # Database
    database_parser = get_config("database")
    database_section = database_parser.get("Default", "database_section")
    database = {
        "username": database_parser.get(database_section, "user"),
        "host": database_parser.get(database_section, "host"),
        "password": database_parser.get(database_section, "password"),
        "database": database_parser.get(database_section, "database"),
        "port": database_parser.getint(database_section, "port", fallback=3306),
    }
    engine = create_async_engine(
        "mysql+aiomysql://{username}:{password}@{host}:{port}/{database}".format(
            **database
        ),
        poolclass=NullPool,
    )
    factory = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

    bot.load_extensions("cogs", directory=directory, factory=factory)
    bot.run(parser.get("TOKEN", "discord_token"))
