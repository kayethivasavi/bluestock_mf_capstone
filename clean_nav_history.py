import pandas as pd

# Read the NAV file
df = pd.read_csv("1.data/raw/02_nav_history.csv")

# Show original rows
print("Original Shape:", df.shape)

# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"])

# Sort by fund code and date
df = df.sort_values(by=["amfi_code", "date"])

# Remove duplicate rows
df = df.drop_duplicates()

# Keep only valid NAV values
df = df[df["nav"] > 0]

# Show cleaned rows
print("Cleaned Shape:", df.shape)

# Save cleaned file
df.to_csv(
    "1.data/processed/nav_history_cleaned.csv",
    index=False
)

print("nav_history_cleaned.csv saved successfully")