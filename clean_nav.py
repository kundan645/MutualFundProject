import pandas as pd

df = pd.read_csv("data/raw/02_nav_history.csv")

# Convert date column
df["date"] = pd.to_datetime(df["date"])

# Sort
df = df.sort_values(["amfi_code", "date"])

# Remove duplicates
df = df.drop_duplicates()

# Forward fill NAV values
df["nav"] = df.groupby("amfi_code")["nav"].ffill()

# Check invalid NAV values
invalid_nav = df[df["nav"] <= 0]

print("Invalid NAV Rows:", len(invalid_nav))

# Save cleaned file
df.to_csv(
    "data/processed/02_nav_history_clean.csv",
    index=False
)

print("NAV cleaning completed!")
print("Final Shape:", df.shape)
