import pandas as pd
import os

# -----------------------------
# File Paths
# -----------------------------
INPUT_FILE = "data/raw/orders.csv"
OUTPUT_FILE = "data/processed/orders_processed.csv"

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv(INPUT_FILE)

print("Original Shape:", df.shape)

# -----------------------------
# Remove Duplicate Rows
# -----------------------------
df = df.drop_duplicates()

# -----------------------------
# Remove Duplicate Order IDs
# -----------------------------
df = df.drop_duplicates(subset=["order_id"])

# -----------------------------
# Handle Missing Values
# -----------------------------

# Remove rows where order_id or customer_id is missing
df = df.dropna(subset=["order_id", "customer_id"])

# Fill missing payment methods
df["payment_method"] = df["payment_method"].fillna("Unknown")

# Fill missing shipping country
df["shipping_country"] = df["shipping_country"].fillna("Unknown")

# Fill missing total amount with median
df["total_amount"] = pd.to_numeric(
    df["total_amount"],
    errors="coerce"
)

median_amount = df["total_amount"].median()
df["total_amount"] = df["total_amount"].fillna(median_amount)

# -----------------------------
# Convert Date
# -----------------------------
df["order_date"] = pd.to_datetime(
    df["order_date"],
    errors="coerce"
)

# Remove invalid dates
df = df.dropna(subset=["order_date"])

# -----------------------------
# Remove Invalid Amounts
# -----------------------------
df = df[df["total_amount"] >= 0]

# -----------------------------
# Standardize Text Columns
# -----------------------------
df["payment_method"] = (
    df["payment_method"]
    .astype(str)
    .str.strip()
    .str.title()
)

df["shipping_country"] = (
    df["shipping_country"]
    .astype(str)
    .str.strip()
    .str.title()
)

# -----------------------------
# Convert IDs to Integer
# -----------------------------
df["order_id"] = df["order_id"].astype(int)
df["customer_id"] = df["customer_id"].astype(int)

# -----------------------------
# Sort by Order Date
# -----------------------------
df = df.sort_values("order_date")

# -----------------------------
# Reset Index
# -----------------------------
df = df.reset_index(drop=True)

# -----------------------------
# Create Output Folder
# -----------------------------
os.makedirs("data/processed", exist_ok=True)

# -----------------------------
# Save Processed Dataset
# -----------------------------
df.to_csv(OUTPUT_FILE, index=False)

print("Processed Shape:", df.shape)
print("Saved Successfully to:", OUTPUT_FILE)