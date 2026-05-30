from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.auth.jwt_handler import criar_token
from app.models.usuario_model import Usuario
from app.schema.auth_schema import LoginRequest


def login_service(
    db: Session,
    usuario: LoginRequest
):

    usuario_encontrado = db.query(
        Usuario
    ).filter(
        Usuario.email == usuario.email
    ).first()

    if not usuario_encontrado:

        raise HTTPException(
            status_code=404,
            detail="Usuário não encontrado"
        )

    if not usuario_encontrado.ativo:

        raise HTTPException(
            status_code=403,
            detail="Usuário desativado"
        )

    token = criar_token({

        "id_usuario":
        usuario_encontrado.id_usuario,

        "email":
        usuario_encontrado.email
    })

    return {
        "access_token": token
    }