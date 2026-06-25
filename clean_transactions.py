import pandas as pd

df = pd.read_csv("data/raw/08_investor_transactions.csv")

print("Original Shape:", df.shape)

# Convert date
df["transaction_date"] = pd.to_datetime(df["transaction_date"])

# Standardize transaction types
df["transaction_type"] = (
    df["transaction_type"]
    .str.strip()
    .str.title()
)

# Standardize common variations
df["transaction_type"] = df["transaction_type"].replace({
    "Sip": "SIP",
    "Lumpsum": "Lumpsum",
    "Redemption": "Redemption"
})

# Check invalid amounts
invalid_amounts = df[df["amount_inr"] <= 0]

print("\nInvalid Amount Rows:")
print(len(invalid_amounts))

# Check KYC values
print("\nKYC Status Values:")
print(df["kyc_status"].unique())

# Remove duplicates
df = df.drop_duplicates()

# Save cleaned file
df.to_csv(
    "data/processed/08_investor_transactions_clean.csv",
    index=False
)

print("\nFinal Shape:", df.shape)
print("Transactions cleaning completed!")
