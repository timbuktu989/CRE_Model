class EquityTier:
    def __init__(self, hurdle_rate, gp_share, lp_shares):
        self.hurdle_rate = hurdle_rate
        self.gp_share = gp_share
        self.lp_shares = lp_shares


class Equity:
    def __init__(self, gp_contrib, lp_contribs):
        self.gp_contrib = gp_contrib
        self.lp_contribs = lp_contribs
        self.total_contrib = gp_contrib + sum(lp_contribs)
        self.waterfall = []

    def add_tier(self, hurdle_rate, gp_share, lp_shares):
        assert len(lp_shares) == len(self.lp_contribs), "Number of LP shares must match the number of LPs"
        tier = EquityTier(hurdle_rate, gp_share, lp_shares)
        self.waterfall.append(tier)

    def calculate_distribution(self, irr):
        gp_cash_flow = 0
        lp_cash_flows = [0] * len(self.lp_contribs)
        remaining_cash_flow = irr * self.total_contrib

        for tier in self.waterfall:
            tier_cash_flow = min(remaining_cash_flow, tier.hurdle_rate * self.total_contrib)
            gp_portion = tier_cash_flow * tier.gp_share
            lp_portions = [tier_cash_flow * lp_share for lp_share in tier.lp_shares]

            gp_cash_flow += gp_portion
            lp_cash_flows = [lp_cash_flow + lp_portion for lp_cash_flow, lp_portion in zip(lp_cash_flows, lp_portions)]

            remaining_cash_flow -= tier_cash_flow

            if remaining_cash_flow <= 0:
                break

        return gp_cash_flow, lp_cash_flows
