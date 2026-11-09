
import yfinance as yf
import pandas as pd
import os

# Project configuration
TICKER = "TMPV.NS"

START_DATE = "2000-01-01"
END_DATE = "2026-01-01"

OUTPUT_FILE = "data/raw/tata_motors_2000_2025.csv"

# Create output directory
os.makedirs("data/raw", exist_ok=True)

print("=" * 50)
print("TATA MOTORS STOCK DATA COLLECTION")
print("=" * 50)

print(f"\nStock ticker: {TICKER}")
print(f"Start date: {START_DATE}")
print(f"End date: {END_DATE}")

# Download historical stock data
stock = yf.download(
    TICKER,
    start=START_DATE,
    end=END_DATE,
    auto_adjust=False,
    progress=True,
    threads=False
)

# Validate downloaded data
if stock.empty:
    print("\nNo data downloaded.")
    print("Please check your internet connection and ticker.")
    raise SystemExit(1)

# Handle MultiIndex columns
if isinstance(stock.columns, pd.MultiIndex):
    stock.columns = stock.columns.get_level_values(0)

# Clean column names
stock.columns = [
    str(col).lower().replace(" ", "_")
    for col in stock.columns
]

# Sort data by date
stock = stock.sort_index()

# Remove duplicate dates
stock = stock[~stock.index.duplicated(keep="first")]

# Save dataset
stock.to_csv(OUTPUT_FILE)

print("\n" + "=" * 50)
print("DATA DOWNLOAD SUCCESSFUL!")
print("=" * 50)

print("\nDataset shape:", stock.shape)

print("\nAvailable columns:")
print(stock.columns.tolist())

print("\nFirst available date:")
print(stock.index.min())

print("\nLast available date:")
print(stock.index.max())

print("\nFirst 5 records:")
print(stock.head())

print("\nDataset information:")
stock.info()

print(f"\nFile saved successfully: {OUTPUT_FILE}")
