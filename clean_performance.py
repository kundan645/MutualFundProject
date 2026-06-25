import pandas as pd

df = pd.read_csv("data/raw/07_scheme_performance.csv")

print("Original Shape:", df.shape)

# Return columns
return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct"
]

# Convert returns to numeric
for col in return_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Check missing values after conversion
print("\nMissing Return Values:")
print(df[return_cols].isnull().sum())

# Expense Ratio Validation
invalid_expense = df[
    (df["expense_ratio_pct"] < 0.1) |
    (df["expense_ratio_pct"] > 2.5)
]

print("\nInvalid Expense Ratio Rows:")
print(len(invalid_expense))

# Check negative AUM
invalid_aum = df[df["aum_crore"] <= 0]

print("\nInvalid AUM Rows:")
print(len(invalid_aum))

# Remove duplicates
df = df.drop_duplicates()

# Save cleaned file
df.to_csv(
    "data/processed/07_scheme_performance_clean.csv",
    index=False
)
print("\nScheme Performance Cleaning Completed!")
print("Final Shape:", df.shape)