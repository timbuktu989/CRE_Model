class Property:
    def __init__(
        self,
        project_name,
        building_address,
        building_city,
        building_state,
        building_zip_code,
        building_region,
        building_sub_region,
        building_class_at_purchase,
        building_class_post_renovation,
        land_area,
        year_built,
        renovation_date,
        general_partner,
        limited_partner,
        gross_square_footage,
        net_square_footage,
        number_of_units,
        all_in_acquisition_costs,
        parking_stalls,
        parking_ratio,
        analysis_start_date,
        building_purchase_month,
        exterior_renovation_start,
        interior_renovation_finish_month,
        month_interior_renovation_completed,
        acquisition_date,
        working_capital_release_month,
        rent_inflation_timing,
        other_income_inflation_timing,
        expense_inflation_timing,
    ):
        self.project_name = project_name
        self.building_address = building_address
        self.building_city = building_city
        self.building_state = building_state
        self.building_zip_code = building_zip_code
        self.building_region = building_region
        self.building_sub_region = building_sub_region
        self.building_class_at_purchase = building_class_at_purchase
        self.building_class_post_renovation = building_class_post_renovation
        self.land_area = land_area
        self.year_built = year_built
        self.renovation_date = renovation_date
        self.general_partner = general_partner
        self.limited_partner = limited_partner
        self.gross_square_footage = gross_square_footage
        self.net_square_footage = net_square_footage
        self.number_of_units = number_of_units
        self.all_in_acquisition_costs = all_in_acquisition_costs
        self.parking_stalls = parking_stalls
        self.parking_ratio = parking_ratio
        self.analysis_start_date = analysis_start_date
        self.building_purchase_month = building_purchase_month
        self.exterior_renovation_start = exterior_renovation_start
        self.interior_renovation_finish_month = interior_renovation_finish_month
        self.month_interior_renovation_completed = month_interior_renovation_completed
        self.acquisition_date = acquisition_date
        self.working_capital_release_month = working_capital_release_month
        self.rent_inflation_timing = rent_inflation_timing
        self.other_income_inflation_timing = other_income_inflation_timing
        self.expense_inflation_timing = expense_inflation_timing

    def update_property_details(self, **kwargs):
        """Update property details."""
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
            else:
                raise AttributeError(f"{key} is not a valid attribute of Property class.")
