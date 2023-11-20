from typing import Union
from fastapi import FastAPI
from generador import Generador

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.post("/GENERAR_CONTRASENA")
async def read_item(generador: Generador):
    return generador.generar()


