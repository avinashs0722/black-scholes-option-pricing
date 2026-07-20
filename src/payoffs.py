import numpy as np


def call_payoff(stock_prices, strike):
    return np.maximum(stock_prices - strike, 0)


def put_payoff(stock_prices, strike):
    return np.maximum(strike - stock_prices, 0)