class Exit:
    def __init__(
        self,
        sale_month,
        sale_date,
        exit_cap_rate,
        noi_at_exit,
        gross_sale_dollars,
        gross_sale_dollars_per_sf,
        gross_sale_dollars_per_unit,
        transactions_costs,
        months_held_after_renovation_complete,
    ):
        self.sale_month = sale_month
        self.sale_date = sale_date
        self.exit_cap_rate = exit_cap_rate
        self.noi_at_exit = noi_at_exit
        self.gross_sale_dollars = gross_sale_dollars
        self.gross_sale_dollars_per_sf = gross_sale_dollars_per_sf
        self.gross_sale_dollars_per_unit = gross_sale_dollars_per_unit
        self.transactions_costs = transactions_costs
        self.months_held_after_renovation_complete = months_held_after_renovation_complete

    def calculate_sale_price(self):
        """Calculate the sale price based on the NOI at exit and exit cap rate."""
        return self.noi_at_exit / self.exit_cap_rate

    def calculate_net_sale_proceeds(self):
        """Calculate the net sale proceeds after accounting for transactions costs."""
        return self.gross_sale_dollars - self.transactions_costs

    def update_exit_details(self, **kwargs):
        """Update exit details."""
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
            else:
                raise AttributeError(f"{key} is not a valid attribute of Exit class.")
