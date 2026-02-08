# Stock Price Trend Analyzer

## What is Trend Analysis?
Trend analysis in stock markets involves identifying the general direction in which a stock's price is moving over a period. It helps investors understand whether a stock is rising (uptrend), falling (downtrend), or moving sideways (no clear direction).

## Logic Used to Detect Trends
This project uses moving averages and slope calculation:
- **Moving Averages (MA):** Two averages are calculated: a short-term (20 days) and a long-term (50 days).
- **Slope Logic:** The slope of the long-term moving average is computed. If the slope is positive and above a threshold, the stock is in an uptrend. If negative and below a threshold, it's a downtrend. Otherwise, it's sideways.

## How to Run the Project
1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
2. Run the analyzer:
   ```
   python trend_analyzer.py
   ```
3. Enter the stock symbol when prompted (e.g., AAPL).

## Sample Graph Explanation
The generated graph shows:
- **Blue line:** Stock closing price
- **Orange line:** Short-term moving average (20 days)
- **Green line:** Long-term moving average (50 days)
- **Title:** Displays detected trend (Uptrend, Downtrend, Sideways)

This visualization helps you see how the moving averages relate to the stock's price and the detected trend.
