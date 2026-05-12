from fastapi import FastAPI

from app.database import Base, engine

# from app.routes.usuario_routes import router as usuario_router
# from app.routes.registro_pescador_routes import router as registro_router
# from app.routes.pontos_coleta_routes import router as ponto_router
# from app.routes.relatorio_routes import router as relatorio_router


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API Rio Seguro",
    version="1.0.0"
)


@app.get("/")
def home():

    return {
        "mensagem": "API funcionando"
    }


# app.include_router(usuario_router)
# app.include_router(registro_router)
# app.include_router(ponto_router)
# app.include_router(relatorio_router)