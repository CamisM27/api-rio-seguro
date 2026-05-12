from pydantic import BaseModel
from datetime import date
from typing import Optional
from pydantic import EmailStr


class UsuarioBase(BaseModel):
    nome: str
    data_nascimento: date
    telefone: Optional[str] = None
    email: Optional[EmailStr]
    tipo_usuario: Optional[str] = None


class UsuarioCreate(UsuarioBase):
    pass


class UsuarioResponse(UsuarioBase):
    id_usuario: int

    class Config:
        from_attributes = True