
import pandas as pd
import numpy as np
import os

# ==========================================
# 1. LOAD DATA
# ==========================================

df = pd.read_csv(
    "data/processed/tata_motors_cleaned.csv",
    index_col=0,
    parse_dates=True
)

os.makedirs("outputs", exist_ok=True)

print("=" * 60)
print("TATA MOTORS - FINAL ANALYTICAL REPORT")
print("=" * 60)


# ==========================================
# 2. OVERALL STOCK PERFORMANCE
# ==========================================

first_price = df["adj_close"].iloc[0]
last_price = df["adj_close"].iloc[-1]

price_change = last_price - first_price

price_return = (
    (last_price / first_price) - 1
) * 100

print("\n1. OVERALL PERFORMANCE")

print(f"First adjusted price: Rs. {first_price:.2f}")
print(f"Last adjusted price: Rs. {last_price:.2f}")
print(f"Price change: Rs. {price_change:.2f}")
print(f"Adjusted price return: {price_return:.2f}%")


# ==========================================
# 3. ANNUAL PERFORMANCE
# ==========================================

year_end_prices = df["adj_close"].resample("YE").last()

annual_returns = year_end_prices.pct_change() * 100

annual_returns.index = annual_returns.index.year

best_year = annual_returns.idxmax()
worst_year = annual_returns.idxmin()

print("\n2. ANNUAL PERFORMANCE")

print("Best performing year:", best_year)
print(f"Return: {annual_returns.max():.2f}%")

print("Worst performing year:", worst_year)
print(f"Return: {annual_returns.min():.2f}%")


# ==========================================
# 4. DAILY RETURNS
# ==========================================

daily_returns = df["adj_close"].pct_change() * 100

print("\n3. DAILY RETURNS")

print(f"Average daily return: {daily_returns.mean():.4f}%")
print(f"Best daily return: {daily_returns.max():.2f}%")
print(f"Worst daily return: {daily_returns.min():.2f}%")


# ==========================================
# 5. VOLATILITY
# ==========================================

daily_decimal_returns = df["adj_close"].pct_change()

rolling_volatility = (
    daily_decimal_returns
    .rolling(30)
    .std() * np.sqrt(252) * 100
)

print("\n4. VOLATILITY")

print(
    "Average rolling annualized volatility:",
    f"{rolling_volatility.mean():.2f}%"
)

print(
    "Maximum rolling annualized volatility:",
    f"{rolling_volatility.max():.2f}%"
)


# ==========================================
# 6. MAXIMUM DRAWDOWN
# ==========================================

running_peak = df["adj_close"].cummax()

drawdown = (
    df["adj_close"] / running_peak - 1
) * 100

max_drawdown = drawdown.min()

trough_date = drawdown.idxmin()

peak_date = df.loc[:trough_date, "adj_close"].idxmax()

print("\n5. MAXIMUM DRAWDOWN")

print(f"Maximum drawdown: {max_drawdown:.2f}%")
print("Peak date:", peak_date.date())
print("Trough date:", trough_date.date())


# ==========================================
# 7. TRADING VOLUME
# ==========================================

print("\n6. TRADING VOLUME")

print(f"Average volume: {df['volume'].mean():,.0f}")
print(f"Maximum volume: {df['volume'].max():,.0f}")


# ==========================================
# 8. ANNUAL RISK AND RETURN TABLE
# ==========================================

annual_volatility = (
    daily_decimal_returns
    .groupby(daily_decimal_returns.index.year)
    .std() * np.sqrt(252) * 100
)

risk_return = pd.concat(
    [
        annual_returns.rename("annual_return_pct"),
        annual_volatility.rename("annualized_volatility_pct")
    ],
    axis=1
)

risk_return.index.name = "year"

risk_return.to_csv(
    "outputs/annual_risk_return.csv"
)


# ==========================================
# 9. EXPORT SUMMARY REPORT
# ==========================================

report = f"""
TATA MOTORS STOCK MARKET DATA ANALYSIS
Historical Period: 2000-2025

OVERALL PERFORMANCE
-------------------
First Adjusted Price: Rs. {first_price:.2f}
Last Adjusted Price: Rs. {last_price:.2f}
Adjusted Price Return: {price_return:.2f}%

ANNUAL PERFORMANCE
------------------
Best Year: {best_year}
Best Annual Return: {annual_returns.max():.2f}%

Worst Year: {worst_year}
Worst Annual Return: {annual_returns.min():.2f}%

DAILY RETURNS
-------------
Average Daily Return: {daily_returns.mean():.4f}%
Best Daily Return: {daily_returns.max():.2f}%
Worst Daily Return: {daily_returns.min():.2f}%

VOLATILITY
----------
Average Rolling Annualized Volatility:
{rolling_volatility.mean():.2f}%

Maximum Rolling Annualized Volatility:
{rolling_volatility.max():.2f}%

MAXIMUM DRAWDOWN
----------------
Maximum Drawdown: {max_drawdown:.2f}%
Peak Date: {peak_date.date()}
Trough Date: {trough_date.date()}

TRADING VOLUME
--------------
Average Volume: {df['volume'].mean():,.0f}
Maximum Volume: {df['volume'].max():,.0f}

NOTE
----
Historical adjusted-price analysis only.
This report is not investment advice.
Corporate actions and the 2025 demerger
must be considered when interpreting results.
"""

with open(
    "outputs/final_analysis_report.txt",
    "w",
    encoding="utf-8"
) as file:
    file.write(report)

print("\n" + "=" * 60)
print("FINAL ANALYSIS COMPLETED!")
print("=" * 60)

print(report)
print("\nReports saved in outputs/")
