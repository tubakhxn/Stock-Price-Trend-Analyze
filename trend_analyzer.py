import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def fetch_stock_data(symbol, period="6mo"):
    data = yf.download(symbol, period=period)
    return data


def calculate_trend(data, short_window=20, long_window=50):
    data['MA_short'] = data['Close'].rolling(window=short_window).mean()
    data['MA_long'] = data['Close'].rolling(window=long_window).mean()
    # Calculate slope of long MA
    ma_long = data['MA_long'].dropna()
    x = np.arange(len(ma_long))
    slope = np.polyfit(x, ma_long.values, 1)[0]
    # Trend logic
    if slope > 0.05:
        trend = "Uptrend"
    elif slope < -0.05:
        trend = "Downtrend"
    else:
        trend = "Sideways"
    return trend, slope


def plot_trend(data, symbol, trend):
    plt.figure(figsize=(12, 6))
    plt.plot(data['Close'], label='Close Price', color='blue')
    plt.plot(data['MA_short'], label='Short MA (20)', color='orange')
    plt.plot(data['MA_long'], label='Long MA (50)', color='green')
    plt.title(f"{symbol} Price Trend: {trend}")
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def main():
    symbol = input("Enter stock symbol (e.g. AAPL): ").upper()
    data = fetch_stock_data(symbol)
    if data.empty:
        print("No data found for symbol.")
        return
    trend, slope = calculate_trend(data)
    print(f"Trend for {symbol}: {trend} (Slope: {slope:.4f})")
    plot_trend(data, symbol, trend)


if __name__ == "__main__":
    main()
