from assumptions.acquisition import Acquisition
from assumptions.debt import Debt
from assumptions.equity import Equity
from assumptions.exit import Exit
from assumptions.operating import Operating
from assumptions.property import Property
from assumptions.renovation import Renovation

from utils.validation import (
    validate_acquisition_data,
    validate_debt_data,
    validate_equity_data,
    validate_exit_data,
    validate_operating_data,
    validate_property_data,
    validate_renovation_data,
)


def main():
    # Load data from the files or API (not provided in this example)
    acquisition_data = {...}
    debt_data = {...}
    equity_data = {...}
    exit_data = {...}
    operating_data = {...}
    property_data = {...}
    renovation_data = {...}

    # Validate data
    valid_acquisition_data = validate_acquisition_data(acquisition_data)
    valid_debt_data = validate_debt_data(debt_data)
    valid_equity_data = validate_equity_data(equity_data)
    valid_exit_data = validate_exit_data(exit_data)
    valid_operating_data = validate_operating_data(operating_data)
    valid_property_data = validate_property_data(property_data)
    valid_renovation_data = validate_renovation_data(renovation_data)

    # Create objects using the validated data
    acquisition = Acquisition(**valid_acquisition_data)
    debt = Debt(**valid_debt_data)
    equity = Equity(**valid_equity_data)
    exit_obj = Exit(**valid_exit_data)
    operating = Operating(**valid_operating_data)
    property_obj = Property(**valid_property_data)
    renovation = Renovation(**valid_renovation_data)

    # Perform desired operations with the objects (not provided in this example)


if __name__ == "__main__":
    main()


