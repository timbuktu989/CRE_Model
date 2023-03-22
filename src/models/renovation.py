class Renovation:
    def __init__(
        self,
        interior_renovation_start_month,
        interior_renovation_end_month,
        units_to_be_upgraded,
        upgraded_sf,
        units_upgraded_per_month,
        percent_units_upgraded_per_month,
        months_to_upgrade,
        upgrade_premium_per_month,
    ):
        self.interior_renovation_start_month = interior_renovation_start_month
        self.interior_renovation_end_month = interior_renovation_end_month
        self.units_to_be_upgraded = units_to_be_upgraded
        self.upgraded_sf = upgraded_sf
        self.units_upgraded_per_month = units_upgraded_per_month
        self.percent_units_upgraded_per_month = percent_units_upgraded_per_month
        self.months_to_upgrade = months_to_upgrade
        self.upgrade_premium_per_month = upgrade_premium_per_month

    def update_renovation_details(self, **kwargs):
        """Update renovation details."""
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
            else:
                raise AttributeError(f"{key} is not a valid attribute of Renovation class.")
