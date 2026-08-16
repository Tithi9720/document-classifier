from app.classifier import classify_text


def test_billing_classification():
    result = classify_text("I was charged twice")

    assert result["category"] == "billing"


def test_account_classification():
    result = classify_text("I forgot my password")

    assert result["category"] == "account"


def test_shipping_classification():
    result = classify_text("Where is my package?")

    assert result["category"] == "shipping"


def test_unknown_classification():
    result = classify_text("The weather is nice today")

    assert result["category"] == "unknown"