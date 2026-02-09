from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
import pandas as pd
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Define the path to the CSV file
CSV_PATH = os.path.join(os.path.dirname(__file__), "clientes.csv")

@app.get("/clientes")
async def get_clientes():
    """
    Reads the clientes.csv file and returns its content as a JSON response.
    """
    try:
        logger.info(f"Intentando leer CSV desde: {CSV_PATH}")
        logger.info(f"Directorio actual: {os.getcwd()}")
        logger.info(f"Archivos en directorio: {os.listdir(os.path.dirname(__file__) or '.')}")

        if not os.path.exists(CSV_PATH):
            logger.error(f"CSV no encontrado en: {CSV_PATH}")
            raise HTTPException(status_code=404, detail="El archivo de clientes no se encuentra.")

        logger.info("CSV encontrado, leyendo...")
        # Leer CSV con manejo de errores tolerante
        df = pd.read_csv(
            CSV_PATH,
            encoding='utf-8',
            on_bad_lines='skip',  # Saltar líneas problemáticas
            engine='python',      # Motor más flexible
            quoting=1,            # QUOTE_ALL
            skipinitialspace=True
        )
        logger.info(f"CSV leído exitosamente. Filas: {len(df)}")

        # Reemplazar valores NaN, inf, -inf con None para JSON
        df = df.replace([float('inf'), float('-inf')], None)
        df = df.fillna(value=None)

        logger.info("Convirtiendo a JSON...")
        return df.to_dict(orient="records")

    except Exception as e:
        logger.error(f"Error al leer CSV: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error al procesar el archivo: {str(e)}")

@app.get("/")
def read_root():
    return {"message": "API de Clientes"}
