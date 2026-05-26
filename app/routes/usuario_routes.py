from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db

from app.schema.usuario_schema import (
    UsuarioCreate
)
from app.services.usuario_service import (
    listar_usuarios_service,
    criar_usuario_service,
    obter_usuario_por_id_service,
    desativar_usuario_service
)
from app.auth.auth_dependency import (
    usuario_autenticado
)

router = APIRouter(
    prefix="/api/v1/usuarios",
    tags=["Usuarios"]
)


@router.get("/")
def listar_usuarios(
    usuario=Depends(
        usuario_autenticado
    ),
    db: Session = Depends(get_db)
):
    usuarios = listar_usuarios_service(db)

    return {
        "mensagem": "Retorna lista de usuarios",
        "dados": usuarios
    }

@router.post("/")
def criar_usuario(
    usuario = Depends(
        usuario_autenticado
    ),
    db: Session = Depends(get_db)
):

    novo_usuario = criar_usuario_service(
        db,
        usuario
    )

    return {
        "mensagem": "usuario criado com sucesso",
        "dados": novo_usuario
    }

@router.get("/{id_usuario}")
def obter_usuario_por_id(
    id_usuario: int,
    db: Session = Depends(get_db),
    usuario = Depends(
        usuario_autenticado
    ),
):

    usuario = obter_usuario_por_id_service(
        db,
        id_usuario
    )

    return {
        "mensagem":
        f"Buscando usuario {id_usuario}",
        "dados": usuario
    }

@router.put(
    "/desativar/{id_usuario}"
)
def desativar_usuario(
    id_usuario: int,
    usuario=Depends(
        usuario_autenticado
    ),
    db=Depends(get_db)
):

    usuario_desativado = (
        desativar_usuario_service(
            db,
            id_usuario
        )
    )

    return {
        "mensagem":
        "Usuário desativado com sucesso",
        "dados":
        usuario_desativado
    }