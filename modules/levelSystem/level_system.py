from typing import Dict


class LevelSystem:
    def __init__(self, experience, git_contrib):
        self.CONTRIBUTION_WEIGHT = 1

        self.TIER_LIST_DISCORD = ["UNRANK", "BRONZE", "SILVER", "GOLD", "PLATINUM", "DIAMOND"]

        self.TIER_POINT_DISCORD: Dict[str, int] = {
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

        self.TIER_WEIGHT_SOLVED = {
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

    def return_tier(self, step: int = 1, tier: int = 0) -> str:
        return str(self.TIER_LIST_DISCORD[tier]) + "_" + str(step)

    def conv_tier_exp(self, tier: str = None) -> int:
        try:
            for tier_name, tier_point in self.TIER_POINT_DISCORD:
                if tier_name == tier:
                    return tier_point
        except Exception as e:
            print(e)

    def conv_exp_tier(self, user_exp: int = 0) -> str:
        try:
            for name, exp in self.TIER_POINT_DISCORD:
                if exp >= user_exp:
                    return name
        except Exception as e:
            print(e)

    def tier_calculation(self) -> int:

        return 10

    def batch_rank(
            self,
            solved_tier: str = "UNRANK",
            git_contribution: int = None,
            return_type: bool = False
    ) -> int or str:
        git_contribution = git_contribution - git_contribution * (git_contribution * (1/100))
        solved_tier_exp = self.conv_tier_exp(tier=solved_tier) *

        batch_tier_exp = None

        if git_contribution > solved_tier_exp:
            batch_tier_exp = git_contribution
        else:
            batch_tier_exp = solved_tier_exp
        if return_type:
            return batch_tier_exp
        else:
            return self.conv_exp_tier(batch_tier_exp)


