import pandas as pd

# Read file
df = pd.read_csv("1.data/raw/07_scheme_performance.csv")

print("Original Shape:", df.shape)

# Check numeric return columns
return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in return_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Find expense ratio anomalies
anomalies = df[
    (df["expense_ratio_pct"] < 0.1) |
    (df["expense_ratio_pct"] > 2.5)
]

print("\nExpense Ratio Anomalies:")
print(anomalies[["scheme_name", "expense_ratio_pct"]])

print("\nNumber of anomalies:", len(anomalies))

print("\nCleaned Shape:", df.shape)

# Save cleaned file
df.to_csv(
    "1.data/processed/scheme_performance_cleaned.csv",
    index=False
)

print("\nscheme_performance_cleaned.csv saved successfully")