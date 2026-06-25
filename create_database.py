from sqlalchemy import create_engine

# Create SQLite database
engine = create_engine("sqlite:///data/db/bluestock_mf.db")

print("Database created successfully!")