import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------
# Page Title
# -------------------------

st.title("Financial Transaction Fraud Detection Dashboard")

st.write("Interactive dashboard for monitoring suspicious transactions.")

# -------------------------
# Load Dataset
# -------------------------

data_path = r"C:\Lytora Analytix\Projects\Financial Transaction System\financial-transaction-cleanup\data\processed\fraud_checked_transactions.csv"

df = pd.read_csv(data_path, low_memory=False)

# convert date column
df["trans_date_trans_time"] = pd.to_datetime(df["trans_date_trans_time"], errors="coerce")

# -------------------------
# KPI Metrics
# -------------------------

total_transactions = len(df)
fraud_transactions = df["is_fraud"].sum()
fraud_rate = fraud_transactions / total_transactions * 100

col1, col2, col3 = st.columns(3)

col1.metric("Total Transactions", total_transactions)
col2.metric("Fraud Transactions", fraud_transactions)
col3.metric("Fraud Rate (%)", round(fraud_rate,2))

# -------------------------
# Fraud vs Normal
# -------------------------

st.subheader("Fraud vs Normal Transactions")

fraud_counts = df["fraud_prediction"].value_counts()

fig1 = plt.figure()
fraud_counts.plot(kind="bar")
plt.xlabel("Transaction Type")
plt.ylabel("Count")
plt.title("Fraud vs Normal Transactions")

st.pyplot(fig1)

# -------------------------
# Transaction Amount Distribution
# -------------------------

st.subheader("Transaction Amount Distribution")

fig2 = plt.figure()
df["amt"].hist(bins=50)
plt.xlabel("Transaction Amount")
plt.ylabel("Frequency")
plt.title("Transaction Amount Distribution")

st.pyplot(fig2)

# -------------------------
# Top Merchants
# -------------------------

st.subheader("Top Merchants by Transactions")

top_merchants = df["merchant"].value_counts().head(10)

fig3 = plt.figure()
top_merchants.plot(kind="bar")
plt.xlabel("Merchant")
plt.ylabel("Transactions")
plt.title("Top Merchants")

st.pyplot(fig3)

# -------------------------
# Fraud Merchants
# -------------------------

st.subheader("Merchants with Most Fraud Transactions")

fraud_merchants = df[df["is_fraud"] == 1]["merchant"].value_counts().head(10)

fig4 = plt.figure()
fraud_merchants.plot(kind="bar")
plt.xlabel("Merchant")
plt.ylabel("Fraud Transactions")
plt.title("High Risk Merchants")

st.pyplot(fig4)

# -------------------------
# Daily Transactions
# -------------------------

st.subheader("Daily Transaction Volume")

df["date"] = df["trans_date_trans_time"].dt.date

daily_tx = df.groupby("date").size()

fig5 = plt.figure()
daily_tx.plot()
plt.xlabel("Date")
plt.ylabel("Transactions")
plt.title("Daily Transaction Trend")

st.pyplot(fig5)

# -------------------------
# Data Table
# -------------------------

st.subheader("Transaction Data")

st.dataframe(df.head(1000))