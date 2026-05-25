from fastapi import Header, HTTPException
from app.auth.jwt_handler import validar_token

def validar_usuario_logado(
    authorization: str = Header(None)
):

    if not authorization:

        raise HTTPException(
            status_code=401,
            detail="Token não enviado"
        )

    try:

        token = authorization.split(
            " "
        )[1]

    except IndexError:

        raise HTTPException(
            status_code=401,
            detail="Formato inválido"
        )

    payload = validar_token(
        token
    )

    if not payload:

        raise HTTPException(
            status_code=401,
            detail="Token inválido ou expirado"
        )

    return payload