from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class RegistroTesteBase(BaseModel):

    data_teste: datetime

    transparencia_agua: int

    espuma: str

    residuos_margem: str

    odor: str

    material_sedimentavel: str

    peixes: Optional[str] = None

    larvas_vermes_vermelhos: Optional[str] = None

    larvas_vermes_conchas: Optional[str] = None

    coliformes: Optional[int] = None

    oxigenio_od1: Optional[int] = None

    oxigenio_od5: Optional[int] = None

    potencial_hidrogenionico: Optional[int] = None

    nitrato: Optional[int] = None

    fosfatos: Optional[int] = None

    id_usuario: int

    id_ponto: int


class RegistroTesteCreate(
    RegistroTesteBase
):
    pass


class RegistroTesteResponse(
    RegistroTesteBase
):

    id_teste: int

    class Config:
        from_attributes = True