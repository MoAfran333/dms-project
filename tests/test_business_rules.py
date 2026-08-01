def test_order_total_matches_items(orders, order_items):

    calculated = (
        order_items.assign(total=lambda x: x.quantity * x.unit_price)
        .groupby("order_id")["total"]
        .sum()
        .reset_index()
    )

    merged = orders.merge(calculated, on="order_id")

    assert (abs(merged["total_amount"] - merged["total"]) < 0.01).all()
