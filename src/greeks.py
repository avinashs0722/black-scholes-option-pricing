import numpy as np
from scipy.stats import norm


def calculate_greeks(S, K, T, r, sigma):

    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    delta_call = norm.cdf(d1)
    delta_put = norm.cdf(d1) - 1

    gamma = norm.pdf(d1) / (S * sigma * np.sqrt(T))

    vega = S * norm.pdf(d1) * np.sqrt(T) / 100

    theta_call = (
        -(S * norm.pdf(d1) * sigma) / (2 * np.sqrt(T))
        - r * K * np.exp(-r * T) * norm.cdf(d2)
    ) / 365

    theta_put = (
        -(S * norm.pdf(d1) * sigma) / (2 * np.sqrt(T))
        + r * K * np.exp(-r * T) * norm.cdf(-d2)
    ) / 365

    rho_call = K * T * np.exp(-r * T) * norm.cdf(d2) / 100

    rho_put = -K * T * np.exp(-r * T) * norm.cdf(-d2) / 100

    return {
        "Call Delta": delta_call,
        "Put Delta": delta_put,
        "Gamma": gamma,
        "Vega": vega,
        "Call Theta": theta_call,
        "Put Theta": theta_put,
        "Call Rho": rho_call,
        "Put Rho": rho_put
    }