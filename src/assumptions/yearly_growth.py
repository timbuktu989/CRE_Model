class YearlyGrowth:
    def __init__(self, year, growth_type, amount):
        self.year = year
        self.growth_type = growth_type
        self.amount = amount

    def __str__(self):
        return f"{self.year} - {self.growth_type}: {self.amount}"
