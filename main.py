import os

import discord
from discord.ext import interaction

from utils.getConfig import get_config

if __name__ == "__main__":
    directory = os.path.dirname(os.path.abspath(__file__))
    
    if False:
        pass
    else:
        bot = interaction.Client(
            intents = discord.Intents.default(),
            enable_debug_events=True,
            global_sync_command=True
        )
        
    bot.load_extensions("cogs", directory=directory)
    bot.run(get_config()["TOKEN"]["discord_token"])
    