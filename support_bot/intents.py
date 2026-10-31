import re

ORDER_WORDS = {"order", "tracking", "shipped", "delivery"}
REFUND_WORDS = {"refund", "return"}
GREETING_WORDS = {"hi", "hello", "hey"}


def classify_intent(message: str) -> str:
    words = re.findall(r"[a-z]+", message.lower())
    found = set(words)
    if found & REFUND_WORDS or " money back " in f" {' '.join(words)} ":
        return "refund"
    if found & ORDER_WORDS:
        return "order_status"
    if found & GREETING_WORDS:
        return "greeting"
    return "other"