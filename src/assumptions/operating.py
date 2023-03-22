class Operating:
    def __init__(
        self,
        operations_start,
        occupancy_start_percentage,
        occupancy_growth_duration,
        stabilization,
        revenues,
        expenses,
        capex_reserves,
    ):
        self.operations_start = operations_start
        self.occupancy_start_percentage = occupancy_start_percentage
        self.occupancy_growth_duration = occupancy_growth_duration
        self.stabilization = stabilization
        self.revenues = revenues
        self.expenses = expenses
        self.capex_reserves = capex_reserves

    def calculate_effective_gross_income(self):
        """Calculate the effective gross income."""
        return self.revenues * (1 - self.occupancy_start_percentage / 100)

    def calculate_net_operating_income(self):
        """Calculate the net operating income."""
        return self.calculate_effective_gross_income() - self.expenses

    def update_operating_details(self, **kwargs):
        """Update operating details."""
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
            else:
                raise AttributeError(f"{key} is not a valid attribute of Operating class.")
