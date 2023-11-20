from typing import Union
from fastapi import FastAPI
from generador import Generador
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.post("/GENERAR_CONTRASENA")
async def read_item(generador: Generador):
    return generador.generar()


