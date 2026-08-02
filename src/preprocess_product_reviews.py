import os
import pandas as pd

# ============================
# File Paths
# ============================
RAW_FILE = "data/raw/product_reviews.csv"
PROCESSED_FILE = "data/processed/product_reviews.csv"

# ============================
# Create processed folder
# ============================
os.makedirs("data/processed", exist_ok=True)

# ============================
# Load Dataset
# ============================
df = pd.read_csv(RAW_FILE)

print("Original Shape:", df.shape)

# ============================
# Remove Duplicate Rows
# ============================
df = df.drop_duplicates()

# ============================
# Remove Completely Empty Rows
# ============================
df = df.dropna(how="all")

# ============================
# Fill Missing Values
# ============================

# Numeric columns
numeric_columns = df.select_dtypes(include=["number"]).columns

for col in numeric_columns:
    df[col] = df[col].fillna(df[col].median())

# Text columns
text_columns = df.select_dtypes(include=["object"]).columns

for col in text_columns:
    df[col] = df[col].fillna("Unknown")
    df[col] = df[col].astype(str).str.strip()

# ============================
# Convert review_date
# ============================
if "review_date" in df.columns:
    df["review_date"] = pd.to_datetime(
        df["review_date"],
        errors="coerce"
    )

# ============================
# Remove Empty Reviews
# ============================
if "review_text" in df.columns:
    df = df[df["review_text"] != ""]
    df = df[df["review_text"] != "Unknown"]

# ============================
# Rating Validation
# ============================
if "rating" in df.columns:
    df = df[(df["rating"] >= 1) & (df["rating"] <= 5)]

# ============================
# Save Processed Data
# ============================
df.to_csv(PROCESSED_FILE, index=False)

print("\nPreprocessing Completed Successfully!")
print("Processed Shape:", df.shape)
print("Saved to:", PROCESSED_FILE)