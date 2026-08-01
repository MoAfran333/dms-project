import pandas as pd
import os

# -----------------------------
# File Paths
# -----------------------------
RAW_DATA = "data/raw/order_items.csv"
PROCESSED_DATA = "data/processed/order_items.csv"

# -----------------------------
# Load Dataset
# -----------------------------
print("Loading dataset...")

df = pd.read_csv(RAW_DATA)

print(f"Rows : {df.shape[0]}")
print(f"Columns : {df.shape[1]}")

# -----------------------------
# Rename Columns
# -----------------------------
df.columns = df.columns.str.strip().str.lower()

# -----------------------------
# Remove Duplicate Records
# -----------------------------
duplicates = df.duplicated().sum()
print("Duplicate Records :", duplicates)

df.drop_duplicates(inplace=True)

# -----------------------------
# Remove Missing Values
# -----------------------------
print("\nMissing Values")
print(df.isnull().sum())

df.dropna(inplace=True)

# -----------------------------
# Convert Datatypes
# -----------------------------
df["order_item_id"] = df["order_item_id"].astype("int64")
df["order_id"] = df["order_id"].astype("int64")
df["product_id"] = df["product_id"].astype("int64")
df["quantity"] = df["quantity"].astype("int32")
df["unit_price"] = df["unit_price"].astype("float64")

# -----------------------------
# Remove Invalid Records
# -----------------------------
df = df[df["quantity"] > 0]
df = df[df["unit_price"] > 0]

# -----------------------------
# Feature Engineering
# -----------------------------
df["total_price"] = df["quantity"] * df["unit_price"]

# Average price per quantity
df["price_per_unit"] = df["total_price"] / df["quantity"]

# -----------------------------
# Remove Outliers (IQR)
# -----------------------------
Q1 = df["unit_price"].quantile(0.25)
Q3 = df["unit_price"].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

print("\nRemoving Outliers...")

df = df[
    (df["unit_price"] >= lower) &
    (df["unit_price"] <= upper)
]

# -----------------------------
# Reset Index
# -----------------------------
df.reset_index(drop=True, inplace=True)

# -----------------------------
# Dataset Summary
# -----------------------------
print("\nProcessed Dataset")
print(df.info())

print("\nStatistics")
print(df.describe())

print("\nFinal Shape :", df.shape)

# -----------------------------
# Save Processed Dataset
# -----------------------------
os.makedirs("data/processed", exist_ok=True)

df.to_csv(PROCESSED_DATA, index=False)

print("\nProcessed file saved successfully.")
print(PROCESSED_DATA)