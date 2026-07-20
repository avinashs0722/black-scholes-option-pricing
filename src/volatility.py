import numpy as np


def calculate_historical_volatility(prices, window=30):
    """
    Calculates annualised historical volatility from daily stock prices.

    prices = Series of stock prices
    window = rolling window in trading days
    """

    daily_returns = prices.pct_change()

    rolling_volatility = daily_returns.rolling(window).std() * np.sqrt(252)

    return rolling_volatility