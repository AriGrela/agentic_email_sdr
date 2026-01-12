"""Tests para el almacenamiento de conversaciones."""

from app.memory.conversation_store import get_conversation, add_message


def test_get_empty_conversation():
    """Test que retorna lista vacía para email sin historial."""
    email = "test@ejemplo.com"
    history = get_conversation(email)
    assert history == []


def test_add_and_get_message():
    """Test que agrega y recupera mensajes correctamente."""
    email = "test2@ejemplo.com"
    
    # Agregar mensaje de usuario
    add_message(email, "user", "Hola")
    
    # Agregar mensaje de asistente
    add_message(email, "assistant", "Hola, ¿en qué puedo ayudarte?")
    
    # Verificar historial
    history = get_conversation(email)
    assert len(history) == 2
    assert history[0]["role"] == "user"
    assert history[0]["content"] == "Hola"
    assert history[1]["role"] == "assistant"
    assert history[1]["content"] == "Hola, ¿en qué puedo ayudarte?"


def test_conversation_persistence():
    """Test que la conversación persiste entre llamadas."""
    email = "test3@ejemplo.com"
    
    add_message(email, "user", "Primer mensaje")
    history1 = get_conversation(email)
    
    add_message(email, "assistant", "Respuesta")
    history2 = get_conversation(email)
    
    assert len(history2) == len(history1) + 1
    assert history2[-1]["content"] == "Respuesta"


def test_multiple_conversations():
    """Test que diferentes emails tienen conversaciones separadas."""
    email1 = "cliente1@ejemplo.com"
    email2 = "cliente2@ejemplo.com"
    
    add_message(email1, "user", "Mensaje cliente 1")
    add_message(email2, "user", "Mensaje cliente 2")
    
    history1 = get_conversation(email1)
    history2 = get_conversation(email2)
    
    assert len(history1) == 1
    assert len(history2) == 1
    assert history1[0]["content"] == "Mensaje cliente 1"
    assert history2[0]["content"] == "Mensaje cliente 2"
