import pandas as pd

# Read transactions file
df = pd.read_csv("1.data/raw/08_investor_transactions.csv")

print("Original Shape:", df.shape)

# Convert transaction date
df["transaction_date"] = pd.to_datetime(df["transaction_date"])

# Standardize transaction types
df["transaction_type"] = df["transaction_type"].str.strip().str.title()

# Keep only positive amounts
df = df[df["amount_inr"] > 0]

# Remove duplicate rows
df = df.drop_duplicates()

# Check KYC values
print("\nKYC Status Values:")
print(df["kyc_status"].unique())

print("\nTransaction Types:")
print(df["transaction_type"].unique())

print("\nCleaned Shape:", df.shape)

# Save cleaned file
df.to_csv(
    "1.data/processed/transactions_cleaned.csv",
    index=False
)

print("\ntransactions_cleaned.csv saved successfully")