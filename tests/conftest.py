import pandas as pd
import pytest


@pytest.fixture(scope="session")
def customers():
    return pd.read_csv("data/customers.csv")


@pytest.fixture(scope="session")
def orders():
    return pd.read_csv("data/orders.csv")


@pytest.fixture(scope="session")
def order_items():
    return pd.read_csv("data/order_items.csv")


@pytest.fixture(scope="session")
def products():
    return pd.read_csv("data/products.csv")


@pytest.fixture(scope="session")
def product_reviews():
    return pd.read_csv("data/product_reviews.csv")
