from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schema.auth_schema import LoginRequest
from app.services.auth_service import login_service

router = APIRouter(
    prefix="/api/v1/auth",
    tags=["Auth"]
)


@router.post("/login")
def login(
    usuario: LoginRequest,
    db: Session = Depends(get_db)
):

    return login_service(
        db,
        usuario
    )