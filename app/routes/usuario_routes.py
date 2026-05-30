from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi import UploadFile, File
from fastapi.responses import Response
from ..database import get_db

from app.schema.usuario_schema import (
    UsuarioCreate
)

from app.services.usuario_service import (
    listar_usuarios_service,
    criar_usuario_service,
    obter_usuario_por_id_service,
    desativar_usuario_service,
    atualizar_foto_usuario_service,
    visualizar_foto_usuario_service,
    reativar_usuario_service
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
    usuario_logado=Depends(
        usuario_autenticado
    ),
    db: Session = Depends(get_db)
):

    usuarios = listar_usuarios_service(
        db
    )

    return {
        "mensagem":
        "Retorna lista de usuarios",
        "dados":
        usuarios
    }


@router.post("/")
def criar_usuario(
    usuario_data: UsuarioCreate,
    db: Session = Depends(get_db)
):

    novo_usuario = criar_usuario_service(
        db,
        usuario_data
    )

    return {
        "mensagem": "usuario criado com sucesso",
        "dados": novo_usuario
    }


@router.get("/{id_usuario}")
def obter_usuario_por_id(
    id_usuario: int,
    usuario_logado=Depends(
        usuario_autenticado
    ),
    db: Session = Depends(get_db)
):

    usuario_encontrado = (
        obter_usuario_por_id_service(
            db,
            id_usuario
        )
    )

    return {
        "mensagem":
        f"Buscando usuario {id_usuario}",
        "dados":
        usuario_encontrado
    }


@router.put(
    "/desativar/{id_usuario}"
)
def desativar_usuario(
    id_usuario: int,
    usuario_logado=Depends(
        usuario_autenticado
    ),
    db: Session = Depends(get_db)
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
        "dados": usuario_desativado
    }
@router.put(
    "/reativar/{id_usuario}"
)
def reativar_usuario(
    id_usuario: int,
    usuario_logado=Depends(
        usuario_autenticado
    ),
    db: Session = Depends(get_db)
):

    usuario = reativar_usuario_service(
        db,
        id_usuario
    )

    return {
        "mensagem":
        "Usuário reativado com sucesso",
        "dados":
        usuario
    }
@router.put(
    "/foto/{id_usuario}"
)
async def atualizar_foto_usuario(
    id_usuario: int,
    foto: UploadFile = File(...),
    usuario_logado=Depends(
        usuario_autenticado
    ),
    db: Session = Depends(get_db)
):

    foto_atualizada = (
        await atualizar_foto_usuario_service(
            db,
            id_usuario,
            foto
        )
    )

    return {
        "mensagem":
        "Foto atualizada com sucesso",
        "dados":
        foto_atualizada
    }

@router.get(
    "/foto/{id_usuario}"
)
def visualizar_foto_usuario(
    id_usuario: int,
    usuario_logado=Depends(
        usuario_autenticado
    ),
    db: Session = Depends(get_db)
):

    return visualizar_foto_usuario_service(
        db,
        id_usuario
    )