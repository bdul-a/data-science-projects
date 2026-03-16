import os

print("Starting financial transaction pipeline...")

print("Step 1: Cleaning raw dataset")
os.system("python scripts/clean_transactions.py")

print("Step 2: Running fraud detection")
os.system("python scripts/fraud_detection.py")

print("Pipeline completed successfully!")