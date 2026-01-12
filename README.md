# Agentic Email SDR System

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
git clone https://github.com/tu-usuario/agentic_email_sdr.git
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

### Respuesta del sistema

El sistema:
1. Clasifica la intención del mensaje
2. Delega al agente apropiado (PricingAgent si es "pricing", SDRAgent en otros casos)
3. Genera una respuesta usando OpenAI
4. Envía el email automáticamente
5. Guarda la conversación en memoria

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

Para probar el sistema localmente con ngrok:

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

- `POST /inbound` - Recibe emails entrantes (simulados)
- `GET /` - Health check básico
- `GET /health` - Health check detallado

### Ejemplo de respuesta

```json
{
  "status": "ok",
  "agent": "PricingAgent",
  "intent": "pricing",
  "email_sent": true
}
```
