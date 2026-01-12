import os
from dotenv import load_dotenv
from typing import Optional

load_dotenv()

OPENAI_API_KEY: Optional[str] = os.getenv("OPENAI_API_KEY")
SENDGRID_API_KEY: Optional[str] = os.getenv("SENDGRID_API_KEY")
FROM_EMAIL: Optional[str] = os.getenv("FROM_EMAIL")

# Validar variables críticas al importar
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY no está configurada en las variables de entorno")

if not SENDGRID_API_KEY:
    raise ValueError("SENDGRID_API_KEY no está configurada en las variables de entorno")

if not FROM_EMAIL:
    raise ValueError("FROM_EMAIL no está configurada en las variables de entorno")
