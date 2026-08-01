import pandas as pd
import pytest


@pytest.fixture(scope="session")
def customers():
    return pd.read_csv("data/processed/customers_processed.csv")


@pytest.fixture(scope="session")
def orders():
    return pd.read_csv("data/processed/orders_processed.csv")


@pytest.fixture(scope="session")
def order_items():
    return pd.read_csv("data/processed/order_items_processed.csv")


@pytest.fixture(scope="session")
def products():
    return pd.read_csv("data/processed/products_processed.csv")


@pytest.fixture(scope="session")
def product_reviews():
    return pd.read_csv("data/processed/product_reviews_processed.csv")
