import pandas as pd
from sklearn.ensemble import IsolationForest


def detect_fraud(input_path, output_path):

    print("Loading cleaned dataset...")

    df = pd.read_csv(r"C:\Lytora Analytix\Projects\Financial Transaction System\financial-transaction-cleanup\data\processed\clean_transactions.csv", low_memory=False)

    # features used for anomaly detection
    features = df[["amt"]]

    print("Training Isolation Forest model...")

    model = IsolationForest(
        n_estimators=100,
        contamination=0.02,
        random_state=42
    )

    df["fraud_prediction"] = model.fit_predict(features)

    # convert prediction labels
    df["fraud_prediction"] = df["fraud_prediction"].map({
        1: "Normal",
        -1: "Fraud"
    })

    fraud_count = (df["fraud_prediction"] == "Fraud").sum()

    print(f"Fraudulent transactions detected: {fraud_count}")

    df.to_csv(output_path, index=False)

    print("Fraud detection completed.")


if __name__ == "__main__":

    detect_fraud(
        r"C:\Lytora Analytix\Projects\Financial Transaction System\financial-transaction-cleanup\data\processed\clean_transactions.csv",
        r"C:\Lytora Analytix\Projects\Financial Transaction System\financial-transaction-cleanup\data\processed\fraud_checked_transactions.csv"
    )
