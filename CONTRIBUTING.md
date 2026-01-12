# Guía de Contribución

¡Gracias por tu interés en contribuir al Agentic Email SDR System!

## Cómo Contribuir

### 1. Fork y Clone

```bash
git clone https://github.com/tu-usuario/agentic_email_sdr.git
cd agentic_email_sdr
```

### 2. Crear una Rama

```bash
git checkout -b feature/mi-nueva-feature
```

### 3. Hacer Cambios

- Sigue las convenciones de código existentes
- Agrega comentarios donde sea necesario
- Asegúrate de que el código funcione correctamente

### 4. Commit

```bash
git commit -m "feat: descripción clara de los cambios"
```

Usa prefijos convencionales:
- `feat:` para nuevas features
- `fix:` para correcciones de bugs
- `docs:` para documentación
- `refactor:` para refactorizaciones
- `test:` para tests

### 5. Push y Pull Request

```bash
git push origin feature/mi-nueva-feature
```

Luego crea un Pull Request en GitHub.

## Estándares de Código

- Usa type hints donde sea posible
- Mantén funciones pequeñas y enfocadas
- Agrega logging para debugging
- Documenta funciones complejas

## Testing

Antes de hacer un PR, asegúrate de:
- Probar localmente con `uvicorn app.main:app --reload`
- Verificar que no haya errores de linting
- Probar los endpoints con `example_usage.py`

¡Gracias por contribuir! 🚀
