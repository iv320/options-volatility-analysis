import yfinance as yf
import pandas as pd

def fetch_options_data(ticker):
    stock = yf.Ticker(ticker)
    expiry = stock.options[0]  # nearest expiry
    calls = stock.option_chain(expiry).calls
    puts = stock.option_chain(expiry).puts
    return calls, puts

def calculate_put_call_ratio(calls, puts):
    total_calls_oi = calls["openInterest"].sum()
    total_puts_oi = puts["openInterest"].sum()
    pcr = total_puts_oi / total_calls_oi
    return pcr

if __name__ == "__main__":
    ticker = "AAPL"
    calls, puts = fetch_options_data(ticker)
    pcr = calculate_put_call_ratio(calls, puts)

    print(f"Put-Call Ratio for {ticker}: {pcr:.2f}")

    if pcr > 1:
        print("Market sentiment: Bearish")
    else:
        print("Market sentiment: Bullish")
