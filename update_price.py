import pandas as pd
from pathlib import Path

# Path to your portfolio CSV
csv_path = Path("Start Your Own/chatgpt_portfolio_update.csv")

# Parameters to edit
ticker_to_update = "HOFT"   # <-- change to your ticker
new_buy_price = 10.15        # <-- change to your new buy price

# Load CSV
df = pd.read_csv(csv_path)

# Find latest row for that ticker
mask = df["Ticker"].str.upper() == ticker_to_update.upper()
if not mask.any():
    raise ValueError(f"No rows found for ticker {ticker_to_update}")

# Update Buy Price
df.loc[mask, "Buy Price"] = new_buy_price

# If you want to recalc cost basis too (shares * buy price)
if "Shares" in df.columns and "Cost Basis" in df.columns:
    shares = df.loc[mask, "Shares"].astype(float)
    df.loc[mask, "Cost Basis"] = shares * new_buy_price

# Save back to CSV
df.to_csv(csv_path, index=False)
print(f"Updated {ticker_to_update} Buy Price to {new_buy_price} in {csv_path}")
