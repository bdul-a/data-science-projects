<<<<<<< HEAD
# Financial Transaction Dataset Cleanup & Fraud Detection

## Project Overview

Financial transaction data often contains inconsistencies such as duplicate records, missing merchant information, incorrect timestamps, and abnormal transaction values. These issues can negatively affect financial reporting and fraud monitoring systems.

This project builds a **complete data cleaning and validation pipeline** for financial transaction logs. The pipeline processes raw transaction data, standardizes timestamps, removes duplicates, handles missing values, and identifies potential fraud transactions using anomaly detection techniques.

The goal of this project is to simulate a **real-world fintech data engineering and analytics workflow**.

---

## Business Problem

A fintech startup stores transaction logs from multiple sources. Due to inconsistent data entry and system integrations, the dataset contains:

* Duplicate transactions
* Negative or abnormal transaction amounts
* Missing merchant names
* Inconsistent timestamp formats

These issues make it difficult for analysts to generate reliable financial reports and detect fraudulent transactions.

This project demonstrates how to **clean, validate, and analyze transaction data** to improve reporting accuracy.

---

## Project Objectives

* Normalize inconsistent timestamp formats
* Detect and remove duplicate transactions
* Handle missing merchant information
* Identify abnormal transactions using anomaly detection
* Build a reusable data cleaning pipeline
* Export a validated dataset for financial reporting and analytics

---

## Dataset

The dataset used in this project is a **financial transaction dataset obtained from Kaggle**.

Typical fields include:

| Column         | Description                             |
| -------------- | --------------------------------------- |
| transaction_id | Unique transaction identifier           |
| account_id     | Customer account ID                     |
| amount         | Transaction value                       |
| timestamp      | Date and time of transaction            |
| merchant       | Merchant where the transaction occurred |
| category       | Transaction category                    |

---

## Tools & Technologies

* Python
* Pandas
* NumPy
* Scikit-learn
* SQL
* Jupyter Notebook
* Matplotlib

---

## Project Workflow

Raw Dataset
↓
Data Loading
↓
Data Inspection
↓
Timestamp Normalization
↓
Duplicate Detection
↓
Missing Data Handling
↓
Outlier / Anomaly Detection
↓
Fraud Detection Model
↓
Validated Transaction Dataset

---

## Project Structure

```
financial-transaction-cleanup
│
├── data
│   ├── raw
│   │   └── transactions.csv
│   │
│   └── processed
│       ├── clean_transactions.csv
│       └── fraud_checked_transactions.csv
│
├── notebooks
│   └── analysis.ipynb
│
├── scripts
│   ├── clean_transactions.py
│   ├── fraud_detection.py
│   └── pipeline.py
│
├── sql
│   └── validation_queries.sql
│
├── requirements.txt
└── README.md
```

---

## Data Cleaning Steps

### Timestamp Normalization

Different timestamp formats were converted into a standardized datetime format using Pandas.

### Duplicate Detection

Duplicate transactions were detected and removed using unique transaction identifiers and transaction attributes.

### Missing Merchant Handling

Transactions with missing merchant names were filled with a placeholder value (`Unknown Merchant`).

### Negative Amount Handling

Negative transactions were flagged and converted to positive values when appropriate.

---

## Fraud Detection

Potential fraud transactions were detected using an **Isolation Forest anomaly detection model**.

The model identifies unusual transactions by analyzing the distribution of transaction amounts and isolating anomalies in the dataset.

Fraud predictions are labeled as:

* **Normal**
* **Fraud**

---

## Example Output

| transaction_id | account_id | amount | merchant         | fraud_prediction |
| -------------- | ---------- | ------ | ---------------- | ---------------- |
| 1001           | 3402       | 120    | Amazon           | Normal           |
| 1002           | 3402       | 9800   | Unknown Merchant | Fraud            |

---

## How to Run the Project

### Install dependencies

```
pip install -r requirements.txt
```

### Run data cleaning pipeline

```
python scripts/pipeline.py
```

This will automatically:

1. Clean the raw transaction dataset
2. Detect anomalies and fraud transactions
3. Export the processed dataset

---

## Results

The pipeline produces a validated dataset that:

* Removes duplicate transactions
* Standardizes timestamps
* Handles missing merchant information
* Detects abnormal transactions
* Flags potential fraud activity

This cleaned dataset can now be used for **financial reporting, analytics dashboards, and fraud monitoring systems**.

---

## Skills Demonstrated

* Data Cleaning & Preprocessing
* Financial Data Analysis
* Anomaly Detection
* Fraud Detection
* SQL Data Validation
* Data Pipeline Automation
* Exploratory Data Analysis

---

## Future Improvements

Possible improvements for this project include:

* Real-time transaction monitoring pipeline
* Advanced machine learning fraud detection models
* Customer spending behavior analysis
* Interactive dashboards using Power BI or Tableau
* Cloud deployment of the pipeline

---

## Author

Data Analytics Project – Financial Transaction Dataset Cleanup & Fraud Detection
=======
# data-science-projects
Data Science projects including SQL, Data Cleaning, Pandas and Business Intelligence
>>>>>>> 9e229b7f6a4aea31b59de8af3edde3aaac7e36d7
