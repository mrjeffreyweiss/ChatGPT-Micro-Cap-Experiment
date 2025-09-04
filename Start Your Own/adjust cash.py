#!/usr/bin/env python3
import pandas as pd
from pathlib import Path
import sys

# Usage: python3 adjust_cash.py +/-AMOUNT
# Example: python3 adjust_cash.py 2500    (adds 2500)
#          python3 adjust_cash.py -1000   (subtracts 1000)

if len(sys.argv) != 2:
    print("Usage: python3 adjust_cash.py +/-AMOUNT")
    sys.exit(1)

try:
    delta = float(sys.argv[1])
except ValueError:
    print("Amount must be a number, e.g. 2500 or -1000")
    sys.exit(1)

csv_path = Path("Start Your Own/chatgpt_portfolio_update.csv")
df = pd.read_csv(csv_path)

# Find latest CASH and TOTAL rows
cash_rows = df[df["Ticker"].str.upper() == "CASH"].copy()
total_rows = df[df["Ticker"].str.upper() == "TOTAL"].copy()

if cash_rows.empty or total_rows.empty:
    raise ValueError("CASH or TOTAL row not found — seed the portfolio first.")

# Update latest CASH and TOTAL entries
cash_idx = cash_rows.index[-1]
total_idx = total_rows.index[-1]

df.at[cash_idx, "Cash Balance"] = float(df.at[cash_idx, "Cash Balance"]) + delta
df.at[total_idx, "Cash Balance"] = float(df.at[total_idx, "Cash Balance"]) + delta
df.at[total_idx, "Total Equity"] = float(df.at[total_idx, "Total Equity"]) + delta

# Save changes
df.to_csv(csv_path, index=False)
print(f"Adjusted cash by {delta:+}. New balances:")
print(df.loc[[cash_idx, total_idx], ["Date","Ticker","Cash Balance","Total Equity"]])
