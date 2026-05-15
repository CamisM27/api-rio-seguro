from fastapi import FastAPI

from app.database import Base, engine

from .routes import (
    usuario_routes,
    relatorio_routes,
    registro_pescador_routes,
    pontos_coleta_routes
)


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API Rio Seguro",
    version="1.0.0"
)

app.include_router(usuario_routes.router)
app.include_router(relatorio_routes.router)
app.include_router(registro_pescador_routes.router)
app.include_router(pontos_coleta_routes.router)


@app.get("/")
def home():

    return {
        "mensagem": "API funcionando"
    }
    