import pandas as pd


def test_review_id_unique(product_reviews):
    assert product_reviews["review_id"].is_unique


def test_rating_range(product_reviews):
    assert product_reviews["rating"].between(1, 5).all()


def test_review_date_valid(product_reviews):
    product_reviews["review_date"] = pd.to_datetime(product_reviews["review_date"])
    assert product_reviews["review_date"].notna().all()
