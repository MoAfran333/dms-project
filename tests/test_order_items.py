def test_order_item_unique(order_items):
    assert order_items["order_item_id"].is_unique


def test_quantity_positive(order_items):
    assert (order_items["quantity"] > 0).all()


def test_unit_price_positive(order_items):
    assert (order_items["unit_price"] > 0).all()
