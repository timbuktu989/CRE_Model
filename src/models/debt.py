class Debt:
    def __init__(
            self,
            loan_to_cost,
            loan_amount_acquisition,
            loan_amount_renovation,
            max_loan_amount,
            percent_of_renovations_financed,
            amortization_period,
            io_period,
            acquisition_loan_start_month,
            acquisition_loan_payoff_month,
            fixed_interest_rate,
            interest_calculation,
            fixed_rate_spread_over_SOFR,
            SOFR_cap,
            SOFR_floor,
            financing_fee,
            exit_fee,
    ):
        self.loan_to_cost = loan_to_cost
        self.loan_amount_acquisition = loan_amount_acquisition
        self.loan_amount_renovation = loan_amount_renovation
        self.max_loan_amount = max_loan_amount
        self.percent_of_renovations_financed = percent_of_renovations_financed
        self.amortization_period = amortization_period
        self.io_period = io_period
        self.acquisition_loan_start_month = acquisition_loan_start_month
        self.acquisition_loan_payoff_month = acquisition_loan_payoff_month
        self.fixed_interest_rate = fixed_interest_rate
        self.interest_calculation = interest_calculation
        self.fixed_rate_spread_over_SOFR = fixed_rate_spread_over_SOFR
        self.SOFR_cap = SOFR_cap
        self.SOFR_floor = SOFR_floor
        self.financing_fee = financing_fee
        self.exit_fee = exit_fee

    def calculate_monthly_interest_payment(self, outstanding_balance, interest_rate):
        """Calculate the monthly interest payment."""
        return outstanding_balance * (interest_rate / 12)

    def calculate_monthly_amortization_payment(self, principal_amount, interest_rate, amortization_period_months):
        """Calculate the monthly amortization payment."""
        if interest_rate == 0:
            return principal_amount / amortization_period_months

        monthly_rate = interest_rate / 12
        return principal_amount * (monthly_rate * (1 + monthly_rate) ** amortization_period_months) / (
                    (1 + monthly_rate) ** amortization_period_months - 1)

    def update_debt_details(self, **kwargs):
        """Update debt details."""
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
            else:
                raise AttributeError(f"{key} is not a valid attribute of Debt class.")
