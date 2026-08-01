def test_product_id_unique(products):
    assert products["product_id"].is_unique


def test_product_id_not_null(products):
    assert products["product_id"].notna().all()


def test_price_positive(products):
    assert (products["price"] > 0).all()


def test_stock_non_negative(products):
    assert (products["stock_quantity"] >= 0).all()


def test_brand_not_null(products):
    assert products["brand"].notna().all()


def test_product_name_not_null(products):
    assert products["product_name"].notna().all()
