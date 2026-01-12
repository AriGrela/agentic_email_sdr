# Agentic Email SDR System

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/github/license/AriGrela/agentic_email_sdr)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104%2B-green)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-orange)

Sistema multi-agente para SDR (Sales Development Representative) por email que clasifica intenciones, delega a agentes especializados y mantiene memoria conversacional.

## 🎯 Características

- **Clasificación de intención** automática (pricing, product_info, general_interest, not_interested)
- **Delegación dinámica** a agentes especializados (PricingAgent, SDRAgent)
- **Memoria conversacional** persistente por email
- **Respuestas automáticas** generadas con OpenAI
- **Arquitectura multi-agente** siguiendo principios de Agentic Engineering

## 🏗️ Arquitectura

```
┌─────────────┐
│   FastAPI   │ ← Webhook endpoint (/inbound)
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ Intent      │ ← Clasifica intención
│ Classifier  │
└──────┬──────┘
       │
       ├─── pricing ────► PricingAgent
       │
       └─── other ──────► SDRAgent
              │
              ▼
       ┌─────────────┐
       │ SendGrid    │ ← Envía respuesta
       └─────────────┘
```

## 🚀 Instalación

### Requisitos

- Python 3.8+
- Cuenta de OpenAI con API key
- Cuenta de SendGrid con API key

### Pasos

1. **Clonar el repositorio**
```bash
git clone https://github.com/AriGrela/agentic_email_sdr.git
cd agentic_email_sdr
```

2. **Crear entorno virtual**
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

4. **Configurar variables de entorno**

Crea un archivo `.env` en la raíz del proyecto:

```env
OPENAI_API_KEY=sk-tu-api-key-aqui
SENDGRID_API_KEY=SG.tu-api-key-aqui
FROM_EMAIL=tu-email@ejemplo.com
```

5. **Ejecutar el servidor**
```bash
uvicorn app.main:app --reload
```

El servidor estará disponible en `http://localhost:8000`

## 📖 Uso

### Endpoint de Webhook

Simula un email entrante enviando un POST a `/inbound`:

```bash
curl -X POST "http://localhost:8000/inbound" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "text=Hola, me interesa conocer los precios&from_email=cliente@ejemplo.com&subject=Consulta"
```

### Ejemplo con Python

```python
import requests

response = requests.post(
    "http://localhost:8000/inbound",
    data={
        "text": "¿Cuánto cuesta el plan básico?",
        "from_email": "cliente@ejemplo.com",
        "subject": "Consulta de precios"
    }
)

print(response.json())
```

### Ejemplo de Salida Real

Cuando envías un email, verás en la consola:

```
--- NUEVO MENSAJE ---
From: cliente@ejemplo.com
Message: ¿Cuánto cuesta el plan básico?
[SDR] Intención detectada: pricing
[SDR] Handoff → PricingAgent
[RESPUESTA GENERADA POR] PricingAgent
```

Y la respuesta JSON:

```json
{
  "status": "ok",
  "agent": "PricingAgent",
  "intent": "pricing",
  "email_sent": true
}
```

### Probar Diferentes Intents

**1. Pricing Intent:**
```bash
curl -X POST "http://localhost:8000/inbound" \
  -d "text=¿Cuánto cuesta?&from_email=cliente1@ejemplo.com"
```

**2. Product Info Intent:**
```bash
curl -X POST "http://localhost:8000/inbound" \
  -d "text=¿Qué características tiene el producto?&from_email=cliente2@ejemplo.com"
```

**3. General Interest:**
```bash
curl -X POST "http://localhost:8000/inbound" \
  -d "text=Hola, me interesa saber más&from_email=cliente3@ejemplo.com"
```

### Ver los Logs

El sistema usa logging estructurado. Para ver todos los logs en detalle:

```bash
# Los logs aparecen automáticamente en la consola cuando ejecutas:
uvicorn app.main:app --reload

# Para guardar logs en un archivo:
uvicorn app.main:app --reload 2>&1 | tee app.log
```

Los logs incluyen:
- Mensajes entrantes
- Intenciones detectadas
- Agente que responde
- Estado de envío de emails
- Errores (si ocurren)

### Flujo del Sistema

El sistema ejecuta automáticamente:
1. **Clasificación**: Detecta la intención del mensaje
2. **Delegación**: Enruta al agente apropiado (PricingAgent o SDRAgent)
3. **Generación**: Crea una respuesta contextual usando OpenAI
4. **Envío**: Envía el email automáticamente vía SendGrid
5. **Memoria**: Guarda la conversación para contexto futuro

## 🔧 Estructura del Proyecto

