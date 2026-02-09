from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, Response
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

        logger.info("Convirtiendo a JSON...")
        # Usar to_json de pandas que maneja NaN correctamente
        json_str = df.to_json(orient="records", force_ascii=False)

        # Devolver como Response con el JSON string
        return Response(content=json_str, media_type="application/json")

    except Exception as e:
        logger.error(f"Error al leer CSV: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error al procesar el archivo: {str(e)}")

@app.get("/")
def read_root():
    return {
        "message": "API de Clientes",
        "version": "1.0",
        "endpoints": {
            "/clientes": "Obtener todos los clientes (lento - 12k registros)",
            "/clientes/sede/{sede}": "Filtrar clientes por código de sucursal (1-16)",
            "/clientes/estado/{estado}": "Filtrar clientes por estado",
            "/sedes": "Listar todas las sucursales disponibles",
            "/stats": "Estadísticas del dataset"
        }
    }

@app.get("/sedes")
async def get_sedes():
    """
    Retorna la lista de sucursales únicas disponibles
    """
    try:
        df = pd.read_csv(CSV_PATH, encoding='utf-8', on_bad_lines='skip', engine='python')
        sedes = sorted(df['co_sucu_in'].dropna().unique().astype(int).tolist())
        return {
            "total": len(sedes),
            "sedes": sedes
        }
    except Exception as e:
        logger.error(f"Error al obtener sedes: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

@app.get("/clientes/sede/{sede}")
async def get_clientes_by_sede(sede: int):
    """
    Filtra clientes por código de sucursal
    """
    try:
        logger.info(f"Filtrando clientes por sede: {sede}")
        df = pd.read_csv(CSV_PATH, encoding='utf-8', on_bad_lines='skip', engine='python')

        # Filtrar por sucursal
        df_filtrado = df[df['co_sucu_in'] == sede]
        logger.info(f"Clientes encontrados: {len(df_filtrado)}")

        if len(df_filtrado) == 0:
            return {"message": f"No se encontraron clientes para la sede {sede}", "data": []}

        json_str = df_filtrado.to_json(orient="records", force_ascii=False)
        return Response(content=json_str, media_type="application/json")

    except Exception as e:
        logger.error(f"Error al filtrar por sede: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

@app.get("/clientes/estado/{estado}")
async def get_clientes_by_estado(estado: str):
    """
    Filtra clientes por estado
    """
    try:
        logger.info(f"Filtrando clientes por estado: {estado}")
        df = pd.read_csv(CSV_PATH, encoding='utf-8', on_bad_lines='skip', engine='python')

        # Filtrar por estado (case-insensitive)
        df_filtrado = df[df['estado'].str.contains(estado, case=False, na=False)]
        logger.info(f"Clientes encontrados: {len(df_filtrado)}")

        if len(df_filtrado) == 0:
            return {"message": f"No se encontraron clientes en {estado}", "data": []}

        json_str = df_filtrado.to_json(orient="records", force_ascii=False)
        return Response(content=json_str, media_type="application/json")

    except Exception as e:
        logger.error(f"Error al filtrar por estado: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

@app.get("/stats")
async def get_stats():
    """
    Retorna estadísticas del dataset
    """
    try:
        df = pd.read_csv(CSV_PATH, encoding='utf-8', on_bad_lines='skip', engine='python')

        return {
            "total_clientes": len(df),
            "sucursales": sorted(df['co_sucu_in'].dropna().unique().astype(int).tolist()),
            "estados": sorted(df['estado'].dropna().unique().tolist()),
            "ciudades_top_10": df['ciudad'].value_counts().head(10).to_dict(),
            "tipos_cliente": df['tip_cli'].value_counts().to_dict()
        }
    except Exception as e:
        logger.error(f"Error al obtener stats: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
