from pydantic import BaseModel
from datetime import datetime


class RelatorioBase(BaseModel):

    data_relatorio: datetime

    id_usuario: int


class RelatorioCreate(RelatorioBase):
    pass


class RelatorioResponse(RelatorioBase):

    id_relatorio: int

    class Config:
        from_attributes = True