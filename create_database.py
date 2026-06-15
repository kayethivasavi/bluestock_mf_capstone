import pandas as pd
from sqlalchemy import create_engine

# Create SQLite database
engine = create_engine("sqlite:///bluestock_mf.db")

# Load cleaned files
nav_df = pd.read_csv(
    "1.data/processed/nav_history_cleaned.csv"
)

txn_df = pd.read_csv(
    "1.data/processed/transactions_cleaned.csv"
)

perf_df = pd.read_csv(
    "1.data/processed/scheme_performance_cleaned.csv"
)

# Save as database tables
nav_df.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

txn_df.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

perf_df.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

print("Database created successfully!")
print("Tables loaded:")
print("- fact_nav")
print("- fact_transactions")
print("- fact_performance")