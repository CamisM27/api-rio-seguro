from pydantic import BaseModel
from datetime import date
from typing import Optional
from pydantic import EmailStr


class UsuarioBase(BaseModel):

    nome: str

    data_nascimento: date

    telefone: Optional[str] = None

    email: Optional[EmailStr] = None

    tipo_usuario: Optional[str] = None

    foto_perfil: Optional[bytes] = None
    
    ativo: Optional[bool] = True


class UsuarioCreate(UsuarioBase):
    pass


class UsuarioResponse(UsuarioBase):

    id_usuario: int

    class Config:
        from_attributes = True