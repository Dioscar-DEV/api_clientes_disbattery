from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, Response
import pandas as pd
import os
import logging
from mapeo_municipios import MAPEO_MUNICIPIOS

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Define the path to the CSV files
CSV_PATH = os.path.join(os.path.dirname(__file__), "clientes.csv")
CIUDADES_PATH = os.path.join(os.path.dirname(__file__), "ciudades_asignadas.csv")

def cargar_clientes_con_distribuidor():
    """
    Carga el CSV de clientes y hace merge con ciudades asignadas para obtener el distribuidor correcto
    Usa mapeo de fallback para municipios comunes que no están en el CSV
    """
    # Leer clientes
    df_clientes = pd.read_csv(
        CSV_PATH,
        encoding='utf-8',
        on_bad_lines='skip',
        engine='python',
        quoting=1,
        skipinitialspace=True
    )

    # Leer asignación de ciudades (tiene: ESTADO, CIUDAD, DISTRIBUIDOR, PARROQUIA, MUNICIPIO)
    df_ciudades = pd.read_csv(CIUDADES_PATH, encoding='utf-8')

    # En el CSV de clientes, la columna 'ciudad' en realidad contiene el MUNICIPIO
    # Normalizar para el merge
    df_clientes['municipio_norm'] = df_clientes['ciudad'].astype(str).str.strip().str.upper()
    df_ciudades['MUNICIPIO_norm'] = df_ciudades['MUNICIPIO'].astype(str).str.strip().str.upper()

    # Hacer merge por municipio
    df_merged = df_clientes.merge(
        df_ciudades[['MUNICIPIO_norm', 'DISTRIBUIDOR', 'CIUDAD', 'ESTADO']].rename(columns={
            'CIUDAD': 'ciudad_real',
            'ESTADO': 'estado_real'
        }),
        left_on='municipio_norm',
        right_on='MUNICIPIO_norm',
        how='left'
    )

    # FALLBACK: Asignar distribuidor usando mapeo manual para municipios sin match
    def asignar_distribuidor_fallback(row):
        if pd.isna(row['DISTRIBUIDOR']):
            municipio_upper = str(row['ciudad']).strip().upper()
            return MAPEO_MUNICIPIOS.get(municipio_upper, None)
        return row['DISTRIBUIDOR']

    df_merged['DISTRIBUIDOR'] = df_merged.apply(asignar_distribuidor_fallback, axis=1)

    # Limpiar columnas temporales
    df_merged = df_merged.drop(['municipio_norm', 'MUNICIPIO_norm'], axis=1)

    logger.info(f"Clientes con distribuidor: {df_merged['DISTRIBUIDOR'].notna().sum()}")
    logger.info(f"Clientes sin distribuidor: {df_merged['DISTRIBUIDOR'].isna().sum()}")

    return df_merged

@app.get("/clientes")
async def get_clientes():
    """
    Retorna TODOS los clientes con su distribuidor asignado (LENTO - ~12k registros)
    Recomendado: Usar filtros por distribuidor, ciudad o estado
    """
    try:
        logger.info(f"Obteniendo todos los clientes...")

        df = cargar_clientes_con_distribuidor()
        logger.info(f"Clientes cargados: {len(df)}")

        logger.info("Convirtiendo a JSON...")
        json_str = df.to_json(orient="records", force_ascii=False)

        return Response(content=json_str, media_type="application/json")

    except Exception as e:
        logger.error(f"Error al leer CSV: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error al procesar el archivo: {str(e)}")

@app.get("/")
def read_root():
    return {
        "message": "API de Clientes Disbattery",
        "version": "2.0",
        "total_clientes": "~12,000 registros",
        "endpoints": {
            "/clientes": "Obtener todos los clientes (lento - recomendado usar filtros)",
            "/distribuidores": "Listar todos los distribuidores/sedes disponibles",
            "/clientes/distribuidor/{nombre}": "Filtrar clientes por distribuidor",
            "/clientes/ciudad/{ciudad}": "Filtrar clientes por ciudad",
            "/clientes/estado/{estado}": "Filtrar clientes por estado",
            "/stats": "Estadísticas completas del dataset"
        }
    }

