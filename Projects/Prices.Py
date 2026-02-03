import yfinance as yf
import pandas as pd
import os

# 1) Ticker and exact date range from your URL
ticker = "ROADSTAR.BO"
start_date = "2025-09-01"
end_date = "2026-01-09"

# 2) Download data from Yahoo
df = yf.download(
    ticker,
    start=start_date,
    end=end_date,
    progress=False
)

# 3) Output folder path (as you requested)
output_folder = r"C:\Users\LENOVO\Downloads\Dowloading"

# Make sure folder exists (create if not)
os.makedirs(output_folder, exist_ok=True)

# 4) Save CSV
output_file = os.path.join(output_folder, f"{ticker}_history.csv")

if df.empty:
    print("No data available for this date range.")
else:
    df.to_csv(output_file)
    print("CSV file downloaded successfully:")
    print(output_file)
