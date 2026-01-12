from app.agents.intent_classifier import classify_intent
from app.agents.pricing_agent import handle_pricing
from app.memory.conversation_store import get_conversation, add_message
from app.tools.sendgrid_tool import send_email
from openai import OpenAI
from app.core.config import OPENAI_API_KEY
import logging

logger = logging.getLogger(__name__)
client = OpenAI(api_key=OPENAI_API_KEY)


def handle_reply(email_text: str, sender_email: str) -> dict:
    """
    Procesa un email entrante, clasifica la intención y delega al agente apropiado.
    
    Args:
        email_text: Contenido del email recibido
        sender_email: Email del remitente
    
    Returns:
        Dict con información sobre la respuesta generada
    """
    try:
        logger.info(f"\n--- NUEVO MENSAJE ---")
        logger.info(f"From: {sender_email}")
        logger.info(f"Message: {email_text[:100]}...")  # Log truncado

        history = get_conversation(sender_email)

        intent = classify_intent(email_text)
        logger.info(f"[SDR] Intención detectada: {intent}")

        if intent == "pricing":
            logger.info("[SDR] Handoff → PricingAgent")
            result = handle_pricing(
                history + [{"role": "user", "content": email_text}]
            )
        else:
            logger.info("[SDR] Responde SDRAgent")
            result = default_sdr_response(email_text, history)

        answer = result["content"]
        responding_agent = result["agent"]

        logger.info(f"[RESPUESTA GENERADA POR] {responding_agent}")

        add_message(sender_email, "user", email_text)
        add_message(sender_email, "assistant", answer)

        email_result = send_email(
            to=sender_email,
            subject="Re: Seguimos en contacto",
            content=answer
        )

        return {
            "success": True,
            "agent": responding_agent,
            "intent": intent,
            "email_sent": email_result.get("success", False)
        }
    
    except Exception as e:
        logger.error(f"Error procesando respuesta: {str(e)}")
        raise


def default_sdr_response(email_text: str, history: list) -> dict:
    """
    Genera una respuesta usando el SDRAgent por defecto.
    
    Args:
        email_text: Contenido del email recibido
        history: Historial de conversación
    
    Returns:
        Dict con agent y content
    """
    prompt = """
Sos un SDR profesional de ACME Solutions.
Respondé de forma clara y profesional.
"""

    messages = [{"role": "system", "content": prompt}]
    messages.extend(history)
    messages.append({"role": "user", "content": email_text})

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )

        return {
            "agent": "SDRAgent",
            "content": response.choices[0].message.content
        }
    except Exception as e:
        logger.error(f"Error generando respuesta SDR: {str(e)}")
        raise
