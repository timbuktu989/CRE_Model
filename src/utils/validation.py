from models.acquisition import Acquisition
from models.debt import Debt
from models.equity import Equity
from models.exit import Exit
from models.operating import Operating
from models.property import Property
from models.renovation import Renovation

# Validate the data from property assumptions
def validate_property_data(data):
    try:
        required_fields = [
            'project_name', 'building_address', 'building_city', 'building_state',
            'building_zip_code', 'building_region', 'building_sub_region',
            'building_class_at_purchase', 'building_class_post_renovation',
            'land_area', 'year_built', 'renovation_date', 'general_partner',
            'limited_partner', 'gross_square_footage', 'net_square_footage',
            'number_of_units', 'all_in_acquisition_costs', 'parking_stalls',
            'parking_ratio', 'analysis_start_date', 'building_purchase_month',
            'exterior_renovation_start', 'interior_renovation_finish_month',
            'month_interior_renovation_completed', 'acquisition_date',
            'working_capital_release_month', 'rent_inflation_timing',
            'other_income_inflation_timing', 'expense_inflation_timing',
        ]

        for field in required_fields:
            if field not in data:
                raise ValueError(f"Missing required field: {field}")

        property_instance = Property(**data)
        return property_instance

    except Exception as e:
        print(f"Error validating Property data: {e}")
        return None

def main():
    property_data = {
        # Fill in the required data for the Property class
    }

    validated_property = validate_property_data(property_data)
    if validated_property:
        print("Property data validated and processed.")
    else:
        print("Property data validation failed.")

if __name__ == "__main__":
    main()

# Validate the data from equity assumptions

def validate_equity_data(data):
    try:
        required_fields = [
            "gp_contrib",
            "lp_contribs"
        ]

        for field in required_fields:
            if field not in data:
                raise ValueError(f"Missing required field: {field}")

        equity_instance = Equity(**data)
        return equity_instance

    except Exception as e:
        print(f"Error validating Equity data: {e}")
        return None

# Validate the data from acquisition assumptions

def validate_acquisition_data(data):
    try:
        required_fields = [
            "acquisition_price",
            "year_1_noi",
            "going_in_cap_rate",
            "closing_costs",
            "other_acquisition_costs",
            "all_in_acquisition_costs"
        ]

        for field in required_fields:
            if field not in data:
                raise ValueError(f"Missing required field: {field}")

        acquisition_instance = Acquisition(**data)
        return acquisition_instance

    except Exception as e:
        print(f"Error validating Acquisition data: {e}")
        return None

# Validate the data from the debt assumptions

def validate_debt_data(data):
    try:
        required_fields = [
            "loan_to_cost",
            "loan_amount_acquisition",
            "loan_amount_renovation",
            "max_loan_amount",
            "percent_of_renovations_financed",
            "amortization_period",
            "io_period",
            "acquisition_loan_start_month",
            "acquisition_loan_payoff_month",
            "fixed_interest_rate",
            "interest_calculation",
            "fixed_rate_spread_over_SOFR",
            "SOFR_cap",
            "SOFR_floor",
            "financing_fee",
            "exit_fee"
        ]

        for field in required_fields:
            if field not in data:
                raise ValueError(f"Missing required field: {field}")

        debt_instance = Debt(**data)
        return debt_instance

    except Exception as e:
        print(f"Error validating Debt data: {e}")
        return None

# Validate the data from exit assumptions

def validate_exit_data(data):
    try:
        required_fields = [
            "sale_month",
            "sale_date",
            "exit_cap_rate",
            "noi_at_exit",
            "gross_sale_dollars",
            "gross_sale_dollars_per_sf",
            "gross_sale_dollars_per_unit",
            "transactions_costs",
            "months_held_after_renovation_complete",
        ]

        for field in required_fields:
            if field not in data:
                raise ValueError(f"Missing required field: {field}")

        exit_instance = Exit(**data)
        return exit_instance

    except Exception as e:
        print(f"Error validating Exit data: {e}")
        return None

# Validate the data from operating assumptions

def validate_operating_data(data):
    try:
        required_fields = [
            "operations_start",
            "occupancy_start_percentage",
            "occupancy_growth_duration",
            "stabilization",
            "revenues",
            "expenses",
            "capex_reserves",
        ]

        for field in required_fields:
            if field not in data:
                raise ValueError(f"Missing required field: {field}")

        operating_instance = Operating(**data)
        return operating_instance

    except Exception as e:
        print(f"Error validating Operating data: {e}")
        return None

# Validate the data from renovation assumptions

def validate_renovation_data(data):
    try:
        required_fields = [
            "renovation_start_month",
            "renovation_duration",
            "total_renovation_cost",
            "total_renovation_cost_per_unit",
            "total_renovation_cost_per_sf",
            "soft_costs",
            "hard_costs",
        ]

        for field in required_fields:
            if field not in data:
                raise ValueError(f"Missing required field: {field}")

        renovation_instance = Renovation(**data)
        return renovation_instance

    except Exception as e:
        print(f"Error validating Renovation data: {e}")
        return None