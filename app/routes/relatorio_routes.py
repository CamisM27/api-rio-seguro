from fastapi import APIRouter, Depends
from ..database import get_db
from app.auth.auth_dependency import (
    usuario_autenticado
)

router = APIRouter(prefix="/api/v1/relatorios", tags=["Relatórios"])

@router.get("/relatorio")
def emitir_relatorio_geral(db = Depends(get_db)):
    # Logica para cruzar dados de pescadores e pontos de coleta
    return {
        "mensagem": "Dados estatísticos consolidados"
    }

@router.get("/pescador/{id_pescador}")
def relatorio_por_pescador(id_pescador: int, db = Depends(get_db)):
    # Emitir relatorio por pescador
    return {
        "mensagem": f"Relatório de atividades do pescador {id_pescador}"
    }