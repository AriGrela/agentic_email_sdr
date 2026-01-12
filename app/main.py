from fastapi import FastAPI, Form, HTTPException
from fastapi.responses import JSONResponse
from app.agents.sdr_agent import handle_reply
import logging

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

app = FastAPI(
    title="Agentic Email SDR System",
    description="Multi-agent email sales system with intent classification and dynamic handoffs",
    version="1.0.0"
)

logger = logging.getLogger(__name__)


@app.post("/inbound")
async def inbound_email(
    text: str = Form(None),
    from_email: str = Form(None),
    sender: str = Form(None),
    subject: str = Form(None)
):
    """
    Simulated inbound email webhook.
    In production, this endpoint would be triggered
    by an email provider (e.g. SendGrid Inbound Parse).
    
    Args:
        text: Contenido del email
        from_email: Email del remitente
        sender: Email del remitente (alternativo)
        subject: Asunto del email
    """
    try:
        email_body = text or ""
        email_from = from_email or sender or ""

        if not email_body:
            raise HTTPException(status_code=400, detail="Email body is required")
        
        if not email_from:
            raise HTTPException(status_code=400, detail="Sender email is required")

        result = handle_reply(email_body, email_from)

        return JSONResponse(content={
            "status": "ok",
            "agent": result.get("agent"),
            "intent": result.get("intent"),
            "email_sent": result.get("email_sent", False)
        })
    
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error procesando email entrante: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error interno: {str(e)}")


@app.get("/")
async def root():
    """Health check endpoint."""
    return {
        "status": "ok",
        "service": "Agentic Email SDR System",
        "version": "1.0.0"
    }


@app.get("/health")
async def health():
    """Health check endpoint."""
    return {"status": "healthy"}
