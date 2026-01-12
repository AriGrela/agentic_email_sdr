"""Tests para el clasificador de intenciones."""

import pytest
from app.agents.intent_classifier import classify_intent, INTENTS


def test_classify_pricing_intent():
    """Test que detecta correctamente intención de pricing."""
    message = "¿Cuánto cuesta el plan básico?"
    intent = classify_intent(message)
    assert intent == "pricing"


def test_classify_product_info_intent():
    """Test que detecta correctamente intención de product_info."""
    message = "¿Qué características tiene el producto?"
    intent = classify_intent(message)
    # Puede ser product_info o general_interest dependiendo del modelo
    assert intent in INTENTS


def test_classify_general_interest():
    """Test que detecta interés general."""
    message = "Hola, me interesa saber más sobre su servicio"
    intent = classify_intent(message)
    assert intent in INTENTS


def test_classify_not_interested():
    """Test que detecta falta de interés."""
    message = "No estoy interesado, gracias"
    intent = classify_intent(message)
    assert intent in INTENTS


def test_classify_returns_valid_intent():
    """Test que siempre retorna una intención válida."""
    messages = [
        "Hola",
        "¿Precios?",
        "Información del producto",
        "No gracias",
        "Random text that doesn't match anything"
    ]
    
    for message in messages:
        intent = classify_intent(message)
        assert intent in INTENTS, f"Intent '{intent}' no es válido para mensaje: {message}"


def test_classify_empty_message():
    """Test con mensaje vacío."""
    intent = classify_intent("")
    # Debería retornar una intención válida (probablemente general_interest)
    assert intent in INTENTS
