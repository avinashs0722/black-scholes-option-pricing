import numpy as np
from scipy.stats import norm


def black_scholes_price(S, K, T, r, sigma, option_type="call"):
    """
    Calculates the Black-Scholes price for a European call or put option.

    S = current stock price
    K = strike price
    T = time to expiry in years
    r = risk-free rate
    sigma = annualised volatility
    option_type = "call" or "put"
    """

    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    if option_type == "call":
        price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)

    elif option_type == "put":
        price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)

    else:
        raise ValueError("option_type must be 'call' or 'put'")

    return price