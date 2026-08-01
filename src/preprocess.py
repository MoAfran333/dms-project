import os
import pandas as pd

# ----------------------------
# Folder Paths
# ----------------------------
RAW_PATH = "data/raw"
PROCESSED_PATH = "data/processed"


def preprocess_customers():
    """
    Preprocess the customers dataset and save the cleaned data.
    """
    try:
        print("\nProcessing customers dataset...")

        customers = pd.read_csv(os.path.join(RAW_PATH, "customers.csv"))

        print(f"Original Customers Shape : {customers.shape}")

        # Convert signup_date to datetime
        customers["signup_date"] = pd.to_datetime(
            customers["signup_date"],
            errors="coerce"
        )

        # Remove leading/trailing spaces
        text_columns = ["name", "email", "gender", "country"]

        for col in text_columns:
            customers[col] = customers[col].str.strip()

        # Remove duplicate rows
        customers = customers.drop_duplicates()

        # Remove rows with missing values
        customers = customers.dropna()

        print(f"Processed Customers Shape: {customers.shape}")

        customers.to_csv(
            os.path.join(PROCESSED_PATH, "customers_processed.csv"),
            index=False
        )

        print("customers_processed.csv saved successfully.")

    except Exception as e:
        print(f"Error while processing customers dataset: {e}")


def preprocess_products():
    """
    Preprocess the products dataset and save the cleaned data.
    """
    try:
        print("\nProcessing products dataset...")

        products = pd.read_csv(os.path.join(RAW_PATH, "products.csv"))

        print(f"Original Products Shape : {products.shape}")

        # Remove leading/trailing spaces
        text_columns = ["product_name", "category", "brand"]

        for col in text_columns:
            products[col] = products[col].str.strip()

        # Convert numeric columns
        products["price"] = pd.to_numeric(
            products["price"],
            errors="coerce"
        )

        products["stock_quantity"] = pd.to_numeric(
            products["stock_quantity"],
            errors="coerce"
        )

        # Remove duplicate rows
        products = products.drop_duplicates()

        # Remove rows with missing values
        products = products.dropna()

        # Convert stock quantity back to integer
        products["stock_quantity"] = products["stock_quantity"].astype(int)

        print(f"Processed Products Shape: {products.shape}")

        products.to_csv(
            os.path.join(PROCESSED_PATH, "products_processed.csv"),
            index=False
        )

        print("products_processed.csv saved successfully.")

    except Exception as e:
        print(f"Error while processing products dataset: {e}")


def main():
    """
    Main function to execute preprocessing.
    """

    print("=" * 60)
    print("        DATA PREPROCESSING PIPELINE STARTED")
    print("=" * 60)

    # Create processed folder if it doesn't exist
    os.makedirs(PROCESSED_PATH, exist_ok=True)

    preprocess_customers()
    preprocess_products()

    print("\n" + "=" * 60)
    print("      DATA PREPROCESSING COMPLETED SUCCESSFULLY")
    print("=" * 60)


if __name__ == "__main__":
    main()