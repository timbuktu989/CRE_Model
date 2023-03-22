import numpy as np
from models.property import Property
from models.acquisition import Acquisition
from models.debt import Debt
from models.exit import Exit
from models.operating import Operating
from models.renovation import Renovation
from utils.financial import calculate_ratios, calculate_waterfall_statement


def process_raw_data(raw_data):
    property_obj = Property(**raw_data["property"])
    acquisition_obj = Acquisition(**raw_data["acquisition"])
    debt_obj = Debt(**raw_data["debt"])
    exit_obj = Exit(**raw_data["exit"])
    operating_obj = Operating(**raw_data["operating"])
    renovation_obj = Renovation(**raw_data["renovation"])

    return property_obj, acquisition_obj, debt_obj, exit_obj, operating_obj, renovation_obj


def generate_monthly_cash_flow(property_obj, acquisition_obj, debt_obj, exit_obj, operating_obj, renovation_obj):
    # Implement the logic to calculate the 120-month cash flow based on the input objects
    monthly_cash_flow = np.zeros(120)  # Replace with actual calculation
    return monthly_cash_flow


def generate_yearly_cash_flow(monthly_cash_flow):
    # Calculate the yearly cash flow from the monthly cash flow
    yearly_cash_flow = np.sum(monthly_cash_flow.reshape(-1, 12), axis=1)
    return yearly_cash_flow


def generate_outputs(raw_input_data):
    property_obj, acquisition_obj, debt_obj, exit_obj, operating_obj, renovation_obj = process_raw_data(raw_input_data)

    monthly_cash_flow = generate_monthly_cash_flow(property_obj, acquisition_obj, debt_obj, exit_obj, operating_obj, renovation_obj)
    yearly_cash_flow = generate_yearly_cash_flow(monthly_cash_flow)
    waterfall_statement = calculate_waterfall_statement(yearly_cash_flow)
    ratios = calculate_ratios(property_obj, acquisition_obj, debt_obj, exit_obj, operating_obj, renovation_obj)

    outputs = {
        "monthly_cash_flow": monthly_cash_flow,
        "yearly_cash_flow": yearly_cash_flow,
        "waterfall_statement": waterfall_statement,
        "ratios": ratios,
    }

    return outputs


if __name__ == "__main__":
    # You can replace the 'raw_input_data' variable with actual data from your SQL database or another source.
    raw_input_data = {}  # Example: {"property": {...}, "operating": {...}, "debt": {...}, "exit": {...}, "renovation": {...}}
    outputs = generate_outputs(raw_input_data)

    # Print or store the outputs as needed.
    print(outputs)
