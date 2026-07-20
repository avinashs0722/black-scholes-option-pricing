import yfinance as yf
import pandas as pd


def get_stock_prices(ticker, start_date="2023-01-01"):
    data = yf.download(ticker, start=start_date, progress=False)

    close_prices = data["Close"]

    if isinstance(close_prices, pd.DataFrame):
        close_prices = close_prices.iloc[:, 0]

    return close_prices


def get_option_chain(ticker, min_days_to_expiry=30):
    from datetime import datetime

    stock = yf.Ticker(ticker)

    expiries = stock.options
    today = datetime.today().date()

    valid_expiries = []

    for expiry in expiries:
        expiry_date = datetime.strptime(expiry, "%Y-%m-%d").date()
        days_to_expiry = (expiry_date - today).days

        if days_to_expiry >= min_days_to_expiry:
            valid_expiries.append(expiry)

    expiry = valid_expiries[0]

    option_chain = stock.option_chain(expiry)

    calls = option_chain.calls
    puts = option_chain.puts

    return expiry, calls, puts