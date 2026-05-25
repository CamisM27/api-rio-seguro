from app.auth.jwt_handler import criar_token

from app.schema.auth_schema import (
    LoginRequest
)


def login_service(
    usuario: LoginRequest
):

    token = criar_token({

        "email": usuario.email
    })

    return {

        "access_token": token
    }