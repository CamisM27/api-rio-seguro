from fastapi import APIRouter, Depends
from ..database import get_db
from app.auth.auth_dependency import (
    usuario_autenticado
)

router = APIRouter(
    prefix="/api/v1/pontos-coleta",
    tags=["Pontos de Coleta"]
)

@router.get("/")
def listar_pontos(db = Depends(get_db)):
    # Query para listar todos os pontos de coleta cadastrados
    return {
        "mensagem": "Retorna todos os pontos de coleta geográficos"
    }

@router.post("/")
def criar_ponto(ponto: dict, db = Depends(get_db)):
    # Logica para criar ponto
    return {
        "mensagem": "Novo ponto de coleta adicionado"
    }