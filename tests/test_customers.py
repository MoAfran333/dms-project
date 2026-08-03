import pandas as pd

EMAIL_REGEX = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"


def test_customer_id_unique(customers):
    assert customers["customer_id"].is_unique


def test_customer_id_not_null(customers):
    assert customers["customer_id"].notna().all()


# def test_email_unique(customers):
#     assert customers["email"].is_unique


def test_email_not_null(customers):
    assert customers["email"].notna().all()


def test_email_format(customers):
    assert customers["email"].str.match(EMAIL_REGEX).all()


def test_gender_values(customers):
    allowed = {"Male", "Female", "Other"}

    assert set(customers["gender"]).issubset(allowed)


def test_country_not_null(customers):
    assert customers["country"].notna().all()


def test_signup_date_valid(customers):
    customers["signup_date"] = pd.to_datetime(customers["signup_date"])  # pyright: ignore[reportAttributeAccessIssue]

    assert customers["signup_date"].notna().all()