```
agentic_email_sdr/
├── app/
│   ├── agents/
│   │   ├── sdr_agent.py          # Agente principal SDR
│   │   ├── pricing_agent.py      # Agente especializado en precios
│   │   └── intent_classifier.py  # Clasificador de intenciones
│   ├── core/
│   │   └── config.py             # Configuración y variables de entorno
│   ├── memory/
│   │   └── conversation_store.py # Almacenamiento de conversaciones
│   ├── tools/
│   │   └── sendgrid_tool.py      # Herramienta de envío de emails
│   └── main.py                   # FastAPI app y endpoints
├── requirements.txt
├── README.md
└── .env                          # Variables de entorno (no commitear)
```

## 🧪 Testing

### Tests Unitarios

El proyecto incluye tests básicos para validar la funcionalidad:

```bash
# Ejecutar todos los tests
pytest

# Ejecutar tests con cobertura
pytest --cov=app tests/

# Ejecutar tests específicos
pytest tests/test_intent_classifier.py
```

### Testing Manual

**Opción 1: Usar el script de ejemplo**

```bash
python example_usage.py
```

Este script prueba automáticamente:
- Health check
- Intención de pricing
- Interés general
- Memoria conversacional

**Opción 2: Testing con curl**

```bash
# Test básico
curl -X POST "http://localhost:8000/inbound" \
  -d "text=Hola&from_email=test@ejemplo.com"

# Test de pricing
curl -X POST "http://localhost:8000/inbound" \
  -d "text=¿Cuánto cuesta?&from_email=test@ejemplo.com"
```

### Testing con ngrok (Webhooks Reales)

Para probar con webhooks reales de SendGrid:

1. **Iniciar el servidor**
```bash
uvicorn app.main:app --reload
```

2. **Exponer con ngrok** (opcional, para webhooks reales)
```bash
ngrok http 8000
```

3. **Configurar webhook en SendGrid** (opcional)
   - Settings → Inbound Parse
   - URL: `https://tu-dominio-ngrok.ngrok.io/inbound`

## 📝 Patrones Agénticos Implementados

- ✅ **Encapsulación de agentes**: Cada agente tiene responsabilidades claras
- ✅ **Abstracción de herramientas**: SendGrid como herramienta independiente
- ✅ **Delegación dinámica**: Handoff automático según intención
- ✅ **Memoria conversacional**: Historial persistente por email
- ✅ **Observabilidad**: Logging estructurado de decisiones
- ✅ **Diseño event-driven**: Respuesta a eventos de email

## 🛠️ Tecnologías

- **Python 3.8+**
- **FastAPI** - Framework web moderno y rápido
- **OpenAI API** - Generación de respuestas con GPT-4o-mini
- **SendGrid** - Envío de emails transaccionales
- **python-dotenv** - Manejo de variables de entorno

## 📄 Licencia

MIT License - Ver [LICENSE](LICENSE) para más detalles.

## 👤 Autor

**Ariel Sebastián Grela**  
Agentic Systems & Software Engineering

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:
1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📚 Documentación API

### Endpoints

#### `POST /inbound`

Recibe emails entrantes simulados y procesa la respuesta automática.

**Form Parameters:**

| Parámetro | Tipo | Requerido | Descripción | Ejemplo |
|-----------|------|-----------|-------------|---------|
| `text` | string | Sí | Contenido del email recibido | `"Hola, me interesa conocer los precios"` |
| `from_email` | string | Sí | Email del remitente | `"cliente@ejemplo.com"` |
| `sender` | string | No | Email del remitente (alternativo) | `"cliente@ejemplo.com"` |
| `subject` | string | No | Asunto del email | `"Consulta de precios"` |

**Response:**

```json
{
  "status": "ok",
  "agent": "PricingAgent",
  "intent": "pricing",
  "email_sent": true
}
```

**Campos de respuesta:**

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `status` | string | Estado de la operación (`"ok"` o error) |
| `agent` | string | Agente que generó la respuesta (`"PricingAgent"` o `"SDRAgent"`) |
| `intent` | string | Intención detectada (`"pricing"`, `"product_info"`, `"general_interest"`, `"not_interested"`) |
| `email_sent` | boolean | Indica si el email se envió correctamente |

**Códigos de estado HTTP:**

- `200 OK` - Email procesado correctamente
- `400 Bad Request` - Faltan parámetros requeridos
- `500 Internal Server Error` - Error interno del servidor

#### `GET /`

Health check básico del servicio.

**Response:**

```json
{
  "status": "ok",
  "service": "Agentic Email SDR System",
  "version": "1.0.0"
}
```

#### `GET /health`

Health check detallado del servicio.

**Response:**

```json
{
  "status": "healthy"
}
```

### Documentación Interactiva

FastAPI genera automáticamente documentación interactiva:

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`
