"""
Ejemplo de uso del sistema Agentic Email SDR.

Este script muestra cómo simular emails entrantes
para probar el sistema localmente.
"""

import requests
import time

BASE_URL = "http://localhost:8000"


def test_pricing_intent():
    """Prueba con una intención de pricing."""
    print("\n🧪 Test 1: Intención de Pricing")
    print("-" * 50)
    
    response = requests.post(
        f"{BASE_URL}/inbound",
        data={
            "text": "Hola, me interesa conocer los precios de sus planes",
            "from_email": "cliente1@ejemplo.com",
            "subject": "Consulta de precios"
        }
    )
    
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    time.sleep(2)


def test_general_interest():
    """Prueba con interés general."""
    print("\n🧪 Test 2: Interés General")
    print("-" * 50)
    
    response = requests.post(
        f"{BASE_URL}/inbound",
        data={
            "text": "Hola, me gustaría saber más sobre su producto",
            "from_email": "cliente2@ejemplo.com",
            "subject": "Más información"
        }
    )
    
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    time.sleep(2)


def test_conversation_memory():
    """Prueba que la memoria conversacional funcione."""
    print("\n🧪 Test 3: Memoria Conversacional")
    print("-" * 50)
    
    email = "cliente3@ejemplo.com"
    
    # Primer mensaje
    print("Enviando primer mensaje...")
    response1 = requests.post(
        f"{BASE_URL}/inbound",
        data={
            "text": "Hola, tengo una pregunta",
            "from_email": email,
            "subject": "Primera consulta"
        }
    )
    print(f"Response 1: {response1.json()}")
    time.sleep(2)
    
    # Segundo mensaje (debería recordar el contexto)
    print("\nEnviando segundo mensaje...")
    response2 = requests.post(
        f"{BASE_URL}/inbound",
        data={
            "text": "Gracias por responder. ¿Podrías darme más detalles?",
            "from_email": email,
            "subject": "Re: Primera consulta"
        }
    )
    print(f"Response 2: {response2.json()}")


def test_health_check():
    """Prueba el health check."""
    print("\n🧪 Test 4: Health Check")
    print("-" * 50)
    
    response = requests.get(f"{BASE_URL}/health")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")


if __name__ == "__main__":
    print("=" * 50)
    print("🚀 Ejemplos de Uso - Agentic Email SDR")
    print("=" * 50)
    print("\n⚠️  Asegúrate de tener el servidor corriendo:")
    print("   uvicorn app.main:app --reload")
    print("\n" + "=" * 50)
    
    try:
        # Verificar que el servidor esté corriendo
        response = requests.get(f"{BASE_URL}/health", timeout=2)
        print("✅ Servidor detectado\n")
    except requests.exceptions.RequestException:
        print("❌ Error: No se puede conectar al servidor")
        print("   Por favor, inicia el servidor primero:")
        print("   uvicorn app.main:app --reload")
        exit(1)
    
    # Ejecutar tests
    test_health_check()
    test_pricing_intent()
    test_general_interest()
    test_conversation_memory()
    
    print("\n" + "=" * 50)
    print("✅ Tests completados")
    print("=" * 50)
