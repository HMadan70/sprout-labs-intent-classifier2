# Sprout Labs: classify customer intents

Sprout Labs' support bot must know what a shopper wants before it can answer.
Your job: a first, rule-based intent classifier.

## What to build
File: `support_bot/intents.py`

```python
def classify_intent(message: str) -> str:
    ...
```

## Input
`message`: one customer message, any case, may contain punctuation.

## Output
Exactly one of these strings:

| Intent | When the message mentions (case-insensitive, whole words) |
|---|---|
| `"order_status"` | `order`, `tracking`, `shipped`, `delivery` |
| `"refund"` | `refund`, `return`, `money back` |
| `"greeting"` | `hi`, `hello`, `hey` (and nothing from the rows above) |
| `"other"` | none of the above, or an empty message |

If a message matches both `order_status` and `refund`, return `"refund"`.

## Run the tests
```
pip install pytest
pytest
```
The tests in `tests/` are only a few examples. Darbni runs more tests when you submit.

## Done when
`pytest` passes locally, then submit your repo URL and the full commit SHA.
