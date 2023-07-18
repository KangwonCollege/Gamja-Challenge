import discord
from discord.ext import interaction
from sqlalchemy.ext.asyncio import async_sessionmaker

from models import database


class BaseCog:
    def __init__(self, client: interaction.Client, factory: async_sessionmaker):
        self.client = client
        self.factory = factory
        super().__init__(self.factory)

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
