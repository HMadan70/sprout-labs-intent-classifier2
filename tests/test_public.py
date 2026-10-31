from support_bot.intents import classify_intent


def test_order_status():
    assert classify_intent("Where is my order?") == "order_status"


def test_refund():
    assert classify_intent("I want a refund") == "refund"


def test_greeting():
    assert classify_intent("Hello there") == "greeting"
