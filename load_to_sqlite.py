import pandas as pd
from sqlalchemy import create_engine

# Connect to database
engine = create_engine(
    "sqlite:///data/db/bluestock_mf.db"
)

# Load cleaned files
nav_df = pd.read_csv(
    "data/processed/02_nav_history_clean.csv"
)

txn_df = pd.read_csv(
    "data/processed/08_investor_transactions_clean.csv"
)

perf_df = pd.read_csv(
    "data/processed/07_scheme_performance_clean.csv"
)

# Save to SQLite
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

print("All cleaned datasets loaded successfully!")
