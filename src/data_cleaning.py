
import pandas as pd
import numpy as np
import os

# ==========================================
# 1. LOAD RAW DATA
# ==========================================

INPUT_FILE = "data/raw/tata_motors_2000_2025.csv"
OUTPUT_FILE = "data/processed/tata_motors_cleaned.csv"

print("=" * 50)
print("TATA MOTORS DATA CLEANING")
print("=" * 50)

df = pd.read_csv(
    INPUT_FILE,
    index_col=0,
    parse_dates=True
)

print("\nOriginal Dataset Shape:", df.shape)


# ==========================================
# 2. STANDARDIZE COLUMN NAMES
# ==========================================

df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

print("\nColumns:", df.columns.tolist())


# ==========================================
# 3. CHECK MISSING VALUES
# ==========================================

print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

# Remove rows without essential price information
required_columns = [
    "open", "high", "low", "close", "adj_close"
]

df = df.dropna(subset=required_columns)


# ==========================================
# 4. REMOVE DUPLICATES
# ==========================================

duplicate_count = df.index.duplicated().sum()

print("\nDuplicate Dates:", duplicate_count)

df = df[~df.index.duplicated(keep="first")]


# ==========================================
# 5. SORT DATA BY DATE
# ==========================================

df = df.sort_index()


# ==========================================
# 6. CHECK INVALID VALUES
# ==========================================

price_columns = [
    "open", "high", "low", "close", "adj_close"
]

# Check non-positive prices
invalid_prices = (df[price_columns] <= 0).any(axis=1)

# Check invalid OHLC combinations
invalid_ohlc = (
    (df["high"] < df["low"]) |
    (df["high"] < df["open"]) |
    (df["high"] < df["close"]) |
    (df["low"] > df["open"]) |
    (df["low"] > df["close"])
)

# Check invalid volume
invalid_volume = df["volume"] < 0

invalid_records = (
    invalid_prices |
    invalid_ohlc |
    invalid_volume
)

print("\nInvalid Records:", invalid_records.sum())

df = df[~invalid_records].copy()


# ==========================================
# 7. FEATURE ENGINEERING
# ==========================================

# Daily percentage return
df["daily_return"] = (
    df["adj_close"].pct_change() * 100
)

# Daily price change
df["price_change"] = df["adj_close"].diff()

# Moving averages
df["50_day_ma"] = (
    df["adj_close"].rolling(window=50).mean()
)

df["200_day_ma"] = (
    df["adj_close"].rolling(window=200).mean()
)

# Daily return volatility (30 trading days)
df["30_day_volatility"] = (
    df["daily_return"]
    .rolling(window=30)
    .std()
)

# Annualized volatility
df["annualized_volatility"] = (
    df["30_day_volatility"] * np.sqrt(252)
)

# Date-based features
df["year"] = df.index.year
df["month"] = df.index.month
df["day"] = df.index.day
df["day_name"] = df.index.day_name()


# ==========================================
# 8. FINAL DATASET INFORMATION
# ==========================================

print("\nFinal Dataset Shape:", df.shape)

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

print("\nFinal Dataset Preview:")
print(df.head())

print("\nStatistical Summary:")
print(df.describe())


# ==========================================
# 9. SAVE CLEANED DATASET
# ==========================================

os.makedirs("data/processed", exist_ok=True)

df.to_csv(OUTPUT_FILE)

print("\n" + "=" * 50)
print("DATA CLEANING COMPLETED SUCCESSFULLY!")
print("=" * 50)

print("Saved File:", OUTPUT_FILE)
print("Total Records:", len(df))
