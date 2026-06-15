import pandas as pd
import os

data_folder = "1.data/raw"

files = [f for f in os.listdir(data_folder) if f.endswith(".csv")]

print(f"\nFound {len(files)} CSV files\n")

for file in files:
    print("=" * 60)
    print(f"FILE: {file}")

    path = os.path.join(data_folder, file)

    try:
        df = pd.read_csv(path)

        print("\nShape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

    except Exception as e:
        print(f"Error reading {file}: {e}")

    print("\n")