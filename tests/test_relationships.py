def test_every_order_has_customer(customers, orders):
    customer_ids = set(customers["customer_id"])
    assert orders["customer_id"].isin(customer_ids).all()


def test_every_order_item_has_order(orders, order_items):
    order_ids = set(orders["order_id"])
    assert order_items["order_id"].isin(order_ids).all()


def test_every_order_item_has_product(products, order_items):
    product_ids = set(products["product_id"])
    assert order_items["product_id"].isin(product_ids).all()


def test_every_review_has_customer(customers, product_reviews):
    customer_ids = set(customers["customer_id"])
    assert product_reviews["customer_id"].isin(customer_ids).all()


def test_every_review_has_product(products, product_reviews):
    product_ids = set(products["product_id"])
    assert product_reviews["product_id"].isin(product_ids).all()
