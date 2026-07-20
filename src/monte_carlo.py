import numpy as np


def monte_carlo_option_price(
    S,
    K,
    T,
    r,
    sigma,
    simulations=100000
):
    """
    Monte Carlo pricing of a European call option.
    """

    Z = np.random.standard_normal(simulations)

    ST = S * np.exp(
        (r - 0.5 * sigma ** 2) * T
        + sigma * np.sqrt(T) * Z
    )

    payoffs = np.maximum(ST - K, 0)

    option_price = np.exp(-r * T) * np.mean(payoffs)

    return option_price