from fastapi import APIRouter, Depends, HTTPException
from ..database import get_db

router = APIRouter(prefix="/api/v1/usuarios", tags=["Usuarios"])

@router.get("/")
def listar_usuarios(db = Depends(get_db)):
    # Query do baco de dados para listar usuarios
    return {
        "mensagem": "Retorna lista de usuarios"
    }

@router.post("/")
def criar_usuario(usuario: dict, db = Depends(get_db)):
    # Logica para criar novos usuarios
    return {
        "mensagem": "usuario criado com sucesso",
        "dados": usuario
    }

@router.get("/{id_usuario}")
def obter_usuario_por_id(id_usuario: int, db = Depends(get_db)):
    return {
        "mensagem": f"Buscando usuario {id_usuario}"
    }