import discord
from discord.ext import interaction
from sqlalchemy.ext.asyncio import async_sessionmaker

from models import database


class BaseCog:
    def __init__(self, client: interaction.Client, factory: async_sessionmaker, used_repository: bool = True):
        self.client = client
        self.factory = factory
        # if used_repository:
        #     super().__init__(self.factory)

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

    @property
    def unrank_emoji(self) -> discord.PartialEmoji:
        return discord.PartialEmoji(name="rank_unlank", id=1130824286777655396, animated=False)

    @property
    def bronze3_emoji(self) -> discord.PartialEmoji:
        return discord.PartialEmoji(name="rank_bronze_3", id=1130824239524614225, animated=False)

    @property
    def bronze2_emoji(self) -> discord.PartialEmoji:
        return discord.PartialEmoji(name="rank_bronze_2", id=1130824241793740800, animated=False)

    @property
    def bronze1_emoji(self) -> discord.PartialEmoji:
        return discord.PartialEmoji(name="rank_bronze_1", id=1130824244918489138, animated=False)

    @property
    def silver3_emoji(self) -> discord.PartialEmoji:
        return discord.PartialEmoji(name="rank_silver_3", id=1130824274551251025, animated=False)

    @property
    def silver2_emoji(self) -> discord.PartialEmoji:
        return discord.PartialEmoji(name="rank_silver_2", id=1130824277227208775, animated=False)

    @property
    def silver1_emoji(self) -> discord.PartialEmoji:
        return discord.PartialEmoji(name="rank_silver_1", id=1130824283627733002, animated=False)

    @property
    def gold3_emoji(self) -> discord.PartialEmoji:
        return discord.PartialEmoji(name="rank_gold_3", id=1130824257115521104, animated=False)

    @property
    def gold2_emoji(self) -> discord.PartialEmoji:
        return discord.PartialEmoji(name="rank_gold_2", id=1130824258948436028, animated=False)

    @property
    def gold1_emoji(self) -> discord.PartialEmoji:
        return discord.PartialEmoji(name="rank_gold_1", id=1130824262513594408, animated=False)

    @property
    def platinum3_emoji(self) -> discord.PartialEmoji:
        return discord.PartialEmoji(name="rank_platinum_3", id=1130824265671909460, animated=False)

    @property
    def platinum2_emoji(self) -> discord.PartialEmoji:
        return discord.PartialEmoji(name="rank_platinum_2", id=1130824268029104138, animated=False)

    @property
    def platinum1_emoji(self) -> discord.PartialEmoji:
        return discord.PartialEmoji(name="rank_platinum_1", id=1130824271111929858, animated=False)

    @property
    def diamond3_emoji(self) -> discord.PartialEmoji:
        return discord.PartialEmoji(name="rank_diamond_3", id=1130824248940838992, animated=False)

    @property
    def diamond2_emoji(self) -> discord.PartialEmoji:
        return discord.PartialEmoji(name="rank_diamond_2", id=1130824252191416371, animated=False)

    @property
    def diamond1_emoji(self) -> discord.PartialEmoji:
        return discord.PartialEmoji(name="rank_diamond_1", id=1130824254116606022, animated=False)


def setup(client: interaction.Client, factory: async_sessionmaker):
    return
