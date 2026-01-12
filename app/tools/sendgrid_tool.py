from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from typing import Dict
import logging
from app.core.config import SENDGRID_API_KEY, FROM_EMAIL

logger = logging.getLogger(__name__)


def send_email(to: str, subject: str, content: str) -> Dict[str, any]:
    """
    Envía un email usando SendGrid.
    
    Args:
        to: Email del destinatario
        subject: Asunto del email
        content: Contenido del email (texto plano)
    
    Returns:
        Dict con status_code y success
    
    Raises:
        Exception: Si hay error al enviar el email
    """
    try:
        if not SENDGRID_API_KEY or not FROM_EMAIL:
            raise ValueError("SENDGRID_API_KEY y FROM_EMAIL deben estar configurados")
        
        message = Mail(
            from_email=FROM_EMAIL,
            to_emails=to,
            subject=subject,
            plain_text_content=content
        )

        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        
        logger.info(f"Email enviado a {to} - Status: {response.status_code}")
        
        return {
            "success": response.status_code in [200, 201, 202],
            "status_code": response.status_code
        }
    
    except Exception as e:
        logger.error(f"Error al enviar email: {str(e)}")
        raise
