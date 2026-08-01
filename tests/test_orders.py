import pandas as pd


def test_order_id_unique(orders):
    assert orders["order_id"].is_unique


def test_order_total_positive(orders):
    assert (orders["total_amount"] > 0).all()


def test_order_date_valid(orders):
    orders["order_date"] = pd.to_datetime(orders["order_date"])

    assert orders["order_date"].notna().all()


def test_payment_method_not_null(orders):
    assert orders["payment_method"].notna().all()
