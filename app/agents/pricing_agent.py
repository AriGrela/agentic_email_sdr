from openai import OpenAI
from app.core.config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def handle_pricing(history):
    prompt = """
Sos un especialista en precios de ACME Solutions.
Respondé de forma clara y concreta.
"""

    messages = [{"role": "system", "content": prompt}]
    messages.extend(history)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )

    return {
        "agent": "PricingAgent",
        "content": response.choices[0].message.content
    }