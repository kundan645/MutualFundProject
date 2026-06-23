import pandas as pd
import os

DATA_FOLDER = "data/raw"

csv_files = [f for f in os.listdir(DATA_FOLDER) if f.endswith(".csv")]

print(f"Found {len(csv_files)} CSV files")

for file in csv_files:
    print("=" * 60)
    print(f"FILE: {file}")

    path = os.path.join(DATA_FOLDER, file)

    try:
        df = pd.read_csv(path)

        print("Shape:")
        print(df.shape)

        print("\nColumns:")
        print(df.columns.tolist())

        print("\nData Types:")
        print(df.dtypes)

        print("\nHead:")
        print(df.head())

    except Exception as e:
        print(f"Error reading {file}: {e}")