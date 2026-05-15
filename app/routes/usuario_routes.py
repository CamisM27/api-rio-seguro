from fastapi import APIRouter, Depends, HTTPException
import database

router = APIRouter(prefix="/api/v1/usuarios", tags=["Usuarios"])

@router.get("/")
def listar_usuarios(db = Depends(database)):
    # Query do baco de dados para listar usuarios
    return {
        "mensagem": "Retorna lista de usuarios"
    }

@router.post("/")
def criar_usuario(usuario: dict, db = Depends(database)):
    # Logica para criar novos usuarios
    return {
        "mensagem": "usuario criado com sucesso",
        "dados": usuario
    }

@router.get("/{id_usuario}")
def obter_usuario_por_id(id_usuario: int, db = Depends(database)):
    return {
        "mensagem": f"Buscando usuario {id_usuario}"
    }