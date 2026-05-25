from fastapi import APIRouter

from app.schema.auth_schema import (
    LoginRequest
)

from app.services.auth_service import (
    login_service
)

router = APIRouter(
    prefix="/api/v1/auth",
    tags=["Auth"]
)


@router.post("/login")
def login(
    usuario: LoginRequest
):

    return login_service(
        usuario
    )