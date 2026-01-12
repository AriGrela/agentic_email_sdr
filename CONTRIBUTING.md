# Guía de Contribución

¡Gracias por tu interés en contribuir al Agentic Email SDR System!

## 🚀 Cómo Contribuir

### 1. Fork el Proyecto

Haz fork del repositorio en GitHub haciendo clic en el botón "Fork".

### 2. Clone tu Fork

```bash
git clone https://github.com/TU-USUARIO/agentic_email_sdr.git
cd agentic_email_sdr
```

### 3. Configurar el Remote Upstream

```bash
git remote add upstream https://github.com/AriGrela/agentic_email_sdr.git
```

### 4. Crear una Rama

```bash
git checkout -b feature/mi-nueva-feature
```

**Convenciones de nombres de ramas:**
- `feature/` - Para nuevas funcionalidades
- `fix/` - Para correcciones de bugs
- `docs/` - Para mejoras de documentación
- `refactor/` - Para refactorizaciones
- `test/` - Para agregar o mejorar tests

### 5. Hacer Cambios

- Sigue las convenciones de código existentes
- Agrega comentarios donde sea necesario
- Asegúrate de que el código funcione correctamente
- Agrega tests si es posible

### 6. Commit tus Cambios

```bash
git add .
git commit -m "feat: descripción clara de los cambios"
```

**Usa prefijos convencionales (Conventional Commits):**
- `feat:` - Nueva funcionalidad
- `fix:` - Corrección de bugs
- `docs:` - Cambios en documentación
- `refactor:` - Refactorización de código
- `test:` - Agregar o modificar tests
- `style:` - Cambios de formato (espacios, comas, etc.)
- `chore:` - Tareas de mantenimiento

**Ejemplos:**
```bash
git commit -m "feat: agregar soporte para nuevos intents"
git commit -m "fix: corregir error en clasificador de intenciones"
git commit -m "docs: actualizar README con ejemplos"
```

### 7. Sincronizar con Upstream

Antes de hacer push, asegúrate de tener la última versión:

```bash
git fetch upstream
git checkout main
git merge upstream/main
git checkout feature/mi-nueva-feature
git rebase main
```

### 8. Push y Pull Request

```bash
git push origin feature/mi-nueva-feature
```

Luego crea un Pull Request en GitHub:
1. Ve a tu fork en GitHub
2. Haz clic en "Compare & pull request"
3. Completa el template del PR
4. Espera la revisión

## 📋 Estándares de Código

### Type Hints

Usa type hints donde sea posible:

```python
def send_email(to: str, subject: str, content: str) -> Dict[str, any]:
    ...
```

### Funciones

- Mantén funciones pequeñas y enfocadas
- Una función = una responsabilidad
- Nombres descriptivos

### Logging

Agrega logging para debugging:

```python
import logging
logger = logging.getLogger(__name__)

logger.info("Mensaje informativo")
logger.error("Error ocurrido")
```

### Documentación

Documenta funciones complejas:

```python
def complex_function(param1: str, param2: int) -> dict:
    """
    Descripción clara de qué hace la función.
    
    Args:
        param1: Descripción del parámetro
        param2: Descripción del parámetro
    
    Returns:
        Descripción del retorno
    
    Raises:
        ExceptionType: Cuándo se lanza
    """
    ...
```

## 🧪 Testing

Antes de hacer un PR, asegúrate de:

### 1. Ejecutar Tests

```bash
# Todos los tests
pytest

# Con cobertura
pytest --cov=app tests/

# Tests específicos
pytest tests/test_intent_classifier.py
```

### 2. Probar Localmente

```bash
# Iniciar servidor
uvicorn app.main:app --reload

# En otra terminal, probar endpoints
python example_usage.py
```

### 3. Verificar Linting

```bash
# Si usas flake8 o similar
flake8 app/
```

## 📝 Template de Pull Request

Al crear un PR, incluye:

- **Descripción**: Qué cambiaste y por qué
- **Tipo de cambio**: Feature, Fix, Docs, etc.
- **Tests**: ¿Agregaste tests? ¿Pasaron todos?
- **Checklist**: 
  - [ ] Tests pasan
  - [ ] Documentación actualizada
  - [ ] Código sigue estándares
  - [ ] Sin errores de linting

## 🎯 Áreas donde Necesitamos Ayuda

- Más tests unitarios
- Mejoras en la documentación
- Nuevos agentes especializados
- Optimizaciones de performance
- Mejoras en el manejo de errores

## ❓ Preguntas

Si tienes dudas, puedes:
- Abrir un Issue
- Contactar al mantenedor

¡Gracias por contribuir! 🚀
