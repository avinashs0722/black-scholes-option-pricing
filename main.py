import matplotlib.pyplot as plt

from src.black_scholes import black_scholes_price
from src.monte_carlo import monte_carlo_option_price

S = 100
K = 100
T = 1
r = 0.05
sigma = 0.20

black_scholes_call = black_scholes_price(
    S, K, T, r, sigma, option_type="call"
)

simulation_counts = [100, 500, 1000, 5000, 10000, 50000, 100000]

monte_carlo_prices = []
percentage_errors = []

for simulations in simulation_counts:
    mc_price = monte_carlo_option_price(
        S, K, T, r, sigma, simulations=simulations
    )

    error = abs(mc_price - black_scholes_call) / black_scholes_call

    monte_carlo_prices.append(mc_price)
    percentage_errors.append(error)

    print(
        f"Simulations: {simulations:>6} | "
        f"MC Price: {mc_price:.4f} | "
        f"Error: {error:.2%}"
    )

plt.figure(figsize=(10, 5))
plt.plot(simulation_counts, percentage_errors, marker="o")
plt.xscale("log")
plt.title("Monte Carlo Convergence to Black-Scholes Price")
plt.xlabel("Number of Simulations")
plt.ylabel("Percentage Error")
plt.grid(True)
plt.savefig("charts/monte_carlo_convergence.png")
plt.show()