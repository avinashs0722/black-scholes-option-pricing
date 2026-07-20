import pandas as pd
from scipy.optimize import brentq

from src.black_scholes import black_scholes_price


def calculate_implied_volatility(market_price, S, K, T, r, option_type="call"):
    """
    Solves for implied volatility by finding the volatility
    that makes Black-Scholes price equal to the market price.
    """

    def objective(sigma):
        return black_scholes_price(S, K, T, r, sigma, option_type) - market_price

    try:
        implied_vol = brentq(objective, 0.001, 5.0)
        return implied_vol
    except ValueError:
        return None


def compare_market_to_model(calls, S, T, r, sigma):
    results = []

    for _, row in calls.iterrows():
        strike = row["strike"]
        market_price = (row["bid"] + row["ask"]) / 2

        if market_price <= 0:
            continue

        model_price = black_scholes_price(
            S=S,
            K=strike,
            T=T,
            r=r,
            sigma=sigma,
            option_type="call"
        )

        difference = market_price - model_price

        model_implied_volatility = calculate_implied_volatility(
            market_price=market_price,
            S=S,
            K=strike,
            T=T,
            r=r,
            option_type="call"
        )

        if model_implied_volatility is None:
            continue

        results.append({
            "Strike": strike,
            "Market Price": market_price,
            "Model Price": model_price,
            "Difference": difference,
            "Model Implied Volatility": model_implied_volatility
        })

    return pd.DataFrame(results)