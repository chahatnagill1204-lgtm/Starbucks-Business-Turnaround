# Starbucks Business Turnaround - Python Analysis
# Run from the project root after placing starbucks_turnaround.csv in data/

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/starbucks_turnaround.csv")

# Core calculations
df["calculated_revenue_growth_pct"] = df["revenue_m"].pct_change() * 100
df["calculated_operating_income_growth_pct"] = df["operating_income_m"].pct_change() * 100
df["calculated_store_growth_pct"] = df["stores"].pct_change() * 100
df["calculated_revenue_per_store_m"] = df["revenue_m"] / df["stores"]

print(df[[
    "fiscal_year", "revenue_m", "operating_income_m", "operating_margin_pct",
    "stores", "calculated_revenue_per_store_m"
]].round(2))

# Revenue vs operating income
plt.figure(figsize=(9, 5))
plt.plot(df["fiscal_year"], df["revenue_m"], marker="o", label="Revenue ($M)")
plt.plot(df["fiscal_year"], df["operating_income_m"], marker="o", label="Operating Income ($M)")
plt.title("Starbucks Revenue vs Operating Income")
plt.xlabel("Fiscal Year")
plt.ylabel("$ Millions")
plt.legend()
plt.grid(alpha=0.25)
plt.show()

# Operating margin
plt.figure(figsize=(9, 5))
plt.plot(df["fiscal_year"], df["operating_margin_pct"], marker="o")
plt.title("Starbucks Operating Margin Trend")
plt.xlabel("Fiscal Year")
plt.ylabel("Operating Margin (%)")
plt.grid(alpha=0.25)
plt.show()

# Demand drivers
demand = df.dropna(subset=["global_transactions_pct", "global_ticket_pct"])
plt.figure(figsize=(9, 5))
plt.plot(demand["fiscal_year"], demand["global_transactions_pct"], marker="o", label="Transactions")
plt.plot(demand["fiscal_year"], demand["global_ticket_pct"], marker="o", label="Ticket")
plt.axhline(0, linewidth=1)
plt.title("Global Comparable-Store Demand Drivers")
plt.xlabel("Fiscal Year")
plt.ylabel("Change (%)")
plt.legend()
plt.grid(alpha=0.25)
plt.show()

# Store productivity
plt.figure(figsize=(9, 5))
plt.plot(df["fiscal_year"], df["calculated_revenue_per_store_m"], marker="o")
plt.title("Revenue per Store")
plt.xlabel("Fiscal Year")
plt.ylabel("Revenue per Store ($M)")
plt.grid(alpha=0.25)
plt.show()
