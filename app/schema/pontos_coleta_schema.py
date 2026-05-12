from pydantic import BaseModel
from decimal import Decimal


class PontoColetaBase(BaseModel):

    nome: str

    descricao: str

    latitude: Decimal

    longitude: Decimal

    rio: str

    comunidade: str


class PontoColetaCreate(
    PontoColetaBase
):
    pass


class PontoColetaResponse(
    PontoColetaBase
):

    id_ponto: int

    class Config:
        from_attributes = True