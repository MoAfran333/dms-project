from pathlib import Path

import pandas as pd
import pytest


def load_csv(path):
    path = Path(path)
    if not path.is_file():
        pytest.skip(f"Missing required dataset: {path}")
    return pd.read_csv(path)


@pytest.fixture(scope="session")
def customers():
    return load_csv("data/processed/customers_processed.csv")


@pytest.fixture(scope="session")
def orders():
    return load_csv("data/processed/orders_processed.csv")


@pytest.fixture(scope="session")
def order_items():
    return load_csv("data/processed/order_items.csv")


@pytest.fixture(scope="session")
def products():
    return load_csv("data/processed/products_processed.csv")


@pytest.fixture(scope="session")
def product_reviews():
    return load_csv("data/processed/product_reviews_processed.csv")
