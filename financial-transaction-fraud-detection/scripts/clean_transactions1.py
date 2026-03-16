# clean_transactions.py

import pandas as pd
import numpy as np


# -------------------------------
# Load Dataset
# -------------------------------

def load_data(path):

    print("Loading dataset...")

    df = pd.read_csv(path)

    print("Dataset loaded successfully\n")

    return df


# -------------------------------
# Inspect Data
# -------------------------------

def inspect_data(df):

    print("Dataset Info")
    print(df.info())

    print("\nMissing Values")
    print(df.isnull().sum())

    print("\nDuplicate Rows")
    print(df.duplicated().sum())


# -------------------------------
# Drop Unnecessary Columns
# -------------------------------

def drop_unnecessary_columns(df):

    print("\nDropping unnecessary columns...")

    if "Unnamed: 0" in df.columns:
        df = df.drop(columns=["Unnamed: 0"])

    return df


# -------------------------------
# Normalize Timestamp
# -------------------------------

def normalize_timestamp(df):

    print("\nNormalizing timestamps...")

    df["trans_date_trans_time"] = pd.to_datetime(
        df["trans_date_trans_time"], errors="coerce"
    )

    invalid = df["trans_date_trans_time"].isnull().sum()

    print(f"Invalid timestamps found: {invalid}")

    return df


# -------------------------------
# Extract Time Features
# -------------------------------

def extract_time_features(df):

    print("\nExtracting time features...")

    df["hour"] = df["trans_date_trans_time"].dt.hour
    df["day"] = df["trans_date_trans_time"].dt.day
    df["month"] = df["trans_date_trans_time"].dt.month
    df["day_of_week"] = df["trans_date_trans_time"].dt.day_name()

    print("Time features created: hour, day, month, day_of_week")

    return df


# -------------------------------
# Remove Duplicates
# -------------------------------

def remove_duplicates(df):

    print("\nRemoving duplicates...")

    before = len(df)

    df = df.drop_duplicates()

    after = len(df)

    print(f"Removed {before - after} duplicate rows")

    return df


# -------------------------------
# Handle Missing Merchants
# -------------------------------

def fill_missing_merchants(df):

    print("\nHandling missing merchants...")

    missing = df["merchant"].isnull().sum()

    print(f"Missing merchant names: {missing}")

    df["merchant"] = df["merchant"].fillna("Unknown Merchant")

    return df


# -------------------------------
# Handle Negative Transactions
# -------------------------------

def handle_negative_amounts(df):

    print("\nChecking negative amounts...")

    negatives = df[df["amt"] < 0]

    print(f"Negative transactions found: {len(negatives)}")

    # flag refunds
    df["is_refund"] = df["amt"] < 0

    # convert to positive
    df["amt"] = df["amt"].abs()

    return df


# -------------------------------
# Detect Outliers (IQR Method)
# -------------------------------

def detect_outliers(df):

    print("\nDetecting anomalies...")

    Q1 = df["amt"].quantile(0.25)
    Q3 = df["amt"].quantile(0.75)

    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    df["is_anomaly"] = (df["amt"] < lower) | (df["amt"] > upper)

    anomalies = df["is_anomaly"].sum()

    print(f"Anomalies detected: {anomalies}")

    return df


# -------------------------------
# Detect High Risk Merchants
# -------------------------------

def detect_high_risk_merchants(df):

    print("\nDetecting high risk merchants...")

    merchant_fraud_rate = df.groupby("merchant")["is_fraud"].mean()

    high_risk_merchants = merchant_fraud_rate[merchant_fraud_rate > 0.20].index

    df["high_risk_merchant"] = df["merchant"].isin(high_risk_merchants)

    print(f"High risk merchants detected: {len(high_risk_merchants)}")

    return df


# -------------------------------
# Export Clean Dataset
# -------------------------------

def export_data(df, path):

    print("\nExporting cleaned dataset...")

    df.to_csv(path, index=False)

    print(f"Clean dataset saved to {path}")


# -------------------------------
# Main Pipeline
# -------------------------------

def main():

    raw_path = r"C:\Lytora Analytix\Projects\Financial Transaction System\financial-transaction-cleanup\data\raw\transactions.csv"

    clean_path = r"C:\Lytora Analytix\Projects\Financial Transaction System\financial-transaction-cleanup\data\processed\clean_transactions.csv"

    df = load_data(raw_path)

    inspect_data(df)

    df = drop_unnecessary_columns(df)

    df = normalize_timestamp(df)

    df = extract_time_features(df)

    df = remove_duplicates(df)

    df = fill_missing_merchants(df)

    df = handle_negative_amounts(df)

    df = detect_outliers(df)

    df = detect_high_risk_merchants(df)

    export_data(df, clean_path)

    print("\nData cleaning pipeline completed successfully!")


# Run Script
if __name__ == "__main__":
    main()