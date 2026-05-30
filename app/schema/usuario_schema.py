from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Optional


class UsuarioBase(BaseModel):

    nome: str
    data_nascimento: date
    telefone: Optional[str] = None
    email: EmailStr
    tipo_usuario: Optional[str] = None


class UsuarioCreate(
    UsuarioBase
):

    foto_perfil: Optional[bytes] = None


class UsuarioResponse(
    UsuarioBase
):

    id_usuario: int
    ativo: bool

    class Config:

        from_attributes = True