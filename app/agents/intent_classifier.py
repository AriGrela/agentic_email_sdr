from openai import OpenAI
from app.core.config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

INTENTS = [
    "pricing",
    "product_info",
    "general_interest",
    "not_interested"
]

def classify_intent(message: str) -> str:
    prompt = f"""
Clasificá la intención del siguiente mensaje
en UNA sola de estas categorías:

- pricing
- product_info
- general_interest
- not_interested

Mensaje:
"{message}"

Respondé SOLO con la categoría.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    intent = response.choices[0].message.content.strip().lower()
    return intent if intent in INTENTS else "general_interest"
