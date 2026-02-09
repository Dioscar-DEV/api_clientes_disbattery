# API de Clientes

API desarrollada con FastAPI que proporciona acceso a información de clientes desde un archivo CSV.

## Endpoints

- `GET /` - Mensaje de bienvenida
- `GET /clientes` - Retorna la lista completa de clientes en formato JSON

## Tecnologías

- Python 3.9
- FastAPI
- Pandas
- Uvicorn

## Instalación Local

```bash
pip install -r requirements.txt
```

## Ejecución Local

```bash
uvicorn main:app --reload
```

La API estará disponible en `http://localhost:8000`

## Documentación

Una vez ejecutada la API, accede a:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Deployment en Railway

Este proyecto está configurado para desplegarse automáticamente en Railway usando Docker.
