class LevelSystem:
    def __init__(self, experience):
        self.experience = experience

    def tier_calculate(self) -> tuple:
        tier = ""
        tier_lever = 0
        _tier_calculate = self.experience
        if _tier_calculate > 5:
            tier = "bronze"
            tier_lever = 3
        return tier, tier_lever

    def rank(self) -> int:

        return rank
