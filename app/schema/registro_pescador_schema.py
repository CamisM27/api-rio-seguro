from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class RegistroPescadorBase(BaseModel):

    data_registro: datetime

    cor_agua: str

    odor: bool

    chuva_ultimos_dias: bool

    chuva_24h: bool

    nome_local: str

    temperatura: str

    id_usuario: int


class RegistroPescadorCreate(
    RegistroPescadorBase
):
    pass


class RegistroPescadorResponse(
    RegistroPescadorBase
):

    id_registro: int

    class Config:
        from_attributes = True