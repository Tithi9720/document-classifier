def classify_text(text: str) -> dict:
    text = text.lower()

    if "refund" in text or "charged" in text or "payment" in text:
        return {
            "category": "billing",
            "confidence": 0.95
        }

    if "password" in text or "login" in text or "account" in text:
        return {
            "category": "account",
            "confidence": 0.90
        }

    if "delivery" in text or "shipping" in text or "package" in text:
        return {
            "category": "shipping",
            "confidence": 0.90
        }

    return {
        "category": "unknown",
        "confidence": 0.50
    }