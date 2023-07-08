import os

import discord
from discord.ext import interaction

from utils.getConfig import get_config

if __name__ == "__main__":
    directory = os.path.dirname(os.path.abspath(__file__))
    parser = get_config()

    bot = interaction.Client(
        intents=discord.Intents.default(),
        enable_debug_events=True,
        global_sync_command=False
    )

    bot.load_extensions("cogs", directory=directory)
    bot.run(parser.get("TOKEN", "discord_token"))