@app.get("/distribuidores")
async def get_distribuidores():
    """
    Retorna la lista de distribuidores/sedes disponibles con cantidad de clientes
    """
    try:
        df = cargar_clientes_con_distribuidor()

        # Contar clientes por distribuidor
        dist_counts = df['DISTRIBUIDOR'].value_counts()

        distribuidores_info = []
        for dist, count in dist_counts.items():
            if pd.notna(dist):  # Solo distribuidores asignados
                distribuidores_info.append({
                    "nombre": dist,
                    "total_clientes": int(count)
                })

        # Contar clientes sin distribuidor asignado
        sin_asignar = df['DISTRIBUIDOR'].isna().sum()

        return {
            "total_distribuidores": len(distribuidores_info),
            "distribuidores": sorted(distribuidores_info, key=lambda x: x['total_clientes'], reverse=True),
            "clientes_sin_asignar": int(sin_asignar)
        }
    except Exception as e:
        logger.error(f"Error al obtener distribuidores: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

@app.get("/clientes/distribuidor/{nombre}")
async def get_clientes_by_distribuidor(nombre: str):
    """
    Filtra clientes por distribuidor/sede
    Ejemplos:
    - "Disbattery"
    - "Oceano Pacifico"
    - "Blitz 2000"
    - "Grupo Disbattery"
    - "Grupo Victoria"
    """
    try:
        logger.info(f"Filtrando clientes por distribuidor: {nombre}")
        df = cargar_clientes_con_distribuidor()

        # Filtrar por distribuidor (case-insensitive y búsqueda parcial)
        df_filtrado = df[df['DISTRIBUIDOR'].str.contains(nombre, case=False, na=False)]
        logger.info(f"Clientes encontrados: {len(df_filtrado)}")

        if len(df_filtrado) == 0:
            return {
                "message": f"No se encontraron clientes para el distribuidor '{nombre}'",
                "sugerencia": "Usa /distribuidores para ver la lista completa",
                "data": []
            }

        # Eliminar columna DISTRIBUIDOR del resultado para reducir tamaño
        df_resultado = df_filtrado.drop('DISTRIBUIDOR', axis=1)
        json_str = df_resultado.to_json(orient="records", force_ascii=False)
        return Response(content=json_str, media_type="application/json")

    except Exception as e:
        logger.error(f"Error al filtrar por distribuidor: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

@app.get("/clientes/ciudad/{ciudad}")
async def get_clientes_by_ciudad(ciudad: str):
    """
    Filtra clientes por ciudad
    """
    try:
        logger.info(f"Filtrando clientes por ciudad: {ciudad}")
        df = cargar_clientes_con_distribuidor()

        # Filtrar por ciudad (case-insensitive)
        df_filtrado = df[df['ciudad'].str.contains(ciudad, case=False, na=False)]
        logger.info(f"Clientes encontrados: {len(df_filtrado)}")

        if len(df_filtrado) == 0:
            return {"message": f"No se encontraron clientes en {ciudad}", "data": []}

        json_str = df_filtrado.to_json(orient="records", force_ascii=False)
        return Response(content=json_str, media_type="application/json")

    except Exception as e:
        logger.error(f"Error al filtrar por ciudad: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

@app.get("/clientes/estado/{estado}")
async def get_clientes_by_estado(estado: str):
    """
    Filtra clientes por estado
    """
    try:
        logger.info(f"Filtrando clientes por estado: {estado}")
        df = cargar_clientes_con_distribuidor()

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
    Retorna estadísticas completas del dataset
    """
    try:
        df = cargar_clientes_con_distribuidor()

        # Distribución por distribuidor
        dist_stats = []
        for dist in df['DISTRIBUIDOR'].dropna().unique():
            datos_dist = df[df['DISTRIBUIDOR'] == dist]
            dist_stats.append({
                "nombre": dist,
                "clientes": len(datos_dist),
                "ciudades": datos_dist['ciudad'].nunique(),
                "estados": datos_dist['estado'].nunique()
            })

        return {
            "total_clientes": len(df),
            "clientes_asignados": df['DISTRIBUIDOR'].notna().sum(),
            "clientes_sin_asignar": df['DISTRIBUIDOR'].isna().sum(),
            "distribuidores": sorted(dist_stats, key=lambda x: x['clientes'], reverse=True),
            "ciudades_top_10": df['ciudad'].value_counts().head(10).to_dict(),
            "estados": sorted(df['estado'].dropna().unique().tolist()),
            "tipos_cliente": df['tip_cli'].value_counts().to_dict() if 'tip_cli' in df.columns else {}
        }
    except Exception as e:
        logger.error(f"Error al obtener stats: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
