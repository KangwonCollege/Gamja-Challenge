from enum import Enum


class BronzeTier(Enum):
    un_rank = "UNRANKED"
    bronze_3 = "BRONZE_3"
    bronze_2 = "BRONZE_2",
    bronze_1 = "BRONZE_1",


class SilverTier(Enum):
    silver_3 = "SILVER_3"
    silver_2 = "SILVER_2"
    silver_1 = "SILVER_1"


class GoldTier(Enum):
    gold_3 = "GOLD_3"
    gold_2 = "GOLD_2"
    gold_1 = "GOLD_1"


class PlatinumTier(Enum):
    platinum_3 = "PLATINUM_3"
    platinum_2 = "PLATINUM_2"
    platinum_1 = "PLATINUM_1"


class DiamondTier(Enum):
    diamond_3 = "DIAMOND_3"
    diamond_2 = "DIAMOND_2"
    diamond_1 = "DIAMOND_1"


class Tier(Enum):
    bronze = BronzeTier
