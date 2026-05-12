import os

from dotenv import load_dotenv
from datetime import datetime, timedelta
from jose import jwt
from jose.exceptions import JWTError

load_dotenv()

KEY = os.getenv("KEY")

ALGORITHM = os.getenv("ALGORITHM")

EXPIRE_MINUTES = int(
    os.getenv("TOKEN_EXPIRE")
)


def criar_token(data: dict) -> str:

    dados = data.copy()

    dados.update({
        "exp": datetime.utcnow() + timedelta(
            minutes=EXPIRE_MINUTES
        )
    })

    token = jwt.encode(
        dados,
        KEY,
        algorithm=ALGORITHM
    )

    return token


def validar_token(token: str):

    try:

        payload = jwt.decode(
            token,
            KEY,
            algorithms=[ALGORITHM]
        )

        return payload

    except JWTError:

        return None