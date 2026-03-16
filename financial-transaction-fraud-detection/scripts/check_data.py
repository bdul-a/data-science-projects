import pandas as pd

# Enter your dataset path here
path = r"C:\Lytora Analytix\Projects\Financial Transaction System\financial-transaction-cleanup\data\raw\transactions.csv"

# Load dataset
df = pd.read_csv(path)

# Show first 5 rows
print("\nFirst 5 Rows of Dataset:")
print(df.head())

# Show column names
print("\nColumn Names:")
print(df.columns)