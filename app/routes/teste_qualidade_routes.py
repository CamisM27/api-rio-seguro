from fastapi import APIRouter, Depends
from ..database import get_db

router = APIRouter(
    prefix="/api/v1/teste",
    tags=["Teste qualidade de água"]
)


@router.get("")
def listar_testes(id_usuario: int, db = Depends(get_db)):
    # Lista os testes da qualidade da água
    return {
        "mensagem": f"Retorna o teste de qualidade da água"
    }

@router.post("")
def criar_testes(id_usuario: int, db = Depends(get_db)):
    # Emitir teste da qualidade da água
    return {
        "mensagem": f"Cria o teste de qualidade da água"
    }

