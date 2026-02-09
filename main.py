from fastapi import FastAPI
from fastapi.responses import FileResponse
import pandas as pd
import os

app = FastAPI()

# Define the path to the CSV file
CSV_PATH = os.path.join(os.path.dirname(__file__), "clientes.csv")

@app.get("/clientes")
async def get_clientes():
    """
    Reads the clientes.csv file and returns its content as a JSON response.
    """
    if not os.path.exists(CSV_PATH):
        return {"error": "El archivo de clientes no se encuentra."}
    
    df = pd.read_csv(CSV_PATH)
    return df.to_dict(orient="records")

@app.get("/")
def read_root():
    return {"message": "API de Clientes"}
