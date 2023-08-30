class LevelSystem:
    def __init__(self, experience, git_contrib):
        self.CONTRIBUTION_WEIGHT = 1

        self.TIER_POINT = {
            "UNRANK": 0,
            "BRONZE_3": 10,
            "BRONZE_2": 20,
            "BRONZE_1": 30,
            "SILVER_3": 50,
            "SILVER_2": 65,
            "SILVER_1": 80,
            "GOLD_3": 100,
            "GOLD_2": 120,
            "GOLD_1": 150,
            "PLATINUM_3": 200,
            "PLATINUM_2": 250,
            "PLATINUM_1": 300,
            "DIAMOND_3": 350,
            "DIAMOND_2": 400,
            "DIAMOND_1": 500
        }

        self.TIER_WEIGHT = {
            "UNRANK": 1,
            "BRONZE": 3,
            "SILVER": 5,
            "GOLD": 8,
            "PLATINUM": 15,
            "DIAMOND": 20,
            "RUBY": 40,
            "MASTER": 80
        }
        self.user_experience = experience

    def conv_tier_name(self, tier: str = None) -> str:
        for tier_name, tier_weight in self.TIER_WEIGHT:
            if tier_name == tier:
                return tier_weight
        return self.user_experience

    def conv_tier_exp(self, user_exp: int = 0) -> str:
        for exp, name in enumerate(self.TIER_POINT):
            if exp >= user_exp:
                return name
        return self.user_experience

    def tier_calculation(self) -> int:

        return 10

    def batch_rank(self) -> int:
        return 10


