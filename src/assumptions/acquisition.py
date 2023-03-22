class Acquisition:
    def __init__(
        self,
        acquisition_price,
        year_1_noi,
        going_in_cap_rate,
        closing_costs,
        other_acquisition_costs,
        all_in_acquisition_costs,
    ):
        self.acquisition_price = acquisition_price
        self.year_1_noi = year_1_noi
        self.going_in_cap_rate = going_in_cap_rate
        self.closing_costs = closing_costs
        self.other_acquisition_costs = other_acquisition_costs
        self.all_in_acquisition_costs = all_in_acquisition_costs

    def calculate_going_in_cap_rate(self):
        """Calculate the Going-in Cap Rate."""
        if self.year_1_noi == 0:
            return 0

        return self.acquisition_price / self.year_1_noi

    def calculate_total_acquisition_costs(self):
        """Calculate the total acquisition costs."""
        return (
            self.acquisition_price
            + self.closing_costs
            + self.other_acquisition_costs
        )

    def update_acquisition_details(
        self,
        acquisition_price=None,
        year_1_noi=None,
        going_in_cap_rate=None,
        closing_costs=None,
        other_acquisition_costs=None,
        all_in_acquisition_costs=None,
    ):
        """Update acquisition details."""
        if acquisition_price is not None:
            self.acquisition_price = acquisition_price
        if year_1_noi is not None:
            self.year_1_noi = year_1_noi
        if going_in_cap_rate is not None:
            self.going_in_cap_rate = going_in_cap_rate
        if closing_costs is not None:
            self.closing_costs = closing_costs
        if other_acquisition_costs is not None:
            self.other_acquisition_costs = other_acquisition_costs
        if all_in_acquisition_costs is not None:
            self.all_in_acquisition_costs = all_in_acquisition_costs
