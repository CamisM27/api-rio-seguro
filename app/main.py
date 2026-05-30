from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import (
    Base,
    engine
)

from app.models.usuario_model import Usuario
from app.models.teste_qualidade_model import RegistroTeste
from app.models.pontos_coleta_model import PontoColeta

from app.routes import (
    usuario_routes,
    relatorio_routes,
    registro_pescador_routes,
    pontos_coleta_routes,
    teste_qualidade_routes,
    auth_routes
)


app = FastAPI(

    title="API Rio Seguro",

    description="""
    API responsável pelo gerenciamento do sistema Rio Seguro.

    Funcionalidades:
    - Usuários
    - Testes de qualidade da água
    - Relatórios
    - Pontos de coleta
    - Registro de pescadores
    - Autenticação JWT
    """,

    version="1.0.0"
)


@app.on_event("startup")
def startup():

    Base.metadata.create_all(
        bind=engine
    )


app.add_middleware(

    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]
)


app.include_router (auth_routes.router)
app.include_router(usuario_routes.router)
app.include_router(relatorio_routes.router)
app.include_router(registro_pescador_routes.router)
app.include_router(pontos_coleta_routes.router)
app.include_router(teste_qualidade_routes.router)


@app.get("/")
def home():

    return {
        "mensagem":
        "API Rio Seguro funcionando"
    }


@app.get("/health")
def health_check():

    return {
        "status": "online"
    }